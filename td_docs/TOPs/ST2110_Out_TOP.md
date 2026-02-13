---
url: https://docs.derivative.ca/ST2110_Out_TOP
category: TOPs
title: ST2110_Out_TOP
---

# ST2110 Out TOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
Support for Blackmagic IP range and Deltacast DELTA-ip-ST2110 devices.
To obtain the SDPs generated for the output essences, use an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") and choose which SDP to obtain.
See also [ST2110 In TOP](https://docs.derivative.ca/ST2110_In_TOP "ST2110 In TOP"), [ST2110 Device CHOP](https://docs.derivative.ca/ST2110_Device_CHOP "ST2110 Device CHOP").
[st2110outTOP_Class](https://docs.derivative.ca/St2110outTOP_Class "St2110outTOP Class")

## Parameters - Video Page
- Active `active` - Controls if this node is sending out data over the ST2110 device.
- ST2110 Device CHOP `st2110devicechop` - Since a NIC has one set of settings such as DHCP/IP settings, that is controlled for each device using the ST2110 Device CHOP. This node will use that device to discover available output channels, and use the settings configured in that node for it's operation.
- Device `device` - Will be populated when the ST2110 Device CHOP is active and configured properly. Select which output channel on the device to use.
- Video Destination IP `videodestip` - The multicast IP address that the video essence should be sent on.
- Video Source Port `videosourceport` - The local network port number that the video essence should be sent from. Some devices will auto-select this port.
- Video Destination Port `videodestport` - The destination network port number that the video essence should be sent to.
- Video Payload Id `videopayloadid` - The Payload Id number to assign to the RTP packets for the video essence. Usually 96 for video.
- Signal Format `signalformat` - The Video Signal Format to send the video as.
- Output Pixel Format `outputpixelformat` - ⊞ - The Pixel Format to send data over the wire as.
  * 8-bit `fixed8` -
  * 10-bit `fixed10` -

- Timecode Object/CHOP/DAT `timecodeop` - For devices that support timecode, this can point to a [Timecode](https://docs.derivative.ca/Timecode "Timecode") source to send over the ancillary essence.
- Memory Mode `memorymode` - ⊞ - Controls how the video data is copied to the output device.
  * Automatic `automatic` - Choses the best option based on the system and the device used.
  * Pinned `pinned` - Use Pinned memory when supported. This allows for faster transfered between the device and the CPU/GPU RAM.
  * Regular `regular` - Use regular CPU RAM memory allocation.

## Parameters - Audio Page
- Audio CHOP `audiochop` - A timesliced audio CHOP that is either 44110 or 48000 Hz, but not all devices support both of those sample rates. This will be sent out over the audio essence.
- Audio Buffer Length `audiobufferlength` - How long of an audio buffer queue to hold. This helps avoid audio pops in the event video generation stutters.
- Audio Dest IP `audiodestip` - The multicast IP address that the audio essence should be sent on.
- Audio Source Port `audiosourceport` - The local network port number that the audio essence should be sent from. Some devices will auto-select this port.
- Audio Destination Port `audiodestport` - The destination network port number that the audio essence should be sent to.
- Audio Payload Id `audiopayloadid` - The Payload Id number to assign to the RTP packets for the audio essence. Usually 97 for audio.

## Parameters - SPS Page
SPS, which stands for Seamless Protection Switching is supported on some cards like the Deltacast IP cards. This allows for a second parallel path for the same data to be sent, as a backup incase the primary path fails.
- Enable SPS `enablesps` - Controls if the SPS stream is active or not.
- SPS Video Destination IP `spsvideodestip` - The multicast IP address that the video SPS essence should be sent on.
- SPS Video Source Port `spsvideosourceport` - The local network port number that the video SPS essence should be sent from. Some devices will auto-select this port.
- SPS Video Destination Port `spsvideodestport` - The destination network port number that the video SPS essence should be sent to.
- SPS Video Payload Id `spsvideopayloadid` - The Payload Id number to assign to the RTP packets for the SPS video essence. Usually 96 for video.
- SPS Audio Dest IP `spsaudiodestip` - The multicast IP address that the audio SPS essence should be sent on.
- SPS Audio Source Port `spsaudiosourceport` - The local network port number that the audio SPS essence should be sent from. Some devices will auto-select this port.
- SPS Audio Destination Port `spsaudiodestport` - The destination network port number that the audio SPS essence should be sent to.
- SPS Audio Payload Id `spsaudiopayloadid` - The Payload Id number to assign to the RTP packets for the audio SPS essence. Usually 97 for audio.

## Parameters - Color Page
- Output Color Space `outputcolorspace` - ⊞ - Controls what color space the data will be converted to before output. If the output (file/SDI/ST2110 etc) supports metadata, will also attempt to include the color space in that. Some output forms only support a limited number of color spaces in their metadata. If the color space is unknown to the output form, then no metadata will be included.
  * sRGB `srgb` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
  * sRGB - Linear `srgblinear` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.601 (NTSC) `rec601ntsc` - [Rec.601](https://en.wikipedia.org/wiki/Rec._601) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.709 `rec709` - [Rec.709](https://en.wikipedia.org/wiki/Rec._709) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.2020 `rec2020` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
  * Rec.2020 ST2084PQ `rec2020st2084pq` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with [Perceptual Quantizer](https://en.wikipedia.org/wiki/Perceptual_quantizer) transfer function. Considered an HDR color space with respect to Reference White.
  * Rec.2020 HLG `rec2020hlg` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with [Hybrid Log Gamma](https://en.wikipedia.org/wiki/Hybrid_log%E2%80%93gamma) transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 `dcip3` - [DCI-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 (D60) `dcip3d60` - [DCI-P3 "D60 sim"](https://en.wikipedia.org/wiki/DCI-P3) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) `displayp3d65` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) - Linear `displayp3d65linear` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and linear transfer function. Considered an HDR color space with respect to Reference White.
  * ACES2065-1 `aces2065-1` - [ACES 2065-1](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACEScg `acescg` - [ACEScg](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACESproxy `acesproxy` - [ACESproxy](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) color space, which has a log transfer function. Considered an HDR color space with respect to Reference White.
  * Passthrough `passthrough` - When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.

- Output Reference White `outputreferencewhite` - ⊞ - When converting the color values to the Working Color Space for output, this controls how they should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Output Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, and the project Working Color Space is HDR while the Output Color Space is SDR: then a color of (1, 1, 1), which is 80 nits in the HDR color space, will be converted to be (0.66, 0.66, 0.66), which is 80 nits still in the SDR Output Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
  * Standard (SDR) `sdr` - Will treat the Output Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Output Color Space as HDR for it's reference white value.

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
Extra Information for the ST2110 Out TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific ST2110 Out TOP Info Channels
  * connected - 1 if the device is connected/active, 0 if not.

  * frames_sent - The number of video frames sent out.

  * frames_dropped - The number of frames drops from the output. These are output frames that the process failed to provide new data for. If TouchDesigner is running lower than the framerate the signal format is running at, this value should be increasing. This means the previously created frame will be sent out a second (or more) times.

  * frames_skipped - These are frames that TouchDesigner produced, but didn't get consumed by the output device. This can be caused by the PCIe bandwidth (or the device) running slower than what is required for the data throughput/framerate.

  * packets_dropped - On the devices that report this, the number of packets dropped on output.

  * packets_underrun - On devices that report this, the number of packets that were missing when the device needed them.

  * frame_queue_length - The number of video frames queued in CPU memory for output.

  * frame_hw_queue_length - The number of video frames queued in the device hardware for output.

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
