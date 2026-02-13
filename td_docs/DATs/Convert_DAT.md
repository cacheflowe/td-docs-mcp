---
url: https://docs.derivative.ca/Convert_DAT
category: DATs
title: Convert_DAT
---

# Convert DAT
## Summary

The Convert DAT changes the text format from simple text to table form and vice-versa.
[convertDAT_Class](https://docs.derivative.ca/ConvertDAT_Class "ConvertDAT Class")

## Parameters - Convert Page
- How `how` - ⊞ - Convert text format.
  * To Text `text` - Converts table format into regular text.
  * To Table `table` - Converts regular text into table format.

- Remove Blank Lines `removeblank` - When enabled, do not convert blank lines into empty rows.
- Split Cells at `delimiters` - A list of individual characters to use to split the string into cells. The delimiters are used independently. That is, if `$%` is used in this parameter, the cells will be split at `$` OR `%`, not only at `$%`. A [Substitute DAT](https://docs.derivative.ca/Substitute_DAT "Substitute DAT") can be used to collapse a more complex delimiter into a single character to be use for the conversion.
- Concatenate with `spacers` - Insert this string between each cell when converting from a table to text.

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
Extra Information for the Convert DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
