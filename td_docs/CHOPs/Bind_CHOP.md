---
url: https://docs.derivative.ca/Bind_CHOP
category: CHOPs
title: Bind_CHOP
---

# Bind CHOP
## Summary

Allows for [binding](https://docs.derivative.ca/Binding "Binding") of CHOP channels and parameters.
When a parameter is bound to a channel in the Bind CHOP (via the [parameter modes](https://docs.derivative.ca/Parameter_Mode "Parameter Mode") Export or Bind), any change in the channel will update the parameter value, and vice versa any change to the parameter will update the channel value.
Additionally, the Bind CHOP is a multi-input CHOP and will match input channels by Channel Number or Channel Name. It monitors the matched channels and updates the Bind CHOP's output channel to match whichever input changed most recently. When bound to a parameter (via Export mode or Bind mode) changes to any matched input or the bound parameter will update the channel's value.
A 'Callbacks DAT' is available for querying where the change was initiated and then taking further actions via python script.
This workflow is useful for binding multiple inputs to a parameter. For example, one input channel might be coming from a [MIDI](https://docs.derivative.ca/MIDI "MIDI") input device, and another channel coming from an [OSC](https://docs.derivative.ca/OSC "OSC") input device, and you want them both to control a given parameter. The Bind CHOP's output channel which is bound to the parameter will update to stay in sync with the most recent change from either of the inputs or the parameter. See video demonstration below.
##### Tutorial
Basic Bind CHOP setup: <https://youtu.be/bLi-xrCUt-c>
[bindCHOP_Class](https://docs.derivative.ca/BindCHOP_Class "BindCHOP Class")

## Parameters - Bind Page
- Match by `match` - ⊞ - Match channels between inputs by name or index.
  * Channel Number `index` -
  * Channel Name `name` -

- Channel Pickup `pickup` - When on a channel's value will not update until the changing input value crosses the current value.
- Callbacks DAT `callbacks` - When channel values change the callbacks DAT can be used to query where the change was initiated and then take further actions via python script.

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
Extra Information for the Bind CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
