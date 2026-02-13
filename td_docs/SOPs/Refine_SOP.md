---
url: https://docs.derivative.ca/Refine_SOP
category: SOPs
title: Refine_SOP
---

# Refine SOP
## Summary

The Refine SOP allows you to increase the number of CVs in any NURBS, Bzier, or polygonal surface or face without changing its shape. It is also used to decrease the number of CVs within a given tolerance (i.e. a simple but fast method of data reduction).
###
The Difference Between Refinement and Unrefinement
Refinement and unrefinement work both on faces (polygons, Bzier curves and NURBS curves) and surfaces (primitive meshes, Bzier surfaces and NURBS surfaces). To unrefine a face or a surface you need to specify a parametric interval (not just a single value as in refinement). This allows you to unrefine primitives within arbitrary intervals, either locally or globally. For example, to unrefine the whole primitive choose 0 and 1 as the two parametric boundaries; [0,0.5] will unrefine only the first parametric half of the primitive.
The interval boundaries are given by the First/Second U/V fields. Since refinement does not need an interval, the Second U/V fields are disabled by default.
The Tolerance control is only available for unrefinement, and not for refinement. Refinement does not need tolerances because it generates a curve or a surface that is mathematically identical to the original. Unrefinement, however, may tend to smooth out (or "melt") the original in a given area. In short, unrefinement is lossy; refinement isn't.
[refineSOP_Class](https://docs.derivative.ca/RefineSOP_Class "RefineSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- First U `firstu` - Enable or disable the First U controls.
- First U `domainu1` - This specifies a starting / ending location to complete the operation. Select this and a parametric U location between 0 and 1.
- Second U `secondu` - Enable or disable the Second U controls.
- Second U `domainu2` - This specifies a starting / ending location to complete the operation. Select this and a parametric U location between 0 and 1.
- U Divisions `divsu` - If refining or sub-dividing, this option specifies the number of refines to be performed between First U and Second U.
- First V `firstv` - Enable or disable the First V controls.
- First V `domainv1` - This specifies a starting / ending location to complete the operation. Select this and a parametric V location between 0 and 1.
- Second V `secondv` - Enable or disable the Second V controls.
- Second V `domainv2` - This specifies a starting / ending location to complete the operation. Select this and a parametric V location between 0 and 1.
- V Divisions `divsv` - If refining or sub-dividing, this option specifies the number of refines to be performed between First V and Second V.

## Parameters - Refine Page
If enabled, will refine the primitive at the locations specified above. If the primitive is a NURBS, then a knot is inserted multiple times as described below.
- NURB Count U `refineu` - Number of knots to insert at each location in the U / V basis when refining NURBS.
- NURB Count V `refinev` - Number of knots to insert at each location in the U / V basis when refining NURBS.
- Spacing `space` - ⊞ - Specify how to measure along splines / curves.
  * Uniform Domain Lengths `domain` - Refine at equal basis intervals if refining a spline.
  * Uniform Arc Lengths `arc` - Each refinement is done at the centre of the maximum knot span (splines) or edge length (polygons).

**Note:** **Uniform Domain Lengths** should be selected if the domain ranges are animating, otherwise the inserted points will be undeterminable as different maximum lengths are encountered.

## Parameters - Unrefine Page
If enabled, will remove CVs from any NURBS curve or surface, polygon or mesh (points/ rows removed) between First U and Second U, and First V and Second V.
- NURB Count U `unrefineu` - Number of knots to remove at each location in the U / V basis if refining NURBS.
- NURB Count V `unrefinev` - Number of knots to remove at each location in the U / V basis if refining NURBS.
- Tolerance U `tolu` - Only remove knots that do change the curve, polygon, or surface by more than this distance.
- Tolerance V `tolv` - Only remove knots that do change the curve, polygon, or surface by more than this distance.

## Parameters - Subdivide Page
Subdivide refines a primitive such that the subdivision causes a sharp discontinuity if ever displaced. In essence subdivide is equivalent to refine for polygons and Bziers, since any refinement causes a potential discontinuity. In the case of a NURBS it is equivalent to a maximum refinement (i.e. count = primitive basis order - 1).
- Spacing `subdivspace` - ⊞ - Subdivide refines a primitive such that the subdivision causes a sharp discontinuity if ever displaced. In essence subdivide is equivalent to refine for polygons and Bziers, since any refinement causes a potential discontinuity. In the case of a NURBS it is equivalent to a maximum refinement (i.e. count = primitive basis order - 1).
  * Uniform Domain Lengths `domain` - Refine at equal basis intervals if refining a spline.
  * Uniform Arc Lengths `arc` - Each refinement is done at the centre of the maximum knot span (splines) or edge length (polygons).

**Note:** **Uniform Domain Lengths** should be selected if the domain ranges are animating, otherwise the inserted points will be undeterminable as different maximum lengths are encountered.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Refine SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
