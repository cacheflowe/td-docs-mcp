---
url: https://docs.derivative.ca/Speed_CHOP
category: CHOPs
title: Speed_CHOP
---

# Speed CHOP
## Summary

The Speed CHOP converts speed (units per second) to distance (units) over a time range. More generally, you give it a rate (the CHOP input) and it outputs a cumulative value. For example, the Speed CHOP converts rotation rate (rotations per second) into the number of rotation turns. ( Math-heads recognize this as an 'integral', which calculates the area under a curve. The curve is the incoming channel values over a time range, the output is the area.)
If you send a Constant CHOP channel that has value 1 into the Speed CHOP, then the Speed CHOP output will increase by 1 every second. If you feed it -2, it will decrease by 2 every second, and if you feed it 0, the output will not change. Use a Trail CHOP to see its results. You can reset the Speed CHOP to 0 by pressing the Reset parameter, or by sending in a channel (whose value is greater than 0) into the second input.
The first input contains the channels to be 'integrated'. By default, the Speed CHOP is time-sliced, so it keeps adding/subtracting to the output each frame it cooks. If you turn off its Time Slice parameter and send it a CHOP with a fixed frame range (like a default Noise CHOP), you can see the cumulative value starting from 0.
The output is calculated by adding the input's channel values for every sample, divided by the [samples per second](https://docs.derivative.ca/CHOP#Parts_of_a_CHOP "CHOP") of the Speed CHOP (typically 60), starting with the sample at the Start index. Negative input values reduce the output, positive values increase it. The cumulative values are put in the output channels.
When the CHOP is reset, its output can be set to any value via the Reset Value parameter.
When the second input is used to reset the output, where the second input is greater than 0, the area is reset and held to the reset value. For example, a [Wave CHOP](https://docs.derivative.ca/Wave_CHOP "Wave CHOP") (which is negative half the time) when passed into the second input causes the output to be reset for half a cycle.
See also: [Lookup CHOP](https://docs.derivative.ca/Lookup_CHOP "Lookup CHOP"), [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP"), [Count CHOP](https://docs.derivative.ca/Count_CHOP "Count CHOP"), [Event CHOP](https://docs.derivative.ca/Event_CHOP "Event CHOP")
[speedCHOP_Class](https://docs.derivative.ca/SpeedCHOP_Class "SpeedCHOP Class")

## Parameters - Speed Page
- Order `order` - ⊞ - Determines the order of the integral to use. If the input is a velocity, a First Order integral will return the position. If the input is an acceleration, a Second Order integral will return the position, and a First Order integral will return the velocity.
  * First `first` -
  * Second `second` -
  * Third `third` -

- Speed `speed` - Allows generating values when no inputs are connected. This parameter is disabled as soon as an input is connected to the Speed CHOP.
- First Constant `constant1` - Constant to add to the entire result after integrating once.
- Second Constant `constant2` - Constant to add to the entire result after integrating twice.
- Third Constant `constant3` - Constant to add to the entire result after integrating three times.
- Limit Type `limittype` - ⊞ - Select limit options such as loop, clamp, or zigzag from the menu. The value will remain in the range from Min to less than Max.
  * Off `off` - Do not limit the values.
  * Clamp `clamp` - Simply cut the channel value off if it is out of the Maximum/Minimum range, and replace it with the Maximum or Minimum limit value.
  * Loop `loop` - Continue the channel at the other end of the interval.
  * Zigzag `zigzag` - Mirror the values back inside the interval.

- Minimum `min` - The minimum value the output channel can have.
- Maximum `max` - The maximum value the output channel can have.
- Speed per Sample `speedsamples` - Applies the speed to each sample of the channel instead of across the whole channel. Useful for working with multi-sample channels.
- Reset Condition `resetcondition` - ⊞ - This menu determines how the Reset input triggers a reset of the channel(s).
  * Off to On `offtoon` - Channels are reset when the Reset input goes off to on.
  * While On `on` - Channels are reset when the Reset input goes on. The channel will hold the reset value until the input turns off.
  * On to Off `ontooff` - Channels are reset when the Reset input goes on to off.
  * While Off `off` - Channels are reset when the Reset input goes off. The channel will hold the reset value until the input turns on.

- Reset Value `resetvalue` - The channel(s) is set to this value when reset.
- Reset `reset` - ⊞ - While On, this toggle resets the channel(s) to the Reset Value.
  * Reset `reset` -
  * Reset Pulse `resetpulse` -

- Reset on Start `resetonstart` - While On, the Speed CHOP will reset each time the .toe file is restarted. If the Speed CHOP's value gets too large it can start stepping as when it reaches the limit of CHOP's number resolution. This is useful for projects that run for a long time, restarting the file will reset this value.
- Reset Pulse `resetpulse` - Click to instantly resets the channel(s) to the Reset Value.
- Reset On Start `resetonstart` - While On, the Speed CHOP will reset each time the .toe file is restarted. If the Speed CHOP's value gets too large it can start stepping as when it reaches the limit of CHOP's number resolution. This is useful for projects that run for a long time, restarting the file will reset this value.

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
Extra Information for the Speed CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
