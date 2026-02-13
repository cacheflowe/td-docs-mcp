---
url: https://docs.derivative.ca/Limit_POP
category: POPs
title: Limit_POP
---

# Limit POP
## Summary

The Limit POP takes any attribute and lets you clamp to a lower-upper range, or takes values outside the range and loops them so they are withing the range, or similarly zig-zags the values within the range. You can limit the maximum-only, or the minimum-only.
If the attribute is multi-component (like Color which has 4 components), then by default all components have the limits applied in the same way. But if you change Parameter Size to, say, 3, then there are a set of parameters for each color component. So R, G and B can have different Limit Types and different minimum and maximum ranges.
Some of these capabilities are possible in the [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP") and [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP") using the min(A), max(A), loop(), zigzag() and clamp() functions.
Values can then be made all positive, and then the final values can be cast to integer attributes (integer, unsigned integer).
**Tip** : If you want to only work with red and blue color components, set Unput Attribute Scope to `Color(0) Color(2)`, or `Color.rb` and set Parameter Size to 2 for independent control.
See also [Quantize POP](https://docs.derivative.ca/Quantize_POP "Quantize POP"), [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP"), [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP")
[limitPOP_Class](https://docs.derivative.ca/LimitPOP_Class "LimitPOP Class")

## Parameters - Limit Page
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

- Limit Type Minimum `mintype` - ⊞ - The wrapping method used when applying limits to the input elements attribute.
  * Off `off` -
  * Clamp `clamp` -
  * Loop `loop` -
  * Zig Zag `zigzag` -
  * Off `off` -
  * Clamp `clamp` -
  * Loop `loop` -
  * Zig Zag `zigzag` -

- Limit Type Maximum `maxtype` - ⊞ - The wrapping method used when applying limits to the input elements attribute.
  * Off `off` -
  * Clamp `clamp` -
  * Loop `loop` -
  * Zig Zag `zigzag` -
  * Off `off` -
  * Clamp `clamp` -
  * Loop `loop` -
  * Zig Zag `zigzag` -

- Minimum Value `min` - The minimum value that the selected attribute can have in the output.
- Maximum Value `max` - The maximum value that the selected attribute can have in the output.
- Positive Only `positive` - Enables absolute value output.
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

## Parameters - Quantize Page
- Quantize `quantize` - ⊞ - Convert values into a finite set of discrete levels.
  * Off `off` -
  * Floor `floor` -
  * Round `round` -
  * Ceiling `ceiling` -
  * > 0 `gt0` -
  * >= 0 `gteq0` -
  * == 0 `eq0` -
  * != 0 `neq0` -
  * <= 0 `lteq0` -
  * < 0 `lt0` -
  * Off `off` -
  * Floor `floor` -
  * Round `round` -
  * Ceiling `ceiling` -
  * > 0 `gt0` -
  * >= 0 `gteq0` -
  * == 0 `eq0` -
  * != 0 `neq0` -
  * <= 0 `lteq0` -
  * < 0 `lt0` -

- Value Step `quantstep` - Determines the step value used in quantization.
- Value Offset `quantoffset` - Determines the offset value used in quantization.
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Limit POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
