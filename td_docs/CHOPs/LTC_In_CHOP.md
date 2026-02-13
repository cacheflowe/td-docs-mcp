---
url: https://docs.derivative.ca/LTC_In_CHOP
category: CHOPs
title: LTC_In_CHOP
---

# LTC In CHOP
## Summary

The LTC In CHOP reads SMPTE timecode data encoded into an audio signal. Read the wikipedia overview [Linear Timecode](http://en.wikipedia.org/wiki/Linear_timecode).
First bring the audio signal into CHOPs using an [Audio Device In CHOP](https://docs.derivative.ca/Audio_Device_In_CHOP "Audio Device In CHOP"). This can then be input into the LTC In CHOP.
See [Timecode](https://docs.derivative.ca/Timecode "Timecode") for the full integration of timecode in TouchDesigner.
See also: [LTC Out CHOP](https://docs.derivative.ca/LTC_Out_CHOP "LTC Out CHOP")
[ltcinCHOP_Class](https://docs.derivative.ca/LtcinCHOP_Class "LtcinCHOP Class")

## Parameters - LTC Page
- Input Frame Rate `inputrate` - This specifies the number of complete frame messages per second the signal encodes. It is usually between 24 and 30.
- Discrete Channels `discrete` - When enabled, adds frame, second, minute, and hour channels will be added to the output.
- Total LTC Frames `totalframes` - When enabled, adds a channel to the output that reports total elapsed LTC frames at the current time. This value will change if up-sampling to the timeline FPS.
- Total Seconds `totalsec` - When enabled, adds a channel to the output that reports total elapsed seconds.
- Up-sample to Timeline FPS `upsample` - Resamples up to the project's FPS.
- User Fields `userfields` - This enables channels for custom user fields which may be encoded in the audio signal.
- Debug Channels `debugchans` - This enables the following debug channels.
  * quantized - Outputs the raw signal quantized to on and off levels.
  * bits - Outputs the above quantized signal into decoded bits. (Note: Bits are decoded from specific edge sequences, not the raw levels themselves).
  * ones_count - Outputs the total number of consecutive decoded one bits. (Note, 12 consecutive ones denotes an end of message).
  * decode_count - Outputs the total number of successful decoded frame messages.

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
Extra Information for the LTC In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
