---
url: https://docs.derivative.ca/SOP_to_DAT
category: DATs
title: SOP_to_DAT
---

# SOP to DAT
## Summary

The SOP to DAT allows you to extract point, vertex and primitive (e.g. polygon) data and attributes from a SOP.
Data is output in columns, with the first column being index. The index refers to the Point or Primitive number. [Attributes](https://docs.derivative.ca/Attribute "Attribute") are output with column name `_attrib_`if it is a single value attribute, or with multiple columns named` _attrib_(0)`,`_attrib_(1)`,`_attrib_(2)`etc. if it is a multiple value attribute.
See also: [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), [Point](https://docs.derivative.ca/Point "Point"), [Point List](https://docs.derivative.ca/Point_List "Point List"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), [Primitive](https://docs.derivative.ca/Primitive "Primitive"), [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [SOP](https://docs.derivative.ca/SOP "SOP"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").

**Example File :** [File:SOPtoDATtoSOP.tox](https://docs.derivative.ca/File:SOPtoDATtoSOP.tox "File:SOPtoDATtoSOP.tox")
[soptoDAT_Class](https://docs.derivative.ca/SoptoDAT_Class "SoptoDAT Class")

## Parameters - SOP To Page
- SOP `sop` - Specify the SOP to pull data from.
- Extract `extract` - ⊞ - Specify whether to pull point data or primitive data.
  * Points `points` - Get point data.
  * Vertices `vertices` - Get vertex data.
  * Primitives `primitives` - Get primitive data.
  * Detail `detail` - Get data for the entire geometry set.

- Group `group` - Point or primitive group to extract. If none specify all data will be extracted.
- Attributes `attrib` - Attributes to extract.
Point specific attributes can include P and Pw for position and weight.
Primitive specific attributes include vertices and close. Vertices list the point numbers in a primitive and close reports whether the primitive is a closed polygon. The index column is the point or primitive number and will always be output.
- Copy Vertex UV to Points `uvforpts` - Copies the vertex UVs to point UVs.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * From Language `language` - pick extension from DATs script language.
  * Custom Extension `custom` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Info CHOP Channels
Extra Information for the SOP to DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common DAT Info Channels
  * num_rows - Number of rows in this DAT.

  * num_cols - Number of columns in this DAT.

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
