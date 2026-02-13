---
url: https://docs.derivative.ca/Oculus_Rift_SOP
category: SOPs
title: Oculus_Rift_SOP
---

# Oculus Rift SOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

Loads geometry for the Oculus Rift Touch controllers.
[oculusriftSOP_Class](https://docs.derivative.ca/OculusriftSOP_Class "OculusriftSOP Class")

## Parameters - Page
- Model `model` - ⊞ - Select which controller model to load.
  * Left Controller `leftcontroller` -
  * Right Controller `rightcontroller` -

## Info CHOP Channels
Extra Information for the Oculus Rift SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
