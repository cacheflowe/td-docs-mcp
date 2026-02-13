---
url: https://docs.derivative.ca/Subdivide_POP
category: POPs
title: Subdivide_POP
---

# Subdivide POP
## Summary

The Subdivide POP subdivides and smooths a surface. It divides each quad into two triangles, and then for each triangle subdivides it into 4 triangles cutting at the midpoint of each edge. The pre-existing and new points are blended with their neighbors to produce a more smooth surface.
Increasing the Depth recurses several times in multiple passes, where the result of a pass is subdivided further in the next pass.
Increasing the Crease Weight parameter toward 1 restores the original shape more, so this is a suitable method to simply subdivide faces as you may want with a Box POP.
[subdividePOP_Class](https://docs.derivative.ca/SubdividePOP_Class "SubdividePOP Class")

## Parameters - Subdivide Page
- Depth `iterations` - Sets the number of iterations to subdivide. Higher numbers give a smoother surface.
- Crease Weight `creaseweight` - Determines how much sharp edges in the geometry should be preserved
- Simple Coefficients `simplecoeffs` - Enables simple coefficient computation when smoothing the interpolated points.
- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Subdivide POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
