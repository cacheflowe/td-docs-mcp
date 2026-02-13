---
url: https://docs.derivative.ca/Switch_CHOP
category: CHOPs
title: Switch_CHOP
---

# Switch CHOP
## Summary

The Switch CHOP allows you to control the flow of channels through a CHOPnet. It selects one of the input CHOPs by index and copies it exactly. This is useful for selecting one of several "gestures" or actions. Only one input chop can be selected at a time.
Inputs are indexed starting at 0, so that the first input is 0, the second is 1, and so on.
If the First Input Is Index parameter is enabled, the first input is used as the "switch" and the remaining inputs will be selection choices. In this case, the second input will be indexed as 0, the third as 1, the fourth as 2, and so on (the Switch input chop is not indexed). The index value is determined by evaluating the first channel in the first input at the current frame. Only integer indices are used; fractional indices will be rounded down to the closest integer.
If the index is less than 0, then the index will be interpreted to be 0. If the index is greater than the number of input chops, the last input chop is selected.
If you wish to blend between inputs use the [Cross CHOP](https://docs.derivative.ca/Cross_CHOP "Cross CHOP") or the [Blend CHOP](https://docs.derivative.ca/Blend_CHOP "Blend CHOP").
[switchCHOP_Class](https://docs.derivative.ca/SwitchCHOP_Class "SwitchCHOP Class")

## Parameters - Switch Page
- First Input is Index `indexfirst` - If enabled, it will use the first input CHOP's first channel to determine which input to select.
- Index `index` - The input index to use if First Input Is Index is off.
- Extend `extend` - ⊞ - Choose extend behaviour when index is out of range. Allows negative indices.
  * Clamp `clamp` -
  * Loop `loop` -
  * ZigZag `zigzag` -

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
Extra Information for the Switch CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
