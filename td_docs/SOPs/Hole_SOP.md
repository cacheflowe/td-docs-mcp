---
url: https://docs.derivative.ca/Hole_SOP
category: SOPs
title: Hole_SOP
---

# Hole SOP
## Summary

The Hole SOP is for making holes where faces are enclosed, even if they are not in the same plane. It can also remove existing holes from the input geometry.
The holes are made by searching for faces which are enclosed by other faces and creating bridges to the interior faces. It offers more flexibility than either the [Extrude SOP](https://docs.derivative.ca/Extrude_SOP "Extrude SOP") or [Divide SOP](https://docs.derivative.ca/Divide_SOP "Divide SOP")'s hole-making capabilities because it can deal with interior faces which are not exactly in the same orientation as the exterior ones. It can also remove existing bridges that it finds in the input geometry if needed.
**Note:** This SOP works with Polygonal and Bezier geometry types only. NURBS surfaces will be converted internally to Beziers.
[holeSOP_Class](https://docs.derivative.ca/HoleSOP_Class "HoleSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Unbridge Holes `unbridge` - This function checks for bridges to holes in the input and removes the bridges, leaving the interior freestanding. At times you may need to unhole faces so that you can connect them in some other way.
- Distance Tolerance `dist` - Interior polygons that are not in exactly the same plane as the exteriors can still become holes. The Distance Tolerance value tells the Hole SOP how far away potential holes can be from the exterior surfaces. Faces beyond this distance will not become holes.
- Angle Tolerance `angle` - Interior faces that are rotated in relation to the exterior faces can become holes. The Angle value sets the maximum rotation of the potential holes from the exteriors. Faces beyond this rotation will not become holes.
- Snap Holes to Outlines `snap` - Points of any holes that are rotated or translated away from the exterior (or outline) plane will be moved so that they lie on the surface of the outline plane, thus avoiding twisted faces.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Hole SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
