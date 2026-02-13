---
url: https://docs.derivative.ca/Rails_SOP
category: SOPs
title: Rails_SOP
---

# Rails SOP
## Summary

The Rails SOP generates surfaces by stretching cross-sections between two rails. This is similar to the [Sweep SOP](https://docs.derivative.ca/Sweep_SOP "Sweep SOP"), but it gives more control over the orientation and scaling of the cross-sections. The first SOP input is the cross-section which will be replicated, and is typically placed in the XY plane. The second input SOP source is the rails along which the cross-section is replicated.
[railsSOP_Class](https://docs.derivative.ca/RailsSOP_Class "RailsSOP Class")

## Parameters - Page
- X-Section Groups `xsectgrp` - You can use a subset of primitives from the Cross-section input by specifying a group here. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rail Groups `railgrp` - You can use a subset of primitives from the Rails input by specifying a group here. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Cycle Type `cycle` - ⊞ - Select how the cross=section is applied along the rails.
  * All Primitives at Each Point `all` - Places all the primitives from the Cross-section input at each point on the backbone.
  * One Primitive at a Time `each` - Similar to the above, except the transformation is applied to individual primitives rather than to the whole.
  * Cycle Primitives `cycle` - This cycles through incoming primitives when placing them on a backbone. i.e. Start with 0 at vertex 0, primitive 1 at vertex 1, etc.

- Sweep along Pairs of Rails `pairs` - Sweeps along rail 1 & 2, 3 & 4, 5 & 6 etc. instead of 1 & 2, 2 & 3, 3 & 4 etc.
- Sweep along First and Last Rail `firstl` - Connects the cross-section between the first and last rails.
- Stretch to Rails `stretch` - Stretches the cross-section geometry to the rail geometry.
- Use Vertex `usevtx` - Specifies two vertices of the cross section polygon to be placed on rail1 and rail2 respectively. Very useful, for instance, to keep the first vertex on rail1 and the seventh vertex on rail2.
- Connection Vertices `vertex` - ⊞ - The vertices at which the cross-section is connected to the rails.
  * `vertex1` -
  * `vertex2` -

- Scale `scale` - Global scaling of the cross-sections.
- Roll `roll` - Non-cumulative rotation of the cross sections around the backbone. All cross sections get the same rotation.
- Fix Flipping `noflip` - Option to correct the flipping when no direction vector is used and the two rails happen to cross each other causing the normal to flip upside down.
- Use Direction `usedir` - Uses the direction vector specified in the X, Y and Z coordinates. Otherwise it will use the normals of the geometry.
- Direction `dir` - ⊞ - The direction vector to use.
  * X `dirx` -
  * Y `diry` -
  * Z `dirz` -

- Create Output Groups `newg` - Selecting this option enables the creation of groups. A group is created for each backbone that is incoming. This allows for easy skinning in the [Skin SOP](https://docs.derivative.ca/Skin_SOP "Skin SOP").
- Group Name `railname` - Specify the name of your output groups in this field. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Rails SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
