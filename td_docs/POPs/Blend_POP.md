---
url: https://docs.derivative.ca/Blend_POP
category: POPs
title: Blend_POP
---

# Blend POP
## Summary

The Blend POP lets you blend together an attribute that occurs in all of it input POPs, such as the P attribute of all the inputs.
There are at least 8 blend types. The simplest blend types will do operations like average an attribute of all the inputs, or take the maximum, minimum, sum or product of all the inputs for one attribute.
The more complex blend types will mix based on a Blend Input factor (often a number between 0 and 1) for each input.
You can specify more than one point attribute, more than one vertex and more than one primitive attribute to blend at the same time.
You can get blend weights from attributes of the input POPs.
The Blend POP's architecture for handling multiple inputs is similar to the [Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP").
**Per-point mapping of parameters** - The Random POP has a Map page, which allows every point to get a different value for the Blend Input weight parameter. In this mechanism, a separate attribute in the input contains values that override (or add to / multiply by) the parameter value. See [Mapping POP Attributes to Parameters](https://docs.derivative.ca/Mapping_POP_Attributes_to_Parameters "Mapping POP Attributes to Parameters").
[blendPOP_Class](https://docs.derivative.ca/BlendPOP_Class "BlendPOP Class")

## Parameters - Blend Page
- Blend Type `blendtype` - ⊞ - The Nth point of each input is blended according to this menu. The first group are simple blends, the last group depends on the weight of each input.
  * Off `off` -
  * Average `avg` -
  * Add `add` -
  * Multiply `mul` -
  * Minimum `min` -
  * Maximum `max` -
  * Differencing `differencing` -
  * Proportional `proportional` -
  * Proportional Smoothed `proportionalsmoothed` -

- Length Mismatch `lengthmismatchnotif` - ⊞ - Length mis-match motification action.
  * Ignore `ignore` -
  * Warning `warning` -
  * Error `error` -
  * Length Mismatch `lengthmismatchnotif` -
  * Length Mismatch Action `lengthmismatchaction` - Specify which attribute values to use when sampling outside of the input range.

- Blend Weights CHOP `weightchop` - Instead of the blend weights coling from parameters, they can come from a CHOP, wither one weight per channel, or one weight per sample.
- Point Attribute Scope `pointattrscope` - ⊞ - The Point attribute scope to blend.
  * * `*` -

- Primitive Attribute Scope `primattrscope` - ⊞ - The Primitive attribute scope to blend.
  * * `*` -

- Vertex Attribute Scope `vertattrscope` - ⊞ - The Vertex attribute scope to blend.
  * * `*` -

- Input `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POP(s) `input0pop` - Input POPs for the current sequence block.
- Blend Input `input0weight` - The weight for the current input.

## Parameters - Map Page
- Mapping `map` - Start of Sequential Parameter Blocks for attribute-to-parameter mapping.
- OP `map0op` - Source OP for parameter mapping. The default of _in0 means the input POP.
- Element `map0element` - The attribute (or component of an attribute) that will be mapped to a parameter per-point.
- Parameter `map0parm` - ⊞ - Parameter on the current POP that will be mapped from the Element (the attribute).
  * input0weight (Blend Input) `input0weight` -

- Combine Operation `map0combineop` - ⊞ - Combine operation for attribute value with parameter value.
  * Set `set` -
  * Multiply `mult` -
  * Add `add` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Blend POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
