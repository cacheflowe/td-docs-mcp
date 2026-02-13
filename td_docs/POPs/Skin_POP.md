---
url: https://docs.derivative.ca/Skin_POP
category: POPs
title: Skin_POP
---

# Skin POP
## Summary

The Skin POP takes any 2-dimensional (or more) arrangement of data (for example three line strips of 20 point each) and connects them together as a mesh of triangles or quads.
See [POP Dimension](https://docs.derivative.ca/POP_Dimension "POP Dimension"). - Dimension is a property of all POPs that you can see in the popup info for a POP. It defines a virtual arrangement of the points, most simply as rows and columns of points (that would be two dimensions) (It doesn't matter how they are connected). In this case the total number of points = numberOfRows * numberOfColumns.
You may see dimension 10 20 3 with a total of 600 points. If the input has three dimensions or more, it applies the skinning to the first two dimensions, and repeats that for all each higher dimension.
Instead you can manually force it to treat your specified number of primitives a group to skin, or every the set of Nth primitive as sets of primitives to skin.
If a channel name is not provided, it uses the names in their sequential order.
See also [Extrude POP](https://docs.derivative.ca/Extrude_POP "Extrude POP").
[skinPOP_Class](https://docs.derivative.ca/SkinPOP_Class "SkinPOP Class")

## Parameters - Skin Page
- Skin `skinops` - ⊞ - Skin primitive method.
  * All Primitives `all` -
  * Groups of N Primitives `group` -
  * Skip Every Nth Primitive `skip` -

- N `inc` - N value when skinning groups of N input primitives or every N input primitives.
- Closed `closed` - The last vertex is connected to the first vertex.
- Output Quads `outputquads` - Whether to output quad primitives instead of triangle primitives.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Skin POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
