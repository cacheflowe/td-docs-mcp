---
url: https://docs.derivative.ca/Convert_POP
category: POPs
title: Convert_POP
---

# Convert POP
## Summary

The Convert POP is a general utility that keeps the points of the input, but reconnects them in various ways as primitives. This includes converting to and from line strips, opening/closing line strips, converting quads to triangles, stripping off all primitives, and creating Point Primitives from points.
It can also “flatten” a POP into an orderly form by first making the points of all primitives unique, and then re-ordering all the points by going through each primitive and ordering the points according to the vertices of each primitive (menu item Unique Points and Reorder to Prim/Vertex Order). The first point in the point list is the first vertex of the first primitive, and the last point of the point list is the last vertex of the last primitive.
See also [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP").
[convertPOP_Class](https://docs.derivative.ca/ConvertPOP_Class "ConvertPOP Class")

## Parameters - Convert Page
- Convert `convert` - ⊞ - Determines the converting operation to apply to the primitives or the points.
  * None `none` -
  * Keep Points, Delete Primitives `deleteprims` -
  * Points to Point Primitives `topointprims` -
  * Line Strips to Lines `linestripstolines` -
  * Triangle, Quads and Lines to Line Strips `tolinestrips` -
  * Quads to Triangles `quadstotriangles` -
  * Close Line Strips `closelinestrips` -
  * Open Line Strips `openlinestrips` -
  * Reverse Vertex Order of Each Primitive `reversevertorder` -
  * Unique and Reorder Points by Prim/Vertex Order `uniquereorderpoints` -
  * Copy Topology Back to CPU (Slow) `cpureadback` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Convert POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
