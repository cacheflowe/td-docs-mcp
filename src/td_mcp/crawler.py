"""
TouchDesigner Documentation Crawler

Scrapes documentation from docs.derivative.ca and saves as markdown files
with metadata headers for use by the TD-MCP server.
"""

import asyncio
import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

# Fix Windows console encoding issues before importing crawl4ai
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    # Disable rich's formatting to avoid Unicode issues on Windows console
    os.environ["NO_COLOR"] = "1"
    os.environ["FORCE_COLOR"] = "0"
    # Try to reconfigure stdout for UTF-8
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

import aiofiles

# Crawl4AI imports
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

# Base URL for TouchDesigner documentation
BASE_URL = "https://docs.derivative.ca"

# Category pages to crawl for operators
OPERATOR_CATEGORIES = {
    "TOPs": "/Category:TOPs",
    "CHOPs": "/Category:CHOPs",
    "DATs": "/Category:DATs",
    "SOPs": "/Category:SOPs",
	"POPs": "/Category:POPs",
    "MATs": "/Category:MATs",
    "COMPs": "/Category:COMPs",
}

# Python reference sections - use TouchDesigner_Python_Classes as primary source
PYTHON_SECTIONS = {
    "Python": "/TouchDesigner_Python_Classes",
}

# General wiki pages that appear in category link lists but aren't operators.
# These get saved to a "General" directory instead of per-category directories.
GENERAL_PAGE_FILENAMES = {
    "TouchDesigner_Glossary.md",
    "TouchDesigner_Python_Classes.md",
    "Tutorials.md",
    "Derivative_About.md",
    "Derivative_General_disclaimer.md",
    "Derivative_Privacy_policy.md",
    "Frequently_Asked_Questions.md",
    "Interoperability.md",
    "Learn_TouchDesigner.md",
    "Main_Page.md",
    "Release_Notes.md",
    "Python.md",
    "Operator.md",
}

# Rate limiting
REQUEST_DELAY = 0.5  # seconds between requests
RETRY_ATTEMPTS = 3
RETRY_BASE_DELAY = 5  # seconds, doubles each attempt


def sanitize_filename(name: str) -> str:
    """Convert a page title to a safe filename."""
    # Remove or replace problematic characters
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    return name


def extract_page_name(url: str) -> str:
    """Extract the page name from a docs.derivative.ca URL."""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    # Remove leading slash and get the page name
    if path.startswith("/"):
        path = path[1:]
    return path


async def get_links_from_category(crawler: AsyncWebCrawler, category_url: str) -> list[str]:
    """Extract all documentation links from a category page."""
    config = CrawlerRunConfig(
        wait_until="domcontentloaded",
    )

    result = await crawler.arun(url=category_url, config=config)

    if not result.success:
        print(f"  Failed to fetch category page: {category_url}")
        return []

    links = []
    # Parse internal links from the page
    # Category pages have links in the mw-category div
    if result.links:
        for link in result.links.get("internal", []):
            href = link.get("href", "")
            # Filter for actual doc pages, not categories or special pages
            if href and not any(skip in href for skip in [
                "Category:", "Special:", "File:", "Help:",
                "Template:", "User:", "Talk:", "index.php",
                "#", "action=edit"
            ]):
                # Make absolute URL
                full_url = urljoin(BASE_URL, href)
                if full_url.startswith(BASE_URL):
                    links.append(full_url)

    return list(set(links))  # Remove duplicates


def is_failed_content(markdown_content: str) -> bool:
    """Check if crawled content is an error page (403, etc.)."""
    stripped = markdown_content.strip()
    return (
        not stripped
        or stripped == "# 403 Forbidden"
        or stripped.startswith("403 Forbidden")
        or stripped == "# Access Denied"
    )


async def crawl_page(
    crawler: AsyncWebCrawler,
    url: str,
    output_dir: Path,
    category: str
) -> bool:
    """Crawl a single documentation page and save as markdown."""
    page_name = extract_page_name(url)
    filename = sanitize_filename(page_name) + ".md"

    # Redirect general/meta pages to the General directory
    if filename in GENERAL_PAGE_FILENAMES:
        output_dir = output_dir.parent / "General"
        output_dir.mkdir(parents=True, exist_ok=True)
        category = "General"

    output_path = output_dir / filename

    # Skip if already exists (resume capability)
    if output_path.exists():
        return True

    config = CrawlerRunConfig(
        wait_until="domcontentloaded",
    )

    # Retry loop with exponential backoff for rate-limited responses
    for attempt in range(RETRY_ATTEMPTS):
        result = await crawler.arun(url=url, config=config)

        if not result.success:
            if attempt < RETRY_ATTEMPTS - 1:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
                print(f" (fetch failed, retrying in {delay}s...)", end="")
                await asyncio.sleep(delay)
                continue
            print(f"    Failed: {page_name}")
            return False

        markdown_content = result.markdown or ""
        markdown_content = clean_markdown(markdown_content)

        if not is_failed_content(markdown_content):
            break  # Success — content looks valid

        if attempt < RETRY_ATTEMPTS - 1:
            delay = RETRY_BASE_DELAY * (2 ** attempt)
            print(f" (403/empty, retrying in {delay}s...)", end="")
            await asyncio.sleep(delay)
        else:
            print(f"    Failed after {RETRY_ATTEMPTS} attempts: {page_name}")
            return False

    # Add metadata header
    metadata = f"""---
url: {url}
category: {category}
title: {page_name}
---

"""

    full_content = metadata + markdown_content

    # Save to file
    async with aiofiles.open(output_path, 'w', encoding='utf-8') as f:
        await f.write(full_content)

    return True


