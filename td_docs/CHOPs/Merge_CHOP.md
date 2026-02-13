---
url: https://docs.derivative.ca/Merge_CHOP
category: CHOPs
title: Merge_CHOP
---

# Merge CHOP
## Summary

The Merge CHOP takes multiple inputs and merges them into the output. All the channels of the input appear in the output. The channel order is the channels of the first input followed by the channels of the second input, and so on.
Channel names may conflict, but a channel is renamed according to the Duplicate Names menu. The CHOP appends or increments the digits of the channel name until an unused name is found.
When the Time Slice flag on the Common parameter page is on, the Merge CHOP will merge only the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") of a channel, not the entire length of all the channels.
[mergeCHOP_Class](https://docs.derivative.ca/MergeCHOP_Class "MergeCHOP Class")

## Parameters - Merge Page
- Align `align` - ⊞ - This menu handles cases where multiple input CHOPs have different start or end times. All channels output from a CHOP share the same start/end interval, so the inputs must be treated with the Align Options:
  * Automatic `auto` - It will trim to the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") if there are any Time Slices, else it will do an Extend Min/Max.
  * Extend to Min/Max `none` - Find the earliest start and latest end, and extend all inputs to that range using the extend conditions. (see [Extend Conditions](https://docs.derivative.ca/CHOP_Channel_Page#Extend_Conditions "CHOP Channel Page")).
  * Stretch to Min/Max `stretch` - Find the earliest start and latest end, and stretch every channel's start and end to that range.
  * Shift to Minimum `start` - Find the earliest start and shift all channels so they all start at that index. All channels are extended to the length of the longest one.
  * Shift to Maximum `end` - Find the latest end and shift all channels so they all end at that index. Extend all channels to the length of the longest one.
  * Shift to First Interval `shift1` - Shift all channels to the start of the first CHOP and sample all inputs using the first input's range.
  * Trim to First Interval `trim1` - Trim all channels to first CHOP's range.
  * Stretch to First Interval `stretch1` - Stretch all channels to the first CHOP's range.
  * Trim to Smallest Interval `trim` - Trim all channels to the smallest start/end interval. The start and end values may not come from the same channel.
  * Stretch to Smallest Interval `squash` - Stretch all channels to the smallest start/end interval. The start and end values may not come from the same channel.

- Duplicate Names `duplicate` - ⊞ - When channels of the input CHOPs have the same name, this menu determines what to do.
  * Make Unique `unique` - Include all the input channels, and when there is a conflict of name, make the new channel's name similar but unique by adding digits to the name.
  * Keep First `first` - Include the channel of the first input CHOP which the name appears in, and discard any further channels with the same name.
  * Keep Last `last` - Include the channel of the last input CHOP which the name appears in, and discard any other channels with the same name.
  * Replace First with Last `replace` -

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

## Info CHOP Channels
Extra Information for the Merge CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
