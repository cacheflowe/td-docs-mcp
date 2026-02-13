---
url: https://docs.derivative.ca/Interpolate_CHOP
category: CHOPs
title: Interpolate_CHOP
---

# Interpolate CHOP
## Summary

The Interpolate CHOP treats its multiple-inputs as keyframes and interpolates between them. The inputs are usually single-frame CHOP channels like those produced by a [Constant CHOP](https://docs.derivative.ca/Constant_CHOP "Constant CHOP"). The Interpolate CHOP first sorts the input CHOPs in time (without shifting them) and interpolates between them to fill the gaps.
The number of channels in the output is the same as the number of channels in the first input.
If a channel is missing in an input, and Match By is set to Channel Name, it is treated as if there is no keyframe at that frame for that channel, and the interpolation occurs between CHOPs before and after that frame.
[interpolateCHOP_Class](https://docs.derivative.ca/InterpolateCHOP_Class "InterpolateCHOP Class")

## Parameters - Interpolate Page
- Shape `blendfunc` - ⊞ - The shape of the interpolation curve:
  * Linear `lin` - A straight line.
  * Ease in `ei` - Exponential rise.
  * Ease out `eo` - Exponential fall.
  * Ease in Ease out `cos` - Half cosine blend.
  * Cubic `cub` - A cubic spline.
  * Add `add` - Overlapping parts, if any, are added.
  * Hold Previous `holdprev` -

- Overlap Priority `overlap` - ⊞ - If an input is not a single frame, and if there are overlaps in the input CHOPs, an option is used to resolve the conflict.
  * Average Overlaps `avg` - Combine the conflicting channels by averaging them.
  * First Segment has Priority `first` - Use the segment with the earliest start time.
  * Last Segment has Priority `last` - Use the segment with the latest start time.

- Match by `match` - ⊞ - Specify how to match the channels of each input.
  * Channel Number `index` - Ignore channel names, and simply pair them in order.
  * Channel Name `name` - Match channel inputs by name, regardless of their order.

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
Extra Information for the Interpolate CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
