---
url: https://docs.derivative.ca/Polygonize_POP
category: POPs
title: Polygonize_POP
---

# Polygonize POP
## Summary

The Polygonize POP is an incomplete POP which takes a TOP image, uses it red channel only, makes a 2-point line primitive wherever there is difference in brightness between neighboring pixels relative to a specified threshold between 0 and 1. It can also take a 3D texture in TOPs and convert it to a set of 3D triangles in POPs representing a surface at the black-to-white threshold in the 3D texture.
Its result looks like a trace made up of continuous many-point line strips, but they are actually all separate 1-pixel-length 2-point lines. This may have some use but the full linestrip and triangulated trace will be implemented in the future. Until then, continue to use the [Trace SOP](https://docs.derivative.ca/Trace_SOP "Trace SOP"), and to make it run faster, include it in an [Engine COMP](https://docs.derivative.ca/Engine_COMP "Engine COMP"). See the example in the Palette in the Techniques folder.
See also [Trace SOP](https://docs.derivative.ca/Trace_SOP "Trace SOP"), [Engine COMP](https://docs.derivative.ca/Engine_COMP "Engine COMP").
[polygonizePOP_Class](https://docs.derivative.ca/PolygonizePOP_Class "PolygonizePOP Class")

## Parameters - Polygonize Page
- TOP `top` - TOP to use as image to polygonize.
- Threshold `threshold` - Sets the minimum brightness difference between neighboring pixels required to generate new points.
- Invert `invert` - Invert the TOP pixel or voxel value.
- Extend `extend` - ⊞ - Sets the Extend mode when sampling the TOP.
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Fill 2D Surface `fill` - Enable the addition of lines for the TOP's contour.
- Shared Points `sharedpoints` - Enables shared points when polygonizing.
- Alt `alt` - For debugging, will be removed.
- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Polygonize POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
