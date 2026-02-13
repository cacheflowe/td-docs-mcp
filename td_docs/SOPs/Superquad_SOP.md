---
url: https://docs.derivative.ca/Superquad_SOP
category: SOPs
title: Superquad_SOP
---

# Superquad SOP
## Summary

The Superquad SOP generates an isoquadric surface. This produces a spherical shape that is similar to a metaball, with the difference that it doesn't change it's shape in response to what surrounds it. You can change the XY Exponent of an isoquadric surface to define it to be more "squarish" or "starish" in shape. Also, an isoquadric surface is always defined as a polygonal or mesh type geometry.
[superquadSOP_Class](https://docs.derivative.ca/SuperquadSOP_Class "SuperquadSOP Class")

## Parameters - Page
- Primitive Type `type` - ⊞ - Select from the following types. For information on the different types, see the [Primitive](https://docs.derivative.ca/Primitive "Primitive") article. Depending on the primitive type chosen, some SOP options may not apply.
  * Polygon `poly` -
  * Mesh `mesh` -

- Connectivity `surftype` - ⊞ - This option is used to select the type of surface, when using a Mesh primitive type.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon).
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Modify Bounds `modifybounds` - Available only when an input is connected to the Superquad SOP to set bounds for the superquad. When Modify Bounds = On the transform parameters below will further modify the position and radius of the bounds.
- Radius `rad` - ⊞ - Determines overall radius.
  * X `radx` -
  * Y `rady` -
  * Z `radz` -

- Center `t` - ⊞ - Offset of superquad center from object center.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Anchor W `anchorw` - Set the point in Z about which the geometry is positioned, scaled and rotated.
- Orientation `orient` - ⊞ - Determines pole axis for the iso surface.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Rows `rows` - Number of rows used in the superquad.
- Columns `cols` - Number of columns used in the superquad.
- XY Exponent `expxy` - The XY Exponent determines inflation / contraction in the X and Y axes.
- Z Exponent `expz` - The Z Exponent determines inflation / contraction in the Z axis. See the [Metaball SOP](https://docs.derivative.ca/Metaball_SOP "Metaball SOP") for a description of exponents.
- Multiple Points per Pole `upole` - Determines whether points at the poles are shared or are unique to the columns.
- Cusp Polygons `cusp` - Makes points unique, causing the superquad to be faceted.
- Cusp Angle `angle` - Input angle in degrees to determine when vertices are shared or not, creating cusping.
- Texture Coordinates `texture` - ⊞ - Adds UV texture coordinates to the sphere.
  * Off `off` - No UV coordinates added to surface.
  * Row & Columns `rowcol` - Adds vertex UV coordinates.

- Compute Normals `normals` - Creates normals on the geometry.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Superquad SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
