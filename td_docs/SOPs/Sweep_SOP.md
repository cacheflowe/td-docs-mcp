---
url: https://docs.derivative.ca/Sweep_SOP
category: SOPs
title: Sweep_SOP
---

# Sweep SOP
## Summary

The Sweep SOP sweeps primitives in the Cross-section input along Backbone Source primitive(s), creating ribbon and tube-like shapes. The cross-section primitives are placed at each point of the backbone perpendicular to it. The Backbone Source can have one or several primitives. If there is more than one, Sweep will sweep the cross section along each one.
A backbone is a primitive curve that can be open or closed, but must have at least two points. The cross section input can also have multiple primitives, and can be assigned to the backbone in various ways. The origin of the cross section primitive is placed at a point on the backbone by default, but you can also choose a point number of the cross section to place. In most cases, it is best to build 1the cross section primitives in the XY plane; Sweep will automatically orient them properly along the backbone. The orientation of the cross section is based on the direction of the backbone line segment and the positive Z axis. So vertical movement in the backbone will result in the cross section rotating around backbone axis. For example, if you create the cross section in the XY plane, you can maintain its orientation (+Y Up) by building the backbone in the XZ plane.
If the backbone primitive(s) have point colors or texture coordinates, they will be maintained and applied to the cross section primitives.
[sweepSOP_Class](https://docs.derivative.ca/SweepSOP_Class "SweepSOP Class")

## Parameters - Sweep Page
- X-Section Group `xgrp` - You can use only a subset of primitives from the Cross-section inputs by specifying a group here.
- Path Group `pathgrp` - You can use only a subset of primitives from the Backbone inputs by specifying a group here.
- Reference Group `refgrp` - You can use only a subset of primitives from the Reference inputs by specifying a group here.
- Cycle Type `cycle` - ⊞ - Determines the Cycle Type based on these menu options.
  * All Primitives at Each Point `all` - Places all the primitives from the Cross-section input at each point on the Backbone.
  * One Primitive at a Time `each` - Similar to the above, except the transformation is applied to individual primitives rather than to the whole.
  * Cycle Primitives `cycle` - This cycles through incoming primitives when placing them on a backbone. i.e. Start with 0 at vertex 0, primitive 1 > vertex 1, etc.

- Angle Fix `angle` - Attempts to fix buckling twists that may occur when sweeping.
- Fix Flipping `noflip` - Attempts to fix buckling twists that may occur when sweeping by fixing flipped normals.
- Remove Coincident Points on Path `skipcoin` - When selected, any points right on top of one another will be ignored.
- Aim at Reference Points `aimatref` - Reference Points are used in conjunction with the backbone to control the orientation of the elements along the sweep. This is done by drawing a line between the reference point and corresponding backbone point in order to determine an angle vector which determines the orientation of the cross-section profiles. Enable this parameter to allow this behaviour.
**Note:** In order for this to work, you must supply **Reference Points** via the third input, and there must be exactly the same number of **Reference Points** as there are points in the **Backbone**.
- Use Vertex `usevtx` - Use vertex number of the incoming cross-section to place the cross-section on the backbone.
- Connection Vertex `vertex` - Specify a specific vertex to connect to the backbone.
- Scale `scale` - Scales the cross sections globally.
- Twist `twist` - Cumulative rotation of the cross sections around the backbone. If a value of five is specified, the cross section at the first point of the backbone is rotated five degrees, the next ten degrees, the next fifteen degrees and so on.
- Roll `roll` - Non-cumulative rotation of the cross sections around the backbone. All cross sections get the same rotation.
**Note:** The **Scale** , **Twist** and **Roll** parameters can now be controlled directly by points' attributes of the same names. Thus, combined with the [Channel SOP](https://docs.derivative.ca/CHOP_to_SOP "CHOP to SOP"), those parameters can now be controlled dynamically. You can use scale and other attributes coming in to taper.

## Parameters - Output Page
- Create Groups `newg` - Selecting this option enables the creation of groups. A group is created for each backbone that is incoming. This allows for easy skinning in the [Skin SOP](https://docs.derivative.ca/Skin_SOP "Skin SOP").
- Sweep Groups `sweepgrp` - Specify the name of your output groups in this field.
- Skin Output `skin` - ⊞ - Determines the output based on these menu options.
  * Off `off` - Doesn't skin the output.
  * On `on` - Skins the output.
  * On with Auto Close `auto` - Closes the skinned mesh if the path curve which it follows is also closed. This allows you to close primitives properly.

**Tip:** There is a way of speeding the skinning of many points using the second input of the [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"). Suppose you have Thousands of proceedurally animated curves you wish to skin with the Sweep SOP - rather than performing a skining operation after the animation, make a second set of unanimated geometry that is preskinned. Then assuming your have a matching number of points you can just swap in the animated points into the skinned geometry.
This technique is significantly faster than using the Skin Output option of the Sweep SOP, or a Skin SOP following the Sweep SOP.
- Fast Sweep `fast` - Enables an optimized skinning technique which speeds up output from 2 - 4 times in many cases at the expense of accuracy. In order for it to work correctly, the input topologies must remain consistent between cooks and each cross-section must have the same number of vertices.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Sweep SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
