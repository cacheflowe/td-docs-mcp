---
url: https://docs.derivative.ca/Envelope_CHOP
category: CHOPs
title: Envelope_CHOP
---

# Envelope CHOP
## Summary

The Envelope CHOP outputs the maximum amplitude in the vicinity of each sample of the input. It takes the absolute value of the input, and uses a sliding window of a number of samples to find the maximum amplitude near each sample.
**Tip:** The loudness levels of an audio track can be kept roughly constant by computing an envelope of the audio with a wide window, and then passing the original audio and the envelope to a [Math CHOP](https://docs.derivative.ca/Math_CHOP "Math CHOP") and selecting **Combine CHOPs - Divide**. This will make the amplitude approximately 1.
[envelopeCHOP_Class](https://docs.derivative.ca/EnvelopeCHOP_Class "EnvelopeCHOP Class")

## Parameters - Envelope Page
- Type `method` - ⊞ - The two methods of calculating the envelope:
  * Exponential Decay `exp` - For each sample, the value is compared to the previous sample. If it is greater than the previous, the value of the envelope is equal to the value of that sample, and that sample is stored as the current peak. If it is less than, the value of the envelope decays exponentially from the last peak to the current value (as more samples pass that are smaller than the peak, the envelope decays toward the waveform). Pros: Always encloses the data. Cons: Slope can be discontinuous, making the output look bumpy.
  * Local Maximum Window `window` - The channel is separated into windows of N samples determined by the Envelope Width. In each window, the maximum amplitude (or power) is found. The maximum value of the window is placed as a data point in the center of the window, and these points are cubically interpolated together to form the output envelope. Pros: Produces Good shapes. Cons: Signal sometimes jumps outside the envelope. The signal is quantized, so pulses can be off by as much as N/2.

- Envelope Bounds `bounds` - ⊞ -
  * Magnitude `mag` -
  * Signal Power `power` -
  * Maximum Values `min` -
  * Minimum Values `max` -

- Envelope Width `width` - The width of the window to use in the envelope calculation. Adjust this width to capture as many features of the input as needed. It is expressed in Units.
- Envelope Width Unit `widthunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Interpolate `interp` - ⊞ -
  * None `none` -
  * Linear `linear` -
  * Cubic `cubic` -

- Normalize Power Envelope `norm` - Keeps the total power in the signal constant when adjusting the Envelope Width.
- Resample Envelope `resample` - When On, the envelope can be resampled to the Sample Rate specified in the parameter below.
- Sample Rate `samplerate` - Set the sample rate to resample the envelope to when the Resample Envelope parameter above is On.

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
Extra Information for the Envelope CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
