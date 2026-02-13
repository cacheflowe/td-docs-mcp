---
url: https://docs.derivative.ca/Event_CHOP
category: CHOPs
title: Event_CHOP
---

# Event CHOP
## Summary

The Event CHOP manages the birth and life of overlapping events triggered by devices like a MIDI keyboard. It can be seen as a simple particle system designed for MIDI keyboards.
The Event CHOP generates one sample for each off-to-on event in the input channels, which would often come from a [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP"), [MIDI In Map CHOP](https://docs.derivative.ca/MIDI_In_Map_CHOP "MIDI In Map CHOP"), [Keyboard In CHOP](https://docs.derivative.ca/Keyboard_In_CHOP "Keyboard In CHOP"), or python events sent to the Event CHOP. The sample exists for the duration of the event's attack+decay+sustain+release time.
**NOTE** : See the examples in Help->[OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets")
The Event CHOP can used to follow a polyphonic music keyboard with MIDI velocity, and can generate generating one object, polygon or geometry instance for each event. It assures the object, polygon or instance exists until the event ends after an attack-decay-sustain-release phase. The Event CHOP is often fed through other OPs to the Instance parameters of a Geometry component.
The Event CHOP outputs up to 8 channels, with one sample generated per off-to-on event that is active. The sample is active until the attack-decay-sustain-release is over, at which moment the sample disappears (like particle death).
Watch the channel graph of the Event CHOP to understand what it is doing. It can be sent to a [Limit SOP](https://docs.derivative.ca/Limit_SOP "Limit SOP") or a [Channel SOP](https://docs.derivative.ca/CHOP_to_SOP "CHOP to SOP") to place geometry for each event. You can send event information to the SOP via the Event CHOP channels that get transformed into geometry channels like `tx`, `ty`, `scale`, texture v (giving movie time offsets), alpha, r, g and b colors.
On a MIDI keyboard, you can trigger many events simultaneously, and, like particles, you may want to launch objects that remain in existence the next time you press the same key.
The Event CHOP is designed to handle this. It creates one sample every time you press any key, and that sample lives for any length of time. This CHOP is lightweight - the minimum number of channels and samples are created, even with 88-key MIDI keyboards and lots of pounding on the keyboard.
There are channels that represent age, note number and MIDI velocity when you pressed the key, as well as a flag telling if the key has since been released.
Each event has a unique ID, held in the `id` channel that can be used to generate random XY displacements of each note, for example.
A movie index is set by the `state` channel which rises from 0 to 1 and loops between 1 to 2 continuously until the note goes into its release state at which time it goes from 2 to 3. So for a bird cycle, you use the 0 to 1 state for the jump phase, 1 to 2 for the flappin in flight phase, and 2 to 3 for the landing phase.
The Event CHOP's 1st input is for event triggers.
The 2nd input resets the triggers.
The 3rd input is optional and allows for sampling values for each event.
See also: [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP"), [Count CHOP](https://docs.derivative.ca/Count_CHOP "Count CHOP"), [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP"), [Trigger CHOP](https://docs.derivative.ca/Trigger_CHOP "Trigger CHOP")
[eventCHOP_Class](https://docs.derivative.ca/EventCHOP_Class "EventCHOP Class")

## Parameters - Channels Page
The Event CHOP outputs seven channels that define the properties of the events.
- ID `id` - The sequence # of the event, starting from 0 and incrementing by 1 for each event.
- Index `index` - The channel index of the incoming CHOP that caused the event.
- Active `active` - While the input is greater than 0 this channel goes to 1, ie when the input channel goes "On".
- Input `input` - The value of the input channel when the input went on (at the birth of the event). It is often the note velocity value. If you pass the Midi In CHOP into the Event CHOP, and set the Midi In option to output the velocity, velocity will end up in this channel and preserved until the event ends.
- Time `time` - Time in seconds from the start of the event.
- ADSR `adsr` - The value according to the Attack, Decay, Sustain, Release. It uses the parameters on the ADSR page, regulating the speed and values, with extended parameters: Attack Time, Attack Level, Decay Time, Sustain Time, Sustain Min, Sustain Max, Release Time, Release Level.
- State `state` - This is good for playing back movies. You divide your movie into 4 parts that correspond to the (0=attack, 1=decay, 2=sustain, 3=release) phases. The state channel outputs fractional values, so you can watch it climb through all the transitions, including multiple sustain-sections. e.g., 0...1...2...2...2...2...3...4. If your movie is 8 seconds long, take the state channel and multiply by 2, passing it as the time-index of the movie.
Goes from 0 to 1 during the attack phase, 1 to 2 as it repeats in the sustain phase, and 2 to 3 in the release phase. It is suitable for indexing movies.
- Reset Condition `resetcondition` - ⊞ - Determines the reset behavior of using the 2nd Input Reset Trigger. This parameter is only active if there is an input connected to the CHOP's 2nd input.
  * Off to On `offtoon` -
  * While On `on` -
  * On to Off `ontooff` -
  * While Off `off` -

- Reset `reset` - When set to 'On' it resets the CHOP clearing all events.
- Reset Pulse `resetpulse` - Immediately resets the CHOP and clears all events in the frame it was clicked.
- Callbacks DAT `callbacks` - The path to a DAT containing onCreate() and onDestroy() callbacks for each event.

## Parameters - ADSR Page
- Attack Time `attacktime` - Affects `adsr` and `state` channel. Time to rise to max attack level.
- Attack Time Unit `attacktunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Attack Level `attacklevel` - Affects `adsr` channel. Peak attack level.
- Decay Time `decaytime` - Affects `adsr` channel and `state` channel. Time after peak to sustain level.
- Decay Time Unit `decaytunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Sustain Time `sustaintime` - Affects `adsr` channel.
- Sustain Time Unit `sustaintunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Sustain Min `sustainmin` - Affects `adsr` channel. Level at start of sustain time.
- Sustain Max `sustainmax` - Affects `adsr` channel. Level at end of sustain time.
- Release Time `releasetime` - Affects `adsr` and `state` channels.
- Release Time Unit `releasetunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Release Level `releaselevel` - Affects `adsr` channel. Level at end of life cycle.
- Speed `speed` - Affects the speed of the event, letting you stretch out or shorten the life of an event.
- Global Speed `globalspeed` -

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
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Event CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
