---
url: https://docs.derivative.ca/Extrude_SOP
category: SOPs
title: Extrude_SOP
---

# Extrude SOP
## Summary

The Extrude SOP can be used for:
  * Extruding and bevelling Text and other geometry
  * Cusping the bevelled edges to get sharp edges
  * Making primitives thicker or thinner

The default is a 1 unit extrusion directly backwards from the input geometry's normals.
It uses the normal of the surface to determine the direction of extrusion. In the case of planar or open polygons, the normal is difficult to determine, and may not always provide the result that you expect. Turn on the Primitive Normals display in the [Viewer](https://docs.derivative.ca/Viewer "Viewer") display options to see the normals.
The extrusion is created by extending surfaces from the vertices of the input geometry along the cross-section curve given in the second input (Input 1). The first vertex of the cross-section curve is placed by default at the vertices of the input geometry and aligned so that the curve's positive Y axis extends opposite to the input geometry's normal. The cross-section's positive X axis by default extends outwards from center of the input geometry.
If no cross-section curve is given, a vertical line going from (0,0,0) to (0,1,0) is used. This results in a 1 unit extrusion directly backwards from the input geometry's normals. As another example, using a straight line from (0,0,0) to (.1,.1,0) will result in an extrusion that extends 1 unit backwards from the input and flares .1 unit outwards on all sides. The Thickness and Depth parameters can be used to shift and scale the cross-section without directly changing the curve.
**Note:** The shape of the cross-section is always relative to its first vertex, so shifting the entire cross-section curve will have no effect. Also, only the X and Y axes of the curve are used i.e. Z position values are ignored.
After the new geometry is created, normals are computed by default.
**Warning:** If you take a default output from a [Text SOP](https://docs.derivative.ca/Text_SOP "Text SOP") and Extrude it, it may have bad rendering artifacts (and too many polygons) as it's extruding each of the triangles of the triangulated letters. You need to change the Output parameter of the Text SOP to Closed Polygons. See [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets").
[extrudeSOP_Class](https://docs.derivative.ca/ExtrudeSOP_Class "ExtrudeSOP Class")

## Parameters - Page
- Source Group `sourcegrp` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified for the source. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- X-Section Group `xsectiongrp` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified for the cross-section. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").

## Parameters - Values Page
- Fuse Points `dofuse` - ⊞ - This should almost always be turned on when cross-sections are used. It consolidates points of polygons that would otherwise cross or overlap when the bevel takes place.
  * No fusion `off` -
  * Clamp all points `all` -
  * Clamp minimal set `min` -
  * Clamp individual face `on` -
  * Clamp straight `straight` -

- Front Face `fronttype` - ⊞ - Control how the front face of the extrusion should be built. You may wish to have a "No Output" because some faces are never actually seen when doing animation and, therefore, would only take up additional overhead if left on.
  * No Output `off` - No face is created.
  * Output Face `face` - Faces are created.
  * Convex Face `convex` - Create faces built with Convex Polygons (use this option if faces are to be deformed, i.e. [Twist SOP](https://docs.derivative.ca/Twist_SOP "Twist SOP"), [Lattice SOP](https://docs.derivative.ca/Lattice_SOP "Lattice SOP")).

- Back Face `backtype` - ⊞ - This value controls whether or not the back of the extruded object will have a face or not. The options are the same as the Front Face options above.
  * No Output `off` -
  * Output Face `face` -
  * Convex Face `convex` -

- Side Mesh `sidetype` - ⊞ - Controls how the cross-section(s) will be extruded. If the input cross-section is a Bzier or NURBS curve, the surface will be constructed with a patch of the same geometry type.
  * No Output `off` - No mesh is created.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon). Compare them in the Model Editor.
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Initialize Extrusion `initextrude` - If the cross-section face that you created doesn't match up nicely to the size of the geometry you are extruding, this command will scale and translate it so that it fits nicely.
The reason it might not be nice to begin with is that the curve wasn't drawn exactly on the world-axis in Model-mode and/or was drawn at a grossly different scale than the object it is extruding.
- Thickness Translate `thickxlate` - Shifts the cross-section profile perpendicularly to the normals of the input geometry. This relates to the X axis of the cross-section profile. When used with text, this typically has the effect of making the text lighter (narrower) or heavier (bolder).
- Thickness Scale `thickscale` - Scales the cross-section profile perpendicularly to the normals of the input geometry. This is equivalent to scaling the cross-section in its X axis. This parameter has no effect on the default profile, which is equivalent to a vertical line along the Y axis. Negative scaling values are allowed.
- Depth Translate `depthxlate` - Moves the cross-section in the direction of the normal. Positive values will move backwards to the direction of the normal. Depth movement relates to the Y axis of the input cross-section. Using this parameter will shift the position of the output geometry in direction of the normal.
- Depth Scale `depthscale` - Scales the cross-section in the direction of the source geometry's normals. This is equivalent to scaling the input cross-section in its Y axis and will determine how deep (thick) the resulting extrusion is.
- Vertex `vertex` - Translates the cross-section such that the vertex specified is at the cross-section origin.
- Cusp Polygonal Sides `docusp` - Determines whether or not sides are to be smooth-shaded or faceted using the angle value in Side Cusp Angle field.
Cusping lets you specify at which angle between adjacent polygons, a sharp edge (faceted edge where vertices are un-shared) should be displayed instead.
- Side Cusp Angle `cuspangle` - When checked, this value will control the angle at which faceting of the sides will occur. A value of 20 is default.
- Consolidate Faces to Mesh `sharefaces` - If selected the extrusion will share points between the front face and the first row of the side mesh and between the last face and the last row of the side mesh.
- Remove Shared Sides `removesharedsides` - Prevents the creation of duplicate sides.

## Parameters - Groups Page
- Create Output Groups `newg` - When this option is checked, it causes the Extrude SOP to generate three new groups representing the primitives belonging to the front faces, back faces, and the side bevel/extrusion. The name of the groups are determined by the three option fields below.
- Front Group `frontgrp` - Output group name to create for front face geometry.
- Back Group `backgrp` - Output group name to create for back face geometry.
- Side Group `sidegrp` - Output group name to create for side bevel/extrude geometry.

Production Tips
This SOP is mainly used for generating bevels and extrusions of text where the input cross-sections are fed from a [Font SOP](https://docs.derivative.ca/Font_SOP "Font SOP"). Any curve or group of curves can also be used as input.
Offsets - This SOP can be used for generating two offsetting curves where the distance between the two curves remains constant. To do this, make sure that you set Side Mesh to No Output, the first thickness to zero and adjust the second to increase or decrease the distance of the offset.
Fixing Stray Normals - If your geometry contains normals that are pointed in many directions (say after reading geometry from a [File In SOP](https://docs.derivative.ca/File_In_SOP "File In SOP"), or if you have a lot of open or non-planar polygons), you can fix it so that they are suitable for extrusion.
Do this by appending a [Group SOP](https://docs.derivative.ca/Group_SOP "Group SOP") to the SOP that contains your geometry, enable Normal, and reduce the Spread Angle to something less than 180. Then append a [Primitive SOP](https://docs.derivative.ca/Primitive_SOP "Primitive SOP"), which should work on the group made in the Group SOP. In the Face/Hull page, set the Vertex menu to Reverse.
Now the normals in your geometry will all be oriented in the roughly the same direction, and ready for extrusion. To narrow the tolerance, decrease the Spread Angle further.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Extrude SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
