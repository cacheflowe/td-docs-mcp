---
url: https://docs.derivative.ca/Lookup_TOP
category: TOPs
title: Lookup_TOP
---

# Lookup TOP
## Summary

The Lookup TOP replaces color values in the TOP image connected to its first input with values derived from a lookup table created from its second input or a lookup table created using the CHOP parameter. When using the 2nd input, the lookup table is created by defining a line (start and end position) on the TOP image. When using a CHOP the lookup table is created directly from the CHOP's values and the 2nd input is ignored.
The Index Range parameter can be used to define the minimum and maximum index values that will map to the first and last values in the lookup table. When the index goes outside of this range, it will **hold** on the first or last value of the lookup table. For example if the range is set to [0.1, 0.2], a value from the first texture of 0.15 will map to the middle of the lookup. A value of 0.1 (and below) will map to the dark end of the lookup and a value of 0.2 (and above) will map to the light end of the lookup.
See also [Remap TOP](https://docs.derivative.ca/Remap_TOP "Remap TOP"), [Displace TOP](https://docs.derivative.ca/Displace_TOP "Displace TOP").
**Note:** This TOP supports 3D Textures and 2D Texture Arrays.
[lookupTOP_Class](https://docs.derivative.ca/LookupTOP_Class "LookupTOP Class")

## Parameters - Lookup Page
- Method `method` - ⊞ - Choose to use a line from the 2nd input (defined using UV coordinates) or CHOP values to define the lookup table.
  * 2nd Input, UV Coordinates `secondinput` - Use the Dark UV and Light UV parameters to define the lookup table as a line extrated from the 2nd input.
  * CHOP Values `chop` - Use a CHOP referenced in th CHOP parameter to define the lookup table.

- Index Range `index` - ⊞ - The Index Range maps the index values to the lookup table's start and end and defaults to 0 and 1. The first parameter represents the start of the lookup table. When the index color has this value, it will index the start of the lookup table. The second parameter represents the end of the lookup table and behaves in the same way. **Note:** When the index goes outside of this range, it will **hold** on the first or last value of the lookup table.
  * `index1` - The minimum index value that maps to the start of the lookup table. Indices below this value will hold on the first value of the lookup table.
  * `index2` - The maximum index value that maps to the end of the lookup table. Indices above this value will hold on the last value of the lookup table.
  * Index Range `index1` -
  * Index Range `index2` -

- Index Channel `channel` - ⊞ - The Index Channel controls how the color from the input is turned into a index to do the lookup. By default, the RGBA Independent option will do a separate lookup in each channel i.e. the red output channel will be based on the red value in the lookup table and the red value in the index image. For other options, like Luminance or RGBA Average, a single index value is calculated from the index color and all channels of the output image will be taken from the same pixel of the lookup table at the given index.
  * Luminance `luminance` -
  * Red `red` -
  * Green `green` -
  * Blue `blue` -
  * Alpha `alpha` -
  * RGB Average `rgbaverage` -
  * RGBA Average `average` -
  * RGB Maximum `rgbmax` -
  * RGBA Maximum `max` -
  * RGBA Independent `independent` -

- Independent Alpha `independentalpha` - When enabled, the Alpha value of the output image is retrieved independently from the lookup table based on the alpha channel of the index image (the first input). This option can reproduce the legacy behavior of using the luminance to lookup the RGB values while using the alpha to separately lookup the alpha value. This option has no effect if using the 'RGBA Independent' or 'Alpha' index channel options since those modes already use the alpha channel as an index.
- Dark UV `darkuv` - ⊞ - Set the UV position to use for dark end of the lookup table. In the original image connected to the first input, any pixel with a value of (0,0,0) will be replaced by the value found at this UV position in the image connected to the second input.
  * `darkuv1` -
  * `darkuv2` -

- Dark UV Unit `darkuvunit` - ⊞ -
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- Light UV `lightuv` - ⊞ - Set the UV position to use for light end of the lookup table. In the original image connected to the first input, any pixel with a value of (1,1,1) will be replaced by the value found at this UV position in the image connected to the second input.
  * `lightuv1` -
  * `lightuv2` -

- Light UV Unit `lightuvunit` - ⊞ -
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- CHOP `chop` - Reference the CHOP to use to define the RGBA (A is optional) values in the lookup table.
- Clamp CHOP Values `clampchopvalues` - Clamps CHOP values between 0-1.
- Output Lookup `displaylookup` - Outputs the lookup table itself, instead of replacing the color values of the first input.

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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Lookup TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
