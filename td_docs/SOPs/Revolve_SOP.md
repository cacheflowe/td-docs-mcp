---
url: https://docs.derivative.ca/Revolve_SOP
category: SOPs
title: Revolve_SOP
---

# Revolve SOP
## Summary

The Revolve SOP revolves faces to create a surface of revolution. The revolution's direction and origin are represented by guide geometry that resembles a thick line with a cross hair at the centre. The cross hair represents the origin of the revolve as entered in the dialog and the stick represents the direction. Changing any of these parameters will cause the guide to change appropriately.
If the guide geometry is too distracting, you can disable it by entering the Viewport options dialog and clicking on the Guide geometry button so that it no longer appears indented. This procedure is global and will disable the guide geometry of other SOPs as well.
[revolveSOP_Class](https://docs.derivative.ca/RevolveSOP_Class "RevolveSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this `SOP` to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").

## Parameters - Revolve Page
- Connectivity `surftype` - ⊞ - This option is used to select the type of surface, when using a Mesh Primitive Type.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon).
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Origin `origin` - ⊞ - Coordinates defining the origin of the revolution.
  * X `originx` -
  * Y `originy` -
  * Z `originz` -

- Direction `dir` - ⊞ - X, Y, and Z coordinates of the direction vector defining the direction of the revolve.
  * X `dirx` -
  * Y `diry` -
  * Z `dirz` -

- Convert Mesh to Polygons `polys` - Changes the output mesh to consist of individual polygons.
- Imperfect `imperfect` - Applies to splines only. If selected, the results are approximated nonrational curves, otherwise they are perfect rational curves.

## Parameters - Detail Page
- Revolve Type `type` - ⊞ - Determines how the revolve should be generated.
  * Closed `closed` - An enclosed curve.
  * Open Arc `openarc` - An open curve segment.
  * Closed Arc `closedarc` - An open arc with connecting edges to the centre resembling a slice of pie.

- Start End Angles `angle` - ⊞ - The start and end angles of the revolve. A revolve will start at the beginning angle, and proceed towards the ending angle. If Beginning = `0` and End = `360` it will be fully revolved. Values greater than 360 are also valid.
  * `beginangle` -
  * `endangle` -

- Divisions `divs` - Density of the resulting mesh surface.
- Order `order` - If a spline type is selected, it is built at this order.
- End Caps `cap` - If selected, it adds faceted end caps.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Revolve SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
