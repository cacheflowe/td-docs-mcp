---
url: https://docs.derivative.ca/Grid_POP
category: POPs
title: Grid_POP
---

# Grid POP
## Summary

The Grid POP creates rows and columns of points in a plane, and optionally creates multiple slices of points resulting in a 3D grid. The points can be connected with a variety of primitives using the Connectivity menu.
The grid size is specified in X, Y and Z, but the grid can be post-rotated to any angles using the Rotate parameters, and translated using the Translate parameters. Columns refers to the divisions in X, Rows to the divisions in Y, and Slices to the divisions in Z (pre-rotation).
Connectivity lets you choose the primitives and their organization that is output. You can output triangles, quads, lines, line strips, point primitives or no primitives (only points). Using the Line toggles, you can make your lines and line strips in X, Y and/or Z. Using the Plane toggles, you can make triangles and quads in XY, YZ and/or ZX.
Randomize parameters will randomize where each point is in its cell, if you think of a cell being the box around a point beside the next point's cell. This is especially useful when Randomize is set to 1, which guarantees that every cell has exactly one point evenly distributed randomly in its cell, and that no points end up in another cell. This is otherwise hard to assure. Random Size Fit puts the randomized grid inside the boundary of the original unrandomized grid, ir or in a space that is one cell larger than the original unrandomized grid.
Anchor will line up the left, center or right side of the grid to X=0. Similar for Y and Z.
Dimension: When the grid is passed to other POPs it cannot be known for certain how many rows, columns and slices were specified in the Grid POP. However the grid (and other generator POPs) output its [Dimensions](https://docs.derivative.ca/Dimension "Dimension") to all POPs connected to it. Dimension is a powerful indicator of the organizations of points in a points list. A 2D grid has dimensions `_numCols numRows_`, and a 3D grid has dimensions` _numCols NumRows numSlices_`. Every POP outputs it dimensions which can be used by built-in attributes like `_Dim[]`. The Append Dimension menu gives you more control over the form of the dimension that is output.
You can output point, vertex or primitive normals (`N` attribute), and you can output point or vertex texture coordinates (`Tex` attribute).
The Grid POP takes an input which will cause the starting grid to have the same bounding box as the bounding box of the input. Then turning on Modify Bounds lets you further transform the grid.
You can turn on Unique Points which makes each vertex of each primitive use a unique point (not point sharing). But the grid Dimension is lost in this case - dimension is simply `_numPoints_`.
See also [Dimension](https://docs.derivative.ca/Dimension "Dimension"), [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP"), [Tube POP](https://docs.derivative.ca/Tube_POP "Tube POP"), [Torus POP](https://docs.derivative.ca/Torus_POP "Torus POP"), [Line POP](https://docs.derivative.ca/Line_POP "Line POP")
[gridPOP_Class](https://docs.derivative.ca/GridPOP_Class "GridPOP Class")

## Parameters - Grid Page
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Lines `lines` -
  * Line Strips `linestrips` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals `quads` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Size `size` - ⊞ - The geometry 3D size.
  * Size `sizex` -
  * Size `sizey` -
  * Size `sizez` -

- Columns `cols` - Number of columns.
- Rows `rows` - Number of rows of points.
- Slices `slices` - Number of slices.
- Unique Points `uniquepoints` - Enable not sharing points between primitives.
- Seed `seed` - Numerical value that initializes the randomization.
- Random `random` - ⊞ - Random value range on points positions.
  * Random `randomx` -
  * Random `randomy` -
  * Random `randomz` -

- Random Size Fit `randomsizefit` - ⊞ - Scale factors for the bounding box as if random wasn't applied.
  * Random Size Fit `randomsizefitx` -
  * Random Size Fit `randomsizefity` -
  * Random Size Fit `randomsizefitz` -

- Line X/Y/Z `line` - ⊞ - Specifies whether to enable Lines in the X/Y/Z axis.
  * Line X/Y/Z `linex` -
  * Line X/Y/Z `liney` -
  * Line X/Y/Z `linez` -

- Plane XY/YZ/ZX `plane` - ⊞ - Plane orientation.
  * Plane XY/YZ/ZX `planex` -
  * Plane XY/YZ/ZX `planey` -
  * Plane XY/YZ/ZX `planez` -

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
  * Primitive `primNormals` -

- Texture Coordinates `texture` - ⊞ - Sets the attribute class where the texture coordinates should be created.
  * None `none` -
  * Point `point` -
  * Vertex `vert` -

- Append Dimension `dimension` - ⊞ - Always add a dimension, or only add a dimesion when its size is 2 or more.
  * When Rows Cols Slices > 1 `morethanone` -
  * Always for Rows Cols `rowscolsalways` -
  * Always for Rows Cols Slices `rowscolsslicesalways` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Grid POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
