---
url: https://docs.derivative.ca/Joint_SOP
category: SOPs
title: Joint_SOP
---

# Joint SOP
## Summary

The Joint SOP will aid in the creation of circle-based skeletons by creating a series of circles between each pair of input circles. This SOP requires at least a pair of circles in order to work correctly.
[jointSOP_Class](https://docs.derivative.ca/JointSOP_Class "JointSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field causes the SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Divisions `divs` - Allows you to specify the number of circles between each pair of input circles.
- Preserve First Input `preserve1` - Preserves the first input circle being fed into the SOP.
- Preserve Last Input `preserve2` - Preserves the last input circle.
- Orient Circles `orient` - This helps to create a joint that blends between the input circles without flattening or curving outwards. In order to do this, there may be a reversal of the normal of each input circle. For example, if the normals of the two input circles are facing away from each other, the joint created (if this option was not enabled) would appear to connect the circles the long way around. This option would reorient the joint such that the shorter distance is used to create the joint.
- Smooth Path `smoothpath` - If not on, the joint circles are blended linearly. Otherwise, they are placed along a cubic piece-wise Bzier curve between the circle centres. This is useful when the input contains more than two circles and the joints must be continuous to each other. If this option isn't enabled, the interpolation may be sharper than desired.
- Smooth Twist `smoothtwist` - Each joint circle is rotated slightly such that its X and Y axis align as it approaches an input circle. This toggle causes the adjustments to be an incremental, or piece-wise, Bzier function. Again this is useful for multi-circle inputs.
- Align Major Axes `majoraxes` - If enabled, this option aligns the first circle's largest axis to the last circle's largest axis. If disabled, the first and last circles' x axes are aligned. This option can help minimize the twist in the joint ellipses between bones.
- Minimum Twist `mintwist` - If on, the rotations of the added circles are calculated such that they never rotate further than one half turn in either direction. This leads to a visually continuous layout suitable for creating a skeleton, but will cause problems if the circles are later skinned since the beginnings of each circle may no longer be continuously aligned.
- LR Scale `lrscale` - ⊞ - These parameters control the shape of the smooth path, varying the shape of the implied curve from the left or right. If the Orient Circles option is on, the sign of the scale has no effect. For a discussion of the relative terms right and left, see [Align SOP](https://docs.derivative.ca/Align_SOP "Align SOP").
  * `lrscale1` -
  * `lrscale2` -

- LR Offset `lroffset` - ⊞ - These parameters allow you to override the distance between circles, thereby affecting the shape of the joint.
  * `lroffset1` -
  * `lroffset2` -

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Joint SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
