---
url: https://docs.derivative.ca/Video_Stream_In_TOP
category: TOPs
title: Video_Stream_In_TOP
---

# Video Stream In TOP
## Summary

The Video Stream In TOP creates a client to receive video and audio across the network from RTSP, HLS, or SRT protocol sources; or from a WebRTC peer via a [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT").
The URL to connect to a RTSP server is in the form:
`rtsp://<ipaddress>:<port>/<streamName>` for example `rtsp://192.168.0.1:554/tdvidstream`
If the server requires a username/password, those can be specified using the form.
`rtsp://username:password@192.168.0.1:554/tdvidstream`
Access **[HLS/DASH](https://en.wikipedia.org/wiki/HTTP_Live_Streaming)** input streams via URLs that point to m3u8 files.
Access streams using **[SRT (Secure Reliable Transport)](https://en.wikipedia.org/wiki/Secure_Reliable_Transport)** protocol with `srt://` URLs. For more information on SRT URLs, please see [Video Stream Out TOP](https://docs.derivative.ca/Video_Stream_Out_TOP "Video Stream Out TOP").
See also [Audio Stream In CHOP](https://docs.derivative.ca/Audio_Stream_In_CHOP "Audio Stream In CHOP"), [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT").
SRT sent in the Video Stream In TOP can include per-frame metadata making it easy to send and receive CHOP/DAT data in sync with video. Attach an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") to the TOP.
The video codecs that can be streamed in via SRT are H.264 and H.265.
For other protocols over IP see [NDI (Network Data Interface)](https://docs.derivative.ca/NDI "NDI"), and [Touch Out TOP](https://docs.derivative.ca/Touch_Out_TOP "Touch Out TOP") / [Touch In TOP](https://docs.derivative.ca/Touch_In_TOP "Touch In TOP").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[videostreaminTOP_Class](https://docs.derivative.ca/VideostreaminTOP_Class "VideostreaminTOP Class")

## Parameters - Play Page
- Active `active` - When set to one, the TOP captures the image stream from the specified url.
- Mode `mode` - ⊞ - Select the mode: either a Server (for RTSP, HLS or SRT URLs), or WebRTC.
  * Server `server` - Use a RTSP, HLS, or SRT server source.
  * WebRTC `webrtc` - Use a WebRTC peer as a source.

- Server URL `url` - The URL (address) of the stream, see summary above for specific details.
- Reload `reload` - Reload the stream by attempting to reconnect.
- Reload Pulse `reloadpulse` - Triggers the Reload immediately on release (button-up). This can be accessed in python using the pulse() method.
- Play `play` - The stream will play forward when Play = On, it will be paused when Off.
- Force Re-buffer `forcerebuffer` - Force the stream to re-buffer if possible.

## Parameters - Image Page
- Deinterlace `deinterlace` - ⊞ - For movies that are stored as fields, where each image is made of two images interleaved together. A 30-frame per second movie would contain 60 fields per second. For each image, the even scanlines of the first field are interleaved with the odd scanlines of the second field. The Video Stream In TOP has several ways of dealing with this:
  * Off `off` - Output the images unchanged.
  * Even `even` - Take only the even scanlines of the file's images and create the odd scanlines by interpolating between the even scanlines. (For historic reasons, scanline 0 is at the top of the images for the purpose of the deinterlacing.)
  * Odd `odd` - Take only the odd scanlines of the file's images and create the even scanlines by interpolating between the odd scanlines.
  * Bob (Split) `bob` - This produces 60 images per second for a 30 frame-per-second movie file. It first outputs the even image (as in Even above) followed by the Odd image. This has the best time-smoothness.

- Field Precedence `precedence` - ⊞ - Where fields are extracted one field at a time, this will extract the Even field first by default, otehrwise it will extract the odd field first. The industry has not standardized on one or the other.
  * Even `even` -
  * Odd `odd` -

- Bottom Half is Alpha (AAA) `bottomhalfalpha` - This is a way of encoding alpha into RGB-only formats like H.264. and several other QuickTime formats. You need to create your movies so that the bottom half of the image is the alpha (RGB = AAA). Turning on this features tells the Video Stream In TOP to take the bottom half of the image and put it into the alpha channel of the output. The image height will be cut in half.

## Parameters - Tune Page
- Pre-Read Frames `prereadframes` - Sets how many video frames TouchDesigner reads ahead and stores in memory. Using this, smooth reading of an image stream is possible even when the disk files are fragmented. The Movie File In TOP will read frames of the movie into memory before they are used, this can eliminate pops or stutters in playback that occur from fragmented files, other resources accessing the hard drive, or movie looping.
- Video Buffer Frames `videobufferframes` - Sets how many video frames TouchDesigner reads ahead and stores in memory. Using this, smooth reading of an image stream is possible even when the disk files are fragmented. The Movie File In TOP will read frames of the movie into memory before they are used, this can eliminate pops or stutters in playback that occur from fragmented files, other resources accessing the hard drive, or movie looping.
- Max Decode CPUs `maxdecodecpus` - Limit the maximum number of CPUs that will be used to decode certain codecs that are capable of multi-CPU decoding, such as H264.
- Network Buffer Size (KB) `networkbuffersize` - Specify the size of the network input buffer in kilobytes.
- Network Queue Size (4KB Each) `networkqueuesize` - Specify the number of 4KB chunks to assign to the network queue. This is data stored after being read off of the network input buffer.
- Disable Buffering `disablebuffering` -
- Hardware Decode `hwdecode` - Enables hardware decoding on Nvidia GPUs.

## Parameters - WebRTC Page
- WebRTC DAT `webrtc` - Set the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") (ie. peer) to get the video stream from. Setting this will automatically populate the WebRTC Connection parameter menu with available connections.
- WebRTC Connection `webrtcconnection` - Select the [WebRTC](https://docs.derivative.ca/WebRTC "WebRTC") peer-to-peer connection. Selecting this will automatically population the WebRTC Track parameter menu with available video input tracks.
- WebRTC Track `webrtctrack` - Select the video input track that's a part of the WebRTC peer-to-peer connection.
## Parameters - Common Page
- Output Resolution `outputresolution` - ⊞ - quickly change the resolution of the TOP's data.
  * Use Input `useinput` - Uses the input's resolution
  * Eighth `eighth` - Multiply the input's resolution by that amount.
  * Quarter `quarter` - Multiply the input's resolution by that amount.
  * Half `half` - Multiply the input's resolution by that amount.
  * 2X `2x` - Multiply the input's resolution by that amount.
  * 4X `4x` - Multiply the input's resolution by that amount.
  * 8X `8x` - Multiply the input's resolution by that amount.
  * Fit Resolution `fit` - Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
  * Limit Resolution `limit` - Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
  * Custom Resolution `custom` - Directly control the width and height.

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
  * Mipmap Pixels `mipmap` - Uses [ mipmap](https://docs.derivative.ca/Mipmapping "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).

- Passes `npasses` - Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image.
- Channel Mask `chanmask` - Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default.
- Pixel Format `format` - ⊞ - Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](https://docs.derivative.ca/Pixel_Formats "Pixel Formats") for more information.
  * Use Input `useinput` - Uses the input's pixel format.
  * 8-bit fixed (RGBA) `rgba8fixed` - Uses 8-bit integer values for each channel.
  * sRGB 8-bit fixed (RGBA) `srgba8fixed` - Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](https://docs.derivative.ca/SRGB "SRGB").
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

## Info CHOP Channels
Extra Information for the Video Stream In TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Video Stream In TOP Info Channels
  * frame_time -

  * file_resx -

  * file_resy -

  * odd_field -

  * connections_lost -

  * connections_failed -

  * num_pre_read_frames -

  * last_frame_network_read_time -

  * last_frame_decode_time -

  * last_gpu_upload_time -

  * connected -

  * connecting -

  * connection_failed -

  * hardware_yuv_to_rgb -

  * network_mbit_rate -

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
