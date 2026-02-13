---
url: https://docs.derivative.ca/Join_SOP
category: SOPs
title: Join_SOP
---

# Join SOP
## Summary

The Join SOP connects a sequence of faces or surfaces into a single primitive that inherits their attributes. Faces of different types can be joined together, and so can surfaces. Mixed face-surface types are not allowed. The surfaces do not have to have the same number of rows or columns in the side being joined. Spline types of different orders and parameterization are all valid inputs. The Join SOP converts simpler primitives such as polygons into Bziers and NURBS if necessary.
Joining is different from filleting (see [Fillet SOP](https://docs.derivative.ca/Fillet_SOP "Fillet SOP")) or stitching (see [Stitch SOP](https://docs.derivative.ca/Stitch_SOP "Stitch SOP")) because it takes n primitives and converts them into one after possibly changing the connected ends of the primitives. Filleting creates a new primitive between each input pair and never affects the original shapes. Stitching changes the original shapes but does not change the number of resulting primitives.
[joinSOP_Class](https://docs.derivative.ca/JoinSOP_Class "JoinSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Blend `blend` - Determines the way the primitives are joined. A blended face or surface will typically reposition the ends to be joined and convert them into a single, common point, row or column respectively. The amount of change can be reduced or eliminated by lowering the tolerance (see Tolerance below). When not blended, the original shapes remain unaffected. Instead, the chosen ends are joined by an arc-like fillet. In either case, the result is a single primitive.
- Tolerance `tolerance` - The meaning of the tolerance varies with the type of join. The shapes of blended primitives will change less if the tolerance is low. If the tolerance is < `1`, a new point, knot, row or column is inserted between the last and before-last point, row or column. The lower the tolerance, the closer the insertion to the ends being pulled together, and thus the smaller the region affected. When the tolerance is zero the blended inputs do not change at all: the faces are connected by a straight line and the surfaces by a flatish, linear patch.
Tolerance also affects the size and roundness of the fillet built between non-blended primitives. A zero tolerance yields a short, flat fillet; a unit tolerance generates pointed, non self-intersected fillet.
- Bias `bias` - Affects only blended primitives by varying the position of the common point, row or column linearly between the two original ends. If the bias is zero, the common part will coincide with the end of the second primitive and the end of the first primitive will be stretched all the way to it. If the bias is one, the common part will coincide with the end of the first primitive and the second primitive will be stretched.
The bias is irrelevant when the blend tolerance is 0.
- Multiplicity `knotmult` - Affects the number of knots inserted at the blend point and thus allows for smooth or pointed connections. The connection will be pointed when the Multiplicity is on. When Blend is not on, an active multiplicity influences the shape and the tightness of the fillet by forcing a multiple knot insertion when on.
The fillet tends to be better behaved when multiplicity in on. However, this means that the resulting face or surface is built with a discontinuity at the connection points and might not lend itself to point modeling in that area too well.
Multiplicity has no effect on polygons and meshes.
- Connect Closest Ends `proximity` - The Join SOP connects the tail of the first primitive with the head on the next primitive, and so on unless this toggle is on, in which case the closest ends are chosen instead. For surfaces, this option enables the proximity test in U or V, as specified in the Direction parameter below.
- Direction `dir` - ⊞ - This menu determines the parametric direction of the joining operation, which can be in U or in V, and is meaningful only when the inputs are surfaces. The U direction is associated with columns; the V direction refers to rows. For example, joining two surfaces in U will generate a surface with more columns than either input. The number of rows might be higher too, but only if the two inputs have a different number of rows or a different V basis.
  * in U `ujoin` -
  * in V `vjoin` -

- Join `joinop` - ⊞ - Can optionally join subgroups of n primitives or every nth primitive in a cyclical manner.
**For Example** ; assume there are six primitives numbered for 0 - 5, and N = 2. Then,
  1. Groups will generate 0-1 2-3 4-5
  2. Skipping will generate 0-2-6 and 1-3-5.
  * All Primitives `all` -
  * Groups of N Primitives `group` -
  * Skip Every Nth Primitive `skip` -

- N `inc` - Determines the number of primitives to be either grouped or skipped. N2.
- Wrap Last to First `loop` - If enabled, it connects the beginning of the first primitive to the end of the last primitive, thus forming a single, closed face or hull. If a single, open primitive exists in the input, it will be closed. The [Primitive SOP](https://docs.derivative.ca/Primitive_SOP "Primitive SOP") provides a more direct way of closing primitives but offers almost no shape controls.
- Keep Primitives `prim` - If this button is not checked, the input primitives will be deleted after being joined. If checked, they will be preserved.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Join SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
