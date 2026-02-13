---
url: https://docs.derivative.ca/Blend_CHOP
category: CHOPs
title: Blend_CHOP
---

# Blend CHOP
## Summary

The Blend CHOP combines two or more CHOPs in input 2, 3 and so on, by using a set of blending channels in input 1. The blending channels cause different strengths of the CHOPs to contribute to the output of the CHOP. It works like the [Blend SOP](https://docs.derivative.ca/Blend_SOP "Blend SOP").
The first channel of input 2 is blended with the first channel of input 3 and input 4 and so on.
Input 1 acts as the control input, which contains the blend weight channels for the rest of the inputs. In it there is one channel for each of the blended CHOPs coming in on input 2, 3 and so on.
The first channel in input 1 is input 2's blend weight, the second channel in input 1 is the input 3's blend weight, and so on. There should be as many blend channels in input 1 as there are inputs, excluding input 1. (However when using Differencing and Omit First Weight Channel is on, the first channel if inout 1 ias assumed to be the weight of input 3, as input 2 is the "base" and doesn't need a weight.)
The interval of the output of the CHOP is the interval of input 1 (the blend channels).
If input 2 onwards are just poses, it's acceptable, as the CHOP blends between poses by using extend conditions.
**Note:** This CHOP is optimized and doesn't cook inputs that have zero weight.
[blendCHOP_Class](https://docs.derivative.ca/BlendCHOP_Class "BlendCHOP Class")

## Parameters - Blend Page
- Method `method` - ⊞ - The blend method:
  * Proportional `prop` - Each blend source contributes to the result according to its blend weight. If the blend weights do not add up to one, they are scaled so that they do.
  * Difference `dif` - In this default behavior of the Blend CHOP, the input 2 is always the "base". There are blend channels for all the other inputs, and when they are all zero, you get base. If any one blend channel is 1 and the others are zero, then your output is the same as the input that corresponds to that blend channel.
  * Quaternion (Commercial) `quaternion` - The first input is used to control the proportional blending of the second two inputs using quaternions. Blending rotation channels properly involves grouping the channels into quaternion groups with the Attribute CHOP before using this or similar quaternion options.
  * Additive `additive` - This method works the same as proportional except the blend weights are not normalized.

- Omit First Weight Channel `firstweight` - When using the Differencing method, the weight channel for the base input has no effect, so the channel is omitted if this option is On.
- Fix Underflows `underflow` - Replace denormalized (very small) numerical values with 0. These values can otherwise cause performance issues.

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
Extra Information for the Blend CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
