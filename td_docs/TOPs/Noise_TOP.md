---
url: https://docs.derivative.ca/Noise_TOP
category: TOPs
title: Noise_TOP
---

# Noise TOP
## Summary

The Noise TOP generates a variety of noise patterns including perlin, simplex, sparse, alligator and random. Some types of noise run on the CPU, while others are calculated on the GPU. The ones that are calculated on the GPU will have GPU in their name.
The first input can be combined with the generated noise in various ways depending on the parameters.
The second input can be used to specify noise coordinates per-pixel. Without a 2nd input connected, the noise coordinates are the 0-1 texture coordinates of the output texture, i.e, the position of the pixel in the output texture. With a 2nd input connected the position of the pixel in the output texture is used to look-up into the 2nd input, and the RGBA of the 2nd input for that sampled pixel will be used as the XYZ and W for the noise coordinate.
**Note:** This TOP supports 3D Textures and 2D Texture Arrays. For this TOP to generate a 3D texture output, it requires a 3D texture type as input. You can use a [Texture 3D TOP](https://docs.derivative.ca/Texture_3D_TOP "Texture 3D TOP") or [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP") to create 3D texture types.
[noiseTOP_Class](https://docs.derivative.ca/NoiseTOP_Class "NoiseTOP Class")

## Parameters - Noise Page
- Type `type` - ⊞ - The noise function used to generate noise. The functions available are:
  * Perlin 2D (GPU) `perlin2d` - Perlin noise function calculated on the GPU. Choose between 2, 3, and 4 dimensional functions.
  * Perlin 3D (GPU) `perlin3d` - Perlin noise function calculated on the GPU. Choose between 2, 3, and 4 dimensional functions.
  * Perlin 4D (GPU) `perlin4d` - Perlin noise function calculated on the GPU. Choose between 2, 3, and 4 dimensional functions.
  * Simplex 2D (GPU) `simplex2d` - Simplex noise function calculated on the GPU. Choose between 2, 3, and 4 dimensional functions.
  * Simplex 3D (GPU) `simplex3d` - Simplex noise function calculated on the GPU. Choose between 2, 3, and 4 dimensional functions.
  * Simplex 4D (GPU) `simplex4d` - Simplex noise function calculated on the GPU. Choose between 2, 3, and 4 dimensional functions.
  * Random (GPU) `randomgpu` - Every sample is randomly generated, calculated on the GPU.
  * Sparse `sparse` - Produces high quality, continuous noise based on Sparse Convolution.
  * Hermite `hermite` - Quicker than Sparse, but produces lower quality noise.
  * Harmomic Summation `harmonic` - Sparse noise with the ability to control the frequency step of the harmonics. Slowest type.
  * Random `random` - (White Noise) Every sample is random and unrelated to any other sample. It is the same as "white noise" in audio.
  * Alligator `alligator` - Cell Noise.

- Seed `seed` - Any number, integer or non-integer, which starts the random number generator. Each number gives completely different noise patterns, but with similar characteristics.
- Period `period` - The approximate separation between peaks of a noise cycle. It is expressed in Units. Increasing the period stretches the noise pattern out.
Period is the opposite of frequency. If the period is 2 seconds, the base frequency is 0.5 cycles per second, or 0.5Hz for short. Hz refers to Hertz, the electrical and audio engineer of the 19th century, not the car guy.
If the Type is set to Random, setting this to zero will produce completely random noise. Otherwise, the period should be greater than zero.
- Harmonics `harmon` - The number of higher frequency components to layer on top of the base frequency. The higher this number, the bumpier the noise will be (as long as roughness is not set to zero). 0 harmonics give the base shape.
- Harmonic Spread `spread` - The factor by which the frequency of the harmonics are increased. It is normally 2. A spread of 3 and a base frequency of 0.1Hz will produce harmonics at 0.3Hz, 0.9Hz, 2.7Hz, etc.. This parameter is only valid for the Harmonic Summation type.
- Harmonic Gain `gain` - Amount of the Harmonic Gain layered on top of the base frequency.
- Roughness `rough` - Controls the effect of the higher frequency noise. When roughness is zero, all harmonics above the base frequency have no effect. At one, all harmonics are equal in amplitude to the base frequency. When roughness is between one and zero, the amplitude of higher harmonics drops off exponentially from the base frequency.
The default roughness is 0.5. This means the amplitude of the first harmonic is 0.5 of the base frequency, the second is 0.25, the third is 0.125. The harmonics are added to the base to give the final shape. The Harmonics parameter and the Roughness parameter must both be non-zero to see the harmonic effects.
- Exponent `exp` - Pushes the noise values toward 0, or +1 and -1. (It raises the value to the power of the exponent.) Exponents greater than one will pull the channel toward zero, and powers less than one will pull peaks towards +1 and -1. It is used to reshape the channels.
- Amplitude `amp` - Defines the noise value's amplitude (a scale on the values output).
- Offset `offset` - Defines the midpoint color of the noise pattern, the default is 0.5 grey.
- Monochrome `mono` - Toggle color or monochrome noise.
- Aspect Correct `aspectcorrect` - Controls if the noise takes aspect ratio into account when calculating it's noise coordinates. When this is off, the noise will stretch to fit a non-square aspect ratio texture.

## Parameters - Transform Page
The Translate, Rotate, Scale and Pivot parameters let you sample in a different part of the 3D noise space. Imagine a different noise value for every XYZ point in space. Normally, the Noise CHOP samples the noise space from (0,0,0) along the X-axis in steps of 2/period. By changing the transform, you are translating, rotating and scaling the plane along which the Noise TOPs samples the noise space. A slight Y-rotation is like walking in a straight path in the mountains, recording your altitude along the way, then re-starting from the same initial location, walking in a slightly different direction. Your altitude starts off being similar but then diverges.
- Transform Order `xord` - ⊞ - The menu attached to this parameter allows you to specify the order in which the transforms will take place. Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - The rotational matrix presented when you click on this option allows you to set the transform order for the rotations. As with transform order (above), changing the order in which the rotations take place will alter the final position.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - Translate the sampling plane through the noise space.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - Rotate the sampling plane in the noise space.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - Scale the sampling plane.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - Control the pivot for the transform of the sampling plane.
  * X `px` -
  * Y `py` -
  * Z `pz` -

- Translate 4D `t4d` - When doing 4D noise, this applies a translation to the 4th coordinate. The previous transformation parameters do not affect the 4th coordinate.
- Scale 4D `s4d` - When doing 4D noise, this applies a scale to the 4th coordinate.

## Parameters - Output Page
- RGB `rgb` - ⊞ - When an input is connected to the Noise TOP, the noise pattern is placed over the input image using UV coordinates and the settings from this menu.
  * Noise `noise` - Just the noise is output.
  * Input * Noise `multiply` - The noise is multiplied with the input.
  * Input + Noise `add` - The input is added to the noise.
  * Input - Noise `subtract` - The input is subtracted from the noise.

- Input Scale `inputscale` - Adjusts how much of the input image is added to the output.
- Noise Scale `noisescale` - Adjusts how much of the noise is added to the output.
- Alpha `alpha` - ⊞ - Sets the alpha channel for the output image.
  * Zero `zero` - Alpha channel is zero.
  * One `one` - Alpha channel is one.
  * Noise `random` - Alpha channel is random noise.
  * Input `input` - Alpha is the pass through from the input.
  * Input * Noise `multiply` - Alpha is the result of the input's alpha channel * the noise.
  * Input + Noise `add` - Alpha is the result of the input's alpha channel + the noise.
  * Input + clamp(Noise) `addclamp` - Alpha is the result of the input's alpha channel + the noise but clamped around [0-1].

- Dither `dither` - Dithers the output to help deal with banding and other artifacts created by precision limitations of 8-bit displays.
- Gradient `gradient` - Turn this on to output the gradient (also known as slope) of the noise function. Currently, only supported for Performance mode Simplex and Perlin noise types. For 2D noise derivatives, the RG channels get populated with the XY derivatives. For 3D, the RGB channels get populated with the XYZ derivatives. And for 4D, the RGBA channels get populated with XYZW derivatives. Note that this calculates derivative of the noise function not derivatives along the noise image.
- Mode `mode` - ⊞ - Pick between Performance vs Quality noise. Performance noise is the existing TD noise. Quality noise reduces certain artifacts and axis alignment issues with the existing noise at the cost of speed. Currently only enabled for Simplex Noise type.
  * Performance `performance` - Performant noise.
  * Quality `quality` - Quality noise.

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

## Operator Inputs
  * Input 0: Composite Input - Control the Composite operation via the parameters on the Output Page of this operator.
  * Input 1: Noise Coordinate Map - A texture specifying the 2, 3 or 4 dimensional lookup into the noise field.

## Info CHOP Channels
Extra Information for the Noise TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
