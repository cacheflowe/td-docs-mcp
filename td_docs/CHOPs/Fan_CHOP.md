---
url: https://docs.derivative.ca/Fan_CHOP
category: CHOPs
title: Fan_CHOP
---

# Fan CHOP
## Summary

The Fan CHOP converts one channel out to many channels, or converts many channels down to one.
Its first operation, **Fan Out** , takes one channel and generates 2 or more channels. It sets to 1 one of the output channels while all others are 0, based on the input channel's value. The first output channel is index value 0, the second, 1, and so on. If the input value is above N-1 or below 0, the value can be clamped, cycled or ignored.
For example, if the value of the input channel at a certain frame is 4, and if the CHOP outputs 8 channels, the fifth channel will have a value of 1, and all other channels will have a zero value at that frame.
The input is assumed to have 1 channel which contains integer values; fractions are truncated and extra channels are ignored. The output channels are binary (0 or 1) channels.
The second operation, **Fan In** , does the opposite: it takes a bunch of binary inputs and produces one channel containing the index of the "On" channel. If more than one input channel is "On", the first "On" input channel is selected.
[fanCHOP_Class](https://docs.derivative.ca/FanCHOP_Class "FanCHOP Class")

## Parameters - Fan Page
- Operation `fanop` - ⊞ - Selects either Fan In or Fan Out.
  * Fan Out `out` - Takes one channel and generates 2 or more channels. It sets to 1 one of the output channels while all others are 0, based on the input channel's value. The first output channel is index value 0, the second, 1, and so on. If the input value is above N-1 or below 0, the value can be clamped, cycled or ignored. The number of channels generated depends on the 'Channel Names' parameter.
  * Fan In `in` - Takes multiple channels as input and produces one channel containing the index of the "On" channel. If more than one input channel is "On", the first "On" input channel is selected. For example if there are 5 channels (chan1, chan2, chan3, chan4, chan5), and chan3 is 1 while the others are 0, then the output channel value will be equal to 2, since the indexing is 0-based.

- Channel Names `channame` - The names for the output channels that this CHOP creates. This also controls how many output channels are created (one for each name) in Fan Out mode. In Fan In mode, only one channel is created, and its name is the base name (minus the number suffix) of the first input channel.
- Outside Range `range` - ⊞ - Determines how to handle input values that are outside the index range (0 to N-1).
  * Clamp Index `clamp` - If less than 0, clamp to 0, and if greater than N-1, clamp to N-1.
  * Loop Index `loop` - Loop back through the index list.
  * Set Channels To 0 `zero` - Don't select any channels; set every channel to zero.

- All Channels Off `alloff` - ⊞ - For a Fan In operation, when all input channels are off, set the output to -1 or 0.
  * Set To 0 `set0` - Selects the first channel.
  * Set To -1 `setneg` - Doesn't select any of the channels.

- Quantize Output `quantize` - On by default. Channels are quatized to the nearest integer. For example, if the input channel's value is 5.6 and 6 channels are created, channel 5 is 1, while the rest are 0.

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
Extra Information for the Fan CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
