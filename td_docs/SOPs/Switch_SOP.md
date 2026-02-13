---
url: https://docs.derivative.ca/Switch_SOP
category: SOPs
title: Switch_SOP
---

# Switch SOP
## Summary

The Switch SOP switches between up to 9999 possible inputs. The output of this SOP is specified by the Select Input field. This is useful for switching the output between several inputs depending on the evaluation of an expression placed in the Select Input field.
[switchSOP_Class](https://docs.derivative.ca/SwitchSOP_Class "SwitchSOP Class")

## Parameters - Page
- Select Input `input` - The index of the source to use, where the first source is 0, the second 1, and so on.
- Extend `extend` - ⊞ - Determines extend behaviour when index is out of range. Allows negative indices.
  * Clamp `clamp` -
  * Loop `loop` -
  * ZigZag `zigzag` -

## Example
Below are two expressions that could be entered in the Select Input field:
  * `me.time.frame - 1` - The first input is selected at frame 1, the second at frame 2, etc.
  * `me.time.frame > 5` - The first input is selected for the first five frames, then the second for the remaining frames.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Switch SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
