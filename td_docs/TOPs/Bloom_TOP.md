---
url: https://docs.derivative.ca/Bloom_TOP
category: TOPs
title: Bloom_TOP
---

# Bloom TOP
## Summary

The Bloom TOP creates a glow effect around bright parts of the input image that simulates light bouncing around a lens assembly of a camera. Parameters control how much of the bright spots of your input image get bloomed, how wide the bloom gets spread, and how it rolls off into the un-bloomed areas.
The bloom starts with a **preprocessing stage** (Pre-Black Level, Pre-Gamma, and Pre-Brightness), (similar to the Black Level, Brightness, and Gamma parameters of a [Level TOP](https://docs.derivative.ca/Level_TOP "Level TOP")) which help to isolate the hot spots of the image that the bloom originates from (the Black Level), and boost the hot spots (Gamma and Brightness). (Switch the Output menu for a moment to Pre-Process to make sure you have a good signal to bloom with.)
The **second stage is a combination of scaled-down (blurred) levels** of the pre-processed image: The first level is the original pre-processed image, the second level is scaled down to half size (essentially 4 pixels averaged into one pixel), the third is the second level scaled down to half, and so on until the "top" level is 1x1 pixel (the average of the whole image.) For example, a 1024 x 1024 input images gives 10 levels. (These are called mipmaps.)
The second stage blends a range of scaled-down blur levels using the Min Bloom Radius and Max Bloom Radius parameters, where 0 refers to the first scaled-down level and 1 refers to the top scaled-down level. The Min and Max determine how dispersed or smeared the blooming is. Note: If Max<Min, Max is set to Min.
In the **third stage, the resulting bloom level is increased, reduced and shaped** using Bloom Threshold, Bloom S-Curve, Bloom Fill and Bloom Intensity. Typically the Fill and Intensity parameters should be adjusted first, and then some adjustment with Threshold, Min and Max, and with more finesse, the S-Curve if necessary.
Tip: If you want to bloom something and composite it over something else or a variant of the original, set the Output parameter to Bloom with Alpha and add it ([Add TOP](https://docs.derivative.ca/Add_TOP "Add TOP")) to something else.
[bloomTOP_Class](https://docs.derivative.ca/BloomTOP_Class "BloomTOP Class")

[![Bloom.png](https://docs.derivative.ca/images/thumb/2/28/Bloom.png/800px-Bloom.png)](https://docs.derivative.ca/File:Bloom.png)
## Parameters - Bloom Page
- Pre-Black Level `preblacklevel` - Similar to the Black Level parameter of a Luma Level TOP. Pixels with a luminosity less than this value are pushed to black.
- Pre-Gamma `pregamma` - Similar to the Gamma parameter of a Luma Level TOP, applies a gamma adjustment to the pixel value after the Pre-Black Level stage, which makes all non-zero values closer to RGB = 1, 1, 1.
- Pre-Brightness `prebrightness` - Similar to the Brightness parameter of a Luma Level TOP, it is a multiplier for the pixel value after the Pre-Gamma stage.
- Min Bloom Radius `minbloomradius` - Determines the minimum blur level to start sampling from. It is 0 to 1, so given a 1024x1024 image has 10 blur levels, if Minimum Bloom Size is set to .2, we will begin sampling from blur level 2 (the Pre-process image scaled to one quarter.) (The actual number of blur levels in the image is automatically determined by the image size.)
- Max Bloom Radius `maxbloomradius` - Determines the maximum blur level we sample from. It is 0 to 1, so if the image has 10 blur levels and a Maximum Bloom Size is set to .8, we will sample mipmap levels up to level 8. If Max<Min, Max is set to Min.
- Bloom Threshold `bloomthreshold` - After the blur levels have been mixed, this cuts away the darkest part of the image, or, when < 0, it adds more of the full-image average.
- Bloom S-Curve `bloomscurve` - Reshapes the bloom rolloff so that it is tighter/steeper to the hot spots.
- Bloom Fill `bloomfill` - Makes the bloom wider.
- Bloom Intensity `bloomintensity` - Final multiplier of accumulated bloom value.
- Output `output` - Permits the user to select the image that is output; useful for previewing the outputs of each stage of the bloom pipeline. If set to "Input", the original image is output; if set to "Preprocess", the preprocessed image is output; "Bloom" outputs only the bloom value with alpha = 1; "Bloom with Alpha" outputs only bloom value with its computed alpha (max of R G and B); and "Input + Bloom" (the default) outputs the combined source image and bloom image.
- Input Image `inputimage0` - Multiplier for the input image value that is added in to the final bloom value.

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
Extra Information for the can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP"). _[Info Channels Common Page](https://docs.derivative.ca/index.php?title=Info_Channels_Common_Page&action=edit&redlink=1 "Info Channels Common Page \(page does not exist\)")_
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
