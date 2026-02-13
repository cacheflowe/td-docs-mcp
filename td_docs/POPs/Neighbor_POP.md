---
url: https://docs.derivative.ca/Neighbor_POP
category: POPs
title: Neighbor_POP
---

# Neighbor POP
## Summary

The Neighbor POP uses the `P` attribute to find, for each point of the input, the closest points to it. It puts the indexes of the closest points in an array attribute `Nebr`. You specify the max number of neighbors, and you choose the Max Neighbors Distance to look for neighbors.
The size of the attribute `Nebr` is the Max Neighbors parameter. If fewer than that number is found, it puts a special number `4294967295` as the value for the neighbor index. The attribute `NumNebrs` holds the number of neighbors found for each point.
You can output the average distance to the found neighbors, optionally including the point's position. Alternately you can output the Inverse Distance Weighted Average, where the closest points have the highest influence on the average.
Instead of outputting the indexes of the neighbors, you can output any set of attributes of the neighbors (careful, this can produce a lot of data).
An alternate form of the Neighbor POP takes a second input, where the each point of the first input is compared to points of the second input.
Neighbors are determined by distance between points, but via the Neighbors Type menu, they can also be determined by connectivity along any primitive connecting edges to neighboring points (only one step currently). For example, two points adjacent to each other in a line strip or quad are neighbors of each other.
( Distribution - Default, Unique, Closest )
Internally it is using a unbounded spatial hashing algorithm nad put into one of Num Hash Buckets.
[neighborPOP_Class](https://docs.derivative.ca/NeighborPOP_Class "NeighborPOP Class")

## Parameters - Neighbor Page
- Neighbors Type `nebrtype` - ⊞ - When checking for neighbors, choose to use edge connectivity or only distance to neighbor points.
  * By Distance `distance` -
  * Connected `connected` -

- Max Neighbors Distance `maxdistance` - Specifies the distance below which a point is considered a neighbor of the current point.
- Distribution `distribution` - ⊞ - Determines what kind of neighbor sets are returned.
  * Default `default` -
  * Unique `unique` -
  * Closest `closest` -

- Num Hash Buckets `numhashbuckets` - The number of buckets the points will be sorted in based on their position. A good heuristic is to choose it to be close to the number of points.
- Output Hash Attrib `outputhash` - Whether to output an attribute with the Spatial Hash values, which can be useful to debug and optimize performance.
- Output `nebroutput` - ⊞ - Whether to output the individual neighbors and their attributes in array attributes, or their average or distance weighted average.
  * Neighbors `nebr` -
  * Average `avg` -
  * Inverse Distance Weighted Average `weightedavg` -

- Max Neighbors `maxneighbors` - Specifies the max number of neighbors. This sets the array size of all the attributes storing neighbors information.
- Neighbors `nebrs` - ⊞ - Enable addition of the neighbors attribute.
  * Neighbors `nebrs` -
  * Neighbor Attr Name `nebrattrname` - Name for the attribute containing the point indices of the neighbors.

- Num Neighbors `numnebrs` - ⊞ - Enable the addition of the number of neighbors attribute.
  * Num Neighbors `numnebrs` -
  * Num Neighbors Attr Name `numnbrsattrname` - The attribute name for the number of neighbors.

- Add Distance Attribute `dodist` - ⊞ - Whether to output an attribute containing the distance to the query point.
  * Add Distance Attribute `dodist` -
  * Distance Attribute Name `distattrname` - Specifies the scope of the attribute that stores the distance values

- Max Neighbors for Average `maxnebrsavg` - Specifies the max number of neighbors considered when averaging neighbor attributes.
- Include Query Point `incquerypt` - When on, includes the query point when calculating average when output is average.
- Add Prefix `addprefix` - Whether to add Nebr prefix when outputting neighbor attributes.
- Cast Integers to Floats `castintstofloats` - When averaging the neighbor attribute values, whether to cast integer attributes to float.
- Neighbor Point Attributes `nebrptattrs` - ⊞ - Creates array attributes the size of max neighbors with the neighbor attributes for each point in the first input.
  * * `*` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Neighbor POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
