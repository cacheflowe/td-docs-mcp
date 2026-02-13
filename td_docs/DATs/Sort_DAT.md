---
url: https://docs.derivative.ca/Sort_DAT
category: DATs
title: Sort_DAT
---

# Sort DAT
## Summary

The Sort DAT will sort table DAT data by row or column.
[sortDAT_Class](https://docs.derivative.ca/SortDAT_Class "SortDAT Class")

## Parameters - Sort Page
- Sort `sortmethod` - ⊞ - Determines how the table will be sorted.
  * Rows (Specify Column Name) `colname` - Sort rows using the column specified under the Name parameter.
  * Rows (Specify Column Index) `colindex` - Sort rows using the column specified under the Index parameter.
  * Rows (Preserve Input Order) `colpreserve` - Uses the current ordering of the input. This sorting allows parameters such as Preserve First, Unique Output, and Reverse Output to be applied to the original input.
  * Columns (Specify Row Name) `rowname` - Sort columns using the row specified under the Name parameter.
  * Columns (Specify Row Index) `rowindex` - Sort columns using the row specified under the Index parameter.
  * Columns (Preserve Input Order) `rowpreserve` - Uses the current ordering of the input. This sorting allows parameters such as Preserve First, Unique Output, and Reverse Output to be applied to the original input.

- Name `name` - When using Sort _Specify Row/Column Name_ , specify the name in this parameter. If the sort name does not find a match, the output will be unsorted.
- Index `index` - When using Sort _Specify Row/Column Index_ , specify the index in this parameter. If the sort index is -1 or out of bounds, the output will be unsorted.
- Order `order` - ⊞ - Determines the type of sorting.
  * Alphabetical `alpha` - Use alphabetical sorting. Numbers are treated as characters, sorted by their ASCII values.
  * Alphabetical with Numbers `alphanum` - Use alphanumerical sorting.
  * Numbers `nums` - Use numerical sorting. Characters are all treated as 0, incoming order is preserved.
  * Random `random` - Randomly sorts the table, uses random Seed parameter below.

- Seed `seed` - The random seed when Sort Order is set to Random.
- Ignore Case `ignorecase` - Ignores case sensitivity when Sort Order is set to Alphabetical or Alphabetical with Numbers.
- Preserve First `preservefirst` - Does not resort the first row or column (depending if Sort is set to Rows or Columns).
- Unique Output `unique` - ⊞ - Remove duplicate rows/column entries in the sorted row/column.
  * Off `off` -
  * Single Row/Col `single` -
  * Entire Rows/Cols `entire` -

- Reverse Output `reverse` - Reverses the sort order.

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
Extra Information for the Sort DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
