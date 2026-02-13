---
url: https://docs.derivative.ca/Merge_POP
category: POPs
title: Merge_POP
---

# Merge POP
## Summary

The Merge POP merges together the points, vertices amd primitives of all its inputs into one output. The number of points of the output is the sum of the number of points of each input. The number of primitives of the output is the sum of the number of primitives of each input. etc.
The Merge POP tries to preserve groups and all the combined attributes. The Merge POP can merge a subset of each input geo using groups.
The Merge POP's architecture for handling multiple inputs is similar to the [Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP").
[mergePOP_Class](https://docs.derivative.ca/MergePOP_Class "MergePOP Class")

## Parameters - Merge Page
- Unique Group Name `uniquegroupname` - Enable specifying a unique group per input.
- Entity `groupentity` - ⊞ - The type of group: points or primitives.
  * Primitives `primitive` -
  * Points `point` -

- Group `group` - Shared group name of elements to merge accross all inputs
- Input `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POP(s) `input0pop` - Input POPs for the current sequence block.
- Entity `input0groupentity` - ⊞ - The type of group, points or primitives, for the current sequence block.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `input0group` - Elements group to merge for the current sequence block.
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Merge POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
