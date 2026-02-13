---
url: https://docs.derivative.ca/DAT_to_CHOP
category: CHOPs
title: DAT_to_CHOP
---

# DAT to CHOP
## Summary

The DAT to CHOP will create a set of CHOP channels with values derived from a [DAT](https://docs.derivative.ca/DAT "DAT").
[dattoCHOP_Class](https://docs.derivative.ca/DattoCHOP_Class "DattoCHOP Class")

## Parameters - DAT to Page
- DAT `dat` - The DAT to be used to retrieve values. This DAT should be in _table_ format. For table format, use either a [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") or a [Convert DAT](https://docs.derivative.ca/Convert_DAT "Convert DAT") set to **To Table**.
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
- Row Select Values `rownames` - Specify actual row names that you want to select. You can use pattern matching, for example row[1-4] will select all the rows names row1 thru row4.
- Row Select Condition `rowexpr` - Specify an expression that will be evaluated. If the expression evaluates to true, the row will be selected.
Expand the parameter and you will see that it is in [expression mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode").
[![SelectDAT rowselectexpr.png](https://docs.derivative.ca/images/f/ff/SelectDAT_rowselectexpr.png)](https://docs.derivative.ca/File:SelectDAT_rowselectexpr.png)
By default, the [Python](https://docs.derivative.ca/Python "Python") expression is re.match('.*',me.inputCell.val) != None. '.*' means match any character multiple times, so this expression matches all values. If you want to match the parent's operator name followed by any numeric number you can use parent().name+'[0-9]*', where '[0-9]*' matches any numerical string. '.*'+parent().name+'.*' will match any cell that contains the operator's parent name. You can check [Regular Expression Operations](https://docs.python.org/3.3/library/re.html) for additional information on how to use the Python Regular Expression module.
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
- Col Select Values `colnames` - Specify actual column names that you want to select. You can use pattern matching, for example colvalue[1-4] will select all the columns named colvalue1 thru colvalue4.
- Col Select Condition `colexpr` - Specify an expression that will be evaluated. If the expression evaluates to true, the column will be selected. See Row Select Condition for more details.
- From Row `fromrow` - When extracting columns by Specified Names, this parameter selects which row to use when matching cell values to Selected Col Values to determine which columns are selected.
- Output `output` - ⊞ - Specify the form of the channels output.
  * Single Channel `single` - A single channel is created with one sample for every value extracted.
  * Channel per Row `chanperrow` - A separate channel is created for every row extracted.
  * Channel per Column `chanpercol` - A separate channel is created for every column extracted.
  * Channel per Value `chanpervalue` - A separate channel is created for every value extracted.

- First Row is `firstrow` - ⊞ - Specifies whether the first row is ignored, names, or values.
  * Ignored `ignored` -
  * Names `names` -
  * Values `values` -

- First Column is `firstcolumn` - ⊞ - Specifies whether the first columnn is ignored, names, or values.
  * Ignored `ignored` -
  * Names `names` -
  * Values `values` -

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).

## Info CHOP Channels
Extra Information for the DAT to CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

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
