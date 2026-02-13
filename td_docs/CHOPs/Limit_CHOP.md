---
url: https://docs.derivative.ca/Limit_CHOP
category: CHOPs
title: Limit_CHOP
---

# Limit CHOP
## Summary

The Limit CHOP can limit the values of the input channels to be between a minimum and maximum, and can quantize the input channels in time and/or value such that the value steps over time.
Limiting a channel causes all its values to lie within a range. Several different methods are for limiting are listed under the Type parameter description.
Quantizing a channel value snaps its values to the closest allowable value (the "quantized values"). Quantizing methods are: Floor, Ceiling, and Round.
Quantizing a channel index is like quantizing in time, and acts as a sample and hold mechanism. The channel is sampled at a quantized index, and held at that value until the next quantized index at which time the value takes on the input value at that point.
[limitCHOP_Class](https://docs.derivative.ca/LimitCHOP_Class "LimitCHOP Class")

## Parameters - Limit Page
- Type `type` - ⊞ - Select limit options such as loop, clamp, or zigzag from the menu. The value will remain in the range from Min to less than Max.
  * Off `off` - Do not limit the values.
  * Clamp `clamp` - Simply cut the channel value off if it is out of the Maximum/Minimum range, and replace it with the Maximum or Minimum limit value.
  * Loop `loop` - Continue the channel at the other end of the interval.
  * Zigzag `zigzag` - Mirror the values back inside the interval.

- Minimum `min` - The minimum value the output channel can have.
- Maximum `max` - The maximum value the output channel can have.
- Positive Only `positive` - Takes the absolute value of the channel, making all negative values positive.
- Normalize `norm` - Scale and offset the channel so that it lies between -1 and +1. The Normalize function does not work with [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing") on.
- Fix Underflows `underflow` - This will cause extremely tiny numbers to be rounded to 0.

## Parameters - Quantize Page
- Quantize Value `quantvalue` - ⊞ - Selects the quantization method to use:
  * Off `off` - No Value quantization is done.
  * Ceiling `ceiling` - The Ceiling function rounds a value to the closest quantized value above it.
  * Floor `floor` - The Floor quantization function rounds a value to the closest quantized value below it.
  * Round `round` - The Round function rounds a value to the nearest quantized value.

- Value Step `vstep` - The increment between quantized values.
- Value Offset `voffset` - The offset for quantized values, to allow steps to not lie at zero, the default.
- Quantize Index `quantindex` - ⊞ - Selects whether to quantize the index relative to the sample 0, or the start index of the CHOP.
  * Off `off` -
  * Offset Relative to Start `relstart` -
  * Offset Relative to Zero `relzero` -

- Step `istep` - The increment between quantized indices, in seconds, frames or samples.
- Step Unit `istepunit` -
- Offset `ioffset` - The offset for quantized indices.
- Offset Unit `ioffsetunit` -

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
Extra Information for the Limit CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
