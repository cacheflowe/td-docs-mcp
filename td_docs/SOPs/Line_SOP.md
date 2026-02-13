---
url: https://docs.derivative.ca/Line_SOP
category: SOPs
title: Line_SOP
---

# Line SOP
## Summary

The Line SOP creates straight lines.
[lineSOP_Class](https://docs.derivative.ca/LineSOP_Class "LineSOP Class")

## Parameters - Page
- Point A `pa` - ⊞ - These X,Y, and Z values set the position of the beginning of the line.
  * X `pax` -
  * Y `pay` -
  * Z `paz` -

- Point B `pb` - ⊞ - These X,Y, and Z values set the position of the end of the line.
  * X `pbx` -
  * Y `pby` -
  * Z `pbz` -

- Number of Points `points` - The number of points the line is made of. Minimum is 2 points.
- Texture Coordinates `texture` - ⊞ - Texture adds (0,1) coordinates to the vertices when set to Unit. Creates a rectangle without uv attributes when set to Off.
  * Off `off` -
  * Unit `unit` -

## Info CHOP Channels
Extra Information for the Line SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
