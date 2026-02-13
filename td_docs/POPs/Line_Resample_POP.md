---
url: https://docs.derivative.ca/Line_Resample_POP
category: POPs
title: Line_Resample_POP
---

# Line Resample POP
## Summary

The Line Resample POP will take a set of line strips, and for each one, resample the line strip in one of four methods: number of Divisions per Line Strip, a specified Distance between Points, point separation based on the curvature of the line strip at each of the original points (By Curvature), and lastly, dividing based on stepping uniformly along another attribute of the line strip (Points as Keyframes) using an "Independent Variable Attribute".
Using a `ControlPoint` attribute you can make the resampled curve pass through (include) the control points exactly.
Resampling By Curvature has two distance parameters - the Minimum Distance where the curvature is high, and the Maximum Distance where the curvature is low (straight sections). Min Max Bias will create more or less minimum-distance points.
Line Resample POP doe not change the shape of the lines, unlike [Line Smooth POP](https://docs.derivative.ca/Line_Smooth_POP "Line Smooth POP").
See also [Line Divide POP](https://docs.derivative.ca/Line_Divide_POP "Line Divide POP"), [Line Smooth POP](https://docs.derivative.ca/Line_Smooth_POP "Line Smooth POP").
[lineresamplePOP_Class](https://docs.derivative.ca/LineresamplePOP_Class "LineresamplePOP Class")

## Parameters - Resample Page
- Resample Method `resamplemethod` - ⊞ - Line strip resample method.
  * None `none` -
  * Divisions per Line Strip `linestrip` -
  * Distance between Points `dist` -
  * By Curvature `curvature` -
  * Points as Keyframes `keyframes` -

- Divisions `resampledivs` - The number of divisions.
- Min Distance `resamplemindist` - The minimum distance between points in the output line strips.
- Max Distance `resamplemaxdist` - Maximum Distance between Points
- Min Max Bias `resampleminmaxbias` - Bias of point creation - more near the minimum or more near the maximum distance.
- Control Points Attribute `usectrlpoints` - ⊞ - One attribute will contain 0 or 1 values in points to signify which ones are control points.
  * Control Points Attribute `usectrlpoints` -
  * Control Points Attribute Name `ctrlpointsattr` - Sets the attribute scope when outputting a control point attribute

- Independant Variable Attribute `indvarattr` - Attribute to use as the independent variable.
- Independant Variable Step `indvarstep` - Step size to use for the independent variable, usually a fraction of the independent variable range.
- Maximum Number of Vertices `maxverts` - Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory.
- Max Tries for Binary Search `maxtries` - Max number of iterations for binary search when linearly resampling.
- Remove Unused Points `rmvunusedpts` - Removes unused points not referenced by primitives.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Line Resample POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
