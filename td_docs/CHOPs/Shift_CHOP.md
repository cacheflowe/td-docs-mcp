---
url: https://docs.derivative.ca/Shift_CHOP
category: CHOPs
title: Shift_CHOP
---

# Shift CHOP
## Summary

The Shift CHOP time-shifts a CHOP, changing the start and end of the CHOP's interval. However, the contents of the channels remain the same.
Each channel can be shifted a different amount by using the $C variable in the Scroll parameter or the Start/End parameters.
An optional second input, the Start/End Reference, is used to align the first input CHOP relative to another reference CHOP. This outputs the channels of the first CHOP only, and the shifts are based on the interval of the second CHOP. It is useful for making several CHOPs match up to the same time.
[shiftCHOP_Class](https://docs.derivative.ca/ShiftCHOP_Class "ShiftCHOP Class")

## Parameters - Shift Page
- Reference `reference` - ⊞ - The start or the end of the channels can be used as the reference position. The channels are shifted by altering the reference position.
  * Start Position `refstart` - Uses the start of the CHOP to do the aligning.
  * End Position `refend` - Uses the end of the CHOP to do the aligning.

- Unit Values `relative` - ⊞ - Determines how the Start and End parameters are to be interpreted:
  * Absolute `abs` - The Start/End parameters are the actual start/end position. It is used, for example, to shift the CHOP to start at 0 seconds.
  * Relative to Start/End `rel` - The Start/End parameters are a shift relative to the input CHOP's start/end position.
  * Relative to Current Frame `cur` - Ignore the Start/End parameters and use the current frame as the new start position.

- Start `start` - The start of the interval, absolute or relative to the input CHOP.
- Start Unit `startunit` -
- End `end` - The end of the interval, absolute or relative to the input CHOP.
- End Unit `endunit` -
- Scroll Offset `scroll` - Without changing the length of the CHOP, you can scroll the channels within its range, and scroll each channel a different amount. By using $C in the parameter, you can make the scroll amount dependent on the channel index.
- Scroll Offset Unit `scrollunit` -

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Shift CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
