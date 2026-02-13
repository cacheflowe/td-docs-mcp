---
url: https://docs.derivative.ca/Mouse_In_CHOP
category: CHOPs
title: Mouse_In_CHOP
---

# Mouse In CHOP
## Summary

The Mouse In CHOP outputs X and Y screen values for the mouse device and monitors the up/down state of the three mouse buttons.
When the Active flag is on, the Mouse X and Y positions are output through the channels named in the Position X and Y parameters and the button states are output through the channels named in the Left, Right and Middle Button parameters.
The button values are 0 for Button Up and 1 for Button Down.
The Mouse In CHOP and [Keyboard In CHOPs](https://docs.derivative.ca/Keyboard_In_CHOP "Keyboard In CHOP") are sometimes connected to the Position and Active inputs respectively of the [Record CHOP](https://docs.derivative.ca/Record_CHOP "Record CHOP") to enable the recording of channels.
[mouseinCHOP_Class](https://docs.derivative.ca/MouseinCHOP_Class "MouseinCHOP Class")

## Parameters - Control Page
- Active `active` - ⊞ - While **On** , the mouse movement will be output from and the CHOP will cook every frame. When set to **Off** it will not cook and the current mouse X or Y values will not be output. **While Playing** will capture mouse events only when the [Timeline](https://docs.derivative.ca/Timeline "Timeline") is playing forward.
  * Off `off` -
  * On `on` -
  * While Playing `play` -

- Output Coordinates `output` - ⊞ - Controls the range of the mouse Position X and Position Y.
  * Normalized `normal` - X and Y mouse positions are normalized to a range of 2 units per monitor. The primary monitor will be -1 to 1 with X=0 and Y=0 at the center of the monitor. Other monitors will be relative to these values. For example a monitor directly to the left of the primary monitor would have values in the range -1 on the right to -3 on the left of it.
  * Normalized Aspect `aspect` - Following the same rules as Normalized, but normalized and adjusted to aspect ratio.
  * Absolute `absolute` - Raw screen coordinates in pixel units. (0,0) is the bottom left of the primary monitor.

- Position X `posxname` - The name of the channel that returns the horizontal movement of the mouse.
- Position Y `posyname` - The name of the channel that returns the vertical movement of the mouse.
- Left Button `lbuttonname` - The name of the channel that returns the state of the left button.
- Right Button `rbuttonname` - The name of the channel that returns the state of the right button.
- Middle Button `mbuttonname` - The name of the channel that returns the state of the middle button.
- Wheel `wheel` - This channel goes up when the wheel is rolled away from the user and goes down when it is rolled the other way.
- Wheel Increment `wheelinc` - The amount that is added or subtracted to the current value of the Wheel channel when the wheel is moved.
- Monitor `monitor` - This channel returns which monitor the mouse cursor is currently on.
- Panels `panels` - Events are only triggered when the specified panel has focus.

## Parameters - Channel Page
This sets the [Sample Rate](https://docs.derivative.ca/CHOP_Channel_Page#Sample_Rate "CHOP Channel Page") and the [Extend Conditions](https://docs.derivative.ca/CHOP_Channel_Page#Extend_Conditions "CHOP Channel Page").
- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

- Extend Right `right` - ⊞ - The right extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

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
Extra Information for the Mouse In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
