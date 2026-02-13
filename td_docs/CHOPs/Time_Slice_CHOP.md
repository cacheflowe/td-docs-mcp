---
url: https://docs.derivative.ca/Time_Slice_CHOP
category: CHOPs
title: Time_Slice_CHOP
---

# Time Slice CHOP
## Summary

The Time Slice CHOP outputs a time slice of samples. It is used to generate smooth in-betweens when TouchDesigner cannot cook/draw fast enough and keep up with the animation's frames per second. When you send it to a [Record CHOP](https://docs.derivative.ca/Record_CHOP "Record CHOP") or [Gesture CHOP](https://docs.derivative.ca/Gesture_CHOP "Gesture CHOP"), you will see the channels recorded and playing back more smoothly.
The number and names of channels does not change between input and output, but the output's frame range is a time slice: it goes from the previous frame that TouchDesigner cooked plus one, to the current frame.
For example, assume the TouchDesigner frames per second is four frames to remain realtime. Say the input to the Time Slice CHOP is a slider which only gets sampled when TouchDesigner draws. We will have slider values for frames 231 and 235, but there are no slider values for frames 232, 233 and 234, the current frame is 235, and the previous frame that TouchDesigner cooked and drew was frame 231. It had to skip.
When the Method is set to Linear in this example, the Time Slice CHOP will output a "time slice" which is a 4-sample CHOP for frames 232 to 235, and the values at frames 232 to 234 will be the values interpolated between the slider at frames 231 and 235.
Therefore any CHOPs after the Time Slice CHOP, like Gesture, Record or [Lag CHOP](https://docs.derivative.ca/Lag_CHOP "Lag CHOP") will get smooth data going into it, even though TouchDesigner isn't cooking every frame.
[timesliceCHOP_Class](https://docs.derivative.ca/TimesliceCHOP_Class "TimesliceCHOP Class")

## Parameters - Time Slice Page
- Method `method` - ⊞ - How to sample the input CHOP to create the output time slice. If the input CHOP is not time sliced and lies outside the current time slice region, its extend regions will be sampled.
  * Hold `hold` - Sample the input at the current time each cook to produce a constant valued time slice.
  * Linear `linear` - Sample the input at the current time each cook and interpolate from the last cook value to this current value.
  * Trim `trim` - Output the input, trimmed to the current time slice range.

- Quaternion Blend `quatrot` - Rotation channels blended using quaternions. Channels must be tagged as rotation channels (For example with the [Attribute CHOP](https://docs.derivative.ca/Attribute_CHOP "Attribute CHOP") or [Object CHOP](https://docs.derivative.ca/Object_CHOP "Object CHOP")).

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
Extra Information for the Time Slice CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
