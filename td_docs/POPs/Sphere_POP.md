---
url: https://docs.derivative.ca/Sphere_POP
category: POPs
title: Sphere_POP
---

# Sphere POP
## Summary

The Sphere POP creates spherical shapes in two different forms: Geodesic type creates a set of triangles of equally-spaced points which can be recursively divided giving more detail, and Grid type where you specify rows and columns of points similar to latitude/longitude lines. In both cases, the points can be connected with a variety of primitives using the Connectivity menu.
Three radii parameters give ellipsoid shapes. The Detail page gives partial spheres spanning a start-end range of latitude and longitude.
The Connectivity menu lets you output triangles, alternating triangles, quads, lines, line strips, point primitives or no primitives (None, only points).
The sphere is symmetric around an axis, Y by default. In Grid mode where you specify the number of columns and rows, Columns run along the longitude lines from top pole to bottom pole, Rows run along the circles of latitude.
In the Connectivity menu you can create lines and line strips along Rows, Columns or both merged together (Rows and Columns).
The sphere can be post-rotated and post-translated using the Rotate and Translate parameters.
Anchor will line up the left, center or right side of the sphere to X=0. Similar for Y and Z.
The Details page lets you make a partial sphere by specifying a latitude (V) and longitude (U) range with any starting/ending angle.
Dimension: When the sphere is passed to other POPs it cannot be known for certain how many rows and columns were specified. However the Sphere POP (and other generator POPs) output its [Dimensions](https://docs.derivative.ca/Dimension "Dimension") as metadata to all POPs connected to it, indicating its organizations of points in the points list. A sphere in Grid mode has dimensions `_numCols numRows_`, which can be used by built-in attributes like`_Dim[]` or by GLSL code.
You can output point or vertex normals (creating the `N` attribute), and you can output point or vertex texture coordinates (`Tex` attribute). The Texture Method menu lets you make Equirectangular or Fish Eye projections, correct for inside or outside the sphere.
The Sphere POP takes an input which will cause the starting sphere to have the same bounding box as the bounding box of the input. Then turning on Modify Bounds lets you further transform the sphere.
See also [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP"), [Tube POP](https://docs.derivative.ca/Tube_POP "Tube POP"), [Torus POP](https://docs.derivative.ca/Torus_POP "Torus POP"), [Dimension](https://docs.derivative.ca/Dimension "Dimension"), [Field POP](https://docs.derivative.ca/Field_POP "Field POP"), [Point Generator POP](https://docs.derivative.ca/Point_Generator_POP "Point Generator POP"), [Revolve POP](https://docs.derivative.ca/Revolve_POP "Revolve POP")
[spherePOP_Class](https://docs.derivative.ca/SpherePOP_Class "SpherePOP Class")

## Parameters - Sphere Page
- Type `type` - ⊞ - Determines the sphere type.
  * Geodesic `geodesic` -
  * Grid `grid` -
  * Tetrahedron `tetrahedron` -
  * Shared Points at Poles `sharedpoles` -

- Geodesic Connectivity `geodesictype` - ⊞ - Menu to select the connectivity between the geodesic sphere points.
  * None `none` -
  * Point Primitives `point` -
  * Triangles `triangles` -

- Grid Connectivity `surftype` - ⊞ - Menu to select the connectivity between the grid sphere points.
  * None `none` -
  * Point Primitives `point` -
  * Rows `rows` - Number of rows in the matrix - 2, 3 or 4.
  * Columns `cols` - Number of columns
  * Rows and Columns `rowcol` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals `quads` -

- Line Type `linetype` - ⊞ - Specifies whether lines should be made of line strip primitives or lines primitives.
  * Line Strip `linestrip` -
  * Lines `lines` -

- Orientation `orient` - ⊞ - Sets the axis for the sphere. Poles of sphere align with orientation axis.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Radius `rad` - ⊞ - Sphere radius.
  * Radius `radx` -
  * Radius `rady` -
  * Radius `radz` -

- Frequency `freq` - Controls the subdivision of the geodesic sphere, a higher frequency means more subdivisions.
- Fuse `fuse` - Fuses together the different subdivided triangles that make up the geodesic sphere.
- Fuse Technique `fusetechnique` - ⊞ - Technique used to fuse the subdivided triangles.
  * Brute Force `bruteforce` -
  * Shared Memory `sharedmemory` -
  * Spatial Grid `spatialgrid` -

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
  * Point `pointtexcoord` -
  * Vertex `vertextexcoord` -

- Texture Method `texmethod` - ⊞ - Determines how the texture coordinates are applied.
  * Equirectangular Inside (Spherical Polar) `equirectangularin` -
  * Equirectangular Outside (Spherical Polar) `equirectangularout` -
  * Equidistant Azimuth (Fish Eye) `equiazimuth` -

- FOV Angle `fov` - Determines the field of view angle for fish eye texture mapping.
- Shared Poles Connectivity `sharedpolessurftype` - ⊞ - Sets the connectivity for spheres that use shared points at the poles.
  * None `none` -
  * Point Primitives `point` -
  * Rows `rows` -
  * Columns `cols` -
  * Rows and Columns `rowcol` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals and Triangles `quadsandtriangles` -

## Parameters - Detail Page
- U Closed `closedu` - Enable closed geometry in U direction.
- Angle U `angleu` - ⊞ - The angle the sphere covers along U.
  * Angle U `beginangleu` -
  * Angle U `endangleu` -

- Tex Coords Range U `texrangeu` - ⊞ - Texture coordinate mode in the U direction.
  * Respect Angles `partial` -
  * 0 to 1 `full` -

- Angle V `anglev` - ⊞ - The angle the sphere covers along V.
  * Angle V `beginanglev` -
  * Angle V `endanglev` -

- Tex Coords Range V `texrangev` - ⊞ - Texture coordinate mode in the V direction.
  * Respect Angles `partial` -
  * 0 to 1 `full` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Sphere POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
