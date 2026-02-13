---
url: https://docs.derivative.ca/Plane_POP
category: POPs
title: Plane_POP
---

# Plane POP
## Summary

The Plane POP creates rows and columns of points in a planar grid shape. The points can be connected with a variety of primitives using the Connectivity menu.
The Connectivity menu lets you output triangles, alternating triangles, quads, lines, line strips, point primitives or no primitives (None, only points).
You specify number of rows and columns. Columns refers to the divisions in X by default, Rows to the divisions in Y by default.
In the Connectivity menu you can create lines and line strips along Rows, Columns or both merged together.
The Orientation menu lets you place the grid on the YZ plane, or the ZX plane.
Anchor will line up the left, center or right side of the grid to X=0, Y=0 or Z=0.
The planar grid can then be post-rotated and post-translated using the Rotate and Translate parameters.
Dimension: When the grid is passed to other POPs it cannot be known for certain how many rows and columns were specified. However the Plane POP (and other generator POPs) output its [Dimensions](https://docs.derivative.ca/Dimension "Dimension") as metadata to all POPs connected to it, indicating its organizations of points in the points list. A plane grid has dimensions `_numCols numRows_`, which can be used by built-in attributes like`_Dim[]` or by GLSL code.
You can output point or vertex normals (creating the `N` attribute), and you can output point or vertex texture coordinates (`Tex` attribute).
After the Orientation is applied, say it is YZ, texture coordinates are assigned where the first component `Tex(0)` is along the axis of the first letter (Y in the YZ orientation), and `Tex(1)` is along the axis of the second letter (Z in the YZ orientation).
The Plane POP takes an input which will cause the starting grid to have the same bounding box as the bounding box of the input. Then turning on Modify Bounds lets you further transform the tube.
See also [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP"), [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP"), [Torus POP](https://docs.derivative.ca/Torus_POP "Torus POP"), [Revolve POP](https://docs.derivative.ca/Revolve_POP "Revolve POP"), [Dimension](https://docs.derivative.ca/Dimension "Dimension")
[planePOP_Class](https://docs.derivative.ca/PlanePOP_Class "PlanePOP Class")

## Parameters - Plane Page
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Rows `rows` - Number of rows in the matrix - 2, 3 or 4.
  * Columns `cols` - Number of columns
  * Rows and Columns `rowcol` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals `quads` -

- Line Type `linetype` - ⊞ - Specifies whether lines should be made of line strip primitives or lines primitives.
  * Line Strip `linestrip` -
  * Lines `lines` -

- Orientation `orient` - ⊞ - Sets the plane orientation.
  * XY plane `xy` -
  * YZ plane `yz` -
  * ZX plane `zx` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Size `size` - ⊞ - The plane 2D size.
  * Size `sizeu` - Plane length along U axis.
  * Size `sizev` - Plane length along V axis.

- Columns `cols` -
- Rows `rows` -
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
  * Vertex `vertNormals` -

- Texture Coordinates `texture` - ⊞ - Sets the attribute class where the texture coordinates should be created.
  * None `none` -
  * Point `point` -
  * Vertex `vert` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Plane POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
