---
url: https://docs.derivative.ca/Multi_Touch_In_DAT
category: DATs
title: Multi_Touch_In_DAT
---

# Multi Touch In DAT
## Summary

The Multi Touch In DAT is used for receiving messages and events from the Windows standard multi-touch API. It captures all the messages, where each new message changes the table it outputs. When a messages is added to the DAT, any script can be called pointing to the new message. The Multi Touch In DAT can be sent to the [Render Pick DAT](https://docs.derivative.ca/Render_Pick_DAT "Render Pick DAT"), or used with interactTouch methods in the [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") and [Web Render TOP](https://docs.derivative.ca/Web_Render_TOP "Web Render TOP"). Multi Touch DAT is not supported on macOS.
It can output either of two table formats: (1) Raw Events as a FIFO (first in - first out) list, or (2) ID Table, which is the events processed into a more usable one-row-per-finger table.
The Raw Events format creates a FIFO-type DAT (see also [FIFO DAT](https://docs.derivative.ca/FIFO_DAT "FIFO DAT")) which, for each multi-touch event, has a row added to the bottom of the table while at the same time a row at the top is deleted.
Note: To operate panel gadgets with multi-touch screens that send events through the Windows event stream, multi-touch works without requiring DATs. You need to use the DAT when using multiple fingers on one panel, like in a container displaying a 3D render whose objects you want to pick.
The ID table format includes the columns:
  * `id` - every finger press increases the id by 1
  * `sn` - an ongoing count of each finger press.
  * `select` - when 1, this row represents a finger is down.
  * `downf` - the absolute frame number when the finger press occurred.
  * `upf` - the absolute frame number that the finger press ended
  * `x`, `y` - the position, in pixels in the horizontal and vertical directions. `NOTE`: The `x` and `y` values are expressed in screen pixels, not panel width/height pixels. For example, the top-right corner of a panel will be different if the panel is scaled within another panel, window or network viewer. It is better to use `u` and `v`, and scale them by the panel Width and Height.
  * `u`, `v` - the position, 0 to 1 in the horizontal and vertical directions
  * `downu`, `downv` - the position, 0 to 1 in the horizontal and vertical directions when the touch first occured (ie. initial touch down location).

`contactx`, `contacty` - the width of the contact area. `contactu`, `contactv` - the height of the contact area.
  *     * `monitor` - monitor number, starting with 0
  * `clicktime` - like `downf`, in seconds
  * `elapsedtime` - the number of seconds that finger has been down.
  * `changedtime` - the time since the finger press that the most recent u or v value changed.
  * `dclick` - double-tap occurred
  * `aux` - user supplied data via the [PanelCOMP_Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class") method `interactTouch()`. When the event is triggered by the mouse via the Include Mouse option, `aux` will include the mouse buttons used (`1` for left, `2` for middle, `4` for right, can be tested bitwise).

You can use the attached callback DAT (named `mtouchin1_callbacks`) to react to multi-touch events. This is suitable for 2D interfaces that do not require a [Render Pick DAT](https://docs.derivative.ca/Render_Pick_DAT "Render Pick DAT").
See the [Palette:multiTouch](https://docs.derivative.ca/Palette:multiTouch "Palette:multiTouch") example in the [Palette](https://docs.derivative.ca/Palette "Palette") under Tools.
See also the [MultiTouch](https://docs.derivative.ca/MultiTouch "MultiTouch") page.
[multitouchinDAT_Class](https://docs.derivative.ca/MultitouchinDAT_Class "MultitouchinDAT Class")

## Parameters - Multi Touch In Page
- Active `active` - Registers event when Active is On.
- Output `outputtype` - ⊞ - Sets how the output is displayed in the table.
  * Raw Events `log` - Events are added to the table in a first in - first out (FIFO) order.
  * ID Table `changes` - Events are processed using one-row-per-finger in the table.

- Panel `panel` - The [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") to capture the touch events from.
- Relative IDs `relativeid` - Reorder the touch ids so only the ones within the specified panel are counted.
- Relative Position `relativepos` - Output position and normalized coordinates relative to lower left corner of the specified panel.
- Occlude Panels by Hierarchy `occlusion` - Only children of the specified panel will receive multitouch events. Touches on parent and sibling panels are ignored.
- Occlude Panels by Depth Layer `occbydepth` - Enable filtering out multitouch events by Panel Depth Layer.
- Occlude Panels Above Depth `occdepthlayer` - Multitouch events from panels with a Depth Layer larger than this value will be ignored.
- Include Mouse `mouse` - When on, the mouse add a touch event when clicked. This event always shares ID 1 with the first touch. Using mouse and multitouch at the same time may result in unexpected behaviours.
- Position Threshold `posthresh` - A new message will not be added if a finger has moved less than this number of units. The units are determined by the input device, not necessarily the resolution of the screen that it is associated with.
- Contact Threshold `contactthresh` - Some touch devices have a width and height of a press, representing pressure of amount of finger contact. This is a minimum threshold below which no events are recognized.
- Min Rows Displayed `minrows` - The minimum number of rows always displayed in the table.
- Double Click (secs) `doubleclickthresh` - The maximum time allowed between clicks to be registered as a 'double-click'.

## Parameters - Received Messages Page
- Callbacks DAT `callbacks` - Path to a DAT containing callbacks.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location (for example, where 'cc' points to).
  * Callbacks DAT `callbacks` - The script is executed from the location of the Callbacks DAT specified above.
  * Specified Operator `op` - The script is executed from the component specified in the Component parameter below.

- From Operator `fromop` - The path that the script will be executed from if the Execute From parameter is set to _Specified Operator_.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a script command, here is an example: `opparm -c /serial1 clear`

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
Extra Information for the Multi Touch In DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
