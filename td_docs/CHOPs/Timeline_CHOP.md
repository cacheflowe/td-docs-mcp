---
url: https://docs.derivative.ca/Timeline_CHOP
category: CHOPs
title: Timeline_CHOP
---

# Timeline CHOP
## Summary

The Timeline CHOP outputs time-based CHOP channels for a specific component. The time channels are defined by a [Time Component](https://docs.derivative.ca/Time_COMP "Time COMP") whose [Path](https://docs.derivative.ca/Network_Path "Network Path") can be determined using the python expression `me.time`. When a **Reference Node** is specified, the time defined at that node is used. When the Reference Node is not specified, then the time defined at the Timeline CHOP's location is used (ie. time defined at `me.time`).
[timelineCHOP_Class](https://docs.derivative.ca/TimelineCHOP_Class "TimelineCHOP Class")

## Parameters - Timeline Page
- Reference Operator `op` - This node is used to specify the time referenced by the Timeline CHOP. The time is defined by the Time COMP found at `me.time`
- Use Timecode `usetimecode` - When enabled, the CHOP will get its time from a timecode reference, rather than the Reference Operator. The Reference Operator will still be used for bpm, time signature, start, and end values.
- Timecode Object/CHOP/DAT `timecodeop` - Reference a timecode that sets the time. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object. The Reference Operator will still be used to get bpm, time signature, start, and end values.
- Frame `frame` - Output a channel for frame number.
- Rate `rate` - Output a channel for the rate (frames per second).
- Start `start` - Output a channel with the Start frame value.
- End `end` - Output a channel with the End frame value.
- Range Start `rangestart` - Output a channel with the Range Start frame value.
- Range End `rangeend` - Output a channel with the Range End frame value.
- Signature 1 `signature1` - Output a channel for the first number in the timing signature, how many beats are in a measure.
- Signature 2 `signature2` - Output a channel for the second number in the timing signature, which kind of note constitutes one beat.
- BPM `bpm` - Output a channel with the BPM value.
- Play `play` - Output a channel with the current play state.

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
Extra Information for the Timeline CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