def clean_markdown(content: str) -> str:
    """Clean up markdown content from wiki page."""
    lines = content.split('\n')
    cleaned_lines = []
    skip_section = False

    for line in lines:
        # Skip navigation/footer sections
        if any(marker in line.lower() for marker in [
            "navigation menu", "retrieved from", "categories:",
            "privacy policy", "about derivative"
        ]):
            skip_section = True
            continue

        # Reset skip on major headers
        if line.startswith('# ') and skip_section:
            skip_section = False

        if not skip_section:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines).strip()


async def crawl_category(
    crawler: AsyncWebCrawler,
    category_name: str,
    category_path: str,
    output_base: Path,
    limit: int | None = None
) -> int:
    """Crawl all pages in a category."""
    print(f"\nCrawling category: {category_name}")

    category_url = BASE_URL + category_path
    output_dir = output_base / category_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get all links from category page
    links = await get_links_from_category(crawler, category_url)

    if limit:
        links = links[:limit]

    print(f"  Found {len(links)} pages to crawl")

    success_count = 0
    for i, url in enumerate(links):
        page_name = extract_page_name(url)
        print(f"  [{i+1}/{len(links)}] {page_name}", end="")

        success = await crawl_page(crawler, url, output_dir, category_name)
        if success:
            success_count += 1
            print(" ✓")
        else:
            print(" ✗")

        # Rate limiting
        await asyncio.sleep(REQUEST_DELAY)

    return success_count


async def crawl_python_reference(
    crawler: AsyncWebCrawler,
    section_name: str,
    section_path: str,
    output_base: Path,
    limit: int | None = None
) -> int:
    """Crawl Python reference documentation."""
    print(f"\nCrawling Python reference: {section_name}")

    section_url = BASE_URL + section_path
    output_dir = output_base / section_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # First, crawl the main reference page
    await crawl_page(crawler, section_url, output_dir, section_name)

    # Get all links from the reference page
    links = await get_links_from_category(crawler, section_url)

    # Filter for Python-related pages (classes, modules, etc.)
    python_links = [
        link for link in links
        if "_Class" in link and "index.php" not in link
    ]

    if limit:
        python_links = python_links[:limit]

    print(f"  Found {len(python_links)} Python pages to crawl")

    success_count = 1  # Count the main page
    for i, url in enumerate(python_links):
        page_name = extract_page_name(url)
        print(f"  [{i+1}/{len(python_links)}] {page_name}", end="")

        success = await crawl_page(crawler, url, output_dir, section_name)
        if success:
            success_count += 1
            print(" ✓")
        else:
            print(" ✗")

        await asyncio.sleep(REQUEST_DELAY)

    return success_count


def extract_class_urls_from_docs(docs_dir: Path) -> list[tuple[str, str]]:
    """Scan saved operator markdown files for Python class page URLs.

    Looks through all .md files in operator category directories (TOPs, CHOPs,
    etc.) for links to *_Class pages on docs.derivative.ca.  Returns a
    deduplicated list of (url, category) tuples so each class file can be saved
    alongside the operator that references it.
    """
    operator_dirs = {"TOPs", "CHOPs", "DATs", "SOPs", "POPs", "MATs", "COMPs"}
    pattern = re.compile(r"https://docs\.derivative\.ca/(\w+_Class)")
    seen: set[str] = set()
    results: list[tuple[str, str]] = []

    for dir_name in operator_dirs:
        cat_dir = docs_dir / dir_name
        if not cat_dir.is_dir():
            continue
        for md_file in cat_dir.glob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8")
            except Exception:
                continue
            for match in pattern.finditer(text):
                url = match.group(0)
                if url not in seen:
                    seen.add(url)
                    results.append((url, dir_name))

    return results


async def crawl_operator_classes(
    crawler: AsyncWebCrawler,
    docs_dir: Path,
    limit: int | None = None,
) -> int:
    """Crawl operator-specific Python class pages discovered in saved docs.

    Each class file is saved into the same category directory as the operator
    that references it (e.g. BlurTOP_Class.md sits alongside Blur_TOP.md in
    TOPs/).
    """
    print("\nCrawling operator Python class pages")

    entries = extract_class_urls_from_docs(docs_dir)
    if limit:
        entries = entries[:limit]

    print(f"  Found {len(entries)} class URLs in operator docs")

    success_count = 0
    for i, (url, category) in enumerate(entries):
        page_name = extract_page_name(url)
        print(f"  [{i+1}/{len(entries)}] {page_name} -> {category}", end="")

        output_dir = docs_dir / category
        success = await crawl_page(crawler, url, output_dir, category)
        if success:
            success_count += 1
            print(" ✓")
        else:
            print(" ✗")

        await asyncio.sleep(REQUEST_DELAY)

    return success_count


