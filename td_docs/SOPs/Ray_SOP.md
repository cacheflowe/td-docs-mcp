---
url: https://docs.derivative.ca/Ray_SOP
category: SOPs
title: Ray_SOP
---

# Ray SOP
## Summary

The Ray SOP is used to project one surface onto another. Rays are projected from each point of the input geometry in the direction of its normal. This can be used to drape clothes over surfaces, shrink-wrap one object with another, and other similar effects.
[raySOP_Class](https://docs.derivative.ca/RaySOP_Class "RaySOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Method `method` - ⊞ - Select the method of projection for the Ray SOP.
  * Minimum Distance `minimum` - Points are placed on the closest point on the collision geometry. This method does not use point normals. Use it to shrinkwrap or project one primitve onto another.
  * Project Rays `project` - Points are projected along their normals until intersecting with collision geometry.

- Transform Points `dotrans` - If selected, it will transform the input points as defined below. Leave this off when only interested in updating the source point attributes.
- Intersect Farthest Surface `lookfar` - If selected, this option allows the user to choose between intersecting with the closest intersecting object or the furthest. See example, below.
- Point Intersection Normal `normal` - ⊞ - If selected, updates each point in the source geometry with the normal at the collision surface it intersects with. If the point doesn't intersect at the collision surface, a normal of (0,0,0) is used.
  * Source Normal `source` -
  * Collision Normal `collision` -
  * Reflected Ray `reflect` -

- Bounces `bounces` - The number of times to bounce the ray off of the collision surface before creating the output position. For example, if bounces is set to 1, then the point will be projected onto surface at the first point it hits. If set to 2, the ray will be re-projected off of that first surface as if it was reflected, or bounced and will then be projected onto the next surface the ray hits. See the second Ray snippet for an example.
- Save Bounce Geometry `bouncegeo` - When enabled, the projected geometry will be saved each time the projected ray bounces off a surface resulting in multiple copies of the input geometry. See the second Ray snippet for an example.
- Point Intersection Distance `putdist` - If selected, updates each point intersected with the distance to the collision surface. If the point doesn't intersect at the collision surface a distance of 0 is used. This value is placed in the `$DIST` point attribute, accessible from the [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP").
- Scale `scale` - A value of zero will leave the input point unaffected. A value of one will land the point on the intersection surface. Negative values and values > 1 are also valid.
- Lift `lift` - This value further offsets the surface input by offsetting it in the direction of its normal.
- Sample `sample` - This value determines the number of rays sent per point. If greater than one, the remaining rays are perturbed randomly, and averaged.
- Jitter Scale `jitter` - Controls the perturbation of the extra sample rays.
- Seed `seed` - Allows a different random sequence at higher sampling rates.
- Create Point Group `newgrp` - If selected, it will create a point group containing all the points which were intersected successfully.
- Ray Hit Group `hitgrp` - Specifies the name of the above point group.

## Example
  1. Place a [Grid SOP](https://docs.derivative.ca/Grid_SOP "Grid SOP") and translate it in TZ by 2.5. Turn it's template flag on.
  2. Append a Point SOP to the Grid and enable the Create Point Normals option.
  3. Place a NURBS Sphere with a Radius of 2,2,2 and translate it in Z by -2.5 .
  4. Display point normals by enabling the option in the Viewport > Display Options.
  5. Append a Ray SOP to the Point SOP and connect the Sphere to the right input. Make it the display SOP.
  6. Toggle the Intersect Farthest Surface button on and off.

The Ray SOP will move the points of the Grid in the direction of the point normals. The first surface of the Collision Source (right input) will be where those points of the grid will rest. You can make those points rest on the other side of the sphere by enabling the Intersect Farthest Surface option. This means that the points should continue to project to the farthest surface of the collision source.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Ray SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
