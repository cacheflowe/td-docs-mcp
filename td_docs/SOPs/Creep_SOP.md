---
url: https://docs.derivative.ca/Creep_SOP
category: SOPs
title: Creep_SOP
---

# Creep SOP
## Summary

The Creep SOP lets you deform and animate Source Input (input0) geometry along the surface of the Path Input (input1) geometry.
[creepSOP_Class](https://docs.derivative.ca/CreepSOP_Class "CreepSOP Class")

## Parameters - Page
- Reset `reset` - Reset's the creep state based on Reset Method parameter below.
- Reset Method `resetmethod` - ⊞ - The Source Input is Translated, Rotated and Scaled so as to complete the given options listed below.
  * Fill path `fillpath` - Values are computed that stretch or shrink the input geometry to the full length and width of the Path Input geometry. These values are placed in the nine transform fields at the bottom of the SOP.
  * Keep proportions `keepproportions` - Similar to above, but the values are initialized so as to minimize distortion of object geometry.

###
## Note
The below three transform fields set the translation of the input geometry along the rows (U) and columns (V) of the Path. A creep translate of `0.5, -0.5, 1` puts the source in the middle of the path, one unit away from it. For scaling, a source of 0.2 0.3 in size will span 20% of the columns, and 30% of the rows on the Path.

Translate `t` - ⊞ - Translate the Source Input Creep geometry on the surface of the Path Input.
  * X `tx` - Translate the Source Input along the Path Input's U parameter

  * Y `ty` - Translate the Source Input along the Path Input's V parameter

  * Z `tz` - Translate the Source Input along the Path Input's W parameter (elevation above/below Path)

Rotate `r` - ⊞ - Rotate the Source Input creep geometry on the surface of the Path Input.
  * X `rx` - Rotate the Source Input along the Path Input's U parameter

  * Y `ry` - Rotate the Source Input along the Path Input's V parameter

  * Z `rz` - Rotate the Source Input along the Path Input's W parameter

Scale `s` - ⊞ - Scale the Source Input creep geometry on the surface of the Path Input.
  * X `sx` -

  * Y `sy` -

  * Z `sz` -

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Creep SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
