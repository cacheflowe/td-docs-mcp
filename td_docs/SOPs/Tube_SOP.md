---
url: https://docs.derivative.ca/Tube_SOP
category: SOPs
title: Tube_SOP
---

# Tube SOP
## Summary

The Tube SOP generates open or closed tubes, cones, or pyramids along the X, Y or Z axes. It outputs as meshes, polygons or simply a tube [Primitive](https://docs.derivative.ca/Primitive "Primitive").
[tubeSOP_Class](https://docs.derivative.ca/TubeSOP_Class "TubeSOP Class")

## Parameters - Tube Page
- Primitive Type `type` - ⊞ - Select from the following types. For information on the different types, see the [Geometry](https://docs.derivative.ca/Category:Geometry "Category:Geometry") category articles. Using the 'Primitive' primitive type is not recommended when using instancing.
  * Primitive `prim` -
  * Polygon `poly` -
  * Mesh `mesh` -
  * NURBS `nurbs` -
  * Bezier `bezier` -

- Connectivity `surftype` - ⊞ - This option is used to select the type of surface, when using a Mesh Primitive Type.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon).
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Orientation `orient` - ⊞ - Primary axis of tube (long axis).
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Orient Bounds `orientbounds` - Available only when an input is connected to the Tube SOP to set bounds for the tube. When Orient Bounds = On it will rotate the geometry to match the orientation of the input SOP used for bounds.
- Modify Bounds `modifybounds` - Enabled only when an input is connected to the Tube SOP to set bounds for the tube. Turn Modify Bounds = On to enable the transform parameters below to further modify the position, scale, radius and height of the bounds.
- Rotate Order `rord` - ⊞ - Sets the order in which the rotations are applied.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Center `t` - ⊞ - Location of the tube center from the object origin.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the Tube along the X, Y, and Z axes.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Radius `rad` - ⊞ - The first field is the radius of the top of the tube and the second field represents the radius of the bottom of the tube.
  * `rad1` -
  * `rad2` -

- Height `height` - The height of the tube.
- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Anchor W `anchorw` - Set the point in Z about which the geometry is positioned, scaled and rotated.
- Imperfect `imperfect` - This option applies only to Bezier and NURBS types. If selected, the tube is an approximated nonrational curve, otherwise it is a perfect rational curve.

## Parameters - Detail Page
- Rows `rows` - Number of rows in tube.
- Columns `cols` - Number of columns in tube.
- U Order `orderu` - If a spline surface is selected, it is built at this order for U.
- V Order `orderv` - If a spline surface is selected, it is built at this order for V.
- End Caps `cap` - If selected, it adds faceted end caps to the ends of the tube.
- Texture Coordinates `texture` - ⊞ - Adds UV texture coordinates to the sphere.
  * Off `off` - No UV coordinates added to surface.
  * Row & Columns `rowcol` - Adds vertex UV coordinates.

- Compute Normals `normals` - Checking this option On will compute surface normals.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Tube SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
