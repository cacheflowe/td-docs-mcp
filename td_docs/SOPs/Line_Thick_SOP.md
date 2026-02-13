---
url: https://docs.derivative.ca/Line_Thick_SOP
category: SOPs
title: Line_Thick_SOP
---

# Line Thick SOP
## Summary

The Line Thick SOP extrudes a surface from a curved line. The line can be of polygon, NURBS, or Bezier geometry type.
[linethickSOP_Class](https://docs.derivative.ca/LinethickSOP_Class "LinethickSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns.
- Start Width `startwidth` - ⊞ - Controls the width of the surface created at the start of the line. Startwidth1 adjusts the width on the inside of the curve, Startwidth2 adjusts the width on the outside of the curve.
  * `startwidth1` -
  * `startwidth2` -

- End Width `endwidth` - ⊞ - Controls the width of the surface created at the end of the line. Endwidth1 adjusts the width on the inside of the curve, Endwidth2 adjusts the width on the outside of the curve.
  * `endwidth1` -
  * `endwidth2` -

- Divisions `divisions` - Number of Divisions (Columns) in the surface geometry created.
- Rows `rows` - Number of Rows in the surface geometry created.
- Domain `domain` - ⊞ - Fraction of the input curve that is used to create the new surface geometry. Domain1 sets position on the curve for Startwidth, Domain2 sets position on the curve for Endwidth.
  * `domain1` -
  * `domain2` -

- Shape `shape` - ⊞ - This menu selects the type of interpolation used between Startwidth and Endwidth.
  * Linear `linear` -
  * Ease In `easein` -
  * Ease Out `easeout` -
  * Ease `ease` -
  * Cubic `cubic` -

- Symmetric `symmetric` - When this is selected, the Endwidth is positioned at the middlepoint on the curve between Domain1 and Domain2. Startwidth is placed at Domain1 and Domain2. The result is a symmetric surface.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Line Thick SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
