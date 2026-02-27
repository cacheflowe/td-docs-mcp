---
url: https://docs.derivative.ca/Experimental:Text_POP
category: POPs
title: Text_POP
---

#  Text POP
## Summary

The Text POP creates geometry from any [TrueType](http://en.wikipedia.org/wiki/TrueType) or [OpenType](http://en.wikipedia.org/wiki/OpenType) font that is installed on the system, or any TrueType/OpenType font file on disk. [Unicode](https://docs.derivative.ca/Unicode "Unicode") is supported.
Text POP supports two connectivity modes Triangles, and Line Strips. Extrusion is enabled for Triangle mode.
Line Strips create a closed line strip for each polygon. When Bridge Holes is toggled, if a glyph has holes these polygons will be bridged together to form a single closed line strip.
**Process multiple strings transformed separately** : The Specification DAT and Specification CHOP allow for individual strings to be each positioned and styled independently in 3D. Each line in the specification OP is an indepedent text block with its own alignment.
Every row of the Spec DAT represents a "text block". Every Spec DAT contains a column named `text` which is the string that overrides the Text parameter.
Most columns override a Text POP parameter, such as `text`, `tx` and `fontsize`. Some column names noted below have no corresponding parameter.
The Spec CHOP can also specify values per block. When including a Spec CHOP the number of Spec CHOP samples needs to be the same number of rows as the Spec DAT following the first column header.
Parameters that can be overridden are `tx`, `ty`, `tz`, `rx`, `ry`, `rz`, `sx`, `sy`, `sz`, `px`, `py`, `pz`, `tracking`, `trackingx`, `trackingy`, `linespacing`, `wordwrap`, `wordwrapsize`, `fontsize`, `fontsizex`, `fontsizey`, `fontcolorr`, `fontcolorg`, `fontcolorb`, `fontcolora`, `text`, `alignx` and `aligny`.
`tracking` and `fontsize` are the same as `trackingx` and `fontsizex` respectively.
`text`, `alignx` and `aligny` can only be specified through the Table DAT.
To put newlines or tabs into the text string formatting, turn the Text parameter into expression mode and use `\n` and `\t` respectively. For example `'first\nsecond'` will put the two words on separate lines.
See also: [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP"), [Unicode](https://docs.derivative.ca/Unicode "Unicode").
[textPOP_Class](https://docs.derivative.ca/TextPOP_Class "TextPOP Class")

## Parameters - Text Page
- Font `font` - Select the font for the text from this drop down menu. All fonts are provided by the OS, any [TrueType](http://en.wikipedia.org/wiki/TrueType) font that is loaded into the OS can be used.
- Font File `fontfile` - Specify any TrueType or OpenType font file (`.ttf, .otf file`) to use for the text. When using a font file, the Font menu above is disabled.
- Typeface `typeface` - Select a specific typeface for the current font e.g. Bold, Regular, Italic, etc.
- Connectivity `connectivity` - ⊞ -
  * Triangles `triangles` -
  * Line Strips `linestrips` -

- Mode `mode` - ⊞ - Controls whether the contents are taken from the Text parameter or from a Specification DAT/CHOP.
  * Text `text` -
  * Specification DAT/CHOP `specdat` -

- Text `text` - The string of text to create as geometry. If newlines or tabs are desired, change this parameter to expression mode, and specify a Python string that includes `\n` or `\t` to signify newlines and tabs. E.g `'First Line\nSecond Line'`.
- Specification DAT `specdat` - A path to a [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") that is the source of the text data when in Specification mode. The table should have 2 or 3 columns labeled `tx`, `ty`, `tx` and `text` in its first row. Each row after that will display one line of text at the given x, y coordinates as measured from the bottom-left corner. x and y are measured in POP space units.
- Specification CHOP `specchop` - A path to a CHOP that can provide numerical data when in Specification mode. Channels named `tx`, `ty` or `tz` can be used to position the text data specified in the Specificaction DAT. Each data row in the DAT should have a corresponding sample in the CHOP.
- Font Size `fontsize` - ⊞ - Sets the font size. The font size defines the distance from the baseline to the top of the layout box for the given font. The default size of 1 of the default font is close to the vertical size of capital letters with no descenders.
  * Font Size `fontsizex` -
  * Font Size `fontsizey` -

- Keep Font Ratio `keepfontratio` - Ignores Y value in Font Size. Sets both X and Y size to Font Size X.
- Tracking `tracking` - ⊞ - The amount of space to add between letters in X and Y. Tracking is way of adding an arbitrary offset between letters. There already is a default offset associated with each font so the letters are flush against each other. The Tracking parameter this adds to that and allows for a Y offset.
  * Tracking `trackingx` -
  * Tracking `trackingy` -

- Line Spacing `linespacing` - Determines the amount of space between lines of text.
- Horizontal Align `alignx` - ⊞ - Determines how the text is positioned horizontally in the panel. For example, with left alignment, the text will be positioned against the left side of the panel plus any defined padding.
  * Left `left` -
  * Center `center` -
  * Right `right` -

- Vertical Align `aligny` - ⊞ - Determines how the text is positioned vertically inside the panel.
  * Bottom `bottom` -
  * Center `center` -
  * Top `top` -
  * Baseline `baseline` -

- Font Color `fontcolor` - ⊞ - The default color of the text.
  * Font Color `fontcolorr` -
  * Font Color `fontcolorg` -
  * Font Color `fontcolorb` -

- Font Alpha `fontalpha` - The blending value used to display the text. 1 is opaque while 0 is transparent.
- Scale Font to BBox Height `scalefonttobboxheight` - Scale the font’s vertical size so it’s based on the vertical bounding box of the font.
- Level of Detail `levelofdetail` - Controls the quality of the text's shape by adding/removing subdivisions to the geometry.
- Extrude `extrude` - Extrude each glyph. Only enabled when set to Triangles.
- Extrude Depth `extrudedepth` - Extrusion depth.
- Break Language `breaklang` - Language type hint to help format the glyphs correctly. This should be a abbreviation from the Text TOP/SOP Unicode Language Abbreviations table.
- Reading Direction `readingdirection` - ⊞ - Use to set whether the language reads Left to Right or Right to Left.
  * Left To Right `lefttoright` -
  * Right To Left `righttoleft` -

- Word Wrap `wordwrap` - When checked text is automatically line wrapped once it takes up the space set in Word Wrap Size parameter below.
- Word Wrap Size `wordwrapsize` - Determines the amount of 3D space used before the line wraps.
- Smart Punctuation `smartpunct` - Enables the use of smart punctuation. For example, pairs of quotes will be replaced with appropriate angled quotes, 3 periods will be replaced with an ellipses character and two hypens will become an em-dash.

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
  * Translate `tx` -
  * Translate `ty` -
  * Translate `tz` -

- Rotate `r` - ⊞ - These three fields rotate the geometry in the three axes.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Scale `s` - ⊞ - These three fields scale the geometry in the three axes.
  * Scale `sx` -
  * Scale `sy` -
  * Scale `sz` -

- Pivot `p` - ⊞ - The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.
For example, during a scaling operation, if the pivot point of an object is located at: `-1, -1, 0` and you wanted to scale the object by `0.5` (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.
- Parameter Color Space `parmcolorspace` - ⊞ - Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space.
  * sRGB `srgb` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.

  * sRGB - Linear `srgblinear` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.

  * Rec.601 (NTSC) `rec601ntsc` - [Rec.601](https://en.wikipedia.org/wiki/Rec._601) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.

  * Rec.709 `rec709` - [Rec.709](https://en.wikipedia.org/wiki/Rec._709) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.

  * Rec.2020 `rec2020` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.

  * DCI-P3 `dcip3` - [DCI-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.

  * DCI-P3 (D60) `dcip3d60` - [DCI-P3 "D60 sim"](https://en.wikipedia.org/wiki/DCI-P3) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.

  * Display-P3 (D65) `displayp3d65` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.

  * ACES2065-1 `aces2065-1` - [ACES 2065-1](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.

  * ACEScg `acescg` - [ACEScg](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.

  * Passthrough `passthrough` - When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.

- Parameter Reference White `parmreferencewhite` - ⊞ - When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space selected.

  * Use Parent Panel `useparent` - Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.

  * Standard (SDR) `sdr` - Will treat the Parameter Color Space as SDR for it's reference white value.

  * High (HDR) `hdr` - Will treat the Parameter Color Space as HDR for it's reference white value.

  * UI `ui` - Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## Info CHOP Channels
Extra Information for the Text POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
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
