---
url: https://docs.derivative.ca/Resample_CHOP
category: CHOPs
title: Resample_CHOP
---

# Resample CHOP
## Summary

The Resample CHOP resamples an input's channels to a new sample rate and/or start/end interval. In all cases, the entire input interval is resampled to match the output interval.
Resample does a simple linear interpolation of the Time Slice in [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing") mode. Only the sample rate can be changed.
[resampleCHOP_Class](https://docs.derivative.ca/ResampleCHOP_Class "ResampleCHOP Class")

## Parameters - Resample Page
- Method `method` - ⊞ - The resample method to apply to the channels:
  * Same Rate, New Interval `strech` - Stretches or compresses the channels like the [Stretch CHOP](https://docs.derivative.ca/Stretch_CHOP "Stretch CHOP").
  * New Rate, Same Time Range `preserve` - Changes the sample rate without changing the time-length of the CHOP.
  * New Rate, Same Index Range `index` - Changes the sample rate without changing the number of samples in the CHOP.
  * New Rate, New Interval `newint` - Changes both the sample rate and stretches/compresses the CHOP.

- Sample Rate `rate` - The new sample rate.
- Unit Values `relative` - ⊞ - Determines how the Start/End parameters are interpreted.
  * Absolute `abs` - The value is the new start/end position.
  * Relative to Start/End `rel` - The value is a shift from the old start/end position.
  * Relative to Current Frame `cur` -

- Start `start` - The CHOP's new start position.
- Start Unit `startunit` -
- End `end` - The CHOP's new end position.
- End Unit `endunit` -
- Quaternion Blend `quatrot` - Uses quaternions to blend between samples.
- Interpolation `interp` - ⊞ - The interpolation method to use when resampling:
  * No Interpolation `nointerp` - Use the value of the nearest sample.
  * Linear `linear` - Use linear interpolation between samples when the output has more samples. Averages all samples near the new sample when the output has fewer samples.
  * Cubic `cubic` - Cubically interpolates between samples, for smoother curves than Linear. This method is not recommended for channels with sharp changes.
  * Pulse Preserve `edge` - A linear interpolation that recognizes single sample pulses and preserves their height and one-sample width. A pulse is a non-zero value proceeded and followed by zero-value samples.
  * Repeat Samples `edge` - This interpolation provides better spaced results when the lengths are integer multiples of original.

- Constant Area `constarea` - If enabled, keeps the area under the channel constant by scaling the values of the channel.
- Correct for Cycles `correct` - If enabled, compensates for cyclic channels (such as angles) by always choosing the shortest step between samples, like 360 to 0 for angles.
- Cycle Length `cyclelen` - The length of the cycle. 360 is typical for angles.
- Use Last Frame Only `uselastframe` - Trim to the input CHOP's last frame and perform the resample on that

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
Extra Information for the Resample CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
