---
url: https://docs.derivative.ca/Copy_CHOP
category: CHOPs
title: Copy_CHOP
---

# Copy CHOP
## Summary

The Copy CHOP produces multiple copies of the second input along the timeline of the first input. The first input provides the trigger signals or the convolve levels.
The Copy CHOP can be used to produce a motion every time a trigger occurs. It can be used to trigger motion, such as eyelid blinks. The copies it produces can be identical, or the copies can be re-cooked each time a copy is added to the timeline. It is useful for triggering a sound multiple times, where the sounds may overlap in time.
Each copy that is added to the output can be completely different than any other copy. By passing variables through the Variables page, the second (Copy) input can be any CHOP chain that uses the variables and recooks to create each copy.
[copyCHOP_Class](https://docs.derivative.ca/CopyCHOP_Class "CopyCHOP Class")

## Parameters - Copy Page
- Copy Method `method` - ⊞ - Select which copy method to use from the menu options below.
  * Triggered Copy `trigger` - The second input is copied at the first input's trigger points only. A trigger point occurs whenever the first input's channel crosses the Trigger Threshold value. Overlapping copies are added.
  * Convolve `convolve` - For every sample in the first input's channel, the second input is shifted to that point in time, scaled by the sample value, and added into the output channels.

- Output Method `output` - ⊞ - Select which output method to use from the menu options below.
  * One Channel per Template Channel `match` - Each output channel is a channel from the first input combined with the corresponding channel from the second input.
  * One Channel per Copy Channel `accum` - Each output channel is a channel from the second input, with copies triggered by every channel of the first input.

- Trigger Threshold `threshold` - The threshold value for triggering copies.
- Remainder `remainder` - ⊞ - See Remainder parameter below..
  * Discard Remainder `crop` -
  * Make Output Longer `extend` -
  * Mix Remainder with Beginning `mix` -

- Keep Non-Scoped Channels `keep` - If enabled, non-scoped channels are copied to the output, otherwise they are deleted.

## Parameters - Stamp Page
- Stamp Inputs `stamp` - Recook the second input for each triggered copy.
- Copy `copy` - Sequence of values available as stamps.
- Param `copy0param` - The parameters are re-calculated for each copy. Set the parameter name here and the value below. You can use CHOP Members and Methods. The parameters you set here are available to any CHOP in the network attached to the second input through the function:
```
fetchStamp(key, default)

```

Where `default` is any initial value for the parameter, and is usually set to 0.
- Value `copy0value` - Set the parameter's value to be copied.

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
Extra Information for the Copy CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
