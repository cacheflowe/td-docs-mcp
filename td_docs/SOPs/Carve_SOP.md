---
url: https://docs.derivative.ca/Carve_SOP
category: SOPs
title: Carve_SOP
---

# Carve SOP
## Summary

The Carve SOP works with any face or surface type, be that polygon, Bzier, or NURBS. It can be used to slice a primitive, cut it into multiple sections, or extract points or cross-sections from it.
Like the Project SOP, it also creates profile curves, but they are extracted as iso-parametric (2D) profiles directly from a surface, whereas the Project SOP extracts a 3D curve projected onto a surface.
Note: When using a Carve SOP on a trimmed surface, you can't fillet or join the trim curves.
[carveSOP_Class](https://docs.derivative.ca/CarveSOP_Class "CarveSOP Class")

## Parameters - Carve Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the Group specified. Accepts patterns, as described in the Scripting Guide under Pattern Matching.
- First U `firstu` - Enables the parameter to set the first position in U.
- First U `domainu1` - This specifies a starting location to begin the cut/extract. Select this and a parametric U location between 0 and 1.
- Second U `secondu` - Enables the parameter to set the second position in U.
- Second U `domainu2` - This specifies an ending location to complete the cut / extract. Select this and a parametric U location between 0 and 1.
- First V `firstv` - Enables the parameter to set the first position in V.
- First V `domainv1` - This specifies a starting location to begin the cut/extract. Select this and a parametric V location between 0 and 1. Applies only to surfaces.
- Second V `secondv` - Enables the parameter to set the second position in V.
- Second V `domainv2` - This specifies an ending location to complete the cut / extract. Select this and a parametric V location between 0 and 1. Applies only to surfaces.

## Parameters - Method Page
- Carve Method `method` - ⊞ - Select between Cut and Extract methods.
  * Cut `cut` - Cut will slice (or 'cut-out') the original geometry within the area specified on the Carve Page.
  * Extract `extract` - Extract will create 3D curves, points, or 2D profiles within the area specified on the Carve page. The Extract Type parameter is used to determine what is extracted.

- Keep Inside `keepin` - Keep the primitives specified between the first and second locations.
- Keep Outside `keepout` - Keep the primitives lying outside the first and second locations.
- Extract Type `extractop` - ⊞ - If enabled, it will extract a cross-section along each location specified above.
Note: if a face is used, only points can be extracted and the V parameters have no effect.
  * Extract 3D Isoparametric Curve(s) `xisoparm` - The extraction operation creates a 3-D, free-floating curve that matches the surface perfectly at the given U or V location.
  * Extract Point(s) `xpoint` - Available for Mesh and surfaces only. If selected, it will create a point at every U, V location specified, rather than removing a U cross section and a V cross section.
  * Extract 2D Isoparametric Profile(s) `xprofile` - Creates a 2D curve at the specified U/V location that matches the surface perfectly.

- Keep Original `keeporiginal` - If selected, it will not remove the original primitive.
- Location `location` - ⊞ - Determines how the Cut/Extract is defined at the boundaries. Additionally, extra subdivisions can be added in two ways using the parameters below.
  * Divisions `div` - The Cut/Extract occurs precisely at the locations defined on the Carve page. Additional divisions can be specified using the U/V Divisions parameters below and they are evenly distributed across the Cut/Extracted geoemtry.
  * Breakpoints `break` - Performs cutting or extractions at breakpoints for curves and surfaces, at vertices for polygons, and along isoparms for meshes.

By default this option will only cut the outer breakpoints within the specified interval. By selecting Breakpoints, the U and V Divisions parameters are replaced with Cut At All Internal U/V Breakpoints, which cut the primitives at all breakpoints falling within the specified interval when enabled.
- U Divisions `divsu` - This specifies the number of cuts / extracts to be performed between first U and the second U.
- V Divisions `divsv` - Specifies the number of cuts/extracts to be performed between first V and second V.
- Cut at All Internal U Breakpoints `allubreakpoints` - When using Location = Breakpoints, the resulting primitive is divided at all U breakpoints into separate primitives.
- Cut at All Internal V Breakpoints `allvbreakpoints` - When using Location = Breakpoints, the resulting primitive is divided at all V breakpoints into separate primitives.

## Example
###
Opening a Closed Primitive
Given a closed surface, it can be converted to an identical open surface at any location by using the Carve SOP, and cutting at a single location (e.g. First U enabled, Second U disabled). The same is true for faces.

###
Dicing a Face or Surface
Select the Cut operation, First U = `0`, Second U = `1`, First V = `0`, Second V = `1`, with (at least) three Divisions for U and V. This will dice the surface into (at least) 3 components. This can later be used with the Primitive SOP to "explode" the surface.

###
Cutting a Hole in a Surface
Select the Cut operation, First U = `0.33`, Second U = `0.66`, First V = `0.33`, Second V = `0.66`, `2` Divisions for U and V. Keep Inside is off, Keep Outside is on. This will cut a rectangular region from the centre of the surface.

###
Animating a Point Over a Face or Surface
Select the Extract option, First U = `x`, Last U disabled, First V = `y`, Last V disabled, Extract Point is on, Keep Primitives is optional. This will create a point over any position on the surface (0<=x<=1, 0<=y<=1).

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Carve SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
