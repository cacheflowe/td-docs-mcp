---
url: https://docs.derivative.ca/Slope_CHOP
category: CHOPs
title: Slope_CHOP
---

# Slope CHOP
## Summary

The Slope CHOP calculates the slope (or "derivative" in math-speak) of the input channels.
If the input CHOP represents position, the slope can be interpreted as speed. By default, the Slope CHOP converts position to speed.
In mathematical terms, the slope is the first derivative of the channel curve. The second and third derivatives can also be calculated. The second derivative can be interpreted as acceleration (and the third derivative could be interpreted as the rate of change in acceleration).
This CHOP can be used in conjunction with the [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP") to manipulate speed or acceleration directly. You can calculate the speed or acceleration of a moving object with a Slope CHOP and manipulate it with other CHOPs. Then you can convert the new speed or acceleration curve back to position data with a Speed CHOP. You may need to adjust the starting position, since the Slope CHOP removes this information. This can be done with the use of the Constant parameters in the Speed CHOP.
The Units option causes the output to be expressed as a change in value per sample, value per frame, or value per second.
[slopeCHOP_Class](https://docs.derivative.ca/SlopeCHOP_Class "SlopeCHOP Class")

## Parameters - Slope Page
- Type `type` - ⊞ - The type of slope to calculate.
  * Slope `slope` - Calculates the slope of the channels.
  * Acceleration `accel` - Calculates the acceleration of the channels.
  * Acceleration Of Slope `slacc` - Calculates the acceleration of the slopes of the channels.

- Method `method` - ⊞ - The sample pairs used to calculate the slope.
  * Use Previous And Current Sample `pc` - The current sample and the sample before it are used. This is the only method applicable in realtime applications.
  * Use Current And Next Sample `cn` - The current and the next samples are used.
  * Use Previous And Next Sample `pn` - The previous and the next samples are used, producing slightly more continuous slopes than the other methods.

The slope at a sample is calculated by looking at the values of samples just before, at, and after it.
For the Slope Type, it needs two values, and the options are given to use three combinations, the default being to use the value at the sample and the one before. (before - current) is divided by the time between the samples (determined by the sampling rate). The slope placed in the channel is expressed in the Units of the CHOP.
For the type Acceleration, it uses three consecutive samples around the sample it is computing. The most accurate acceleration is obtained with Use Previous and Next Sample.
- Slope per Sample `slopesamples` - Applies the slope to each sample of the channel instead of across the whole channel. Useful for working with multi-sample channels.

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
Extra Information for the Slope CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
