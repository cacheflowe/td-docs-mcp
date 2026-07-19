---
url: https://docs.derivative.ca/MIDI_In_DAT
category: DATs
title: MIDI_In_DAT
---

# MIDI In DAT

## Summary

The MIDI In DAT logs all [MIDI](../Interoperability/MIDI.md "MIDI") messages coming into TouchDesigner from a specified MIDI device. It outputs columns in a table format - message, type, channel, index, value.

However general setup is simpler. Once you have MIDI set up via the Dialogs -> MIDI Device Mapper, TouchDesigner is ready to receive MIDI via Select CHOPs that point to `/local/maps/map1` for device 1, etc.

Also note that the controller indices reported by the MIDI In DAT are always converted to the 1 based range 1-128.

#### Columns Representing MIDI Event Timestamps

Five columns express the timestamp of the MIDI events coming from the operating system in in different ways:
  * `timestamp` - the actual timestamp number coming from the operating system in miliseconds
  * `delta_timestamp` - # of milliseconds between the MIDI event and the previous event
  * `timeslice_msec` - the time of the event within the current [timeslice](../Glossary/Time_Slicing.md "Time Slicing") in milliseconds. This is a calculated value based on an even resampling of all events received in a frame, hence differs from 'timestamp'
  * `absmsec` - [absolute time](../Glossary/Absolute_Time.md "Absolute Time") of the event expressed in integer milliseconds. This is a calculated value based on an even resampling of all events received in a frame, hence differs from 'timestamp'
  * `absframe` - same as `absTime.frame`, the absolute frame number the event was processed in

To see the MIDI event info as a CHOP, create a [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP"), set the Mode to "Automatic High Frequency" to a Trail CHOP and move a slider quickly to see the density of sample changes.

See also the [MIDI Event DAT](MIDI_Event_DAT.md "MIDI Event DAT"), [MIDI In Map CHOP](../CHOPs/MIDI_In_Map_CHOP.md "MIDI In Map CHOP"), [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP"), [MIDI Out CHOP](../CHOPs/MIDI_Out_CHOP.md "MIDI Out CHOP"), Tscript `midi()` Command, [MIDI Device Mapper Dialog](https://docs.derivative.ca/MIDI_Device_Mapper_Dialog "MIDI Device Mapper Dialog").

[midiinDAT_Class](MIDI_In_DAT_Class.md "MidiinDAT Class")

## Parameters - Connect Page
- Active `active` - Logs MIDI events when turned on.
- Device Table `device` - Path to the MIDI device [Table DAT](../Glossary/Table_DAT.md "Table DAT")
- Device ID `id` - Path to the MIDI device [Table DAT](../Glossary/Table_DAT.md "Table DAT")

14 Bit Values `value14` - Turn on 14 Bit MIDI Event logging. The two 7-bit messages are consolidated and treated as a single 14-bit value to be outputted, unlike the MIDI Event DAT where both messages are outputted separately.

The incoming 7-bit messages must follow this specification to be properly interpreted as 14-bit:
  * Of the two messages, one is the MSB (Most Significant Byte) and the other is the LSB (Least Significant Byte), the values of which are combined to interpret the 14-bit value.
  * MSB message must be in the controller range 0-31.
  * LSB message must be in the controller range 32-63. And it's index should be MSB index + 32. i.e. if the MSB message has index 12, then the LSB message must have index 44.
  * In addition, the index pairs 98, 99 and 100, 101 can also be used as MSB, LSB pairs.
  * If only MSB message is received, nothing will be outputted. If multiple LSB messages are received sequentially without an MSB message, the value of the last received MSB message will be used to calculate the 14 bit value.
  * In this mode, messages in the index range 64-95 will be interpreted as 7 bit and be outputted as such since the range 64-95 is reserved for 7 bit messages.

## Parameters - Filter Page
- Skip Sense `skipsense` - Does not log sense messages when this is turned on.
- Skip Timing `skiptiming` - Does not report timing messages when this is turned on.
- Filter Messages `filter` - Turning this on enables the message filtering parameters below.
- Message `message` - Filter by the MIDI message content. Example "Control Change"
- Channel `channel` - Filter by the MIDI message channel. Channels range from 1 to 16.
- Index `index` - Filter by the MIDI message index. Indices range from 1 to 128.
- Value `value` - Filter by the MIDI message value. Values range from 0 to 127.

## Parameters - Received Messages Page
- Callbacks DAT `callbacks` - Runs this script once for each row added to the table (ie. each MIDI event received). See [midiinDAT_Class](MIDI_In_DAT_Class.md "MidiinDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location (for example, where 'cc' points to).
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.
- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute from is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator.
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

Extra Information for the MIDI In DAT can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

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
