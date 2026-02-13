---
url: https://docs.derivative.ca/Math_POP
category: POPs
title: Math_POP
---

# Math POP
## Summary

The Math POP takes one attribute of its input, does some math operations, and outputs to any existing attribute or a new attribute.
The attribute you specify can be any type, including float2, float3, float4. For Input Attribute Scope you can specify a subset of the components, like `P(1) P(0)` which has the effect of re-ordering Y and X.
Math operation include simple Multiply and Add, as well as 30+ math functions including the trigonometry functions, exponential, log, power, and combining multiple components of an attribute into one like `length()`.
The result can then be re-ranged (see the standalone [ReRange POP](https://docs.derivative.ca/ReRange_POP "ReRange POP") and quantized (see the standalone [Quantize POP](https://docs.derivative.ca/Quantize_POP "Quantize POP")).
If you set Parameter Size to 3 and your attribute is a float3 like `P`, then for each component of `P` you can have separate Multiply, Add and Operation parameters.
The Math POP operates on either point, vertex or primitive attributes.
Angle Units can be specified in degrees, radians or rotations (cycles). One cycle is 360 degrees or 6.283 (2 Pi) radians.
When creating new attribute, the Math POP will determine what data type it will be, but you can override it with the >>> expansion parameters. You can cause the output parameter to be integers.
See also [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP"), [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP"), [ReRange POP](https://docs.derivative.ca/ReRange_POP "ReRange POP"), [Quantize POP](https://docs.derivative.ca/Quantize_POP "Quantize POP")
[mathPOP_Class](https://docs.derivative.ca/MathPOP_Class "MathPOP Class")

## Parameters - Math Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- Angle Units `angleunit` - ⊞ - Any angles in parameters are expressed in degrees (0-360 is one rotation), radians (0-2*pi) or cycles (0-1 is one rotation).
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -

- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Pre Operation `preoper` - ⊞ - Math operation before the add-multiply-add.
  * None `none` -
  * abs(A) `abs` -
  * sign(A) `sign` -
  * sqrt(A) `sqrt` -
  * A * A `square` -
  * 1 / A `inverse` -
  * floor(A) `floor` -
  * round(A) `round` -
  * ceil(A) `ceil` -
  * int(A) `int` -
  * fract(A) `fract` -
  * degrees(A) `degrees` -
  * radians(A) `radians` -
  * normalize(A) `normalize` -
  * exp10(A) `exp10` -
  * exp2(A) `exp2` -
  * exp(A) `exp` -
  * log10(A) `log10` -
  * log2(A) `log2` -
  * ln(A) `ln` -
  * sin(A) `sin` -
  * cos(A) `cos` -
  * tan(A) `tan` -
  * asin(A) `asin` -
  * acos(A) `acos` -
  * atan(A) `atan` -
  * dbtopow(A) `dbtopow` -
  * powtodb(A) `powtodb` -
  * dbtoamp(A) `dbtoamp` -
  * amptodb(A) `amptodb` -
  * length(A) `length` -
  * compadd(A) `compadd` -
  * compsub(A) `compsub` -
  * compmult(A) `compmult` -
  * compdiv(A) `compdiv` -
  * compavg(A) `compavg` -
  * compmin(A) `compmin` -
  * compmax(A) `compmax` -

- Pre Add `preadd` - Value to add before the multiply.
- Multiply `mult` - Multiply by this value.
- Post Add `postadd` - Value to add after the multiply.
- Post Operation `postoper` - ⊞ - Math operation after the add-multiply-add.
  * None `none` -
  * abs(A) `abs` -
  * sign(A) `sign` -
  * sqrt(A) `sqrt` -
  * A * A `square` -
  * 1 / A `inverse` -
  * floor(A) `floor` -
  * round(A) `round` -
  * ceil(A) `ceil` -
  * int(A) `int` -
  * fract(A) `fract` -
  * degrees(A) `degrees` -
  * radians(A) `radians` -
  * normalize(A) `normalize` -
  * exp10(A) `exp10` -
  * exp2(A) `exp2` -
  * exp(A) `exp` -
  * log10(A) `log10` -
  * log2(A) `log2` -
  * ln(A) `ln` -
  * sin(A) `sin` -
  * cos(A) `cos` -
  * tan(A) `tan` -
  * asin(A) `asin` -
  * acos(A) `acos` -
  * atan(A) `atan` -
  * dbtopow(A) `dbtopow` -
  * powtodb(A) `powtodb` -
  * dbtoamp(A) `dbtoamp` -
  * amptodb(A) `amptodb` -
  * length(A) `length` -
  * compadd(A) `compadd` -
  * compsub(A) `compsub` -
  * compmult(A) `compmult` -
  * compdiv(A) `compdiv` -
  * compavg(A) `compavg` -
  * compmin(A) `compmin` -
  * compmax(A) `compmax` -

- Map from Low `fromlow` - Reranges the attribute value.
- Map from High `fromhigh` - Reranges the attribute value.
- Map to Low `tolow` - Reranges the attribute value.
- Map to High `tohigh` - Reranges the attribute value.
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
Extra Information for the Math POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
