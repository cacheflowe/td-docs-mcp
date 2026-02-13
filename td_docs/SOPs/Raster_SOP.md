---
url: https://docs.derivative.ca/Raster_SOP
category: SOPs
title: Raster_SOP
---

# Raster SOP
## Summary

The Raster SOP converts TOP image data to geometry by scanning left to right, top to bottom, outputting a geometry point at each pixel. This output can be used to display image data on laser devices, oscilloscopes or similar devices using the [Laser CHOP](https://docs.derivative.ca/Laser_CHOP "Laser CHOP"). This is different from the [Trace SOP](https://docs.derivative.ca/Trace_SOP "Trace SOP") which only outputs contour shapes from an image.
[rasterSOP_Class](https://docs.derivative.ca/RasterSOP_Class "RasterSOP Class")

## Parameters - Raster Page
- TOP `top` - The path to the TOP to rasterize into geometry.
- Direction `direction` - ⊞ - Determines the direction of rasterization. Depending on the image horizontal or vertical might work better.
  * Horizontal `horizontal` - Scan horizontally.
  * Vertical `vertical` - Scan vertically.

- Download Type `downloadtype` - ⊞ - Gives the option for a delayed data download from the GPU, which is much faster and does not stall the render.
  * Immediate (Slow) `immediate` -
  * Next frame (Fast) `nextframe` -

## Info CHOP Channels
Extra Information for the Raster SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
