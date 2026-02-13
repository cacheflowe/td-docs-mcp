---
url: https://docs.derivative.ca/Proximity_POP
category: POPs
title: Proximity_POP
---

# Proximity POP
## Summary

The Proximity POP connects points to nearby points in its first input within a specified near/far distance. If a second input is connected, it connects points of the second input with points of the first input that are in-range.
Two parameters set the Maximum Distance and the Minimum Distance between points to connect. You can limit how many lines each point can connect from. The Uniform Distribution parameter gives a more random distribution of connecting points.
You can ensure each pair of points have at most one line between them.
When there are two inputs to Proximity, you can output (via the Output menu) the connecting lines, or simply point primitives of the first input that are within range of the second input. When outputting lines, you can include primitive attributes `LineDir` and `LineLength`.
When outputting points you can also output all the attributes of the matching point as separate new attributes (`EndP`, `EndN`, `EndTex` etc) by select End Point Attributes.
Each connecting primitive is a 2-point "line primitive", not a line strip.
See also [Neighbor POP](https://docs.derivative.ca/Neighbor_POP "Neighbor POP"), [Line Metrics POP](https://docs.derivative.ca/Line_Metrics_POP "Line Metrics POP")
[proximityPOP_Class](https://docs.derivative.ca/ProximityPOP_Class "ProximityPOP Class")

## Parameters - Proximity Page
- Maximum Distance `maxdist` - Maximum distance from current point for candidate points to create lines to.
- Minimum Distance `mindist` - Minimum distance from current point for candidate points to create lines to.
- Max Lines per Point `maxlinesperpoint` - Specifies the max number of lines emanating from each point in the first input.
- Uniform Distribution `uniformdist` - Allows evenly distributed selection among nearby points, rather than defaulting to the first ones found.
- Max Temp Neighbors `maxtempneighbors` - Used internally to store candidate points to create lines to before removing some to reach the max number of lines per point.
- Duplicate Lines `duplines` - ⊞ - Determines what to do with duplicated proximity lines
  * Do Nothing `donothing` -
  * Avoid `avoid` -
  * Delete `delete` -

- Num Hash Buckets `numhashbuckets` - The number of buckets the points will be sorted in based on their position. A good heuristic is to choose it to be close to the number of points.

## Parameters - Output Page
- Output `output` - ⊞ - Whether to output points with attributes or lines.
  * Lines (Shared Points) `lines` -
  * Point Prims `points` -

- Line Direction `linedir` - ⊞ - Enable addition of line direction attribute.
  * Line Direction `linedir` -
  * Line Direction Attrib Name `linedirname` - Attribute name for line direction.

- Line Length `linelength` - ⊞ - Enable addition of line length attribute.
  * Line Length `linelength` -
  * Line Length Attrib Name `linelengthname` - Attribute name for line length.

- End Point Attributes `endptattrs` - Enable outputting end point attributes from second input
- Origin `origin` - ⊞ - Sets whether the lines origin comes from the first input or the second input.
  * First Input Points `first` -
  * Second Input Points `second` -

- Remove Unused Points `remunusedpoints` - Removes unused points not referenced by primitives.
- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Proximity POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
