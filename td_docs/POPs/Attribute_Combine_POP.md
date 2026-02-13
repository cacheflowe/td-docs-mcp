---
url: https://docs.derivative.ca/Attribute_Combine_POP
category: POPs
title: Attribute_Combine_POP
---

# Attribute Combine POP
## Summary

The Attribute Combine POP takes multiple POP inputs and lets you choose attributes from each input by name or by pattern matching, and send the attributes to the output.
On the Inputs page is a set of sequential blocks to specify the inputs. For each block, you can either wire one input to the node, or using its In POP(s) parameter you can specify one or more POPs using pattern matching.
For each block you can use the In Attributes and pattern matching to specify which attribute(s) you want from that input. You can also specify a new name to rename the attributes.
For each block, if there is a **name conflict** with a prior input, the Duplicate Attributes menu will give you the choice to make up a new incremented attribute name, to use the first or last occurance of an attribute, or use only the first input's attribute.
**Point , Vertex or Primitive Attributes**: All attributes of the first in put are sent to then output. The from the Attribute Class menu you choose which attribute type you want to pass to the output (one only) from the rest of the outputs. For example you an merge the primitive attribute from all the inputs.
The **Length Mismatch** parameter lets you choose what to do when, say the input POPs don't have the same number of points. You can choose to not infor the user (None), or put a Warning on the node, or put an Error on the node. In any case, when there is a mismatch, for shorter inputs, you can choose to hold the values of the last points of the attributes, make them 0, make them 1, or do nothing.
This **architecture for handling multiple inputs** to POPs in the Attribute Combine POP is also part of numerous other POPs, such as the [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP"), [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP"), [Blend POP](https://docs.derivative.ca/Blend_POP "Blend POP"), [Merge POP](https://docs.derivative.ca/Merge_POP "Merge POP") and [Switch POP](https://docs.derivative.ca/Switch_POP "Switch POP").
[attributecombinePOP_Class](https://docs.derivative.ca/AttributecombinePOP_Class "AttributecombinePOP Class")

## Parameters - Inputs Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Length Mismatch `lengthmismatchnotif` - ⊞ - Length mis-match motification action.
  * Ignore `ignore` -
  * Warning `warning` -
  * Error `error` -
  * Length Mismatch `lengthmismatchnotif` -
  * Length Mismatch Action `lengthmismatchaction` - Specify which attribute values to use when sampling outside of the input range.

- Duplicate Attributes `duplicateattrs` - ⊞ - Determines what to do with duplicated attributes.
  * Auto-Rename `autorename` -
  * Keep First `keepfirst` -
  * Keep Last `keeplast` -
  * Only Replace Attribs of First Input `replaceattribs` -

- In `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POP(s) `input0pop` - Input POPs for the current sequence block.
- In Attributes `input0attrs` - ⊞ - Selected attributes for the current sequence block.
  * * `*` -

- Rename to `input0renameto` - Change the input attributes to a new name.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Attribute POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
