---
url: https://docs.derivative.ca/Cycle_CHOP
category: CHOPs
title: Cycle_CHOP
---

# Cycle CHOP
## Summary

The Cycle CHOP creates cycles. It can repeat the channels any number of times before and after the original. It can also make a single cycle have a smooth transition from its end to its beginning, so it loops smoothly.
Since channels may not naturally loop well, the Cycle CHOP provides three different methods of blending between the cycles.
[cycleCHOP_Class](https://docs.derivative.ca/CycleCHOP_Class "CycleCHOP Class")

## Parameters - Cycle Page
- Cycles Before `before` - The number of cycles to loop before the input CHOP. This parameter can be fractional.
- Cycles After `after` - The number of cycles to loop after the input CHOP. This parameter can be fractional.
- Mirror Cycles `mirror` - If enabled, consecutive cycles are mirror images (reversed) of each another. The first cycle is never mirrored.
- Blend Start to End `extremes` - If on, the end of the CHOP is blended into the start of the CHOP to produce a smooth loop. If Cycles Before and Cycles After are 0, Region is non-zero, and Extend Conditions are "Cycle", it loops smoothly forever.

## Parameters - Blend Page
- Method `blendmethod` - ⊞ - How to blend between cycles:
  * Preserve Length `pre` - Keeps the total length of each cycle the same as the length of the input CHOP.
  * Overlap Sequences `ovl` - Overlaps each cycle with the previous cycle.
  * Insert Blend Region `ins` - Inserts a region between the cycles where blending is done.

- Shape `blendfunc` - ⊞ - The shape of the blending function:
  * Linear `lin` - Linear blend.
  * Ease in `ei` - Uses an easein() function for blending.
  * Ease out `eo` - Uses an easeout() function for blending.
  * Ease in Ease out `cos` - Uses both easein() and easeout() functions.
  * Cubic `cub` - For Insert Blend Region, uses a cubic() interpolation to fill the region between the cycles.
  * Add `add` - The overlapped regions have the overlapping samples simply added. This is suitable for looping audio.
  * Hold Previous `holdprev` -

- Region `blendregion` - The size of the blend region, in either seconds, samples or frames (set with Units in the Common page).
- Blend Region Units `blendregionunit` -
- Bias `blendbias` - The bias of the blend. A -1 biases the blend toward the beginning of the blend region, 0 is no bias and +1 biases towards the end of the blend region.
- Step `step` - If set to 1, the next cycle will be shifted up or down in value, so that it begins where the last cycle ended. Suitable for the root object of walk cycles.
- Step Scope `stepscope` - The names of those channels that will be affected by the Step parameter.

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
Extra Information for the Cycle CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
