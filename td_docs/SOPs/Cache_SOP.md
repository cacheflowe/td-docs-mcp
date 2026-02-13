---
url: https://docs.derivative.ca/Cache_SOP
category: SOPs
title: Cache_SOP
---

# Cache SOP
## Summary

The Cache SOP collects its input geometry in a cache for faster random-access playback of multiple SOPs. It should be used when cook times for a chain of SOPs is long and a quicker playback is needed.
Once cached, the geometries can be accessed in any order. This is advantageous to a 2D flipbook or scene render since the geometry is still fully 3-Dimensional. The upshot being that you can scrub otherwise sluggish animations in real time because things are precomputed and stored in a cache.
[cacheSOP_Class](https://docs.derivative.ca/CacheSOP_Class "CacheSOP Class")

## Parameters - Page
- Active `active` - While On, this node will cache a single snapshot of it's input's geometry each cook.
- Pre-Fill `prefill` - Cooks 'Cache Size' number of times to fill the Cache SOP with geometry. When set > 0, it will fill the cache. If set > 0 during playback, it will fill immediately. If set > 0 and saved out, then next time the file is opened the cache will pre-fill. While this is > 0, the node behaves as if the 'On' parameter is 0. If set to 0, then back > 0, it will clear the previous data, and pre-fill again. For more information refer to the [Pre-Filling](https://docs.derivative.ca/Pre-Filling "Pre-Filling") article.
- Cache Size `cachesize` - The size of the cache.
- Step Size `step` - The number of frames that the node will cook before it caches another geometry. When set to 1, it will cache every cook, when set to 2, it will cache every two cooks, etc.
- Output Index `outputindex` - Determines which cached geometry to output. 0 is the most recent cached geometry. Valid values are between 0 and cachesize - 1.
- Cache Points Only `cachepoints` - Store a single topology for the first cached geometry and only point data for the remaining geometries.
- Blend Position `blendpos` - Interpolate points between geometries.
- Reset `reset` - When On, clears out all of the cached geometry.
- Reset Pulse `resetpulse` - Instantly clears out all of the cached geometry.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Cache SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
