---
url: https://docs.derivative.ca/Sphere_SOP
category: SOPs
title: Sphere_SOP
---

# Sphere SOP
## Summary

The Sphere SOP generates spherical objects of different geometry types. It is capable of creating non-uniform scalable spheres of all geometry types.
If an input is provided, the sphere's radius is automatically determined as a function of the input's bounding geometry.
[sphereSOP_Class](https://docs.derivative.ca/SphereSOP_Class "SphereSOP Class")

## Parameters - Page
- Primitive Type `type` - ⊞ - Select from the following types. For information on the different types, see the [Geometry](https://docs.derivative.ca/Category:Geometry "Category:Geometry") category articles. Depending on the primitive type chosen, some SOP options may not apply. Using the 'Primitive' primitive type is not recommended when using instancing.
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

- Orient Bounds `orientbounds` - Available only when an input is connected to the Sphere SOP to set bounds for the sphere. When Orient Bounds = On it will rotate the geometry to match the orientation of the input SOP used for bounds.
- Modify Bounds `modifybounds` - Available only when an input is connected to the Sphere SOP to set bounds for the sphere. When Modify Bounds = On the transform parameters below will further modify the rotation, position, and radius of the bounds.
- Rotate Order `rord` - ⊞ - Sets the order in which the rotations are applied.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Radius `rad` - ⊞ - The radius of the sphere in X, Y and Z.
  * X `radx` -
  * Y `rady` -
  * Z `radz` -

- Center `t` - ⊞ - Offset of sphere center from object center.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the Sphere along the X, Y, and Z axes.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Anchor W `anchorw` - Set the point in Z about which the geometry is positioned, scaled and rotated.
- Orientation `orient` - ⊞ - Determines axis for sphere. Poles of sphere align with orientation axis.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -

- Frequency `freq` - This controls the level of polygons used to create the sphere, when using the Polygon Primitive Type.
- Rows `rows` - Number of rows in a sphere when using the mesh, imperfect NURBS and imperfect Bzier.
- Columns `cols` - Number of columns in a sphere when using the mesh, imperfect NURBS and imperfect Bzier.
- U Order `orderu` - If a spline curve is selected, it is built at this order for U.
- V Order `orderv` - If a spline curve is selected, it is built at this order for V.
- Imperfect `imperfect` - This option applies only to Bzier and NURBS spheres. If selected, the spheres are approximated nonrational curves, otherwise they are perfect rational curves.
- Unique Points per Pole `upole` - Applies to Mesh, NURBS and Bzier surfaces only. This option determines whether points at the poles are shared or are individual to the columns.
- Accurate Bounds `accurate` - If the SOP is being used to generate a bounding sphere for it's input geometry, this parameter tells the SOP to use a more accurate (but slower) bounding sphere calculation.
- Texture Coordinates `texture` - ⊞ - Adds UV texture coordinates to the sphere.
  * Off `off` - No UV coordinates added to surface.
  * By Primitive Type `byprimtype` - Adds vertex UV coordinates.
  * Equirectangular Inside (Spherical Polar) `equirectangularin` -
  * Equirectangular Outside (Spherical Polar) `equirectangularout` -
  * Equidistant Azimuth (Fish Eye 180) `equiazimuth` -
  * Equidistant Azimuth (Fish Eye 360) `equiazimuth360` -

- Compute Normals `normals` - Creates normals on the geometry.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Sphere SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
