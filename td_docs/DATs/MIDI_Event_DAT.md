---
url: https://docs.derivative.ca/MIDI_Event_DAT
category: DATs
title: MIDI_Event_DAT
---

# MIDI Event DAT
## Summary

The MIDI Event DAT logs all [MIDI](https://docs.derivative.ca/MIDI "MIDI") messages coming into or out of TouchDesigner from all MIDI In/Out operators. Note: no messages will be logged if there are no active MIDI In or Out operators set to receive them. It outputs columns in a table format: message, type, channel, index, value.
The table is FIFO "first-in first-out" and limited to parameter-set number of lines. An optional script may be run for each packet received.
See also the [MIDI In DAT](https://docs.derivative.ca/MIDI_In_DAT "MIDI In DAT"), [MIDI In Map CHOP](https://docs.derivative.ca/MIDI_In_Map_CHOP "MIDI In Map CHOP"), [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP"), [MIDI Out CHOP](https://docs.derivative.ca/MIDI_Out_CHOP "MIDI Out CHOP"), Tscript `midi()` Command.
[midieventDAT_Class](https://docs.derivative.ca/MidieventDAT_Class "MidieventDAT Class")

## Parameters - Connect Page
- Active `active` - Logs MIDI events when turned on.

## Parameters - Filter Page
- Skip Sense `skipsense` - Does not log sense messages when this is turned on.
- Skip Timing `skiptiming` - Does not report timing messages when this is turned on.
- Filter Messages `filter` - Turning this on enables the message filtering parameters below.
- Message `message` - Filter by the MIDI message content. Example "Control Change"
- Channel `channel` - Filter by the MIDI message channel. Channels range from 1 to 16.
- Index `index` - Filter by the MIDI message index. Indices range from 1 to 128.
- Value `value` - Filter by the MIDI message value. Values range from 0 to 127.
- Dir `dir` - Filter by the message direction, "input" or "output".

## Parameters - Received Messages Page
- Callbacks DAT `callbacks` - Runs this script once for each row added to the table (ie. MIDI event recieved). See [midieventDAT_Class](https://docs.derivative.ca/MidieventDAT_Class "MidieventDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a python script `op(_"opname"_).par.clear.pulse()`
- Bytes Column `bytes` - Outputs the raw bytes of the message in a separate column.

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
Extra Information for the MIDI Event DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
