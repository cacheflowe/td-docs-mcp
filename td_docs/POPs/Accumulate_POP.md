---
url: https://docs.derivative.ca/Accumulate_POP
category: POPs
title: Accumulate_POP
---

# Accumulate POP
## Summary

The Accumulate POP takes an attribute from the input, and creates a new attribute whose values in each point are the sum of the values in the input attribute of the previous points.
For example, if an input has 100 points, and an attribute called `Steps` contains the same number, say 3 for each point, then the output attribute `Scan` will contain 3, 6, and 9 for the first three points, and 300 for the last point. It is the running sum or "integral".
If you change Type to Exclusive Scan, it will not count the current point's value, so the `Scan` attribute will contain 0, 3, 6 up to 297 in the last point.
The Accumulate POP can work on a point, vertex or primitive attribute. If the input is a float3, the new attribute will be float3, etc.
You can check it all with a [POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT").
See also: [Analyze POP](https://docs.derivative.ca/Analyze_POP "Analyze POP"), [Histogram POP](https://docs.derivative.ca/Histogram_POP "Histogram POP")
[accumulatePOP_Class](https://docs.derivative.ca/AccumulatePOP_Class "AccumulatePOP Class")

## Parameters - Accumulate Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- Type `scantype` - ⊞ - The accumulated value for each point includes the current point's value, or does not include the current point's value.
  * Inclusive Scan `inclusive` -
  * Exclusive Scan `exclusive` -

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

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Accumulate POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
