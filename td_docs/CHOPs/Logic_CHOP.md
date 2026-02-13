---
url: https://docs.derivative.ca/Logic_CHOP
category: CHOPs
title: Logic_CHOP
---

# Logic CHOP
## Summary

The Logic CHOP first converts channels of all its input CHOPs into binary (0 = off, 1 = on) channels and then combines the channels using a variety of logic operations.
**NOTE:** The Logic CHOP is superceded by more convenient operators like the [CHOP Execute DAT](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT") or the [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT") which will run their scripts when CHOP channels change.
The Logic CHOP performs logic operations on the samples in CHOP channels. The channels of a CHOP can be combined into one channel, and several CHOPs can be combined into one CHOP.
With one input CHOP, you can invert the values of each sample. You can also do logic operations on the samples of one channel by the samples in the other channels, reducing N channels down to one. You can combine by applying an "or", "and", etc..
With two or more CHOP inputs, you can combine the channels in one CHOP with the channels in all the other CHOPs, reducing N CHOPs to 1.
To do math operations (add, multiply, ...) between channels or CHOPs, use the [Math CHOP](https://docs.derivative.ca/Math_CHOP "Math CHOP").
[logicCHOP_Class](https://docs.derivative.ca/LogicCHOP_Class "LogicCHOP Class")

## Parameters - Logic Page
- Convert Input `convert` - ⊞ - This menu determines the method to convert inputs to binary:
  * Off When Zero `nonzero` - Returns a logical 0 when channel value is zero;
Non zero values return 1.
  * Off When Zero Or Less `pos` - Returns a logical 0 when a channel value is zero or less; and 1 when values are positive.
  * Off When Outside Bounds `bound` - Returns 0 when channel value is outside the bounds set by the Bounds parameter below.
  * On When Value Changed `valchange` - Returns 1 when the channel value changes.
  * On When Channel Name Changed `namechange` - Returns 1 when the channel name changes.

[![TouchChannels92.gif](https://docs.derivative.ca/images/b/b8/TouchChannels92.gif)](https://docs.derivative.ca/File:TouchChannels92.gif)
- Channel Pre OP `preop` - ⊞ - Once converted by the Convert Input stage, Channel Pre OP defines a unary operation on each input sample:
  * Off `off` -
  * Invert `invert` - Changes 0 to 1; and 1 to 0.
  * Toggle `toggle` - Causes each 0 to 1 transition of the input channel to switch the current state between 0 and 1.
  * Radio Button `radio` - Only one channel per input can be on at once. If another channel turns on, the previously "on" channel is turned off.
  * Last Two On `radio2` - This is like Radio Button, but it keeps up to two channels on. If followed by a [Lag CHOP](https://docs.derivative.ca/Lag_CHOP "Lag CHOP"), it is useful for blending between pairs of poses.
  * Rising Edge `rise` - On for one sample only, at each place where a channel goes from off to on.
  * Falling Edge `fall` - On for one sample only, at each place where a a channel goes from on to off.

- Combine Channels `chanop` - ⊞ - Takes the first input and combines its channels, then the second input and combines its channels, and so on.
  * Off `off` -
  * And `and` -
  * Or `or` -
  * Exclusive Or `xor` -
  * Not And `nand` -
  * Not Or `nor` -
  * Equivalence `eqv` -
  * Lowest Index On `lowest` -
  * Highest Index On `highest` -

- Combine CHOPs `chopop` - ⊞ - Combine CHOPs combines the first channels of each CHOP, the second channels of each CHOP, etc.. Channels between inputs can be combined by number or name. Combining (Logic) Operations are:
  * Off `off` -
  * And `and` - On if all inputs are on, otherwise off.
  * Or `or` - On if at least one input is on, otherwise off.
  * Exclusive Or `xor` - On if one input on, but not more than one.
  * Not And `nand` - Off if all inputs are on, otherwise on.
  * Not Or `nor` - Off if at least one input is on, otherwise on.
  * Equivalence `eqv` - On if inputs are equal (all on or off), otherwise off.
  * Lowest Index On `lowest` - Gives the lowest index of the channel that is currently on,
or -1 if no channels are on.
  * Highest Index On `highest` - Gives the highest index of the channel that is currently on on,
or -1 if no channels are on.

[![TouchChannels93.gif](https://docs.derivative.ca/images/9/91/TouchChannels93.gif)](https://docs.derivative.ca/File:TouchChannels93.gif)
- Match by `match` - ⊞ - Channels are matched between inputs by Channel Name or Channel Number.
  * Channel Number `index` -
  * Channel Name `name` -

- Align `align` - ⊞ - Inputs that don't start at the same frame can be aligned. Se the section, Align Options.
  * Automatic `auto` -
  * Extend to Min/Max `none` -
  * Stretch to Min/Max `stretch` -
  * Shift to Minimum `start` -
  * Shift to Maximum `end` -
  * Shift to First Interval `shift1` -
  * Trim to First Interval `trim1` -
  * Stretch to First Interval `stretch1` -
  * Trim to Smallest Interval `trim` -
  * Stretch to Smallest Interval `squash` -

- Bounds `bound` - ⊞ - Set lower and upper bounds for when Convert Input is set to **Off When Outside Bounds**.
  * `boundmin` -
  * `boundmax` -

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
Extra Information for the Logic CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
