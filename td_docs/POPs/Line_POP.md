---
url: https://docs.derivative.ca/Line_POP
category: POPs
title: Line_POP
---

# Line POP
## Summary

The Line POP generates a line strip where you create a set of points using parameters, and then subdivide each segment using various interpolation methods. The default is two points with 20 divisions between them, linearly interpolated.
You add a point by creating a new sequential block on the Points page and specifying the position `P` using its parameters. But each point can have any set of attributes: On the Setup page, use New Attribute to define all the attributes you want for the points.
The points are automatically connected as a line strip. On Setup, you can choose the Interpolation Method for the Divisions page, the default being Linear interpolation, but also possible are splines including Cardinal, BSpline, Beziers and Quadratic. With the spline types, the Line POP adds extra parameters on the Point page for setting the spline weight, tangents and/or tension. You can also choose to have a different interpolation method per-point.
On the Setup page, the toggle Multiple Line Strips lets you break the points into separate line strips, thus a parameter is added to the Points' sequential block that lets you indicate where the line breaks are. Also points can be repeated, and line strips can be open or closed.
The Divisions page subdivides the line strips in two stages. The first stage allows setting the total divisions for the line strip, or the divisions per-segment, or lets you divide by distance along the curves. The second stage lets you further re-sample the line strip, adding or removing points.
If you want to output your pre-divided point list, then do some other operations on it with other POPs, and then divide using the [Line Divide POP](https://docs.derivative.ca/Line_Divide_POP "Line Divide POP"), you can output the line strip(s) of the Line POP with the necessary attributes to be used by the Line Divide POP to control the divisions, including the interpolation type (`SegMethod`, in integer form). `SegMethod` is 0 for Linear, 1 for Cardinal and so on following the order in the Interpolation Method menu. It will also output attributes for weight and tangents etc. Look at the mclick popup info box to see the attributes it outputs.
See also [Line Divide POP](https://docs.derivative.ca/Line_Divide_POP "Line Divide POP"), [Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP"), [Point POP](https://docs.derivative.ca/Point_POP "Point POP"), [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP"), [Pattern POP](https://docs.derivative.ca/Pattern_POP "Pattern POP").
[linePOP_Class](https://docs.derivative.ca/LinePOP_Class "LinePOP Class")

## Parameters - Setup Page
- Multiple Line Strips `multiplelinestrips` - Allows the creation of multiple line strips, adding a line break toggle per point.
- Interpolation Method per Segment `interpmethodpersegment` - When toggle is on, it uses a separate interpolation method for each segment in the input line strips.
- Interpolation Method `interpmethod` - ⊞ - Method to use for interpolation.
  * Linear `linear` -
  * Cardinal (Interpolating) `cardinal` -
  * BSpline `bspline` -
  * Cubic Bezier With Tangents `cubicbeziertang` -
  * Cubic Bezier `cubicbezier` -
  * Quadratic Bezier `quadraticbezier` -

- Tension `tension` - Controls how tightly the cardinal line strip bends through the control points
- Enable Weights `enableweights` - Enable specifying control points weigths
- Enable Tangents `enabletangent` - Enable specifying control points tangents
- Enable Point Repeat `enablepointrepeat` - Enable specifying repeated control points for B-Splines
- Closed `closed` - The last vertex is connected to the first vertex.
- Pre-Multiply RGB by Alpha `premultcolor` - Enable RGB values pre-multiplication with the Alpha.
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

- Position `pt1pos` - ⊞ -
  * Position `pt1posx` -
  * Position `pt1posy` -
  * Position `pt1posz` -

## Parameters - Divisions Page
- Output `output` - ⊞ - Whether to output the control points or the subdivided line(s)
  * Subdivided Lines `subdivlines` -
  * Control Points `ctrlpoints` -

- Divisions Method `divmethod` - ⊞ - The method to apply the divisions.
  * Divisions per Line Strip `linestrip` -
  * Divisions per Segment `segment` -
  * Divisions Defined per Segment `defpersegment` -
  * Distance between Points (per Segment) `distseg` -

- Divisions `divs` - The number of divisions.
- Distance `dist` - Distance between points when post-resampling by distance.
- Add ControlPoint Attribute `addctrlpointattr` - Whether to the output control points with attributes or subdivided line strips.
- Post-Resample Method `resamplemethod` - ⊞ - Resampling method used after division.
  * None `none` -
  * Divisions per Line Strip `linestrip` -
  * Distance between Points `dist` -
  * Points as Keyframes `keyframes` -

- Divisions `resampledivs` - The number of divisions.
- Distance `resampledist` - Sets the maximum distance when resampling by distance between points
- Independant Variable Attribute `indvarattr` - ⊞ - Attribute to use as the independent variable.
  * P(0) `P(0)` -

- Independant Variable Step `indvarstep` - Step size to use for the independent variable, usually a fraction of the independent variable range.
- Maximum Number of Vertices `resamplemaxverts` - Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory.
- Max Tries for Binary Search `maxtries` - Max number of iterations for binary search when linearly resampling.

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

## Info CHOP Channels
Extra Information for the Line POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
