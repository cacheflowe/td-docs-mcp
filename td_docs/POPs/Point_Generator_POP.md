---
url: https://docs.derivative.ca/Point_Generator_POP
category: POPs
title: Point_Generator_POP
---

# Point Generator POP
## Summary

The Point Generator POP creates a specified number of points, either randomly or in a pattern, on the surface of shape or within the volume of a closed shape.
The Shape is not a set of polygons (see [Sprinkle POP](https://docs.derivative.ca/Sprinkle_POP "Sprinkle POP") for that) but is a common mathematical shape like a sphere, circle, box, cylinder, torus, rectangle or line, whose shape and position/scale/rotation is controlled with POP parameters.
A menu chooses between points on a surface, or points within its volume.
Volumes should be closed surfaces, but Point Generator still gives a distribution of points around holes of non-closed surfaces.
A Random toggle, when off, gives predictable but patterned distribution of points on/in surfaces.
There are controls of orientation axis and angles of the basic shapes.
Note: Presently there is no option to make the distribution of points be uniform per unit of surface area. For example, triangles get approximately the same number of points on small triangles as on large triangles. (future option)
A Random distribution of points along a line segment in Line mode is controlled with two points in XYZ.
You can add normal (`N` float3) and tangent (`T` float4) attribute vectors on points, vertices or primitives, with some choices of further randomization of these attributes.
See also [Sprinkle POP](https://docs.derivative.ca/Sprinkle_POP "Sprinkle POP"), [Random POP](https://docs.derivative.ca/Random_POP "Random POP"), [Noise POP](https://docs.derivative.ca/Noise_POP "Noise POP")
[pointgeneratorPOP_Class](https://docs.derivative.ca/PointgeneratorPOP_Class "PointgeneratorPOP Class")

## Parameters - Point Generator Page
- Shape `shape` - ⊞ - Sets the points generated shape.
  * Sphere `sphere` -
  * Box `box` -
  * Torus `torus` -
  * Tube `tube` -
  * Rectangle `rectangle` -
  * Circle `circle` -
  * Line `line` -

- Create Point Primitives `createpointprim` - Enable creating point primitives
- Number of Points `numpoints` - Sets the number of points.
- Distribution `distribution` - ⊞ - Determines what distribution type is returned
  * Volume `volume` -
  * Surface `surface` -

- Random `random` - Enable random surface distribution.
- Seed `seed` - Numerical value that initializes the randomization.
- Orientation `orient` - ⊞ - Sets the point cloud orientation.
  * Default `default` -
  * XY Plane (Z axis) `xy` -
  * YZ Plane (X axis) `yz` -
  * ZX Plane (Y axis) `zx` -

- Size `size` - ⊞ - The geometry 3D size.
  * Size `size1` -
  * Size `size2` -
  * Size `size3` -
  * Size `sizex` -
  * Size `sizey` -
  * Size `sizez` -

- Radius `radius` - ⊞ - Radius.
  * Radius `radius1` -
  * Radius `radius2` -
  * Radius `radius3` -
  * Radius `radiusx` -
  * Radius `radiusy` -
  * Radius `radiusz` -

- Height `height` - The height of the tube.
- Point A `pointa` - ⊞ - Line first point.
  * Point A `pointa1` -
  * Point A `pointa2` -
  * Point A `pointa3` -
  * Point A `pointax` -
  * Point A `pointay` -
  * Point A `pointaz` -

- Point B `pointb` - ⊞ - Line second point.
  * Point B `pointb1` -
  * Point B `pointb2` -
  * Point B `pointb3` -
  * Point B `pointbx` -
  * Point B `pointby` -
  * Point B `pointbz` -

- Normal `normal` - ⊞ - Choose whether to create a normal attribute and the attribute class of the normal attribute.
  * None `none` -
  * Point `pointNormals` -
  * Vertex `vertNormals` -
  * Primitive `primNormals` -

- Normal Direction `normaldirection` - ⊞ - Choose the normal direction.
  * Default `default` -
  * Random `random` -

- Tangent `dotangent` - ⊞ - Sets the tangent mode.
  * Off `off` -
  * Default `default` -
  * Random to Normal `randomtonormal` -
  * Random `random` -

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

- Translate `t` - ⊞ - Translate the points in the three axes.
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

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Point Generator POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
