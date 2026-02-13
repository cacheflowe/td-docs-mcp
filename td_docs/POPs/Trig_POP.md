---
url: https://docs.derivative.ca/Trig_POP
category: POPs
title: Trig_POP
---

# Trig POP
## Summary

The Trig POP is a simple operator that converts attributes that are angles into the trigonometry representation of angles (sine, cosine, tangent). Alternately, the Trig POP can convert from the sine, cosine, tangent representation back to angles using the asin, acos and atan functions. asin(x) can be thought of as "the angle whose sine value is x".
You can choose the units your angles are expressed in - degrees (360 per rotation), radians (2 * 3.14157 per rotation) or simply rotations (1 means 1 rotation)
For example if an attribute has a value of 30 (degrees) and the Operation is set to sin(A), the Trig POP will output .5 to a new attribute.
sinh, cosh and tanh are the hyperbolic functions.
This POP does the same thing as the sin, cos... , asin, acos ... functions in the [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP"), [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP"), [Math POP](https://docs.derivative.ca/Math_POP "Math POP"). where you can also choose the units of your angles.
sin and cos are true "functions" because for every value of angle A, there is one and only one value for sin(A). However asin(A) etc are not functions as values of A may have an infinite number or zero numbers of values for asin(A)).
The function atan2(A,B) requires that you provide two attribute values.
Note: the other trig functions not included are cot(x) is equal to 1/tan(x). sec(x) = 1/cos(x), and csc(x) = 1/sin(x).
See also [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP"), [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP")
[trigPOP_Class](https://docs.derivative.ca/TrigPOP_Class "TrigPOP Class")

## Parameters - Trigonometry Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Input Attribute Scope A `inputattrscopea` - Input attribute or attribute components for functions argument A.
- Input Attribute Scope B `inputattrscopeb` - Input attribute or attribute components for functions argument B.
- Operation `operation` - ⊞ - Selects the operation to perform.
  * None `none` -
  * cos(A) `cos` -
  * sin(A) `sin` -
  * tan(A) `tan` -
  * acos(A) `acos` -
  * asin(A) `asin` -
  * atan(A) `atan` -
  * atan2(A,B) `atan2` -
  * cosh(A) `cosh` -
  * sinh(A) `sinh` -
  * tanh(A) `tanh` -
  * None `none` -
  * cos(A) `cos` -
  * sin(A) `sin` -
  * tan(A) `tan` -
  * acos(A) `acos` -
  * asin(A) `asin` -
  * atan(A) `atan` -
  * atan2(A,B) `atan2` -
  * cosh(A) `cosh` -
  * sinh(A) `sinh` -
  * tanh(A) `tanh` -

- From Angle Units `fromunit` - ⊞ - Controls the angle unit when the selected operation takes an angle as argument.
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -

- To Angle Units `tounit` - ⊞ - Determines the angles units after the operation.
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -

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
Extra Information for the Trig POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
