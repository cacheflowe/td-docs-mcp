---
url: https://docs.derivative.ca/Pulse_CHOP
category: CHOPs
title: Pulse_CHOP
---

# Pulse CHOP
## Summary

The Pulse CHOP generates pulses in one channel at regular intervals. The amplitude of each pulse can be edited with the CHOP sliders or with handles on the graph.
The Pulse CHOP gives a set of pulses in a static channel of a specifiable length.
See also the [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP") to get an endless stream of pulses that is [Time Sliced](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)"), and the [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP") for a string of static pulses.
The Pulse CHOP can be used as triggers to the [Copy CHOP](https://docs.derivative.ca/Copy_CHOP "Copy CHOP"), and can represent regularly-timed events.
By default, the pulses are a single sample long, but you can increase the Pulse Width so that the pulses are steps to the next pulse. You can also interpolate the values between pulses, as Linear, Ease In Ease Out, Cubic or other curves.
The pulses can be restricted to a minimum / maximum limit. If the Limit Type is Clamp, the graph has additional convenient handles at the minimum and maximum for each pulse.
The Pulse CHOP generates a single channel, and you can merge several Pulse CHOPs into a multi-channel CHOP.
The Pulse CHOP uses its optional first input as a start/end reference, so a number of Pulse CHOPs can be stretched to the same interval.
The optional second input is used to specify pulses at specific sample locations. Every single-sampel input channel is then interpreted as the location of a pulse.
In order to set the value at the last sample, the option, Last Pulse at Last Sample is provided. Otherwise, the last pulse is prior to the last sample.
[pulseCHOP_Class](https://docs.derivative.ca/PulseCHOP_Class "PulseCHOP Class")

## Parameters - Pulse Page
- Number of Pulses `number` - The number of pulses to generate.
- Interpolate `interp` - ⊞ - You can interpolate the values between pulses using the following function curves:
  * Off `nointerp` - Disables interpolation.
  * Linear (Ramp) `linear` - Use linear interpolation between samples when the interval is lengthened. Averages all samples near the new sample when the interval is shortened.
  * Ease in `easein` - Uses an easein() function for blending.
  * Ease out `easeout` - Uses an easeout() function for blending.
  * Ease in Ease out `cosine` - Uses both easein() and easeout() functions.
  * Cubic `cubic` - Cubically interpolates between samples, for smoother curves than Linear. This method is not recommended for channels with sharp changes.
  * Connect `connect` - Instead of the pulses returning to 0, the pulse value is held until the pulse.

- Pulse Width `width` - By default, the pulses are a single sample long, but you can increase the Pulse Width so that the pulses are steps to the next pulse.
- Pulse Width Unit `widthunit` - ⊞ - Select the units to use for this parameter, Samples, Frames, or Seconds.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Limit Type `limit` - ⊞ - Enable the Minimum and Maximum clamping values below with this menu.
  * Off `nolimit` - Pulses are allowed to be any value with no clamping.
  * Clamp `clamp` - Clamps pulse values to the Minimum and Maximum values specified below.

- Minimum `min` - The pulses can be restricted to a Minimum limit. If the Limit Type is Clamp, the graph has additional convenient handles at the minimum for each pulse.
- Maximum `max` - The pulses can be restricted to a Maximum limit. If the Limit Type is Clamp, the graph has additional convenient handles at the maximum for each pulse.
- Minimum Spacing `minspacing` - When creating pulses via the second input, the Minimum Spacing parameter will separate out pulses from each other with the minimum distance specified here. The unit of the spacing is controlled by the Pulse Index Unit parameter.
- Cascade when Spacing `cascade` - When minimum spacing between pulses is enabled, cascading will shift pulses by the amount of samples added via the minimum spacing.
- Outside Pulses `outpulse` - Control how to deal with pulse positions specified outside the operators range.
- Pulse Index Unit `pulseunit` - Control what unit the in the second input specified values should be interpreted as.
- Separate Output Channels `separateoutchan` - When toggled on, will create a seperate channel per pulse.
- Non-Additives `nonadditives` - When enabled will not add up amplitudes of pulses specified on the same sample index.
- Last Pulse at Last Sample `lastpulse` - In order to set the value at the last sample, the option Last Pulse at Last Sample is provided. Otherwise, the last pulse is prior to the last sample.

## Parameters - Values Page
- Pulse `pulse` - Sequence of pulse values
- Pulse 0 `pulse0value` - The value of the sequence pulse.

## Parameters - Channel Page
- Channel Names `channelname` - You can creates many channels with simple patterns like "`chan[1-20]`", which generates 20 channels from chan1 to chan20. See the section, Common CHOP Parameters for a description of this and all Options. See [Scope and Channel Name Matching](https://docs.derivative.ca/CHOP_Common_Page#Scope "CHOP Common Page") Options.
- Start `start` - Start of the interval, expressed in Units (seconds, frames or samples).
- Start Unit `startunit` - ⊞ - Select the units to use for this parameter, Samples, Frames, or Seconds.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- End `end` - End of the interval, expressed in Units (seconds, frames or samples).
- End Unit `endunit` - ⊞ - Select the units to use for this parameter, Samples, Frames, or Seconds.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Sample Rate `rate` - The sample rate of the channels, in samples per second. Default: `me.time.rate`
- Extend Left `left` - ⊞ - The left extend conditions (before/after range).
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
  * Input 0: Start/End/Rate Reference -

  * Input 1: Pulse Sample Index -

## Info CHOP Channels
Extra Information for the Pulse CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
