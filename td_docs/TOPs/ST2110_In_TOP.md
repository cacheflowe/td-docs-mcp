---
url: https://docs.derivative.ca/ST2110_In_TOP
category: TOPs
title: ST2110_In_TOP
---

# ST2110 In TOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
Support for Blackmagic IP range and Deltacast DELTA-ip-ST2110 devices.
See also [ST2110 Out TOP](https://docs.derivative.ca/ST2110_Out_TOP "ST2110 Out TOP"), [ST2110 Device CHOP](https://docs.derivative.ca/ST2110_Device_CHOP "ST2110 Device CHOP").
[st2110inTOP_Class](https://docs.derivative.ca/St2110inTOP_Class "St2110inTOP Class")

## Parameters - ST2110 In Page
- Active `active` - Controls if this input has it's connection open and is capturing data.
- ST2110 Device CHOP `st2110devicechop` - Since a NIC has one set of settings such as DHCP/IP settings, that is controlled for each device using the [ST2110 Device CHOP](https://docs.derivative.ca/ST2110_Device_CHOP "ST2110 Device CHOP"). This node will use that device to discover available input channels, and use the settings configured in that node for it's operation.
- Device `device` - Will be populated when the [ST2110 Device CHOP](https://docs.derivative.ca/ST2110_Device_CHOP "ST2110 Device CHOP") is active and configured properly. Select which input channel on the device to use.
- Setup Mode `setupmode` - ⊞ - Controls how this node configures it's input streams.
  * SDP Parameters `sdpparameters` - Use the Video, Audio and Ancillary SDP parameters to point to string that contain the SDPs each essences.
  * NMOS `nmos` - Use NMOS to push the configuration onto this stream. The [Riedel NMOS Explorer](https://www.riedel.net/en/downloads/firmware-software) is a free basic app that does NMOS control.

- Video SDP `videosdp` - The SDP string for the video essence.
- Audio SDP `audiosdp` - The SDP string for the audio essence.
- Ancillary SDP `ancillarysdp` - The SDP string for the ancillary essence.
- Set Source IP from SDP `setsourceipfromsdp` - On devices that support it, this causes the Source IP to also be assigned to the device's configuration, based on what is in the SDP.
- Main Stream Identifier `mainstreamidentifier` - Default's to 'primary' when blank, controls the name of identifier to select the section of the SDP to use, for the main stream.
- SPS Stream Identifier `spsstreamidentifier` - Default's to 'secondary' when blank, controls the name of identifier to select the section of the SDP to use, for the SPS stream.
- Deinterlace `deinterlace` - ⊞ - Controls how the content is deinterlaced, if desired.
  * Off `off` -
  * Even `even` -
  * Odd `odd` -
  * Bob (Split) `bob` -

- Field Precedence `precedence` - ⊞ - When using 'Bob (Split)' deinterlacing, controls which field is used as the first frame of the two fields.
  * Even `even` -
  * Odd `odd` -

- Input Pixel Format `inputpixelformat` - ⊞ - Controls the bit depth to convert the input signal into when uploading the data to the GPU.
  * 8-bit `fixed8` -
  * 10-bit `fixed10` -

- Input Color Space `inputcolorspace` - ⊞ - Controls what color space the input data will be treated as. It will be converted to the Working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") when uploaded to the GPU.
  * Automatic `automatic` - Automatically try to determine the input's color space based on color space metadata available from the input, if any. If no color space can be determined, it is assumed to be sRGB.
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

- Input Reference White `inputreferencewhite` - ⊞ - When converting the input color values to the Working Color Space, this controls how they should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
  * Standard (SDR) `sdr` - Will treat the Input Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Input Color Space as HDR for it's reference white value.

- Transfer Mode `transfermode` - ⊞ - Controls the strategy used to upload images to the GPU.
  * Automatic `automatic` - Use the best option based on the hardware.

-->
  * Pre-Upload `preupload` - Upload every frame as they become available from the device. This is usually used for Automatic.
  * On-Demand `ondemand` - Only upload frames when they are chosen to be shown. This is a lower performance mode, and usually only useful in a low performance situation, where PCIe bandwidth is constrained and frames are already being dropped.

- Reset Stats `resetstats` - Reset the stats given from the [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").

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
Extra Information for the ST2110 In TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific ST2110 In TOP Info Channels
  * connected - 1 if the node is successfully connected to the device, 0 if not. This does not necessarily mean there is valid input coming to the device.

  * sync_timeouts - When using the 'Sync Group' feature, this counts how many times the group failed to all provide a frame with similar enough timestamps within the timeout period.

  * last_sync_wait - How long the node had to wait from the time it was ready for a new frame until all the inputs provided valid frames for a synced output.

  * odd_field - When de-interlacing an interlaced input, this will be 1 when the odd field is being shown and 0 when the even field is being shown.

  * capture_fps - The calculated number of frames per second that are being captured by the device. This does **not** map directly to the signal format rate. It won't show 59.97 for example. This is simply a count of how many frames were captured in the last 1000ms.

  * capture_total - The total number of frames that have been captured this capture began.

  * frames_repeated - How many times the node has shown the same frame more than once. It does not currently correct for if the repeats are expected, such as when capturing a 30hz signal but TouchDesigner is running at 60fps. In that case the channel will keep increasing since each captured frame will be shown twice.

  * frames_dropped - This counts how many frames were captured by the card, but never consumed by TouchDesigner's reading thread. This occurs if the capture is running faster than TouchDesigner is able to consume frames.

  * frames_skipped - This counts how many frames were consumed by TouchDesigner's reading thread, but never consumed by the node itself. This can occur if TouchDesigner isn't running at full frame rate.

  * packets_received - The number of packets received on the primary port.

  * video_receive_jitter - The arrival jitter for video packets on the primary port.

  * audio_receive_jitter - The arrival jitter for audio packets on the primary port.

  * sps_packets_received - The number of packets received on the SPS port.

  * sps_video_receive_jitter - The arrival jitter for video packets on the SPS port.

  * sps_audio_receive_jitter - The arrival jitter for audio packets on the SPS port.

  * connection_changes - Counts connection changes, not supported by all devices.

  * signal_fps - The actual signal format FPS of the input signal. 0 if unknown.

  * rgb_input - Will be 1 if the input is detected as an RGB (such as RGB 4:4:4) format. 0 if it is a YUV/YCbCr based. -1 if it is unknown or not supported by the the library.

  * frame_queue_length - The number of receieved frames queued inside TouchDesigner.

  * frame_hw_queue_length - The number of frames still queued on the device that TouchDesigner has not yet read.

  * last_dma_copy_time - The number of milliseconds it took to copy the last frame from the device to the CPU. -1 if this is not measured.

  * frame_timestamp - Time in seconds of the last frame displayed. -1 if this is not provided by the device.

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
