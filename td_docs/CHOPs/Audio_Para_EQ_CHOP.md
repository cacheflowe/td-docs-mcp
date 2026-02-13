---
url: https://docs.derivative.ca/Audio_Para_EQ_CHOP
category: CHOPs
title: Audio_Para_EQ_CHOP
---

# Audio Para EQ CHOP
## Summary

The Audio Para EQ CHOP (parametric [equalizer](http://en.wikipedia.org/wiki/Equalization_\(audio\))) applies up to 3 parametric filters to the incoming sound. The three filters are in series, where internally, the second filter takes its input from the output of the first filter, and so on.
It is called parametric because each filter has 3 controls - center frequency, bandwidth and boost, which in the old days, was more than usual analog filters.
Each filter has a center frequency (the Frequency parameter) where the filter will have the most effect, and a bandwidth which is roughly expressed in octaves, and is typically 3 or 4. The Boost parameter, when it is greater than 0, will make louder the audio around the center frequency. When boost is less than 0, it will make the audio quieter around the center frequency. Boost is in decibels (dB) where 0 dB has no effect.
You can best hear the effects of the Audio Para EQ CHOP by passing it rich-spectrum music. The Audio Para EQ CHOP is implemented with three 4-pole filters internally.
Input 2-4: See [Frequency Modulation Channels](#Frequency_Modulation_Channels_Input), and the Scope parameter.
The Audio Para EQ CHOP is implemented as three 4-pole filters in series.
See [Audio Filter CHOP](https://docs.derivative.ca/Audio_Filter_CHOP "Audio Filter CHOP"), [Audio Band EQ CHOP](https://docs.derivative.ca/Audio_Band_EQ_CHOP "Audio Band EQ CHOP"), [Audio Spectrum CHOP](https://docs.derivative.ca/Audio_Spectrum_CHOP "Audio Spectrum CHOP"), [Audio Dynamics CHOP](https://docs.derivative.ca/Audio_Dynamics_CHOP "Audio Dynamics CHOP")
[audioparaeqCHOP_Class](https://docs.derivative.ca/AudioparaeqCHOP_Class "AudioparaeqCHOP Class")

## Parameters - Parametric EQ Page
- Frequency Units `units` - ⊞ - How frequency is expressed:
  * Logarithmic `logarithmic` - The filter cutoff frequency can be expressed as a power-of-10. See Frequency (Hz = 10**val) below.
  * Frequency `frequency` - The filter cutoff frequency can be expressed in Hz.

- Enable EQ1 `enableeq1` - When off, it passes the sound through the first equalizer unchanged.
- Boost (dB) EQ1 `boost1` - When boost is greater than 0, it will make louder the audio around the center frequency. When boost is less than 0, it will make the audio quieter around the center frequency. Boost is in decibels (dB) where 0 dB has no effect.
- Frequency (Hz=10**val) EQ1 `frequencylog1` - The frequency is expressed in power-of-10, where value 0 translates to 1 Hz (10**0), value 1 is 10 Hz (10**1), value 2 is 100 Hz (10**2), value 3 is 1000 Hz, value 4 is 10,000 Hz, value 4.5 is 31,623 Hz. The parameter in this form gives more meaningful range in relation to human hearing, as increasing the parameter by 1 raises the frequency by about 3 octaves.
- Frequency (Hz) EQ1 `frequencyhz1` - The filter frequency is expressed in Hz (cycles per second). This parameter set to 1000 has exactly the same effect as the above parameter set to 3.
- Bandwidth EQ1 `bandwidth1` - Bandwidth determines how much the levels decrease near the center frequency, expressed in octaves.
- Enable EQ2 `enableeq2` - When off, it passes the sound through the second equalizer unchanged.
- Boost (dB) EQ2 `boost2` - When boost is greater than 0, it will make louder the audio around the center frequency. When boost is less than 0, it will make the audio quieter around the center frequency. Boost is in decibels (dB) where 0 dB has no effect.
- Frequency (Hz=10**val) EQ2 `frequencylog2` - The frequency is expressed in power-of-10, where value 0 translates to 1 Hz (10**0), value 1 is 10 Hz (10**1), value 2 is 100 Hz (10**2), value 3 is 1000 Hz, value 4 is 10,000 Hz, value 4.5 is 31,623 Hz. The parameter in this form gives more meaningful range in relation to human hearing, as increasing the parameter by 1 raises the frequency by about 3 octaves.
- Frequency (Hz) EQ2 `frequencyhz2` - The filter frequency is expressed in Hz (cycles per second). This parameter set to 1000 has exactly the same effect as the above parameter set to 3.
- Bandwidth EQ2 `bandwidth2` - Bandwidth determines how much the levels decrease near the center frequency, expressed in octaves.
- Enable EQ3 `enableeq3` - When off, it passes the sound through the third equalizer unchanged.
- Boost (dB) EQ3 `boost3` - When boost is greater than 0, it will make louder the audio around the center frequency. When boost is less than 0, it will make the audio quieter around the center frequency. Boost is in decibels (dB) where 0 dB has no effect.
- Frequency (Hz=10**val) EQ3 `frequencylog3` - The frequency is expressed in power-of-10, where value 0 translates to 1 Hz (10**0), value 1 is 10 Hz (10**1), value 2 is 100 Hz (10**2), value 3 is 1000 Hz, value 4 is 10,000 Hz, value 4.5 is 31,623 Hz. The parameter in this form gives more meaningful range in relation to human hearing, as increasing the parameter by 1 raises the frequency by about 3 octaves.
- Frequency (Hz) EQ3 `frequencyhz3` - The filter frequency is expressed in Hz (cycles per second). This parameter set to 1000 has exactly the same effect as the above parameter set to 3.
- Bandwidth EQ3 `bandwidth3` - Bandwidth determines how much the levels decrease near the center frequency, expressed in octaves.
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

Frequency Modulation Channels Input
The second input is the **Frequency Modulation Channels** , which allows the filter parameters to be changed within the CHOP's time slice interval (typically 1/60 sec). This prevents audible stepping of the parameters that you are changing quickly.
You can send in a channel called `frequency` to override the value of the parameter. You would do this if you want to adjust the center frequency very quickly. The parameter can only change as fast as the timeline rate, typically 1/60 seconds. Changed quickly, the stepping in frequency is noticable. To improve on that, you would send a `frequency` channel in that is at a higher sample rate, like 400, which you can set in a CHOP like an LFO CHOP.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -
  * Input 2:  -
  * Input 3:  -

## Info CHOP Channels
Extra Information for the Audio Para EQ CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
