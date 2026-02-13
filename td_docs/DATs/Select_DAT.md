---
url: https://docs.derivative.ca/Select_DAT
category: DATs
title: Select_DAT
---

# Select DAT
## Summary

The Select DAT allows you to fetch a DAT from any other location in the project, and to select any subset of rows and columns if it is a table.
[selectDAT_Class](https://docs.derivative.ca/SelectDAT_Class "SelectDAT Class")

## Parameters - Select Page
- DAT `dat` - The [path](https://docs.derivative.ca/Network_Path "Network Path") of the DAT being referenced.
- Include First Row `firstrow` - Forces the first row to be selected even if it is not specified by the Select Rows settings.
- Include First Col `firstcol` - Forces the first column to be selected even if it is not specified by the Select Cols settings.
- Select Rows `extractrows` - ⊞ - This parameter allows you to pick different ways of specifying the rows selected.
  * All `all` - All rows selected.
  * by Name `byname` - Rows selected using Start Row Name and End Row Name parameters.
  * by Index `byindex` - Rows selected using Start Row Index and End Row Index parameters.
  * by Start Name, End Index `bynameindex` - Rows selected using Start Row Name and End Row Index parameters.
  * by Start Index, End Name `byindexname` - Rows selected using Start Row Index and End Row Name parameters.
  * by Values `bynames` - Rows selected by specifying the row values explicitly.
  * by Condition `byexpr` - Rows selected by an expression to be evaluated for the from column.

- Start Row Name `rownamestart` - Specify the row name to start the selection range from.
- Start Row Index `rowindexstart` - Specify the row index to start the selection range from.
- End Row Name `rownameend` - Specify the row name to end the selection range.
- End Row Index `rowindexend` - Specify the row index to end the selection range.
- Row Select Values `rownames` - Specify actual row names that you want to select. You can use TouchDesigner's pattern matching (see wiki page [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching")), for example `row[1-4]` will select all the rows names `row1` thru `row4`. Some characters like `'` need a `\` in front of it.
- Row Select Condition `rowexpr` - Specify an expression that will be evaluated. If the expression evaluates to true, the row will be selected.
Expand the parameter and you will see that it is in [expression mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode").
[![SelectDAT rowselectexpr.png](https://docs.derivative.ca/images/f/ff/SelectDAT_rowselectexpr.png)](https://docs.derivative.ca/File:SelectDAT_rowselectexpr.png)
By default, the [Python](https://docs.derivative.ca/Python "Python") expression is `re.match('.*',me.inputCell.val) != None`. `'.*'` means match any character multiple times, so this expression matches all values. If you want to match the parent's operator name followed by any numeric number you can use `parent().name+'[0-9]*'`, where `'[0-9]*'` matches any numerical string. `'.*'+parent().name+'.*'` will match any cell that contains the operator's parent name. You can check [Regular Expression Operations](https://docs.python.org/3.3/library/re.html) for additional information on how to use the Python Regular Expression module.
- From Column `fromcol` - When selecting rows by values, this parameter selects which column to use when matching cell values to Selected Row Values to determine which rows are selected.
- Select Cols `extractcols` - ⊞ - This parameter allows you to pick different ways of specifying the columns selected.
  * All `all` - All columns selected.
  * by Name `byname` - Columns selected using Start Col Name and End Col Name parameters.
  * by Index `byindex` - Columns selected using Start Col Index and End Col Index parameters.
  * by Start Name, End Index `bynameindex` - Columns selected using Start Col Name and End Col Index parameters.
  * by Start Index, End Name `byindexname` - Columns selected using Start Col Index and End Col Name parameters.
  * by Values `bynames` - Columns selected by specifying the column values explicitly.
  * by Condition `byexpr` - Rows selected by an expression to be evaluated for the from row.

- Start Col Name `colnamestart` - Specify the column name to start the selection range from.
- Start Col Index `colindexstart` - Specify the column index to start the selection range from.
- End Col Name `colnameend` - Specify the column name to end the selection range.
- End Col Index `colindexend` - Specify the column index to end the selection range.
- Col Select Values `colnames` - Specify actual column names that you want to select. You can use TouchDesigner's pattern matching (see wiki page [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching")), for example `colvalue[1-4]` will select all the columns named `colvalue1` thru `colvalue4`. Matching some characters like `'` need a `\` in front of it.
- Col Select Condition `colexpr` - Specify an expression that will be evaluated. If the expression evaluates to true, the column will be selected. See Row Select Condition for more details.
- From Row `fromrow` - When extracting columns by Specified Names, this parameter selects which row to use when matching cell values to Selected Col Values to determine which columns are selected.
- Output `output` - ⊞ - Determines what format will be used for output from the DAT.
  * Input Data `data` - Passes through data from first input without manipulation.
  * Strings `string` - Evaluates input data as strings, including expanding any variable values to full strings.
  * Expressions `expr` - Evaluates input data as expressions.

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
Extra Information for the Select DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
