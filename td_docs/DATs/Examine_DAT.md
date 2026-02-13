---
url: https://docs.derivative.ca/Examine_DAT
category: DATs
title: Examine_DAT
---

# Examine DAT
## Summary

The Examine DAT lets you inspect an operator's python storage, locals, globals, expressions, and extensions.
[examineDAT_Class](https://docs.derivative.ca/ExamineDAT_Class "ExamineDAT Class")

## Parameters - Examine Page
- Operator `op` - Path to the operator to examine.
- Source `source` - ⊞ - Specifies what part of the operator to examine.
  * Operator Storage `storage` - Examine the operator's [storage](https://docs.derivative.ca/Storage "Storage").
  * Operator Locals `locals` - Examine the local dictionary associated with the operator's module. (DATs only).
  * Extensions `extensions` - Examine any [extension](https://docs.derivative.ca/Extensions "Extensions") objects defined in the Component.
  * Globals `globals` - Examine the global dictionary associated with the project (accessible via the textport).
  * Expression `expression` - Specify the object to be examined.

- Subkey `subkey` - If the object to be examined is a dictionary you can specify which element to examine here.
- Expression `expression` - When source is set to Expression, enter your expression in this parameter.
- Level `level` - Clamp the maximum depth level.
- Key `key` - Filter Key results.
- Type `type` - Filter Type results.
- Value `value` - Filter Value results.
- Expand Classes `expandclasses` - When true, complex object structures (example OP) are further expanded.
- Max Levels `maxlevels` - Specify the maximum depth in which to expand a python object.
- Format `format` - ⊞ - Determines whether the output is raw text or in table format.
  * Text `text` -
  * Table `table` -

- Output Headers `outputheaders` - Turn this on to display the column names when **Format** is set to Table.
- Output Level `outputlevel` - Turn this on to output the **Level** column of the results.
- Output Key `outputkey` - Turn this on to output the **Key** column of the results.
- Output Type `outputtype` - Turn this on to output the **Type** column of the results.
- Output Value `outputvalue` - Turn this on to output the **Value** column of the results.

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
Extra Information for the Examine DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
