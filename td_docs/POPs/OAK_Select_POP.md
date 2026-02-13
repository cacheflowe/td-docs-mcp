---
url: https://docs.derivative.ca/OAK_Select_POP
category: POPs
title: OAK_Select_POP
---

# OAK Select POP
## Summary

The OAK Select POP can receive point cloud data.
[oakselectPOP_Class](https://docs.derivative.ca/OakselectPOP_Class "OakselectPOP Class")

## Parameters - OAK Page
- Active `active` - When enabled, data from the specified OAK Device CHOP will be retrieved.
- OAK Device CHOP `chop` - Reference to the OAK Device CHOP running a depthai pipeline.
- Stream `stream` - The name of the stream to be received.
- Cache Size `cachesize` - The Cache Size parameter works like the Queue Size parameter on the OAK Select CHOP. Picking 2 is a good default choice because it enables TouchDesigner to show an image to the user while asynchronously writing new data into the remaining buffer.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.
## Info CHOP Channels
Extra Information for the OAK Select POP POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
