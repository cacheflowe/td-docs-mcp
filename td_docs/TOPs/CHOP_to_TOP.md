---
url: https://docs.derivative.ca/CHOP_to_TOP
category: TOPs
title: CHOP_to_TOP
---

# CHOP to TOP
## Summary

The CHOP to TOP puts CHOP channels into a TOP image. By default the texture created will be 32-bit floating point to match the precision of the CHOP data. This can be changed setting the TOP's Pixel Format to something other than 'Input'.
The Data Format parameter determines how the input channels are converted into pixel colors in the output image. For example, when the Data Format is set to 'R', each channel will be interpreted as a row of red pixel data. Likewise, if the Data Format is RGBA, then the first 4 channels will become a set of red, blue, green and alpha data for one row of pixels and each subsequent set of 4 channels will become additional rows. _Note:_ Channels are grouped by their order in the CHOP rather than their names i.e. just because a channel is named g0 or b1 does not mean it will necessarily be be placed in a blue or green pixel.
The Image Layout parameter controls how the pixel rows are arranged in the output image. By default, the width of the image will be equal to the number of samples in the CHOP, clamped to a maximum texture width (often 32768) (the sample rate is ignored), and the height will be equal to the number of channel sets. For example, when the Data Format is RGB and the there are 9 input channels (for example, r0 g0 b0 r1 g1 b1 r2 g2 b2), there will be 3 rows of pixels using the default image layout.
If the channel length is longer than the image width, the wrapped layout option can be used to continue the channel data onto additional rows of pixels. Each new set of channels will still begin on a new row of pixels.
If the Image Layout parameter is set to Fit to Square, the TOP determines the image resolution based on the total number of samples across all channel sets (approximately the square root of the number of samples + 1) in width and height. This layout is most often used for point cloud data, where an efficient layout is preferred and the position of a pixel is not generally important. Unlike in the wrapped layout, channel sets in this mode are appended immediately to the end of the previous set, so that any empty pixels will appear at the end of the image. Where there are some unused pixels, you can fill the unused pixels at the top with a special value based on the Extra Pixel Values parameter, (0, 0, 0, 0) by default. To put (0, 0, 0, -1) you have to set the pixel format to 32-bit float so you can represent negative and positive numbers of any value.
[choptoTOP_Class](https://docs.derivative.ca/ChoptoTOP_Class "ChoptoTOP Class")

## Parameters - CHOP to TOP Page
- CHOP `chop` - The path of the CHOP being referenced.
- Data Format `dataformat` - ⊞ - Determines how the input CHOP channels will be turned into an image. If the CHOP is missing channels required to provide all the data for a scanline, the extra channels are ignored.
  * R `r` - Each channel is treated as the Red channel for a new scanline. Using the default Image Layout, the height of the image will be equal to the number of channels in the CHOP.
  * RG `rg` - The first two channels will be the Red and Green channels for a scanline, the next two channels will be Red and Green for the next scanline, etc. Using the default Image Layout, the height of the image will be half the number of channels in the CHOP, rounded down.
  * RGB `rgb` - The first three channels will be the Red, Green and Blue channels for a scanline, the next three channels will be Red, Green and Blue for the next scanline, etc. Using the default Image Layout, the height of the image will be the number of channels in the CHOP divided by 3, rounded down.
  * RGBA `rgba` - The first four channels will be the Red, Green, Blue, and Alpha channels for a scanline, the next four channels will be Red, Green, Blue and Alpha for the next scanline, etc. Using the default Image Layout, the height of the image will be the number of channels in the CHOP divided by 4, rounded down.
  * A `a` - Each channel is treated as the Alpha channel for a new scanline. Using the default Image Layout, the height of the image will be equal to the number of channels in the CHOP.
  * Legacy `legacy` - This mode only creates a single scanline in all cases. More than 4 channels will not do anything. If the CHOP has 1 or 2 channels, it will set R,G,B,A to the first channel of the CHOP. The 2nd channel is ignored. If it has 3 channels, it sets the 3 channels to R,G,B and A = sample number / # of samples (i.e A is a ramp starting at 0 and climbing to the (width -1). If it has 4 channels, they are set to R,G,B,A.

- Clamp CHOP Values `clamp` - Clamps CHOP values to 0-1 range.
- Image Layout `layout` - ⊞ - Controls the dimensions of the output image and how the CHOP samples are arranged as pixels. This menu replaces the previous 'Crop Long Channels' and 'Fit to Square' parameters.
  * Row per Channel Set (Cropped) `rowscropped` - Each set of channels, as determined by the Data Format, is converted into a row of pixels in the output image. If the channel length exceeds the maximum texture resolution, or the custom width defined in the Output Resolution, the remaining samples are **ignored**. This option is equivalent to turning on the previous Crop Long Channels parameter.
  * Row(s) per Channel Set (Wrapped) `rowswrapped` - Each set of channels, as determined by the Data Format, is converted into a row of pixels in the output image. If the channel length exceeds the maximum texture resolution, or the custom width defined in the Output Resolution, the remaining samples will be put **into a new row of pixels**. Additional channel sets will begin in a new row of the output rather than at the end of the previous set. This option is equivalent to turning off the previous Crop Long Channels parameter.
  * Fit to Square (Combine Sets) `square` - Pixels are arranged in the smallest square texture that fits all of the given CHOP samples. Channel sets, as determined by the Data Format, are wrapped onto the next row of pixels if the CHOP channel length exceeds the width of the texture. Unlike the wrapped layout, the next channel set will begin at the next available pixel rather than starting in a new row. This option is equivalent to turning off the old 'Crop Long Channels' parameter and turning on the previous 'Fit to Square' parameter. This layout is most often used for point cloud data, where the position of a pixel in the image is not generally important.

- Extra Pixel Values (RGBA) `rgba` - ⊞ - If the current Image Layout results in more pixels than there are available samples in the input CHOP, the values specified here will be used to fill in the extra pixels. (All textures require full rows of pixels, in other words all rows of pixels have the same number of pixels.)
  * Red `rgba1` -
  * Green `rgba2` -
  * Blue `rgba3` -
  * Alpha `rgba4` -

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
Extra Information for the CHOP to TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
