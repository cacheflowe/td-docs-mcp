---
url: https://docs.derivative.ca/Lag_CHOP
category: CHOPs
title: Lag_CHOP
---

# Lag CHOP
## Summary

The Lag CHOP adds lag and overshoot to channels. It can also limit the velocity and acceleration of channels. Lag slows down rapid changes in the input channels. Overshoot amplifies the changes in the input channels.
Two values exist for each parameter. For example, in the Lag effect, when the input channel value is rising, the first lag parameter is used, and when the channel value is decreasing, the second lag parameter is used. This can give a quick rise, and a slow fall. But lag up and down are often kept at the same value.
For a similar, less-abrupt effect, see the [Filter CHOP](https://docs.derivative.ca/Filter_CHOP "Filter CHOP").
[lagCHOP_Class](https://docs.derivative.ca/LagCHOP_Class "LagCHOP Class")

## Parameters - Lag Page
- Method `lagmethod` - ⊞ - The method by which lag is applied to the channels.
  * Lag Value `value` - Up is defined as an increase in values of the input channels, and down is a decrease in values of the inputs.
  * Lag Amplitude `amp` - Up is defined as an increase in amplitude (moving away from zero) and down is defined as a decrease in amplitude (moving towards zero) of each input channel.
  * Lag Magnitude `mag` - All the input channels are treated as components of one vector, and each operation is applied to the vector as a whole. Only the first parameter in Lag, Overshoot, Clamp Slope and Clamp Acceleration applies in this mode.
  * Quaternion Rotation (Commercial) `rotation` - Allows the lag to work with quaternion rotations.

- Lag `lag` - ⊞ - Applies a lag to a channel. The first value is for lagging up, and the second is for lagging down. It is approximately the time that the output follows 90% of a change to the input.
  * `lag1` - Lagging up value.
  * `lag2` - Lagging down value.

- Lag Unit `lagunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Overshoot `overshoot` - ⊞ - Applies overshoot to a channel. The first value is for overshoot while moving up, and the second is for overshoot while moving down.
  * `overshoot1` -
  * `overshoot2` -

- Overshoot Unit `overshootunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Clamp Slope `clamp` - Clamps the slope (or velocity) to lie between the values listed in Max Slope below. Slope is expressed as value/Units.
- Max Slope `slope` - ⊞ - The first value limits the slope when it is rising, and the second value limits the slope when it is decreasing.
  * `slope1` -
  * `slope2` -

- Clamp Acceleration `aclamp` - Clamps the acceleration to lie between the values listed in Max Acceleration below. Acceleration is expressed as value/(Units*2) .
- Max Acceleration `accel` - ⊞ - The first value limits the acceleration when it is rising, and the second value limits the acceleration when it is decreasing.
  * `accel1` -
  * `accel2` -

- Lag per Sample `lagsamples` - Applies the lag to each sample of the channel instead of across the whole channel. Useful for working with multi-sample channels.
- Snap `snap` - When On, if the difference between the output lag value and the input CHOP's value is within the specified threshold, the output value gets snapped to be equal to the input value.
- Threshold `threshold` - The threshold value for snapping the output to the input.
- Reset `reset` - When On resets (bypasses) the lag effect.
- Reset Pulse `resetpulse` - Instantly resets the lag effect.

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
Extra Information for the Lag CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
