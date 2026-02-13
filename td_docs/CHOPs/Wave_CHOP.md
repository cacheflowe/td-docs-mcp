---
url: https://docs.derivative.ca/Wave_CHOP
category: CHOPs
title: Wave_CHOP
---

# Wave CHOP
## Summary

The Wave CHOP makes repeating waves with a variety of shapes. It is by default 10-seconds of 1-second sine waves, a total of 600 frames. You can adjust period (frequency), phase, shape, amplitude and offset.
The Wave CHOP gives a set of waves in channels of a specifiable time-range. It is superceded by the [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP") which gives an endless stream of waves that is [Time Sliced](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)"), and the [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP") that has more control over shaping waveform samples (and is time-independent). The [Audio Oscillator CHOP](https://docs.derivative.ca/Audio_Oscillator_CHOP "Audio Oscillator CHOP") also creates waveforms that are continually repeated, but its defaults are for higher-frequency waves at higher (audio) sample rates.
Because the Extend Conditions of the Wave CHOP are set to Repeat, the wave will repeat outside the 10-second range.
Applied to the actual waveform can be an offset, decay and ramp.
Multiple channels can be generated in the Channel Name parameter using [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion"). A few examples of name pattern name expansion:
  * `tx ty tz`
  * `t[xyz]` - expands to `tx ty tz`
  * `chan[1-4]` - expands to `chan1 chan2 chan3 chan4`
  * `c[xyz][1-5:2]` - expands to `cx1 cx3 cx5 cy1 cy3 cy5 cz1 cz3 cz5`

See also: [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP"), [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP"), [Audio Oscillator CHOP](https://docs.derivative.ca/Audio_Oscillator_CHOP "Audio Oscillator CHOP").
[waveCHOP_Class](https://docs.derivative.ca/WaveCHOP_Class "WaveCHOP Class")

## Parameters - Wave Page
- Type `wavetype` - ⊞ - There is a choice of waveforms shapes:
  * Constant `const` - [![TouchChannels69.gif](https://docs.derivative.ca/images/6/6c/TouchChannels69.gif)](https://docs.derivative.ca/File:TouchChannels69.gif)(1) A constant-valued "wave".
  * Sine `sin` - [![TouchChannels71.gif](https://docs.derivative.ca/images/a/ad/TouchChannels71.gif)](https://docs.derivative.ca/File:TouchChannels71.gif)(-1 to 1) A Sine wave.
  * Gaussian `normal` - [![TouchChannels74.gif](https://docs.derivative.ca/images/2/2b/TouchChannels74.gif)](https://docs.derivative.ca/File:TouchChannels74.gif)(0 to 1) A Gaussian (also known as a bell or normal) curve.
  * Triangle `tri` - [![TouchChannels76.gif](https://docs.derivative.ca/images/c/c0/TouchChannels76.gif)](https://docs.derivative.ca/File:TouchChannels76.gif)(-1 to 1) A ramp-up to 1 and ramp-down to 0 that can be shaped with the Bias parameter.
  * Ramp `ramp` - [![TouchChannels78.gif](https://docs.derivative.ca/images/c/cd/TouchChannels78.gif)](https://docs.derivative.ca/File:TouchChannels78.gif)(0 to 1) A ramp from 0 to 1.
  * Square `square` - [![TouchChannels80.gif](https://docs.derivative.ca/images/3/33/TouchChannels80.gif)](https://docs.derivative.ca/File:TouchChannels80.gif)(-1 to 1) Step-up/step-down, with Bias control to make it rectangular.
  * Pulse `pulse` - [![TouchChannels82.gif](https://docs.derivative.ca/images/c/c4/TouchChannels82.gif)](https://docs.derivative.ca/File:TouchChannels82.gif)(0 to 1) Produces a 1 for one sample, 0 otherwise.
  * Expression `expr` - A user defined expression.

The Sine formula is:
```
out = Amplitude * (Offset + sin ((Period*index - Phase)*360))

```
- Period `period` - The period is the number of seconds, frames or samples that the waveform repeats in. It is expressed in the chop's Units (default is Seconds), found on the Common page.
- Period Unit `periodunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Phase `phase` - The phase shifts the waveform in time, and is expressed as a fraction of a period, usually between 0 and 1.
- Bias `bias` - You can vary the shape of some of the waveform types by changing the bias within the range -1 to +1.
- Offset `offset` - The waveform's value can be offset. A sine wave can remain always positive by setting Offset to 1.
- Amplitude `amp` - The wave's value can be scaled.
- Decay Rate `decay` - The wave's amplitude can be reduced over time with an "exponential decay". For example, if the Decay is 0.2 and the Units are seconds, then the amplitude will decay to 0.8 after 1 second, and 0.8 of 0.8 (or 0.64) after 2 seconds.
- Decay Rate Unit `decayunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Ramp Slope `ramp` - Then a ramp is added to the result with a slope of Ramp. The channel increases by the Ramp Slope value every Unit of time. For example, if Ramp is 1.2, the channel increases by 1.2 every second, in addition to the shape of the wave.
- Ramp Slope Unit `rampunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Expression `exprs` - If the waveform type is Expression, the Expression parameter is used to input a math expression. Some local variables are available: $I (Index), $L (the loop variable over the period 0 to 1), $C (the cycle variable, the integer number of cycles the waveform has passed at the current index).

## Parameters - Channel Page
- Channel Names `channelname` - You can creates many channels with simple patterns like "`chan[1-20]`", which generates 20 channels from chan1 to chan20. See the section, Common CHOP Parameters for a description of this and all Options. See [Scope and Channel Name Matching](https://docs.derivative.ca/CHOP_Common_Page#Scope "CHOP Common Page") Options.
- Start `start` - Start of the interval, expressed in Units (seconds, frames or samples).
- Start Unit `startunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- End `end` - End of the interval, expressed in Units (seconds, frames or samples).
- End Unit `endunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

- Extend Right `right` - ⊞ - The right extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

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

## Info CHOP Channels
Extra Information for the Wave CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
