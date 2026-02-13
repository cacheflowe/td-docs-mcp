---
url: https://docs.derivative.ca/Constant_CHOP
category: CHOPs
title: Constant_CHOP
---

# Constant CHOP
## Summary

The Constant CHOP creates new constant-value channels. Each channel can be named and assigned a different value. To create a channel, simply enter a channel name in a name parameter on the Constant page, then adjust the below value.
The CHOP interval (length of time) is one sample long by default (one sample at index 0 = frame 1). An interval range can be optionally set in the Channel page.
You can use [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion") like `geo[1-4][xyz]` to generate multiple channels in one line.
A simple Constant CHOP with no inputs is the most common use of the CHOP. However, the channels names and values can be set up by connecting any CHOP to its input and clicking the Snapshot Input button (Snap page). This allows you to get some channels from another CHOP and adjust them with sliders in the Constant CHOP.
The second input can be used to add offsets to the constant values. When the second input (Active) is greater than zero, any change to the first input will be added to the output of the CHOP. This is useful for adjusting Constant CHOP values from external input devices like a MIDI slider box. For example you can connect the mouse or a MIDI slider box to a [Mouse In CHOP](https://docs.derivative.ca/Mouse_In_CHOP "Mouse In CHOP") or [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP"), and you can raise/lower the Constant CHOP values by holding the Active input On, while moving the mouse or sliders.
[constantCHOP_Class](https://docs.derivative.ca/ConstantCHOP_Class "ConstantCHOP Class")

## Parameters - Constant Page
The channel is created if there is a name in the Name field. You can enter channel name patterns in the Name field, so you can create many channels with the same value. For example, try entering:
```
geo[1-5:2]:s[xyz]

```

in the first channel field instead of "`chan1`". See [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion"), [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Constant `const` - Sequence of name/value pairs defining the channels
- Name `const0name` - The name of the channel.
- Value `const0value` - The value of the channel.

## Parameters - Snap Page
[![ConstantCHOPSnapPage.png](https://docs.derivative.ca/images/2/26/ConstantCHOPSnapPage.png)](https://docs.derivative.ca/File:ConstantCHOPSnapPage.png)
The Constant CHOP can preset its channel names and values using the Snap page. We often want to grab some channels (Snapshot) and edit them later.
- Snapshot Input `snap` - The optional first CHOP input on Constant is used when the Snapshot Input button is pressed. At this time, the channel names and values at the CHOP input at the current frame are used to initialize the channel names and values of the constant sliders.
To snap channels from other OPs, connect a Parameter CHOP to the Constant CHOP and hit `Snapshot Input`.
You can simulate the pressing of the Snapshot Input button from a script. To simulate the clicking of a CHOP dialog box button from a script use the [Par Class](https://docs.derivative.ca/Par_Class "Par Class") pulse() Method:
Example:
```
op('constant1').par.snap.pulse()

```
- First Channel `first` - The First Channel parameter is used to select a smaller set of the incoming channels. This is useful if the number of incoming channels is greater than the 40 channels the Constant CHOP can hold, and you must break it into several CHOPs.
- Active Needs Current `current` - This is used with the second input as described above, when you want to add a displacement to channels by using external devices or sources.      When Active Needs Current is On, the second CHOP input (the Active input) has an effect only if the Constant CHOP is the current CHOP.     When Active Needs Current is Off, the Constant CHOP is affected any time the Active input is on (greater than 0).     This is used by the Channel Editor when editing keyframes using CHOPs. An input device like a button in the Keyboard In CHOP or a MIDI keyboard can be fed to the Active input of many Constant CHOPs. Only the current CHOP will be affected if this option is On.

## Parameters - Channel Page
- Single Sample `single` - Turn this Off to make constant channels that are longer than one Sample.
- Start `start` - Start and end of the interval, expressed in Units (seconds, frames or samples). The parameters are expressed in the `Units` found on the Common page. To set the CHOP to be 100 samples long, Set `Units` to Samples, `Single Frame` Off and `Start` / `End` to 0 and 99.
- Start Unit `startunit` - ⊞ - Select the units to use for this parameter, Samples, Frames, or Seconds.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- End `end` - Start and end of the interval, expressed in Units (seconds, frames or samples). The parameters are expressed in the `Units` found on the Common page. To set the CHOP to be 100 samples long, Set `Units` to Samples, `Single Frame` Off and `Start` / `End` to 0 and 99.
- End Unit `endunit` - ⊞ - Select the units to use for this parameter, Samples, Frames, or Seconds.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - The right extend conditions (after range).
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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Constant CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
