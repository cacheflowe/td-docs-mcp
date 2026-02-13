---
url: https://docs.derivative.ca/Stretch_CHOP
category: CHOPs
title: Stretch_CHOP
---

# Stretch CHOP
## Summary

The Stretch CHOP preserves the shape of channels and the sampling rate, but resamples the channels into a new interval. All data in the range is stretched or compressed to the new start and end positions.
A Reverse Interval parameter reverses the order of the samples of each channel.
[stretchCHOP_Class](https://docs.derivative.ca/StretchCHOP_Class "StretchCHOP Class")

## Parameters - Stretch Page
- Interpolation `interp` - ⊞ - The interpolation method to use when resampling.
  * No Interpolation `nointerp` - Use the value of the nearest sample.
  * Linear `linear` - Use linear interpolation between samples when the interval is lengthened. Averages all samples near the new sample when the interval is shortened.
  * Cubic `cubic` - Cubically interpolates between samples, for smoother curves than Linear. This method is not recommended for channels with sharp changes.
  * Pulse Preserve `edge` - A linear interpolation that recognizes single sample pulses and preserves their height and one sample width. A pulse is a non-zero value preceded and followed by zero-value samples.
  * Repeat Samples `repeat` - This interpolation provides better spaced results when the lengths are integer multiples of original.

- Constant Area `constarea` - If enabled, keeps the area under the channel constant by scaling the values of the channel.
- Unit Values `relative` - ⊞ - Determines how Start/End parameters are interpreted:
  * Absolute `abs` - The value is the new start/end position.
  * Relative to Start/End `rel` - The value is a shift from the old start/end position.
  * Relative to Current Frame `cur` -

- Start `start` - ⊞ - The CHOP's new start position.
  * Start `start` -
  * Start Unit `startunit` -

- End `end` - ⊞ - The CHOP's new end position.
  * End `end` -
  * End Unit `endunit` -

- Length Scale `scale` - Scales the length of the channel after determining the start/end interval. Good for doubling or halving the length.
- Reverse Interval `reverse` - Reverses the channel so that it plays backwards.
- Start Unit `startunit` -
- End Unit `endunit` -

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
Extra Information for the Stretch CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
