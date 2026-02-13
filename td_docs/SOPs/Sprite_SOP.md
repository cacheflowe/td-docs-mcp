---
url: https://docs.derivative.ca/Sprite_SOP
category: SOPs
title: Sprite_SOP
---

# Sprite SOP
## Summary

The Sprite SOP creates geometry (quad sprites) at point positions defined by the CHOP referenced in the XYZ CHOP parameter.
[spriteSOP_Class](https://docs.derivative.ca/SpriteSOP_Class "SpriteSOP Class")

## Parameters - Page
- XYZ CHOP `xyzchop` - A CHOP with 3 channels is required to specify the X, Y, and Z position of the quad to be generated. Each sample creates 1 quad. The created quads are centered at the points defined by each sample.
- Camera `camera` - The geometry will always face the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") specified here.
- Width CHOP `widthchop` - A 1 channel CHOP can be specified to set the width of the quad at that sample.
- Color CHOP `colorchop` - A 3 channel CHOP can be specified to set the R, G, and B color values of the quad at that sample.
- Alpha CHOP `alphachop` - A 1 channel CHOP can be specified to set the alpha of the quad at that sample.
- Perspective Width `perspectivewidth` - The width of the geometry created. This parameter only has an effect when the Use Constant Width is less that 1.0.
- Use Constant Width `constantwidth` - This blends between using Perspective Width and Constant Width. When Use Constant Width = 0, width is determined only by Perspective Width, when Use Constant Width = 1, width is determined only by Constant Width parameters below.
- Constant Width Near `constantwidthnear` - The width used for quads located at a position Constant Width Falloff Start or closer.
- Constant Width Far `constantwitdhfar` - The width used for quads located at a position Constant Width Falloff End or farther.
- Constant Width Falloff Start `falloffstart` - At this position the or closer the geometry uses the Constant Width Near parameter for its width.
- Constant Width Falloff End `falloffend` - At this position the or farther the geometry uses the Constant Width Far parameter for its width.
**NOTE** : Inbetween Falloff Start and Falloff End the width is determined using a half-cosine falloff between the two values.

## Info CHOP Channels
Extra Information for the Sprite SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
