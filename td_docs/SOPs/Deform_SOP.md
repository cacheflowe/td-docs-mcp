---
url: https://docs.derivative.ca/Deform_SOP
category: SOPs
title: Deform_SOP
---

# Deform SOP
## Summary

The Deform SOP takes geometry along with point weights (assigned by the [Capture SOP](https://docs.derivative.ca/Capture_SOP "Capture SOP")) and deforms geometry as Capture Regions are moved. This gives you the flexibility to procedurally modify geometry between the Capture and Deform SOPs.
See also [Deforming Geometry (Skinning)](https://docs.derivative.ca/Deforming_Geometry_\(Skinning\) "Deforming Geometry \(Skinning\)").
[deformSOP_Class](https://docs.derivative.ca/DeformSOP_Class "DeformSOP Class")

## Parameters - Page
- Group `group` - Optional point and/or primitive group to be deformed. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Delete Capture Attributes `delcaptatr` - The point capture attributes can significantly increase the memory usage of the geometry. This option will delete the point capture attributes after it deforms the geometry in order to save memory for any subsequent SOPs.
- Delete Point Colors `delcolatr` - You may find that you are using point coloring from the Capture SOP to assist in the capturing process. If you do not need these point colors after the Deform SOP, you can turn this parameter on to delete the colors.
- Deform Normals `donormal` - Turn this on to deform the normals as the geometry deforms.
- Skeleton Root Path `skelrootpath` - Specify the path to the root of the skeleton.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Deform SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
