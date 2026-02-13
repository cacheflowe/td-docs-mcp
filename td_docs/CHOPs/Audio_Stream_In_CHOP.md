---
url: https://docs.derivative.ca/Audio_Stream_In_CHOP
category: CHOPs
title: Audio_Stream_In_CHOP
---

# Audio Stream In CHOP
## Summary

The Audio Stream In CHOP can stream audio into TouchDesigner from any [rtsp](http://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol) server, or from a [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") peer. See [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP").
[audiostreaminCHOP_Class](https://docs.derivative.ca/AudiostreaminCHOP_Class "AudiostreaminCHOP Class")

## Parameters - Audio Stream In Page
- Source Type `srctype` - ⊞ - Select the source type: either from a server URL, or a WebRTC peer.
  * Server `server` - Server source type for RTSP.
  * WebRTC `webrtc` - WebRTC peer source.

- Server URL `url` - The URL address of the stream. E.g rtsp://localhost:554/tdaudio
- Video Stream In TOP `videostreamintop` - Point to a [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP") whose stream has audio embedded to extract the audio channels.
- Play `play` - Turns the audio streaming on (1) or off (0).
- Open Timeout `opentimeout` - The time (in milliseconds) TouchDesigner will wait attempting to open the audio stream.
- Audio Sync Offset `syncoffset` - Offsets the audio playback of the movie. This can be used to get better sync between the audio and images in the stream when there is audio latency in the system (For example, audio latency from the [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP") queue). A negative value plays audio that amount of time sooner, to counteract delay introduced by buffering such as in [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP").
- Audio Sync Offset Unit `syncoffsetunit` - ⊞ - Specify which units to use for the Audio Sync Offset parameter.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Volume `volume` - 0 = mute, 1 = full volume.

## Parameters - WebRTC Page
- WebRTC DAT `webrtc` - Set the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") (ie. peer) to get the audio stream from. Setting this will automatically populate the WebRTC Connection parameter menu with available connections.
- WebRTC Connection `webrtcconnection` - Select the [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") peer-to-peer connection. Selecting this will automatically population the WebRTC Track parameter menu with available audio input tracks.
- WebRTC Track `webrtctrack` - Select the audio input track that's a part of the WebRTC peer-to-peer connection.

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
Extra Information for the Audio Stream In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio Stream In CHOP Info Channels
  * sample -

  * true_sample -

  * seconds -

  * fraction -

  * file_length -

  * true_file_length -

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
