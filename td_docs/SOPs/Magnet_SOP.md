---
url: https://docs.derivative.ca/Magnet_SOP
category: SOPs
title: Magnet_SOP
---

# Magnet SOP
## Summary

The Magnet SOP allows you to affect deformations of the input geometry with another object using a "magnetic field" of influence, defined by a metaball field. It allows the creation of animated bumps and dents within objects, and other special effects.
It is important to note that the actual deformation comes from the Translate parameters of the Magnet SOP, and not from the metaball. The metaball defines the area of effect for the Translate parameters of the Magnet SOP. The weight of the metaball determines the effectiveness of the Translate within the Magnet SOP.
The power of the magnet is greatest at the centre of a metaball field and diminishes to nothing at the edge of the field.
[magnetSOP_Class](https://docs.derivative.ca/MagnetSOP_Class "MagnetSOP Class")

## Parameters - Page
- Deform Group `deformgrp` - Allows you to specify a group of geometry to be deformed, and a group that will act as the magnet respectively. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Magnet Group `magnetgrp` - Allows you to specify a group of geometry to be deformed, and a group that will act as the magnet respectively. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").

## Parameters - Deform Page
- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the order of the rotations within the overall transform order.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - These three fields move the Source geometry in the three axes. The Translates of the metaball only affect the position of the area of influence. The influence itself is provided by an imaginary magnet within the Magnet SOP itself, and the attitude of this influence is determined by the Translates of the Magnet SOP.
**Note:** If the **Translate** values of the Magnet SOP are all zero, the magnet will have no deforming influence. The weight of the [Metaball SOP](https://docs.derivative.ca/Metaball_SOP "Metaball SOP") scales the influence of the Magnet SOP's Translates.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the Source geometry in the three axes.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - These three fields scale the input geometry in the three axes.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - The pivot point for the transformations. Not the same as the pivot point in the pivot channels.
  * X `px` -
  * Y `py` -
  * Z `pz` -

## Parameters - Attributes Page
- Affect Position `position` - Allow the magnet to affect the position of the input geometry. This is enabled by default.
- Affect Point Color `color` - Allow the magnet to affect the point color of the input geometry.
**Tip:** To control the contribution of each magnet on the surface's Point Color when the **Affect Point Color** option is enabled, set your point colors to black (0,0,0) before the Magnet SOP by using a [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"). The Translate fields in the Magnet SOP will then add per-point rgb color with values of 2,2,2 approaching white.
The scale and rotate channels of the magnet move you about in 3D color space. This is not recommended.
- Affect Point Normal `nml` - Allow the magnet to affect the point normals of the input geometry.
- Affect Point Velocity `velocity` - Allow the magnet to affect the velocity of the input geometry.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Magnet SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
