---
url: https://docs.derivative.ca/Circle_POP
category: POPs
title: Circle_POP
---

# Circle POP
## Summary

The Circle POP creates a number of points in a circle, ellipse or arc, and optionally connects them as a line strip, a set of triangles, separate 2-point lines, or unconnected as point primitives. You can choose to not Close the circle, where the last point/section is not connected to first.
You can add texture coordinate, normal or tangent attributes to the points or to the vertices. Of note are normals, which can optionally point radially away from the center, or tangent to the circle.
Orientation can be in any of the XY, YZ or ZX planes and then further rotated and translated.m
If a POP is connected to the input, it will translate / scale the circle to the bounding box of the input. If a POP is connected to the input and if Modify Bounds is set, it will scale / translate the circle to the bounding box of the input, and you can further translate/scale/rotate the circle.
See also [Rectangle POP](https://docs.derivative.ca/Rectangle_POP "Rectangle POP"), [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP"), [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP"), [Line POP](https://docs.derivative.ca/Line_POP "Line POP").
[circlePOP_Class](https://docs.derivative.ca/CirclePOP_Class "CirclePOP Class")

## Parameters - Circle Page
- Connectivity `connectivity` - ⊞ - Determines whether and how to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Surface `surface` -
  * Line Strip `linestrip` -
  * Lines `lines` -

- Orientation `orient` - ⊞ - Sets the circle orientation.
  * XY Plane `xy` -
  * YZ Plane `yz` -
  * ZX Plane `zx` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Radius `rad` - ⊞ - Distance to the center.
  * Radius `radx` -
  * Radius `rady` -

- Divisions `divs` - The number of divisions of the circle or arc.
- Closed `closed` - The last vertex is connected to the first vertex.
- Arc Angles `angle` - ⊞ - The start and end angles of an arc.
  * Arc Angles `beginangle` -
  * Arc Angles `endangle` -

- Anchor U `anchoru` - Puts the left side, the middle or the right side at the origin 0.
- Anchor V `anchorv` - Puts the bottom side, the middle or the top side at the origin 0.
- Translate `t` - ⊞ - Translate the points in the three axes.
  * Translate `tx` -
  * Translate `ty` -
  * Translate `tz` -

- Rotate `r` - ⊞ - Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Uniform Scale `scale` - Specifies a uniform scale factor in all axes.
- Normal `normal` - ⊞ - Choose whether to create a normal attribute and the attribute class of the normal attribute.
  * None `none` -
  * Point `pointNormals` -

- Normal Direction `normaldirection` - ⊞ - Choose the normal direction.
  * Default `default` -
  * Radial `radial` -
  * Tangent `tangent` - Enable the output of a Tangent attribute.

- Tangent `tangent` - ⊞ -
  * None `none` -
  * Point `pointNormals` -

- Tangent Direction `tangentdirection` - ⊞ - How to calculate the tangent for each point.
  * Radial `radial` -
  * Tangent `Tangent` -

- Texture Coordinates `texture` - ⊞ - Sets the attribute class where the texture coordinates should be created.
  * None `none` -
  * Point `pointNormals` -
  * Vertex `vertNormals` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Circle POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
