---
url: https://docs.derivative.ca/ListAttribute_Class
category: Python
title: ListAttribute_Class
---

# ListAttribute Class
The ListAttribute class describes an attribute defining a cell or set of cells in a [List Component](https://docs.derivative.ca/ListCOMP_Class "ListCOMP Class").

## Members
`text` → `str` :
Get or set contents.

`textColor` → `tuple[float, float, float, float]` :
Get or set text color. In the form of a tuple (r, g, b, a).

`textJustify` → `JustifyType` :
Get or set text justification. Value is one of: JustifyType.TOPLEFT, JustifyType.TOPCENTER, JustifyType.TOPRIGHT, JustifyType.CENTERLEFT, JustifyType.CENTER, JustifyType.CENTERRIGHT, JustifyType.BOTTOMLEFT, JustifyType.BOTTOMCENTER, JustifyType.BOTTOMRIGHT

`textOffsetX` → `float` :
Get or set horizontal text offset.

`textOffsetY` → `float` :
Get or set vertical text offset.

`wordWrap` → `bool` :
Get or set word wrapping.

`help` → `str` :
Get or set help string when rolling over the cell.

`bgColor` → `tuple[float, float, float, float]` :
Get or set background color. In the form of a tuple (r, g, b, a).

`fontFace` → `str` :
Get or set font face. Example 'verdana'.

`fontFile` → `str` :
Get or set font file. VFS embedded files supported as well.

`fontBold` → `bool` :
Get or set whether or not text is rendered in bold font.

`fontItalic` → `bool` :
Get or set whether or not text is rendered italicized.

`fontSizeX` → `float` :
Get or set font horizontal size.

`fontSizeY` → `float` :
Get or set font vertical size. If not specified, uses fontSizeX.

`sizeInPoints` → `bool` :
Get or set text size units. When True size is in points, when False it is in pixels.

`top` → `TOP` :
Get or set background image [TOP](https://docs.derivative.ca/TOP_Class "TOP Class").

`topFill` → `FillMode` :
Get or set background TOP fit. Values: FillMode.STRETCH, FillMode.HORIZONTAL, FillMode.VERTICAL, FillMode.BEST, FillMode.NATIVE, FillMode.OUTSIDE.

`topBorderInColor` → `tuple[float, float, float, float]` :
Get or set inside top color. In the form of a tuple (r, g, b, a).

`topBorderOutColor` → `tuple[float, float, float, float]` :
Get or set outside top color. In the form of a tuple (r, g, b, a).

`bottomBorderInColor` → `tuple[float, float, float, float]` :
Get or set inside bottom color. In the form of a tuple (r, g, b, a).

`bottomBorderOutColor` → `tuple[float, float, float, float]` :
Get or set outside bottom color. In the form of a tuple (r, g, b, a).

`leftBorderInColor` → `tuple[float, float, float, float]` :
Get or set inside left color. In the form of a tuple (r, g, b, a).

`leftBorderOutColor` → `tuple[float, float, float, float]` :
Get or set outside left color. In the form of a tuple (r, g, b, a).

`rightBorderInColor` → `tuple[float, float, float, float]` :
Get or set inside right color. In the form of a tuple (r, g, b, a).

`rightBorderOutColor` → `tuple[float, float, float, float]` :
Get or set outside right color. In the form of a tuple (r, g, b, a).

`colWidth` → `float` :
Get or set column width, expressed in pixels.

`colStretch` → `bool` :
Get or set column stretchiness. When True, colWidth specifies minimum width.

`rowHeight` → `float` :
Get or set row height, expressed in pixels.

`rowStretch` → `bool` :
Get or set row stretchiness. When True, rowWidth specifies minimum width.

`rowIndent` → `float` :
Get or set row indent, expressed in pixels.

`editable` → `bool` :
Get or set whether or not contents are editable. When True, contents can be edited by clicking on the cell.

`draggable` → `bool` :
Get or set whether or not cell is draggable.

`focus` → `bool` **(Read Only)** :
Returns True if the cell/row/column/table is currently being edited.

`radio` → `bool` **(Read Only)** :
Returns true if the mouse last selected the cell/row/column/table.

`rollover` → `bool` **(Read Only)** :
Returns true if the mouse is currently over the cell/row/column/table.

`select` → `bool` **(Read Only)** :
Returns true if the mouse is currently pressed over the cell/row/column/table.
## Methods
No operator specific methods.

Lets you embed files inside a `.tox[](https://docs.derivative.ca/.tox ".tox")` or `.toe[](https://docs.derivative.ca/.toe ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
