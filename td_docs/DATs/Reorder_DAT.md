---
url: https://docs.derivative.ca/Reorder_DAT
category: DATs
title: Reorder_DAT
---

# Reorder DAT
## Summary

The Reorder DAT allows you to reorder the rows and columns of the input table. You can also use In Specified Order option to get duplicate copies of rows and columns.
[reorderDAT_Class](https://docs.derivative.ca/ReorderDAT_Class "ReorderDAT Class")

## Parameters - Reorder Page
- Reorder `reorder` - ⊞ - This parameter allows you to reorder either rows or columns.
  * Rows `row` -
  * Columns `col` -

- Method `method` - ⊞ - Specify how to reorder the table.
  * Reverse `reverse` - Reverse the order rows or columns.
  * Replace by Names `replacenames` - Copy a row or column in the input table specified in From to the row or column specified in To. Rows or Columns are specified by names.
  * Replace by Indices `replaceindices` - Copy a row or column in the input table specified in From to the row or column specified in To. Rows or Columns are specified by numbers.
  * Swap by Names `swapnames` - Swap a row or column specified in From with the row or column specified in To. Rows or Columns are specified by names. Swaps are cumulative.
  * Swap by Indices `swapindices` - Swap a row or column specified in From with the row or column specified in To. Rows or Columns are specified by numbers. Swaps are cumulative.
  * In Specified Order by Name `specifyname` - Copy the rows or columns in the specified order by name. Any row or column not listed will be appended in input order. You can specify a row or column more than once to get multiple copies of it.
  * In Specified Order by Index `specifyindex` - Copy the rows or columns in the specified order by index. Any row or column not listed will be appended in input order. You can specify a row or column more than once to get multiple copies of it.

- Before `before` - The rows or columns to copy or swap from.
- After `after` - The rows or columns to copy or swap to.
- Order `order` - The order of input rows and columns to copy.
- Delete Unspecified `delete` - Only available when Method is 'In Specified Order by Name' or 'In Specified Order by Index'. It will delete any row/column not listed in the Order parameter.

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
Extra Information for the Reorder DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
