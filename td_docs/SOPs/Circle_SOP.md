---
url: https://docs.derivative.ca/Circle_SOP
category: SOPs
title: Circle_SOP
---

# Circle SOP
## Summary

The Circle SOP creates open or closed arcs, circles and ellipses.
If two NURBS circles that are non-rational (i.e. their X and Y radii are unequal) are skinned, more isoparms may be generated than expected. This is because non-rational NURBS circles parameterise their knots based on chord length, and the Skin SOP must consolidate the total number of knots between the two circles before skinning.
To remedy this, you may want to use a Refine SOP, and unrefine the resulting skin, or better yet - before unrefining, start with the same circle and use a Primitive or Transform SOP to deform the second copy before skinning.
[circleSOP_Class](https://docs.derivative.ca/CircleSOP_Class "CircleSOP Class")

## Parameters - Page
- Primitive Type `type` - ⊞ - For information on the different types, see the [Primitive](https://docs.derivative.ca/Primitive "Primitive") and [Spline](https://docs.derivative.ca/Spline "Spline") articles. Depending on the primitive type chosen, some SOP options may not apply. Using the 'Primitive' primitive type is not recommended when using instancing.
  * Primitive `prim` -
  * Polygon `poly` -
  * NURBS Curve `nurbs` -
  * Bezier Curve `bezier` -

- Orientation `orient` - ⊞ - The plane on which the circle lies.
  * XY Plane `xy` -
  * YZ Plane `yz` -
  * ZX Plane `zx` -

- Modify Bounds `modifybounds` - Available only when an input is connected to the Curcle SOP to set bounds for the sphere. When Modify Bounds = On the transform parameters below will further modify the radius and position of the bounds.
- Radius `rad` - ⊞ - The Radius of the Circle in the X and Y directions.
  * X `radx` -
  * Y `rady` -

- Center `t` - ⊞ - The Center of the Circle in X, Y and Z.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Order `order` - If a spline curve is selected, it is built at this order.
- Divisions `divs` - The number of edges (points +1) used to describe the circle. This option applies to polygons and imperfect splines. The more Divisions a circle has, the smoother it looks. Using three divisions makes a triangle, four divisions a diamond, five divisions a pentagon, and so on. Also, for open arc types, the number of points will equal Divisions + 1, and for closed arc types, Divisions + 2.
- Arc Type `arc` - ⊞ - Determines how the circle should be drawn. Applies to polygons and imperfect splines only.
  * Closed `closed` - An enclosed curve.
  * Open Arc `openarc` - An open curve segment.
  * Closed Arc `closedarc` - An Open Arc with connecting edges to the centre resembling a slice of pie.
  * Sliced Arc `slicedarc` - Same as Closed Arc, but connects every single point to the center of the circle.Same as Closed Arc, but connects every single point to the center of the circle.

Arc options are available for polygonal circles and some spline types. The difference between the choices: Open, Closed, and Slice are illustrated below for the polygonal case:
[![TouchGeometry220.gif](https://docs.derivative.ca/images/9/93/TouchGeometry220.gif)](https://docs.derivative.ca/File:TouchGeometry220.gif)
- Arc Angles `angle` - ⊞ - The beginning and ending angles of the arc. An arc will start at the beginning angle, and proceed towards the ending angle. If beginning=0 and end=360 it will be a full circle. As a reference:
[![TouchGeometry222.gif](https://docs.derivative.ca/images/d/db/TouchGeometry222.gif)](https://docs.derivative.ca/File:TouchGeometry222.gif)
**Note:** The total angle can exceed 360, making multiple wraps of the circle.
  * `beginangle` -
  * `endangle` -

- Imperfect `imperfect` - This option applies only to Bezier and NURBS circles. If selected, the circles are approximated non-rational curves, otherwise they are perfect rational closed curves.
- Texture Coordinates `texture` - ⊞ - Option to include texture cooordinates or not.
  * Off `off` - No texture coordinates are created.
  * Face `face` - Default texture coordinates are created. To modify texture coordinates, see [Texture SOP](https://docs.derivative.ca/Texture_SOP "Texture SOP").

- Compute Normals `normals` - When On, normals are created for the surface.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Circle SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
