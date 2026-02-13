---
url: https://docs.derivative.ca/Spring_CHOP
category: CHOPs
title: Spring_CHOP
---

# Spring CHOP
## Summary

The Spring CHOP creates vibrations influenced by the input channels, as if a mass was attached to a spring.
It acts as if, for every channel, there is a mass at the end of a spring, affected by a distance from the actual position (the output of the channel at the previous frame) to the desired position (the input channel at the current frame). When the distance (output - input) is zero, there is no force and therefore no movement.
Alternately, when Input Effect is force, the input is used as a force on the spring/mass, and the CHOP reacts to this force plus the force of the spring/mass. In this case, the mass would always stabilize at value 0 if the input is a force of 0.
The damping acts to make the spring system lose energy, so that higher damping makes everything come to rest sooner.
Its behavior is best understood by feeding it a chop that steps from one constant value to another in sequence, then playing with the constants.
[springCHOP_Class](https://docs.derivative.ca/SpringCHOP_Class "SpringCHOP Class")

## Parameters - Spring Page
- Spring Constant `springk` - The strength of the spring. Larger spring constants produce higher frequency oscillations.
- Mass `mass` - The mass of the object on the end of the spring. Higher masses will produce lower frequency oscillations, have higher amplitudes, and be more resistant to damping.
- Damping Constant `dampingk` - The amount of damping (resistance) applied to the spring action. Higher damping causes oscillations to die off more quickly.
- Input Effect `method` - ⊞ - Determines whether the input channel(s) represents a position or a force.
  * Position `disp` -
  * Force `force` -

- Intial Conditions from Channel `condfromchan` - If On, the initial position and velocity are calculated from the values at the beginning of the channel.
- Initial Position `initpos` - The initial position of the mass attached to the spring.
- Initial Speed `initspeed` - The initial velocity of the mass attached to the spring.
- Intial Conditions from Channel `condfromchan` - If On, the initial position and velocity are calculated from the values at the beginning of the channel.
- Reset `reset` - While On resets the spring effect of the CHOP.
- Reset Pulse `resetpulse` - Instantly reset the spring effect.

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
Extra Information for the Spring CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
