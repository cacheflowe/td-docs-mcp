---
url: https://docs.derivative.ca/Script_CHOP
category: CHOPs
title: Script_CHOP
---

# Script CHOP
## Summary

The Script CHOP runs a script each time the Script CHOP cooks. By default, the Script CHOP is created with a docked DAT that contains three Python methods: `cook`, `onPulse`, and `setupParameters`. The `cook` method is run each time the Script CHOP cooks. The `setupParameters` method is run whenever the Setup Parameter button on the Script page is pressed. The `onPulse` method is run whenever a custom pulse parameter is pushed.
Refer to Help -> Python Examples, and Help -> [Operator Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets").
Note: Because the Script CHOP can get data from anywhere, it's difficult to determine what it procedurally depends on. So every time that any Script OP runs it will make a list of operators, parameters, nodes etc that it depends upon, and when they change, the Script OP will re-cook.
The Script CHOP enables numPy arrays to be converted into the CHOP's channels. Also any CHOP can get its channels converted into numPy arrays. (May 2021) See `numPyArray()` in [CHOP Class](https://docs.derivative.ca/CHOP_Class "CHOP Class").
See also: [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Script TOP](https://docs.derivative.ca/Script_TOP "Script TOP")
[scriptCHOP_Class](https://docs.derivative.ca/ScriptCHOP_Class "ScriptCHOP Class")

## Parameters - Script Page
- Callbacks DAT `callbacks` - Specifies the DAT which holds the callbacks.
- Setup Parameters `setuppars` - Clicking the button runs the `setupParameters()` callback function.
- Modify Outside of Cook `modoutsidecook` - Allows CHOP to be updated by external script without having to lock the CHOP

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
Extra Information for the Script CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
