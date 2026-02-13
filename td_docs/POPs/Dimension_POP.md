---
url: https://docs.derivative.ca/Dimension_POP
category: POPs
title: Dimension_POP
---

# Dimension POP
## Summary

The Dimension POP can alter the dimensions of a POP. See [Dimension](https://docs.derivative.ca/Dimension "Dimension").
The product of the new dimensions has to be equal to the number of points, otherwise it will give a warning and not change anything.
In all cases the points and point order does not change in any way, nor do vertices nor primitives – no data change. It only changes how the organization of points is viewed.
You can add a Dimension
```
20 33 -> 20 33 1 or 1 20 33
```

Or remove a dimension
```
12 5 30 -> 60 39
```

Or swap, which often would not make sense
```
12 25 -> 25 12
```

Or split a dimension into two equal dimensions
```
160  5  15 -> 80 2 5 15
```

[dimensionPOP_Class](https://docs.derivative.ca/DimensionPOP_Class "DimensionPOP Class")

}}
## Parameters - Dimension Page
- Mode `mode` - ⊞ - Choose to reorder dimensions or set dimensions.
  * Reorder Dimensions (Reorder Points) `reorderdims` -
  * Set Dimensions `setdims` -

- Dimension Order `dimorder` - Determines the dimension indices to reorder.
- Dimension `dim` - Start of Sequential Parameter Blocks for dimensions.
- Number `dim0number` - The size of the dimension in the current block.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Dimension POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
