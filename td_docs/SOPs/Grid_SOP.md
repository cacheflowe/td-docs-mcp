---
url: https://docs.derivative.ca/Grid_SOP
category: SOPs
title: Grid_SOP
---

# Grid SOP
## Summary

The Grid SOP allows you to create grids and rectangles using polygons, a mesh, Bzier and NURBS surfaces, or multiple lines using open polygons.
[gridSOP_Class](https://docs.derivative.ca/GridSOP_Class "GridSOP Class")

## Parameters - Page
- Primitive Type `type` - ⊞ - Select from the following types. For information on the different types, see the Geometry Types section. Depending on the primitive type chosen, some SOP options may not apply.
  * Polygon `poly` -
  * Mesh `mesh` -
  * NURBS `nurbs` -
  * Bezier `bezier` -

- Connectivity `surftype` - ⊞ - (Results only viewable for polygons and meshes).
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wireframe display, but all polygons are open (if the primitive type is polygon). Compare them in the Model Editor.
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Orientation `orient` - ⊞ - Specifies on which plane the Grid is built.
  * XY Plane `xy` -
  * YZ Plane `yz` -
  * ZX Plane `zx` -

- Modify Bounds `modifybounds` - Enabled only when an input is connected to the Grid SOP to set bounds for the grid. Turn Modify Bounds = On to enable the transform parameters below to further modify the position and scale of the bounds.
- Size `size` - ⊞ - The X and Y scale of the grid.
  * X `sizex` -
  * Y `sizey` -

- Center `t` - ⊞ - Center of grid in X, Y, and Z.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Rows `rows` - The number of rows and columns. Rows are horizontal lines; Columns are vertical lines. Two rows by two columns makes a square or rectangle. For example, one row and two columns makes a single line if Connectivity is set to Rows.
For NURBS and Bzier surfaces, the Rows & Cols refer to the surface hull construction, and as such, the number of Rows and Cols should not be less than the Order in U or V.
- Columns `cols` - The number of rows and columns. Rows are horizontal lines; Columns are vertical lines. Two rows by two columns makes a square or rectangle. For example, one row and two columns makes a single line if Connectivity is set to Rows.
For NURBS and Bzier surfaces, the Rows & Cols refer to the surface hull construction, and as such, the number of Rows and Cols should not be less than the Order in U or V.
- U Order `orderu` - U Order Degree of spline basis +1 in the U parametric direction.
- V Order `orderv` - V Order Degree of spline basis +1 in the V parametric direction.
- End Point Interpolate in U `interpu` - End-point interpolate in U Extends the surface to touch the end point in the U direction.
- End Point Interpolate in V `interpv` - End-point interpolate in V Extends the surface to touch the end point in the V direction.
- Texture Coordinates `texture` - ⊞ - This adds uv coordinates to the geometry created by the Grid SOP.
  * Off `off` - No uv coordinates added.
  * Row & Columns `rowcol` - uv coordinates added based on Rows and Columns in the geometry.

- Compute Normals `normals` - Checking this option On will compute surface normals.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Grid SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