def find_failed_files(output_dir: Path) -> list[tuple[Path, str, str]]:
    """Find markdown files that contain 403/error content.

    Returns list of (file_path, url, category) tuples.
    """
    failed = []
    for md_file in output_dir.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        # Extract metadata from frontmatter
        if not text.startswith("---"):
            continue

        # Check body after frontmatter
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue

        body = parts[2].strip()
        if is_failed_content(body):
            # Parse url and category from frontmatter
            url = ""
            category = ""
            for line in parts[1].strip().split("\n"):
                if line.startswith("url:"):
                    url = line[4:].strip()
                elif line.startswith("category:"):
                    category = line[9:].strip()
            if url and category:
                failed.append((md_file, url, category))

    return failed


async def retry_failed(output_dir: Path):
    """Find and re-crawl pages that previously returned 403/error content."""
    print("TouchDesigner Documentation Crawler - Retry Failed")
    print("=" * 40)

    failed = find_failed_files(output_dir)
    if not failed:
        print("No failed files found!")
        return

    print(f"Found {len(failed)} failed files to re-crawl\n")

    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
    )

    async with AsyncWebCrawler(config=browser_config, verbose=False) as crawler:
        success_count = 0
        for i, (file_path, url, category) in enumerate(failed):
            page_name = extract_page_name(url)
            print(f"  [{i+1}/{len(failed)}] {page_name}", end="")

            # Delete the failed file so crawl_page doesn't skip it
            file_path.unlink()

            category_dir = output_dir / category
            success = await crawl_page(crawler, url, category_dir, category)
            if success:
                success_count += 1
                print(" ✓")
            else:
                print(" ✗")

            await asyncio.sleep(REQUEST_DELAY)

        print("\n" + "=" * 40)
        print(f"Re-crawled {success_count}/{len(failed)} pages successfully")

        # Check if any still failed
        still_failed = find_failed_files(output_dir)
        if still_failed:
            print(f"\n{len(still_failed)} pages still failing:")
            for fp, url, _ in still_failed:
                print(f"  - {fp.name}")


async def run_crawler(
    output_dir: Path,
    categories: list[str] | None = None,
    limit: int | None = None,
    skip_classes: bool = False,
    classes_only: bool = False,
):
    """Main crawler entry point."""
    print("TouchDesigner Documentation Crawler")
    print("=" * 40)
    print(f"Output directory: {output_dir}")

    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
    )

    async with AsyncWebCrawler(config=browser_config, verbose=False) as crawler:
        total_pages = 0

        if not classes_only:
            # Crawl operator categories
            for cat_name, cat_path in OPERATOR_CATEGORIES.items():
                if categories is None or cat_name in categories:
                    count = await crawl_category(
                        crawler, cat_name, cat_path, output_dir, limit
                    )
                    total_pages += count

            # Crawl Python reference
            for section_name, section_path in PYTHON_SECTIONS.items():
                if categories is None or section_name in categories or "Python" in (categories or []):
                    count = await crawl_python_reference(
                        crawler, section_name, section_path, output_dir, limit
                    )
                    total_pages += count

        # Crawl operator-specific Python class pages found in saved docs
        if not skip_classes:
            count = await crawl_operator_classes(crawler, output_dir, limit)
            total_pages += count

        print("\n" + "=" * 40)
        print(f"Crawling complete! Total pages saved: {total_pages}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Crawl TouchDesigner documentation from docs.derivative.ca"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("td_docs"),
        help="Output directory for markdown files (default: td_docs)"
    )
    parser.add_argument(
        "-c", "--categories",
        nargs="+",
        choices=list(OPERATOR_CATEGORIES.keys()) + ["Python"],
        help="Specific categories to crawl (default: all)"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit pages per category (for testing)"
    )
    parser.add_argument(
        "--retry-failed",
        action="store_true",
        help="Re-crawl pages that previously returned 403/error content"
    )
    parser.add_argument(
        "--skip-classes",
        action="store_true",
        help="Skip crawling operator-specific Python class pages"
    )
    parser.add_argument(
        "--classes-only",
        action="store_true",
        help="Only crawl operator-specific Python class pages (skip stages 1 & 2)"
    )

    args = parser.parse_args()

    try:
        if args.retry_failed:
            asyncio.run(retry_failed(args.output))
        else:
            asyncio.run(run_crawler(
                args.output, args.categories, args.limit,
                args.skip_classes, args.classes_only,
            ))
    except KeyboardInterrupt:
        print("\nCrawling interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
