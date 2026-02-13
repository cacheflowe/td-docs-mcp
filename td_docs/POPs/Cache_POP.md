---
url: https://docs.derivative.ca/Cache_POP
category: POPs
title: Cache_POP
---

# Cache POP
## Summary

The Cache POP receives POP data every frame in its input and holds the most recent frames of data (up to Cache Size) in GPU memory. It outputs any of these held frames, determined by Output Index, which acts like a time-delay of its input. Furthermore, [Cache Select POPs](https://docs.derivative.ca/Cache_Select_POP "Cache Select POP") and [Cache Blend POPs](https://docs.derivative.ca/Cache_Blend_POP "Cache Blend POP") can access any combination the Cache POP's set of held inputs, allowing for multi-frame blends.
If the Cache POP's Step Size is 3, for example, the Cache POP will hold every third frame, making the amount of time covered by the Cache POP triple. This reduces the amount of memory needed for long caches. Note that the data held in GPU memory is uncompressed.
You can freeze the set of data held in the Cache POP by turning off the Active toggle parameter. You can clear and hold the cache to zero frames while the Reset parameter is on (the input is simply sent to the output), and you can hit Reset Pulse to clear the cache and start growing the cache again right away. (An [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") connected to a Cache POP will show the number of frames in the cache.)
The values you provide for Cache Index are 0 and negative integers. -2 is the third most recent cached data. Indexes that are out of range are clamped to be between and including -(Cache Size-1), and 0.
You can also specify two channels to define the weights, one for weight and for indices.
Cache POP gives you choices on how to number the index of the cached images.
When the `.toe` or `.tox` file is restarted, the cache starts cleared - nothing is saved in the file.
Note that when frames are dropped, data in the cache may be older that they would be if frames were not dropped. The [Trail POP](https://docs.derivative.ca/Trail_POP "Trail POP"), though different in functionality, deals with frame drops more elegantly by filling in data for missing frames, and tagging each timeslice with an `Age` attribute. The Cache POP does not have this built-in.
See also [Cache Select POP](https://docs.derivative.ca/Cache_Select_POP "Cache Select POP"), [Cache Blend POP](https://docs.derivative.ca/Cache_Blend_POP "Cache Blend POP"), [Trail POP](https://docs.derivative.ca/Trail_POP "Trail POP"), [Cache TOP](https://docs.derivative.ca/Cache_TOP "Cache TOP"), [Texture 3D TOP](https://docs.derivative.ca/Texture_3D_TOP "Texture 3D TOP").
[cachePOP_Class](https://docs.derivative.ca/CachePOP_Class "CachePOP Class")

## Parameters - Cache Page
- Active `active` - ⊞ - When enabled, the cache POP will capture input POP frames.
  * Active `active` -
  * Active Pulse `activepulse` - When clicked (pulsed) it will be active for one frame and adds one snapshot to the cache, discarding the oldest.

- Cache Size `cachesize` - The maximum number of snapshots to hold in the cache. When full, oldest ones are replaced with the newest ones.
- Step Size `step` - ⊞ - Time steps between snapshots into cache.
  * Step Size `step` -
  * Step Size Unit `stepunit` - The step time can be expressed in seconds or frames.

- Output Index `outputindex` - ⊞ - Specify the index of POP to output - 0 is current, negative is farther into past.
  * Output Index `outputindex` -
  * Output Index Unit `outputindexunit` - Index is expressed in seconds, frames (based on timeline frames per second) or raw index.

- Interpolate Frames `interp` - When on the selected index can interpolate between the cached frames if each snapshot has the same number of points. Otherwise, the nearest cached frame is used.
- Reset `reset` - ⊞ - Resets cache and holds one snapshot.
  * Reset `reset` -
  * Reset `resetpulse` - Reset cache to 0 snapshots.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Cache POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
