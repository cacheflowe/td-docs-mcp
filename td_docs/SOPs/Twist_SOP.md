---
url: https://docs.derivative.ca/Twist_SOP
category: SOPs
title: Twist_SOP
---

# Twist SOP
## Summary

The Twist SOP performs non-linear deformations such as bend, linear taper, shear, squash and stretch, taper and twist. Each deformation will distort the object in one or more axes.
[twistSOP_Class](https://docs.derivative.ca/TwistSOP_Class "TwistSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Operation `op` - ⊞ - This menu allows you to select a type of non-linear deformation. Select from the following options:
  * Twist `twist` - Rotates the input geometry around the Primary Axis.
  * Bend `bend` - Bends the input geometry about the Primary Axis while keeping points on the Secondary Axis stationary.
  * Shear `shear` - Shears the input geometry along the Secondary Axis while looking down the Primary Axis.
  * Taper `taper` - Tapers the input geometry along the Secondary Axis while looking down the Primary Axis.
  * Linear Taper `ltaper` - Tapers the input geometry as with the Taper option; however, only the edges remain straight through the Taper operation.
  * Squash & Stretch `squash` - Traditional animator's bounce tools.

- Primary Axis `paxis` - ⊞ - These menus allows you to select the primary and secondary axes for the deformation. The selected deformation will first occur in the Primary Axis and then the Secondary Axis.
  * X Axis `x` - This field allows you to choose the origin of the deformation.
  * Y Axis `y` - This field allows you to choose the origin of the deformation.
  * Z Axis `z` - This field allows you to choose the origin of the deformation.

- Secondary Axis `saxis` - ⊞ - These menus allows you to select the primary and secondary axes for the deformation. The selected deformation will first occur in the Primary Axis and then the Secondary Axis.
  * X Axis `x` - This field allows you to choose the origin of the deformation.
  * Y Axis `y` - This field allows you to choose the origin of the deformation.
  * Z Axis `z` - This field allows you to choose the origin of the deformation.

- Pivot `p` - ⊞ - This field allows you to choose the origin of the deformation.
  * X `px` -
  * Y `py` -
  * Z `pz` -

- Strength `strength` - The Strength of the effect being applied. The Rolloff determines an accentuation of the effect being applied. When you are using different types of transformations this Strength / Roll will have different effects:
  * Bend - Strength and Roll are used to control the extremities of the geometry (try a value of 0.5).
  * Twist - Strength and Roll are used to affect the twist amount based on the distance.
  * Shear - Strength and Roll are used to affect the shear amount based on distance.
  * Taper - Strength and Roll are used to affect the direction of the bow (inwards vs. outwards).
  * Linear Taper - Strength and Roll have no effect for this option.
  * Squash and Stretch - Strength and Roll are used to maintain the apparent volume of the source geometry.

- Typically, Rolloff should equal `1` - which spreads the effect evenly (although not being limited to) across the bounds of the geometry. Values higher than `1` iterate the effect multiple times through the same range. If Rolloff equals `0`, then the effect may be localised to a small segment at the centre of the deformed geometry and Strength may not appear to work properly.
**Note:** To be certain to see the effects of the Twist SOP, make sure you have enough divisions along the edges. By using a centre that is different from that of the object you can improve your control of the object. Try moving the pivot point to the bottom of an object that you are squashing and stretching.
- Rolloff `roll` - The Strength of the effect being applied. The Rolloff determines an accentuation of the effect being applied. When you are using different types of transformations this Strength / Roll will have different effects:
  * Bend - Strength and Roll are used to control the extremities of the geometry (try a value of 0.5).
  * Twist - Strength and Roll are used to affect the twist amount based on the distance.
  * Shear - Strength and Roll are used to affect the shear amount based on distance.
  * Taper - Strength and Roll are used to affect the direction of the bow (inwards vs. outwards).
  * Linear Taper - Strength and Roll have no effect for this option.
  * Squash and Stretch - Strength and Roll are used to maintain the apparent volume of the source geometry.

- Typically, Rolloff should equal `1` - which spreads the effect evenly (although not being limited to) across the bounds of the geometry. Values higher than `1` iterate the effect multiple times through the same range. If Rolloff equals `0`, then the effect may be localised to a small segment at the centre of the deformed geometry and Strength may not appear to work properly.
**Note:** To be certain to see the effects of the Twist SOP, make sure you have enough divisions along the edges. By using a centre that is different from that of the object you can improve your control of the object. Try moving the pivot point to the bottom of an object that you are squashing and stretching.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Twist SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
