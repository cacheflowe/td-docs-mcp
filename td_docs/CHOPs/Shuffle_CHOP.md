---
url: https://docs.derivative.ca/Shuffle_CHOP
category: CHOPs
title: Shuffle_CHOP
---

# Shuffle CHOP
## Summary

The Shuffle CHOP reorganizes the samples in a set of channels.
It is useful for transforming data received by the [SOP to CHOP](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP") and [TOP to CHOPs](https://docs.derivative.ca/TOP_to_CHOP "TOP to CHOP") into channels containing only one row or column. Data can be easily manipulated, then transformed back if needed.
[shuffleCHOP_Class](https://docs.derivative.ca/ShuffleCHOP_Class "ShuffleCHOP Class")

## Parameters - Shuffle Page
- Method `method` - ⊞ - Chooses the operation "shuffle" performs:
  * Off `off` -
  * Swap Channels and Samples `swap` - Performs a channel transpose operation, by storing all samples at the same index in the same channel. If 25 channels are in the CHOP with a length of 33 samples, 33 channels will be created with a length of 25.
  * Sequence Channels by Name `seqname` - Sequence channels together that share the same alphabetic name, in the order of their number. (i.e. chan2, chan3 and chan1 would be sequenced in the order chan1, chan2, chan3).
  * Sequence All Channels `seqall` - Sequence all channels in the CHOP resulting in one long channel.
  * Sequence N Channels `seqn` - Sequence channels in groups of N together. For N=4, channels 0 to 3, 4 to 7, etc. will be sequenced.
  * Sequence Every Nth Channel `seqeveryn` - Sequence every Nth channel together. For N=4, channels 0,4,8,.., 1,5,9,..., etc. will be sequenced.
  * Sequence All Samples `sallsamples` -
  * Split All Samples `splitall` - Split every channel into channels of 1 sample, each containing a different sample from the original channel.
  * Split N Samples `splitn` - Split each channel into segments of N samples (specified below).
  * Split Every Nth Sample `spliteveryn` - Take every Nth sample from the original to form N new channels.

For all splitting operations, channels will be numbered according to their segment number. (i.e. chan would be split into chan1, chan2, chan3, etc).
- N Value `nval` - The value of N for Sequence: Every Nth Channel, Sequence N Channels, Split N Samples and Split Every Nth Sample.
- Use First Sample Only `firstsample` - Just use the first sample of each channel.

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
Extra Information for the Shuffle CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
