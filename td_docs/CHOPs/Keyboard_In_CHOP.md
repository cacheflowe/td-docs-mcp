---
url: https://docs.derivative.ca/Keyboard_In_CHOP
category: CHOPs
title: Keyboard_In_CHOP
---

# Keyboard In CHOP
## Summary

The Keyboard In CHOP receives ASCII input from the keyboard, and outputs channels for the number of keys specified. It creates a single-frame channel representing the current state of each key.
The channels for keys are created by specifying the first key, the number of keys to follow, and the order with which they are selected. Key channel names are either determined by the name of the key, or the channel number.
**NOTE:** The Keyboard In CHOP does not handle rapid repeats of characters and does not output channels or all keys. A better way is as follows: Create a [Panel Execute DAT](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT"), and set the 'Panel' parameter to the panel in which keyboard keys need to be monitored. Set the Panel Value to: `key`. In this DAT, if you enter `print(panelValue)` in the onValueChange() callback, you will see a line printed for every keystroke.
[keyboardinCHOP_Class](https://docs.derivative.ca/KeyboardinCHOP_Class "KeyboardinCHOP Class")

## Parameters - Keys Page
- Active `active` - ⊞ - While **On** , the keyboard inputs will be monitored and the CHOP will cook every frame. When set to **Off** it will not cook and the current keyboard values will not be output. **While Playing** will capture keyboard events only when the [Timeline](https://docs.derivative.ca/Timeline "Timeline") is playing forward.
  * Off `off` -
  * On `on` -
  * While Playing `play` -

- Keys `keys` - Enter the keys to monitor create a channel for. Can be selected from the dropdown menu on the right. Valid keys are the numbers 0-9, letters A-Z, and keypad 0-9.
- Modifier Keys `modifiers` - ⊞ - If it is set to Ctrl, the keys will only go On if you are also pressing the Ctrl key. This works similarly for Alt and Shift modifiers. If it set to Ignore, it doesn't matter if the Ctrl/Alt/Shift key is down or not.
  * Ignore `ignore` -
  * None `none` -
  * Control `ctrl` -
  * Alt `alt` -
  * Control and Alt `ctrlalt` -
  * Shift `shift` -
  * Shift and Alt `shiftalt` -
  * Shift and Control `shiftctrl` -
  * Shift and Control and Alt `shiftctrlalt` -

- Channel Names `channelnames` - ⊞ - Channel names are generated automatically using one of these criteria.
  * by Key Name `key` - Keys Q W R will be called kq kw ke, based on the key name (key pad channels are named kp0, kp1...).
  * by Channel Number `number` - Channels are named k1 k2 k3 k4 based on the order of the channels.

- Panels `panels` - When a path to a [Panel COMP](https://docs.derivative.ca/Panel_Component "Panel Component")(s) is specified, only keyboard events that take place when that panel(s) has focus will reported by the Keyboard In CHOP.

## Parameters - Channel Page
This sets the [Sample Rate](https://docs.derivative.ca/CHOP_Channel_Page#Sample_Rate "CHOP Channel Page") and the [Extend Conditions](https://docs.derivative.ca/CHOP_Channel_Page#Extend_Conditions "CHOP Channel Page").
- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - The right extend conditions (after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Default Value `defval` - The value used for the Default Value extend condition.

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
Extra Information for the Keyboard In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
