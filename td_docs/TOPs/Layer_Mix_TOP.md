---
url: https://docs.derivative.ca/Layer_Mix_TOP
category: TOPs
title: Layer_Mix_TOP
---

# Layer Mix TOP
## Summary

The Layer Mix TOP lets you composite unlimited image layers and do adjustments, all within one node.
Each of the inputs gets a block of parameters that you can use to modify the incoming images.
The possible built-in controls per-layer include crop, pre-fit, justify, extend, scale, rotate, translate, pivot and then layer transparency, gamma and level, and finally the composite (blend) operation.
To avoid clutter, on the first page you choose which controls you want to be per-layer.
The entire mixing of layers is done with one single-pass shader that is generated on-the-fly.
You can composite back to front, or front-to-back.
You can specify a large background plate (image or constant) to composite your layers over. The background plate can be a constant-colored image with the resolution of the first input, or defined as a width-height on the Common page, or a separate TOP image.
The inputs can be a mix of wired inputs and references to TOPs using pattern matching of names.
[layermixTOP_Class](https://docs.derivative.ca/LayermixTOP_Class "LayermixTOP Class")

## Parameters - Setup Page
- Background `background` - ⊞ - This menu determines which background plate to use while compositing.
  * Off `off` - No background is used. There must be at least two layer sources provided as inputs if there is no background.
  * Background TOP `backgroundtop` - Another TOP's output image will be used as the background.
  * Constant Layer `constlayer` - A constant RGBA value will be used as the background.

- Size `size` - ⊞ - This menu determines the resolution of the output image. This parameter does not affect what gets composited, regardless of which menu item is selected. It only controls the output resolution.
  * First Input `firstinput` - The resolution is the same size as the first wired input.
  * Background TOP `bgtopsize` - The resolution is the same size as another TOP's output resolution.
  * Output Resolution `outputres` - The resolution is defined by the Resolution parameter on the Common page.

- Background TOP `bgtop` - The path of the Background TOP being referenced. The Background and Size parameters will share the same TOP if the Background TOP menu item is selected for both menus.
- Background Color `bgcolor` - ⊞ - Sets the red, green, blue, and alpha color channels if the Constant Layer menu item is selected for the Background parameter.
  * Background Color `bgcolorr` -
  * Background Color `bgcolorg` -
  * Background Color `bgcolorb` -
  * Background Color `bgcolora` -

- Enable Crop `enablecrop` - Adds crop (left, right, bottom, top) parameters to each layer. If disabled, each layer will have default UV bounds of (0, 1, 0, 1).
- Crop Unit `cropunit` - ⊞ - Sets the units used by the Crop parameter for each layer.
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- Pre-Fit Layer `prefit` - ⊞ - Determines how each layer fills the composite.
  * Per Layer `prefitperlayer` - Adds Pre-Fit Layer menu parameters to each layer, allowing layers to independently adjust their pre-fits.
  * Fill `fill` - All layers are stretched/squashed to fill the resolution and aspect ratio of the output resolution.
  * Fit Horizontal `fithorz` - All layers are stretched/squashed to fit the output resolution horizontally.
  * Fit Vertical `fitvert` - All layers are stretched/squashed to fit the output resolution vertically.
  * Fit Best `fitbest` - All layers are stretch/squashed to fit the output resolution using the best possible match that does not crop any of the layer. The aspect ratio of the layer is maintained.
  * Fit Outside `fitoutside` - All layers are stretched squashed to fit the output resolution using the worst possible match. This is the opposite of Fit Best. The aspect ratio of the layer is maintained.
  * Native Resolution `nativeres` - All layers are not squashed or stretched. The layers use their own resolution and aspect ratio during the composite. Pixel accurate composites require Native Resolution. Use this setting to maintain an image's original resolution during the composite.

- Enable Justify `enablejust` - Adds justify parameters to each layer. If disabled, each layer will default to center horizontal and center vertical alignment.
- Extend `extend` - ⊞ - Sets the extend (or repeat) conditions of the layers. This parameter determines what happens at the edges of the layers.
  * Per Layer `extperlayer` - Adds Extend menu parameters to each layer, allowing layers to independently adjust their extend conditions.
  * Hold `hold` - The pixel values at the edges of all layers continue to extend past that edge.
  * Zero `zero` - The image does not extend past the edges of all layers.
  * Repeat `repeat` - The image is repeated at the edges of all layers.
  * Mirror `mirror` - The image is mirrored at the edges of all layers.

- Scale `scalemode` - ⊞ - Adds scale parameters to the layers.
  * Off `off` - No scale parameters are added, so x and y scales are defaulted to 1.
  * Uniform `uniform` - Adds a uniform scale parameter to each layer that scales the x and y axes simultaneously.
  * XY `xy` - Adds an x and y scale parameter to each layer.
  * XY + Uniform `xyuniform` - Adds both x and y and uniform scale parameters to each layer.

- Enable Rotate `enabler` - Adds rotation parameters to each layer. If disabled, each layer will have default rotation of 0.
- Enable Translate `enablet` - Adds translation parameters to each layer. If disabled, each layer will have default translation of 0.
- Enable Pivot `enablep` - Adds pivot parameters to each layer. If disabled, each layer will default the pivot to the center of the layer.
- Translate / Pivot Unit `transpvtunit` - ⊞ - Sets the units used by the Translate and Pivot parameters for each layer.
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- Enable Opacity `enableopac` - Adds opacity parameters to each layer. If disabled, each layer will have default opacity of 1. Setting a layer's opacity to 0 can be used to optimize the Layer Mix TOP to stop wired input nodes from cooking if it isn't being displayed.
- Enable Brightness `enablebright` - Adds brightness parameters to each layer. If disabled, each layer will have default brightness of 1.
- Enable Levels `enablelevels` - Adds black level and gamma parameters to each layer, using Luma Level TOP's algorithm. If disabled, each layer will have default black level of 0 and gamma of 1.
- Operation / Swap `operand` - ⊞ - Sets the composite (blend) operation and swap order for the layers.
  * Operation / Swap `operand` - If set to Per Layer, it will add Operation / Swap parameters to each layer. If set to a blend operation, this parameter will apply the operation to all layers.
  * Swap Order `swaporder` - Swaps the order of all input pairs. A operation B is changed to B operation A. Operations like Add don't matter, but many do, like Over and Hard Light. If the Operation parameter is set to Per Layer, each layer will have its own Swap Order parameter to allow for swapping of specific layers.

- Composite Order `comporder` - ⊞ - Sets the compositing order of the layers. Front to Back means the first input will be layered at the top of the compositing stack. Back to Front means the first input will be layered at the bottom of the compositing stack.
[![LayerMixTOP Composite Order.png](https://docs.derivative.ca/images/thumb/5/58/LayerMixTOP_Composite_Order.png/450px-LayerMixTOP_Composite_Order.png)](https://docs.derivative.ca/File:LayerMixTOP_Composite_Order.png)
  * Front to Back `fronttoback` - Compositing follows this order: (((Input_0 op_0 Input_1) op_1 Input_2) op_2 Background). If there is no background plate, op_2 and Background are ignored.
  * Back to Front `backtofront` - Compositing follows this order: (Input_2 op_2 (Input_1 op_1 (Input_0 op_0 Background))). If there is no background plate, op_0 and Background are ignored.

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

- Parameter Color Space `parmcolorspace` - ⊞ - Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space.
  * sRGB `srgb` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
  * sRGB - Linear `srgblinear` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.601 (NTSC) `rec601ntsc` - [Rec.601](https://en.wikipedia.org/wiki/Rec._601) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.709 `rec709` - [Rec.709](https://en.wikipedia.org/wiki/Rec._709) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.2020 `rec2020` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 `dcip3` - [DCI-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 (D60) `dcip3d60` - [DCI-P3 "D60 sim"](https://en.wikipedia.org/wiki/DCI-P3) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) `displayp3d65` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACES2065-1 `aces2065-1` - [ACES 2065-1](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACEScg `acescg` - [ACEScg](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Passthrough `passthrough` - When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.

- Parameter Reference White `parmreferencewhite` - ⊞ - When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space selected.
  * Use Parent Panel `useparent` - Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
  * Standard (SDR) `sdr` - Will treat the Parameter Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Parameter Color Space as HDR for it's reference white value.
  * UI `ui` - Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## Parameters - Layers Page
- Layer `lay` - Sequence of layers.
- TOP / Bypass `lay0top` - ⊞ - Sets the path and bypass for the layers.
  * TOP / Bypass `lay0top` - The path of inputs. If there are wired inputs, it will override and disable this parameter in sequential order.
  * Bypass `lay0bypass` - Bypassing the layer will ignore the layer when compositing. Bypassing a layer can be used to optimize the Layer Mix TOP to stop wired input nodes from cooking if it isn't being displayed.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Layer Mix TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
