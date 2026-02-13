---
url: https://docs.derivative.ca/Polyreduce_SOP
category: SOPs
title: Polyreduce_SOP
---

# Polyreduce SOP
## Summary

The Polyreduce SOP reduces a high detail polygonal model into one consisting of fewer polygons. The second input's polygons represent feature edges. They are matched to the input mesh by point numbers.
The methods to reduce polygonal models are:
  * A percentage of their former size
  * A specfic number of polys (within a few)
  * According to distance from a camera

Note that as it requires (and outputs) a triangular mesh, the polygon count may increase as a result of this operation.
A second input for feature edges is provided.
[polyreduceSOP_Class](https://docs.derivative.ca/PolyreduceSOP_Class "PolyreduceSOP Class")

## Parameters - Reduce Page
- Polygons `reduce` - The polygons which will be candidates for simplification. Other polygons which share points with these might also be affected.
- Features `creases` - Which polygons are feature edges.
- Method `method` - ⊞ - Select how to reduce the number of polygons from the following methods.
  * Percentage `percentage` - Choose reduction level with a percentage.
  * Number `number` - Choose reduction level by number of polygons.
  * Distance `distance` - Reduce polygons based on distance to an object.

- Keep % `percentage` - Specify the percentage of polygons to keep when Method set to 'Percentage'.
- Keep # `numpolys` - Specify the number of polygons to keep when Method set to 'Number'.
- Object `obj` - The object to use as a reference.
- Dist. Threshhold `distance` - The world distance at which the polygons should be left at full detail.
- Minimum % `minpercent` - A lower bound to the level of reduction.

## Parameters - Clean Page
- Stiffen Border `borderweight` - Without any constraints, the edges of planar surfaces can erode. This controls a bias which penalizes such erosion.
- Stiffen Features `creaseweight` - The amount of penalty to add to the feature edges being eroded.
- Equalize Edges `lengthweight` - This bias penalizes the removal of long edges. It tends to reduce high aspect ratio triangles at the expense of more uniform reduction.
- Prevent Mesh Inversion `meshinvert` - When enabled, each reduction is tested to see if it would flip a triangle normal. While encurring a slight cost, the results are almost always worth it.
- Pre-Triangulate `triangulate` - As only triangular polygons will be reduced, this option will automatically triangulate the input polygons.
- Prevent Cracking `keepedges` - This prohibits the removal of any edge that occurs at the boundary of the polygons. This ensures no cracks develop with unreduced areas.
- Use Original Points `originalpoints` - When it collapses edges, it will use one of the two original points instead of finding the optimal interior point.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Polyreduce SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
