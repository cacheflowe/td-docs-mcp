---
url: https://docs.derivative.ca/Merge_DAT
category: DATs
title: Merge_DAT
---

# Merge DAT
## Summary

The Merged DAT is a multi-input DAT which merges the text or tables from the input DATs together.
[mergeDAT_Class](https://docs.derivative.ca/MergeDAT_Class "MergeDAT Class")

## Parameters - Merge Page
- DAT `dat` - Specifies the path to DATs to be merged. Can be used in conjunction with the operator's wired inputs.
- How `how` - ⊞ - Sets how tables are merged together.
  * Append Rows `row` - Merges tables together by adding rows from subsequent tables to the first table. If the By Name option is used, then data from subsequent tables will be added to the column with the same name, and the first row will not be added. If the subsequent tables have more columns than the input table, they will be appended.
  * Append Columns `col` - Merges tables together by adding columns from subsequent tables to the first table. If the By Name option is used, then data from subsequent tables will be added to the row with the same name, and the first column will not be added. If the subsequent tables have more rows than the input table, they will be appended.
  * Collapse Columns `collapsecol` - Merges tables together by concatenating all cells in a row into one single cell. You will have one column and one or more rows at the end.
  * Collapse Rows `collapserow` - Merges tables together by concatenating all cells in a column into one single cell. You will have one row and one or more columns at the end.
  * Collapse Cells `collapsecells` - Merges tables together by concatenating all cells together. You will have one single cell at the end.
  * Replace Cells by Column `repcolcells` - Replaces data in the first table with data in subsequent tables, matching by row names. Data from the last table will always be used.
  * Replace Cells by Row `reprowcells` - Replaces data in the first table with data in subsequent tables, matching by column names. Data from the last table will always be used.

    For example, if your first input table is ```
 Name          Species	  Age
 Birch	        Ferret	  6
 Diefenbaker	Ferret	  4

```
    and you have two more input tables in the order ```
 Name          Species	   Age
 Birch	        Ferret	   5
 Diefenbaker	Wolverine  5

```
```
 Name          Species	  Age
 Birch	        Ferret	   6
 Diefenbaker	Otter	   10

```
    your output table will be ```
 Name          Species	  Age
 Birch	        Ferret	   5

```
- By Name `byname` - Specifies if you are appending columns and rows by name.
- Concatenate with `spacer` - Allows you to separate the cell data with a string when concatenating. The default is a space.
- Append Unmatched `unmatched` - If the subsequent tables have rows or columns that are not found in the first table, these will be added to the output.

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
Extra Information for the Merge DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
