---
url: https://docs.derivative.ca/Audio_File_Out_CHOP
category: CHOPs
title: Audio_File_Out_CHOP
---

# Audio File Out CHOP
## Summary

The Audio File Out CHOP saves an audio stream out to a file using a variety of different codecs.
Currently supports **.wav** , **.mp3** , **.aiff** , and **.ogg** container formats.
See also: [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP").
[audiofileoutCHOP_Class](https://docs.derivative.ca/AudiofileoutCHOP_Class "AudiofileoutCHOP Class")

## Parameters - Audio File Out Page
- File Type `filetype` - ⊞ - Select the file type (container) of the output file.
  * WAV `wav` - .wav file type. The audio codec can be chosen using the Codec parameter.
  * OGG `ogg` - .ogg file type. The audio codec is Vorbis. Vorbis compression will have gapless playback.
  * MP3 `mp3` - .mp3 file type. The audio codec is MP3. MP3 compression will not have gapless playback. Vorbis (.ogg) is a good alternative for this.
  * AIFF `aiff` - .aiff file type. The audio codec is Uncompressed 16-bit (PCM).

- Unique Suffix `uniquesuff` - When enabled, me.fileSuffix will be a unique suffix when used in the file parameter.
- N `n` - When unique suffix is disabled, me.fileSuffix will simply contain the value of N, instead of being unique
- File `file` - Sets the path and filename of the audio file that is saved out. The file extension must match the file type parameter.
- Codec `codec` - ⊞ - Select the compression codec when outputting WAV or AIFF file types. When using AIFF, Big Endian options are available, these are the industry standard when working with AIFF files.
  * Uncompressed 16-bit (PCM) `pcm16` - Uncompressed audio (Pulse Code Modulation)
  * Uncompressed 24-bit (PCM) `pcm24` - Uncompressed audio (Pulse Code Modulation)
  * Uncompressed 32-bit (PCM) `pcm32` - Uncompressed audio (Pulse Code Modulation)

- Bit Rate `bitrate` - ⊞ - Selects the bit rate for the MP3 file type.
  * 96 kb/s `b96` -
  * 128 kb/s `b128` -
  * 192 kb/s `b192` -
  * 256 kb/s `b256` -
  * 320 kb/s `b320` -

- Record `record` - When toggled on, it will open the audio file and begin recording. When toggled off, it will close the file and release the read/write lock.
- Pause `pause` - Pauses the recording of the audio to the audio file.
- Header Source DAT `headerdat` - The path to a Table DAT that stores header metadata that should be written to the output image or movie file. Header data is written as key-value pairs with the first column storing the keys and the second column storing the associated values. See File Metadata for more information on supported metadata.

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
Extra Information for the Audio File Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio File Out CHOP Info Channels
  * last_samples_written -

  * total_samples_written -

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
