---
url: https://docs.derivative.ca/Trail_CHOP
category: CHOPs
title: Trail_CHOP
---

# Trail CHOP
## Summary

The Trail CHOP displays a history of its input channels back in time. A window of time is displayed from the current frame back in time, the size of this window is set by the Window Length parameter. The last sample in the Trail CHOP is a sample of the input at the current frame.

**Note:** If the input channels change in number or names, the Trail CHOP clears its trails and begins anew. You can use a [Replace CHOP](https://docs.derivative.ca/Replace_CHOP "Replace CHOP") in this case to create stand in values.

[trailCHOP_Class](https://docs.derivative.ca/TrailCHOP_Class "TrailCHOP Class")

## Parameters - Trail Page
- Active `active` - When On the Trail CHOP will record its input.
- Grow Length `growlength` - When On the length of the Trail CHOP's recording will keep getting longer as the timeline moves forward. Use this for recording any length as needed.
- Window Length `wlength` - The amount of history recorded is set by Window Length. The Units menu on the right determine which units to use in the parameter (Samples, Frames, Seconds). A setting of 4 seconds will show the value of the input channel for the previous 4 seconds.
- Window Length Unit `wlengthunit` - Choose between using Samples, Frames, or Seconds as the units for the Window Length parameter.
- Capture `capture` - ⊞ - Determines when to capture values.
  * Time Slice `timeslice` - Captures a sliding window of the input every cook. Useful for capturing a continuous log.
  * Only When Input Cooks `inputcooks` - Captures the input only whenever the input cooks. Useful for capturing discrete events separated by long pauses.

- Resample `resample` - Enable parameter below to resample the output to a different length.
- Resample `samples` - Resample the output to this specified length.
- Rate `setrate` - Enable parameter below to use a different sample rate.
- Sample Rate `rate` - Resample using this sample rate instead of the global frame rate (`$FPS`).
- Reset `reset` - While On, this toggle resets the channel(s) to 0.
- Reset Pulse `resetpulse` - Click to instantly resets the channel(s) to 0.

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
  * Input 2:  -
  * Input 3:  -

## Info CHOP Channels
Extra Information for the Trail CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
