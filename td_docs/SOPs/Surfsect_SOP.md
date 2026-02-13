---
url: https://docs.derivative.ca/Surfsect_SOP
category: SOPs
title: Surfsect_SOP
---

# Surfsect SOP
## Summary

The Surfsect SOP performs boolean operations with NURBS and Bezier surfaces, or only generates profiles where the surfaces intersect. The individual surfaces do not need to be solids (i.e. wrap in U and V), nor do they need to form a solid as a group (for example, you can cut a grid with a sphere).
The surfaces in the first input are denoted by "A" in the parameter list. The surfaces in the second input are denoted by "B". The entire A set is intersected with the B set, which allows for true csg operations with spline surfaces. Thus, if A forms a solid and B forms a solid, any boolean operation between A and B will produce a solid. If either set has an open topology, the result will also be open.
What is deemed to be the inside and outside of a trim region depends on the direction of the surface normals. If necessary, use the [Primitive SOP](https://docs.derivative.ca/Primitive_SOP "Primitive SOP") to reverse the surface normals by reversing the surface's U or V direction.
[surfsectSOP_Class](https://docs.derivative.ca/SurfsectSOP_Class "SurfsectSOP Class")

## Parameters - Page
- Group A `groupa` - Subset of NURBS and Bezier surfaces. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Group B `groupb` - Subset of NURBS and Bezier surfaces to intersect with A. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
3D Tolerance `tol3d` - World space precision of the intersection.
2D Tolerance `tol2d` - Domain precision of the intersection.
- Marching Steps `step` - Number of steps for tracing each profile span.

## Parameters - Boolean Page
Enables boolean operations between the surfaces in A and B:
- Operation `boolop` - ⊞ - Select from the following operations: Union, Intersect, A-B, B-A, or User-defined.
If the Operation is set to User-defined, the following options become available:
  * Union `union` -
  * Intersect `intersect` -
  * A minus B `aminusb` -
  * B minus A `bminusa` -
  * User Defined: `other` -

- Keep Inside A `insidea` - Preserve the inside sections of the A surfaces.
- Keep Inside B `insideb` - Preserve the inside sections of the B surfaces.
- Keep Outside A `outsidea` - Preserve the outside sections of the A surfaces.
- Keep Outside B `outsideb` - Preserve the outside sections of the B surfaces.

## Parameters - Generate Profiles Page
Just create profiles where the surfaces intersect.
- Target `target` - ⊞ - Which surface to output profiles for: A, B, or both.
  * A `a` -
  * B `b` -
  * A and B `both` -

- A Profiles Group `creategroupa` - Place the A profiles in a user-defined group.
`profilesa` - The name assigned to profile group A.
- B Profiles Group `creategroupb` - Place the B profiles in a user-defined group.
`profilesb` - The name assigned to profile group B.
- Avoid Already Trimmed-Out Parts `mindholes` - Intersect only the visible surface parts and truncate the intersection profile at the trimmed-in surface boundaries.
- Join Profiles Created by Multiple Surfaces `join` - If a surface has several adjacent profiles caused by its intersection with two or more surfaces, the profiles will be joined into a single curve-on-surface.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Surfsect SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
