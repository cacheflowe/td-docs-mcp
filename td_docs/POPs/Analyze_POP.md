---
url: https://docs.derivative.ca/Analyze_POP
category: POPs
title: Analyze_POP
---

# Analyze POP
## Summary

The Analyze POP analyzes any point, vertex or primitive attributes of a POP, and outputs a single point containing the resulting statistics. It typically computes an average, minimum or maximum values of any attribute.
Attach an Analyze POP to a [POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT") (and set its Transpose) to see what it comes up with.
If you select more than one attribute, or if you select all (*), it will append the attribute names of the input POP to all the output attribute names.
Tip: The results on the Analyze POP are a single point on the GPU. What you do with it next affects performance. The more you stay on the GPU the faster it will be. Pulling the results to the CPU and using them in parameters will be slower. You can get it to the CPU on the next frame (faster) by using a POP to CHOP but of course it's delayed. Or you can fully stay in the GPU’s POP world by passing the point as an input to other operators like to a Math Mix POP.
In the case of an attribute with multiple components, the analysis is per component. For example for `P`, `Min(0)` is the min X value, `Min(1)` is the min Y value. `indexMin(0)` is the index of the point with the min X value, `IndexMin(1)` is the index of the point with the min Y value.
It can optionaly output the sum and power of the samples of the input attribute.
As noted above it can output the index of the point (the point number) of the sample with the maximum or minimum value of the selected input attribute.
It is also possible to combine the components of a vector to a single component before performing the analysis, using the Combine Components menu.
**Note** : Palette: popViewer can show the ranges of all attributes.
See also: [Accumulate POP](https://docs.derivative.ca/Accumulate_POP "Accumulate POP"), [Histogram POP](https://docs.derivative.ca/Histogram_POP "Histogram POP")
[analyzePOP_Class](https://docs.derivative.ca/AnalyzePOP_Class "AnalyzePOP Class")

## Parameters - Analyze Page
- Attributes Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Number of Elements in Group `numgroupelements` - Output an attribute with the number of elements in the selected group.
- Input Attributes `inputattrs` - ⊞ - Input attributes.
  * * `*` -

- Append Attrib Names to Output `appendattrname` - Makes the output attribute names include the name of the input attributes that are being analyzed, for clarity.
- Combine Components `combine` - ⊞ - First perform an operation to combine all components of an attribute into one value, then analye the results.
  * Off `off` -
  * Add `add` -
  * Subtract `sub` -
  * Multiply `mul` -
  * Divide `div` -
  * Average `avg` - Sums the point valus and takes the average.
  * Minimum `min` - Calculate and output the minimum value for the input attribute(s).
  * Maximum `max` - Calculate and output the maximum value for the input attribute(s).
  * Length `len` -

- Average `avg` -
- Centroid `centroid` - Outputs the average of the minimum and maximum values of the attribute.
- Minimum `min` -
- Maximum `max` -
- Size `size` - Enable size computation on the input attribute by subtracting the minimum value from the maximum values.
- Index of Minimum `minindex` - Index of the element with the minimum value.
- Index of Maximum `maxindex` - Index of the element with the maximum value.
- Sum `sum` - Compute the sum of attribute or components of attribute.
- RMS Power `rmspower` - Enable discrete root-mean-square power computation.
- Num Points, Vertices, Primitives `numpointsvertsprims` - Output the number of points, vertices, and primitives, in attributes.
- Num Prims/Verts per Type `numprimsbatch` - Output the number of primitives and vertices per primitive type in attributes.
- Dimension `dimension` - Outputs the dimension sizes of this POP.
- P Attribute Values `pattrvals` - ⊞ - Choose which analyzed result to place in the P attribute.
  * Don't Create P Attribute `none` -
  * Input Attribute Average `avg` -
  * Input Attribute Centroid `centroid` -
  * Input Attribute Minimum `min` -
  * Input Attribute Maximum `max` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Analyze POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
