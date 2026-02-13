---
url: https://docs.derivative.ca/Sequencer_CHOP
category: CHOPs
title: Sequencer_CHOP
---

# Sequencer CHOP
## Summary

**NOTE** : **The[Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP") replaces the Sequencer CHOP**. Sequencer CHOP has been removed (it will still work in existing files). See the [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP") examples in the OP Snippets (Help -> Operator Snippets). The Timer CHOP is an engine for running timed processes. It outputs channels such as timing fractions, counters, pulses and timer states, and it calls python functions (callbacks) on various timing events.
[sequencerCHOP_Class](https://docs.derivative.ca/SequencerCHOP_Class "SequencerCHOP Class")

## Parameters - Sequencer Page
- DAT List `datlist` - The table of CHOPs to sequence, the table contains the paths to the CHOPs to be sequenced.
- Blend Scope `blendscope` - Specifies which channels should blend between transitions, otherwise they add or jump.
- Add Scope `addscope` - Specifies which channels should add during transitions, otherwise they blend or jump.
- Queue `queue` - Specifies the channel that controls when to queue (pause).
- Trigger `trigger` - Begin transitioning immediately, instead of waiting until the end of the current CHOP channels.
- Reset `reset` - While On, resets the sequence to the default CHOP.
- Reset Pulse `resetpulse` - Instantly resets the sequence.

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

## Info CHOP Channels
Extra Information for the Sequencer CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
