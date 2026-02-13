---
url: https://docs.derivative.ca/Join_CHOP
category: CHOPs
title: Join_CHOP
---

# Join CHOP
## Summary

The Join CHOP takes all its inputs and appends one CHOP after another. It is expected they all have the same channels.
The end section of the first CHOP is overlapped with the start section of the second CHOP, and so on for the rest of the input CHOPs. The second input is shifted to line up with the end of the first.
Blending allows you to splice channels together by slowly phasing out one CHOP while phasing into the next, or by inserting interpolation curves between the channels of the adjacent CHOPs.
Quaternion Blend blends rotation triplets (rx ry rz) together using the shortest rotation arc. Rotation triplets are identified by "quaternion" attributes, which are set in the [Attribute CHOP](https://docs.derivative.ca/Attribute_CHOP "Attribute CHOP").
Translation Blending blends translation channels together by slowly changing from the final velocity of the previous channel to the initial velocity of the next. The next channel may be shifted up or down. If this is undesirable, use cubic blending instead (in the Shape menu). Translation Blending is done on channel triplets that represent translations or positions (*tx *ty *tz).
[joinCHOP_Class](https://docs.derivative.ca/JoinCHOP_Class "JoinCHOP Class")

## Parameters - Blend Page
- Method `blendmethod` - ⊞ - The blend method to produce a seamless sequence:
  * Preserve Length `pre` - The total length of the CHOPs is constant.
  * Overlap Sequences `ovl` - Overlaps the current CHOP with the prior CHOP. Better for audio.
  * Insert Blend Region `ins` - Inserts a region between the CHOPs where the blending is done.

- Shape `blendfunc` - ⊞ - The blend interpolation shape to use. See Shape in the [Cycle CHOP](https://docs.derivative.ca/Cycle_CHOP "Cycle CHOP").
  * Linear `lin` -
  * Ease in `ei` -
  * Ease out `eo` -
  * Ease in Ease out `cos` -
  * Cubic `cub` -
  * Add `add` -
  * Hold Previous `holdprev` -

- First Input Specifies Blend Regions `blendbyinput` - When this is checked on, the first input can be a multi-channel input which specifies blend regions for the remaining inputs into the Join CHOP. Channel 1 of input0 is used to blend between input1 & input2, channel 2 between input2 & input3, and so on. If not enough channels are specified, the last channel is repeated.
- Region `blendregion` - The size of the blend region.
- Blend Region Unit `blendregionunit` -
- Bias `blendbias` - Which segment to favour when blending: the previous (-1), the next (+1) or neither (0).
- Match by `match` - ⊞ - Match channels between inputs by index or by name.
  * Channel Number `index` -
  * Channel Name `name` -

## Parameters - Scope Page
- Step `step` - If set to 1, the next segment will be shifted up or down so that it begins where the last segment ended.
- Step Scope `stepscope` - The names of channels that use Step.
- Blend Scope `blendscope` - The names of the channels that should be blended. Other channels will not be blended.
- Translate X Blend `transscopex` - The names of channels that will be translation-blended. Each string field contains a list of its component channels, such as *tx, *ty and *tz.
- Translate Y Blend `transscopey` - The names of channels that will be translation-blended. Each string field contains a list of its component channels, such as *tx, *ty and *tz.
- Translate Z Blend `transscopez` - The names of channels that will be translation-blended. Each string field contains a list of its component channels, such as *tx, *ty and *tz.

## Parameters - Rotate Page
- Quaternion Blend `quatrot` - Use quaternion blending on rotation channels.
- Shortest Path Rotation Blending `shortrot` - If enabled, compensates.
- Rotation Scope `rotscope` - Enabled when Shortest Path Rotation Blending is turned on.
- Cycle Length `cyclelen` - Enabled when Shortest Path Rotation Blending is turned on.

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
Extra Information for the Join CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
