---
url: https://docs.derivative.ca/LTC_Out_CHOP
category: CHOPs
title: LTC_Out_CHOP
---

# LTC Out CHOP
## Summary

The LTC Out CHOP outputs "linear timecode" which is a SMPTE timecode data encoded into an audio signal. See also [Linear Timecode](http://en.wikipedia.org/wiki/Linear_timecode).
Use an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") to determine which values are currently being output.
The output of this CHOP can be sent to an [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP").
See also: [LTC In CHOP](https://docs.derivative.ca/LTC_In_CHOP "LTC In CHOP")
[ltcoutCHOP_Class](https://docs.derivative.ca/LtcoutCHOP_Class "LtcoutCHOP Class")

## Parameters - LTC Page
- Play Mode `playmode` - ⊞ - Specifies the method used to output LTC, there are 2 options.
  * Sequential `sequential` - This mode continually plays forward.
  * Timecode Object/CHOP/DAT `timecodeop` - This mode allows the user to set the LTC value by reference to a timecode in the form of either a CHOP, DAT, or [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.

- Play `play` - Specifies whether the count should increment or hold steady.
- Cue `cue` - While set to on, the output is held at the specified initial values below.
- Cue Pulse `cuepulse` - When pulsed, the output is set to the initial values below.
- Frame `frame` - The initial frame to count from.
- Second `second` - The initial second to count from.
- Minute `minute` - The initial minute to count from.
- Hour `hour` - The initial hour to count from.
- Frame Rate `framerate` - The number of complete frame messages per second the signal encodes. It is usually between 24 and 30. Note that although we support framerates above 30, using custom usage of the User Bits 1 field, the generated LTC signal is non-standard and will likely not be readable by other software or devices. LTC is limited to 30fps when following the standard.
- Drop Frame Numbering `dropframe` - Drop frame numbering converts 30 fps time code to the 29.97 fps NTSC standard. Frame numbers 0 and 1 are skipped during the first second of every minute, except multiples of 10 minutes.
- High FPS Behaviour `highfpsbehaviour` - ⊞ - Specifies the method for counting frame numbers when the set frame rate is higher than the LTC frame rate. Menu enabled only when the set frame rate is a multiple of the LTC frame rate. This menu has 2 options.
  * Cycle Frames `cycleframes` - This mode loops the LTC frame count until the end of each FPS cycle
  * Duplicate Frames `duplicateframes` - This mode repeats each individual LTC frame count in multiples until the end of each FPS cycle

- Timecode Object/CHOP/DAT `timecodeop` - Set the LTC output value with a reference to a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.
- Audio Rate `audiorate` - This audio sampling rate of the output signal.

## Parameters - User Page
User Data bits in LTC are reversed for transmitting of custom user data in the time code signal. This is often used for reel number and date but can be used for anything.
- User Data 1 `user1` - Send this value in the bits reserved for User Data 1.
- User Data 2 `user2` - Send this value in the bits reserved for User Data 2.
- User Data 3 `user3` - Send this value in the bits reserved for User Data 3.
- User Data 4 `user4` - Send this value in the bits reserved for User Data 4.
- User Data 5 `user5` - Send this value in the bits reserved for User Data 5.
- User Data 6 `user6` - Send this value in the bits reserved for User Data 6.
- User Data 7 `user7` - Send this value in the bits reserved for User Data 7.
- User Data 8 `user8` - Send this value in the bits reserved for User Data 8.

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
Extra Information for the LTC Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific LTC Out CHOP Info Channels
  * ltc_frame -

  * ltc_second -

  * ltc_minute -

  * ltc_hour -

  * ltc_message_rate -

  * ltc_message_rate_df -

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
