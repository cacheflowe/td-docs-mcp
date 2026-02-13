---
url: https://docs.derivative.ca/Audio_Spectrum_CHOP
category: CHOPs
title: Audio_Spectrum_CHOP
---

# Audio Spectrum CHOP
## Summary

The Audio Spectrum CHOP calculates and displays the frequency spectrum of the input channels.
In the default Visualization Mode the CHOP is set to display the spectrum in a more understandable way by emphasizing the higher frequency levels and the lower frequency ranges.
In another Mode, the Time to Magnitude and Phase mode, the audio can be converted to the frequency spectrum domain, manipulated and then converted back to get a filtered audio signal. When converting a signal to its spectrum, two channels are created from the one containing the audio signal. One channel contains the magnitude of the frequency components, and the other contains the phase. The channels are named, for example `chan1_m` and `chan1_p` where `_m` and `_p` are the suffixes for the magnitude and phase channels.
**Tip** : You can reduce cook time if you decrease the FFT Size from its default 8192 samples. The fastest form of this CHOP is by setting the Output Length parameter to "Output Length Manually". For example set the output buffer size to 2048 samples and the FFT Size to 2048. Each time it cooks, the CHOP is looking at the latest 2028 samples (at 44.1 KHz that amounts to the 50 msec, or 3 frames), which is plenty. Note the default form of the CHOP gives you 22,000 samples: 1 Hz to 22,050 Hz in steps of 1 Hz (when set to Frequency vs Logarithmic scaling), designed for clear interpretation: sample 1000 is the level of audio at 1000 Hz.
**Tip** : To find the exact frequency of a wave entering the Audio Spectrum CHOP, look at the Info pop-up for that node (MMB on the node). It says: Set "Frequency <-> Logarithmic Scaling" to 0, then multiply any sample to xxxx to get the Frequency at that sample. xxxx depends on the sample rates etc and isn't a constant.
See [Audio Filter CHOP](https://docs.derivative.ca/Audio_Filter_CHOP "Audio Filter CHOP"), [Audio Para EQ CHOP](https://docs.derivative.ca/Audio_Para_EQ_CHOP "Audio Para EQ CHOP"), [Audio Band EQ CHOP](https://docs.derivative.ca/Audio_Band_EQ_CHOP "Audio Band EQ CHOP"), [Audio Oscillator CHOP](https://docs.derivative.ca/Audio_Oscillator_CHOP "Audio Oscillator CHOP") set to White Noise.
[audiospectrumCHOP_Class](https://docs.derivative.ca/AudiospectrumCHOP_Class "AudiospectrumCHOP Class")

## Parameters - Spectrum Page
- Mode `mode` - ⊞ - Select which mode to use, modes described below.
  * Visualization `visual` - Show the spectrum in a way that more useful, with (by default) high frequencies boosted in level, and lower frequencies boosted in horizontal range.
  * Time to Magnitude and Phase `timetoraw` - Calculate the frequency spectrum assuming input is a signal.
  * Magnitude and Phase to Time `rawtotime` - Reconstructs a signal assuming input is a frequency spectrum similar to that coming from and Audio Spectum CHOP set to the above option.

- FFT Size `fftsize` - ⊞ - Converting to frequency needs a power-of-2 number of samples, like 512, 1024, 2048. (FFT means Fast [Fourier](http://en.wikipedia.org/wiki/Joseph_Fourier) Transform.) The more samples, the more accurate the spectrum but the more it doesn't represent the most recent sound. Whatever the size, the CHOP uses the most recent samples. Knowing that audio at 44100 samples per second with a timeline frame rate of 60 frames per second gives 735 samples per frame, if the CHOP cooks 1 frame later and the FFT size is 1024, then it will re-use 1024-735 = 289 samples, which is good as there's a little overlap. However if it cooks 2 frames later, it will miss using 446 frames since it will have advanced 735*2=1470 samples and it will only use 1024 of them.
  * 64 `64` -
  * 128 `128` -
  * 256 `256` -
  * 512 `512` -
  * 1024 `1024` -
  * 2048 `2048` -
  * 4096 `4096` -
  * 8192 `8192` -
  * 16384 `16384` -

- Frequency <-> Logarithmic Scaling `frequencylog` - Logarithmic (=1) is more tangible for human hearing. Each octave is represented with the same number of samples, so low frequencies are more readable. Frequency (=0) shows one sample for a fixed number of Hz, which is what the raw FFT gives, but most of the upper samples are uninteresting. Your ears hear ranges of octaves better. **IMPORTANT NOTE** : If Mode is set to Visualization and this parameter is set to 0, the output data is interpreted more simply: **1 sample per Hz**. Set the CHOP viewer Units to Samples (via RMB on CHOP graph) and the level you see at sample 5000 is the level at 5 KHz.
- High Frequency Boost `highfreqboost` - When 0, the levels are not changed. When greater than 1, the levels are boosted, mostly at the high frequencies. High Frequency Boost can be over-driven past 1.
- Output Length `outputmenu` - ⊞ - The method how output length will be determined.
  * Match Length To Frequency `matchtofrequency` -
  * Set Length Manually `setmanually` -

- Set Output Length `outlength` - Number of Samples desired in output. The fewer the samples, the less the frequency resolution.

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

## Notes
A reasonable scenario (in terms of CPU usage) is an FFT size of 2048. You get good definition with the spectrum, and also enough padding to (almost) deal with two dropped frames.
An [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") can be attached and the channel `hz_per_sample` can be viewed. Applicable only of the Frequency axis is set to Linear. With it set to output to normal FFT, to determine the frequency that a given sample represents, use the formula:
In order to convert back to a signal, both channels are required. The suffixes should be the same as those used in the previous Audio Spectrum CHOP.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Audio Spectrum CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio Spectrum CHOP Info Channels
  * hz_per_sample -

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
