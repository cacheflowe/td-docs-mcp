---
url: https://docs.derivative.ca/Primitive_POP
category: POPs
title: Primitive_POP
---

# Primitive POP
## Summary

The Primitive POP lets you manually create primitives. Primitives are made from points, so it takes an optional input POP, from which you can delete its primitives and create new ones. Then you can add a set of new points manually using blocks of sequential parameters on the Points page.
Next on the Primitives page you create new triangles, quads, lines, line strips and point primitives. When Method is By Set, and Primitive Type is Triangles, every 3 points creates a triangle. When Method is By Pattern, the points are selected by [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching"), for example selecting Line Strip and pattern `[0-9]` creates a 10-point line strip.
On the Setup page the points can be given any new built-in or custom attributes.
On the Setup page you can remove the original primitives from the input POP by turning on turn on Delete Primitives + Keep Points.
On the Post page you can remove unused points in the result or turn them into point primitives.
When you create new primitives from the consolidated set of points, using sequential blocks you can create any combination of primitive types, and each primitive's vertices can be manually-specified or generated using numeric patterns.
See also [Point POP](https://docs.derivative.ca/Point_POP "Point POP") which is basically the Points page of the Primitive POP.
You can re-connect a set of existing points by connecting a POP to the input, turning on Delete Primitives and Keep Points, adding no new points, then creating new primitives on the Primitive page.
To create a Point primitive per point, on the Primitive page, change Type to Point.
[primitivePOP_Class](https://docs.derivative.ca/PrimitivePOP_Class "PrimitivePOP Class")

## Parameters - Setup Page
- Delete Primitives and Keep Points `keep` - Enable removal of input primitives while keeping points.
- Add Points `addpts` - Whether to add new points.
- Pre-Multiply RGB by Alpha `premultcolor` - Enable RGB values pre-multiplication with the Alpha.
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * Custom `custom` -
  * N `n` - N value when creating primitives by groups of N points or every N points.
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

- Default Value `attr0value` - ⊞ - Default values of the attribute components.
  * Default Value `attr0value0` - Attribute value(s).
  * Default Value `attr0value1` - Attribute value(s).
  * Default Value `attr0value2` - Attribute value(s).
  * Default Value `attr0value3` - Attribute value(s).

## Parameters - Points Page
- Point `pt` -
- Position `pt0pos` - ⊞ -
  * Position `pt0posx` -
  * Position `pt0posy` -
  * Position `pt0posz` -

## Parameters - Primitives Page
- Method `method` - ⊞ - How to create new primitives - specifying by ordering rules, or by using alphanumeric patterns like [0-5]
  * None `none` -
  * By Set `set` - Specifies the method to use to group points by sets.
  * By Pattern `pattern` -

- Primitives Type `setprimtype` - ⊞ - Primitive type to output from the set
  * None `none` -
  * Points `points` -
  * Lines `lines` -
  * Triangles `triangles` -
  * Quads `quads` -
  * Line Strip `linestrip` -
  * Closed Line Strip `closedlinestrip` -

- Set `set` - ⊞ -
  * All Points `all` -
  * Groups of N Points `group` -
  * Skip Every Nth Point `skip` -

- N `n` -
- Primitive `prim` - Start of Sequential Parameter Blocks for primitive creation.
- Type `prim0type` - ⊞ - Determines the type.
  * None `none` -
  * Points `points` -
  * Lines `lines` -
  * Triangles `triangles` -
  * Quads `quads` -
  * Line Strip `linestrip` -
  * Closed Line Strip `closedlinestrip` -

- Point Index Pattern `prim0pattern` - Index-matching pattern.

## Parameters - Post Page
- Unused Points `unusedpointsop` - ⊞ - Sets the operation to do with the points not used by primitives.
  * Do Nothing `donothing` -
  * Remove `remove` -
  * Turn into Point Prims `pointprims` -

- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Create POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
