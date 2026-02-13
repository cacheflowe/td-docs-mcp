---
url: https://docs.derivative.ca/Align_SOP
category: SOPs
title: Align_SOP
---

# Align SOP
## Summary

The Align SOP aligns a group of primitives to each other or to an auxiliary input, by translating or rotating each primitive along any pivot point.
**Left and Right Primitives** - The notions of "left" and "right" which follow depend on context. If an auxiliary input is used, it is always the right primitive and the primary input geometry are all left primitives. If only one input is used, then for each pair being aligned, there is a left and a right primitive. This means that relative to neighbouring primitives, one primitive can be both left and right.
[![TouchGeometry72.gif](https://docs.derivative.ca/images/2/25/TouchGeometry72.gif)](https://docs.derivative.ca/File:TouchGeometry72.gif)
[alignSOP_Class](https://docs.derivative.ca/AlignSOP_Class "AlignSOP Class")

## Parameters - Page
- Group `group` - A subset of primitives to align (accepts patterns, as described in Pattern Matching in the [Scripting Guide](http://www.derivativeinc.com/Tools/Touch000/Manual/Guides/ScriptingGuide/ScriptingGuide.pdf)). If blank, it aligns the entire input.
- Align `align` - ⊞ - Can optionally align subgroups of _n_ primitives or every _n_ th primitive in a cyclical manner.
  * All Primitives `all` -
  * Groups of N Primitives `group` -
  * Skip Every Nth Primitive `skip` -

- N `inc` - Determines the number of primitives to be either grouped or skipped.
Example: Assume there are six primitives numbered for 0 - 5, and N = 2. Then:
**a)**
**b)**

## Parameters - Align Page
- Bias `bias` - Determines which primitive remains unaffected: 0 Left, 1 Right.
- Left UV `leftuv` - ⊞ - Pivot Location for each "left" primitive.
  * U `leftuv1` -
  * V `leftuv2` -

- Right UV `rightuv` - ⊞ - Pivot location for each "right" primitive.
  * U `rightuv1` -
  * V `rightuv2` -

- Right UV End `rightuvend` - ⊞ - If an auxiliary input is used, this location specifies an end point for the alignment. Left primitives are then distributed uniformly between the `Right UV` and the `Right UV End`.
  * U `rightuvend1` -
  * V `rightuvend2` -

- Individual Alignment `individual` - Causes each primitive of the input to be aligned. If unchecked, only the first primitive is aligned and all others are placed relative to it, preserving the spatial layout of the left primitives.
- Translate `dotrans` - When enabled, translates primitives during alignment by translating the left UV position to the right UV position.
- Rotate `dorotate` - When enabled, rotates primitives during alignment by aligning the left UV tangents (at the left UV position) to the right UV tangents (at the right UV position).

## Parameters - Transform Page
- Transform Order `xord` - ⊞ - Sets the overall transform and rotation order for the transformations. The transform and rotation order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the overall transform and rotation order for the transformations. The transform and rotation order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - Allows you to perform a post-alignment transformation. Specify the amount of translation about the local `xyz` axes.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - Allows you to perform a post-alignment transformation. Specify the amount of rotation about the local `xyz` axes.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - Allows you to perform a post-alignment transformation. Specify the amount of scaling about the local `xyz` axes.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - Allows you to perform a post-alignment transformation. Specify the amount of translation / rotation / scaling about the local `xyz` axes
  * X `px` -
  * Y `py` -
  * Z `pz` -

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Align SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
