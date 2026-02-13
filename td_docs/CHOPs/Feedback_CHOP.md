---
url: https://docs.derivative.ca/Feedback_CHOP
category: CHOPs
title: Feedback_CHOP
---

# Feedback CHOP
## Summary

The Feedback CHOP stores channels from the current frame to be used in a later frame, without forcing recooking back one frame. It allows you to get the state of a CHOP as it was one frame or time slice ago.
For example, if you need the position or speed of an object from a frame ago in order to compute its position, displacement or speed at the current frame, you would select a CHOP containing those values, and it will output it a frame or time slice later.
CHOPs like the [Lag CHOP](https://docs.derivative.ca/Lag_CHOP "Lag CHOP") and [Filter CHOP](https://docs.derivative.ca/Filter_CHOP "Filter CHOP") look back in time (iterate) internal to the CHOP, but sometimes the output of a chain of CHOPs is needed as the input of the same chain one frame later.
It allows connecting CHOPs in circular loops without **Infinite Recursion** errors. It simply copies its input without cooking it first.
[feedbackCHOP_Class](https://docs.derivative.ca/FeedbackCHOP_Class "FeedbackCHOP Class")

## Parameters - Feedback Page
- Output `output` - ⊞ - Choose what to output from this menu.
  * Previous Channels at Previous Time `previous` - Grabs the channels at prior time.
  * Previous Channels at Current Time `shift` - Grabs channels at current time.
  * Last Sample at Current Time `sample` - Uses the last sample received.

- Delta Time `delta` - Time differential during feedback. If on, it adds a 'dt' channel whose value is the elapsed time since the last cook.
- Reset `reset` - Activates feedback when set to 0. Disables feedback when set to 1. When disabled, the Feedback CHOP passes thru the data connected to its input.
- Reset Pulse `resetpulse` - Resets the feedback in a single frame when clicked.

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
Extra Information for the Feedback CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
