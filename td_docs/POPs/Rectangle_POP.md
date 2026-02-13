---
url: https://docs.derivative.ca/Rectangle_POP
category: POPs
title: Rectangle_POP
---

# Rectangle POP
## Summary

The Rectangle POP creates a 4-point rectangle with optional rounded corners, and outputs it as a line strip, a pair of triangles, a quad, separate 2-point lines, unconnected point primitives, or without any primitives.
The mode Fill Camera View uses a [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and extra viewing information (aspect ratio) to put the four points of the rectangle at the corners of the camera view at a certain distance away from the camera. This is useful for rendering a background plate that fills the field of view of a camera, behind the geometry of a scene, or for aligning geometry in the field of view of a camera.
If a POP is connected to the input, it will translate / scale the rectangle to the bounding box of the input. If a POP is connected to the input and if Modify Bounds is set, it will scale / translate the rectangle to the bounding box of the input, and you can further translate/scale/rotate the rectangle.
You can add texture coordinates (`Tex`), or normal (`N`) attributes to the points or to the vertices.
Orientation is in the XY plane. The left, middle or right side of the rectangle can be anchored to X=0. Similar for Y, and then the rectangle can be further scaled, rotated and translated.
See also [Circle POP](https://docs.derivative.ca/Circle_POP "Circle POP"), [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP"), [Line POP](https://docs.derivative.ca/Line_POP "Line POP"), [Point POP](https://docs.derivative.ca/Point_POP "Point POP").
[rectanglePOP_Class](https://docs.derivative.ca/RectanglePOP_Class "RectanglePOP Class")

## Parameters - Rectangle Page
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `point` -
  * Lines `lines` -
  * Line Strips `linestrips` -
  * Triangles `triangles` -
  * Quadrilaterals `quads` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP.
- Orientation `orient` - ⊞ - Sets the rectangle orientation.
  * XY plane `xy` -
  * YZ plane `yz` -
  * ZX plane `zx` -
  * Fill Camera View `cam` -

- Camera `camera` - Specify the camera component.
- Dist from Camera `distfromcam` - Sets the distance of the rectangle from the camera when orienting it to face the camera
- Camera Aspect `cameraaspect` - ⊞ - The aspect ratio for the projection.
  * Camera Aspect `cameraaspectx` -
  * Camera Aspect `cameraaspecty` -

- Size `size` - ⊞ - The geometry 3D size.
  * Size `sizex` -
  * Size `sizey` -

- Round Corners `roundcorners` - Enable round corners.
- Corner Radius `cornerradius` - Set the corner radius for the round corners rectagle
- Corner Sides `cornersides` - Sets the number of sides on round corners
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

- Texture Coordinates `texture` - ⊞ - Sets the attribute class where the texture coordinates should be created.
  * None `none` -
  * Point `point` -
  * Vertex `vert` -

- Texture Fit `texturefit` - ⊞ - Determines how the texture coordinates are scaled and positioned relative to the rectangle.
  * Fill `fill` -
  * Fit Best `best` -
  * Fit Outside `outside` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Rectangle POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
