---
url: https://docs.derivative.ca/Object_Merge_SOP
category: SOPs
title: Object_Merge_SOP
---

# Object Merge SOP
## Summary

The Object Merge SOP allows you to merge the geometry of several SOPs spanning different components. The SOP data will be baked so that all merged SOPs are relative to each other as if they were located using the transforms of the COMPs they originally came from.
[objectmergeSOP_Class](https://docs.derivative.ca/ObjectmergeSOP_Class "ObjectmergeSOP Class")

## Parameters - Object Merge Page
- Transform Object `xform` - Specify a geometry component to which all the merged geometry should be transformed relative to.
- Merge `merge` - Sequence of SOPs to merge
- SOP `merge0sop` - Each source allows you to specify a pattern of SOP paths. The geometry of each SOP is merged into this SOP. Each SOP can reside in a different component. A pattern can be a complete path to a single SOP or it may consist of wildcards, etc.

## Info CHOP Channels
Extra Information for the Object Merge SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
