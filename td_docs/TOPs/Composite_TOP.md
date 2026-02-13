---
url: https://docs.derivative.ca/Composite_TOP
category: TOPs
title: Composite_TOP
---

# Composite TOP
## Summary

The Composite TOP is a multi-input TOP that will perform a composite operation for each input. Select the composite operation using the Operation parameter on the Composite parameter page.
**Note:** See also the [blendModes component](https://docs.derivative.ca/Palette:blendModes "Palette:blendModes") in the Palette. Refer also to [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets").
**Note:** This TOP supports 3D Textures and 2D Texture Arrays.
[compositeTOP_Class](https://docs.derivative.ca/CompositeTOP_Class "CompositeTOP Class")

## Parameters - Composite Page
- TOP `top` - In addition to all the inputs attached, you can specify more using the TOPs listed in this field. Example: `ramp*` will composite all TOPs whose name starts with `ramp`.
- Preview Grid `previewgrid` - This outputs an image showing the effect of all operation types in a grid, with the inputs swapped on the right side of each tile.
- Select Input `selectinput` - Instead of doing the composites, this causes only one of the inputs to pass through.
- Input Index `inputindex` - When passing through an input with Select Input on, this is the index of the image that is passed through.
- Operation `operand` - ⊞ - Choose which composite operation is performed from this menu. Search the web for 'blend modes' for more detailed information on the effects of each type.
  * Add `add` - input1.rgba + input2.rgba
  * Atop `atop` - (input1.rgba * input2.a) + (input2.rgba * (1.0 - input1.a))
  * Average `average` - (input1.rgba + input2.rgba)/2
  * Brightest `brightest` -
  * Burn Color `burncolor` -
  * Burn Linear `burnlinear` -
  * Chroma Difference `chromadifference` -
  * Color `color` -
  * Darker Color `darkercolor` -
  * Difference `difference` - absoluteValue(input1.rgb - input2.rgb). Alpha always equals 1.0
  * Dimmest `dimmest` -
  * Divide `divide` - input1.rgba / input2.rgba
  * Dodge `dodge` -
  * Exclude `exclude` -
  * Freeze `freeze` -
  * Glow `glow` -
  * Hard Light `hardlight` -
  * Hard Mix `hardmix` -
  * Heat `heat` -
  * Hue `hue` -
  * Inside `inside` - input1.rgba * clamp(input2.a, 0.0, 1.0)
  * Inside Luminance `insideluminance` -
  * Inverse `inverse` -
  * Lighter Color `lightercolor` -
  * Luminance Difference `luminancedifference` -
  * Maximum `maximum` - max(input1.r, input2.r), max(input1.g, input2.g), max(input1.b, input2.b), max(input1.a, input2.a)
  * Minimum `minimum` - min(input1.r, input2.r), min(input1.g, input2.g), min(input1.b, input2.b), min(input1.a, input2.a)
  * Multiply `multiply` -
  * Negate `negate` -
  * Outside `outside` - input1.rgba * (1.0 - input2.a)
  * Outside Luminance `outsideluminance` -
  * Over `over` - (input2.rgba * (1.0 - input1.a)) + input1.rgba
  * Overlay `overlay` -
  * Pinlight `pinlight` -
  * Reflect `reflect` -
  * Screen `screen` - 1.0 - ((1.0 - input1.rgba) * (1.0 - input2.rgba))
  * Soft Light `softlight` -
  * Linear Light `linearlight` -
  * Stencil Luminance `stencilluminance` -
  * Subtract `subtract` - input1.rgba - input2.rgba
  * Subtractive `subtractive` -
  * Under `under` - (input1.rgba * (1.0 - input2.a)) + input2.rgba
  * Vivid Light `vividlight` -
  * Xor `xor` - (input1.rgba * (1.0 - input2.a)) + (input2.rgba * (1.0 - input1.a))
  * Y Film `yfilm` -
  * Z Film `zfilm` -

- Swap Operation Order `swaporder` - Swaps the order of the input pairs. A operation B is changed to B operation A. Operations like Add don't matter, but many do, like Over and Hard Light.

## Parameters - Transform Page
- Fixed Layer `size` - ⊞ - The selected input will become the fixed layer and the other input will be the overlay. This does not change the order of the composite (Input1 + Input2), only which layer is considered fixed and which layer is adjustable by the parameters on the Transform page. The resolution and aspect ratio of the Fixed Layer is used as the composite's final resolution and aspect ratio unless manually on the [Common Page](#Parameters_-_Common_Page)
  * Input 1 `input1` -
  * Input 2 `input2` -

- Pre-Fit Overlay `prefit` - ⊞ - Determines how the Overlay layer (Overlay layer is the input that is NOT the Fixed Layer) fills the composite.
  * Fill `fill` - Overlay layer is stretched/squashed to fill the resolution and aspect ratio of the Fixed Layer.
  * Fit Horizontal `fithorz` - Overlay layer is stretched/squashed to fit the Fixed Layer horizontally.
  * Fit Vertical `fitvert` - Overlay layer is stretched/squashed to fit the Fixed Layer vertically.
  * Fit Best `fitbest` - Overlay layer is stretch/squashed to fit the Fixed Layer using the best possible match that does not crop any of the Overlay layer. The aspect ratio of the Overlay is maintained.
  * Fit Outside `fitoutside` - Overlay layer is stretched squashed to fit the Fixed Layer using the worst possible match. This is the opposite of Best Fit. The aspect ratio of the Overlay is maintained.
  * Native Resolution `nativeres` - Overlay is not squashed or stretched. The Overlay layer uses its own resolution and aspect ratio during the composite. Pixel accurate composites require Native Resolution, use this setting for to maintain an image's original resolution during the composite.

- Justify Horizontal `justifyh` - ⊞ - Specify the horizontal alignment of the Overlay.
  * Left `left` - The Overlay is aligned to the left side of the Fixed Layer.
  * Center `center` - The Overlay is centered in the Fixed Layer.
  * Right `right` - The Overlay is aligned to the right side of the Fixed Layer.

- Justify Vertical `justifyv` - ⊞ - Specify the vertical alignment of the Overlay.
  * Bottom `bottom` - The Overlay is aligned to the bottom of the Fixed Layer.
  * Center `center` - The Overlay is centered in the Fixed Layer.
  * Top `top` - The Overlay is aligned to the top of the Fixed Layer.

- Extend Overlay `extend` - ⊞ - Sets the extend (or repeat) conditions of the Overlay layer. This parameter determines what happens at the edges of the Overlay layer.
  * Hold `hold` - The pixel values at the edges of the Overlay layer continue to extend past that edge.
  * Zero `zero` - The image does not extend past the edges of the Overlay.
  * Repeat `repeat` - The image is repeated at the edges of the Overlay.
  * Mirror `mirror` - The image is mirrored at the edges of the Overlay.

> **NOTE:** All the transform parameters below affect the Overlay layer only.

- Rotate `r` - Rotates the Overlay layer. Increasing values rotate clockwise, decreasing values rotate counter-clockwise.
- Translate `t` - ⊞ - Translates the Overlay layer in x and y.
  * X `tx` -
  * Y `ty` -

- Translate Units `tunit` - Sets the units used in the Translate parameter.
- Scale `s` - ⊞ - Scales the Overlay layer in x and y.
  * X `sx` -
  * Y `sy` -

- Pivot `p` - ⊞ - Allows you to define the point about which the Overlay layer scales and rotates. Altering the pivot point produces different results depending on the Transform Order.
  * X `px` -
  * Y `py` -

- Pivot Units `punit` - Sets the units used in the Pivot parameter.
- Translate Step `tstep` - ⊞ - Translates the Overlay layers cumulatively, starting at the 3rd input (index 2). That layer is translated by the amount specified, the next layer is translated by 2 times that amount, the following layer by 3 times that amount and so on.
  * X `tstepx` -
  * Y `tstepy` -

- Translate Step Units `tstepunit` - Sets the units used in the Translate Step parameter
- Legacy Transform `legacyxform` - When enabled, will use the legacy method of building the transform matrix, which has inverted rotation and transform order.

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
Extra Information for the Composite TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
