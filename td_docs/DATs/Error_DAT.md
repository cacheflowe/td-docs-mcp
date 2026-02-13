---
url: https://docs.derivative.ca/Error_DAT
category: DATs
title: Error_DAT
---

# Error DAT
## Summary

The Error DAT lists the most recent TouchDesigner errors in its FIFO (first in/first out) table.
You can filter our messages using pattern matching on some of the columns like Severity, Type and path of the node containing the error. One column contains the absolute frame (`absTime.frame`) in which the error occurred.
[errorDAT_Class](https://docs.derivative.ca/ErrorDAT_Class "ErrorDAT Class")

## Parameters - Error Page
- Active `active` - Inhibits and allows message to be added to log.
- Severity `severity` - Filter pattern for the output. Can be a combination or one of: `message`, `warning` or `abort`
- Type `type` - Filter pattern for the output where the source operator family is specified. Can be a combination or one of the operator families.
- Source `source` - Filter pattern for the output where the logging of errors can be limited to specific locations in the project.
- Message `message` - Filter pattern for the output applied to the error message.
- Log Current Errors `logcurrent` - Traverse through all nodes and captures all current errors.

## Parameters - Log Page
- Callbacks DAT `callbacks` - The DAT's script will execute once for each message coming in. See [errorDAT_Class](https://docs.derivative.ca/ErrorDAT_Class "ErrorDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The path that the script will be executed from if the Execute From parameter is set to Specified Operator.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading.

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
Extra Information for the Error DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
