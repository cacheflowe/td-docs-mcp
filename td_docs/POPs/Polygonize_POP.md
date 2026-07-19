---
url: https://docs.derivative.ca/Polygonize_POP
category: POPs
title: Polygonize_POP
---

# Polygonize POP

## Summary

The Polygonize POP takes as input a TOP that is a 3D texture (see [Texture 3D TOP](../TOPs/Texture_3D_TOP.md "Texture 3D TOP")), or a POP that is arranged as a 3-dimensoinal grid of points (See [Dimension](../Glossary/Dimension.md "Dimension")) and creates a 3D polygonal surface that encloses pixels or points exceeding a specified threshold.

When the input is a 3D texture, it uses one of the 3D texture's RGBA channels or a combination of them (the Channel menu) to compare against the Threshold parameter. When the input is a POP, it uses a single value float attribute (or component of a vector attribute) to compare against the Threshold parameter.

It makes a closed polygonal surface that encloses all the points/pixels whose values are above the threshold. i.e. All the pixels/points inside the surface are above the threshold, and all pixels/points whose values are below the threshold are outside the surface. (A polygon passes through each pixel where the value is above the Threshold and a neighbor point's/pixels' value is less than the threshold.)

( An example of an input POP that is arranged as a 3-dimensoinal grid of points is a Grid POP with Slices > 1, passed to a Noise POP that creates a single-float Noise attribute whose vaues are between -1 and 1. The Polygonize POP's Threshold parameter would be around 0. )

The density of points in the output can be redued using the Resolution Multiplier parameter.

The surface at the borders of the volume are controlled with the Extend menu - the boundary can be closed or open.

When using a 3D texture, the pixels are assumed to be cubes and the output `P(0)` range is -.5 to .5. The output can be re-ranged using ReRange P parameters.

See also [Trace POP](https://docs.derivative.ca/Trace_POP "Trace POP").

[polygonizePOP_Class](Polygonize_POP_Class.md "PolygonizePOP Class")

Input Attribute Scope `inputattrscope` - When using a POP with dimension 3 as an input, the attribute scope to sample.

Use Position Attribute `posattrib` - When using a POP with dimension 3 as an input, whether to use the P attribute to position the surface.

## Parameters - Polygonize Page
- TOP `top` - TOP to use as image to polygonize.
- Channel `channel` - ⊞ - When using a TOP input, the color channel to sample.
  * Luminance `luminance` -
  * Red `red` -
  * Green `green` -
  * Blue `blue` -
  * Alpha `alpha` -
  * RGB Average `rgbaverage` -
  * RGBA Average `average` -
  * RGB Maximum `rgbmax` -
  * RGBA Maximum `max` -
- Resolution Multiplier `resmult` - Resolution multiplier to apply to the input.
- Inside `inside` - ⊞ - Whether values above the threshold or below or equal the threshold are considered inside. Determines the winding of triangles and subsequently the orientation of their normals.
  * <= (Signed Distance) `lteq` -
  * > (Density) `gt` -
- Threshold `threshold` - The threshold value is where the surface will be created.
- Extend `extend` - ⊞ - Sets the Extend mode when sampling the TOP.
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -
- Unique Points `uniquepoints` - Whether the points are shared between the triangles or unique to each triangle.
- ReRange P `rerangep` - Whether to re-range P.
- Map to Low `tolow` - ⊞ - The low value of the new range in XYZ.
  * Map to Low `tolow0` -
  * Map to Low `tolow1` -
  * Map to Low `tolow2` -
- Map to High `tohigh` - ⊞ - The high value of the new range in XYZ.
  * Map to High `tohigh0` -
  * Map to High `tohigh1` -
  * Map to High `tohigh2` -
- Normals Method `nmlmethod` - ⊞ - How to compute normals for the triangles.
  * No Normal `none` -
  * Field Gradient `gradient` -
  * From Surface `surface` -
- Step Multiplier `nmlstepmul` - When the method is Field Gradient, a multiplier on the size of the step used to calculate the gradient using neighboring field values.
- Texture Coordinates `texture` - Whether to output a point Texture Coordinates attribute (Tex).
- Fraction of Max Allocation `allocfract` - This POP doesn't know in advance how much GPU memory it will need, but except in rare cases (very high amount of detail, a lot of variation in neighboring voxels in the source) it doesn't need the maximum allocation. This allows to save GPU memory. If points and primitives are missing or the info popup shows the max numbers are reached, it means the fraction is too low.
- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels

Extra Information for the Polygonize POP can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

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
