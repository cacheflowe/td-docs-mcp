---
url: https://docs.derivative.ca/Keyboard_In_DAT
category: DATs
title: Keyboard_In_DAT
---

# Keyboard In DAT
## Summary

The Keyboard In DAT lists the most recent key events in its FIFO (first in/first out) table. There is one row for every key press down and every key-up, including Shift, Ctrl and Alt, with distinction between left and right side. For convenience, with each key press, a column indicates if the Shift, Ctrl and Alt were being held down at the time.
You get key presses even of the cursor is outside the TouchDesigner windows, whether they are control panels, Perform Mode or the network editor window. Exceptions: while entering text in the editor window.
You can set a filter to watch only certain keys. Custom shortcuts can be defined and handled by a [python callback in the attached script](https://docs.derivative.ca/KeyboardinDAT_Class "KeyboardinDAT Class").
[keyboardinDAT_Class](https://docs.derivative.ca/KeyboardinDAT_Class "KeyboardinDAT Class")

## Parameters - Keyboard In Page
- Active `active` - Inhibits and allows message to be added to log.
- Perform Window Only `perform` - When on, key events are only detected while in perform mode.
- Keys `keys` - List of keys to allow through the filter. Just put the characters in the list, space-separated. Eg. '1 2 g h' for the 1, 2, g and h keys. Only these keys will be added to the log and generate an event. If blank, no filtering will be done. List of accepted keys: [Keyboard UI](https://docs.derivative.ca/Keyboard_UI "Keyboard UI")
- Shortcuts `shortcuts` - List of shortcuts to watch for. See "Shortcuts" in the notes for defining shortcuts.
- Panels `panels` - Optional list of references to panels to detect events from. Events will only be fired when any of the listed panels has focus.
- Left/Right Modifiers `lrmodifiers` - When on, the states of the left and right modifier keys (see Notes) will be added to the table. Switching the state of this parameter will reset the table's contents.

## Parameters - Log Page
- Callbacks DAT `callbacks` - Path to a DAT containing callbacks for each keyboard event received. See keyboardinDAT_Class for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location (for example, where 'cc' points to).
  * Callbacks DAT `callbacks` -
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a python script `op(_"opname"_).par.clear.pulse()`

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

## Notes
**Shortcuts** are defined by a list of modifier keys (see below) and a "trigger" key separated by .'s.
For example, `ctrl.shift.a` the modifier keys are ctrl and shift, and the trigger key is a. This shortcut will be activated when one of the ctrl and shift keys are pressed and the trigger key, a is pressed down. If any other modifier keys are pressed, the shortcut will not be detected.
Modifier Keys - The following are all the valid modifier keys:
  * `lalt` - Left alt key.
  * `ralt` - Right alt key.
  * `alt` - Either left or right alt key.
  * `lctrl` - Left ctrl key.
  * `rctrl` - Right ctrl key.
  * `ctrl` - Either left or right ctrl key.
  * `lshift` - Left shift key.
  * `rshift` - Right shift key.
  * `shift` - Either left or right shift key.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Keyboard In DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
