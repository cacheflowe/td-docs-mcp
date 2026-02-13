---
url: https://docs.derivative.ca/Facet_POP
category: POPs
title: Facet_POP
---

# Facet POP
## Summary

The Facet POP does operations to make points ve shared between multiple primitives, or create new points so that the points are not shared.
Unique Points will create new points so that each vertex of each primitive does not shared a point with any other vertex. (exception: on closed line strips the first vertex and the last vertex refer to the same point, by definition)
Consolidate Points will potentially reduce the number of points by combining points that are within a specified distance tolerance into one point. Then multiple vertices may refer to each point, i.e. "share" a point.
Cusp Polygon will look at all edges between polygons, and if the adjacent two faces to an edge are not aligned within a specified angle tolerance, it will make the edge point unique.
You may follow the Facet POP with a [Normal POP](https://docs.derivative.ca/Normal_POP "Normal POP") which computes the point or vertex normals, giving the surfaces a faceted loop or not.
[facetPOP_Class](https://docs.derivative.ca/FacetPOP_Class "FacetPOP Class")

## Parameters - Facet Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Operation `operation` - ⊞ - Selects the operation to perform.
  * No Operation `none` -
  * Unique Points `unique` -
  * Cusp Polygons `cusp` -
  * Consolidate Points `conspoints` -

- Angle `angle` - The threshold angle between faces above which the shared edge vertices don't share points.
- Distance `dist` - Sets the maximum distance between points when consolidating points.
- Max Tries `maxtries` - Max number of iterations when trying to consolidate points, in case the target point has already been consolidated.
- Remove Degenerate `removedegenerate` - Remove primitives where consecutive vertices reference the same point.
- Remove Unused Points `removeunusedpoints` - Removes unused points not referenced by primitives.
- Technique `technique` - ⊞ - Points consolidation technique.
  * Brute Force `bruteforce` -
  * Shared Memory `sharedmemory` -
  * Spatial Grid `spatialgrid` -
  * Spatial Grid Per Voxel `spatialgridpervoxel` -

- Voxels Grid Resolution `gridres` - Defines the voxel grid resolution used when consolidating points via the Spatial Grid Per Voxel method.
- Specify Bounding Box `specifybbox` - Enable specifying a bounding box when consolidating points with the spacial grid per voxel method.
- Bounding Box `bbox` - SOP to use as bounding box when specifying a bounding box when consolidating points with the Spatial Grid method.
- Compute Point Normals `computenormals` - Whether to compute point normals as a post operation.
- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Facet POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
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
