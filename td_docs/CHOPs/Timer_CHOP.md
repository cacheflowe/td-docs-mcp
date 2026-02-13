---
url: https://docs.derivative.ca/Timer_CHOP
category: CHOPs
title: Timer_CHOP
---

# Timer CHOP
## Summary

The Timer CHOP is an engine for running timed processes. It outputs channels such as timing fractions, counters, pulses and timer states, and it calls python functions (callbacks) when various timing events occur.
Examples using the Timer CHOP include triggering multiple timed cues, running playlists, timelines, state machines, and driving pre-animated animation components in 3D scenes. See Help -> Operator Snippets for numerous examples.
You set a timer to a number of seconds (or unlimited), frames or samples, and trigger it to start via the Start parameter or the second input CHOP. The Timer CHOP outputs in seconds, frames, samples, fraction and on-off states as it’s counting, including a `done` channel that goes on when it is complete. When it reaches certain states like end-of-cycles or when it’s done, various python callbacks are called allowing you to customize its behavior.
The Timer CHOP gets triggered by events (via pulsing its parameters or driving its two inputs). It takes events in, counts time, changes state. Via its python callback functions, you can send events out to other nodes, set parameters, get/set values in DATs, CHOPs and storage, restart itself, or trigger other nodes. As such, it can operate as a state machine.
It has play/pause, plus a speed control to slow down or speed up the timer.
It can also cycle indefinitely and then can be signaled to end immediately or at the end of the current cycle.
**Recommended** : the **OP Snippets for Timer CHOP**. See the channel descriptions in [Initialize Start](https://docs.derivative.ca/Initialize_Start "Initialize Start").
**Multiple Timer segments** - One Timer CHOP can also have multiple timers within it. By attaching a Table DAT you can define one timer (segment) per row. In Serial Timers mode it allows for one time segment followed by another. In Parallel Timers mode, the timers all run in parallel, each with its own begin time and length, and its own set of output channels.
[![Timer CHOP.2.png](https://docs.derivative.ca/images/8/82/Timer_CHOP.2.png)](https://docs.derivative.ca/File:Timer_CHOP.2.png)
The Timer CHOP can be Locked to Timeline in a deterministic way, or run more freely in Sequential Mode. When run independently from the timeline, you can jump ahead, break out of cycles, pause, `goTo()` exact position or timecode in the timer, and dynamically adjust the speed.
Attach an Info DAT to the Timer CHOP to see the timecodes, or use the `.timecode` members. Custom text strings can be placed in the Info DAT for each segment, and custom animated channels can be created.
To make an entire Timer CHOP loop after the last segment, set the On Done menu to Re-Start.
**Tip: What happens when you press Start** - The timers are at 0 when you Initialize, for example `timer_frames` = 0. On the frame when you press Start, by default, the `running` channel goes from 0 to 1, and all the `timer_` counter channels step forward by 1 frame. If you want the timers to hold at 0 until the next frame, set the Run Value parameter to Zero. This is useful when you are cutting from black or other media to a visible first-frame of a movie when `running` goes to 1.
**Chaining Timers** - The Timer CHOPs can be chained together, so that when one ends, the next can begin. They just need to all be Initialized together, where the `ready_pulse` channel of one Timer CHOP is exported to the Initialize parameter of the next Timer CHOP. Then they can be run in sequence, where the output of one Timer CHOP’s `done_pulse` channel is wired to the Start input (or exported to the Start parameter) of the next Timer CHOP. You start the chain of timers by starting the first Timer CHOP. By using some Timer CHOPs to loop awaiting input or response, or by adding logic to decide which CHOP to start next, state machines can be implemented.
### Callbacks
The callbacks are called at different moments during the timer progression.
`onInitialize()` gets called when you pulse the Initialize parameter. Here you can prepare any part of your setup prior to starting. At the end of Initialize the timer goes into a "ready" state.
`onStart()` gets called on the frame that the Start parameter is pulsed. The timer then goes into a "running" state.
`onTimerActive()` gets called every frame that the timer is running and there is no Delay or Play is off.
`onCycleStart()` gets called if the timer is set to cycle via the Cycle parameters.
Before a cycle or segment ends, an `onCycleEndAlert()` callback based on the Cycle End Alert parameter can be called to allow you to prepare for the next cycle, segment or Timer CHOP.
`onSegmentEnter()` and `onSegmentExit()` get called if the timer is being driven by a Segments DAT which acts like several timers in one. The argument `segment` in these callbacks is actually an object with useful members including any custom columns you have in your segment table: In `onSegmentEnter()`, put the code `print(help(segment))`
`onDone()` gets called when the timer reaches its finished state.
You can initialize at a specific time by using `.masterSeconds` in `onInitialize()`.
**See also** : [Trigger CHOP](https://docs.derivative.ca/Trigger_CHOP "Trigger CHOP"), [Event CHOP](https://docs.derivative.ca/Event_CHOP "Event CHOP"), [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP"), [Count CHOP](https://docs.derivative.ca/Count_CHOP "Count CHOP"), [Beat CHOP](https://docs.derivative.ca/Beat_CHOP "Beat CHOP"), [Event CHOP](https://docs.derivative.ca/Event_CHOP "Event CHOP"), [Clock CHOP](https://docs.derivative.ca/Clock_CHOP "Clock CHOP"), [Delay CHOP](https://docs.derivative.ca/Delay_CHOP "Delay CHOP"), [CHOP Execute DAT](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT"), [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP"). time measurements{| class="wikitable"|+ Time Measurements and what affects them|- ! Name !! Speed !! Play !! Cycles !! Go To and Cueing !! Subrange !! Delay Between Segments|-| Cumulative Time Count | | slows if speed<1 | | pauses when off | | keeps counting | | jumps | | jumps | | pauses|-| Playing Time Count | | unaffected | | pauses when off | | keeps counting | | keeps counting | | keeps counting | | keeps counting|-| Running Time Count | | unaffected | | unaffected | | keeps counting | | keeps counting | | keeps counting | | keeps counting|-| Master Time Count | | slows if speed<1 | | pauses when off | | see note * | | jumps | | jumps | | keeps counting|-| Segment + Fraction | | 0 to 1 per-segment | | pauses when off | | see note * | | jumps | | jumps | | pauses|} **note: jumps back every cycle if Cycle Limit is off. keeps counting up if Cycle Limit is on.**
[timerCHOP_Class](https://docs.derivative.ca/TimerCHOP_Class "TimerCHOP Class")

## Parameters - Timer Page
- Active `active` - ⊞ - The Timer cooks: Never / Always / While Running (while in "running" state) / While Playing (while in "running" state and Play is on).
  * Never `never` -
  * Always `always` -
  * While Running `running` -
  * While Playing `playing` -

- Time Control `timecontrol` - ⊞ - **Sequential** (timeline-independent) or **Locked to Timeline**. In Locked to Timeline, non-deterministic features are disabled. **External CHOP Channel** lets you drive the master time (`.masterSeconds` etc) using a CHOP channel defined by the parameters on the External page. **External Timecode** lets you drive the master time using a timecode CHOP/DAT/Object.
  * Lock To Timeline `lock` - Output is determined by the current frame position.
  * Sequential `sequential` - Output runs continuously, regardless of current frame position.
  * External CHOP Channel `chop` - Output is determined by external CHOP channel value.
  * External Timecode `timecode` - Output is determined by the value of an external timecode.

- Defer Par Changes `deferpars` - When On, parameter changes like Length, Cycles and others are ignored until the next Intitalize. When Off, paraameter changes affect the timer immediately (possibly giving jumps in state).
- Initialize `initialize` - (pulse parameter) Initialize is the signal to get the timer ready: sets the frames, samples and fraction counters to zero (delay, timer, cycle, segment), set the output channels in the proper state, `done` to be off, the onInitialize() callback is run, and when initialize is complete, it indicates it’s ready by turning on the `ready` channel, awaiting a Start pulse.
- Start `start` - (pulse) Start is the signal to begin the timers counting. It will count through the delay first, then the timer length. It does an Initialize if it is not already initialized, and then starts counting.
- Length Type `lengthtype` - ⊞ - Describes how the length is defined.
  * Fixed `fixed` - Lengths are finite, that is of a specific duration.
  * Infinite `infinite` - The segments run continuously without end.

- Length `length` - ⊞ - (float) the time-length of the timer. Set the Units menu to Seconds, Frames or Samples.
  * Length `length` -
  * Length Units `lengthunits` -

- Delay `delay` - ⊞ - (float) after Start, the delay before the timer begins counting.
  * Delay `delay` -
  * Delay Units `delayunits` -

- Run Values `runvalues` - ⊞ - On the frame that Start is triggered and the `running` channel goes from 0 to 1, this determines what the channels `timer_frames`, `timer_samples` and `timer_fraction` will be. If the menu is set to Zero, these channels will be 0 as they are when the timer is initialized. If set to One, on the first frame running is 1, `timer_frames` and `timer_samples` will be set to one frame, and `timer_fraction` will also have stepped forward by a frame.
  * Zero `zero` -
  * One `one` -

- Play `play` - (onoff) Pauses the timer. It is basically a 0 or 1 multiplier on the Speed.
- Speed `speed` - (default 1) Slows down or speeds up the timer.
- Cue `cue` - ⊞ - Freezes playing at the Cue Point.
  * Cue `cue` -
  * Cue Pulse `cuepulse` -

- Cue Point `cuepoint` - ⊞ - Time (Seconds, Frames or Fraction) which the cue point is frozen to.
  * Cue Point `cuepoint` -
  * Cue Units `cueunits` -

- Cycle `cycle` - (default Off) causes the timer to loop back to 0 when it reaches the end of the cycle.
- Cycle Limit `cyclelimit` - When the Cycle parameter is On, this determines if it will cycle indefinitely or cycle some maximum number of cycles.
- Maximum Cycles `maxcycles` - When Cycle is on and Cycle Limit is on, this sets the maximum number of cycles.
- Cycle End Alert `cycleendalert` - ⊞ - The number of seconds, frames or samples before a cycle, segment or done state is reached that the `onCycleEndAlert()` callback is called. This allows you to prepare for the next cycle, segment or timer.
  * Cycle End Alert `cycleendalert` -
  * Notify Units `notifyunits` -

- Exit Segment at End of Cycle `exitendcycle` - When pulsed, it will exit the cycle (and segment) at the end of the currently-playing cycle.
- Go to End of Cycle `gotoendcycle` - When pulsed, it will exit the cycle (and segment) immediately.
- Go to Done `gotodone` - Will immediately go to the Done state.
- On Done `ondone` - ⊞ - Determines which action to take when the timer gets to the end, ie "is done" or finished. Note there is also a onDone callback that can be used for customizing behavior.
  * Do Nothing `donothing` - No action taken.
  * Re-Initialize `reinit` - Will re-initialize the timer, this is the same as pulsing the Initialize parameter above.
  * Re-Start `restart` - Will re-initialize and re-start the timer, this is the same as pulsing the Start parameter above.
  * Re-Start without Initializing `restartnoinit` - Will re-star the timeer without re-initializing.

- Callbacks DAT `callbacks` - The path to the DAT containing callbacks for this Timer CHOP.
- Length Units `lengthunits` - ⊞ - Choose between using Samples, Frames, or Seconds as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Delay Units `delayunits` - ⊞ - Choose between using Samples, Frames, or Seconds as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Cue Pulse `cuepulse` - Jump instantly to the Cue Point.
- Cue Units `cueunits` - ⊞ - Choose between using Samples, Frames, Seconds, Fraction(0-1) as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -
  * % `fraction` -

- Notify Units `notifyunits` - ⊞ - Choose between using Samples, Frames, or Seconds as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

## Parameters - Segments Page
You can specify multiple timers in one Timer CHOP. A "segment" acts as one timer, with its own length, delay time, number of cycles to repeat and other conditions.
- Segments DAT `segdat` - A table DAT that contains one row per timer (segment). The column headings can be `delay` or `begin`, `length`, `cycle`, `cyclelimit`, `maxcycles` and `cycleendalert`, which override the equivalent parameters. (These are the internal names for the corresponding parameters.) `begin` is unique as it replaces `delay`, and it represents the time from Start that the timer will begin counting, whether the CHOP is set to Serial Timers or Parallel Timers (see Segment Method).
The Segments DAT also can include any number of custom columns. See Columns to Custom Channels and Columns to Info DAT below.
- Segment Method `segmethod` - ⊞ - If the Segment Method is **Serial Timers** , the timers will be played back-to-back. If the Segment Method is **Parallel Timers** , the timers can be played at the same time, and a set of channels will be output for each timer.
  * Serial Timers `serial` -
  * Parallel Timers `parallel` -

- Segment Units `segunits` - ⊞ - For the columns `delay`, `begin`, `length` and `cycleendalert`, you specify whether it’s seconds, frames or samples with this menu.
  * Samples `samples` -
  * Frames `frames` -
  * Seconds `seconds` -

- Segments End Time `segsendtime` - ⊞ - Describes how the end time is calculated.
  * From Segments DAT `dat` - The end time is based on the Segments DAT values.
  * From Length Parameter `par` - The end time is based on the Length parameter value.
  * Max of Parameter/Table `max` - The end time is based on the greater of the Length parameter value and the Segments DAT values.

- Columns to Custom Channels `channelcolumns` - Optional extra columns (any name) in the segments DAT can be output as extra channels (the columns must contain numbers). Specify their names in the Columns to Channels parameter. The channel name will be the column name. You can also output the `length`, `delay`, etc columns as channels.
- Custom Channel Interpolation `interpolation` - ⊞ - By default, custom channels step to their new value at the begin of the segment. This menu lets you interpolate to the new value linearly, or any combination of ease-in and ease-out.
  * Step to Value `steptovalue` -
  * Linear to Value `lineartovalue` -
  * Ease In to Value `easeintovalue` -
  * Ease Out to Value `easeouttovalue` -
  * Ease In-Out to Value `easeinouttovalue` -

- Columns to Info DAT `infocolumns` - Optional extra columns (any name) in the segments DAT can be output to the Info DAT (attach an Info DAT to the Timer CHOP) if you specify their names in this parameter.
- Go to Previous Segment `gotoprevseg` - (pulse) Jump to Previous Segment.
- Go to Next Segment `gotonextseg` - (pulse) Jump to Next Segment.
_Lingo_
  * Segment – each segment acts as one timer, with delay time, length, number of cycles to repeat and other conditions.
  * Begin – in Parallel Timers, the number of seconds after a Start (frames or samples) after which each timer starts counting up from zero.
  * Done – The state it goes into when all the timers has finished counting, whether they are in Parallel or Serial, Segments or not.
  * End – Cycle End is the end of each cycle, Segment End is the end of the segment.
  * Cumulative Time – Zero at Start, a count that is affected by speed and rises while timers are active (not during delays).
  * Running Time – Zero at Start, the wall-clock time since Start was called no matter what are the delays, speeds, cycles or premature clicking of Go To Segment End. It stops counting when Done has been reached.

## Parameters - Sub Range Page
Operate the timer within a sub range of the total length.
- Sub Range `subrange` - Turn this parameter on to limit the timer output to a subrange of the full length.
- Sub Start `substart` - ⊞ - The beginning point of the sub range.
  * Sub Start `substart` -
  * Sub Start Units `substartunits` -

- Sub End `subend` - ⊞ - The end point of the sub range.
  * Sub End `subend` -
  * Sub End Units `subendunits` -

- Sub End Action `subendaction` - ⊞ - Controls the behavior once the sub range end point is reached: Loop at End, or Pause at End.
  * Pause at End `pause` -
  * Loop at End `loop` -

- Sub Start Units `substartunits` - ⊞ - Choose between using Samples, Frames, or Seconds as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Sub End Units `subendunits` - ⊞ - Choose between using Samples, Frames, or Seconds as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

## Parameters - Outputs Page
- Timer Fraction `outfraction` - Outputs channel `timer_fraction` for each segment.
- Timer Count `outtimercount` - ⊞ - Outputs the elapsed Seconds channel as `timer_seconds`, Frames outputs channel as `timer_frames`, or Samples outputs channel as `timer_samples`. Because this is elapsed time, `timer_frames` starts at 0, as do the others.
  * Off `off` -
  * Samples `samples` -
  * Frames `frames` -
  * Seconds `seconds` -
  * All `all` -

- Timer Active `outtimeractive` - Outputs channel `timer_active` which is on only while the timer fraction is counting (is non-zero).
- Timer Pulse `outtimerpulse` - Outputs channel `timer_pulse` when the timer reaches its length.
- Delay Fraction `outdelayfraction` - Outputs a 0-1 fraction in `delay_fraction` while the delay occurs.
- Delay Count `outdelaycount` - ⊞ - Outputs the delay count in seconds, frames or samples.
  * Off `off` -
  * Samples `samples` -
  * Frames `frames` -
  * Seconds `seconds` -
  * All `all` -

- Initializing `outinit` - Outputs channel `initializing` = 1 while the timer is initalizing (i.e. while the callback `onInitialize()` returns non-zero).
- Ready `outready` - Outputs channel `ready` which is 1 after an Initialize and before a Start.
- Ready Pulse `outreadypulse` - Outputs a pulse when initialization has finished and the timer is ready to start. It pulses even when the timer starts rights away after an initialization.
- Running `outrunning` - Outputs channel `running` which is 1 after a Start and before the Done.
- Done `outdone` - Outputs channel `done` when done or complete.
- Done Pulse `outdonepulse` - Outputs channel `done` when the all timers have reached their completion.
- Cycles `outcycle` - Outputs channel `cycles`, which is the number of cycles completed (In a segment), starting with 0 during the entire first cycle. If you jump to Done, cycle is incremented as if it played normally to the done state.
- Cycle Pulse `outcyclepulse` - Outputs a pulse at the end of every cycle, even on the first and only cycle.
- Cycles + Fraction `outcycleplusfraction` - Outputs channel `cycle_plus_fraction`, starting with 0 for entire first cycle.
- Segment `outseg` - Outputs channel `segment`, starting with 0 for first segment.
- Segment Pulse `outsegpulse` - Outputs channel `segment_pulse` which is a pulse at the end of each segment.
- Segment + Fraction `outsegplusfraction` - Outputs channel `segment_plus_fraction`, starting with 0 for first segment ending at #segments at end.
- Length `outlength` - ⊞ - Outputs channel `length`, starting with 0 for first segment ending at #segments at end.
  * Off `off` -
  * Seconds `seconds` -
  * Frames `frames` -
  * Samples `samples` -
  * All `all` -

- Cumulative Timer Count `outcumulativecount` - ⊞ - Outputs `cumulative_seconds`, `cumulative_frames` or `cumulative_samples`. It is a time count that adds up all the Timer Active times for all segments since Start: it is affected by "Speed", and counts up only while `timer_active` (Play) is on. See the python member `.cumulativeSeconds`.
  * Off `off` -
  * Samples `samples` -
  * Frames `frames` -
  * Seconds `seconds` -
  * All `all` -

- Playing Timer Count `outplayingcount` - ⊞ - Outputs `playing_seconds`, `playing_frames` or `playing_samples`. It is a time count that adds up all the Timer Active times for all segments since Start: it is not affected by "Speed", and counts up only while `timer_active` and `play` is on. See the python member `.playingSeconds`.
  * Off `off` -
  * Seconds `seconds` -
  * Frames `frames` -
  * Samples `samples` -
  * All `all` -

- Running Time Count `outrunningcount` - ⊞ - Outputs the "wall-clock" time since Start occurred, no matter what are the delays, speeds, cycles or pre-mature clicking of Go To Segment End, etc. It stops counting when Done has been reached. `running_seconds`, `running_frames`, or `running_samples`. When CHOP is set to Parallel Timers, this will output a channel per segment plus one global running time channel. See the python member `.runningSeconds`.
  * Off `off` -
  * Samples `samples` -
  * Frames `frames` -
  * Seconds `seconds` -
  * All `all` -

- Master Time Count `outmastercount` - ⊞ - Outputs `master_seconds`, `master_frames` or `master_samples`. It is a time count that adds up all the Timer Active times for all segments since Start: it is affected by "Speed", and counts up only while `timer_active` and `play` is on. It also includes any delay times. See the python member `.masterSeconds`.
  * Off `off` -
  * Seconds `seconds` -
  * Frames `frames` -
  * Samples `samples` -
  * All `all` -

## Parameters - External Page
- External CHOP `extchop` - The CHOP used to control the current point in the timer.
- External Units `extunits` - ⊞ - Choose between using Samples, Frames, or Seconds as the units for this parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -
  * % `fraction` -

- External Channel `extchannel` - The channel that will control the current point of the timer.
- External Timecode Object/CHOP/DAT `exttcop` - Time is specified using a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.
- External Start Offset `extstartoff` - Specifies the external time at which the timer should start.
- External Initialize Offset `extinitoff` - Specifies the external time at which the timer should initialize.
- Sample Rate `rate` - The sample rate that the CHOP outputs at, which is also used when the units of Length, Delay and Cycle End Alert time are set to Samples. The default sample rate is 60 samples per second.
- External Timecode Object `exttcobj` - Time is specified using a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.

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
Extra Information for the Timer CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Timer CHOP Info Channels
  * frames_timer -

  * frames_segment -

  * frames_cumulative -

  * frames_running -

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
