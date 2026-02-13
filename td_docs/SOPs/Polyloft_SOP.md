---
url: https://docs.derivative.ca/Polyloft_SOP
category: SOPs
title: Polyloft_SOP
---

# Polyloft SOP
## Summary

The Polyloft SOP generates meshes of triangles by connecting (i.e. lofting/stitching) the points of open or closed faces without adding any new points. Polyloft can also connect groups of unrelated points in a similar fashion. The faces and the point groups need not have the same number of points.
The optional input specifies the rest geometry, typically the copy of the main input at a specific face (usually 1). This forces the point order to remain constant throughout the animation and prevents the triangular stitch from popping as the geometry deforms. If you specify face or point groups for lofting using rest geometry, make sure they are defined in the second input.
[polyloftSOP_Class](https://docs.derivative.ca/PolyloftSOP_Class "PolyloftSOP Class")

## Parameters - Polyloft Page
- Connect Closest Ends `proximity` - Start stitching at the two closest points, and handle arbitrary face orientation and start vertices.
- Consolidate Points `consolidate` - Fuse neighbouring points before stitching.
- Distance `dist` - Threshold distance for consolidation.
- Minimize `minimize` - ⊞ - Distance minimization goal:
  * 2-Point Distance `point2` - Default stitching target.
  * 3-Point Distance `point3` - May help avoid intersections.

- U Wrap `closeu` - ⊞ - Close the stitch in U (close each cross-section).
  * Off `nonewu` -
  * On `wu` -
  * If Primitive does `ifprimwu` -

- V Wrap `closev` - ⊞ - Connect first and last cross-sections.
  * Off `nonewv` -
  * On `wv` -
  * If Primitive does `ifprimwv` -

- Create Polygon Group `creategroup` - Place the generated triangles into a group.
- Name `polygroup` - Specify the name of the group here when the above parameter Create Polygon Group = On.
- Method `method` - ⊞ - Selects how to perform the lofting/stitching.
  * Faces `faces` - Stitch a set of faces by connecting their control vertices.
  * Points `points` - Stitch sets of points, each set acting as a cross-section.

- Group `group` - Subset of faces to loft.
- Keep Primitives `prim` - Preserve the cross-sections after stitching.

## Parameters - Point Groups Page
Stitch sets of points, each set acting as a cross-section.
- Point Group `point` - Sequence of point sets to be stitched.
- Point Group `point0group` - Point groups.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Polyloft SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
