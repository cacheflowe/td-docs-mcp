---
url: https://docs.derivative.ca/Lookup_DAT
category: DATs
title: Lookup_DAT
---

# Lookup DAT
## Summary

The Lookup DAT outputs values from a lookup Table. The first input is an index into the second input.
The Lookup DAT allows you to select rows from its second input by referencing data either via row/column indices or row/column names. The advantage of the Lookup DAT is such that the order the data is selected is independent from the order in the Lookup Table, rather the Index Table dictates the order therefore allowing for reordering of data and selecting rows/columns multiple times.
[lookupDAT_Class](https://docs.derivative.ca/LookupDAT_Class "LookupDAT Class")

## Parameters - Lookup Page
- Index `index` - ⊞ - Select how the index values are interpreted: as values/indices contained in a column or contained in a row.
  * Row Indices `rowindices` - Rows selected in the Lookup DAT are represented as numerical indices in the Index input.
  * Col Indices `colindices` - Columns selected in the Lookup DAT are represented as numerical indices in the Index input.
  * Row Values `rowvalues` - Rows selected in the Lookup DAT are represented as values in the Index input. By default the first column is used to match the index but this can changed by setting the Value Location as well as Name or Index Parameter.
  * Col Values `colvalues` - Columns selected in the Lookup DAT are represented as values in the Index input. By default the first row is used to match the index but this can changed by setting the Value Location as well as Name or Index Parameter.

- Value Location `valueloction` - ⊞ - When 'Row Values' or 'Col Values' is selected in the Index Parameter, this parameter lets you select how the lookup row or column where the index value searches will be specified.
  * Name `name` - The lookup row or column is specified by name.
  * Index `index` - The lookup row or column is specified by index.

- Value Name `valuename` - Specify the name of the lookup row or column.
- Value Index `valueindex` - Specify the index of the lookup row or column.
- Include Header `includeheader` - Include the first row or column.

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
Extra Information for the Lookup DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
