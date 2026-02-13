---
url: https://docs.derivative.ca/Tablet_CHOP
category: CHOPs
title: Tablet_CHOP
---

# Tablet CHOP
## Summary

The Tablet CHOP gets the [Wacom](http://www.wacom.com) tablet X and Y values, and also gets pen tip pressure, X tilt and Y tilt, and the various pen buttons. Two pens can be used to output one set of channels for each pen. The Tablet CHOP will initialize/install when the CHOP is created.
It supports the simultaneous use of two devices (Stylus Pen, Airbrush or 4D Mouse) on the same tablet, with the "1st Pen" folder controlling the parameters of the primary device (the first one activated), and the "2nd Pen" folder controlling the parameters of the other device.
Put a channel name in a parameter to create that channel.
The range of all axes is -1.0 to 1.0. The values of the Button parameters are 0 for Button Up and 1 for Button Down. All axis and button channels are active when the Active state is On.
In most parameter fields of this CHOP, if you put a channel name in the parameter, it will attempt to read that parameter and output the channel. Otherwise no channel is created.
For advice on setting up the tablet and tuning the sensitivity of the pen and tablet, please read the [Wacom Intuos](https://docs.derivative.ca/Wacom_Intuos_Tablet "Wacom Intuos Tablet") article.
[tabletCHOP_Class](https://docs.derivative.ca/TabletCHOP_Class "TabletCHOP Class")

## Parameters - 1st Pen Page
This page let you assign channels names for the inputs from the 1st Pen assigned to the tablet.
- X Coordinate `xcoord` - The channel name for the movement of the pen in the x direction.
- Y Coordinate `ycoord` - The channel name for the movement of the pen in the y direction.
- Pressure `pressure` - The channel name for the pressure reported by the pen.
- X Tilt `xtilt` - The channel name for the tilt of the pen in the x direction.
- Y Tilt `ytilt` - The channel name for the tilt of the pen in the y direction.
- Finger Wheel `tanpressure` - The channel name for a finger rollar wheel if available.
- Thumb Wheel `zcoord` - The channel name for a thumb rollar wheel if available.
- Rotation `rotation` - The channel name for the rotation the pen is reporting.
- Button 1 `button1` - The channel name for the button reported as Button 1.
- Button 2 `button2` - The channel name for the button reported as Button 2.
- Button 3 `button3` - The channel name for the button reported as Button 3.
- Button 4 `button4` - The channel name for the button reported as Button 4.
- Button 5 `button5` - The channel name for the button reported as Button 5.

## Parameters - 2nd Pen Page
The second pen has the same parameters as the first pen, and the values are taken from the second device.

## Parameters - Channel Page
- Active `active` - ⊞ - While **On** , the pen movement will be output from and the CHOP will cook every frame. When set to **Off** it will not cook and the values will not be updated. **While Playing** will capture pen events only when the [Timeline](https://docs.derivative.ca/Timeline "Timeline") is playing forward.
  * Off `off` -
  * On `on` -
  * While Playing `play` -

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
Extra Information for the Tablet CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
