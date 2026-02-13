---
url: https://docs.derivative.ca/Override_CHOP
category: CHOPs
title: Override_CHOP
---

# Override CHOP
## Summary

The Override CHOP lets you take inputs from several CHOP sources, and uses the most-recently changed input channels to determine the output. For example, if a 16-channel CHOP comes from one MIDI device, and another 16-channel CHOP comes from another place like another device or a preset, then Override selects the most recently-changed channels and outputs those values.
The Override CHOP outputs the same channels as the first input. If subsequent inputs have more or less channels than the first input, the missing/extra channels are ignored. The output defaults to the channel values of the first input, but when a value changes in any monitored channel, that value will become the new output for the corresponding channel name or number. If the same channel name or number is changing in two or more inputs at the same time, precedence is given by input order.
The Override CHOP output is reset to the default each time the number of inputs to the CHOP changes or the method of matching (by number or by name) changes.
The CHOP length is the length of the first input. From frame to frame, if all values are the same, the output is unchanged.
An optional channel can be created that will tell you which input has the most recently changed channel.
[overrideCHOP_Class](https://docs.derivative.ca/OverrideCHOP_Class "OverrideCHOP Class")

## Parameters - Override Page
- Match by `match` - ⊞ - Monitors the channels in each input and matches them according to this menu.
  * Channel Number `index` - Matches channels by their order number.
  * Channel Name `name` - Matches channels by their name.

- Create Input Index `makeindex` - Creates a channel (specified by the Channel Name parameter below) that is an index indicating which input has the most recently changed channel.
- Channel Name `indexname` - Specifies the name of the index channel. Only used if the Create Input Index checkbox is selected.
- Monitor on Input Cooks `cookmonitor` - Deprecated.

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
Extra Information for the Override CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
