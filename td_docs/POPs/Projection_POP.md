---
url: https://docs.derivative.ca/Projection_POP
category: POPs
title: Projection_POP
---

# Projection POP
## Summary

The Projection POP takes a float3 3D spatial attribute, like `P`, and outputs to a float3 attribute, transforming the attribute between cartesian (orthographic), polar, cylindrical, and perspective coordinate systems. For example, all the the points in cartesian X, Y and Z format can be converted into a polar longitude/latitude/radius format.
The menu From Coordinate System lets you choose how to interpret the 3 numbers of the input attribute:
  * Cartesian treats the 3 numbers of the float3 attribute as X, Y and Z in the usual 3D "orthogonal" coordinate space. (In TouchDesigner X is horizontal left-to-right, Y is vertical bottom to top. Z is along line of sight distant to near.)
  * Spherical treats the three numbers of the attribute as longitude, latitude and radius, assuming the axis is the vertical Y axis.
  * Cylindrical treats the 3 numbers of the attribute as latitude (angle around Y), Y value and a radius.
  * Screen Space is a perspective form along the Z axis - you need to specify additional camera/perspective info. 0,0 is the bottom left corner, 1, 1 is top right.
  * Normalized Device Coordinates (NDC) - For points within the field of view, the first and second components are between -1 and 1 where 0,0 is at the center. The third component is between 0 and 1 (as re-ranged to the Near and Far distances).

The menu To Coordinate System lets you choose what form you want the 3 numbers of the output attribute to be in.
The angles can be expressed in
  * Degrees in the usual graphics standard (360 is a full rotation), or
  * Radians (Pi 3.14157 is one full rotation)
  * Cycles (value of 1 means one full 360 degrees rotation)
  * Normalized - a 0-1 normalized form which, like Spherical longitude is like a wraparound: looking along the -Z axis, the value is 0 at the back, .25 the left, .5 is face-on, .75 at the right, and 1 at the back. For latitude the value goes from 0 at the south pole and 1 at the north pole. This is used for mapping a texture on a sphere sometimes.

See also tbe [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP"), [Tube POP](https://docs.derivative.ca/Tube_POP "Tube POP"), [Normalize POP](https://docs.derivative.ca/Normalize_POP "Normalize POP") and the [Texture Map POP](https://docs.derivative.ca/Texture_Map_POP "Texture Map POP").
[projectionPOP_Class](https://docs.derivative.ca/ProjectionPOP_Class "ProjectionPOP Class")

## Parameters - Projection Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Input Attribute Scope `inputattrscope` - Input's attributes you want to affect within the chosen attribute class, or attribute components.
- From Coordinate System `fromcoordsys` - ⊞ - The coordinate system to convert from.
  * Cartesian `cartesian` -
  * Spherical `spherical` -
  * Cylindrical `cylindrical` -
  * Screen Space `screenspace` -
  * Normalized Device Coordinates `ndc` -

- To Coordinate System `tocoordsys` - ⊞ - Specifies the target coordinate system for the operation.
  * Cartesian `cartesian` -
  * Spherical `spherical` -
  * Cylindrical `cylindrical` -
  * Screen Space `screenspace` -
  * Normalized Device Coordinates `ndc` -

- Angle Units `angunit` - ⊞ - The unit for the angles, when some of the coordinates are angles in the source or destination coordinate system.
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -
  * Normalized `norm` -

- Camera `camera` - Specify the camera component.
- Aspect Correct UVs `aspectcorrectuv` - Whether respect the aspec ratio for the projection.
- Aspect Ratio `aspect` - ⊞ - The aspect ratio of the camera projection.
  * Aspect Ratio `aspectx` -
  * Aspect Ratio `aspecty` -

- Horizontal FOV `fov` - Horizontal field of view when source or destination coordinate system is screen space or normalized device coordinates.
- Near Depth `depthnear` - Depth of the near clipping plane.
- Far Depth `depthfar` - Depth of the far clipping plane.
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

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Projection POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
