---
url: https://docs.derivative.ca/Pattern_CHOP
category: CHOPs
title: Pattern_CHOP
---

# Pattern CHOP
## Summary

The Pattern CHOP generates a sequence of samples in a channel. Unlike the [Wave CHOP](https://docs.derivative.ca/Wave_CHOP "Wave CHOP") its purpose is generating arrays of samples that have no reference to time (seconds or frames).
It is useful for curve generation like lookup tables, simple shapes that can be converted to SOPs, generating channels that are passed to the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") to generate instances, and other non-time-based curve-generation, with as little need to make expressions in Python.
All defaults are in samples, not seconds or frames (though like all CHOPs, it carries with it a sample rate). There is no start-end, just Length in samples.
**Tip** : To display a CHOP viewer in the units of samples, make the [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active") and change [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") -> Units to be Samples.
The Pattern CHOP optionally takes one input CHOP to match the length and sample rate, and, choosing via the Combine Channels menu, Appends or Inserts the new channel(s), Replaces the incoming channels, Adds to the incoming channels or Multiplies the incoming channels.
The Pattern CHOP defaults to one cycle of the curve over the length of the CHOP, no matter how many samples long.
**Tip: Customizing each channel:** The python object for the Pattern CHOP has a `chanIndex` member, so if Pattern generates three channels you can put something like `[1, 3, 7][me.chanIndex]` in any parameter to customize its value for each channel. For example, in the Type parameter, put the expression `['sin', 'cos', 'ramp'][me.chanIndex]` to get 3 different curve types.
[patternCHOP_Class](https://docs.derivative.ca/PatternCHOP_Class "PatternCHOP Class")

## Parameters - Pattern Page
- Type `wavetype` - ⊞ - The shape of one cycle of the pattern.
  * Constant `const` - (1)
  * Sine `sin` - (-1 to 1)
  * Cosine `cos` - (-1 to 1)
  * Triangle `tri` - (-1 to 1)
  * Ramp `ramp` - (0-1)
  * Ramp Samples `rampsamples` - (0 to numSamples-1)
  * Square `square` - (-1 to -1)
  * Pulse `pulse` - (0-1)
  * Random `random` - (0-1)
  * Random per Cycle `randomcycle` - All samples in a cycle will have the same randomly generated value.
  * Random Non-Repeating Integers `randomnonrepint` - This wave type is used in conjunction with the Randomize pulse. Between each Randomize pulse, the random values at each sample will be non-repeating. For example in the simplest case with a channel length of 1, each time Randomize is pulsed the random value of sample 1 after the pulse will be different than the random value before the pulse.
  * Step `step` - (0 to 1) step function
  * Cyclic Ramp `rampcyclic` - (0 to (numSamples -1) / numSamples). Same as 'Ramp' type, but on phase shifting the value never goes out of range.

- Length `length` - Set the number of samples for this CHOP.
- Number of Cycles `numcycles` - Set the number of repeating cycles of the Type shapes over the Length, except for Random.
- Step per Cycle `steppercycle` -
- Number of Steps `numsteps` -
- Bias `bias` - Makes Triangle type into a sawtooth wave, and sets the Square type variable-width.
- Seed `seed` - The seed for the random Types.
- Phase `phase` - Shifts the cycle.
- Phase Step per Channel `phasestep` - Increases the phase for each channel. A Phase Step of .25 when there are 2 channels will shift the second channel to be 1/4 cycle later phase than the first phase, where if the 2 channels are used for x and y, will draw a circle when passed to a CHOP to SOP.
- Taper `taper` - ⊞ - Two parameters to multiply by a line from `taper1` at the start to `taper2` at the end. The default of (`1 1`) has no effect.
  * `taper1` -
  * `taper2` -

- Taper Decay Rate `taperdecay` - An exponent that is applied to the result of the taper.
- Amplitude `amp` - See also the Range.
- Offset `offset` - See also the Range.
- From Range `fromrange` - ⊞ - A value at each From Range will become its corresponding To Range value.
  * `fromrange1` -
  * `fromrange2` -

- To Range `torange` - ⊞ - A value at each From Range will become its corresponding To Range value.
  * `torange1` -
  * `torange2` -

- Integer `integer` - ⊞ - A round-off menu to convert all numbers to integers.
  * Off `off` -
  * Ceiling `ceiling` -
  * Floor `floor` -
  * Round `round` -

- Reverse `reverse` - Reverses the final order of the samples as in the [Stretch CHOP](https://docs.derivative.ca/Stretch_CHOP "Stretch CHOP").
- Randomize `randomize` - When the Type parameter above is set to Random Non-Repeating Integers, this trigger will randomize all the values.

## Parameters - Channel Page
- Channel Names `channelname` - You can creates many channels with simple patterns like `chan[1-20]`, which generates 20 channels from `chan1` to `chan20`, or `t[xyz]` which generates `tx`, `ty` and `tz`. See the section, Common CHOP Parameters for a description of this and all Options. See [Scope and Channel Name Matching](https://docs.derivative.ca/CHOP_Common_Page#Scope "CHOP Common Page") Options.
- Combine Channels `combine` - ⊞ - If an input CHOP is attached, it adopts the length and sample rate of the input CHOP, and
  * Off `off` - It only adopts the length and sample rate of the input.
  * Append `append` - It appends the new Pattern CHOP channels after the last incoming channel.
  * Insert `insert` - It inserts the new channels before the first incoming channel.
  * Replace `replace` - It replaces the incoming channels using channel-name-matching.
  * Add `add` - It adds incoming channels to the generated channels, matching by channel-name-matching.
  * Multiply `multiply` - It multiplies incoming channels with the generated channels, matching by channel-name-matching.

- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left right extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - The right extend conditions (before/after range).
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
Extra Information for the Pattern CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
