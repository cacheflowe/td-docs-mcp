---
url: https://docs.derivative.ca/Filter_CHOP
category: CHOPs
title: Filter_CHOP
---

# Filter CHOP
## Summary

The Filter CHOP smooths or sharpens the input channels. It filters by combining each sample and a range of its neighbor samples to set the new value of that sample. Each filter type uses its own weighting factors for the neighboring samples. The Filter Width determines the number of neighbors to use.
The default Gaussian filter nicely smooths out data, typically with a Filter Width around .3 seconds. The Box Filter is interesting when your inputs are step changes to new values: the values linearly interpolate to the new value.
It is useful to follow the Filter CHOP with a [Trail CHOP](https://docs.derivative.ca/Trail_CHOP "Trail CHOP") and connect the filtered and pre-filtered signal to its inputs.
If you want to pass one or more channels in, each with multi-samples, and you want to filter each sample as if each sample was its own filter, turn on the Filter per Sample parameter.
For a similar, more-abrupt effect, see the [Lag CHOP](https://docs.derivative.ca/Lag_CHOP "Lag CHOP").
The Filter CHOP can filter both motion and sound, but other CHOPs are more appropriate for filtering sound (see the [Audio Filter CHOP](https://docs.derivative.ca/Audio_Filter_CHOP "Audio Filter CHOP"), [Band EQ CHOP](https://docs.derivative.ca/Band_EQ_CHOP "Band EQ CHOP"), and [Parametric EQ CHOP](https://docs.derivative.ca/Parametric_EQ_CHOP "Parametric EQ CHOP")).
[filterCHOP_Class](https://docs.derivative.ca/FilterCHOP_Class "FilterCHOP Class")

##  Notes on the One Euro Filter
The one Euro Filter is especially useful when a person is in an interaction loop with TouchDeigner and wants quick response: It responds quickly to large changes in value, and it smooths out jitters in the input:
  * Cutoff Frequency: Decrease it if slow speed jitter is a problem.
  * Slope Cutoff Frequency: Avoids high derivative bursts caused by jitter. (The research paper implementation fixes this value to 1Hz but defaults to )
  * Speed Coefficient: Increase if high speed lag is a problem.

The 1 € filter ("one Euro filter") is a simple algorithm to filter noisy signals for high precision and responsiveness. It uses a first order low-pass filter with an adaptive cutoff frequency: at low speeds, a low cutoff stabilizes the signal by reducing jitter, but as speed increases, the cutoff is increased to reduce lag. The algorithm is easy to implement, uses very few resources, and with two easily understood parameters, it is easy to tune. In a comparison with other filters, the 1 € filter has less lag using a reference amount of jitter reduction. (researchgate.net)
Here is a procedure to tune the One Euro filter: First Speed Coefficient is set to 0 and Cutoff Frequency to a reasonable middle-ground value such as 1 Hz. Then the body part is held steady or moved at a very low speed while Slope Cutoff Frequency is adjusted to remove jitter and preserve an acceptable lag during these slow movements (decreasing Slope Cutoff Frequency reduces jitter but increases lag, Slope Cutoff Frequency must be > 0). Next, the body part is moved quickly in different directions while Speed Coefficient is increased with a focus on minimizing lag. First find the right order of magnitude to tune Speed Coefficient, which depends on the kind of data you manipulate and their units: do not hesitate to start with values like 0.001 or 0.0001. You can first multiply and divide Speed Coefficient by factor 10 until you notice an effect on latency when moving quickly. Note that parameters Speed Coefficient and Speed Coefficient have clear conceptual relationships: if high speed lag is a problem, increase Speed Coefficient. If slow speed jitter is a problem, decrease Slope Cutoff Frequency.
reference: Casiez, G., Roussel, N. and Vogel, D. (2012). 1€ Filter: A Simple Speed-based Low-pass Filter for Noisy Input in Interactive Systems

## Parameters - Filter Page
- Type `type` - ⊞ - There are seven types of filters:
  * Gaussian `gauss` - This filter has a Gaussian (normal or "bell" curve) shape that smooths the channel. It acts as a low pass filter. The wider the filter, the lower the cutoff frequency, resulting in smoother data.
  * Left Half Gaussian `halfgauss` - This produces a lag on the channel. If the input channels represent values over time, this filter is seen as only using samples back in time from the current sample. For time-data, this is more realistic as you can't look ahead in time. (Maybe some day.) It has a half-bell shape.
  * Box `box` - This filter is box-shaped, meaning that each neighbor sample it uses has the same weighting factor. It can produce unwanted steps in the output channel because the effect of the samples at the extremes of the filter don't fade out as the window slides over the samples. It low-pass filters data, similar to the Gaussian filter.

    NOTE: When using Gaussian or Box filtering, the channel is delayed by half the filter size (i.e. a Filter Size of 30 samples will delay the output by 15 samples). To eliminate this delay, use either a Left Half Gaussian or a Left Half Box filter. Applying a Sharpen or Edge Detect filter always delays the output by half the filter size. Applying a Despike filter will delay the output by the full filter size.
  * Left Half Box `halfbox` - This filter produces a lag on the data, uses only samples back in time, and otherwise acts like a box filter.
  * Edge Detect `edge` - This filter detects "edges", sharp changes in the input channels. It acts as a high pass filter. As the filter width is increased, more low frequencies are added.
  * Sharpen `sharpen` - This filter sharpens all high frequencies. It is the sum of the edge detect result and the original data.
  * De-spike `despike` - This filter removes "spikes" (samples more than `Spike Tolerance' above or below the expected sample value). The filter width allows you to eliminate spikes that are several samples long. Wide filters will remove wide spikes (spikes of several samples) and small filters will only remove narrow spikes (one or two samples in length).
  * Ramp Preserve `ramp` - This filter attempts to output an increasing ramp that increases at the 'Ramp Rate' parameter rate. The input channel to the Filter CHOP should be increasing at this rate, with possibly some errors/noise in it. The Ramp Preserve will ignore the input channel unless the difference between the input value and the current ramp value is larger than 'Ramp Tolerance' parameter. When the difference becomes greater than the tolerance, the ramp will reset to start at the current input value.
  * One Euro `oneeuro` - This filter is good for filtering noisy signals while maintaining high precision and resposiveness.

- Effect `effect` - The extent to which the filter affects the channel (0 - not at all, 1 - maximum effect).
- Filter Width `width` - The amount of surrounding samples used in the calculation of the current sample. It is expressed in the Units.
- Filter Width Unit `widthunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Spike Tolerance `spike` - For the De-spike filter type, this is the amount that a sample can differ from its neighbours without being considered a spike.
- Ramp Tolerance `ramptolerance` - When using a Ramp Preserve filter, if the input value deviates from the current output ramp value by this much, then the ramp will reset to the new input value. Otherwise the Ramp Preserve will continue climbing at the specified 'Ramp Rate'.
- Ramp Rate `ramprate` - When using a Ramp Preserve filter, this is the rate that the CHOP's output channel will increase. Only if the input channel value deviates from the desired output value by 'Ramp Tolerance' amount will the CHOP instead output the input channel value.
- Number of Passes `passes` - The number of times the filter is applied to the channel.
- Cutoff Frequency (Hz) `cutoff` - Decrease it if slow speed jitter is a problem.
- Speed Coefficient `speedcoeff` - Increase if high speed lag is a problem.
- Slope Cutoff Frequency (Hz) `slopecutoff` - Avoids high derivative bursts caused by jitter.
- Slope Down Reset `slopedownreset` - When On resets (bypasses) the filter effect when the downward slope exceeds the Slope Down Max value to the right.
- Slope Down Max `slopedownmax` - Set the maximum value of the slope downwards beyond which the filter resets when the toggle to the left is On.
- Slope Up Reset `slopeupreset` - When On resets (bypasses) the filter effect when the upward slope exceeds the Slope Up Max value to the right.
- Slope Up Max `slopeupmax` - Set the maximum value of the slope upwards beyond which the filter resets when the toggle to the left is On.
- Reset `reset` - When On resets (bypasses) the filter effect.
- Reset Pulse `resetpulse` - Instantly resets the filter effect.
- Filter per Sample `filterpersample` - Applies the filter to each sample of the channel instead of across the whole channel. Useful for working with multi-sample channels.

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
Extra Information for the Filter CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
