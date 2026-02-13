---
url: https://docs.derivative.ca/Audio_Play_CHOP
category: CHOPs
title: Audio_Play_CHOP
---

# Audio Play CHOP
## Summary

The Audio Play CHOP plays back a sound file through any attached audio output device using DirectSound. It supports `.aif`, `.mp3`, `.mid`, `.wav` and `.m4a` files up to 48.000 kHz, which can have mono, stereo or even up to 5.1 channels in them. The audio channels can then be routed to any speaker location that DirectSound uses. See Outputs section below.
**NOTE** : With the Audio Play CHOP, audio samples do not enter or pass through TouchDesigner, so you will not see them in CHOPs, and you cannot process them in CHOPs. The Audio Play CHOP starts an external process that opens the file and sends it directly to the the audio outputs of your computer. If you want to process the audio within TouchDesigner or output them into a [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP") or [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP"), use the [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP").
The Audio Play CHOP contains a channel called _state_. This channel is 1 whenever any file is being played, 0 otherwise.
The first input (Input 0:Triggers) is used to trigger the audio file to play. The second input (Input 1: Volume) can be used to control volume, if no input is connected the Volume parameter will be used. The third input (Input 2: Pan) is for panning, no input assumes it is centered. When using the DAT List parameter, the inputs can contain mulitiple channels to manipulate each file individually. Multiple Audio Play CHOPs can output to different devices simutaneously.
It can also be triggered by the Trigger parameter below, but in this case if multiple files are specified via the DAT List, then all files will be played at the same time when triggered.
Sound files can also be triggered through the `play()` method [audioplayCHOP_Class](https://docs.derivative.ca/AudioplayCHOP_Class "AudioplayCHOP Class"). Some advanced options are only available through the [audioplayCHOP_Class](https://docs.derivative.ca/AudioplayCHOP_Class "AudioplayCHOP Class").
The file can be read in from disk or from the web. Use `http://` when specifying a URL.
[audioplayCHOP_Class](https://docs.derivative.ca/AudioplayCHOP_Class "AudioplayCHOP Class")

## Parameters - AudioPlay Page
- Device `device` - A menu of available audio devices to output to. Selecting _default_ sets the audio device to that which is selected in Windows Control Panel>Sound>Playback.
- Outputs `outputs` -
- Sound File `file` - `.aif`, `.mp3`, `.mid`, `.wav` or `.m4a` audio file. The file can be mono or stereo.
- DAT List `datlist` - Links to a [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") which can be used as list of audio files to choose from. When using the DAT List, the first input (Input 0: Triggers) on the CHOP can contain mulitiple channels to fire the files in the list individually. Using the `audioplay` command the index can be specified directly.
- Volume `volume` - 0 = mute, 1 = full volume. Using the second input (Input 1: Volume) or the python `.play(volume=_val_)`method, will override the value of this parameter.
- Mode `mode` - ⊞ - Determines how the audio is triggered when using the first input to trigger.
  * Play While On `on` - Plays while input is 1.
  * Trigger `trigger` - Triggers once when input goes to 1.
  * Loop `loop` - Plays and loops when input goes to 1.

- Trigger `trigger` - Triggers the audio to play.
- Cook Every Frame `cookalways` - Forces CHOP to cook every frame.

## Parameters - Output 1 Page
- Stereo Mode `stereo` - Sets output to just 2 channels, front left and front right.
Outputs - The outputs on this page and the following Output 2 page are for routing to an audio device's different speaker outputs. Not all devices will support all outputs. For each speaker output, you can route any of the file's channels to play through it. For example, you can easily output the front left channel of the file to the all the front left speaker outputs, or you could output the front left channel to both front and rear speaker outputs. The value of each output parameter determines which channel from the file it plays, see below.
**File's channel mapping for outputs**
  * -1 - no audio plays through this output
  * 0 - File's front left channel will play
  * 1 - File's front right channel will play
  * 2 - File's rear left channel will play
  * 3 - File's rear right channel will play
  * 4 - File's center channel will play
  * 5 - File's sub or low frequency channel will play

The following speaker outputs are found on this parameter page.
- Front Left `frontleft` - Play audio on this output based on mapping table above.
- Front Right `frontright` - Play audio on this output based on mapping table above.
- Front Center `frontcenter` - Play audio on this output based on mapping table above.
- Low Frequency `lowfrequency` - Play audio on this output based on mapping table above.
- Back Left `backleft` - Play audio on this output based on mapping table above.
- Back Right `backright` - Play audio on this output based on mapping table above.
- Front Left of Center `frontleftcenter` - Play audio on this output based on mapping table above.
- Front Right of Center `frontrightcenter` - Play audio on this output based on mapping table above.
- Back Center `backcenter` - Play audio on this output based on mapping table above.

## Parameters - Output 2 Page
The following speaker outputs are found on this parameter page.
- Side Left `sideleft` - Play audio on this output based on mapping table above.
- Side Right `sideright` - Play audio on this output based on mapping table above.
- Top Center `topcenter` - Play audio on this output based on mapping table above.
- Top Front Left `topfrontleft` - Play audio on this output based on mapping table above.
- Top Front Center `topfrontcenter` - Play audio on this output based on mapping table above.
- Top Front Right `topfrontright` - Play audio on this output based on mapping table above.
- Top Back Left `topbackleft` - Play audio on this output based on mapping table above.
- Top Back Center `topbackcenter` - Play audio on this output based on mapping table above.
- Top Back Right `topbackright` - Play audio on this output based on mapping table above.

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
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Audio Play CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio Play CHOP Info Channels
  * device_default -

  * sample_state0 -

  * sample_time0 -

  * sample_length0 -

  * sample_channels0 -

  * queue_read_pos0 -

  * queue_write_pos0 -

  * queue_length0 -

  * sample_name0_Notify -

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
