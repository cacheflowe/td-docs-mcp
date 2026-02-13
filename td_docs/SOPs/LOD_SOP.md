---
url: https://docs.derivative.ca/LOD_SOP
category: SOPs
title: LOD_SOP
---

# LOD SOP
## Summary

The LOD SOP is unusual in so far as it does not actually alter any geometry. Instead it builds a level of detail cache for the input object. The cache to be drawn is based upon the distance to the camera. Thus, a complicated object will be drawn with a lower level of detail when it is farther away.
The second input is the **Rest Geometry**. If provided, this is the geometry wich will be used to do the (expensive) polygon reduction, and only the points of the left input will be used.
[lodSOP_Class](https://docs.derivative.ca/LodSOP_Class "LodSOP Class")

## Parameters - Page
- Step % `steppercent` - Each successive level of detail will contain approximately this percentage on the number of polygons in the higher level of detail.
- Dist. Threshhold `distance` - This is the distance from the camera at which full detail will be present.
- Minimum % `minpercent` - The objects won't be drawn with fewer than this number of polygons.
- Stiffen Border `borderweight` - The amount of weight to avoid erosion of boundary polygons.
- Equalize Edges `lengthweight` - The amount of weight to favour even sized polygons.
- Pre-Triangulate `triangulate` - Polygons can only be reduced if they are triangles. This option thus first converts them.
- Optimize Rendering `tstrips` - When set, triangle strips will be generated and used for drawing.
- Only Affect Polygons `polysonly` - If this is enabled, only the polygonal portion of the model will be displayed at lower levels of detail. Otherwise, all types of surfaces are affected by the distance to the camera.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the LOD SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
