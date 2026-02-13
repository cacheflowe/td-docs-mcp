---
url: https://docs.derivative.ca/Stitch_SOP
category: SOPs
title: Stitch_SOP
---

# Stitch SOP
## Summary

The Stitch SOP is used to stretch two curves or surfaces to cover a smooth area. It can also be used to create certain types of upholstered fabrics such as cushions and parachutes.
If a second input is given, it must contain one surface that the primitives in the first input can stitch to. The left input can contain either faces or surfaces; in either case, each primitive in the first input is stitched to a parametric area of the surface in the second input in such a way that the parametric area allocated to each primitive is the same and the size of all areas added together equals the parametric range specified in the R Width (see below).
Please refer to the [Align SOP](https://docs.derivative.ca/Align_SOP "Align SOP") for a discussion of "left" and "right" primitives as well as the option of an auxiliary input.
[stitchSOP_Class](https://docs.derivative.ca/StitchSOP_Class "StitchSOP Class")

## Parameters - Page
- Group `group` - Which primitives to stitch. If blank, it stitches the entire input. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Stitch `stitchop` - ⊞ - Stitches sub-groups of n primitives or patterns of primitives.
  * All Primitives `all` -
  * Groups of N Primitives `group` -
  * Skip Every Nth Primitive `skip` -

- N `inc` - The value entered for N determines the pattern of primitives stitched.
- Wrap Last to First `loop` - If enabled, it connects the beginning of the first primitive in the left input to the end of the last primitive in the same input. If only one primitive exists, its ends will be stitched together.
- Direction `dir` - ⊞ - Allows stitching along either the U or V parametric direction.
  * in U `ujoin` -
  * in V `vjoin` -

- Tolerance `tolerance` - This parameter minimizes modification to the input sources. A smaller value creates less modification.
- Bias `bias` - Determines which primitive remains unaffected. The values go from `0 - 1`, where `0` - first, and `1` - last.
- Left UV `leftuv` - ⊞ - Point on each left / right primitive at which to begin / end the stitch.
  * `leftuv1` -
  * `leftuv2` -

- Right UV `rightuv` - ⊞ - Point on each left / right primitive at which to begin / end the stitch.
  * `rightuv1` -
  * `rightuv2` -

- LR Width `lrwidth` - ⊞ - The first value represents the width of the left stitch. The second value represents the width of the right stitch.
  * `lrwidth1` -
  * `lrwidth2` -

- Stitch `dostitch` - If selected, move a single row from each primitive to coincide.
- Tangent `dotangent` - If selected, modifies neighbouring rows on each primitive to create identical slopes at the given rows.
- Sharp Partials `sharp` - If selected, creates sharp corners at the ends of the stitch when the stitch partially spans a primitive.
- Fixed Intersection `fixed` - When the tangent option is on, this option allows some flexibility as to which side of each slope is modified.
- LR Scale `lrscale` - ⊞ - Use this parameter to control the direction and position of the tangential slopes.
  * `lrscale1` -
  * `lrscale2` -

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Stitch SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
