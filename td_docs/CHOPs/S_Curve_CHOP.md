---
url: https://docs.derivative.ca/S_Curve_CHOP
category: CHOPs
title: S_Curve_CHOP
---

# S Curve CHOP
## Summary

This CHOP generates S curves.
[scurveCHOP_Class](https://docs.derivative.ca/ScurveCHOP_Class "ScurveCHOP Class")

## Parameters - S Curve Page
- Curve Type `type` - ⊞ - What Curve Type to Generate.
  * Half Cosine `halfcosine` -
  * Logistic `log` -
  * Arctangent `atan` -

- Length `length` - Set the number of samples for this CHOP.
- Prepend `prepend` - Add this number of samples to the beginning of the curve.
- Append `append` - Add this number of samples to the end of the curve.
- Steepness `steepness` - Controls the steepness of the S Curve.
- Linearize `linearize` - Control the amount of cruvature in the curve.
- Bias `bias` - Move the curve's bias backward or forward.
- From Range `fromrange` - ⊞ - Specify the low and high range of the input index.
  * `fromrange1` -
  * `fromrange2` -

- To Range `torange` - ⊞ - Specify the low and high range of the curve.
  * `torange1` -
  * `torange2` -

## Parameters - Channel Page
- Channel Names `channelname` - You can creates many channels with simple patterns like "`chan[1-20]`", which generates 20 channels from chan1 to chan20. See the section, Common CHOP Parameters for a description of this and all Options. See [Scope and Channel Name Matching](https://docs.derivative.ca/CHOP_Common_Page#Scope "CHOP Common Page") Options.
- Sample Rate `rate` - The sample rate of the channels, in samples per second. Default: `me.time.rate`
- Extend Left `left` - ⊞ - The left extend condition (before range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - The right extend conditions (after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Default Value `defval` - The value used for the Default Value extend condition.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the S Curve CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
