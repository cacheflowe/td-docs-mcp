---
url: https://docs.derivative.ca/Unicode
category: Glossary
title: Unicode
---

# Unicode

[Unicode](https://en.wikipedia.org/wiki/Unicode) text is fully supported in TouchDesigner. Unicode can be typed into parameters, DATs, Python scripts etc. Unicode encoded text files can be loaded into DATs. File paths can include any Unicode character that is legal for a file path. The [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP") and [Text SOP](https://docs.derivative.ca/Text_SOP "Text SOP") can accept unicode characters directly. Fallback fonts will be used if a Unicode character can not be displayed in the currently selected font.

[Tscript](https://docs.derivative.ca/Tscript "Tscript") does _not_ support Unicode, so anything that goes through TScript will lose Unicode characters and result in incorrect script execution.

TouchDesigner saves out `.txt` and other file formats using UTF-8, although it should be able to load UTF-16 and UTF-32 files as well for compatibility.

Node names, channel names, parameter names, and SOP attributes are still limited to the basic alphanumeric character set.

###  Byte Order Marks

TouchDesigner looks for [Byte Order Marks](https://en.wikipedia.org/wiki/Byte_order_mark) at the start of .txt files to determine the encoding the file uses. Any UTF8/UTF16/UTF32 .txt file must have this mark to be properly interpreted. If the BOM is missing, it will assume the file is using CP1252 encoding, which was the previous encoding older versions of TouchDesigner used.

Unicode text is fully supported in TouchDesigner. Unicode can be typed into parameters, DATs, Python scripts etc. Unicode encoded text files can be loaded into DATs. File paths can include any unicode character that is legal for a file path.

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
