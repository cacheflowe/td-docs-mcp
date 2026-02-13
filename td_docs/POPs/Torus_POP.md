---
url: https://docs.derivative.ca/Torus_POP
category: POPs
title: Torus_POP
---

# Torus POP
## Summary

The Torus POP creates rows and columns of points in a closed tube shape. The points can be connected with a variety of primitives using the Connectivity menu.
The ring and the cross-section of the torus each have a radius parameter.
The Connectivity menu lets you output triangles, alternating triangles, quads, lines, line strips, point primitives or no primitives (None, only points).
You specify number of rows and columns. Columns refers to the divisions around the ring, Rows to the divisions around the cross-section circle.
In the Connectivity menu you can create lines and line strips along Rows, Columns or both merged together.
The torus is symmetric around an axis, Y by default, but the torus can be post-rotated and post-translated using the Rotate and Translate parameters.
Anchor will line up the left, center or right side of the torus to X=0, Y=0 or Z=0.
The Details page lets you make a partial torus by specifying an arc of the ring with any starting/ending angle.
The End Caps toggle will add triangles or quads to fill the end caps and make the torus a closed volume, which still preserves the [Dimension](https://docs.derivative.ca/Dimension "Dimension") since no points are added or removed, only primitives are added.
[Dimension](https://docs.derivative.ca/Dimension "Dimension"): When the torus is passed to other POPs it cannot be known for certain how many rows and columns were specified. However the Torus POP (and other generator POPs) output its Dimensions as metadata to all POPs connected to it, indicating its organizations of points in the points list. A torus has dimensions numCols numRows, which can be used by built-in attributes like `_Dim[]` or by GLSL code.
You can output point or vertex normals (creating the `N` attribute), and you can output point or vertex texture coordinates (`Tex` attribute).
The Torus POP takes an input which will cause the starting tube to have the same bounding box as the bounding box of the input. Then turning on Modify Bounds lets you further transform the torus.
See also [Tube POP](https://docs.derivative.ca/Tube_POP "Tube POP"), [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP"), [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP"), [Field POP](https://docs.derivative.ca/Field_POP "Field POP"), [Point Generator POP](https://docs.derivative.ca/Point_Generator_POP "Point Generator POP"), [Revolve POP](https://docs.derivative.ca/Revolve_POP "Revolve POP"), [Dimension](https://docs.derivative.ca/Dimension "Dimension")
[torusPOP_Class](https://docs.derivative.ca/TorusPOP_Class "TorusPOP Class")

## Parameters - Torus Page
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

- Orientation `orient` - ⊞ - Sets the axis for the torus.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Radius `rad` - ⊞ - Radii of ring and radius of swept circle.
  * Radius `radx` -
  * Radius `rady` -

- Columns `cols` -
- Rows `rows` -
- Anchor U `anchoru` - Puts the left side, the middle or the right side at the origin 0.
- Anchor V `anchorv` - Puts the bottom side, the middle or the top side at the origin 0.
- Anchor W `anchorw` - Puts the back side, the middle or the front side at the origin 0.
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
  * Point `pointNormals` -
  * Vertex `vertNormals` -

## Parameters - Detail Page
- U Closed `closedu` - Enable closed geometry in U direction.
- V Closed `closedv` - Enable closed geometry in V direction.
- Angle U `angleu` - ⊞ - The angle the torus covers along U.
  * Angle U `beginangleu` -
  * Angle U `endangleu` -

- Angle V `anglev` - ⊞ - The angle the torus covers along V.
  * Angle V `beginanglev` -
  * Angle V `endanglev` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Torus POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
