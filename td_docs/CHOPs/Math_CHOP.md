---
url: https://docs.derivative.ca/Math_CHOP
category: CHOPs
title: Math_CHOP
---

# Math CHOP
## Summary

The Math CHOP performs arithmetic operations on channels. The channels of a CHOP can be combined into one channel, and several CHOPs can be combined into one CHOP.
The OP page lets you pre-operate on each sample, like making all samples positive or taking the square of each sample.
Using **Combine Channels** , for an input CHOP with multi-channels, you can multiply the samples of one channel by the samples in the other channels, reducing N channels down to one. You can combine them by multiplying, adding, finding the maximum, etc..
Using **Combine CHOPs** , where there are two or more CHOP inputs, you can multiply (or add, etc.) the channels in one CHOP with the channels in all the other CHOPs, reducing N CHOPs to 1. (otherwise channels of multi-inputs are just merged)
You can then post-operate on the resulting samples - negate, square root, etc.
Then using the Mult-Add page it can offset and scale the values of each sample.
More conveniently you can use the Range page to do linear scaling as well by setting an output low-high range for a certain input low-high range.
Finally, you can round the resulting values off to an integer.
**Tip** : You can affect only certain channels of your input by using the Scope parameter on the Common page.
**Note** : To do logic operations (and, or, ...) between channels or CHOPs, use the [Logic CHOP](https://docs.derivative.ca/Logic_CHOP "Logic CHOP").
**Tip: Customizing each channel:** : You can use the local member `chanIndex` in a parameter like Post-Add, for example, `me.chanIndex*2` to give a different post-add value for each channel. `chanIndex` is available in numerous CHOPs like the [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP"). (expressions are non-optimized)
[mathCHOP_Class](https://docs.derivative.ca/MathCHOP_Class "MathCHOP Class")

## Parameters - OP Page
The four steps are performed in the following order:
- Channel Pre OP `preop` - ⊞ - Unary operations can be performed on individual channels. A menu of unary operations (as described above) that are performed on each channel as it comes in to the Math CHOP include:
  * Off `off` - Don't do anything to the channel.
  * Negate `negate` - Take the negative value of each sample of the channel.
  * Positive `pos` - Make negative values of the channel positive (absolute).
  * Root `root` - Take the square root of all values in the channel.
  * Square `square` - Square all the values in the channel.
  * Inverse `inverse` - Take the inverse (1/x) of all values in the channel.

- Combine Channels `chanop` - ⊞ - A choice of operations is performed between the channels of an input CHOP, for each input. The Nth sample of one channel is combined with the Nth sample of other channels:
  * Off `off` - Don't combine the channels.
  * Add `add` - Sum all the channels.
  * Subtract `sub` - Subtract all the channels from the first.
  * Multiply `mul` - Multiply all the channels.
  * Divide `div` - Divide the first channel by all the rest.
  * Average `avg` - Take the average of all the channels.
  * Minimum `min` - Take the minimum value of all the channels.
  * Maximum `max` - Take the maximum value of all the channels.
  * Length `len` - Assume the channels are a vector and compute its length.

- Combine CHOPs `chopop` - ⊞ - A menu of operations that is performed between the input CHOPs, combining several CHOPs into one.
  * Off `off` - Don't combine the channels.
  * Add `add` - Sum all the channels.
  * Subtract `sub` - Subtract all the channels from the first.
  * Multiply `mul` - Multiply of all the channels.
  * Divide `div` - Divide the first channel by all the rest.
  * Average `avg` - Take the average of all the channels.
  * Minimum `min` - Take the minimum value of all the channels.
  * Maximum `max` - Take the maximum value of all the channels.
  * Length `len` - Assume the channels are a vector and compute its length.

- Channel Post OP `postop` - ⊞ - A menu (same as Channel Pre OP) is performed as the finale stage upon the channels resulting from the above operations.
  * Off `off` -
  * Negate `negate` -
  * Positive `pos` -
  * Root `root` -
  * Square `square` -
  * Inverse `inverse` -

- Match by `match` - ⊞ - Match channels between inputs by name or index.
  * Channel Number `index` -
  * Channel Name `name` -

- Align `align` - ⊞ - This menu handles cases where multiple input CHOPs have different start or end times. All channels output from a CHOP share the same start/end interval, so the inputs must be treated with the Align Options:
  * Automatic `auto` - It will trim to the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") if there are any Time Slices, else it will do an Extend Min/Max.
  * Extend to Min/Max `none` - Find the earliest start and latest end, and extend all inputs to that range using the extend conditions. (see [Extend Conditions](https://docs.derivative.ca/Extend_Conditions "Extend Conditions")).
  * Stretch to Min/Max `stretch` - Find the earliest start and latest end, and stretch every channel's start and end to that range.
  * Shift to Minimum `start` - Find the earliest start and shift all channels so they all start at that index. All channels are extended to the length of the longest one.
  * Shift to Maximum `end` - Find the latest end and shift all channels so they all end at that index. Extend all channels to the length of the longest one.
  * Shift to First Interval `shift1` - Shift all channels to the start of the first CHOP and sample all inputs using the first input's range.
  * Trim to First Interval `trim1` - Trim all channels to first CHOP's range.
  * Stretch to First Interval `stretch1` - Stretch all channels to the first CHOP's range.
  * Trim to Smallest Interval `trim` - Trim all channels to the smallest start/end interval. The start and end values may not come from the same channel.
  * Stretch to Smallest Interval `squash` - Stretch all channels to the smallest start/end interval. The start and end values may not come from the same channel.

- Interp Pars per Sample `interppars` - Use this option when the input is a higher frequency than the timeline (example: audio). It will avoid any pops or crackles in the output when adjusting the multiply, add or range parameters.
- Integer `integer` - ⊞ - The resulting values can be converted to integer.
  * Off `off` - Don't affect the value.
  * Ceiling `ceiling` - Round a value up to the next integer.
  * Floor `floor` - Round a value down to the next integer.
  * Round `round` - Round a value to the nearest integer.

## Parameters - Mult-Add Page
The three steps are next performed in the following order:
- Pre-Add `preoff` - First, add the value to each sample of each channel.
- Multiply `gain` - Then multiply by this value.
- Post-Add `postoff` - Then add this value.

## Parameters - Range Page
This is the final step prior to output.
- From Range `fromrange` - ⊞ - Another way to multiply/add. Converts from one low-high range to another range.
  * `fromrange1` -
  * `fromrange2` -

- To Range `torange` - ⊞ - Another way to multiply/add. Converts from one low-high range to another range.
  * `torange1` -
  * `torange2` -

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
Extra Information for the Math CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
