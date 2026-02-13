---
url: https://docs.derivative.ca/Twist_POP
category: POPs
title: Twist_POP
---

# Twist POP
## Summary

The Twist POP performs non-linear deformations on points such as Twist, Bend, Shear, Taper, Linear Taper, and Squash & Stretch.
You set up one or two axes (X, Y or Z) and a pivot point to determine the direction and center of deformation. The amount of deformation is set by the Strength parameter, and the rolloff away from the pivot point and/or axes is affected by the Rolloff parameter.
The amount of deformation can also be increased or decreased using a Weight attribute, which multiplies the Strength per-point.
You can deform any point, vertex or primitive attribute.
[twistPOP_Class](https://docs.derivative.ca/TwistPOP_Class "TwistPOP Class")

## Parameters - Twist Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- Weight Attribute `weightattr` - Specifies the scope of the attribute that stores weight values
- Operation `op` - ⊞ - Selects the operation to perform.
  * Twist `twist` -
  * Bend `bend` -
  * Shear `shear` -
  * Taper `taper` -
  * Linear Taper `ltaper` -
  * Squash & Stretch `squash` -

- Primary Axis `paxis` - ⊞ - Primary transform axis of the twist.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Secondary Axis `saxis` - ⊞ - Secondary transform axis.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Pivot `p` - ⊞ - The pivot point for the transform rotates and scales.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

- Strength `strength` - Sets the transform operation strength.
- Rolloff `rolloff` - Rolloff factor on the twist operation.
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
Extra Information for the Twist POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
