---
url: https://docs.derivative.ca/Out_POP
category: POPs
title: Out_POP
---

# Out POP
## Summary

The Out POP outputs data to POPs outside its parent component. For each Out POP inside a component, there is one output connector added to the Out POP's parent component.
You can wire a POP to its input, or reference another POP with the Select POP parameter.
By putting a string in the Label parameter, when you roll your cursor over the parent component's output, it will display the label.
[outPOP_Class](https://docs.derivative.ca/OutPOP_Class "OutPOP Class")

## Parameters - Out Page
- Select POP `selectpop` - POP reference to output when no input is connected.
- Label `label` - Creates a pop-up label when the cursor rolls over this Component output.
- Connect Order `connectorder` - All the connect orders from the Out OPs are sorted to determine the order of the connectors on the parent COMP.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Out POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
