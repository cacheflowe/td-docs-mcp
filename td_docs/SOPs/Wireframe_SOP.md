---
url: https://docs.derivative.ca/Wireframe_SOP
category: SOPs
title: Wireframe_SOP
---

# Wireframe SOP
## Summary

The Wireframe SOP converts edges to tubes and points to spheres, creating the look of a wire frame structure in renderings. This is ideal for modelling tube structures and pipes.
[wireframeSOP_Class](https://docs.derivative.ca/WireframeSOP_Class "WireframeSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Wire Radius `radius` - Radius of the individual wires used in the construction of the geometry.
- Round Corners `corners` - When selected, rounds the corners by placing spheres at the point locations with the same radius as the wires.
- End Caps `caps` - When selected, places end-caps on all wire geometry.
- Remove Polygons `remove` - Removes the polygons from the output geometry, leaving only the converted line structures.
- Fast Wire `fast` - Faster wire calculation at the expense of accuracy.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Wireframe SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
