---
url: https://docs.derivative.ca/Warp_CHOP
category: CHOPs
title: Warp_CHOP
---

# Warp CHOP
## Summary

The Warp CHOP time-warps the channels of the first input (the Pre-Warp Channels) using one warping channel in the second input (the Warp Curve). The Warp Curve acts as either a rate control or an index control, as explained below. The Warp CHOP usually works on non-time-sliced channels, like pre-key-framed channels of motion. See also the [Lookup CHOP](https://docs.derivative.ca/Lookup_CHOP "Lookup CHOP"), the [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP") and the [Audio Oscillator CHOP](https://docs.derivative.ca/Audio_Oscillator_CHOP "Audio Oscillator CHOP").
In the Rate Control Method, feeding the Warp CHOP a Warp Curve with a constant value of 1 makes the output identical to the Pre-Warp Channels, assuming the two inputs have the same start-end interval. That is, where the rate is 1, the Pre-Warp Channels are not warped.
Where the Warp Curve is above 1, it causes a speed-up in the animation. Where the Warp Curve is below 1, it causes a slow-down in the animation. Rates less than 0 cause the animation to go in reverse.
In the Index Control Method, the Warp Curve acts as an index into the first input. If the Warp Curve is a straight ramp with a slope of 1 (in Units), it produces unwarped output channels. If Units is set to Seconds, a Warp Curve value of 0 gets the Pre-Warp Channels' values at time 0 seconds. A Warp Curve value of 2 gets the Pre-Warp Channels' values at time 2 seconds.
The Warp CHOP will output the same number of channels and channel names as the Pre-Warp Channels input, and the sample rate will be the same as that of the Pre-Warp input. However, the CHOP will output the same start-end time interval as the Warp Curve input.
If you take a Warp Curve and pass it directly to a Warp CHOP with the Rate Control Method, it is equivalent to passing the same curve to an Speed CHOP and then passing it to the Warp CHOP with the Index Control Method.
[warpCHOP_Class](https://docs.derivative.ca/WarpCHOP_Class "WarpCHOP Class")

## Parameters - Warp Page
- Method `method` - ⊞ - The warping method to use: Rate or Index Control.
  * Rate Control `rate` -
  * Index Control `index` -

- Stretch Indices to Channel Length `scaleindex` - If on, the minimum and maximum values in the Warp Curve are mapped to the beginning and end of the channels to be warped. Otherwise, the Warp Curve is applied as-is to the Pre-Warp Channels.
The Warp CHOP does linear interpolation of the Pre-Warped Channels when they are both stretched and compressed.

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
Extra Information for the Warp CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
