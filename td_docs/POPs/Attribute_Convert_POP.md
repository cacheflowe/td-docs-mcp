---
url: https://docs.derivative.ca/Attribute_Convert_POP
category: POPs
title: Attribute_Convert_POP
---

# Attribute Convert POP
## Summary

The Attribute Convert POP lets you copy a POP [attribute](https://docs.derivative.ca/Attribute "Attribute") from one "attribute class" to another. That is, attributes can be on a point, a vertex, or a primitive. You can, for example convert a primitive attribute to the points of that primitive. In some cases it is ambiguous, like when a point is shared between multiple primitives or multiple vertices, so the POP picks one value and doesn't complain.
When it converts, it can delete the original attribute, and it can error or warning if the attribute it creates already exists.
See the [POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT") to find all the attributes of a POP.
See [Attribute POP](https://docs.derivative.ca/Attribute_POP "Attribute POP") to copy or rename an attribute within one attribute class.
Note: There currently are no attributes on the POP as a whole.
[attributeconvertPOP_Class](https://docs.derivative.ca/AttributeconvertPOP_Class "AttributeconvertPOP Class")

## Parameters - Attribute Convert Page
- Convert Operation `convertop` - ⊞ - Chooses which attribute class (Point, Vertex, Primitive) for convert from and to.
  * None `none` -
  * Point to Vertex `pointtovert` -
  * Vertex to Point `verttopoint` -
  * Point to Primitive `pointtoprim` -
  * Primitive to Point `primtopoint` -
  * Vertex to Primitive `verttoprim` -
  * Primitive to Vertex `primtovert` -

- Input Attributes `inputattrs` - ⊞ - Input attributes to convert to the new attribute class.
  * * `*` -

- New Attribute Name `newattrs` - Name of new attribute being created.
- Delete Original `deleteorig` - Delete the selected incoming attribute.
- Notification if Attribute Exists `notificationifexists` - ⊞ - Whether to display a notification if the attribute already exists on the input.
  * Ignore `ignore` -
  * Warning `warning` -
  * Error `error` -

- Override if Attribute Exists `overrideifexists` - When on, overrides an input attribute if a new attribute created by this POP has the same name.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Attribute Convert POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
