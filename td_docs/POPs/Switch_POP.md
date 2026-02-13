---
url: https://docs.derivative.ca/Switch_POP
category: POPs
title: Switch_POP
---

# Switch POP
## Summary

The Switch POP lets you choose one of the inputs, and outputs the input unchanged. The number of points, vertices and primitives of all of the inputs can be different.
It uses a numeric parameter, Index, to choose the input, with 0 referring to the first input. If Index is fractional - a non-integer, it can blend two inputs: If the inputs have the same number of points, vertices and primitives, they can be blended, two adjacent inputs at a time.
Tip: Since it blends only adjacent inputs (input N with input N+1 or N-1), to blend from the last input to the first input, attach the first input again as the last input, and use CHOPs to loop from 0 to number-of-inputs snap back to 0 when Index reaches number-of-inputs.
If Index is out of range, it clamps.
See the Blend POP to blend arbitrary combinations of inputs.
The Switch POP's architecture for handling multiple inputs is similar to the [Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP").
[switchPOP_Class](https://docs.derivative.ca/SwitchPOP_Class "SwitchPOP Class")

## Parameters - Switch Page
- Index `index` - Input index to output.
- Extend `extend` - ⊞ - Determines what to do when the index exceeds the number of inputs. Allows for negative indices.
  * Clamp `clamp` -
  * Loop `loop` -
  * ZigZag `zigzag` -

- Blend between Inputs `blend` - Blends the input POPs attributes when using floating point numbers in the index parameter.
- Length Mismatch `lengthmismatchnotif` - ⊞ - Length mis-match motification action.
  * Length Mismatch `lengthmismatchnotif` -
  * Length Mismatch Action `lengthmismatchaction` - Specify which attribute values to use when sampling outside of the input range.

- Point Attribute Scope `pointattrscope` - ⊞ - The Point attribute scope to blend.
  * * `*` -

- Primitive Attribute Scope `primattrscope` - ⊞ - The Primitive attribute scope to blend.
  * * `*` -

- Vertex Attribute Scope `vertattrscope` - ⊞ - The Vertex attribute scope to blend.
  * * `*` -

- Input `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POP(s) `input0pop` - Input POPs for the current sequence block.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Switch POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
