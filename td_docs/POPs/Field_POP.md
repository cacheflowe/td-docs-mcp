---
url: https://docs.derivative.ca/Field_POP
category: POPs
title: Field_POP
---

# Field POP
## Summary

The Field POP adds a `Weight` attribute that determines how much each point is within a 3D shape. Fields are bounding regions in 3D space. The shapes include spheres (ellipsoids), cylinders, planes, paraboloids, etc, where all points within the shape (or on one side of the shape) are given a Weight of 1 and all other points are 0. The Field POP is often used to isolate or cut out sections of points in point clouds.
It also can output a `Dist` attribute, which is a distance to the surface for points that are outside the shape.
There are parameters that soften the `Weight` transition from 0 to 1: The Transition range is the distance over which the weight goes from 1 to 0, Transition Align determines if the transition from 1 to 0 starts at the field shape surface, or ends at the surface (default is half-way). The Transition Type allows for linear, ease-in ease-out, or smooth step transitions.
**Multiple fields in one Field POP**: A parameter called Specification POP is a pointer to a POP where each point is a specification defining a separate field - one point per field. The attributes of the specification POP are named the same as parameters tokens in the Field POP, and override the parameters for each field. Menus and toggles are represented as integers, starting at 0 for the first menu entry. You need only to create a Point POP with attributes named as the Field POP parameters, and then add a point per field, and set their values. (An attribute `sizex` will override the Size X (`sizex`) parameter.) Alternately you can generate points procedurally with attributes that match the Field POP parameter names. The workflow is the same as multiple strings defined in a specification DAT of the [Geo Text COMP](https://docs.derivative.ca/Geo_Text_COMP "Geo Text COMP") and the [Text COMP](https://docs.derivative.ca/Text_COMP "Text COMP").
**Using P as field position** : Although the rule is that the attribute name must be the same as the name of the parameter of the Field POP, `P` (position attribute) is a special case as it overrides `tx`, `ty` and `tz` parameters of the Field POP. If the node `point1` has attributes `radx` and `P`, they override the Field POP's `radx`, `tx`, `ty` and `tz` parameters.
**Multiple weights raw or mixed** : When you specify multiple fields, their weights are mixed together into the `Weight` attribute (using a blend mode like Screen of the [Composite TOP](https://docs.derivative.ca/Composite_TOP "Composite TOP") - combining multi-fields increase the `Weight` but it never exceeds 1). Alternately the weight for each field can be output raw in a multi-value `Weights` array attribute.
The `Weight` or `Distance` attribute can be added/multiplied with any another attribute, like a `PartForce` attribute to confine forces to certain regions.
[fieldPOP_Class](https://docs.derivative.ca/FieldPOP_Class "FieldPOP Class")

## Parameters - Field Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Field Attribute Scope `fieldattrscope` - Determines the scope of the attribute used to output the weight.
- Specification POP `specpop` - Reference to a POP where each point is a specification defining a separate field.
- Mode `mode` - ⊞ - Select the shape of the field.
  * Sphere `sphere` -
  * Box `box` -
  * Torus `torus` -
  * Tube Infinite `tubeinfinite` -
  * Tube Capped `tubecapped` -
  * Tube Rounded `tuberounded` -
  * Capsule `capsule` -
  * X-Plane `xplane` -
  * Y-Plane `yplane` -
  * Z-Plane `zplane` -
  * Parabola `parabola` -
  * Line Projection `lineprojection` -

- Size `size` - ⊞ - The geometry 3D size.
  * Size `sizex` -
  * Size `sizey` -
  * Size `sizez` -

- Radius `rad` - ⊞ - Radius of field.
  * Radius `radx` -
  * Radius `rady` -
  * Radius `radz` -

- Height `height` - The height of the tube.
- Roundness `roundness` - Roundness factor for rounded fields modes.
- Point A `pointa` - ⊞ - Shape first point.
  * Point A `pointax` -
  * Point A `pointay` -
  * Point A `pointaz` -

- Point B `pointb` - ⊞ - Shape second point.
  * Point B `pointbx` -
  * Point B `pointby` -
  * Point B `pointbz` -

- Strength `strength` - ⊞ - Sets the field strength.
  * Strength `strengthx` -
  * Strength `strengthy` -

- Exponent `exponent` - Sets the exponent on parabola fields.
- Transition Range `transitionrange` - Determines a transition range for weights.
- Transition Align `transitionalign` - Determines a transition offset for weights.
- Transition Type `transitiontype` - ⊞ - Determines a transition function for weights.
  * Linear `linear` -
  * Smooth Step `smoothstep` -
  * Ease In Ease Out `easeinout` -

- Absolute Value `absvalue` - Enable using the absolute value on the transitioned weight.
- Invert `invert` - Invert the attribute value resulting from the field.
- To Range `torange` - ⊞ - Sets the output range on the weigths.
  * To Range `torangemin` - Sets low value on the output range.
  * To Range `torangemax` - Sets high value on the output range.

- Delete Zeros `deletezeros` - Enable removal of points with weigth zero.
- Line Strip Behavior `linestripbehavior` - ⊞ - What to do when points of a line strip are deleted.
  * Delete Point of Line Strip `delpointoflinestrip` -
  * Split Line Strip `splitlinestrip` -
  * Delete Line Strip `dellinestrip` -

## Parameters - Transform Page
- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the order of the rotations within the overall transform order.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - Translate the field in the three axes.
  * Translate `tx` -
  * Translate `ty` -
  * Translate `tz` -

- Rotate `r` - ⊞ - Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Scale `s` - ⊞ - These three fields scale the Source geometry in the three axes.
  * Scale `sx` -
  * Scale `sy` -
  * Scale `sz` -

- Pivot `p` - ⊞ - The pivot point for the transform rotates and scales.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

## Parameters - Output Page
- Weight `weight` - ⊞ - Output a field weight attribute.
  * Weight `weight` -
  * Weight Output Attribute `outputattr` - Specifies the weight output attribute scope.

- Signed Distance `signeddistance` - ⊞ - Output a signed distance attribute for each point.
  * Signed Distance `signeddistance` -
  * Signed Distance Output Attribute `sdoutputattr` - Attribute scope for the signed distance field output.

- Per-Field Weights `perfieldweights` - ⊞ - Output an attribute array value for each field in the Specification POP.
  * Per-Field Weights `perfieldweights` -
  * Weights `perfieldweightsoutputattr` - Specifies the per-field weights output attribute scope.

- Per-Field Distances `perfielddistances` - ⊞ - Output an attribute array value for each field in the Specification POP.
  * Per-Field Distances `perfielddistances` -
  * Distances `perfielddistancesoutputattr` - Specifies the attribute scope used to output per field distances.

- Combine Operation `combineop` - ⊞ - Specify how to combine the output value with the combine attribute value.
  * None `none` -
  * Add `add` -
  * Multiply `mult` -

- Combine Entity `combineentity` - ⊞ - Specify which computed value to use for the combine operation.
  * Weight `weight` -
  * Signed Distance `signeddistance` -

- Combine Attribute `combineattr` - Input attribute scope for the combine operation.
- Combine Output Attribute `combineoutputattr` - ⊞ - Output attribute scope for the combine operation.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `combineoverrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `combineattrtype` - ⊞ - The combined output attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * Color `color` -
  * Color (double) `dcolor` -
  * Direction `dir` -
  * Direction (double) `ddir` -

- Components `combineattrnumcomps` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `combineattrdefaultval` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `combineattrdefaultval0` -
  * Default Value `combineattrdefaultval1` -
  * Default Value `combineattrdefaultval2` -
  * Default Value `combineattrdefaultval3` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Field POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
