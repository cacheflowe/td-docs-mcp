---
url: https://docs.derivative.ca/Lookup_CHOP
category: CHOPs
title: Lookup_CHOP
---

# Lookup CHOP
## Summary

The Lookup CHOP outputs values from a lookup table. The first input (the Index Channel) is an index into the second input (the Lookup Table). Lookup outputs interpolated values from the lookup table.
Both the Index and Lookup Tables can contain any number of channels.
An Index sample with value 0 maps to the beginning (first sample) of the lookup table, and an index sample with value of 1 maps to the end (last sample) of the lookup table.
The output CHOP is the same length as the Index input. It is the same number of channels as the Lookup Table input, and has the same channel names as the Lookup Table input. The output is filled with the data extracted from the lookup tables. Indexes that fall between two lookup table samples are interpolated. The lookup table can be sampled outside its range.
NOTE: The Extend Conditions of the lookup table are used in this case where the index is less than 0 or greater than 1.
The sample rate of the output is the sample rate of the Index input.
The Lookup CHOP can be used to fetch values from a color lookup table, where a single index produces red, green and blue channels. It can also be used for rolloff or decay tables, where it specifies how much a parameter drops with distance.
[lookupCHOP_Class](https://docs.derivative.ca/LookupCHOP_Class "LookupCHOP Class")

## Parameters - Lookup Page
- Index Range `index` - ⊞ - The Index Range maps the index channel's values to the lookup table's start and end and defaults to 0 and 1. The first parameter represents the start of the lookup table. When the index channel has this value, it will index the start of the lookup table. The second parameter represents the end of the lookup table and behaves in the same way.
  * `index1` -
  * `index2` -

- Cyclic Range `cyclic` - ⊞ - Adapts the range of the Lookup Table (2nd input) for cyclic or non-cyclic input indices. When using a cyclic input index (1st input), the lookup value for index 0.0 and 1.0 result in the same value. To avoid this, set Cyclic Range to Yes and the lookup will cycle smoothly.
  * Automatic `auto` - Checks the right extend condition of each channel (Assumes type cycle and mirror are cyclic lookups).
  * Yes `yes` - For looking up a cyclic output (oscillator, beat driven output etc).
  * No `no` - For looking up a single wave (slider mapping, etc).

- Per Index Channel `chanmatch` - ⊞ - Determines how index channels are mapped to lookup Channel tables.
  * One Lookup Table Channel `onetoone` - The first index channel is matched to the full lookup table.
  * All Lookup Table Channels `onetomany` - Each index channel is matched with every lookup table.

- Match by `match` - ⊞ - Determines how index channels are matched with a lookup channel in 'One Lookup Table Channel' mode.
  * Channel Number `index` - An index channel is matched to a lookup table by its index within the clip. Lookup tables are cycled if there are few of them than index channels.
  * Channel Name `name` - An index channel is matched to a lookup table by name. Unmatched index channels are left "as is".

- Interpolate `interp` - When on, the input can be interpolated between samples. When off, the nearest sample is used.
- Extend Left `left` - ⊞ - The left extend conditions (before/after range) for the lookup output.
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

- Extend Right `right` - ⊞ - The right extend conditions (before/after range) for the lookup output.
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

- Default Value `defval` - The value used for the Default Value extend condition.

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
Extra Information for the Lookup CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
