---
url: https://docs.derivative.ca/Line_Smooth_POP
category: POPs
title: Line_Smooth_POP
---

# Line Smooth POP
## Summary

The Line Smooth POP smooths line strips by blending the positions of adjacent points along a line strip.
It blends based on a choice of two methods: In the Smooth by Edge Distance method you give it a distance and it will find the points within that distance along the edge in both directions and blend them using either a Gaussian weighting or a Box weighting. With the Gaussian weighting, points farther from the computed point are given a lower weight. With a Box weighting, all points that are found along the adjacent edges up to the specified distance are give equal weight in computing the resulting point position.
In the second Smooth by Point Steps method you give a number of adjacent points in each direction to include in the smoothing calculation. In this method, points that are far from a given points may be included in the smoothing.
In the End Points Fixed option, it assures that the original end points of each line strip do not move.
In the Pre-Divide stage, it optionally adds more points by subdividing, similar to how the [Line Divide POP](https://docs.derivative.ca/Line_Divide_POP "Line Divide POP") adds new points, and it can add points based on the curvature of adjacent points.
**Per-point mapping of parameters** - The Line Smooth POP has a Map page, which allows every point to get a different value for Edge Distance and Point Step Filter Size parameters. In this mechanism, a separate attribute in the input contains values that override (or add to / multiply by) the parameter value. See [Mapping POP Attributes to Parameters](https://docs.derivative.ca/Mapping_POP_Attributes_to_Parameters "Mapping POP Attributes to Parameters").
See also [Line Divide POP](https://docs.derivative.ca/Line_Divide_POP "Line Divide POP"), [Line Resample POP](https://docs.derivative.ca/Line_Resample_POP "Line Resample POP")
[linesmoothPOP_Class](https://docs.derivative.ca/LinesmoothPOP_Class "LinesmoothPOP Class")

## Parameters - Line Smooth Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -

- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- Pre-Divide `prediv` - Enable preceding division
- Max Distance `maxdivdist` - Maximum Distance between Points
- Maximum Number of Vertices `maxverts` - Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory.
- Filter Method `filtermethod` - ⊞ - Determines the line smoothing method.
  * Smooth by Edge Distance `dist` -
  * Smooth by Point Steps `point` -

- Filter Type `filtertype` - ⊞ - Determines smoothing kernel type.
  * Gaussian `gaussian` -
  * Box `box` -

- Edge Distance `filterdist` - When Smoothing by Edge Distance, this is how far to look in each direction along the adjacent edges to contribute to a smoothed position value.
- Point Step Filter Size `filtersize` - Sets the number of points used by the smoothing kernel.
- Effect `effect` - Determines the amount of smoothing applied
- End Points Fixed `endpointsfixed` - Enable output of fixed endpoints
- Output Attribute Scope `outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `overrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attrtype` - ⊞ - The output attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * Color `color` -
  * Color (double) `dcolor` -
  * Direction `dir` -
  * Direction (double) `ddir` -

- Components `attrnumcomps` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `attrdefaultval` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `attrdefaultval0` - Default value(s) of the attribute.
  * Default Value `attrdefaultval1` - Default value(s) of the attribute.
  * Default Value `attrdefaultval2` - Default value(s) of the attribute.
  * Default Value `attrdefaultval3` - Default value(s) of the attribute.

## Parameters - Resample Page
- Resample Method `resamplemethod` - ⊞ - Line strip resample method.
  * None `none` -
  * Distance between Points `dist` -
  * By Curvature `curvature` -

- Min Distance `resamplemindist` - The minimum distance between points in the output line strips.
- Max Distance `resamplemaxdist` - Maximum Distance between Points
- Min Max Bias `resampleminmaxbias` - Bias of point creation - more near the minimum or more near the maximum distance.
- Max Tries for Binary Search `maxtries` - Max number of iterations for binary search when linearly resampling.

## Parameters - Map Page
- Mapping `map` - Start of Sequential Parameter Blocks for attribute-to-parameter mapping.
- OP `map0op` - Source OP for parameter mapping. The default of _in0 means the input POP.
- Element `map0element` - The attribute (or component of an attribute) that will be mapped to a parameter per-point.
- Parameter `map0parm` - ⊞ - Parameter on the current POP that will be mapped from the Element (the attribute).
  * filterdist (Edge Distance) `filterdist` -
  * filtersize (Point Step Filter Size) `filtersize` -

- Combine Operation `map0combineop` - ⊞ - Combine operation for attribute value with parameter value.
  * Set `set` -
  * Multiply `mult` -
  * Add `add` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Line Smooth POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
