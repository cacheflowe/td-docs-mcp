---
url: https://docs.derivative.ca/Audio_File_In_CHOP
category: CHOPs
title: Audio_File_In_CHOP
---

# Audio File In CHOP
## Summary

The Audio File In CHOP reads audio from files on disk or at `http://` addresses. File types `.mp3`, `.aif`, `.aiff`, `.au`, and `.wav` files are supported. It always outputs time sliced audio data. If you want to record the data, use a [Record CHOP](https://docs.derivative.ca/Record_CHOP "Record CHOP") or [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP").
See [Audio Movie CHOP](https://docs.derivative.ca/Audio_Movie_CHOP "Audio Movie CHOP") for reading from movie files. See [OSC In CHOP](https://docs.derivative.ca/OSC_In_CHOP "OSC In CHOP") for receiving audio streams via OSC.
For large files the Audio File In CHOP streams the file from disk so loading the entire file into memory is not needed.
  * It streams files from disk and from `http:` locations (latter copies to local disk first) - It only keeps a few seconds in memory at a time.
  * The supported audio files are `.mp3 .aif .aiff .wav` and other [audio formats](https://docs.derivative.ca/File_Types "File Types").
  * It also plays audio-only from any movie files that TouchDesigner supports, like `.mov, .mpg .mp4`. See also the [Audio Movie CHOP](https://docs.derivative.ca/Audio_Movie_CHOP "Audio Movie CHOP") for playing audio from movie files in sync with their video.
  * Audio files can be dragged/dropped onto TouchDesigner, double-clicked (if preferred), and RMB Open With... TouchDesigner.

[audiofileinCHOP_Class](https://docs.derivative.ca/AudiofileinCHOP_Class "AudiofileinCHOP Class")

## Parameters - Audio File In Page
- File `file` - Path of source.
- Reload `reloadpulse` - Instantly reload the file from disk.
- Play `play` - Audio will playback when this is set to 1 and stop when set to 0.
- Play Mode `playmode` - ⊞ - Specifies the method used to playback the audio, there are 3 options.
  * Locked to Timeline `locked` - This mode locks the playback position to the timeline. Scrubbing or jumping in the timeline will change the song position accordingly. The parameters Play, Reset, Speed, and Index are disabled in this mode since the timeline is directly tied to playback position.
  * Specify Index `specify` - This mode allows the user to specify a particular position in the song using the Index parameter below. Use this mode for random access to any location in the audio stream.
  * Sequential `sequential` - This mode continually plays regardless of the timeline position (the Index parameter is disabled). Reset and Speed parameters below are enabled to allow some control.
  * Timecode Object/CHOP/DAT `timecodeop` - This mode allows the user to set the movie index by reference to a timecode in the form of either a CHOP, DAT, or [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.

- Speed `speed` - This is a speed multiplier which only works when Play Mode is _Sequential_. A value of 1 is the default playback speed. A value of 2 is double speed, 0.5 is half speed and so on. This node can not play audio backwards so negative values will not work well.
- Cue `cue` - Jumps to Cue Point when set to 1. Only available when Play Mode is Sequential.
- Cue Pulse `cuepulse` - Instantly jumps to the Cue Point.
- Cue Point `cuepoint` - Set any index in the song as a point to jump to.
- Cue Point Unit `cuepointunit` - Units used when setting the Cue Point parameter.
- Index `index` - This parameter explicitly sets the song position when Play Mode is set to Specify Index. The units menu on the right lets you specify the index in the following units: Index, Frames, or Seconds.
- Index Unit `indexunit` - Units used for the Index parameter.
- Timecode Object/CHOP/DAT `timecodeop` - Set the audio file index with a reference to a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.
- Repeat `repeat` - ⊞ - Repeats the audio stream when the end is reached.
  * Off `off` -
  * On `on` -

- Trim `trim` - Enables the Trim parameters below.
- Trim Start `trimstart` - Sets an **In** point from the beginning of the audio, allowing you to trim the starting position of the audio stream. The units menu on the right let you specify this position by index, frames, or seconds.
- Trim Start Unit `trimstartunit` - Units used for the Trim Start parameter.
- Trim End `trimend` - Sets an **Out** point from the end of the audio, allowing you to trim the ending position of the audio stream. The units menu on the right let you specify this position by index, frames, or seconds.
- Trim End Unit `trimendunit` - Units used for the Trim End parameter.
- Pre-Read Length `prereadlength` - The amount of audio to buffer to maintain smooth playback. This will slightly impact memory usage, but does **not** create any delay in the audio.
- Pre-Read Length Unit `prereadlengthunit` - Units used for the Pre-Read Length parameter.
- Open Timeout `opentimeout` - The time (in milliseconds) TouchDesigner will wait for the audio file to open. If the Open Timeout time is reached, the Audio File In CHOP will stop waiting, and play silence. If the file still isn't opened the next time the CHOP cooks, it'll wait again, and do the same. It'll keep doing this until the file is opened, or the open fails.
- Mono `mono` - Output mono channel only even if file has multiple channels.
- Volume `volume` - Set the level the file is read in at. A setting of 1 is full signal while 0 is muted.

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
Extra Information for the Audio File In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio File In CHOP Info Channels
  * sample -

  * true_sample -

  * fraction -

  * file_length -

  * file_length_frames -

  * true_file_length -

  * true_file_length_frames -

  * open -

  * opening -

  * open_failed -

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
