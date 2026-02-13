---
url: https://docs.derivative.ca/Curveclay_SOP
category: SOPs
title: Curveclay_SOP
---

# Curveclay SOP
## Summary

The Curveclay SOP is similar to the Clay SOP in that you deform a spline surface not by modifying the CVs but by directly manipulating the surface. However, instead of using a point on the surface, you use one or more faces to deform that surface. Also, CurveClay does not yet support polygonal meshes.

The combination of inputs will determine the modes of transformation. For any combination of inputs, the following parameters modify the following behaviors of the SOP.
[curveclaySOP_Class](https://docs.derivative.ca/CurveclaySOP_Class "CurveclaySOP Class")

## Parameters - Curve Clay Page
- Face Group `facegroup` - Subset of faces (NURBS, Bézier, Polygons) to project, or subset of proles to deform, depending on how many inputs are connected.
Examples include: 0.5 1.2-3.9 5.*
This group can even take surfaces (possibly intermixed with profile curves) when the 2nd input is not present, indicating that all the surface’s proles must be used.
Then, the example above becomes: 0.5 1.2-3.9 5
- Surface Group `surfgroup` - Subset of spline surfaces to be deformed when all three SOP inputs are connected.
- Divisions on Face `divs` - The number of points to evaluate on the proles or the faces. This SOP works by using a straight line approximation of the given curve to deform the surface. Thus, more segments are slower, but the result looks better. Fewer divisions need to be specified when deforming proles and when the rest and deforming faces have an equal number of breakpoints.
- Sharpness `sharp` - Species the area around the face to deform. The larger the sharpness is, the smaller the deformation area around them (thus having a sharper pull on the surface).
- Refinement `refine` - Usually, CurveClay automatically renes the surface. However, you may specify some degree of renement control. In general, the more rened the surface is, the smoother the result. Better renement results in a denser surface. You should experiment with values between -1 and 1. When the value is negative, the SOP will rst rene the surface to the same detail level as when renement is 0, and then it unrenes it. The lower the value, the more unrened it becomes.

## Parameters - Projection Page
Controls curve projection. Enabled if all 3 inputs exist.
- Projection Axis `projop` - ⊞ - Choice of several projection axes:
  * X `xaxis` - Cartesian Axis - X, Y, or Z.
  * Y `yaxis` - Cartesian Axis - X, Y, or Z.
  * Z `zaxis` - Cartesian Axis - X, Y, or Z.
  * Minimum Distance `mindist` - Project curve points to their closest places on surface.
  * User Defined: `other` - Enter Vector into the field below.

`projdir` - ⊞ - Specify the direction vector of the projection.
  * `projdir1` -
  * `projdir2` -
  * `projdir3` -

## Parameters - Displacement Page
How to deform surface. Enabled if only 1 input exists.
- Displacement Axis `deformop` - ⊞ - Choice of several projection axes:
  * Surface Normal `snormal` - The proles will be deformed along the surface normal.
  * X `xaxis` - Cartesian axis - X, Y, or Z.
  * Y `yaxis` - Cartesian axis - X, Y, or Z.
  * Z `zaxis` - Cartesian axis - X, Y, or Z.
  * User Defined: `other` - Enter the vector into the eld below.

`deformdir` - ⊞ - Specify the direction vector of the displacement.
  * `deformdir1` -
  * `deformdir2` -
  * `deformdir3` -

- Distance `deformlen` - Distance deformed along the vector.
- Deform Inside of Loop `deforminside` - Check if the inside of closed loops should be deformed.
- Consider Profiles Individually `individual` - Check if multiple curves form a closed loop.

## Notes
When using CurveClay on a wrapped surface, here are some points to remember:
  * You may want to use a higher number of divisions, since when going across the seam of the wrapped surface, straight line approximation would be turned off and more sample points may be needed.
  * If you’re not going across the seam, then the reﬁnement of the surface is only local. However, when the deformation area of the surface gets near the seam, the reﬁnement is done over the whole surface. Do not be alarmed if the whole surface has been reﬁned.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Curveclay SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
