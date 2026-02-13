---
url: https://docs.derivative.ca/SOP_to_POP
category: POPs
title: SOP_to_POP
---

# SOP to POP
## Summary

The SOP to POP converts the SOP 3D geometry to POP geometry.
The attributes of the SOP point list are converted to point attributes, with `P` position converted to `P`, but `uv` renamed to `Tex`, and `Cd` (color in SOPs) renamed to `Color` in POPs, `width` to `LineWidth` and `pscale` to `PointScale`.
For primitives, the triangles and quads are converted intact as triangles and quads. Because POPs do not support polygons with 5 or more points, a menu lets you choose between creating line strips, converting to triangles, or ignoring these primitives.
Mesh primitives in SOPs are converted to a choice of quad, line strip or point primitives. It does not preserve the row/column [Dimension](https://docs.derivative.ca/Dimension "Dimension") but the [Dimension POP](https://docs.derivative.ca/Dimension_POP "Dimension POP") can be used to preserve that information.
SOP primitives like sphere are converted only as points in POPs. and the more rarely used SOP Bezier/NURBS primitives are also converted to points with no primitives.
The vertices of the primitives are converted to POP vertices intact, including all vertex attributes with the same `uv`, `Cd` and other renaming.
Primitive attributes are converted intact, again with `Cd` renamed as `Color`.
The attributes in POPs are 32-bit float to float4 attributes.
[soptoPOP_Class](https://docs.derivative.ca/SoptoPOP_Class "SoptoPOP Class")

## Parameters - SOP to Page
- SOP `sop` - Reference to a SOP that will have its geometry converted to POP geometry.
5+ Points Polygons `polygons` - ⊞ - Select what to do with 5+ points polygons.
  * Ignore `ignore` -
  * Triangulated `triangulated` -
  * Closed Line Strip `closedlinestrip` -

- Meshes `mesh` - ⊞ - Choose what to do with meshes in the input SOP.
  * Ignore `ignore` -
  * Convert to Quads `quads` -
  * Convert Rows to Line Strips `rows` -
  * Convert Columns to Line Strips `cols` -
  * Convert Rows and Columns to Line Strips `rowscols` -
  * Convert to Point Primitives `points` -

- Input Color Space `inputcolorspace` - ⊞ - Override / set the color space, or use the color space in the file, or assume default if there is none.
  * Automatic `automatic` -
  * sRGB `srgb` -
  * sRGB - Linear `srgblinear` -
  * Rec.601 (NTSC) `rec601ntsc` -
  * Rec.709 `rec709` -
  * Rec.2020 `rec2020` -
  * Rec.2020 ST2084PQ `rec2020st2084pq` -
  * Rec.2020 HLG `rec2020hlg` -
  * DCI-P3 `dcip3` -
  * DCI-P3 (D60) `dcip3d60` -
  * Display P3 (D65) `displayp3d65` -
  * Display P3 (D65) - Linear `displayp3d65linear` -
  * ACES2065-1 `aces2065-1` -
  * ACEScg `acescg` -
  * ACESproxy `acesproxy` -
  * Passthrough `passthrough` -

- Input Reference White `inputreferencewhite` - ⊞ - Color space to use for the incoming data.
  * Default For Color Space `default` -
  * Standard (SDR) `sdr` -
  * High (HDR) `hdr` -
  * UI `ui` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the SOP to POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
