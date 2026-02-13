---
url: https://docs.derivative.ca/Line_Divide_POP
category: POPs
title: Line_Divide_POP
---

# Line Divide POP
## Summary

The Line Divide POP takes any set of line strips, and for each it generates a new line strip that is subdivided using various interpolation methods. The default is linear interpolation with 4 divisions between incoming points.
You can choose the Interpolation Method, the default being Linear interpolation, but you can also choose spline types like Cardinal, BSpline, Beziers and Quadratic. With the spline types, it can use incoming attributes (like those set in the [Line POP](https://docs.derivative.ca/Line_POP "Line POP")) that specify the spline properties like `Weight`, tangents (`TanIn` and `TanOut`), tangent constraints (`TanInConstraint`) and/or tension. It will also interpret an interpolation method per-point if a `SegMethod` attribute exists.
There are two stages of doing divisions, The first stage allows setting the total divisions for the line strip, or divisions per-segment, dividing by distance along the curves, or by curvature of the line strip. It interpolates all the attributes.
The second stage lets you further re-sample the line strip with one of three methods: Divisions per Line Strip, Distance between Points, or Points as Keyframes.
Points as Keyframes interpolates by treating one attribute as an independent variable (like `Time`, or `U`), like a `y = f(x)` mathematical function. (For example, if you have an attribute `Time` on the points, you can resample curves at equal steps of time, assuming you curves express values over time.)
NOTE: The Maximum Number of Vertices parameter is required because it is not known on the GPU how many points you will end up with, and the GPU needs to pre-allocate enough memory to do the job. Oherwise line strips will be truncated.
To add: distinguish the different beziers, explain `TanInConstraint`. `ControlPoint` attribute (laser)
See also [Line POP](https://docs.derivative.ca/Line_POP "Line POP"), [Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP"), [Point POP](https://docs.derivative.ca/Point_POP "Point POP"), [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP"), [Pattern POP](https://docs.derivative.ca/Pattern_POP "Pattern POP").
[linedividePOP_Class](https://docs.derivative.ca/LinedividePOP_Class "LinedividePOP Class")

## Parameters - Divide Page
- Divisions Method `divmethod` - ⊞ - The method to apply the divisions.
  * None `none` -
  * Divisions per Line Strip `linestrip` -
  * Divisions per Segment `segment` -
  * Distance between Points `dist` -
  * Distance by Curvature `curvature` -

- Divisions `divs` - The number of divisions.
- Min Distance `mindist` - The minimum distance between points in the output line strips.
- Max Distance `maxdist` - Divide the line so there are no two adjacent points farther apart than this distance - max distance between points.
- Min Max Bias `minmaxbias` - Bias of point creation - more near the minimum or more near the maximum distance.
- By Edge `byedge` - When dividing using the distance between points, whether to restart at each segment (edge).
- Add ControlPoint Attribute `addctrlpointattr` - Whether to output a ControlPoint attribute set to 1 for control points.
- Maximum Number of Vertices `maxverts` - Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory.

## Parameters - Interpolate Page
- Interpolation Method per Segment `interpmethodpersegment` - ⊞ - When toggle is on, it uses a separate interpolation method for each segment in the input line strips.
  * Interpolation Method per Segment `interpmethodpersegment` -
  * Segment Method Attribute `segmethodattr` - Attribute scope for the segment method index.

- Interpolation Method `interpmethod` - ⊞ - Method to use for interpolation.
  * Linear `linear` -
  * Cardinal (Interpolating) `cardinal` -
  * BSpline `bspline` -
  * Cubic Bezier With Tangents `cubicbeziertang` -
  * Cubic Bezier `cubicbezier` -
  * Quadratic Bezier `quadraticbezier` -

- Weight Attribute `useweight` - ⊞ - When on, the points will have a weight attribute affecting the tightness of the curve around the point.
  * Weight Attribute `useweight` -
  * Weight Attribute Name `weightattr` - Specifies the scope of the attribute that stores weight values

- In Tangent Attribute `usetanin` - ⊞ - When on, the points will have a attribute to be the tangent going into the point.
  * In Tangent Attribute `usetanin` -
  * In Tangent Attribute Name `taninattr` - Name of the incoming tangent attribute.

- Out Tangent Attribute `usetanout` - ⊞ - When on, the points will have a attribute to be the tangent going out of the point.
  * Out Tangent Attribute `usetanout` -
  * Out Tangent Attribute Name `tanoutattr` - Name of the output tangent attribute.

- In Tangent Constraint Attribute `usetaninconst` - ⊞ - When on, the points will have an attribute to be constraints of a curve at that point..
  * In Tangent Constraint Attribute `usetaninconst` -
  * In Tangent Constraint Attribute Name `taninconstattr` - Name of the in tangent constraint attribute.

- Clamped `clamped` - When using Cardinal or BSpline interpolation, whether to duplicate the start and end control points so the resulting curve start and end at the control points. Only has an effect on open line strips.
- Tension `tension` - Controls how tightly the cardinal line strip bends through the control points

## Parameters - Resample Page
- Post-Resample Method `resamplemethod` - ⊞ - Resampling method used after division.
  * None `none` -
  * Divisions per Line Strip `linestrip` -
  * Distance between Points `dist` -
  * Points as Keyframes `keyframes` -

- Divisions `resampledivs` - The number of divisions.
- Independant Variable Attribute `indvarattr` - Attribute to use as the independent variable.
- Independant Variable Step `indvarstep` - Step size to use for the independent variable, usually a fraction of the independent variable range.
- Maximum Number of Vertices `resamplemaxverts` - Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory.
- Max Tries for Binary Search `maxtries` - Max number of iterations for binary search when linearly resampling.
- Remove Unused Points `rmvunusedpts` - Removes unused points not referenced by primitives.
- Max Distance `resamplemaxdist` - Maximum Distance between Points
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Line Divide POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
