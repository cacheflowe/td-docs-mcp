---
url: https://docs.derivative.ca/Transform_POP
category: POPs
title: Transform_POP
---

# Transform POP
## Summary

The Transform POP applies a translate, rotate and scale to the position (attribute `P`) and normal (attribute `N`) of all the points of the input.
It can apply the transform to any float3 attribute, not just `P`, and then output to any existing or new float3 attribute, by default `P`. It can apply the transform to point, vertex or primitive attributes.
It can apply partial transforms to the points based on a 0 to 1 `Weight` attribute so that some parts of the geometry are affected and other parts not transformed. The [Field POP](https://docs.derivative.ca/Field_POP "Field POP") can generate a `Weight` attribute to be used by Transform.
**Per-point mapping of parameters** - using the Map page, every point can receive a different value for the transform parameters, based on mapping incoming attributes to the translate, scale, rotate, pivot etc. parameters, So essentially every point can get a completely different transform. See [Mapping POP Attributes to Parameters](https://docs.derivative.ca/Mapping_POP_Attributes_to_Parameters "Mapping POP Attributes to Parameters").
A further transform can be applied by specifying a Look At component (typically a [Null COMP](https://docs.derivative.ca/Null_COMP "Null COMP") or [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP")), and choosing which axis points to the origin of that component.
Another transform may be applied by providing a 16-value transform matrix via a CHOP or DAT.
The order of applying the translate, rotate and scale parameters is determined by the Transform Order and the Rotate Order menus.
The Inverse toggle parameter applies an inverse of the transform specified. (Instead of tx=2 ry=50 sz=4, the equivalent of sz=.25, ry=-50 tx=-2)
On the Align page there are numerous options for aligning the X, Y or Z coordinate to the different sides/center of the input's bounding box or to the bounding box of a reference POP.
See also [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP"), [Trig POP](https://docs.derivative.ca/Trig_POP "Trig POP")
[transformPOP_Class](https://docs.derivative.ca/TransformPOP_Class "TransformPOP Class")

## Parameters - Transform Page
- Mode `mode` - ⊞ - Choose what the transform is applied to.
  * Transform Geometry `transformgeo` -
  * Transform Attribute `transformattrib` -
  * Transform Attribute Scope as Position `transformattribscopepos` -
  * Transform Attribute Scope as Vector `transformattribscopevec` -
  * Transform Attribute `transformattr` -
  * Transform Attribute Scope as Position `transformattrscopepos` -
  * Transform Attribute Scope as Vector `transformattrscopevec` -

- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Input Attribute (Scope) `inputattrscope` - Input attribute when mode is Transform Attribute, input attribute scope when mode is Transform Attribute Scope
- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Weight Attribute `weightattr` - Specifies the scope of the attribute that stores weight values
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

- Translate `t` - ⊞ - Translate the points in the three axes.
  * Translate `tx` -
  * Translate `ty` -
  * Translate `tz` -

- Rotate `r` - ⊞ - Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Scale `s` - ⊞ - Scale factor for each axis.
  * Scale `sx` -
  * Scale `sy` -
  * Scale `sz` -

- Pivot `p` - ⊞ - The pivot point for the transform rotates and scales.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

- Uniform Scale `scale` - Specifies a uniform scale factor in all axes.
- Invert `invert` - Invert the transform resulting from the Translate, Rotate and Scale parameters.
- Vectors Maintain Length `vlength` - Enable preserving the original vector length after applying transformations.
- Look At `lookat` - Allows you to orient your object by naming the object you would like it to Look At, or (Z axis) point to. Once you have designated this object to look at, it will continue to face that object, even if you move it. This is useful if, for instance, you want a camera to follow another object's movements. The Look At parameter points the object in question at the other object's origin.
- Up Vector `upvector` - ⊞ - Sets the up vector when setting up the look at transform.
  * Up Vector `upvectorx` -
  * Up Vector `upvectory` -
  * Up Vector `upvectorz` -

- Forward Direction `forwarddir` - ⊞ - Determines the forward direction for look at transformation.
  * +X `posx` -
  * -X `negx` -
  * +Y `posy` -
  * -Y `negy` -
  * +Z `posz` -
  * -Z `negz` -

- Xform Matrix/CHOP/DAT `xformmatrixop` - Sets as transform using a 4x4 matrix directly.
- Multiply Order `multiplyorder` - ⊞ - Order of transform between the transform matrix and the transform resulting from the Translate Rotate Scale parameters.
  * Input, then Transform Page `inputxformpage` -
  * Transform Page, then Input `xformpageinput` -

- Output Attribute (Scope) `outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
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

## Parameters - Align Page
- Align Transform Order `alignxformorder` - ⊞ - Whether the transform from the Transform page or the Align page is applied first.
  * Transform, then Align `transformalign` -
  * Align, then Transform `aligntransform` -

- Align Operation Order `alignopord` - ⊞ - Set the order in which scale and transform is applied in the align transform.
  * Scale Translate `st` -
  * Translate Scale `ts` -

- Align Translate X `aligntx` - ⊞ - Sets the center of the geometry in X for the align transform.
  * Off `off` -
  * Origin `origin` -
  * Reference Input `reference` -

- From Input `fromx` - ⊞ - Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above.
  * Min `min` -
  * Center `center` -
  * Max `max` -

- To Reference `tox` - ⊞ - Determines where on the reference the input is aligned.
  * Min `min` -
  * Center `center` -
  * Max `max` -

- Align Translate Y `alignty` - ⊞ - Sets the center of the geometry in Y for the align transform.
  * Off `off` -
  * Origin `origin` -
  * Reference Input `reference` -

- From Input `fromy` - ⊞ - Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above.
  * Min `min` -
  * Center `center` -
  * Max `max` -

- To Reference `toy` - ⊞ - Determines where on the reference the input is aligned.
  * Min `min` -
  * Center `center` -
  * Max `max` -

- Align Translate Z `aligntz` - ⊞ - Sets the center of the geometry in Z for the align transform.
  * Off `off` -
  * Origin `origin` -
  * Reference Input `reference` -

- From Input `fromz` - ⊞ - Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above.
  * Min `min` -
  * Center `center` -
  * Max `max` -

- To Reference `toz` - ⊞ - Determines where on the reference the input is aligned.
  * Min `min` -
  * Center `center` -
  * Max `max` -

- Align Scale `alignscale` - ⊞ - Sets the scale of the geometry for the align transform.
  * Per Axis `peraxis` -
  * Unity `unity` -
  * Reference `reference` -

- Align Scale X `alignscalex` - ⊞ - If align scale is per axis, sets the X scale of the geometry for the align transform.
  * Off `off` -
  * Unity `unity` -
  * Reference Input `reference` -
  * Unity Proportional `unityprop` -
  * Reference Proportional `referenceprop` -

- Align Scale Y `alignscaley` - ⊞ - If align scale is per axis, sets the Y scale of the geometry for the align transform.
  * Off `off` -
  * Unity `unity` -
  * Reference Input `reference` -
  * Unity Proportional `unityprop` -
  * Reference Proportional `referenceprop` -

- Align Scale Z `alignscalez` - ⊞ - If align scale is per axis, sets the Z scale of the geometry for the align transform.
  * Off `off` -
  * Unity `unity` -
  * Reference Input `reference` -
  * Unity Proportional `unityprop` -
  * Reference Proportional `referenceprop` -

## Parameters - Map Page
- Mapping `map` - Start of Sequential Parameter Blocks for attribute-to-parameter mapping.
- OP `map0op` - Source OP for parameter mapping. The default of _in0 means the input POP.
- Element `map0element` - The attribute (or component of an attribute) that will be mapped to a parameter per-point.
- Parameter `map0parm` - ⊞ - Parameter on the current POP that will be mapped from the Element (the attribute).
  * t (Translate) `t` -
  * tx `tx` -
  * ty `ty` -
  * tz `tz` -
  * r (Rotate) `r` -
  * rx `rx` -
  * ry `ry` -
  * rz `rz` -
  * s (Scale) `s` -
  * sx `sx` -
  * sy `sy` -
  * sz `sz` -
  * p (Pivot) `p` -
  * px `px` -
  * py `py` -
  * pz `pz` -
  * scale (Uniform Scale) `scale` -

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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Transform POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
