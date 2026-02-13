---
url: https://docs.derivative.ca/Torus_SOP
category: SOPs
title: Torus_SOP
---

# Torus SOP
## Summary

The Torus SOP generates complete or specific sections of torus shapes (like a doughnut).
[torusSOP_Class](https://docs.derivative.ca/TorusSOP_Class "TorusSOP Class")

## Parameters - Torus Page
- Primitive Type `type` - ⊞ - Select from the following types. For information on the different types, see the [Geometry](https://docs.derivative.ca/Category:Geometry "Category:Geometry") category articles.
  * Polygon `poly` -
  * Mesh `mesh` -
  * NURBS `nurbs` -
  * Bezier `bezier` -

- Connectivity `surftype` - ⊞ - This option is used to select the type of surface, when using a Mesh primitive type.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon).
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Orientation `orient` - ⊞ - The axis along which the torus is constructed.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Modify Bounds `modifybounds` - Enabled only when an input is connected to the Torus SOP to set bounds for the torus. Turn Modify Bounds = On to enable the transform parameters below to further modify the position and radius of the bounds.
- Radius `rad` - ⊞ - The first value (radx) defines the radius of the torus, the second value (rady) determines the radius of the inner ring.
[![TouchGeometry256.gif](https://docs.derivative.ca/images/4/4a/TouchGeometry256.gif)](https://docs.derivative.ca/File:TouchGeometry256.gif)
  * X `radx` -
  * Y `rady` -

- Center `t` - ⊞ - Offset of torus center from object origin.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Anchor W `anchorw` - Set the point in Z about which the geometry is positioned, scaled and rotated.
- Rows `rows` - The rows define the number of divisions along the torus.
- Columns `cols` - The columns determine the number of divisions along the torus' cross-section.

## Parameters - Detail Page
- Angle Offset `angleoffset` - Rotates the torus along the minor radius. For example, if using 4 rows set this value to 45 to create flat top + bottom surfaces.
- Imperfect `imperfect` - This option applies only to Bezier and NURBS types. If selected, the tube is an approximated nonrational curve, otherwise it is a perfect rational curve.
- U Order `orderu` - If a spline curve is selected, it is built at this order for U and V.
- V Order `orderv` - If a spline curve is selected, it is built at this order for U and V.
- U Angle `angleu` - ⊞ - The start and end sweep angles of the torus, if U Wrap is not enabled.
  * `beginangleu` -
  * `endangleu` -

- V Angle `anglev` - ⊞ - These are the start and end angles of the cross-section circle that is swept to make the torus, if V Wrap is not enabled.
  * `beginanglev` -
  * `endanglev` -

- U Wrap `closeu` - If U Wrap is checked, it creates a 360 cross-section.
- V Wrap `closev` - Checking V Wrap creates a torus along V by closing the primitive.
- U End Caps `capu` - If U End Caps is checked, it puts faceted end-caps on the ends of the torus if it is less than 360.
For more capping options, turn this parameter off, and append a Cap SOP.
- V End Caps `capv` - If V End Caps is checked, it applies a face between the top and bottom of the torus - if the torus is open.
For more capping options, turn this parameter off, and append a Cap SOP.

- Texture Coordinates `texture` - ⊞ - This adds uv coordinates to the geometry created by the Torus SOP.
  * Off `off` - No uv coordinates added.
  * Row & Columns `rowcol` - uv coordinates added based on Rows and Columns in the geometry.

- Compute Normals `normals` - Checking this option On will compute surface normals.
## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Torus SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
