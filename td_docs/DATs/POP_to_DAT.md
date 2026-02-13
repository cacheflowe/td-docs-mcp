---
url: https://docs.derivative.ca/POP_to_DAT
category: DATs
title: POP_to_DAT
---

# POP to DAT
## Summary

The POP to DAT converts, using the Extract menu, a POP's points or primitives to a table of points (one row per point), or a table of primitives (one row per primitive), or a table of vertices (one row per vertex).
In all cases it creates a column for each attribute component, and the Attributes parameter lets you select specific attributes to include.
The Primitives table has an optional column showing the primitive type - point, line, linestrip, triangle, quad.
The Transpose toggle parameter lets you transpose the table (swap rows and columns) which puts all the attribute names in the first column, for greater readability in some cases.
Without affecting the source, you can thin out the displayed data to restrict, for example, points in a certain point index range, or display 1 in N points, or randomly thin out the data. this makes large datasets much easier to inspect.
You can also choose to display only points or primitives that are in specific [Groups](https://docs.derivative.ca/Group "Group").
Because POP data is on the GPU and DAT tables are on the CPU, there may be a pause caused by the GPU to CPU transfer. The default for Download Type is Next Frame (Fast) which causes minimal delay but the DAT is displayed one [Time Slice](https://docs.derivative.ca/Time_Slicing "Time Slicing") later. Otherwise the Download Type is Immediate, which may cause a several-millisecond delay in the current frame.
See also [DAT to POP](https://docs.derivative.ca/DAT_to_POP "DAT to POP"), [POP to CHOP](https://docs.derivative.ca/POP_to_CHOP "POP to CHOP"), [POP to TOP](https://docs.derivative.ca/POP_to_TOP "POP to TOP").
[poptoDAT_Class](https://docs.derivative.ca/PoptoDAT_Class "PoptoDAT Class")

## Parameters - POP to Page
- Active `active` - When enabled, the DAT will grab and convert the referenced POP's up-to-date geometry information. When disabled, will hold the last converted values.
- POP `pop` - The POP from which to convert the data.
- Download Type `downloadtype` - ⊞ - Gives the option for a delayed data download from the GPU, which is much faster and does not stall the render.
  * Immediate (Slow) `immediate` -
  * Next frame (Fast) `nextframe` -

- Extract `extract` - ⊞ - Specify whether to convert point, primitive, vertices, or detail data.
  * Points `points` - Convert point data.
  * Vertices `vertices` - Convert vertices data.
  * Primitives `primitives` - Convert primitive data.
  * Detail `detail` - Convert detail data.

- Attributes `attrib` - Attributes to convert.
- Primitive Type `primitivetype` - When enabled, adds a column showing the primitive type: point, line, linestrip, triangle, or quad.
- Transpose `transpose` - When enabled converts columns into rows. The number of rows becomes the number of columns.
- Thin Out Range `thinoutrange` - Enable index-based filtering.
- Thin Range Start `thinrangestart` - Determines the starting index for range-based filtering.
- Thin Range Length `thinrangelength` - Determines the number of elements being filtered by index range.
- Thin Step `thinstep` - Filters every Nth element.
- Thin Random `thinrandom` - Determines the proportion of elements randomly filtered.
- Thin Random Seed `thinrandomseed` - Sets the random seed for elements being randomly filtered.
- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Invert Group `invertgroup` - If there are input groups and a group is specified in the Group parameter, this will cause the POP to act only on elements not in the specified group.
- Group Columns `grpcol` - ⊞ - When set to something else but None, will add one or a column per group fetching the group name of the element.
  * None `none` -
  * Group Names in one Column `onecolumn` -
  * Column per Group `colpergrp` -

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
Extra Information for the POP to DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
