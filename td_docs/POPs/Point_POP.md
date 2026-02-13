---
url: https://docs.derivative.ca/Point_POP
category: POPs
title: Point_POP
---

# Point POP
## Summary

The Point POP is similar to the [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP") but it creates points only and has no inputs. It is suitable for creating single-point POPs that can act like Uniforms in a [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP") or [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP") when combining with other attributes. (Math Mix and Combine let you combine single-point POPs with multi-point POPs.)
It is useful for creating POPs with no `P` attribute, like for example, one `Color` attribute. it is useful for creating a simple point list for the [Field POP](https://docs.derivative.ca/Field_POP "Field POP") and [Force POP](https://docs.derivative.ca/Force_POP "Force POP") (one point per field or force).
Any attributes can be created on the Setup page, then you give each point values on the Points page.
For every point in the point list, it creates a Point Primitive in the primitive list (attach a [POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT") to confirm, and select the class Primitive). You can create point only with no primitives by turning off Create Point Primitives.
[pointPOP_Class](https://docs.derivative.ca/PointPOP_Class "PointPOP Class")

## Parameters - Setup Page
- Create P Attribute `createp` - Enable adding the position attribute
- Create Point Primitives `createpointprim` - Enable creating point primitives
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * Custom `custom` -
  * N `n` -
  * Color `color` -
  * Tex `tex` -
  * PointScale `pointscale` -
  * LineWidth `linewidth` -

- Custom Name `attr0customname` - The name of the new cutom attribute.
- Type `attr0type` - ⊞ - Determines the type.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * dir `dir` -
  * dbl dir `ddir` -

- Number of Components `attr0numcomps` - ⊞ - Number of components of the new attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

## Parameters - Points Page
- Point `pt` -
- Position `pt0pos` - ⊞ -
  * Position `pt0posx` -
  * Position `pt0posy` -
  * Position `pt0posz` -

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
Extra Information for the Point POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
