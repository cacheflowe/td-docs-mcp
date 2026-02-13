---
url: https://docs.derivative.ca/Quantize_POP
category: POPs
title: Quantize_POP
---

# Quantize POP
## Summary

The Quantize POP takes any attribute of its input, quantizes the values to integers or any step size, or it converts values to logical 0 or 1 values, and then outputs the resuting values to the same attribute, any other existing attribute or a new attribute. It operates on either point, vertex or primitive [attributes](https://docs.derivative.ca/Attribute "Attribute").
It can round to the nearest step, or round down to the next lowest step, or round up to the next higher step. Alternately it can compare logically to any parameter-specified value and set the result to 0 or 1.
If you set Parameter Size to 3 and your attribute is a float3 like `P`, then for each component of `P` you can have separate quantizing parameters for each attribute component.
The attributes you specify can be any type, including float2, float3, float4, double, etc. You can cause the output parameter to be converted to integers.
When creating a new attribute, you simply put the new attribute name in Output Attribute Scope. The Quantize POP will determine what data type it will be, but you can override it with the >>> expansion parameters.
For Input Attribute Scope you can specify a subset of the components, like `P(0) P(1)` (same as `P.xy` in [swizzle](https://docs.derivative.ca/index.php?title=Swizzle&action=edit&redlink=1 "Swizzle \(page does not exist\)") notation)
[quantizePOP_Class](https://docs.derivative.ca/QuantizePOP_Class "QuantizePOP Class")

## Parameters - Quantize Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Quantize `quantize` - ⊞ - Convert values into a finite set of discrete levels.
  * Off `off` -
  * Floor `floor` -
  * Round `round` -
  * Ceiling `ceiling` -
  * > `gt` -
  * >= `gteq` -
  * == `eq` -
  * != `neq` -
  * <= `lteq` -
  * < `lt` -
  * Off `off` -
  * Floor `floor` -
  * Round `round` -
  * Ceiling `ceiling` -
  * > `gt` -
  * >= `gteq` -
  * == `eq` -
  * != `neq` -
  * <= `lteq` -
  * < `lt` -

- Value Step `quantstep` - Determines the step value used in quantization.
- Value Offset `quantoffset` - Determines the offset value used in quantization.
- Value Compare `quantcompare` - Sets the compare value for boolean quantize operations.
- Cast to `castto` - ⊞ - Allows to cast the output attribute to a different type if wanted.
  * Automatic `auto` -
  * Float `float` -
  * Int `int` -

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
Extra Information for the Quantize POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
