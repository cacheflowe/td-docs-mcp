---
url: https://docs.derivative.ca/Polystitch_SOP
category: SOPs
title: Polystitch_SOP
---

# Polystitch SOP
## Summary

The Polystitch SOP attempts to stitch polygonal surfaces together, thereby eliminating cracks that result from evaluating the surfaces at differing levels of detail.
First, the boundaries of all the polygons to be stitched are found. An edge is a boundary edge if it is shared by no other polygon. The uniqueness of edges is determined by point numbers, and not by spatial positioning. Each boundary is then split at each "corner" into a number of pieces. A list of corner points can be manually specified, or any point at which the boundary changes direction by a certain amount can be flagged as a corner.
Finally, any two boundary pieces that are within the tolerance of each other are stitched together. This is performed by snapping the points of the high detail edge to those of the low detail edge.
[polystitchSOP_Class](https://docs.derivative.ca/PolystitchSOP_Class "PolystitchSOP Class")

## Parameters - Page
- Polygons to Stitch `stitch` - The polygons to consider for stitching.
- Corner Points `corners` - A list of point numbers that are to be considered breaks in the boundary edges.
- Max Dist to Stitch `tol3d` - The maximum distance two edges can be from each other and still be stitched.
- Consolidate Points `consolidate` - When several points along one edge are snapped to the same position, consolidate them into a single point. This only consolidates along the boundary, not across the boundary.
- Automatically Find Corners `findcorner` - Whenever an edge changes direction at a point more than the specified angle, it will mark that point as a corner.
- Corner Angle `angle` - The maximum angle a boundary point can change before it is considered a corner.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Polystitch SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
