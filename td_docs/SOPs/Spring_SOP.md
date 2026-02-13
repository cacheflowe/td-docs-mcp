---
url: https://docs.derivative.ca/Spring_SOP
category: SOPs
title: Spring_SOP
---

# Spring SOP
## Summary

The Spring SOP deforms and moves the input geometry using spring "forces" on the edges of polygons and on masses attached to each point.
Geometry is deformed using forces that simulate simple physics on the points and edges. A simulated "mass" is assigned to each point. Its primitive edges act as "springs" which oppose the forces, and pull the points back toward their original positions. When the springs are stretched by the forces, they try to pull the points back. The points do not stop moving when they return to their original positions, however, but continue to oscillate because of their mass, until the oscillation dies out.
Forces which act upon the points are as follows:      external force (gravity)     wind (similar to external force)     turbulence (chaotic forces)
The greater the drag value, or smaller the mass, the faster the oscillation dies out.
[springSOP_Class](https://docs.derivative.ca/SpringSOP_Class "SpringSOP Class")

## Parameters - State Page
- Preroll Time `timepreroll` - How many seconds of the simulation to bypass, after the reset time is reached. For example, if you put the number 33 into this field (and reset is at `$TSTART`), frame one will show the simulation that was at a time of 33 seconds. In other words, the first thirty-two seconds have been bypassed, and the time at thirty-three seconds is shifted to frame one. The first thirty-two seconds must still be calculated in order to compute the status of the points, so you will notice some delay upon reset.
- Time Inc `timeinc` - The Time Inc parameter determines how often to cook the SOP. By default, this parameter is set to `1/$FPS`. This means that the SOP will cook once for every frame. When complex dynamics are involved, the SOP may require more frequent cooking for increased mathematical accuracy. To get sub-frame accuracy in the cooking, set the Time Inc to something smaller than `1/$FPS` . For example, setting the Time Inc to `0.5/$FPS` will mean that the SOP gets cooked twice for every frame.
**Note:** Never set this parameter greater than `1/$FPS`.
- Accurate Moves `accurate` - This option makes the nodes move more accurately between frames by calculating their trajectories for fractional frame values.
- Attractor Use `attractmode` - ⊞ - Describes how attractor points are assigned to each particle.
  * All Points `all` - All point attractors affect all particles (or points).
  * Single Point per Particle `single` - When enabled, each particle is assigned a single attractor point, and is affected by only that point. Assignment is done by point number modulo the total number of attractor points.

- Reset `reset` - While On resets the spring effect of the SOP.
- Reset Pulse `resetpulse` - Instantly reset the spring effect.

## Parameters - Forces Page
- External Force `external` - ⊞ - Forces of gravity acting on the points. When drag is zero, the points can accelerate with no limit on their speed.
  * X `externalx` -
  * Y `externaly` -
  * Z `externalz` -

- Wind `wind` - ⊞ - Wind forces acting on the points. Similar to external force. Using wind (and no other forces, such as turbulence), the points will not exceed the wind velocity.
  * X `windx` -
  * Y `windy` -
  * Z `windz` -

- Turbulence `turb` - ⊞ - The amplitude of turbulent (chaotic) forces along each axis. Use positive values, if any.
  * X `turbx` -
  * Y `turby` -
  * Z `turbz` -

- Turb Period `period` - A small period means that the turbulence varies quickly over a small area, while a larger value will cause points close to each other to be affected similarly.
- Seed `seed` - Random number seed for the simulation.

## Parameters - Nodes Page
- Fixed Points `fixed` - This is a point group. All points in the point group will remain unaffected by the forces. Also see the [Group SOP](https://docs.derivative.ca/Group_SOP "Group SOP") for notes on how to specify point ranges.
- Fixed Points go to Source Positions `revertfixed` - Determines whether or not points in the Fixed Points group should be moved to the positions of the corresponding points in the Source geometry.
- Copy Groups from Source `copygroups` - Determines if the Spring SOP should copy groups from the Source geometry at each frame. This lets you specify the name of an animating group in the Fixed Points field, and the contents of this group will be kept up to date.
- Add Mass Attribute `domass` - When selected, the Mass is computed for the deforming geometry.
- Mass `mass` - Mass of each point. Heavier points take longer to get into motion, and longer to stop.
- Add Drag Attribute `dodrag` - When selected, the geometry is deformed by the Drag attribute.
- Drag `drag` - Drag of each point.
- Spring Behavior `springbehavior` - ⊞ - How the springs will behave:
  * Hooke's Law `hooke` - Springs will work according to Hooke's Law. This is generally more stable than Normalized Displacement.

     **Hooke's Law** : Force = Displacement Spring constant
  * Normalize Displacement `normalize` - Similar to Hooke's Law except that the displacement is normalized to the original length of the Spring.

- Spring Constant `springk` - The spring constant. How tight the springs are. Increase this value to make the springs tighter and thus make the object more rigid. As this number becomes higher, the springs can oscillate out of control. Decrease the Time Inc if this happens.
- Initial Tension `tension` - The Initial k constant of the geometry before being deformed by the spring operation.

## Parameters - Limits Page
+ Limit Plane `limitpos` - ⊞ - The points will bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are one thousand units away, which is very large. Reduce the values to about one to see the effect.
  * X `limitposx` -
  * Y `limitposy` -
  * Z `limitposz` -

- Limit Plane `limitneg` - ⊞ - The points will bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are one thousand units away, which is very large. Reduce the values to about one to see the effect.
  * X `limitnegx` -
  * Y `limitnegy` -
  * Z `limitnegz` -

- Hit Behavior `hit` - ⊞ - Control over what happens when the geometry hits either the six collision planes or the collision object. The options are:
  * Bounce on Contact `bounce` - Geometry will bounce upon contact with the Collision input.
  * Stick on Contact `stick` - Geometry will stick to the Collision input upon contact.

- Gain Tangent `gaintan` - Friction parameters which can be regarded as energy-loss upon collision. The first parameter affects the energy loss (gain) perpendicular to the surface. 0 means all energy (velocity) is lost, 1 means no energy is lost perpendicular to surface. The second parameter is the energy gain tangent to the surface.
- Gain Normal `gainnorm` - Friction parameters which can be regarded as energy-loss upon collision. The first parameter affects the energy loss (gain) perpendicular to the surface. 0 means all energy (velocity) is lost, 1 means no energy is lost perpendicular to surface. The second parameter is the energy gain tangent to the surface.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Spring SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
