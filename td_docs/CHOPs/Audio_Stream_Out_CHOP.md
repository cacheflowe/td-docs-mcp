---
url: https://docs.derivative.ca/Audio_Stream_Out_CHOP
category: CHOPs
title: Audio_Stream_Out_CHOP
---

# Audio Stream Out CHOP
## Summary

The Audio Stream Out CHOP can stream audio out to any [rtsp](http://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol) client such as VideoLAN's VLC media player and Apple's Quicktime, or to a [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") peer.
To access the stream in one of these players, open a "Network Stream" or "URL" under the File menu.

Below is an example of a URL used to access the stream in a rtsp client.
  * IP Address = IP address of computer running TouchDesigner with the Audio Stream Out CHOP.
  * Port = number set in the Port parameter.
  * Stream Name = name given to stream in the Stream Name parameter.

The URL required is rtsp://<_IP address_ >:<_Port_ >/<_Stream Name_ >
[audiostreamoutCHOP_Class](https://docs.derivative.ca/AudiostreamoutCHOP_Class "AudiostreamoutCHOP Class")

## Parameters - Audio Stream Out Page
- Active `active` - Toggle's the rtsp server on or off.
- Mode `mode` - ⊞ - Select the stream out mode: either [RTSP](https://docs.derivative.ca/RTSP "RTSP") or [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC").
  * RTSP `rtsp` -
  * WebRTC `webrtc` -

- Port `port` - Port number used to transmit the audio stream. This number is needed in the URL supplied to the client receiving the stream. See example in Summary at top.
- Stream Name `streamname` - Name assigned to the stream. This stream name is needed in the URL supplied to the client receiving the stream. See example in Summary at top.

## Parameters - WebRTC Page
- WebRTC `webrtc` - Set the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") (ie. peer) to send the audio stream over. Setting this will automatically populate the WebRTC Connection parameter menu with available connections.
- WebRTC Connection `webrtcconnection` - Select the [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") peer-to-peer connection. Selecting this will automatically population the WebRTC Track parameter menu with available audio output tracks.
- WebRTC Track `webrtctrack` - Select the audio output track that's a part of the WebRTC peer-to-peer connection. The audio stream will be sent over this track.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Audio Stream Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio Stream Out CHOP Info Channels
  * packet_loss_ratio -

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
