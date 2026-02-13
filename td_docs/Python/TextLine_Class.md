---
url: https://docs.derivative.ca/TextLine_Class
category: Python
title: TextLine_Class
---

# TextLine Class
A line of text in the [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP") or [Text SOP](https://docs.derivative.ca/Text_SOP "Text SOP"), after it has been formatted. It is also used by the [Geo Text COMP](https://docs.derivative.ca/Geo_Text_COMP "Geo Text COMP") to return the position and glyphs for a block of text. Contains various members about the line such as it's text, position etc."

## Members
`glyph` → `int` **(Read Only)** :
The index of the glyph that represents this text line.

`fontIndex` → `int` **(Read Only)** :
The index of the font that the glyph belongs to. Glyphs are not interchangable between fonts.

`text` → `str` **(Read Only)** :
The text for this line.

`origin` → `tdu.Position` **(Read Only)** :
A tdu.Position object that gives the baseline origin of the line of text.

`lineWidth` → `float` **(Read Only)** :
The width of the format box of this line of text. This member is not used by the [Geo Text COMP](https://docs.derivative.ca/Geo_Text_COMP "Geo Text COMP").
## Methods
No operator specific methods.
