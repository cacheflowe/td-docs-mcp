---
url: https://docs.derivative.ca/Skin_SOP
category: SOPs
title: Skin_SOP
---

# Skin SOP
## Summary

The Skin SOP takes any number of faces and builds a skin surface over them. If given two or more surfaces, however, the SOP builds four skins, one for each set of boundary curves.
All face and surface types are valid as long as the input(s) contain only faces or only surfaces. Different face types can be skinned together into one surface. For example, it is possible to skin a cubic open NURBS curve with a polygon and a quintic closed Bzier curve even if the three faces have a different number of control vertices. Similarly, this SOP can skin the boundary curves of surfaces of different types, number of rows, columns, etc.
When face types are input, the number of input SOPs and the number of faces in each input establish the skinning method. If only one input exists, a "linear-skinning" operation is performed by running a skin across the cross-sections. The result is the classic ruled or skinned surface. If a second input exists, a "bi-linear skinning" is performed which computes a cross-skin between the faces in the first input (U cross-sections) and the faces in the second input (V cross-sections). The result is a surface whose name derives from the number of cross-sections in each direction: triangular, square, or multiple boundary surface, as well as a special case of swept surfaces and N-rails. When possible, cross-sections are interpolated as isoparms.
If you need more control over tangency in the skin, try using the [Bridge SOP](https://docs.derivative.ca/Bridge_SOP "Bridge SOP").
**Tip:** If you have problems with the results being skinned in the wrong order, try inserting a Sort SOP ahead of the Skin SOP, and Sort by Normals.
[skinSOP_Class](https://docs.derivative.ca/SkinSOP_Class "SkinSOP Class")

Types of Surfaces
Single Boundary Surface - One face, open or closed, is converted into a surface whose boundaries match the shape of the face exactly. Basically, this operation builds an interior area for the face. The surface type will be similar to the type of the face. For example, a NURBS curve yields a NURBS surface. If the curve is highly concave, the result may look less satisfactory than expected.
[![TouchGeometry81.gif](https://docs.derivative.ca/images/b/bd/TouchGeometry81.gif)](https://docs.derivative.ca/File:TouchGeometry81.gif)
Patch - Two boundary faces define a ruled surface. The arrows on the two faces indicate the required parametric direction, which must be the same for both faces to avoid a bad twist in the surface. Use the Primitive SOP or the modeler to correct the problem. The surface type will be similar to the most complex type between the two cross-sections. For example, if a polygon and a NURBS curve are skinned together, the surface type will be NURBS. The surface always contains the two faces as two of its boundaries.
[![TouchGeometry178.gif](https://docs.derivative.ca/images/3/3f/TouchGeometry178.gif)](https://docs.derivative.ca/File:TouchGeometry178.gif)
Linear Ruled/Skinned Surface - Two or more faces are skinned linearly into a single surface. The arrows on the faces indicate the required parametric direction of each face, which must be the same for all faces to avoid bad twists or flips in the surface. Use the Primitive SOP or the modeler to correct the problem. The surface type will be similar to the most complex type among all cross-sections. For example, if a polygon, a Bzier and a NURBS curve are skinned together, the surface type will be NURBS. The surface goes through each cross-section unless "Preserve Shape" if OFF (see parameters below). If the cross-sections have repeated points, or share points between them, the result might not look good when shape preservation is enabled.
[![TouchGeometry182.gif](https://docs.derivative.ca/images/1/18/TouchGeometry182.gif)](https://docs.derivative.ca/File:TouchGeometry182.gif)
A Special Swept Surface - This case does a bilinear skin and requires two inputs. The U face (1st input) is swept along the V face (second input). The two faces do not need to touch at their endpoints. If their endpoints coincide, though, the two of the surface's boundaries will match the two faces exactly. The surface type will be similar to the most complex type of the two faces. For example, if a polygon and a Bzier curve are skinned together, the surface type will be Bzier.
[![TouchGeometry186.gif](https://docs.derivative.ca/images/1/19/TouchGeometry186.gif)](https://docs.derivative.ca/File:TouchGeometry186.gif)
Triangular Surface - This case requires two inputs for the bilinear skin. One input has two faces; the other input, just one. The endpoints of the faces need not coincide, but if they do, the surface boundaries will match the face shapes exactly. Basically, the three faces define an interior area to be filled by a surface. The surface type will be similar to the most complex type among the three boundary faces. For example, if the faces are Bzier and NURBS curves, the surface will be a NURBS primitive.
[![TouchGeometry190.gif](https://docs.derivative.ca/images/7/7e/TouchGeometry190.gif)](https://docs.derivative.ca/File:TouchGeometry190.gif)
Square Surface - Four faces define the outer boundaries of a surface. This case requires two inputs for the bilinear skin: the two U boundaries (1st input) are cross-skinned with the V boundaries (the 2nd input). The endpoints of the faces need not coincide, but if they do, the surface boundaries will match the face shapes exactly. Basically, the four faces define an interior area to be filled by a surface. The surface type will be similar to the most complex type among the four boundary faces. For example, if the faces are polygons and NURBS curves, the surface will be a NURBS primitive.
[![TouchGeometry194.gif](https://docs.derivative.ca/images/7/70/TouchGeometry194.gif)](https://docs.derivative.ca/File:TouchGeometry194.gif)
A Special Case of M-rails - One input contains the rails, and the other input the cross-section. The cross-section is swept along the rails to form a surface. The arrows on the faces indicate the required parametric direction of each face, which must be the same for all faces to avoid bad twists or flips in the surface. Use the Primitive SOP or the modeler to correct the problem. The surface type will be similar to the most complex type among both rails and cross-section. For example, if the faces are polygons and NURBS curves, the surface will be a NURBS primitive.
[![TouchGeometry198.gif](https://docs.derivative.ca/images/f/f7/TouchGeometry198.gif)](https://docs.derivative.ca/File:TouchGeometry198.gif)
Multiple-Boundary Surface - Not to be confused with N-ary patches. This case generalizes the square surface concept by allowing more interior cross-sections both in U and V. If no interior cross-sections exist, this case reduces to a square surface. The surface interpolates all the boundaries and the interior cross-sections. The result improves when the faces intersect. The arrows on the faces indicate the required parametric direction of each face, which must be the same for all faces to avoid bad twists or flips in the surface. Use the Primitive SOP or the modeler to correct the problem. The surface type will be similar to the most complex type among all faces. For example, if the faces are polygons and NURBS curves, the surface will be a NURBS primitive.
[![TouchGeometry205.gif](https://docs.derivative.ca/images/e/ef/TouchGeometry205.gif)](https://docs.derivative.ca/File:TouchGeometry205.gif)

## Parameters - Page
- U Cross Sections `uprims` - Empty by default, this field provides a way to specify a subset of the first input's faces and surfaces. Do so by selecting one or more primitive groups from this field's pop-up menu.
- V Cross Sections `vprims` - Empty by default, this field provides a way to specify a subset of V faces. If a second input exists, the primitive groups available for selection are taken from the second input. If only the first input is present, the groups listed in the pop-up menu belong to the first input. This means that two inputs are not always needed for a bilinear skin as long as the first input has both U and V groups in it.
- Connectivity `surftype` - ⊞ - (Results only viewable for polygons and meshes).
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon). Compare them in the Model Editor.
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Preserve Shape `keepshape` - This parameter determines the precision of a linear skin (case c in the diagram). If enabled, it ensures that the generated surface goes through each cross-section. Here, a cross-section can be a face or a surface boundary, depending on the types being skinned. If disabled, Preserve Shape produces a surface whose CVs coincide with the CVs of the cross-sections (after they have being converted to a common type and an identical number of CVs). The skinning algorithm is faster with shape preservation OFF, but it lacks precision.
Skinning with shape preservation ON may produce unintuitive shapes when the cross-sections have many coincident CVs or are very close to each other. In this case try to jitter the CVs, vary the V Order (see below), or simply disable shape preservation.
Preserve shape is deactivated when doing bi-linear skinning.
- V Wrap `closev` - ⊞ - This menu (menu: Off, On, If primitive does) setting determines whether the surface should be wrapped in the V parametric direction. The options are to open (Off), close (On), or inherit the closure type from the cross-sections. V Wrap is ignored when doing bilinear skinning.
  * Off `nonewv` -
  * On `wv` -
  * If Primitive does `ifprimwv` -

- Use V Order `force` - Enables or disables the use of the V Order parameter. If the flag is OFF, the skinned surface is built as a cubic (order 4) in V, unless fewer than four cross-sections for an open V or 3 cross-section for a closed V are given. For example, if the input consists of two faces and the V Wrap flag is OFF, the surface will be linear in V (order 2). The status of the V Order flag is irrelevant when the faces or surfaces are all polygons or meshes respectively, and when doing a bilinear skin.
Here, cross-section refers either to a face or a surface boundary, depending on the types being skinned.
- V Order `orderv` - Specifies the order of the skinned surface when the V Order flag is enabled. A NURB surface of order "n" can be constructed with at least n or n-1 cross-sections, depending on whether the surface is open or closed in V respectively. A Bzier surface of the same order can be constructed with at least M*(n-1) + 1 cross-sections if open, or M*(n-1) cross-sections if closed. M is a non-negative, integer multiplier. The V order is ignored when the faces or surfaces are all polygons or meshes respectively, and when building a bilinear skin.
- Skin `skinops` - ⊞ - Can optionally skin subgroups of n primitives or every nth primitive in a cyclical manner.
**For example** ; assume there are six primitives numbered for 0 - 5, and N = 2. Then,
  * Groups will generate 0-1 2-3 4-5
  * Skipping will generate 0-2-6 and 1-3-5.
  * All Primitives `all` -
  * Groups of N Primitives `group` -
  * Skip Every Nth Primitive `skip` -

- N `inc` - Determines the number of primitives to be either grouped or skipped. N2.
- Keep Primitives `prim` - Determines whether the input primitives will be preserved (On) or deleted from the output (Off).
- Output Polygons `polys` - If set, this flag instructs the program to convert the skinned surface(s) to polygons if the surface type is Mesh.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Skin SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
