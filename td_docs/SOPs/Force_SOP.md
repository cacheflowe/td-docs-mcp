---
url: https://docs.derivative.ca/Force_SOP
category: SOPs
title: Force_SOP
---

# Force SOP
## Summary

The Force SOP adds force attributes to the input metaball field that is used by either [Particle SOP](https://docs.derivative.ca/Particle_SOP "Particle SOP") or [Spring SOP](https://docs.derivative.ca/Spring_SOP "Spring SOP") as attractor or repulsion force fields. In general, force values greater than 0 cause points to be attracted, less than 0 cause points to be repelled.
[forceSOP_Class](https://docs.derivative.ca/ForceSOP_Class "ForceSOP Class")

## Parameters - Page
- Radial Force `doradial` - When checked, triggers a force towards or away from the centre of the metaball field, depending on the value of the force.
- Force `radial` - When Radial Force is checked, this controls the strength of the Radial Force field.
- Directional Force `doaxis` - When checked, enables all parameters below to allow control of specific force attributes.
- Direction `dir` - ⊞ - When Directional Force is checked, determines the direction vector axis, and activates forces along the directional vector for the directional forces below.
  * X `dirx` -
  * Y `diry` -
  * Z `dirz` -

- Axial Force `axial` - When Directional Force is checked, controls the force along the primary axis. Increasing this value will cause the particles to move up the primary axis of the metaball field as defined by the direction vector.
- Vortex Force `vortex` - When Directional Force is checked, this field controls the amount of twist particles are given around the primary axis. Positive values cause the particles to spin clockwise, negative values cause counter-clockwise spins. It is a centrifugal force.
- Spiral Force `spiral` - Controls the attraction/repulsion force perpendicular to the primary axis (Direction field). Values greater than 0 will cause the points to be drawn toward the primary axis. Values less than 0 push particles away perpendicular to the primary axis. It is a tangential force.

Tips
To view the metaball field of influence, turn on the hulls display of the input metaball/s object/s. Both the [Particle SOP](https://docs.derivative.ca/Particle_SOP "Particle SOP") and [Spring SOP](https://docs.derivative.ca/Spring_SOP "Spring SOP") will display these hulls as guide geometry.
Adjust the weights of the metaball inputs to increase or decrease the field effect within the metaball field of influence.
In general, it is a good idea to try and keep the scale of forces and force fields to a smaller rather than a larger scale. This tends to make particle movement and attraction more manageable and realistic.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Force SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
