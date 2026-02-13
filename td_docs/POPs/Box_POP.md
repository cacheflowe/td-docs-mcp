---
url: https://docs.derivative.ca/Box_POP
category: POPs
title: Box_POP
---

# Box POP
## Summary

The Box POP creates 6-sided boxes. The box can have 8 points - one at each corner with each face sharing a point with two other faces. Or the box can have 24 points with each of the 6 faces using 4 unique points (Unique Points toggle parameter).
Where the box has 8 points, the user can choose to have vertex normals or primitive normals, which renders the cube "faceted" (flat-looking). Or the user can choose point normals (or no normals) which will make corners look non-faceted.
The Connectivity menu allows for no primitives to be output (just points) (None), or the points connected with 4-point Quadrelaterals (quads) or 3-point Triangles, or output one Point Primitive for every point.
The box can have optional rounded corners with control over radius and the amount of subdivision at the corners.
Tip: To subdivide the faces send the Box POP to a [Subdivide POP](https://docs.derivative.ca/Subdivide_POP "Subdivide POP") with Crease Weight 1.
Texture coordinates can be created with different placement - per-face, or one cube map that is wrapped over all the faces, etc. Point or vertex colors can be applied.
The Anchor parameters can shift the lower or upper side of the box to X=0, Y=0, Z=0. The box can be post-translated/rotated.
[boxPOP_Class](https://docs.derivative.ca/BoxPOP_Class "BoxPOP Class")

## Parameters - Box Page
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Triangles `triangles` -
  * Quadrilaterals `quads` -

- Unique Points `uniquepoints` - Enable not sharing points between primitives.
- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Size `size` - ⊞ - The geometry 3D size.
  * Size `sizex` -
  * Size `sizey` -
  * Size `sizez` -

- Round Corners `roundcorners` - Enable round corners.
- Corner Radius `cornerradius` - Set the corner radius for the round corners box.
- Subdivisions Depth `depth` - Controls the number of subdivision iterations applied to rounded corner boxes. Higher numbers gives a smoother surface.
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
  * Point `pointNormals` -
  * Vertex `vertNormals` -

- Texture Method `texmethod` - ⊞ - Determines how the texture coordinates are applied.
  * Box Inside `boxinside` -
  * Face Inside `faceinside` -
  * Cube Map Inside `cubemapinside` -
  * Box Outside `boxoutside` -
  * Face Outside `faceoutside` -
  * Cube Map Outside `cubemapoutside` -

- Extend to Corner `extenduv` - When rounding corners, chooses if texture goes around the rounded part or not.
- Color `color` - ⊞ - Puts a different color on each point, vertex or primitive, mostly for testing purposes.
  * None `none` -
  * Point `pointColor` -
  * Vertex `vertColor` -
  * Primitive `primColor` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Box POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
