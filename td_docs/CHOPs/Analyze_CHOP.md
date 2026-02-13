---
url: https://docs.derivative.ca/Analyze_CHOP
category: CHOPs
title: Analyze_CHOP
---

# Analyze CHOP
## Summary

The Analyze CHOP looks at the values of all the values of a channel, and outputs a single-number result into the output. The output is one sample long. It can analyze for maximum, average, peaks and other aspects of a channel.
[analyzeCHOP_Class](https://docs.derivative.ca/AnalyzeCHOP_Class "AnalyzeCHOP Class")

## Parameters - Analyze Page
- Function `function` - ⊞ - This menu determines the function applied to the channel.
  * Average `average` - The average of the channel.
  * Maximum `maximum` - The maximum value of the channel.
  * Minimum `minimum` - The minimum value of the channel.
  * Index of Maximum `maximumindex` -
  * Index of Minimum `minimumindex` -
  * Sum `sum` - The sum of all the samples in the channel.
  * RMS Power `rmspower` - The RMS (root-mean-square) of the channel.
  * Value of First Peak `firstpeakvalue` - The value of the first peak in the channel.
  * Index of First Peak `firstpeakindex` - The index of the first peak in the channel. The index of the first sample is 0.
  * Value of Last Peak `lastpeakvalue` -
  * Index of Last Peak `lastpeakindex` -
  * Value of Highest Peak `highestpeakvalue` - The value of the highest peak in the channel.
  * Index of Highest Peak `highestpeakindex` - The index of the highest peak in the channel. If multiple samples have the same highest peak value, it returns the index of the last peak sample.
  * Value of Lowest Peak `lowestpeakvalue` - The value of the lowest peak in the channel.
  * Index of Lowest Peak `lowestpeakindex` - The index of the lowest peak in the channel. If multiple samples have the same lowest peak value, it returns the index of the last peak sample.
  * Total Peaks `totalpeaks` - The total number of peaks in the channel.
  * Duplicates `duplicates` - This will create two extra channels per input channel for total number of duplicates of a specific value (count) as well as first sample index that value appeared in the channel (index).

- Allow Start Peaks `allowstart` - If the values of the first 2 samples are v0 and v1, if v0 > v1, count it as a peak. The default is to never count the first sample as a peak.
- Allow End Peaks `allowend` - If the values of the last 2 samples are vn and vm, if vm > vn, count it as a peak. The default is to never count the last sample as a peak.
- No Peak Value `nopeakvalue` - When no peaks are found, make this number (default is `-1`) the result that is output. When the Function is set to Peak Index or Peak Value, it is a way to detect that no peaks were found.
- Analyze Valleys vs Peaks `valleys` - Analyze instead for the First Valley, Highest Valley, and Lowest Valley, when the corresponding Function menu options are chosen.

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
Extra Information for the Analyze CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
