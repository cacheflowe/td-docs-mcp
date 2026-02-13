---
url: https://docs.derivative.ca/Texture_Map_POP
category: POPs
title: Texture_Map_POP
---

# Texture Map POP
## Summary

The Texture Map POP creates the `Tex` attribute which is used to apply texture maps to surfaces, or to position procedurally-generated textures to surfaces.
The `Tex` attribute is a float3 3-component attribute. It can appear as a point attribute or a vertex attribute. It is created by all the generator POPs like the [Plane POP](https://docs.derivative.ca/Plane_POP "Plane POP"), [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP"), [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP"), [Rectangle POP](https://docs.derivative.ca/Rectangle_POP "Rectangle POP"), [Box POP](https://docs.derivative.ca/Box_POP "Box POP") etc., but `Tex` can also created with the Texture Map POP.
There are various projection methods, each useful depending on the type of geometry it is being applied to and its use-case.
Equirectangular Inside and Outside is a spherical polar longitude/latitude mapping used on vertices, used in VR, either to be viewed from the inside of a sphere or outside.
Domes require the mapping type Equidistant Azimuth, a fish eye projection. Projection mapping uses perspective from camera simulating what is "seen" from the position of a projector.
Triplanar Coordinates is a type that generates 3 sets of texture coordinates (3 attributes) used to map 1 texture onto an object but is a blend of 3 orthographic projections onto 3 sides of an object.
There is nothing special about the `Tex` attribute - any attribute can be used by a Material. The [Normalize POP](https://docs.derivative.ca/Normalize_POP "Normalize POP") and the [Projection POP](https://docs.derivative.ca/Projection_POP "Projection POP") produce attributes that can be used with a material, like doing orhtographic scaled projections, or spherical/cylindrical projections.
Some materials require multiple texture coordinates, which can be created with any of these methods in creating `Tex2`, `Tex3`, etc. and provided to the materials.
Note: In SOPs this was similar to the use of the `uvw` attribute for texture coordinates.
See also [PBR MAT](https://docs.derivative.ca/PBR_MAT "PBR MAT"), [Phong MAT](https://docs.derivative.ca/Phong_MAT "Phong MAT"), [Normalize POP](https://docs.derivative.ca/Normalize_POP "Normalize POP") and the [Projection POP](https://docs.derivative.ca/Projection_POP "Projection POP")
[texturemapPOP_Class](https://docs.derivative.ca/TexturemapPOP_Class "TexturemapPOP Class")

## Parameters - Texture Page
- Primitive Group `group` - Optional primitive group to select.
- Transform Input Texture Coord `transforminput` - Enable transforms on the input texture coordinates.
- Input Texture Coord Attribute `inputtexattr` - Input Texture coordinate attribute to transform.
- Position Attribute `posattr` - Projected position attribute.
- Projection Axis `axis` - ⊞ - Transform axis used for the projection
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- FOV Angle `fov` - Determines the camera's field of view angle.
- Center Mode `centermode` - ⊞ - For fisheye projection, whether the projection will use the bounding box center or a manually specified center.
  * Bounding Box Center `bbcenter` -
  * Manual `manual` -

- Center `center` - ⊞ - For fisheye projection, when center is manual, the position of the center to use for the projection.
  * Center `centerx` -
  * Center `centery` -
  * Center `centerz` -

- Camera `camera` - Specify the camera component.
- Camera Aspect `cameraaspect` - ⊞ - The aspect ratio for the projection.
  * Camera Aspect `cameraaspectx` -
  * Camera Aspect `cameraaspecty` -

- Apply to `applyto` - ⊞ - Where to apply the texture coordinates.
  * Natural location `natural` -
  * Point texture `point` -
  * Vertex texture (fix seams) `vertex` -

- Scale `s` - ⊞ - UV transform scaling factor.
  * Scale `su` -
  * Scale `sv` -
  * Scale `sw` -

- Offset `offset` - ⊞ - Adds an offset to the resulting texture mapping.
  * Offset `offsetu` - Adds an offset to the texture map coordinate.
  * Offset `offsetv` - Adds an offset to the texture map coordinate.
  * Offset `offsetw` - Adds an offset to the texture map coordinate.

- Rotate `angle` - Rotates the texture coordinate the specified value.
- Fix Face Seams `fixseams` - Enable attempting to correct texture continuity at face seams.
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

- Texture Method `texmethod` - ⊞ - Determines how the texture coordinates are applied.
  * XYZ Normalized (Point) `xyznorm` -
  * XYZ Position (Point) `xyzposition` -
  * Cylindrical (Vertex) `cylin` -
  * Face (Vertex) `face` -
  * Face Fit Outside (Vertex) `facefitoutside` -
  * Equirectangular Inside (Spherical Polar) (Vertex) `equirectangularin` -
  * Equirectangular Outside (Spherical Polar) (Vertex) `equirectangularout` -
  * Equidistant Azimuth (Fish Eye) (Point) `equiazimuth` -
  * Perspective From Camera (Point) `persp` -
  * Triplanar Coordinates (Point) `triplanar` -

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

- Translate `t` - ⊞ - Translate the texture coordinates in the three axes.
  * Translate `tx` -
  * Translate `ty` -
  * Translate `tz` -

- Rotate `r` - ⊞ - Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Scale `scaletwo` - ⊞ - UV transform scaling factor.
  * Scale `scaletwox` -
  * Scale `scaletwoy` -
  * Scale `scaletwoz` -

- Pivot `p` - ⊞ - The pivot point for the transform rotates and scales.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Texture Map POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
