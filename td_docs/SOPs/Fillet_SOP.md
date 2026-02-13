---
url: https://docs.derivative.ca/Fillet_SOP
category: SOPs
title: Fillet_SOP
---

# Fillet SOP
## Summary

The Fillet SOP is used to create smooth bridging geometry between two curves / polygons or two surfaces / meshes.
Filleting creates a new primitive between each input pair and never affects the original shapes. This is in contrast to the [Join](https://docs.derivative.ca/Join_SOP "Join SOP") and [Stitch SOPs](https://docs.derivative.ca/Stitch_SOP "Stitch SOP"). The [Join SOP](https://docs.derivative.ca/Join_SOP "Join SOP") converts and possibly changes the connected ends of primitives, and stitching changes the original shapes but does not change the number of resulting primitives.
Please refer to the [Align SOP](https://docs.derivative.ca/Align_SOP "Align SOP") for a discussion of "left" and "right" primitives as well as the option of an auxiliary input.
Note: Trim curves are not taken into account by a fillet. To do this, use the Join SOP.
[filletSOP_Class](https://docs.derivative.ca/FilletSOP_Class "FilletSOP Class")

## Parameters - Page
- Group `group` - Which primitives to fillet. If blank, it fillets the entire input. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Fillet `fillet` - ⊞ - Can optionally fillet subgroups of N primitives or every nth primitive in a cyclical manner.
**Example** : Assume there are six primitives numbered for 0 - 5, and N = 2. Then:
  1. Groups will fillet 0-1 2-3 4-5
  2. Skipping will fillet 0-2-6 and 1-3-5.
  * All Primitives `all` -
  * Groups of N Primitives `group` -
  * Skip Every Nth Primitive `skip` -

- N `inc` - Determines the number of primitives to be either grouped or skipped.
- Wrap Last to First `loop` - Connects the beginning of the first primitive to the end of the last primitive filleted, or, if only one primitive exists, it creates a fillet between its ends.
- Direction `dir` - ⊞ - This menu determines the parametric direction of the filleting operation, which can be in U or in V, and is meaningful only when the inputs are surfaces. The U direction is associated with columns; the V direction refers to rows.
  * in U `ujoin` -
  * in V `vjoin` -

- Fillet Type `fillettype` - ⊞ - Select which type of fillet to use in this menu.
  * Freeform `freeform` - Allows full specifications of the fillet.
  * Convex `convex` - May negate scale values to ensure convex fillets.
  * Circular `circular` - Attempts to build a fillet as close to a radial arc as the shape and orientation of the inputs permit. You do not need to specify a radius - it is automatically determined to ensure a smooth connection between the inputs. As the two inputs come into proximity of each other, the fillet radius decreases. The tangent scales are ignored (as in the [Bridge SOP](https://docs.derivative.ca/Bridge_SOP "Bridge SOP")); only the sign of the tangent is taken into account in order to save you from needing to flip the normals of either input.

- Primitive Type `primtype` - ⊞ - Select what type of primitive will be created by the fillet in this menu.
  * Input Geometry Type `input` - Builds a fillet of the matching type between pairs of primitives. If the pair of primitives are different types, then the most general type is used (i.e. NURBS over Bzier, Bzier over polygons).
  * Polygon `polygon` - Builds a polygonal fillet between pairs of primitives.
  * NURBS `nurbs` - Builds a NURBS fillet between pairs of primitives at the given order.
  * Bezier `bezier` - Builds a Bzier fillet between pairs of primitives at the given order.

- Order `order` - Order at which to build the spline fillets.
- Left UV `leftuv` - ⊞ - Parametric point on each left primitive at which to begin the fillet.
  * `leftuv1` -
  * `leftuv2` -

- Right UV `rightuv` - ⊞ - Parametric point on each right primitive at which to begin the fillet.
  * `rightuv1` -
  * `rightuv2` -

- LR Width `lrwidth` - ⊞ - The first value represents the proportion of the left primitive that the left end of the fillet spans. The second value represents the proportion of the right primitive that the right end of the fillet spans.
  * `lrwidth1` -
  * `lrwidth2` -

- LR Scale `lrscale` - ⊞ - Use to control the direction and scale of the first and last segments of the fillet.
  * `lrscale1` -
  * `lrscale2` -

- LR Offset `lroffset` - ⊞ - Controls the position of the first and last segments of the fillet.
  * `lroffset1` -
  * `lroffset2` -

- Match Input to Fillets `seamless` - If selected, then the inputs are modified in such a way that the isoparms appear continuous from one primitive, through the fillet to the other primitive. Also, the primitives are promoted to the same type and order. This will minimize if not eliminate any artifacts introduced in rendering at the cost of more refined geometry.
- Cut Primitives `cut` - If selected, the primitives are trimmed at the point the fillet begins.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Fillet SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
