---
url: https://docs.derivative.ca/Substitute_DAT
category: DATs
title: Substitute_DAT
---

# Substitute DAT
## Summary

The Substitute DAT changes the cells of the incoming DAT using pattern matching and substitution strings. It outputs a table with the same number of rows and columns.
See examples below. Also you can use the second input to provide a table of strings to substitute, the first column being the "before" strings and the second column being the "after" strings.
**See also** : the Python `.replace()` [[1]](https://www.w3schools.com/python/ref_string_replace.asp), which is a method you can apply to any string. You can do that in an [Evaluate DAT](https://docs.derivative.ca/Evaluate_DAT "Evaluate DAT") or [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT").
[substituteDAT_Class](https://docs.derivative.ca/SubstituteDAT_Class "SubstituteDAT Class")

## Parameters - Substitute Page
- Before `before` - Search term to replace. The following special characters may be used:
  * * - match any number of characters
  * ? - match a single character
  * [] - match any character defined within the brackets

To match these special characters exactly, put a backslash (`\`) before the special character.
- After `after` - The replacement term. This replaces everything matched in the search term. Spaces are permitted.
- Match `match` - ⊞ - Specify where to match:
  * Anywhere `anywhere` - Matches any part of the string.
  * Exact `exact` - The string must match the search term exactly.
  * At Start `start` - Match the search term to the beginning of the string.
  * At End `end` - Match the search term to the end of the string.

- Case Sensitive `case` - Respect case sensitivity in search term.
- Expand the From String `expand` - Expand variables and back quotes in the From string.
- Expand the To String `expandto` - Expand variables and back quotes in the To string.
- First Match Only `first` - Replaces only the first instance of the matching string.

## Parameters - Scope Page
- Exclude First Row `xfirstrow` - Forces the first row to be ignored even if it is not specified by the Select Rows settings.
- Exclude First Col `xfirstcol` - Forces the first column to be ignored even if it is not specified by the Select Cols settings.
- Select Rows `extractrows` - ⊞ - This parameter allows you to pick different ways of specifying the rows scoped.
  * All `all` - All rows scoped.
  * by Name `byname` - Rows scoped using Start Row Name and End Row Name parameters.
  * by Index `byindex` - Rows scoped using Start Row Index and End Row Index parameters.
  * by Start Name, End Index `bynameindex` - Rows scoped using Start Row Name and End Row Index parameters.
  * by Start Index, End Name `byindexname` - Rows scoped using Start Row Index and End Row Name parameters.
  * by Values `bynames` - Rows scoped by specifying the row values explicitly.
  * by Condition `byexpr` - Rows scoped by an expression to be evaluated for the from column.

- Start Row Name `rownamestart` - Specify the row name to start the scope range from.
- Start Row Index `rowindexstart` - Specify the row index to start the scope range from.
- End Row Name `rownameend` - Specify the row name to end the scope range.
- End Row Index `rowindexend` - Specify the row index to end the scope range.
- Row Select Values `rownames` - Specify actual row names that you want to scope. You can use pattern matching, for example row[1-4] will scope all the rows names row1 thru row4.
- Row Select Condition `rowexpr` - Specify an expression that will be evaluated. If the expression evaluates to true, the row will be selected.
Expand the parameter and you will see that it is in [expression mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode").
[![SelectDAT rowselectexpr.png](https://docs.derivative.ca/images/f/ff/SelectDAT_rowselectexpr.png)](https://docs.derivative.ca/File:SelectDAT_rowselectexpr.png)
By default, the [Python](https://docs.derivative.ca/Python "Python") expression is `re.match('.*',me.inputCell.val) != None`. `'.*'` means match any character multiple times, so this expression matches all values. If you want to match the parent's operator name followed by any numeric number you can use `parent().name+'[0-9]*'`, where `'[0-9]*'` matches any numerical string. `'.*'+parent().name+'.*'` will match any cell that contains the operator's parent name. You can check [Regular Expression Operations](https://docs.python.org/3.7/library/re.html) for additional information on how to use the Python Regular Expression module.
- From Column `fromcol` - When selecting rows by values, this parameter selects which column to use when matching cell values to Selected Row Values to determine which rows are scoped.
- Select Cols `extractcols` - ⊞ - This parameter allows you to pick different ways of specifying the columns scoped.
  * All `all` - All columns scoped.
  * by Name `byname` - Columns scoped using Start Col Name and End Col Name parameters.
  * by Index `byindex` - Columns scoped using Start Col Index and End Col Index parameters.
  * by Start Name, End Index `bynameindex` - Columns scoped using Start Col Name and End Col Index parameters.
  * by Start Index, End Name `byindexname` - Columns scoped using Start Col Index and End Col Name parameters.
  * by Values `bynames` - Columns scoped by specifying the column values explicitly.
  * by Condition `byexpr` - Columns scoped by an expression to be evaluated for the from row.

- Start Col Name `colnamestart` - Specify the column name to start the scope range from.
- Start Col Index `colindexstart` - Specify the column index to start the scope range from.
- End Col Name `colnameend` - Specify the column name to end the scope range.
- End Col Index `colindexend` - Specify the column index to end the scope range.
- Col Select Values `colnames` - Specify actual column names that you want to scope. You can use pattern matching, for example colvalue[1-4] will scope all the columns named colvalue1 thru colvalue4.
- Col Select Condition `colexpr` - Specify an expression that will be evaluated. If the expression evaluates to true, the column will be scoped. See Row Select Condition for more details.
- From Row `fromrow` - When scoping columns by Specified Names, this parameter selects which row to use when matching cell values to Selected Col Values to determine which columns are scoped.

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
  * Input 0:  - Data to operate on.
  * Input 1:  - _(optional)_ A [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") with a `before` and `after` column containing strings to sustitute in the first input. This doesn't have to be the whole cell content but can be any partial string as well.

## Info CHOP Channels
Extra Information for the Substitute DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
