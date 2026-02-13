---
url: https://docs.derivative.ca/Orbbec_TOP
category: TOPs
title: Orbbec_TOP
---

# Orbbec TOP
## Summary

The Orbbec TOP can be used to retrieve video streams and IMU data from an [Orbbec camera](https://docs.derivative.ca/Orbbec "Orbbec"). The available video streams depend on the connected camera, but typically include color, depth, IR and point cloud data. This node uses the Orbbec SDK and a list of [compatible camera models](https://github.com/orbbec/OrbbecSDK) can be found on the project's Github page.
Skeleton tracking data can be obtained from compatible Kinect Orbbec cameras (Femto Mega, Femto Bolt, etc) using the [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP") and [Kinect Azure CHOP](https://docs.derivative.ca/Kinect_Azure_CHOP "Kinect Azure CHOP"). **Note:** if using the Kinect Azure nodes with Orbbec hardware, you should not use the Orbbec TOP in the same project or it could lead to instabilities.
The cameras may be connected either by USB or ethernet depending on the model.
**Note:** Obtaining color video images over ethernet may not be supported for older firmware. We recommend you update your camera firmware to the latest version that is compatible with the Orbbec SDK that your TouchDesigner build is using.
**MacOS:** Connecting to Orbbec cameras on Mac OS systems requires root privileges. You can launch TouchDesigner with root privileges by opening a Terminal window and using the sudo command i.e. `sudo "/Applications/TouchDesigner.app/contents/MacOS/TouchDesigner"`
To obtain more than one video stream from a camera, you can use one or more [Orbbec Select TOPs](https://docs.derivative.ca/Orbbec_Select_TOP "Orbbec Select TOP") linked to the primary Orbbec TOP. All resolution and configuration is handled by the primary Orbbec TOP.
An [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") can be used to view the current value of each supported camera property, and an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") can be used to see the minimum, maximum, and default value of each supported camera property.
[orbbecTOP_Class](https://docs.derivative.ca/OrbbecTOP_Class "OrbbecTOP Class")

## Parameters - Orbbec Page
- Active `active` - Turn this parameter off to disable communication with the camera. This will also stop any [Orbbec Select TOPs](https://docs.derivative.ca/Orbbec_Select_TOP "Orbbec Select TOP") that rely on this TOP.
- Device Source `devicesource` - ⊞ - Specifies which mode to use to connect to a camera. **Note:** We generally recommend users to connect to cameras through the Device menu parameter instead of specifying the IP address.
  * Auto-Detect `auto` - Connect to enumerated cameras through the Device menu.
  * IP Address `ipaddress` - Connect to cameras by specifying their IP addresses.

- Device `device` - Use this parameter to select the serial number of the camera you wish to connect to. Only one Orbbec TOP can connect to any camera at one time. Use an [Orbbec Select TOP](https://docs.derivative.ca/Orbbec_Select_TOP "Orbbec Select TOP") to obtain additional video streams from the same camera. Both USB and ethernet connected cameras are discoverable by this menu. Cameras connected through this menu can automatically reconnect after unplugging and replugging. **Note:** It can take up to 30s for a camera to appear after it has been plugged in.
- IP `ip` - The IP address of the camera to connect to.
- Color Resolution `colorres` - ⊞ - Select the resolution of the sensor's color camera. Every camera has a default resolution that it will use automatically. Additional options will appear in the menu depending on the camera model. Not all frame rates (FPS) will be available for all camera resolutions.
  * Default `default` - Use the default resolution for the camera.

- Color FPS `colorfps` - ⊞ - Set the frame rate in frames-per-second for the color camera. The camera will assume a default frame rate automatically, but additional rates will appear in this list depending on the camera model. Not all frame rates may be supported by the current camera resolution.
  * Default `default` - The default frame rate for the sensor's color camera.

- Depth Resolution `depthres` - ⊞ - Select the resolution of the sensor's depth camera. Every camera has a default resolution that it will use automatically. Additional options will appear in the menu depending on the camera model. Not all frame rates (FPS) will be available for all camera resolutions.
  * Default `default` - The default resolution rate for the sensor's depth camera.

- Depth FPS `depthfps` - ⊞ - Set the frame rate in frames-per-second for the depth camera. The camera will assume a default frame rate automatically, but additional rates will appear in this list depending on the camera model. Not all frame rates may be supported by the current camera resolution.
  * Default `default` - The default frame rate for the sensor's depth camera.

- Depth Align Mode `depthalignmode` - ⊞ - This parameter can be used to transform the depth image to match the resolution of the color camera. This may be done in either hardware or software depending on the camera model. Some resolutions may not be supported. The node will display an error if the current depth and color resolutions are not compatible.
  * Disabled `disabled` - The depth image will be displayed in its native resolution.
  * Hardware `hardware` - The depth image will be transformed to the color camera's resolution using hardware remapping.
  * Software `software` - The depth image will be transformed to the color camera's resolution using software remapping.

- Image `image` - ⊞ - Select which of the camera's video streams to display in the node's output image. Additional streams can be obtained for the same camera using the [Orbbec Select TOP](https://docs.derivative.ca/Orbbec_Select_TOP "Orbbec Select TOP").
  * Color `color` - The video stream for the color camera. This is usually an 8-bit RGBA image.
  * Depth `depth` - The video stream for the depth camera. This is a 32-bit floating point texture where each pixel measures the depth in meters.
  * IR `ir` - The raw IR image from the depth camera. The resolution and frame rate are based on the depth camera settings.
  * Point Cloud `pointcloud` - A 3D point cloud where the x, y and z positions are stored in meters in the red, blue and green channels of a 32 bit floating point image.

- Enable Gyro Sensor `gyro` - Enable rotational IMU data from the gyro sensor if it is available on the current camera. The data is measured in degrees/sec and accessible as CHOP channels by attaching an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
- Enable Accel Sensor `accel` - Enable linear acceleration IMU data from the accel sensor if it is available on the current camera. The data is measured in m/s^2 and accessible as CHOP channels by attaching an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
- Properties CHOP `propschop` - The path of the properties CHOP being referenced. Each channel of the CHOP represents an [OBPropertyID](https://orbbec.github.io/OrbbecSDK/doc/api/English/Property_8h.html#a9e7aac1ea041c8958ea8c6e3aa53bbab) which can be used to control camera settings. The channel name must be all lowercase and cannot include the 'OB_PROP_' prefix. For example, a valid channel name for 'OB_PROP_COLOR_MIRROR_BOOL' would be 'color_mirror_bool'. Supported properties differ between each Orbbec camera model. The current value of each supported property can be viewed in an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP"). The minimum, maximum, and default values of each supported property can be viewed in an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT").

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
Extra Information for the Orbbec TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
