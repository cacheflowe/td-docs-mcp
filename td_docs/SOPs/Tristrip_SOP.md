---
url: https://docs.derivative.ca/Tristrip_SOP
category: SOPs
title: Tristrip_SOP
---

# Tristrip SOP
## Summary

The Tristrip SOP convert geometry into triangle strips. Triangle strips are faster to render than regular triangles or quads.
[tristripSOP_Class](https://docs.derivative.ca/TristripSOP_Class "TristripSOP Class")

## Parameters - Page
- Source Group `group` - Specify a group of primitive to convert to tristrips. If no group is specified, then the entire geometry will be converted.
- Constrain Strip Length `constrainstriplength` - When checked on, the length (number of triangles) of the tristrips can be constrained to a maximum using the Maximum Strip Length parameter below.
- Maximum Strip Length `maxstriplength` - Set the maximum number of triangles in each tristrip.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Tristrip SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
