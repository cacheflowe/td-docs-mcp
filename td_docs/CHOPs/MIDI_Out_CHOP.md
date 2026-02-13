---
url: https://docs.derivative.ca/MIDI_Out_CHOP
category: CHOPs
title: MIDI_Out_CHOP
---

# MIDI Out CHOP
## Summary

The MIDI Out CHOP sends [MIDI](https://docs.derivative.ca/MIDI "MIDI") events to any available MIDI devices when its input channels change. More flexibly, the Python [midioutCHOP Class](https://docs.derivative.ca/MidioutCHOP_Class "MidioutCHOP Class") can be used to send any type of MIDI event to a MIDI device via an existing MIDI Out CHOP. In [Tscript](https://docs.derivative.ca/Tscript "Tscript"), the `midi` command can output MIDI events.
The MIDI devices can be other software programs (such as midisynth) or devices attached to the serial ports. Channels are used to control the sending of the MIDI events. The channels are evaluated over the last time slice (from the last [Timeline](https://docs.derivative.ca/Timeline "Timeline") position to the current).
The MIDI Out CHOP sends MIDI events based on any changes to its input channels. The channels have to be named appropriately, like `ch3c14` and `ch7n60`.
An event is sent every time a channel changes its value during this slice. All timing is preserved, as long as the [Timeline](https://docs.derivative.ca/Timeline "Timeline") is running in realtime (the "Realtime" flag is in the top menu bar).
Naming the CHOP channels: Channels are mapped to events by their name. Events like notes, controllers and velocities must be followed by the note/controller number (n65, c7). If the number is left off a note event, the note number is the value of the channel. Other events, which are sent to the entire channel, do not need a trailing number (pc, pw). The channel prefix can be used to identify the MIDI channel the event should be sent on (i.e. "ch1n45" assigns that TouchDesigner channel to note 45 messages on MIDI channel 1). Channels can always be renamed with a [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") before entering the MIDI Out CHOP.
The MIDI Out CHOP sends MIDI velocity as well. The values of the channels entering the MIDI Out CHOPs are sent as the velocity of the note. If Normalize is "None", the channel needs to be 0 to 127. If Normalize is "0 to 1", channel values between 0 and 1 are scaled to be MIDI 0 to 127.
The "Cook Every Frame" option cooks the CHOP every frame, even if the CHOP isn't being displayed. All Volume Off and All Volume On flags are new and emit events for Controller 7 of all 16 channels. MIDI output go in a separate thread to allow output that slows TouchDesigner less. It now works in Time Slice mode for note events and controller events. (Not for Program Change or Sysex messages yet) Note channels only trigger anew Note On when the input channel goes from 0 or less to a value greater than zero. Similar for Note Off events.The channel name determines how it is interpreted.
For example,      ch3n60 - this channel is interpreted as channel3 note 60. A Note On event is sent when the value goes from 0 or less to greater than zero     ch5n - This channel will contain note numbers.¬† The value quantized to an integer, and when the integer value changes, the note of the old value goes off and the note of the new value goes on. If the channel steps from 53 to 78, it sends a Note Off event for note 53, and a Note On event for note 78.     ch14c7 - the value of the channel is sent to controller 7 (volume) of channel 14. By default, the values 0 to 1 are mapped to MIDI value 0 to 127.
These features work in Time Slice mode:      By default, channels are to start with "ch" followed by the channel number (1-16). In the case of notes, it is followed by "n" for notes, then digits for the note number. In the case of controllers, it is followed by "c" and a controller number. These prefixes can be altered. MIDI Out now interprets aftertouch, pressure, pitchwheel channels, and outputs these events to the MIDI stream. Note-normalization is added allowing 0 to 127 and 0 to 1 ranges. MIDI Out reads a bar ramp channel to output MIDI clock events¬† (with a channel popup menu to the parameter to select the channel name). Program change events are implemented through the "pc" channels.both 7 and 14 bit controller events can be output. You can capture a MIDI stream and output it to a file.
See also the [MIDI In DAT](https://docs.derivative.ca/MIDI_In_DAT "MIDI In DAT"), [MIDI Event DAT](https://docs.derivative.ca/MIDI_Event_DAT "MIDI Event DAT"), [MIDI In Map CHOP](https://docs.derivative.ca/MIDI_In_Map_CHOP "MIDI In Map CHOP"), [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP"), `midi` command.
[midioutCHOP_Class](https://docs.derivative.ca/MidioutCHOP_Class "MidioutCHOP Class")

## Parameters - Dest Page
- Active `active` - Enable or disable the MIDI Out CHOP.
- MIDI Destination `destination` - ⊞ - Where the MIDI events are sent to. MIDI Mapper is the default destination.
  * Device `device` -
  * File `file` -

- Device Table `device` - Path to the MIDI device [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT").
- Device ID `id` - Specify the id of which device to use.
- One Based Index `onebased` - Make the index 1 based instead of the default 0 based.
- MIDI File `file` - The filename of the output MIDI file.
- Write MIDI File `writefile` - Writes all the data to a MIDI file.
- Channel Prefix `prefix` - The prefix string that all input channels must have in order to extract the channel number from their name (i.e. "ch1note44", with a channel prefix of "ch").
- Cook Every Frame `cookalways` - Forces a cook of the CHOP every frame. It should be On because the MIDI Out CHOP will otherwise only cook if the CHOP leads to a graphics display viewer. You want it to cooks whether you are displaying anything or not.

## Parameters - Output Page
- Automatic Note Off `autonoteoff` - ⊞ - A MIDI 'All Note Off' event can be sent upon the start and/or end of the output.
  * None `none` -
  * At Playback Start `start` -
  * At Playback End `end` -
  * At Playback Start and End `both` -

- All Notes Off `reset` - Sends an All Notes Off message to all MIDI channels.
- All Volume Off `volumeoff` - Sends an All Notes Off message to all MIDI channels.
- All Volume On `volumeon` - Sends an All Notes On message to all MIDI channels.
- Send Start/Stop/Continue Events `startstop` - Sends the appropriate events when the framebar starts or stops.
- Send MIDI Timecode `sendmtc` - While enabled, the MIDI Out CHOP will send MIDI Timecode (MTC) as a stream of quarter frame messages.
- Timecode Object/CHOP/DAT `timecodeop` - The MIDI Timecode value to send. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.

## Parameters - Note Page
- Note Name `notename` - The base name of the note channels. If input channels have a number after the name, it is assumed to be the note number. If not, the channel value is assumed to contain the note number.
- Aftertouch Name `aftername` - The name of the aftertouch channel.
- Pressure Name `pressname` - The name of the channel pressure channel.
- Normalize `notenorm` - ⊞ - Values in the range 0-1 are mapped to MIDI value 0-127.
  * None `off` -
  * 0 to 1 `0to1` -

- Pitch Wheel Name `pitchname` - The name of the pitch wheel channel.

## Parameters - Control Page
- Controller Name `controlname` - The base name of the controller channels.
- Controller Format `controlformat` - ⊞ - Sends 7 or 14 bit controller events.
  * 7 bit Controllers `7bit` -
  * 14 bit Controllers `14bit` -

- Normalize `controlnorm` - ⊞ - Maps channel values from different ranges to 0-127.
  * None `off` -
  * 0 to 1 `0to1` -
  * -1 to 1 `-1to1` -
  * On/Off `onoff` -

- Program Change `progname` - The name of the program change channel.
- Bar Ramp Name `barname` - Clock ticks frequency is determined by the period of the ramp. The ramp must be 0 to 1. An incoming channel name for a 0 to 1 ramp over each 4-beat bar.
- Ticks per Bar `barticks` - Default is 96 = 4 beats * 24 ticks per beat.

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
Extra Information for the MIDI Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific MIDI Out CHOP Info Channels
  * events_sent -

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
