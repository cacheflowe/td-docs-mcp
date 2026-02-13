---
url: https://docs.derivative.ca/Video_Stream_Out_TOP
category: TOPs
title: Video_Stream_Out_TOP
---

# Video Stream Out TOP
## Summary

**NOTE**
**Hardware:** This TOP uses the Nvidia Hardware Encoder to create the stream and therefore requires an Nvidia GPU and Windows to operate.
The Video Stream Out TOP acts as an [RTMP](https://docs.derivative.ca/RTMP "RTMP") or [SRT](https://docs.derivative.ca/SRT "SRT") sender, can create an [RTSP](https://docs.derivative.ca/RTSP "RTSP") server, to send compressed video and audio across the network. It uses Nvidia's hardware encoder. For RTSP, it can handle multiple clients connecting to it at the same time. Multiple Video Stream Out TOPs using the same port will be handled using the same underlying RTSP server. The Video Stream Out TOP can also be used to send a video stream through [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") video/audio tracks.
The video codecs that can be streamed out are H.264, H.265 (HEVC) and AV1. (AV1 is supported by recent NVIDIA GPUs only.). Not every streaming protocol and/or service supports every codec option.
The audio codecs that can be streamed out are MP3, AAC and Opus.
##### RTMP
Enhanced RTMP is also supported.
To obtain the RTMP URL stream to, you may need to search to find the correct URL depending on your location and the service you are using. This should be in the format:
`{service url}/{stream key}`.
For example for Twitch the URL would be something like
`rtmp://live-yto.twitch.tv/app/live_1234567_sduhy3xJ1KJ34Eg6CjksdJLubFS7gtUY`
For more information on different services see [RTMP](https://docs.derivative.ca/RTMP "RTMP").
##### SRT
[SRT](https://en.wikipedia.org/wiki/Secure_Reliable_Transport) can use either H.264 or H.265 video codec. It can also send per-frame metadata when a CHOP or DAT is specified in the Per-Frame Metadata parameter.
The SRT server is settings are controlled by URL options. E.g to create a Video Stream Out, in listener-mode you'd specify the URL:
`srt://0.0.0.0:9494?mode=listener`
To connect to listener in a Video Stream In TOP, you'd do:
`srt://127.0.0.1:9494?mode=caller`
Either side of the connection can be the listener or the caller, it doesn't matter which is sending the video and which is receiving the video. The receiver would set their mode to be the opposite of whatever the sender is setting their mode to be.
All the options that are available are listed [here](https://ffmpeg.org/ffmpeg-protocols.html#srt). Multiple options can be set using a & as separator. E.g
`srt://127.0.0.1:9494?mode=caller&send_buffer_size=100000`
SRT sent from the Video Stream Out TOP can include per-frame metadata making it easy to send and receive CHOP/DAT data in sync with video. It can be read with the [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP").
##### RTSP
Obtain the URL to connect to the Video Steam Out TOP's RTSP server by using an Info DAT or by middle clicking on the node. It will be in the form:
`rtsp://<ipaddress>:<port>/<streamName>`
e.g.
`rtsp://192.168.0.1:554/tdvidstream`
##### Limitations
RTSP streaming does not support sending directly to another RTSP server via RTP.
NVIDIA Geforce level cards have a limit of 8 encoders sessions available per-system. Using a lower resolution does not avoid the encoder session limit. Quadros/RTX Pro cards have no session limit. In either case, the total amount of pixels that can be encoded will depend on the underlaying hardware, with newer/more powerful cards being able to encode more pixels. Refer to [Nvidia Video GPU Support Matrix](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new) for more information.
One test using the default TouchDesigner startup file on a M6000 was able to do 13 1080p@30hz Video Stream Out TOPs.
See also the [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP"), [RTMP](https://docs.derivative.ca/RTMP "RTMP"), [RTSP](https://docs.derivative.ca/RTSP "RTSP") and [Video Streaming User Guide](https://docs.derivative.ca/Video_Streaming_User_Guide "Video Streaming User Guide"), [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP").
For other protocols over IP see [NDI (Network Data Interface)](https://docs.derivative.ca/NDI "NDI"), and [Touch Out TOP](https://docs.derivative.ca/Touch_Out_TOP "Touch Out TOP") / [Touch In TOP](https://docs.derivative.ca/Touch_In_TOP "Touch In TOP").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[videostreamoutTOP_Class](https://docs.derivative.ca/VideostreamoutTOP_Class "VideostreamoutTOP Class")

## Parameters - Video Stream Out Page
- Active `active` - Controls if the server is active or not. If this is Off then the port this server uses will not be tied up.
- Mode `mode` - ⊞ - Selects if the mode works as an RTSP server, sends RTMP to a receiever such as a distribution service like YouTube or Twitch, or sends to an SRT destination.
  * RTSP Server `rtspserver` - Use the RTSP and RTP protocol. More information [here](https://docs.derivative.ca/index.php?title=Experimental:Video_Stream_Out_TOP&action=edit&redlink=1 "Experimental:Video Stream Out TOP \(page does not exist\)").
  * RTMP Sender `rtmpsender` - Use the RTMP protocol. More information [here](https://docs.derivative.ca/index.php?title=Experimental:Video_Stream_Out_TOP&action=edit&redlink=1 "Experimental:Video Stream Out TOP \(page does not exist\)").
  * SRT `srt` - Use the SRT protocol. More information [here](https://docs.derivative.ca/index.php?title=Experimental:Video_Stream_Out_TOP&action=edit&redlink=1 "Experimental:Video Stream Out TOP \(page does not exist\)").
  * WebRTC `webrtc` - Use a WebRTC peer. More info: [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC"), [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT").

- Network Port `port` - The port the server should listen on. Multiple Video Stream Out TOPs can use the same port as long as each has a unique Stream Name.
- Stream Name `streamname` - The name of the stream for this node. This name is what comes after the / in the URL after the ipaddress:port combination.
- Multi-Cast `multicast` - Controls if RTSP server sends its video out using unicast or multicast UDP packets.
- Destination URL `url` - The URL to send the SRT/RTMP stream to. For RTMP, this should be in the format of {service url}/{stream key}. For example for twitch the URL would be something like `rtmp://live-yto.twitch.tv/app/live_1234567_sduhy3xJ1KJ34Eg6CjksdJLubFS7gtUY`. You may need to search to find the correct URL depending on your location and the service you are using. For SRT refer to the SRT documentation or the note at the start of this page.
- Force IDR `forceidr` - For debugging, this will force the server to create a new video keyframe to send to all the clients. If clients aren't getting proper image this can be used to attempt to fix it. If you need to use this parameter please report the case to support@derivative.ca.
- FPS `fps` - The FPS to send video at.
- Video Codec `videocodec` - ⊞ - Select which codec to use for encoding the stream, not every codec is compatible with every streaming protocol
  * H.264 (NVIDIA GPU) `h264` - Usable with RTMP and SRT.
  * H.265/HEVC (NVIDIA GPU) `h265` - Usable with RTMP via Enchanced RTMP, and SRT.
  * AV1 (NVIDIA GPU) `av1` - Usable with RTMP, via Enhanced RTMP.

- Profile `profile` - ⊞ - The H.264 profile to use to encode the frames. Some decoders can only support H.264 encoder at certain profiles.
  * Baseline `baseline` -
  * Main `main` -
  * High `high` -

- Quality `quality` - ⊞ - The quality level of the encoding.
  * Low-Latency, Low Quality `lowlatencylow` -
  * Low-Latency, Medium Quality `lowlatencymedium` -
  * Low-Latency, High Quality `lowlatencyhigh` -
  * High-Latency, Low Quality `highlatencylow` -
  * High-Latency, High Quality `highlatencyhigh` -

-->
  * High-Latency, Ultra High Quality `highlatencyultrahigh` -

- Keyframe Interval `keyframeinterval` - Set the keyframe interval for the encoder, in frames. This sets both the GOP length and the IDR interval. Both of these control how many frames are between each IDR (key) frame.
- Max B-Frames `maxbframes` - The maximum number of bi-directional frames that can occur between keyframes. More will increase latency but reduce bandwidth.
- Intra-Refresh Period `intrarefreshperiod` - Intra-refresh is a gradual keyframe that is applied across the image to clean up streaming artifacts over multiple frames, instead of one large keyframe. This controls the number of frames that elapse between each intra-refresh occuring.
- Intra-Refresh Length `intrarefreshlength` - The number of frames the intra-refresh will be spread out across.
- Bitrate Mode `bitratemode` - ⊞ - Chooses between constant (CBR) and variable (VBR) bit rate modes. Mode streaming services prefer a constant bit rate mode.
  * Constant (CBR) `constant` -
  * Variable (VBR) `variable` -
  * Constant HQ (CBR) `constanthq` -
  * Variable HQ (VBR) `variablehq` -

- Average Bitrate (Mb/s) `avgbitrate` - The target bitrate for the encoding. This is specified in Mb/s (megabits/second).
- Max Bitrate (Mb/s) `maxbitrate` - The maximum bitrate for the encoding. This is specified in Mb/s (megabits/second).
- Num H264 Slices per Frame `numslices` - This controls how many pieces (slices) each H.264 frame is separated into. Some decoders are able to decode multiple slices simultaneously so setting this to a value above 1 allows those decoders to run more efficiently.
- Mux Rate (Mb/s) `forcemuxrate` - ⊞ -
  * Mux Rate (Mb/s) `forcemuxrate` -
  * Mux Rate (Mb/s) `muxrate` -

- VBV Buffer Size (Mb) `forcevbvbufsize` - ⊞ -
  * VBV Buffer Size (Mb) `forcevbvbufsize` -
  * VBV Buffer Size (Mb) `vbvbufsize` -

- RTMP Buffer Size (S) `forcertmpbufsize` - ⊞ -
  * RTMP Buffer Size (S) `forcertmpbufsize` -
  * RTMP Buffer Size (S) `rtmpbufsize` -

- Audio CHOP `audiochop` - A timesliced audio source to send along with the video. Depending on the protocol and audio codec, you same need to resample the audio using a [Resample CHOP](https://docs.derivative.ca/Resample_CHOP "Resample CHOP") to either 44100 or 48000Hz.
- Audio Codec `audiocodec` - ⊞ - The audio codec to compress the audio to.
  * MP3 `mp3` - Compressed lossy codec. Can only do 2 channels of audio.
  * AAC `aac` - [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding) is a lossy audio compression codec. Can only do 2 channels of audio. MP3 compression will not have gapless playback. Note: A particlular behavior on Windows OS AAC encoder; for 1 and 2 channels the selection of bit rate is for both channels combined. i.e. it’s 192kb/s for one channel, or 2x96kb/s for two. However, when using more than 2 channels the bitrate is per channel ie. for 6 channel then it’s 6x192kb/s.
  * Opus `opus` - [Opus](https://en.wikipedia.org/wiki/Opus_\(audio_format\)) is a lossy audio compression codec.

- Audio Bit Rate `audiobitrate` - ⊞ - Set the bit rate used for encoding audio.
  * 96 kb/s `b96` -
  * 128 kb/s `b128` -
  * 192 kb/s `b192` -
  * 256 kb/s `b256` -
  * 320 kb/s `b320` -

- Include Silent Audio Stream `includesilentaudio` - ⊞ - Some broadcasting services require an audio stream to be included. This will include a silent audio stream along with the video in the event there isn't actual audio being streamed video the CHOP parameter.
  * Automatic `automatic` -
  * On `on` -
  * Off `off` -

- Per-Frame Metadata CHOP/DAT `perframemetadata` - Send metadata from this OP with each frame of the video stream. This data can be recevied from the [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP") using an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") and [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT").
- Per-Frame Metadata `perframemetadata` - Send metadata from this OP with each frame of the video stream. This data can be received from the [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP") using an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") and [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT").

## Parameters - WebRTC Page
- WebRTC `webrtc` - Set the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") (ie. peer) to send the video stream over. Setting this will automatically populate the WebRTC Connection parameter menu with available connections.
- WebRTC Connection `webrtcconnection` - Select the [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") peer-to-peer connection. Selecting this will automatically population the WebRTC Track parameter menu with available video output tracks.
- WebRTC Video Track `webrtcvideotrack` - Select the video output track that's a part of the WebRTC peer-to-peer connection.
- WebRTC Audio Track `webrtcaudiotrack` - Optionally select the audio output track that's a part of the WebRTC peer-to-peer connection, to be sent along with the video.

## Parameters - Common Page
- Output Resolution `outputresolution` - ⊞ - quickly change the resolution of the TOP's data.
  * Use Input `useinput` - Uses the input's resolution.
  * Eighth `eighth` - Multiply the input's resolution by that amount.
  * Quarter `quarter` - Multiply the input's resolution by that amount.
  * Half `half` - Multiply the input's resolution by that amount.
  * 2X `2x` - Multiply the input's resolution by that amount.
  * 4X `4x` - Multiply the input's resolution by that amount.
  * 8X `8x` - Multiply the input's resolution by that amount.
  * Fit Resolution `fit` - Fits the width and height to the resolution given below, while maintaining the aspect ratio.
  * Limit Resolution `limit` - The width and height are limited to the resolution given below. If one of the dimensions exceeds the given resolution, the width and height will be reduced to fit inside the given limits while maintaining the aspect ratio.
  * Custom Resolution `custom` - Enables the Resolution parameter below, giving direct control over width and height.

- Resolution `resolution` - ⊞ - Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions.
  * W `resolutionw` -
  * H `resolutionh` -

- Resolution Menu `resmenu` - A drop-down menu with some commonly used resolutions.
- Use Global Res Multiplier `resmult` - Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier.
- Output Aspect `outputaspect` - ⊞ - Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.)
  * Use Input `useinput` - Uses the input's aspect ratio.
  * Resolution `resolution` - Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
  * Custom Aspect `custom` - Lets you explicitly define a custom aspect ratio in the Aspect parameter below.

- Aspect `aspect` - ⊞ - Use when Output Aspect parameter is set to Custom Aspect.
  * Aspect1 `aspect1` -
  * Aspect2 `aspect2` -

- Aspect Menu `armenu` - A drop-down menu with some commonly used aspect ratios.
- Input Smoothness `inputfiltertype` - ⊞ - This controls pixel filtering on the input image of the TOP.
  * Nearest Pixel `nearest` - Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
  * Interpolate Pixels `linear` - Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
  * Mipmap Pixels `mipmap` - Uses [ mipmap](https://docs.derivative.ca/Mipmapping "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.

- Fill Viewer `fillmode` - ⊞ - Determine how the TOP image is displayed in the viewer.
**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing.
  * Use Input `useinput` - Uses the same Fill Viewer settings as it's input.
  * Fill `fill` - Stretches the image to fit the edges of the viewer.
  * Fit Horizontal `width` - Stretches image to fit viewer horizontally.
  * Fit Vertical `height` - Stretches image to fit viewer vertically.
  * Fit Best `best` - Stretches or squashes image so no part of image is cropped.
  * Fit Outside `outside` - Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
  * Native Resolution `nativeres` - Displays the native resolution of the image in the viewer.

- Viewer Smoothness `filtertype` - ⊞ - This controls pixel filtering in the viewers.
  * Nearest Pixel `nearest` - Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
  * Interpolate Pixels `linear` - Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
  * Mipmap Pixels `mipmap` - Uses [ mipmap](https://docs.derivative.ca/Mipmapping "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.

- Passes `npasses` - Duplicates the operation of the TOP the specified number of times. Making this larger than 1 is essentially the same as taking the output from each pass, and passing it into the first input of the node and repeating the process. Other inputs and parameters remain the same for each pass.
- Channel Mask `chanmask` - Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default.
- Pixel Format `format` - ⊞ - Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](https://docs.derivative.ca/Pixel_Formats "Pixel Formats") for more information.
  * Use Input `useinput` - Uses the input's pixel format.
  * 8-bit fixed (RGBA) `rgba8fixed` - Uses 8-bit integer values for each channel.
  * sRGB 8-bit fixed (RGBA) `srgba8fixed` - Uses 8-bit integer values for each channel and stores color in sRGB colorspace.
  * 16-bit float (RGBA) `rgba16float` - Uses 16-bits per color channel, 64-bits per pixel.
  * 32-bit float (RGBA) `rgba32float` - Uses 32-bits per color channel, 128-bits per pixels.
  * 10-bit RGB, 2-bit Alpha, fixed (RGBA) `rgb10a2fixed` - Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
  * 16-bit fixed (RGBA) `rgba16fixed` - Uses 16-bits per color channel, 64-bits total per pixel.
  * 11-bit float (RGB), Positive Values Only `rgba11float` - A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
  * 16-bit float (RGB) `rgb16float` -
  * 32-bit float (RGB) `rgb32float` -
  * 8-bit fixed (Mono) `mono8fixed` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
  * 16-bit fixed (Mono) `mono16fixed` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
  * 16-bit float (Mono) `mono16float` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
  * 32-bit float (Mono) `mono32float` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
  * 8-bit fixed (RG) `rg8fixed` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
  * 16-bit fixed (RG) `rg16fixed` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
  * 16-bit float (RG) `rg16float` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
  * 32-bit float (RG) `rg32float` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
  * 8-bit fixed (A) `a8fixed` - An Alpha only format that has 8-bits per channel, 8-bits per pixel.
  * 16-bit fixed (A) `a16fixed` - An Alpha only format that has 16-bits per channel, 16-bits per pixel.
  * 16-bit float (A) `a16float` - An Alpha only format that has 16-bits per channel, 16-bits per pixel.
  * 32-bit float (A) `a32float` - An Alpha only format that has 32-bits per channel, 32-bits per pixel.
  * 8-bit fixed (Mono+Alpha) `monoalpha8fixed` - A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
  * 16-bit fixed (Mono+Alpha) `monoalpha16fixed` - A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
  * 16-bit float (Mono+Alpha) `monoalpha16float` - A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
  * 32-bit float (Mono+Alpha) `monoalpha32float` - A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Video Stream Out TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Video Stream Out TOP Info Channels
  * last_encode_time -

  * last_send_delay -

  * packet_loss_ratio -

###
## Common TOP Info Channels
  * resx - Horizontal resolution of the TOP in pixels.

  * resy - Vertical resolution of the TOP in pixels.

  * aspectx - Horizontal aspect of the TOP.

  * aspecty - Vertical aspect of the TOP.

  * depth - Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.

  * gpu_memory_used - Total amount of texture memory used by this TOP.

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
