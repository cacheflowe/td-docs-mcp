---
url: https://docs.derivative.ca/Rectangle_SOP
category: SOPs
title: Rectangle_SOP
---

# Rectangle SOP
## Summary

The Rectangle SOP creates a 4-sided polygon. It is a planar surface. The rectangle can be explicitly sized, or sized from other sources such as at the camera's view frustum, or the bounding box of a SOP connected to this node's input.
[rectangleSOP_Class](https://docs.derivative.ca/RectangleSOP_Class "RectangleSOP Class")

## Parameters - Page
- Orientation `orient` - ⊞ - Picks the major plane the rectangle's y-axis orients itself with. Set it to camera if it is to point towards a camera.
  * XY plane `xy` -
  * YZ plane `yz` -
  * ZX plane `zx` -
  * Fill Camera View `cam` -

- Camera `camera` - Specifies which camera to use if Orientation is set to camera.
- Camera Z `camz` - Used when using 'Fill Camera View'. Camera Z is an arbitrary distance you specify from the camera. It will move the rectangle so it is this many units away from the camera, then scale the rectangle so it fills the viewer.
- Camera Aspect `cameraaspect` - ⊞ - Specify the aspect ratio of the camera with this parameter and the Restangle SOP's aspect ratio will match. This makes it easy to apply a texture on the rectangle which matches the camera's viewport without any further adjustments.
  * X `cameraaspectx` -
  * Y `cameraaspecty` -

- Modify Bounds `modifybounds` - If a SOP is connected to the node's input, then the rectangle will be sized based on the bounding box of that SOP. Enabling Modify Bounds allows the resulting rectangle to be further modified by scaling it's size or moving it's center.
- Size `size` - ⊞ - Adjusts the size of the rectangle in X and Y. If the size of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as a scale. Otherwise it will set the size of the rectangle for all other modes.
  * X `sizex` -
  * Y `sizey` -

- Center `t` - ⊞ - These X, Y, and Z Values determine where the center of the Rectangle is located. If the position of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as an offset. Otherwise it will set the center of the rectangle for all other modes.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Texture Coordinates `texture` - ⊞ - Texture addes (0,1) coordinates to the vertices when set to Face. Creates a rectangle without uv attributes when set to Off.
  * Off `off` -
  * Face `face` -

- Compute Normals `normals` - Create a normal (N) attribute for this geometry.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Rectangle SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
