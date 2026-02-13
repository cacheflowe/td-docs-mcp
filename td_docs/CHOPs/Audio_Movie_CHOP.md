---
url: https://docs.derivative.ca/Audio_Movie_CHOP
category: CHOPs
title: Audio_Movie_CHOP
---

# Audio Movie CHOP
## Summary

The Audio Movie CHOP plays the audio of a movie file that is played back with a [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP"). Use the Movie File In TOP parameter to specify which Movie File In TOP to get the audio signal from.
[audiomovieCHOP_Class](https://docs.derivative.ca/AudiomovieCHOP_Class "AudiomovieCHOP Class")

## Parameters - Movie Audio Page
- Play `play` - Audio playback is enabled when this is set to On. No audio output when Off.
- Movie File In TOP `moviefileintop` - Put the path of a Movie File In TOP in this parameter. The file named in the Movie File In TOP will be the source for the audio.
- Pre-Read Length `prereadlength` - Use to read-ahead the audio into cache. You can specify in samples, frames and in seconds using the Units menu.
- Pre-Read Length Unit `prereadlengthunit` - Specify which units to use for the Pre-Read Length parameter.
- Open Timeout `opentimeout` - The amount of time TouchDesigner will wait for the audio samples to be read from the movie file. On file opening, if this timeout period is reached and the read-ahead has not finished, the audio will be output as zeros until all the pre-read samples have been read from the file.
- Audio Sync Offset `syncoffset` - Offsets the audio playback of the movie. This can be used to get better sync between the audio and images in the movie when there is audio latency in the system (For example, audio latency from the [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP") queue). A negative value plays audio that amount of time sooner, to counteract delay introduced by buffering such as in [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP").
- Audio Sync Offset Unit `syncoffsetunit` - Specify which units to use for the Audio Sync Offset parameter.
- Index Channel `index` - Turn this parameter On to output an additional channel which reports the current position in the movie ie. 0 = start, 1 = end.
- Audio Track Index `audiotrack` - When the movie has multiple audio tracks available this parameter can select between them.
