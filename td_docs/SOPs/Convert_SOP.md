---
url: https://docs.derivative.ca/Convert_SOP
category: SOPs
title: Convert_SOP
---

# Convert SOP
## Summary

The Convert SOP converts geometry from one geometry type to another type. Types include polygon, mesh, Bezier patche, particle and sphere primitive.
[convertSOP_Class](https://docs.derivative.ca/ConvertSOP_Class "ConvertSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- From Type `fromtype` - ⊞ - Determines which geometry by type will be converted. The default is All Types:
  * All Types `all` - All geometry will be converted.
  * Sphere `sphere` -
  * Tube `tube` -
  * Particles `part` -
  * Meta-ball `metaball` -
  * Polygon `poly` -
  * Mesh `mesh` -
  * Bezier Curve `bezcurve` -
  * Bezier Surface `bezsurf` -
  * NURBS Curve `nurbcurve` -
  * NURBS Surface `nurbsurf` -
  * Circle `circle` -
  * Triangle Strip `tristrip` -
  * Triangle Fan `trifan` -

- Convert to `totype` - ⊞ - Determines what the above From Type geometry will be converted to. Conversion to Polygons is the default:

**Notes** : Not all geometry can be converted to specific types. For example, a triangulated polygon surface to a single NURBS surface, or a Mesh sphere into a primitive sphere. Also, certain conversions will preserve shapes. For example, converting a Bzier curve to a NURBS curve or a polygonal mesh to a NURBS Surface.
**Circle Notes** : Converting to primitive circles is available for action users who are used to working with polygon circles so that you can convert them to primitive circles for the TouchDesigner Skeleton, Arm, and Limb SOPs.
**Trimmed Surface Notes** : If the primitive to be converted is a curve (NURBS or Bezier) and is flat, a trimmed surface will be generated such that the visible piece coincides with the curve. If the curve is not flat, it will be converted to a non-trimmed surface. The advantage of the trimmed solution is that it yields a very clean surface and handles concave curves perfectly.
  * Polygon `poly` -
  * Mesh `mesh` -
  * Bezier Curve `bezcurve` -
  * Bezier Surface `bezsurf` -
  * NURBS Curve `nurbcurve` -
  * NURBS Surface `nurbsurf` -
  * Circle `circle` -
  * Trimmed Bezier Surface `trimbezsurf` -
  * Trimmed NURBS Surface `trimnurbsurf` -
  * Particles `part` -

- Connectivity `surftype` - ⊞ - This option is used to select how the points of the created surface are connected.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quadrilaterals in wire frame display, but all polygons are open (if the primitive type is polygon).
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

## Parameters - Level of Detail Page
This affects the use of the U/V/Trim Curve fields:
  * For Level of Detail: U, V, Trim Curve Level of Detail

In a spline's case, the span is the curve arc between two breakpoints. The number of divisions per span specifies how many points to be created between the two breakpoints. If the number of divisions = 0, a single segment will connect the two breakpoints; if number of divisions = 1, two edges will be created; etc. The advantage of Divisions over the Level of Detail is that it tells you exactly how many points you'll end up with - extremely useful for polygonal modeling.
- U `lodu` - When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh.
When set to Divisions per Span, specificies the number of divisions per span.
**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the `primdist()` expression. Then the detail will increase/decrease as the camera gets closer/further away.
- V `lodv` - When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh.
When set to Divisions per Span, specificies the number of divisions per span.
**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the `primdist()` expression. Then the detail will increase/decrease as the camera gets closer/further away.
- Trim-Curve `lodtrim` - The trimmed part of a surface will be converted using this Trim lod (level of detail) instead of using an implicit "1" constant.

## Parameters - Divisions per Span Page
This affects the use of the U/V/Trim Curve fields:
  * For Divisions per Span: U, V, Number of Trim Curve Divisions.

In a spline's case, the span is the curve arc between two breakpoints. The number of divisions per span specifies how many points to be created between the two breakpoints. If the number of divisions = 0, a single segment will connect the two breakpoints; if number of divisions = 1, two edges will be created; etc. The advantage of Divisions over the Level of Detail is that it tells you exactly how many points you'll end up with - extremely useful for polygonal modeling.
- U `divu` - When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh.
When set to Divisions per Span, specificies the number of divisions per span.
**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the `primdist()` expression. Then the detail will increase/decrease as the camera gets closer/further away.
- V `divv` - When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh.
When set to Divisions per Span, specificies the number of divisions per span.
**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the `primdist()` expression. Then the detail will increase/decrease as the camera gets closer/further away.
- Trim-Curve `divtrim` - The trimmed part of a surface will be converted using this Trim lod (level of detail) instead of using an implicit "1" constant.

- U Order `orderu` - When converting to a spline type, this specifies the degree + 1 of the U or V basis function.
Paste Coordinates
  * From Feature Surfaces - The resulting mesh will have the shape of the paste hierarchy (i.e. the top-most features will determine the shape).
  * From Base Surface - The resulting mesh will take the shape of the bottom-most surface.

Paste Attributes
  * From Feature Surfaces - Each mesh point has the attributes of the top-most feature at that location.
  * From Base Surface - The resulting mesh will inherit the primitive attributes of the root surface (e.g. the material), and the point attributes will be those of the root surface as well.

By using base coordinates and feature attributes you are, in fact, pasting attributes onto the surface.
- V Order `orderv` - When converting to a spline type, this specifies the degree + 1 of the U or V basis function.
Paste Coordinates
  * From Feature Surfaces - The resulting mesh will have the shape of the paste hierarchy (i.e. the top-most features will determine the shape).
  * From Base Surface - The resulting mesh will take the shape of the bottom-most surface.

Paste Attributes
  * From Feature Surfaces - Each mesh point has the attributes of the top-most feature at that location.
  * From Base Surface - The resulting mesh will inherit the primitive attributes of the root surface (e.g. the material), and the point attributes will be those of the root surface as well.

By using base coordinates and feature attributes you are, in fact, pasting attributes onto the surface.
- Preserve Original `new` - When checked, the original geometry will be retained along with the converted geometry.
- Interpolate Through Hulls `interphull` - This option applies to the conversion between polygonal faces and grids to NURBS and Bzier surfaces and curves. When selected, the resulting curves retain the same topology as the original polygon. When not selected, the polygon points are used as a hull to define the new curve or surface.
- Particle Type `prtype` - ⊞ - Selects how the particles are rendered.
  * Render as Lines `lines` - Each particle will be rendered as a 2-point line, with the length determined based on the particles velocity. If the particle has no velocity it will just be a single pixel in size.
  * Render as Point Sprites `pointprites` - For use with the [Point Sprite MAT](https://docs.derivative.ca/Point_Sprite_MAT "Point Sprite MAT"). Each particle is a square of pixels that always face the camera. The size of the square is determined by parameters in the Point Sprite and the `pscale` vertex/point attribute. The point sprites will have texture coordinates generated for them automatically also ((0,0) in the bottom left and (1,1) in the top right).

## Notes
Face to Surface Conversion - When converting from a set of polygons to a mesh, a single mesh will result only if [Facet SOP](https://docs.derivative.ca/Facet_SOP "Facet SOP").
Otherwise, each polygon is converted individually into a mesh. In fact, any individual face can be converted to any surface. This is accomplished by cutting the face into three or four adjacent sections, and then creating a patch from them.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Convert SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
