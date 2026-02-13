---
url: https://docs.derivative.ca/Sprinkle_SOP
category: SOPs
title: Sprinkle_SOP
---

# Sprinkle SOP
## Summary

The Sprinkle SOP is used to add [points](https://docs.derivative.ca/Point_Class "Point Class") to either the surface or the volume of a SOP. You can create points on a surface, or within a closed volume based on the Method menu. The Surface method keeps the distribution of points constant per unit area of surface, whereas Per-Primitive gives each primitive, usually triangles, a constant number per primitive no matter their size.
The second input is used when you are scattering on a deforming surface. You generally don't want the distribution of points to jump while deforming, so you give the deformed surface as second input and the un-deformed surface as the first input. The Sprinkle SOP will then distribute points on the un-deformed surface, and then put them on their equivalent place on the deformed surface.
[sprinkleSOP_Class](https://docs.derivative.ca/SprinkleSOP_Class "SprinkleSOP Class")

## Parameters - Sprinkle Page
- Seed `seed` - Any number, integer or non-integer, which starts the random number generator. Each number gives completely different point positions.
- Method `method` - ⊞ - Describes where points are located.
  * Surface `surface` - Points are evenly distributed along the entire surface of the geometry. That is, smaller polygons receives fewer points on average than larger polygons, etc.
  * Per Primitive `perprim` - Points are distributed equally amongst each primitive. That is, each polygon receives the same number of points.
  * Bounding Box `boundingbox` - Points are distributed within the bounding box volume of the geometry. This can be faster, though less accurate than the volume method.
  * Approximate Volume `approxvol` - Points are evenly distributed within an approximation of the volume. Areas close to the surface may receive fewer points.
  * Volume `volume` - Points are evenly distributed within the entire volume of the geometry.

- Number of Points `numpoints` - The total number of points created.
- Consolidate `consolidate` - Remove points until remaining are a minimum distance apart.
- Distance to Nearest Point `neardist` - Minimum distance when using Consolidate option.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Sprinkle SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
