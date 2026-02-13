---
url: https://docs.derivative.ca/Normalize_POP
category: POPs
title: Normalize_POP
---

# Normalize POP
## Summary

The Normalize POP can re-scale all your XYZ position values to be in the 0-1 range, and it can do that to any attribute.
It can output to any existing or new attribute.
It is much more powerful than that: It can convert any position into polar or cylindrical coordinates, i.e. latitude, longitude and radius expressed in 0-1 ranges.
It can put any of these normalized values into any component of a float2, float3 or float4 attribute.
After normalizing the values between 0 and 1, it can also Bias the numbers to be closer to 0 or to 1, it can apply a Lookup function to the normalized value (like applying an ease-in ease-out), then apply an Exponent (boosts or lowers but keeps 0 and 1 values the same), and then Re-range the 0-1 values to any other range.
**Normalizing into polar or cylindrical form** : When normalizing a polar radius for example, it finds the point that is farthest from 0, 0, 0 and then computes the distance of each point in comparison to the farthest point. So that normalizes the radius.
When normalizing a point into a longitude around the Y-axis, it gives a value from 0 to 1, where a value of 0 or 1 is on the “back side” along the -Z axis, and a longitude value of .5 is on the “front side” along the +Z axis.
Similarly for latitude around the Y axis, a value of 0 is at the south pole (in the western civilization way of thinking), a value of 1 is at the north pole, and a value of .5 means the point is around the equator.
A similar kind of thing is done for cylindrical normalization around the Y axis.
**See also** the [Projection POP](https://docs.derivative.ca/Projection_POP "Projection POP") and the [Texture Map POP](https://docs.derivative.ca/Texture_Map_POP "Texture Map POP").
**About feeding components to Normalize and other POPs** - If you put `P(1) P(0) P(2)` (or `P.yxz`), it will first swap the first 2 components (x and y) and pass that to the next stage where if you have Box X, it will be processing the original y coordinate (`P(1)`) of the input.
[normalizePOP_Class](https://docs.derivative.ca/NormalizePOP_Class "NormalizePOP Class")

## Parameters - Normalize Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Aspect Correct `aspectcorrect` - Whether to preserve the input attribute aspect ratio.
- Replace Errors `replace` - Enable replacing inf or nan floating points values by a specific value.
- Error Value `errval` - Sets the replacing value on normalization errors
- Mode `mode` - ⊞ - Mode for the simplex noise types (Performance is legacy)
  * Mode `mode0` -
  * Mode `mode1` -
  * Mode `mode2` -

- Bias `bias` - ⊞ - Moves the normalized value bias forward or backward.
  * Bias `bias0` -
  * Bias `bias1` -
  * Bias `bias2` -

- Lookup Curve `lookupcurve` - ⊞ - Specifies whether to use a lookup curve from a list of predefined lookup curves.
  * Lookup Curve `lookupcurve0` -
  * Lookup Curve `lookupcurve1` -
  * Lookup Curve `lookupcurve2` -

- Exponent `exp` - ⊞ - Sets the exponent. The internal value is raised by the power of the exponent
  * Exponent `exp0` -
  * Exponent `exp1` -
  * Exponent `exp2` -

- Map to Low `tolow` - ⊞ - Reranges the attribute value.
  * Map to Low `tolow0` -
  * Map to Low `tolow1` -
  * Map to Low `tolow2` -

- Map to High `tohigh` - ⊞ - Reranges the attribute value.
  * Map to High `tohigh0` -
  * Map to High `tohigh1` -
  * Map to High `tohigh2` -

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
Extra Information for the Normalize POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
