---
url: https://docs.derivative.ca/Fractal_SOP
category: SOPs
title: Fractal_SOP
---

# Fractal SOP
## Summary

The Fractal SOP allows you created jagged mountain-like divisions of the input geometry. It will create random-looking deviations and sub-divisions along either a specified normal vector (the Direction xyz fields) or the vertex normals of the input geometry. This is great for the creation of terrains and landscapes.
[fractalSOP_Class](https://docs.derivative.ca/FractalSOP_Class "FractalSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Divisions `divs` - The number of subdivisions of the input geometry. Values in the range of 1 - 3 are reasonable to start with. Higher values cause excessive geometry and should be used with caution.
- Smoothness `smooth` - The smoothness value scales the deviations. The range is usually between 0 and 1, and small numbers create larger deviations than large numbers. Smoothness and Scale have a similar effect, but there is a subtle difference. Smoothness is calculated for each iteration of the SOP. The number of Iterations is, in turn set by the number of Divisions. Scale, by contrast, is a global scaling of the amplitude of the deviations, with no consideration of the stage at which they are created. Using low values of smoothness (producing large deviations) and a small scale value will give a slightly more random looking result than doing the opposite; high roughness values (small deviations) and large scale values, providing Divisions is greater than 1.
- Scale `scale` - Global setting of the fractal divisions. See the above discussion about Smoothness vs. Scale.
- Seed `seed` - The random seed used for fractalising. Specifying a different integer value gives a different shape.
- Fixed Boundary `fixed` - When enabled, this option prevents Fractal from applying any deviations to the edges (boundaries) so that you could, for example, fractalise a plane and still be able to connect the edges of the plane to the sides of the box. This is achieved by first refining the surface between all breakpoints, and then fractalized.
- Use Vertex Normals `vtxnms` - Instead of using the Direction fields below, this sets the direction of the fractalisation at any given point to be the direction of the vertex normals of the input. This may be preferable when using a sphere or other rounded object as the input, as the deviations will originate from the center of the sphere instead of all being the same direction.
- Direction `dir` - ⊞ - The direction of the Fractalisation. The default values of `0, 0, 1` make the fractal deviations point in the Z direction. Can be overridden by: Use Vertex Normals.
  * X `dirx` -
  * Y `diry` -
  * Z `dirz` -

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Fractal SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
