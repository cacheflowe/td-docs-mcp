---
url: https://docs.derivative.ca/ZED_TOP
category: TOPs
title: ZED_TOP
---

# ZED TOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The ZED TOP captures video from the ZED depth camera.
**NOTE:** This TOP works with the [Stereolabs ZED](https://www.stereolabs.com/zed/) hardware. For more information and to know what ZED SDK to install refer to the [ZED](https://docs.derivative.ca/ZED "ZED") article.
It supports point clouds - getting the camera space positions of the color pixels, outputted as a 32-bit float RGB texture with XYZ in the RGB channels.
When used for point cloud rendering with TOPs, it can be used directly with the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") as it is in in the format needed for instancing.
It can instead pass its image data directly to the [ZED POP](https://docs.derivative.ca/ZED_POP "ZED POP") for rendering with POPs.
This node is where the device it actually configured. It can output one image type (color, depth etc). To get other images from the same device, use a [ZED Select TOP](https://docs.derivative.ca/ZED_Select_TOP "ZED Select TOP").
The ZED TOP can also playback pre-recorded captures of ZED to a `.svo` file. The ZED toolkit allows you to record large video datasets using H.264, H.265 or lossless compression using Stereolabs’ SVO format to store videos along with additional metadata such as timestamps and sensor data. When loading SVO files when the ZED TOP Input Source is set to SVO File, it will behave as if a ZED was connected and a live feed was available.
See also [ZED Select TOP](https://docs.derivative.ca/ZED_Select_TOP "ZED Select TOP"), [ZED CHOP](https://docs.derivative.ca/ZED_CHOP "ZED CHOP"), [ZED POP](https://docs.derivative.ca/ZED_POP "ZED POP") and [ZED SOP](https://docs.derivative.ca/ZED_SOP "ZED SOP").
[zedTOP_Class](https://docs.derivative.ca/ZedTOP_Class "ZedTOP Class")

## Parameters - ZED Page
- Active `active` - When set to 1 the TOP captures the image stream from the camera.
- Input Source `inputsource` - ⊞ - Select which input type to use between USB, recorded SVO file, or network streaming
  * Camera `camera` - USB.
  * SVO File `svofile` - Recorded SVO file. Camera settings will not be applied to SVO mode.
  * Network Stream `networkstream` - Network streaming.

- Camera `camera` - Selects which ZED camera to use.
- File `file` - The path and name of the recorded SVO file to load. SVO and SVO2 playback is supported.
- Stream IP `streamip` - The IP address of the streaming camera.
- Stream Port `streamport` - The port of the streaming camera.
- Initialize `initialize` - (pulse) Initializes the SVO playback: sets the SVO position to zero.
- Start `start` - (pulse) Start is the signal to commence the SVO playback.
- Play `play` - SVO plays when 1, SVO stops when 0.
- Cue `cue` - Jumps to Cue Point when set to 1.
- Cue Point `cuepoint` - Set the SVO position in the SVO playback as a point to jump to.
- Cue Unit `cueunit` - ⊞ - Select the units for this parameter from Index, Frames, and Seconds.
  * I `indices` -
  * F `frames` -
  * S `seconds` -

- Perspective `perspective` - ⊞ - Choose between Left or Right camera.
  * Left `left` -
  * Right `right` -

- Image `image` - ⊞ - Selects between the Color, Depth, Confidence, Disparity, Normals, Point Cloud, Spatial Texture, or Mask modes.
  * Color `color` - Uses the RGB image from the camera.
  * Depth `depth` - Textures where the value of the pixel is the distance in meters from the camera.
  * Confidence `confidence` - Gives the confidence/certainty of the depth map ranging from 0-1.
  * Disparity `disparity` - Uses the disparity map from the camera.
  * Normals `normals` - Each RGB pixel of the texture gives the XYZ pixel normal in meters.
  * Point Cloud `pointcloud` - The texture will be a 32-bit floating point texture where RGB pixel values are XYZ pixel values relative to the color camera, in meters.
  * Spatial Texture `spatialtexture` - Uses the texture extracted during spatial mapping by the ZED SOP.
  * Mask `mask` - Gives a texture where each pixel gives the ID of tracked bodies. Body tracking must enabled through a ZED CHOP.

- Camera Resolution `cameraresolution` - ⊞ - Selects the resolution of the camera capture.
  * 2208 x 1242 `2208x1242` -
  * 1920 x 1080 `1920x1080` -
  * 1280 x 720 `1280x720` -
  * 672 x 376 `672x376` -

- Camera FPS `camerafps` - Sets the frame rate of the camera capture.
- Sensing Mode `sensingmode` - ⊞ - Selects betweem Standard and Fill mode.
  * Standard `standard` - Uses depth map that preserves edges and depth accuracy.
  * Interpolate `interpolate` - Interpolate between depth edges.

- Depth Quality `depthquality` - ⊞ - Selects the depth computation mode of the camera.
  * Performance `performance` - Uses minimal resources for computation.
  * Quality `quality` - Uses high quality depth map requiring more resources.
  * Ultra `ultra` - An even better quality depth map than high, but also requiring even more resources.
  * Neural `neural` - This use an AI model to refine the depth. On first use the model will need to be optimized for your GPU, which will take serveral minutes. This only needs to occur once per machine.

- Minimum Depth `mindepth` - Sets the minimum depth in meters that will be computed.
- Maximum Depth `maxdepth` - Sets the maximum depth in meters.
- Too Close Value `toocloseval` - For depth pixels that are too close to resolve, this pixel value will be output instead.
- Too Far Value `toofarval` - For depth pixels that are too far to resolve, this pixel value will be output instead.
- Unknown Value `unknownval` - For depth pixels whose depth can not be determined, output this value instead.
- Depth Stabilization `depthstabilization` - Enables depth stabilization for the camera.
- Rerange `rerange` - Enabling this will remap pixel values to 0-1.
- Reference Frame `referenceframe` - ⊞ - Select between World and Camera reference frames for the Point Cloud pixels.
  * World `world` - The pixel values are with reference to the initial position of the camera.
  * Camera `camera` - The pixel values are with relative to the current position of the camera.

- Camera Transform `resetcameratransform` - Resets the camera position used for the reference frame above.
- Mirror Image `mirrorimage` - Flips the image in the y-axis.
- Disable Self-Calibration `disableselfcalib` - Disables self-calibration process at camera opening.
- Region of Interest Mask `roimmask` - Specify the TOP operator that contains the Region of Interest Mask texture. If more than half of an objects bounding box is outside of the region of interest mask, it will discard the detection.
- Region of Interest Channel `roimchannel` - ⊞ - Determines which part of the texture used to calculate the final mask.
  * Luminance `luminance` - Region of Interest Mask calculated based on luminance values.
  * Red `red` - Region of Interest Mask calculated based on red channel values.
  * Green `green` - Region of Interest Mask calculated based on green channel values.
  * Blue `blue` - Region of Interest Mask calculated based on blue channel values.
  * Alpha `alpha` - Region of Interest Mask calculated based on alpha channel values.
  * RGB Average `rgbaverage` - Region of Interest Mask calculated based on combined RGB average values.
  * RGBA Average `average` - Region of Interest Mask calculated based on combined RGBA average values.

## Parameters - Settings Page
- Brightness `bright` - Turn on to enable brightness adjustment controls for the camera. When disabled, the camera will use default brightness.
- Brightness `brightval` - The brightness of the camera feed.
- Contrast `cont` - Turn on to enable contrast adjustment controls for the camera. When disabled, the camera will use default contrast.
- Contrast `contval` - The contrast of the camera feed.
- Hue `hue` - Turn on to enable hue adjustment controls for the camera. When disabled, the camera will use default hue.
- Hue `hueval` - The hue of the camera feed.
- Saturation `sat` - Turn on to enable saturation adjustment controls for the camera. When disabled, the camera will use default saturation.
- Saturation `satval` - The saturation of the camera feed.
- Sharpness `sharp` - Turn on to enable sharpness adjustment controls for the camera. When disabled, the camera will use default sharpness.
- Sharpness `sharpval` - The sharpness of the camera feed.
- Gamma `gamma` - Turn on to enable gamma adjustment controls for the camera. When disabled, the camera will use default gamma.
- Gamma `gammaval` - The gamma of the camera feed.
- Auto Gain-Exposure `autogainexp` - Turn on to enable auto gain and exposure for the camera. When disabled, the camera will not apply auto gain and exposure.
- Gain `gain` - Turn on to enable gain adjustment controls for the camera. When disabled, the camera will use default gain.
- Gain `gainval` - The gain of the camera feed.
- Exposure `exp` - Turn on to enable exposure adjustment controls for the camera. When disabled, the camera will use default exposure.
- Exposure `expval` - The exposure of the camera feed.
- Region of Interest `roi` - Turn on to enable region of interest adjustment controls for the camera when auto gain and exposure is enabled. When disabled, the region of interest will be the full image. The region of interest is a rectangle that defines the target area for auto gain and exposure computation. It must be given according to camera resolution.
- ROI Coordinate `coord` - ⊞ - The coordinate of the top-left corner of the region of interest rectangle.
  * ROI Coordinate `coordx` - The x coordinate of the top-left corner.
  * ROI Coordinate `coordy` - The y coordinate of the top-left corner.

- ROI Dimension `dim` - ⊞ - The dimensions of the region of interest rectangle.
  * ROI Dimension `dimw` - The width of the rectangle.
  * ROI Dimension `dimh` - The height of the rectangle.

- Auto White Balance `autowhitebal` - Turn on to enable auto white balance for the camera. When disabled, the camera will not apply auto white balance.
- White Balance `whitebal` - Turn on to enable white balance controls for the camera. When disabled, the camera will use default white balance.
- White Balance `whitebalval` - The white balance of the camera feed. White balance values are internally multiplied by 100 to be within the range of [2800, 6500].
- LED Status `ledstat` - Turn on to enable the front LED of camera. When disabled, the camera LED will be disabled.

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
Extra Information for the ZED TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific ZED TOP Info Channels
  * vertical_fov - The physical vertical FOV of the camera, in degrees.

  * horizontal_fov - The physical horizontal FOV of the camera, in degrees.

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
