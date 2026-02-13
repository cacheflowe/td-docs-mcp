---
url: https://docs.derivative.ca/Connectivity_POP
category: POPs
title: Connectivity_POP
---

# Connectivity POP
## Summary

The Connectivity POP is intended to re-connect the input's points with a set of new primitives, similar to what the [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP") or [Torus POP](https://docs.derivative.ca/Torus_POP "Torus POP") does to their sets of points. It works on any POP, especially those that ore organized as multi-[Dimensions](https://docs.derivative.ca/Dimension "Dimension"), that is, having rows, columns, slices and any number of dimensions.
Like the Grid POP you can connect the points in any dimension with line strips, or in any two dimensions with meshes of triangles or quads, or leave them as point primitives or no primitives.
It generally takes care of the incoming POP's arrangements points, and also offers more kinds of line strip connections, like zig-zag or spiral connections of points.
See also [Torus POP](https://docs.derivative.ca/Torus_POP "Torus POP"), [Dimension POP](https://docs.derivative.ca/Dimension_POP "Dimension POP"), [Dimension](https://docs.derivative.ca/Dimension "Dimension"), [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP"), [Plane POP](https://docs.derivative.ca/Plane_POP "Plane POP")
[connectivityPOP_Class](https://docs.derivative.ca/ConnectivityPOP_Class "ConnectivityPOP Class")

## Parameters - Connectivity Page
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Lines `lines` -
  * Line Strips `linestrips` -
  * Line Strip per Plane `linestripperplane` -
  * Zig Zag per Plane `zigzagperplane` -
  * Spiral per Plane `spiralperplane` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals `quads` -

(First) Dimension Index `firstdim` - Select the dimension index. For modes requiring two dimensions, selects the first dimension index.
- Second Dimension Index `seconddim` - Dimension index to the second dimension.
(First) Dimension Closed `firstdimclosed` - Enable wrapping on the first dimension.
- Second Dimension Closed `seconddimclosed` - Enable wrapping on the second dimension.
- Reorder Points by Prim/Vertex Order `reorderpoints` - Reorder points by primitive or vertex reference order.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Connectivity POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
