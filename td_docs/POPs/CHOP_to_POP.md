---
url: https://docs.derivative.ca/CHOP_to_POP
category: POPs
title: CHOP_to_POP
---

# CHOP to POP
## Summary

The CHOP to POP takes CHOP channels and lets you convert them to attributes of a POP. Each CHOP sample becomes one POP point.
You can manually list the CHOP channels you want to convert, and then list the names of the POP attributes you want create, matching channels to attributes one by one. Built-in attributes like `P`, `N`, `Color` and `Tex` are assumed to be their multi-component forms. Other channel names will be assumed to be converted to scalar float attributes.
Channel to attribute mapping can be done through sequential blocks which give you more control over the type of attribute you create, for example, an array of 5 integers.
Alternately, channels can be automatically converted to attributes based on a naming standard. Set the Channels Selection menu to Autoconvert Precise Names. This is the same channel naming standard that [POP to CHOP](https://docs.derivative.ca/POP_to_CHOP "POP to CHOP") produces when POP to CHOP's Name Format menu is set to Precise, which handles attributes that have `()` and `[]`:
  * the attribute name is the same including maintaining capital letters
  * components of a vector attribute have `_0 _1 _2` suffixed i.e. `Tex_0 Tex_1 Tex_2`
  * arrays are represented with a leading-following underscore - `MyArray_0_` and for vector arrays `MyVectorArray_0_1`.
  * The channel name optionally has a single character at the end to signify data type: `f` (float), `F` (double), `i` int, `I` double int, `u` unsigned, `U` double unsigned.

You can get the `P` position attribute from the CHOP, or you can create your own line for `P` with a start-end position that you specify.
The POP points can be connected as an open or closed linestrip, or be created as single-point primitives, or have no primitives.
You can override the number of points that it produces and CHOP to POP will optionally interpolate from samples of the input.
See also [POP to CHOP](https://docs.derivative.ca/POP_to_CHOP "POP to CHOP")
[choptoPOP_Class](https://docs.derivative.ca/ChoptoPOP_Class "ChoptoPOP Class")

## Parameters - CHOP to Page
- CHOP `chop` - The CHOP to convert to POP attributes.
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Line Strip `linestrip` -
  * Lines `lines` -

- Override Number of Points `overridenumpoints` - ⊞ - When on, overrides the number of points to create.
  * Override Number of Points `overridenumpoints` -
  * Number of Points `numpoints` - Sets the number of points when the automatic number of points is overriden.

- Interpolate `interpolate` - When on, the CHOP can be interpolated between samples. When off, the nearest sample is used. Only when the POP is set to a different number of points than samples.
- Specify Position `specifypos` - Enable mapping the samples to a points positions range.
- Start Position `startpos` - ⊞ - Start position for samples mapped to a points positions range.
  * Start Position `startposx` -
  * Start Position `startposy` -
  * Start Position `startposz` -

- End Position `endpos` - ⊞ - End position for samples mapped to a points positions range.
  * End Position `endposx` -
  * End Position `endposy` -
  * End Position `endposz` -

- Closed `closed` - The last vertex is connected to the first vertex.
- Channels Selection `chanssel` - ⊞ - Channels can be automatically converted to attributes based on a naming standard.
  * Specify Channels `spec` -
  * Autoconvert Precise Names with Type Suffix `precisenamessuffix` -
  * Autoconvert Precise Names `precisenames` -

- Channel Scope `chanscope` - Pattern of channel names to convert to attribute point values.
- Attribute Scope `attrscope` - ⊞ - A list of attributes to be created according to the channel scope.
  * P `P` -
  * P(0) `P(0)` -
  * P(1) `P(1)` -
  * P(2) `P(2)` -
  * Color `Color` -
  * Color(0) `Color(0)` -
  * Color(1) `Color(1)` -
  * Color(2) `Color(2)` -
  * Color(3) `Color(3)` -
  * N `N` -
  * N(0) `N(0)` -
  * N(1) `N(1)` -
  * N(2) `N(2)` -
  * Tex `Tex` -
  * Tex(0) `Tex(0)` -
  * Tex(1) `Tex(1)` -
  * Tex(2) `Tex(2)` -

- Attributes `attrs` - Attributes to create when matching channels are found in the CHOP.
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- Channel Scope `attr0chanscope` - Pattern of channel names to convert to attribute point values.
- New Attribute Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * New Attribute Name `attr0name` -
  * Custom Name `attr0customname` - The name of the new cutom attribute.

- Attribute Type `attr0type` - ⊞ - Determines the type.
  * Attribute Type `attr0type` -
  * Components `attr0numcomps` - The number of components in the new custom attribute.

- Default Value `attr0defaultval` - ⊞ - The value of the new custom attribute if it cannot be computed.
  * Default Value `attr0defaultval0` - Value of attribute there is no CHOP sample to convert to attribute value.
  * Default Value `attr0defaultval1` -
  * Default Value `attr0defaultval2` -
  * Default Value `attr0defaultval3` -

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
Extra Information for the CHOP to POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
