---
url: https://docs.derivative.ca/In_POP
category: POPs
title: In_POP
---

# In POP
## Summary

The In POP gets data from a POP that is connected to one of the inputs of the In POP's parent component. For each In POP inside a component, there is one input connector added to the In POP's parent component.
If there is nothing connected to the parent component's input, then the In POP will output what is connected to its second input, if any. This is useful for making sure there is some default data to work with.
[inPOP_Class](https://docs.derivative.ca/InPOP_Class "InPOP Class")

## Parameters - In Page
- Label `label` - Creates a pop-up label when the cursor rolls over this Component input.
- Connect Order `connectorder` - All the connect orders from the In Ops are sorted to determine the order of the connectors on the parent COMP.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the In POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
