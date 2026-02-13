---
url: https://docs.derivative.ca/Text_SOP
category: SOPs
title: Text_SOP
---

# Text SOP
## Summary

The Text SOP creates text geometry from any [TrueType](http://en.wikipedia.org/wiki/TrueType) or [OpenType](http://en.wikipedia.org/wiki/OpenType) font that is installed on the system, or any TrueType/OpenType font file on disk. [Unicode](https://docs.derivative.ca/Unicode "Unicode") is supported.
See also: [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP"), [Unicode](https://docs.derivative.ca/Unicode "Unicode").
[textSOP_Class](https://docs.derivative.ca/TextSOP_Class "TextSOP Class")

## Parameters - Text Page
- Font `font` - Select the font for the text from this drop down menu. All fonts are provided by the OS, any [TrueType](http://en.wikipedia.org/wiki/TrueType) font that is loaded into the OS can be used.
- Font File `fontfile` - Specify any TrueType or OpenType font file (`.ttf, .otf file`) to use for the text. When using a font file, the Font menu above is disabled.
- Bold `bold` - Displays the text in **bold**.
- Italic `italic` - Displays the text in _Italic_.
- Font Size X `fontsizex` - Sets the font size in X (horizontal). The font size defines the distance from the baseline to the top of the layout box for the given font. The default size of 1 of the default font is close to the vertical size of capital letters with no descenders.
- Font Size Y `fontsizey` - Sets the font size in Y (vertical).
- Keep Font Ratio `keepfontratio` - Ignores Y value in Font Size. Sets both X and Y size to Font Size X.
- Scale Font to BBox Height `scalefontobboxheight` - Scale the font’s vertical size so it’s based on the vertical bounding box of the font.
- Output `output` - ⊞ - Specify geometry output of Triangles, Closed Polygons or Open Polygons.
  * Triangles `triangles` - The output is a triangulated mesh suitable for shaded renders.
  * Closed Polygons (Filled Holes) `closedpolys` - The output is a set of separated closed outlines, suitable for [Laser CHOP](https://docs.derivative.ca/Laser_CHOP "Laser CHOP"), [Extrude SOP](https://docs.derivative.ca/Extrude_SOP "Extrude SOP"), etc. Append a [Hole SOP](https://docs.derivative.ca/Hole_SOP "Hole SOP") to preserve holes properly.
  * Open Polygons `openpolys` - The output is a set of separated open outlines, suitable for the [Laser CHOP](https://docs.derivative.ca/Laser_CHOP "Laser CHOP"), etc. Renders as a wireframe always.

- Level of Detail `levelofdetail` - Controls the quality of the text's shape by adding/removing subdivisions to the geometry.
- Language `language` - Language type hint to help format the glyphs correctly. This should be a abbreviation from the [Text TOP/SOP Unicode Language Abbreviations](https://docs.derivative.ca/Text_TOP/SOP_Unicode_Language_Abbreviations "Text TOP/SOP Unicode Language Abbreviations") table.
- Reading Direction `readingdirection` - ⊞ - Use to set whether the language reads Left to Right or Right to Left.
  * Left To Right `lefttoright` -
  * Right To Left `righttoleft` -

- Kerning `kerning` - ⊞ - The amount of space to add between letters in X and Y. Kerning is way of adding an arbitrary offset between letters. There already is a default offset associated with each font so the letters are flush against each other. The Kerning parameter this adds to that and allows for a Y offset.
  * `kerning1` -
  * `kerning2` -

- Line Spacing `linespacing` - Determines the amount of space between lines of text.
- Horizontal Align `alignx` - ⊞ - Sets the horizontal alignment.
  * In Reading Direction `reading` -
  * Left `left` - Left justifies the text.
  * Center `center` - Centers the text.
  * Right `right` - Right justifies the text.

- Word Wrap `wordwrap` - When checked text is automatically line wrapped once it takes up the space set in Word Wrap Size parameter below.
- Word Wrap Size `wordwrapsize` - Determines the amount of 3D space used before the line wraps.
- Text `text` - The string of text to create as geometry. If newlines or tabs are desired, the recommended way is to change this parameter to expression mode, and specify a Python string that includes \n or \t to signify newlines and tabs. E.g `'First Line\nSecond Line'`.
- Legacy Parsing `legacyparsing` - **Note, it's recommended to use a Python expression in the Text parameter instead of enabling legacy parsing, as this parsing can easily run into issues with more complex strings.** When enabled and if the Text parameter is in Constant Mode, \t and \n character sequences will be turned into tab and newline characters respectively. Otherwise the \t and \n sequences will be left as literal \ and t and \ and n.

## Parameters - Transform Page
- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the order of the rotations within the overall transform order.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - These three fields move the geometry in the three axes.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the geometry in the three axes.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - These three fields scale the geometry in the three axes.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.
For example, during a scaling operation, if the pivot point of an object is located at: `-1, -1, 0` and you wanted to scale the object by `0.5` (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left.
  * X `px` -
  * Y `py` -
  * Z `pz` -

## Info CHOP Channels
Extra Information for the Text SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

###
## Common Operator Info Channels
  * total_cooks - Number of times the operator has cooked since the process started.

  * cook_time - Duration of the last cook in milliseconds.

  * cook_frame - Frame number when this operator was last cooked relative to the component timeline.

  * cook_abs_frame - Frame number when this operator was last cooked relative to the absolute time.

  * cook_start_time - Time in milliseconds at which the operator started cooking in the frame it was cooked.

  * cook_end_time - Time in milliseconds at which the operator finished cooking in the frame it was cooked.

  * cooked_this_frame - 1 if operator was cooked this frame.

  * warnings - Number of warnings in this operator if any.

  * errors - Number of errors in this operator if any.
