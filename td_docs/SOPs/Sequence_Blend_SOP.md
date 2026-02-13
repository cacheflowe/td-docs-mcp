---
url: https://docs.derivative.ca/Sequence_Blend_SOP
category: SOPs
title: Sequence_Blend_SOP
---

# Sequence Blend SOP
## Summary

The Sequence Blend SOP allows you do 3D Metamorphosis between shapes and Interpolate point position, colors, point normals, and texture coordinates between shapes.
See also [Blend SOP](https://docs.derivative.ca/Blend_SOP "Blend SOP") and [Switch SOP](https://docs.derivative.ca/Switch_SOP "Switch SOP").
[sequenceblendSOP_Class](https://docs.derivative.ca/SequenceblendSOP_Class "SequenceblendSOP Class")

## Parameters - Page
- Blend Factor `blend` - This value determines the blend transition between consecutive geometry inputs. Values between 0 and 1 will control the metamorphosis between geometry input 1 and 2, values between 1 and 2 will control the metamorphosis between geometry input 2 and 3, and so on.
- Blend Position `dopos` - If checked, only point xyz positions are blended.
- Blend Colors `doclr` - Point Colors are blended.
- Blend Normals `donml` - Point normals are blended.
- Blend Texture `douvw` - Point texture coordinates are blended.
- Blend Up `doup` - When checked, the Up Vector of the geometry inputs will be blended based on the weights of the blend channels.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Sequence Blend SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
