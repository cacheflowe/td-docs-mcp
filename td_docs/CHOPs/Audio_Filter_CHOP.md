---
url: https://docs.derivative.ca/Audio_Filter_CHOP
category: CHOPs
title: Audio_Filter_CHOP
---

# Audio Filter CHOP
## Summary

The Audio Filter CHOP removes low frequencies, high frequencies, both low and high, or removes a mid-frequency range.
A Low pass filter removes the higher frequencies of a sound, while a high pass filter reduces the bass of the sound. A band pass filter is used to extract a frequency range (i.e. extracting a person's voice from background noise) and a band reject filter is used to cut out a frequency range.
If a certain frequency lies outside the pass band, sounds at that frequency will be reduced in magnitude. The farther outside the pass band the frequency is, the more it will be reduced.
The Cutoff frequency is also known as the "half-power" frequency. A wave at the cutoff frequency will be reduced to half power.
The Rolloff of a filter determines how quickly the drop occurs at its Cutoff frequencies. A low rolloff will produce a gradual filter falloff (more of the sounds outside the frequency range are heard), and a high rolloff will produce a sharp filter falloff.
Refer to [audio filter](http://en.wikipedia.org/wiki/Audio_filter) for more insight.
You can see the effects of the Audio Filter CHOP by passing it white noise from an Oscillator CHOP and sending the result to an Audio Spectrum CHOP. The Audio Filter CHOP is implemented with a 4-pole filter internally.
Moving the Dry / Wet parameter to Dry will bring back the incoming signal un-affected.
Input 2: See [ Cutoff Modulation Channels](#Cutoff_Modulation_Channels_Input)
See [Audio Para EQ CHOP](https://docs.derivative.ca/Audio_Para_EQ_CHOP "Audio Para EQ CHOP"), [Audio Band EQ CHOP](https://docs.derivative.ca/Audio_Band_EQ_CHOP "Audio Band EQ CHOP"), [Audio Spectrum CHOP](https://docs.derivative.ca/Audio_Spectrum_CHOP "Audio Spectrum CHOP"), [Audio Dynamics CHOP](https://docs.derivative.ca/Audio_Dynamics_CHOP "Audio Dynamics CHOP")
[audiofilterCHOP_Class](https://docs.derivative.ca/AudiofilterCHOP_Class "AudiofilterCHOP Class")

## Parameters - Filter Page
- Filter `filter` - ⊞ - The filter type:
  * Low Pass `lowpass` - All frequencies below the High Cutoff are passed through the filter (the "pass band").
  * High Pass `highpass` - All frequencies above the Low Cutoff are passed through.
  * Band Pass `bandpass` - All frequencies between the Low and High Cutoff are passed through.
  * Band Reject `bandreject` - All frequencies above the High Cutoff and below the Low Cutoff are passed though.

- Cutoff Units `units` - ⊞ - The filter cutoff frequency can be expressed in Hz (menu set to Frequency) or power-of-10 (menu set to Logarithmic). It enables one of the next 2 Filter Cutoff parameters.
  * Logarithmic `logarithmic` -
  * Frequency `frequency` -

- Filter Cutoff (Hz=10**val) `cutofflog` - The filter cutoff frequency expressed in power-of-10, where value 0 translates to 1 Hz (10**0), value 1 is 10 Hz (10**1), value 2 is 100 Hz (10**2), value 3 is 1000 Hz, value 4 is 10,000 Hz, value 4.5 is 31,623 Hz. The parameter in this form gives more meaningful range in relation to human hearing, as increasing the parameter by 1 raises the frequency by about 3 octaves.
- Filter Cutoff (Hz) `cutofffrequency` - The filter cutoff frequency expressed in Hz (cycles per second). This parameter set to 1000 has exactly the same effect as the above parameter set to 3.
- Filter Resonance `resonance` - Increasing the resonance will boost the loudness of the passed frequencies near the cutoff frequency.
- Roll-Off (dB per Octave) `rolloff` - Rolloff determines how much the levels decrease near the cutoff frequency. This parameter will make it decrease by 12 [decibels](http://en.wikipedia.org/wiki/Decibel) (dB) per octave, to, more extremely, 24 decibels per octave. 12 and 24 decibels correspond to levels of about 1/4 and 1/16.
- Dry / Wet Mix `drywet` - As this parameter is reduced from 1 (Wet) toward 0 (Dry), it removes the effect of the filter.

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

Cutoff Modulation Channels Input
The second input is the **Cutoff Modulation Channels** , which allows the filter parameters to be changed within the CHOP's time slice interval (typically 1/60 sec). This prevents audible stepping of the parameters that you are changing quickly.
You can send in a channel called `cutofffrequency` to override the value of the parameter. You would do this if you want to adjust the cutoff frequency very quickly. The parameter can only change as fast as the timeline rate, typically 1/60 seconds. Changed quickly, the stepping in frequency is noticeable. To improve on that, you would send a `cutofffrequency` channel in that is at a higher sample rate, like 400, which you can set in a CHOP like an LFO CHOP.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Audio Filter CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
