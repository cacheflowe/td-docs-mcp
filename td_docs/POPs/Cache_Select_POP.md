---
url: https://docs.derivative.ca/Cache_Select_POP
category: POPs
title: Cache_Select_POP
---

# Cache Select POP
## Summary

The Cache Select POP takes a reference to a Cache POP and outputs one of its cached data sets based on the Cache Index parameter. A Cache Index value of 0 outputs the Cache POP's current frame's data, -1 outputs its previous cached data (the second newest set), and so on. So the values you provide for index are negative integers and 0. Indexes that are out of range are clamped to be the Cache POP's -(Cache Size-1), and 0.
See also: [Cache POP](https://docs.derivative.ca/Cache_POP "Cache POP"), [Cache Blend POP](https://docs.derivative.ca/Cache_Blend_POP "Cache Blend POP")
[cacheselectPOP_Class](https://docs.derivative.ca/CacheselectPOP_Class "CacheselectPOP Class")

## Parameters - Cache Select Page
- Cache POP `cachepop` - The Cache POP to fetch cache snapshots from.
- Cache Index `index` - ⊞ - The cache index to output.
  * Cache Index `index` -
  * Cache Index Unit `cacheindexunit` - Index is expressed in seconds, frames (based on timeline frames per second) or raw index.

- Interpolate Frames `interp` - When on the selected index can interpolate between the cached frames if each snapshot has the same number of points. Otherwise, the nearest cached frame is used.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Cache Select POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
