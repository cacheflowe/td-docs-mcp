---
url: https://docs.derivative.ca/Cache_Blend_POP
category: POPs
title: Cache_Blend_POP
---

# Cache Blend POP
## Summary

The Cache Blend POP takes a reference to a [Cache POP](https://docs.derivative.ca/Cache_POP "Cache POP") and outputs a blend of its cached data sets based on a Cache Index parameter and the Cache Weight parameter of the each of the sequential blocks.
The blend is done on each point separately, so the results of one point is not affected by any other point.
This is useful for doing time-blurs of geometry data, and calculating slope or speed of a point (assuming the number of points in the input is not changing).
A Cache Index value of 0 blends the Cache POP's current frame's data, -1 blends in its previous cached data (the second newest set), and so on.
The weights are normalized.
See also: [Cache POP](https://docs.derivative.ca/Cache_POP "Cache POP"), [Cache Select POP](https://docs.derivative.ca/Cache_Select_POP "Cache Select POP"), [Blend POP](https://docs.derivative.ca/Blend_POP "Blend POP")
[cacheblendPOP_Class](https://docs.derivative.ca/CacheblendPOP_Class "CacheblendPOP Class")

## Parameters - Cache Blend Page
- Cache POP `cachepop` - The Cache POP to retrieve from.
- CHOP `chop` - Weight and index can be channels of a CHOP versus being parameters.
- Index Channel `indexchan` - Name of the channel to use for cache index when using a CHOP.
- Index Channel Unit `indexchanunit` - ⊞ - Unit of the index channel when using a CHOP.
  * I `indices` -
  * F `frames` -
  * S `seconds` -

- Weight Channel `weightchan` - Specifies the channel that contains weight values.
- Interpolate Frames `interp` - When on the selected index can interpolate between the cached frames if each snapshot has the same number of points. Otherwise, the nearest cached frame is used.
- Cache `cache` - Start of Sequential Parameter Blocks for managing weights and index of POPs in the cache.
- Cache Index `cache0index` - ⊞ - The Cache Index to select.
  * Cache Index `cache0index` -
  * Cache Index Unit `cache0indexunit` - Index is expressed in seconds, frames (based on timeline frames per second) or raw index.

- Cache Weight `cache0weight` - Weight to use for the POP in the cache at the index.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Cache Blend POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
