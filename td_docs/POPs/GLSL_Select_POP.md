---
url: https://docs.derivative.ca/GLSL_Select_POP
category: POPs
title: GLSL_Select_POP
---

# GLSL Select POP

## Summary

The GLSL Select POP allows you to select one of the Extra Output POPs that can be made available with a [GLSL Advanced POP](GLSL_Advanced_POP.md "GLSL Advanced POP").

[glslselectPOP_Class](GLSL_Select_POP_Class.md "GlslselectPOP Class")

## Parameters - GLSL Select Page
- POP `pop` - POP reference.
- Output Name `name` - Name of an extra output on the selected GLSL Advanced POP to select and output.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels

Extra Information for the GLSL Select POP can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

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
