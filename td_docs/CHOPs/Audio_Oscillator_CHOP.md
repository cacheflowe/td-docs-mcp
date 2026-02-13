---
url: https://docs.derivative.ca/Audio_Oscillator_CHOP
category: CHOPs
title: Audio_Oscillator_CHOP
---

# Audio Oscillator CHOP
## Summary

The Audio Oscillator CHOP generates sounds in three ways. It repeats common waveforms (sine, triangle), it generates white noise (a random number for each sample), or it repeats a prepared incoming audio clip of any duration. It outputs typically 44100 samples per second. In contrast, the [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP") by default generates waves at lower frequencies and lower sample rates (60 samples/second), however both Audio Oscillator and LFO are interchangeable by changing their frequencies and sample rates.
When it is synthesizing tones from the basic waveforms, the Audio Oscillator CHOP steps through the waveform at a rate that depends on the Pitch Control input. By default, a Pitch Control of 0 gives a middle A at 440 Hz; a 1 gives 880 Hz; a -1 gives 220 Hz. Steps of 1 in Pitch Control are 1 octave apart. Steps of 1/12 (.08333) are 1 semitone apart.
The Audio Oscillator is roughly modelled after the [APR 2600 voltage-controlled oscillator](https://www.google.com/search?q=ARP+2600+Oscillator+design&oq=ARP+2600+Oscillator+design) (VCO).
Up to three input CHOPs can be connected to the Audio Oscillator CHOP.
**Pitch Control** - The first (optional) input affects the pitch. Output channels are generated for each Pitch Control channel. When pitch control is 0, it outputs a wave at the base frequency (default 440 Hz at 44,100 samples per second). It is "logarithmic": By default, increasing the pitch control by 1 increases the pitch by 1 octave, by 2 it increases by 2 octaves (4 times the frequency).
**Reset Pulse** - The second (optional) input contains pulses that restart the oscillator from the beginning of the wave or the Playback Source. 0 in the input means "play the oscillator". 1 means "stop the oscillator and cue it at the start of the waveform or Playback Source".
**Playback Source** - The third (optional) input is a replacement of the waveform Type. It is a sound clip to play at a rate modified by the Pitch Control, and can contain any number of channels. These channels are generated for each Pitch Control channel. The waveform Type and the Base Frequency parameters are disabled.
If you plug any sound clip into the Audio Oscillator CHOP's Playback Source, and Pitch Control is a constant value of 0 of any duration, it will just repeat the Playback Source. If you feed a [Wave CHOP](https://docs.derivative.ca/Wave_CHOP "Wave CHOP") as its Pitch Control, it will raise and lower the speed/pitch of the input.
The Audio Oscillator CHOP can serve as a general motion time-warper and repeater. If you put motion channels into the third input, you can control the time warp by feeding different Pitch Control curves. 0 pitch is normal speed, 1 is double speed.
Unlike the Wave CHOP, this is an iterating CHOP, that is, it steps through the waveform while the pitch changes. To see this effect, feed an LFO CHOP into the Audio Oscillator. Unlike the LFO CHOP, the Audio Oscillator CHOP is designed for audio frequencies.
See also: [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP"), [Wave CHOP](https://docs.derivative.ca/Wave_CHOP "Wave CHOP").
[audiooscillatorCHOP_Class](https://docs.derivative.ca/AudiooscillatorCHOP_Class "AudiooscillatorCHOP Class")

## Parameters - Waveform Page
- Type `wavetype` - ⊞ - The shape of the waveform to repeat, unless overridden by the Playback Source:
  * Sine `sin` - (-1 to 1)
  * Gaussian `normal` - (0 to 1)
  * Triangle `tri` - (-1 to 1)
  * Ramp `ramp` - (0 to 1)
  * Square `square` - (-1 to 1)
  * Pulse `pulse` - (0 to 1)
  * White Noise `whitenoise` - Random samples between -1 and 1

- Base Frequency `frequency` - The cycles per second when the Pitch Control is zero.
- Units per Octave `octave` - Amount that the Pitch Control needs to increase by to raise the pitch by one octave. The default of 1 means that Pitch Control of 1 raises the pitch by 1 octave. Units per Octave of .08333 means that a Pitch Control of 3 raises the pitch by a factor of 3 x .08333 (three semitones). This is suitable for using MIDI note numbers as pitch control.
- Offset `offset` - Values output from the CHOP can have an offset added to them.
- Amplitude `amp` - Values output from the CHOP can be scaled.
- Bias `bias` - Shape control for Triangle, Gaussian and Square waves. For triangle waves, it moves the peak. For square waves, it alters the width of the peak. Zero means no bias.
- Phase `phase` - A value of .5 is a phase shift of 180 degrees, or one half cycle.
- Smooth Pitch Changes `smooth` - If the Pitch Control channel input to the Audio Oscillator CHOP is rising and is running at the Touch default of 60 frames per second, then the pitch will hold for 1/60 second before stepping up for another 1/60 second. This is an audible step. With this option On, the pitch rises for every audio sample, giving perfectly smooth glissando at extra compute cost.
- Reset Condition `resetcondition` - ⊞ - This menu determines how the Reset input triggers a reset of the channel(s).
  * Off to On `offtoon` - Channels are reset when the Reset input goes off to on.
  * While On `on` - Channels are reset when the Reset input goes on. The channel will hold the reset value until the input turns off.
  * On to Off `ontooff` - Channels are reset when the Reset input goes on to off.
  * While Off `off` - Channels are reset when the Reset input goes off. The channel will hold the reset value until the input turns on.

- Reset `reset` - This button resets the channel(s) to 0 when On.
- Reset Pulse `resetpulse` - Instantly resets the channel(s) to 0.

## Parameters - Channel Page
- Sample Rate `rate` - Set the sample rate of the CHOP in samples per second.

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
  * Input 1:  -
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Audio Oscillator CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
