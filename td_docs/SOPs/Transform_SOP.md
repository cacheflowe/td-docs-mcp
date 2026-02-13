---
url: https://docs.derivative.ca/Transform_SOP
category: SOPs
title: Transform_SOP
---

# Transform SOP
## Summary

The Transform SOP translates, rotates and scales the input geometry in "object space" or local to the SOP. The Model Editor and the Transform SOP both work in "object space", and change the X Y Z positions of the points. In contrast, animating the transformation channels of an object in the Geometry Viewer Pane moves/scales the entire object in "world space" and does not affect the XYZ point positions of the geometry.
[transformSOP_Class](https://docs.derivative.ca/TransformSOP_Class "TransformSOP Class")

## Parameters - Transform Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu.
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

- Translate `t` - ⊞ - These three fields move the Source geometry in the three axes.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the Source geometry in the three axes.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - These three fields scale the Source geometry in the three axes.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.
For example, during a scaling operation, if the pivot point of an object is located at: `-1, -1, 0` and you wanted to scale the object by `0.5` (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left.
[![TouchGeometry91.gif](https://docs.derivative.ca/images/b/bf/TouchGeometry91.gif)](https://docs.derivative.ca/File:TouchGeometry91.gif)
In the example above, rotations performed on an object with different pivot points produce very different results.
  * X `px` -
  * Y `py` -
  * Z `pz` -

- Uniform Scale `scale` - Uniform Scale allows you to shrink or enlarge geometry along all three axes simultaneously.
- Normals Maintain Length `vlength` - When selected, vector type attributes (i.e. normals, velocity) maintain the same length under transforms. i.e. When geometry is scaled, the normals remain constant in length.
- Look At `lookat` - Allows you to orient your object by naming the object you would like it to Look At, or point to. Once you have designated this object to look at, it will continue to face that object, even if you move it. This is useful if, for instance, you want a camera to follow another object's movements. The Look At parameter points the object in question at the other object's origin.
**Tip:** To designate a centre of interest for the camera that doesn't appear in your scene, create a Null object and disable its display flag. Then Parent the Camera to the newly created Null object, and tell the camera to look at this object using the Look At parameter. You can direct the attention of the camera by moving the Null object with the Select state. If you want to see both the camera and the Null object, enable the Null object's display flag, and use the Select state in an additional Viewport by clicking one of the icons in the top-right corner of the TouchDesigner window.
- Up Vector `upvector` - ⊞ - When orienting an object, the Up Vector is used to determine where the positive Y axis points.
  * X `upvectorx` -
  * Y `upvectory` -
  * Z `upvectorz` -

- Forward Direction `forwarddir` - ⊞ -
  * +X `posx` -
  * -X `negx` -
  * +Y `posy` -
  * -Y `negy` -
  * +Z `posz` -
  * -Z `negz` -

## Parameters - Post Page
The transforms on this page are apllied after the settings made on the Transform page (see above).
- Post Transform Order `postxord` - ⊞ - Set the order in which scale and transform is applied in the post transform.
  * Scale Translate `st` -
  * Translate Scale `ts` -

- Post Translate X `posttx` - ⊞ - Sets the center of the geometry after the Transform page has been applied.
  * Off `off` - No Change.
  * Origin `origin` - Moves the geometry to the origin 0,0,0.
  * Reference Input `reference` - Moves the geometry to a location based on the Reference Input supplied to this SOP's second input (ie. Input 1).

- From Input `fromx` - ⊞ - Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above.
  * Min `min` - Align to the geometry's minimum bounds in this axis.
  * Center `center` - Align to the geometry's center point in this axis.
  * Max `max` - Align to the geometry's maximum bounds in this axis.

- To Reference `tox` - ⊞ - When using Reference Input this determines which part of the Reference Input to align the geometry to.
  * Min `min` - Align to the Reference Input's minimum bounds in this axis.
  * Center `center` - Align to the Reference Input's center in this axis.
  * Max `max` - Align to the Reference Input's maximum bounds in this axis.

- Post Translate Y `postty` - ⊞ - Sets the center of the geometry after the Transform page has been applied.
  * Off `off` - No Change.
  * Origin `origin` - Moves the geometry to the origin 0,0,0.
  * Reference Input `reference` - Moves the geometry to a location based on the Reference Input supplied to this SOP's second input (ie. Input 1).

- From Input `fromy` - ⊞ - Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above.
  * Min `min` - Align to the geometry's minimum bounds in this axis.
  * Center `center` - Align to the geometry's center point in this axis.
  * Max `max` - Align to the geometry's maximum bounds in this axis.

- To Reference `toy` - ⊞ - When using Reference Input this determines which part of the Reference Input to align the geometry to.
  * Min `min` - Align to the Reference Input's minimum bounds in this axis.
  * Center `center` - Align to the Reference Input's center in this axis.
  * Max `max` - Align to the Reference Input's maximum bounds in this axis.

- Post Translate Z `posttz` - ⊞ - Sets the center of the geometry after the Transform page has been applied.
  * Off `off` - No Change.
  * Origin `origin` - Moves the geometry to the origin 0,0,0.
  * Reference Input `reference` - Moves the geometry to a location based on the Reference Input supplied to this SOP's second input (ie. Input 1).

- From Input `fromz` - ⊞ - Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above.
  * Min `min` - Align to the geometry's minimum bounds in this axis.
  * Center `center` - Align to the geometry's center point in this axis.
  * Max `max` - Align to the geometry's maximum bounds in this axis.

- To Reference `toz` - ⊞ - When using Reference Input this determines which part of the Reference Input to align the geometry to.
  * Min `min` - Align to the Reference Input's minimum bounds in this axis.
  * Center `center` - Align to the Reference Input's center in this axis.
  * Max `max` - Align to the Reference Input's maximum bounds in this axis.

- Post Scale `postscale` - ⊞ - Sets the scale of the geometry after the Transform page has been applied.
  * Per Axis `peraxis` - Allows individual settings for each axis using the parameters below.
  * Unity `unity` - Scales the geometry to fit in a 1,1,1 bounding box.
  * Reference `reference` - Scales the geometry to fit the Reference Input's bounding box (second input on this SOP ie. Input 1).

- Post Scale X `postscalex` - ⊞ - Sets the scale of the geometry after the Transform page has been applied to scale.
  * Off `off` - No change the the scale in this axis.
  * Unity `unity` - Scale the geometry to 1.0 (ie. -0.5 to 0.5) in this axis.
  * Reference Input `reference` - Scale the geometry to fit the Reference Input in this axis.
  * Unity Proportional `unityprop` - Scale the geometry to 1.0 (ie. -0.5 to 0.5) in this axis while keeping the input geometry's original proportions.
  * Reference Proportional `referenceprop` - Scale the geometry to fit the Reference Input in this axis while keeping the input geometry's original proportions.

- Post Scale Y `postscaley` - ⊞ - Sets the scale of the geometry after the Transform page has been applied to scale.
  * Off `off` - No change the the scale in this axis.
  * Unity `unity` - Scale the geometry to 1.0 (ie. -0.5 to 0.5) in this axis.
  * Reference Input `reference` - Scale the geometry to fit the Reference Input in this axis.
  * Unity Proportional `unityprop` - Scale the geometry to 1.0 (ie. -0.5 to 0.5) in this axis while keeping the input geometry's original proportions.
  * Reference Proportional `referenceprop` - Scale the geometry to fit the Reference Input in this axis while keeping the input geometry's original proportions.

- Post Scale Z `postscalez` - ⊞ - Sets the scale of the geometry after the Transform page has been applied to scale.
  * Off `off` - No change the the scale in this axis.
  * Unity `unity` - Scale the geometry to 1.0 (ie. -0.5 to 0.5) in this axis.
  * Reference Input `reference` - Scale the geometry to fit the Reference Input in this axis.
  * Unity Proportional `unityprop` - Scale the geometry to 1.0 (ie. -0.5 to 0.5) in this axis while keeping the input geometry's original proportions.
  * Reference Proportional `referenceprop` - Scale the geometry to fit the Reference Input in this axis while keeping the input geometry's original proportions.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Transform SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
