---
url: https://docs.derivative.ca/Insert_DAT
category: DATs
title: Insert_DAT
---

# Insert DAT
## Summary

The Insert DAT allows you to insert a row or column into an existing table.
You can add strings that will be put in the new cells, space separated. If you want a cell to include spaces, in the Contents parameter put the cell contents in quotes: `cell1 'cell 2' cell3`. Or a list in the parameter expression: `['cell1', 'cell 2']`
If the input DAT is not a table, it will be converted to a table.
[insertDAT_Class](https://docs.derivative.ca/InsertDAT_Class "InsertDAT Class")

## Parameters - Insert Page
- Insert `insert` - ⊞ - Specify what to insert.
  * Row `row` - Insert a row.
  * Column `col` - Insert a column.

- At `at` - ⊞ - Specify where to insert.
  * Before First `start` - Insert at the beginning.
  * After Last `end` - Append to the end.
  * Index `index` - Insert at the specified index.

- Index `index` - Index to insert the row or column. Use "After Last" from the "At" parameter to append at the end of the table.
- Contents `contents` - Entries for each cell separated by spaces. Put entries that have spaces in quotes, for example `Name Species "Home Planet"` will put `Name` in the first cell, `Species` in the second, and `Home Planet` in the third. Extra entries will be ignored.
- Include Names `includenames` -
- Replace if Duplicate Name `replaceduplicate` -
- Replace `replace` -
- Names `replace0names` -
- Cell Expression `replace0expr` - ⊞ -
  * me.subRow `me.subRow` -
  * me.subCol `me.subCol` -
  * me.subCol * 100 + me.subRow `me.subCol * 100 + me.subRow` -
  * f'({me.subRow}, {me.subCol})' `f'({me.subRow}, {me.subCol})'` -
  * op('tablename')[me.subRow, me.subCol] `op('tablename')[me.subRow, me.subCol]` -
  * op('chopname')[0][me.subRow] `op('chopname')[0][me.subRow]` -
  * op('chopname')[me.fillName][me.subRow] `op('chopname')[me.fillName][me.subRow]` -
  * op('sopname').points[me.subRow].P[0] `op('sopname').points[me.subRow].P[0]` -
  * op('sopname').points[me.subRow].P[me.subCol] `op('sopname').points[me.subRow].P[me.subCol]` -

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * frag `frag` -
  * glsl `glsl` -
  * html `html` -
  * md `md` -
  * py `py` -
  * rtf `rtf` -
  * tsv `tsv` -
  * txt `txt` -
  * vert `vert` -
  * xml `xml` -
  * From Language `languageext` - pick extension from DATs script language.
  * Custom Extension `customext` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Insert DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
