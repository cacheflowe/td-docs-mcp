---
url: https://docs.derivative.ca/DAT_to_SOP
category: SOPs
title: DAT_to_SOP
---

# DAT to SOP
## Summary

The DAT to SOP can be used to create geometry from DAT tables, or if a SOP input is specified, to modify attributes on existing geometry. See also the [Add SOP](https://docs.derivative.ca/Add_SOP "Add SOP").
Without a SOP input, the output is created entirely from the DAT, one SOP point per row of the DAT, except for an optional top row with column headings. The common columns headings include the point number `index`, point position `P(0) P(1) P(2)`, point weight `Pw`, the color and alpha `Cd(0) Cd(1) Cd(2) Cd(3)`, texture coordinates `uv(0) uv(1) uv(2)`, and point normal `N(0) N(1) N(2)`. If no index column is specified, row number is used as the point number. If there is no heading for the Point DAT, the list of attributes is assumed to be in order `P(0) P(1) P(2) Pw Cd(0) Cd(1) Cd(2) Cd(3) N(0) N(1) N(2) uv(0) uv(1) uv(2)` for the first 14 columns. If an input is used, attributes are read in and replace the ones in the existing geometry. The Merge parameter will be enabled when an input is connected. Depending on the Merge menu setting, either the Points DAT or Primitive DAT parameter used for the merge data. If an input is used, the Points or Primitives DAT must have a column named `_index_`. This column is used to match the point or primitive to the incoming geometry by point or primitive number. Attributes in the columns headings should have column name _`attrib`_if it is a single value attribute, or have multiple columns named` _attrib_(0)`,`_attrib_(1)`,`_attrib_(2)`etc if it is a multiple-value attribute. Data can also be converted into a form that can be rendered as particles.
**Example File :** [File:SOPtoDATtoSOP.tox](https://docs.derivative.ca/File:SOPtoDATtoSOP.tox "File:SOPtoDATtoSOP.tox")
[dattoSOP_Class](https://docs.derivative.ca/DattoSOP_Class "DattoSOP Class")

## Parameters - Page
- Points DAT `pointsdat` - DAT with point data. The optional `_index_`indicates the point number, if none is specified, row number will be used. Attributes can be specified in `_attribute_name_(attribute_index)`. If there are no named column headings for the Point DAT, the index column should be removed and the list of attributes is assumed to be in order `P(0) P(1) P(2) Pw Cd(0) Cd(1) Cd(2) Cd(3) N(0) N(1) N(2) uv(0) uv(1) uv(2)` for the first 14 columns. Sample point data: ```
   index	P(0)	P(1)	P(2)	Pw	N(0)	N(1)	N(2)
   0		-0.5	-0.5	-0.5	1	0	0	-1
   1		-0.5	0.5	-0.5	1	0	0	-1
   2		0.5	0.5	-0.5	1	0	0	-1
   3		0.5	-0.5	-0.5	1	0	0	-1
   ...

```

The common columns attributes include point position `P(0) P(1) P(2)`, point weight `Pw`, the color and alpha `Cd(0) Cd(1) Cd(2) Cd(3)`, texture coordinates `uv(0) uv(1) uv(2)`, and point normal `N(0) N(1) N(2)`. See [Point Attributes](https://docs.derivative.ca/Attribute#Point_Attributes "Attribute") for a list of attributes.
- Vertices DAT `verticesdat` - DAT with vertex data. `index` indicates the primitive number and `vindex` the vertex number in that primitive. Attributes are specified in the same manner as for points. ample vertex data: ```
   index	vindex	uv(0)	uv(1)	uv(2)
   0		0	0	0	0
   0		1	0	1	0
   0		2	1	1	0
   0		3	1	0	0
   1		0	1	0	0
   1		1	1	1	0
   1		2	1	1	1
   1		3	1	0	1
   ...

```

Common attributes include the color and alpha `Cd(0) Cd(1) Cd(2) Cd(3)`, texture coordinates `uv(0) uv(1) uv(2)`, and vertex normal `N(0) N(1) N(2)`. See [Vertex Attributes](https://docs.derivative.ca/Attribute#Vertex_Attributes "Attribute") for a list of attributes.
- Primitives DAT `primsdat` - DAT with primitive data. The optional `index` indicates the primitive number, if none is specified, row number will be used. Column headings are required; `vertices` list the point numbers in order, `close` indicates whether the primitive is a closed or open curve. Attributes are specified in the same manner as for points. Sample primitive data: ```
   index	vertices	close	Cd(0)	Cd(1)	Cd(2)	Cd(3)
   0		0 1 2 3		1	0.2	1	1	1
   1		4 5 6 7		1	0.2	0.2	0.5	1
   2		8 9 10 11	1	0.2	0.2	0.2	1

```

Common attributes include the color and alpha `Cd(0) Cd(1) Cd(2) Cd(3)`. See [Primitive Attributes](https://docs.derivative.ca/Attribute#Primitive_Attributes "Attribute") for a list of attributes.
- Detail DAT `detaildat` - DAT with detail data. Attribute names are specified on the first row and attribute data on the second row. Sample detail data: ```
   pCaptPath		pCaptData(0)	pCaptData(1)	pCaptData(2)	...
   /bone1/cregion 	0		3.33333		0		...

```
- Merge `merge` - ⊞ - Specify whether to merge point data or primitive data. This parameter is only enabled when there is an input connected to the SOP.
  * Points `points` - Merge point data.
  * Vertices `vertices` -
  * Primitives `primitives` - Merge primitive data.
  * Detail `detail` -

- Add Float Attributes `float` - Add a non-standard attribute specified in the point or primitive DAT as a float.
- Add Int Attributes `int` - Add a non-standard attribute specified in the point or primitive DAT as an int. It will not be added if it has already been specified in the Float attributes.
- Add String Attributes `string` - Add a non-standard attribute specified in the point or primitive DAT as a string. It will not be added if it has already been specified in the Float or Int attributes.
- Build `build` - ⊞ - Specifies how to build geometry.
  * Use Primitive DAT `dat` - Build geometry using data from the Primitive DAT.
  * Connect All Points `all` - Connect all points.
  * Connect Every 2 Points `pts2` - Connect points in pairs.
  * Connect Every 3 Points `pts3` - Connect points in triples.
  * Connect Every 4 Points `pts4` - Connect every 4 points together.
  * Connect Every N Points `ptsn` - Connect every N points together.
  * Polygon with N Rows `polyrow` - Create a polygon grid with N rows.
  * Polygon with N Columns `polycol` - Create a polygon grid with N columns.
  * Mesh with N Rows `meshrow` - Create a mesh grid with N rows.
  * Mesh with N Columns `meshcol` - Create a mesh grid with N columns.
  * Particle System using All Points `particleall` - Creates a particle system of points.

- N `n` - Number of points used for building primitives.
- Closed U `closed` - Closed curves in U.
- Closed V `closedv` - Closed curves in V.
- Connectivity `connect` - ⊞ - Connectivity of polygons.
  * Rows `rows` - Creates horizontal lines.
  * Columns `cols` - Creates vertical lines.
  * Rows and Columns `rowcol` - Both Rows and Columns. Looks like Quads in wireframe display, but all polygons are open (if the primitive type is polygon). Compare them in the Model Editor.
  * Triangles `triangles` - Build the grid with Triangles.
  * Quadrilaterals `quads` - Generates sides composed of quadrilaterals (default).
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.

- Particle Type `prtype` - ⊞ - When creating a particle system, specify to render the particles as lines or point sprites.
  * Render as Lines `lines` -
  * Render as Point Sprites `pointprites` -

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the DAT to SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
