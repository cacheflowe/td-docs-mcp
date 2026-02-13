---
url: https://docs.derivative.ca/MIDI_In_Map_CHOP
category: CHOPs
title: MIDI_In_Map_CHOP
---

# MIDI In Map CHOP
## Summary

See first the [MIDI In DAT](https://docs.derivative.ca/MIDI_In_DAT "MIDI In DAT"). The MIDI In Map CHOP reads in specified channels from the [MIDI Device Mapper Dialog](https://docs.derivative.ca/MIDI_Device_Mapper_Dialog "MIDI Device Mapper Dialog") which prepares slider channels starting from s1, s2, etc. and button channels starting with b1, b2 and so on. The MIDI In Map CHOP selects from these channels.
**NOTE** : (Apr 12 09) This page needs to be updated with the info in the release notes.
Another CHOP, the [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP") retrieves [MIDI](https://docs.derivative.ca/MIDI "MIDI") data more directly but it is less portable as it addresses the MIDI channel numbers, note numbers and controller numbers in the CHOP, so in order to change the MIDI mapping, you need to change the settings in TouchDesigner, whereas with the MIDI In Map CHOP, users need only set the mapping in the Dialogs -> MIDI Device Mapper.
See also the [MIDI In DAT](https://docs.derivative.ca/MIDI_In_DAT "MIDI In DAT"), [MIDI Event DAT](https://docs.derivative.ca/MIDI_Event_DAT "MIDI Event DAT"), [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP"), [MIDI Out CHOP](https://docs.derivative.ca/MIDI_Out_CHOP "MIDI Out CHOP"), `midi` command, [MIDI Device Mapper Dialog](https://docs.derivative.ca/MIDI_Device_Mapper_Dialog "MIDI Device Mapper Dialog").
[midiinmapCHOP_Class](https://docs.derivative.ca/MidiinmapCHOP_Class "MidiinmapCHOP Class")

## Parameters - MidiInMap Page
- Device Table `device` - Path to the MIDI device [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT").
- Device ID `id` - Specify the id of which device to use.
- Sliders `sliders` - The slider controllers to import from the MIDI Mapper. For example to import the first 16 sliders, slider 20 and sliders 32 to 40, type: ```
 s[1-16] s20 s[32-40]

```
- Buttons `buttons` - The buttons to import from the MIDI Mapper. For example to import the first 16 buttons, button 20 and buttons 32 to 40, type: ```
 b[1-16] b20 b[32-40]

```
- Include Velocity in Buttons `bvelocity` - Enable velocity on button inputs if available.
- Queue Slider Events `squeue` -

## Parameters - Channel Page
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
  * Default Value `default` -

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
Extra Information for the MIDI In Map CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
