---
url: https://docs.derivative.ca/Select_POP
category: POPs
title: Select_POP
---

# Select POP
## Summary

The Select POP takes individual attributes from its single input and outputs the attributes unchanged. It is used frequently so you can work on attributes separately, and then after processing the attributes, you can combine them back together downstream with an [Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP").
The number of points does not change. The data in the selected attributes does not change. The topology does not change either - it outputs the same primitives and vertices as the input.
Because attributes of operators in the POPs family that are not changed in a POP don't actually copy their data or allocate any more memory (they are simply a reference to the POP that does have the data), selecting attributes and combining them back does not make anything faster or memory-efficient. It's mostly a workflow preference that is more similar to the CHOPs workflow. Middle-mouse click on the Select POP node to see the info pop-up, and note that the GPU memory consumed is 0.
Instead of a wired input you can use the POP parameter to reference another POP in the current or any other network.
Note: Unlike the [Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP") that increases the number of point attributes and does not change the number of points, the [Merge POP](https://docs.derivative.ca/Merge_POP "Merge POP") increases number of points by merging primitives and their vertices together with the point lists of each input. For example, it merges the `P` attribute of all the points together to make a longer point list.
See also [Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP"), [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP") and [math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP") (can also extract individual attributes), [Merge POP](https://docs.derivative.ca/Merge_POP "Merge POP"), [Topology POP](https://docs.derivative.ca/Topology_POP "Topology POP")
[selectPOP_Class](https://docs.derivative.ca/SelectPOP_Class "SelectPOP Class")

## Parameters - Select Page
- POP `pop` - POP to select attributes from.
- Point Attribute Scope `pointattrscope` - ⊞ - The Point attribute scope to blend.
  * * `*` -

- Primitive Attribute Scope `primattrscope` - ⊞ - The Primitive attribute scope to blend.
  * * `*` -

- Vertex Attribute Scope `vertattrscope` - ⊞ - The Vertex attribute scope to blend.
  * * `*` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Select POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
