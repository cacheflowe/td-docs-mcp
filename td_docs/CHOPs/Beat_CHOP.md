---
url: https://docs.derivative.ca/Beat_CHOP
category: CHOPs
title: Beat_CHOP
---

# Beat CHOP
## Summary

The Beat CHOP generates a variety of ramps, pulses and counters that are timed to the beats per minute and the sync as produced by the [Beat Dialog](https://docs.derivative.ca/Beat_Dialog "Beat Dialog").
  * You can generate a ramp every 1/4 1/2 1 2 4 8 32 beats.
  * You can generate ramps of any other length, like 12 beats per bar (ramp) and fractional beats like 3.33 beats per ramp.
  * You can generate a set of channels, where each channel is delayed relative to the prior channel. This is useful, for example, for moving eight objects delayed by one beat each.
  * There also is a counter of how many ramps it has generated.
  * The Count+Ramp type generates a continuously-rising ramp equal to the number of cycles since the start.
  * If Play Mode is set to Local Sequential, it doesn't look at start/end of the timeline (i.e. doesn't reset when the timeline loops), so is more appropriate for long improvised playing.

**Note:** for the purposes of this dialog, a _bar_ is 4 beats and the _period_ is the number of beats set by the Period parameter.
The [Beat Dialog](https://docs.derivative.ca/Beat_Dialog "Beat Dialog") is used to manually tap the beat to set the beats-per-minute (BPM). The Beat CHOP converts the BPM into a repeating ramp or pulse that keeps time with the music after you stop tapping.
You can set the global beats-per-minute with the python command: `op('/local/time').tempo = 140`
The phase can be controlled with the Beat CHOP's Reset parameters.
The Beat CHOP's timing is defined by the [Component Time](https://docs.derivative.ca/Component_Time "Component Time") of the Reference Node. If the Reference Node parameter is left blank, then the time defined at the Beat CHOP's location is used. The default is in `/local/time`.
See also: [Timeline CHOP](https://docs.derivative.ca/Timeline_CHOP "Timeline CHOP"), [Time COMP](https://docs.derivative.ca/Time_COMP "Time COMP").
[beatCHOP_Class](https://docs.derivative.ca/BeatCHOP_Class "BeatCHOP Class")

## Parameters - Beat Page
- Reference Operator `op` - This node is used to specify the time settings referenced by the Beat CHOP. The time is defined by the Time COMP found at `timepath("_reference_node_")`
- Use Reference Time Slice `reftimeslice` - Turn on this checkbox to use the [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing") used by the Reference Node.
- Play Mode `playmode` - ⊞ - Specifies the method used to playback the output.
  * Locked to Timeline `locked` - This mode locks the output to the local component [Timeline](https://docs.derivative.ca/Timeline "Timeline"). Scrubbing or jumping in the local time will update the output accordingly. When the local timeline loops the output is reset and starts over. The output will be the same for each pass through the local timeline.
  * Locked to Global `global` - This mode locks the output to the Global beat source. It will follow the Beat CHOP with whose 'Update Global' flag is turned on.
  * Local Sequential `local` - This mode produces a continuous output regardless of the timeline position.

- Period `period` - Number of beats it takes to generate one cycle of ramp. Use the drop down menu to select from some commonly used Period lengths.
- Multiples `multiples` - The number of channels to create.
- Shift Offset `shiftoffset` - Delays all channels by this amount. 0 = no change, .5 means 50% of one period later.
- Shift Step `shiftstep` - When set to 1, and Multiples is 5, each ramp channel is 1/5 cycle later than the previous channel. When set to .1, the delay is 1/50 cycle. This is a way to stagger the channels.
- Random Offset `randoffset` - The amount that each ramp is randomly time-shifted relative to a perfect ramp.
- Random Seed `randseed` - Changing this generates a different set of random offsets.
- Reset Condition `resetcondition` - ⊞ - This menu determines how the Reset input triggers a reset of the channel(s).
  * Off to On `offtoon` - Channels are reset when the Reset input goes off to on.
  * While On `on` - Channels are reset when the Reset input goes on. The channel will hold the reset value until the input turns off.
  * On to Off `ontooff` - Channels are reset when the Reset input goes on to off.
  * While Off `off` - Channels are reset when the Reset input goes off. The channel will hold the reset value until the input turns on.

- Reset Bar Value `resetbarvalue` - Specifies which Bar the Beat CHOP will jump to when the Reset Condition is met. Beat values are derived from the fractional part of this value.
- Wait after Reset `resetwait` - When using the **While On** Reset Condition, Wait After Reset will hold the channels at zero until the next bar is started, after which the output will continue. When Wait After Reset is off, the channels will restart output as soon as the reset condition is done.
- Reset `reset` - This button resets the ramps to zero when On. The ramp is also zero when the Beat CHOP's input is above 0.
- Reset Pulse `resetpulse` - Instantly resets the ramps to zero.
- Update Global `updateglobal` - Any Beat CHOP can be made the "global beat source" by turning on Update Global. A reference Beat CHOP is created at /local/master_beat (if it doesn't already exist) and all Beat CHOPs can synchronize to this by setting 'Play Mode: Locked to Global'. That master Beat CHOP also needs 'Update Global' turned on, if not already on. This means you require exactly one master Beat CHOP per toe. You can turn switch back to 'Play Mode: Locked to Sequential' when desired. $MASTER_BEAT is set to whatever Beat CHOP has this option turned on.

## Parameters - Output Page
- Ramp `ramp` - Outputs a 0-1 ramp each period.
- Pulse `pulse` - Outputs a pulse each period.
- Sine `sine` - Outputs a sine wave each period.
- Count `count` - Increases the count each period.
- Count+Ramp `countramp` - A ramp that counts up until the bar is reset.
- Bar `bar` - Output the current bar.
- Beat `beat` - Output the current beat.
- Sixteenths `sixteenths` - Output the current sixteenths.
- Ramp Bar `rampbar` - Outputs a 0-1 ramp each bar.
- Ramp Beat `rampbeat` - Outputs a 0-1 ramp each beat.
- BPM `bpm` - Outputs the current BPM.

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
Extra Information for the Beat CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
