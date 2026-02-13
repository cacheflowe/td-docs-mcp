---
url: https://docs.derivative.ca/Audio_Band_EQ_CHOP
category: CHOPs
title: Audio_Band_EQ_CHOP
---

# Audio Band EQ CHOP
## Summary

The Audio Band EQ CHOP is a 16-band [equalizer](http://en.wikipedia.org/wiki/Equalization_\(audio\)) which filters audio input channels in the same way that a conventional band (graphic) equalizer uses a bank of sliders to filter fixed-frequency bands of sound.
The CHOP has 16 bands from 25 Hz to 22 kHz with one parameter per band. The bandwidth per band is approximately half the frequency between the prior and next bands.
See [Audio Filter CHOP](https://docs.derivative.ca/Audio_Filter_CHOP "Audio Filter CHOP"), [Audio Para EQ CHOP](https://docs.derivative.ca/Audio_Para_EQ_CHOP "Audio Para EQ CHOP"), [Audio Dynamics CHOP](https://docs.derivative.ca/Audio_Dynamics_CHOP "Audio Dynamics CHOP"), [Audio Spectrum CHOP](https://docs.derivative.ca/Audio_Spectrum_CHOP "Audio Spectrum CHOP")
[audiobandeqCHOP_Class](https://docs.derivative.ca/AudiobandeqCHOP_Class "AudiobandeqCHOP Class")

## Parameters - Low Bands Page
- Dry / Wet Mix `drywet` - As this parameter is reduced from 1 (Wet) toward 0 (Dry), it removes the effect of the filter.
25 Hz `band1` - Controls boost/cut centered at 25 Hz.
40 Hz `band2` - Controls boost/cut at the 40 Hz band.
60 Hz `band3` - Controls boost/cut at the 60 Hz band.
90 Hz `band4` - Controls boost/cut at the 90 Hz band.
150 Hz `band5` - Controls boost/cut at the 150 Hz band.
240 Hz `band6` - Controls boost/cut at the 240 Hz band.
370 Hz `band7` - Controls boost/cut at the 370 Hz band.
590 Hz `band8` - Controls boost/cut at the 590 Hz band.

## Parameters - High Bands Page
930 Hz `band9` - Controls boost/cut at the 930 Hz band.
1.5 KHz `band10` - Controls boost/cut at the 1.5 Hz band.
2.3 KHz `band11` - Controls boost/cut at the 2.3 Hz band.
3.6 KHz `band12` - Controls boost/cut at the 3.6 Hz band.
5.6 KHz `band13` - Controls boost/cut at the 5.6 Hz band.
8.9 KHz `band14` - Controls boost/cut at the 8.9 Hz band.
14 KHz `band15` - Controls boost/cut at the 14 Hz band.
22 KHz `band16` - Controls boost/cut at the 22 Hz band.

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
Extra Information for the Audio Band EQ CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
