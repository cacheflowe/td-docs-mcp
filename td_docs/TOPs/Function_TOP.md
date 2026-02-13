---
url: https://docs.derivative.ca/Function_TOP
category: TOPs
title: Function_TOP
---

# Function TOP
## Summary

The Function TOP can perform mathematical operations like sin, cos, or exp on the color values of the input image. Different functions can be performed on each color channel. Some functions will take an additional value from the Base, Exponent or Constant Value parameters, and some functions take an additional input value from the second input image.
For some functions, you can use the 'Replace Errors' parameter to insert a new value for values that would otherwise be undefined e.g. log(-1)
##### Supported functions:
  * _Input_ - Pass along the input value unchanged
  * _Constant_ - Replace the input with the value of the 'Constant' parameter.
  * _Square Root_ - Find the square root of the input value i.e. sqrt(x).
  * _Absolute Value_ - Get the absolute value of the input i.e. abs(x).
  * _Sign_ - Returns -1 if the input value is below 0, 0 if it equals 0, and 1 if it's greater than zero.
  * _Cosine_ - Returns the cosine of the input. 1
  * _Sine_ - Returns the sine of the input. 1
  * _Tangent_ - Returns the tangent of the input. 1
  * _Arccosine_ - Returns the arccosine of the input i.e. acos(x). 1
  * _Arcsine_ - Returns the sine of the input i.e. asin(x). 1
  * _Arctan (Input1)_ - Returns the arctangent of the input i.e. atan(x). 1
  * _Arctan (Input1 / Input2)_ - Returns the arctangent of input1 over input2 i.e. atan(x,y). 1
  * _Hyperbolic Cosine_ - Returns the hyperbolic cosine of the input i.e. cosh(x). 1
  * _Hyperbolic Sine_ - Returns the sine of the input i.e. sinh(x). 1
  * _Hyperbolic Tangent_ - Returns the tangent of the input i.e. tanh(x). 1
  * _Log Base 10_ - Returns the base 10 logarithm of the input i.e. log10(x).
  * _Log Base 2_ - Returns the base 2 logarithm of the input i.e. log2(x).
  * _Log Base N_ - Returns the base N logarithm of the input, where N is set by the 'Base Value' parameter.
  * _Natural Log_ - Returns the natural log of the input i.e. ln(x).
  * _Exponent_ - Returns e to the power of the input i.e. e^x.
  * _Exponent 2_ - Returns 2 to the power of the input i.e. 2^x.
  * _Exponent 10_ - Returns 10 to the power of the input i.e. 10^x.
  * _Base Power_ - Returns the 'Base Value' parameter to the power of x. 2
  * _Input1 ^ Exponent_ - Returns the input value to the power of the exponent parameter. 2
  * _Input1 ^ Input2_ - Returns the value of input 1 to the power of input 2. 2
  * _dB to Power_ - Converts decibels to power.
  * _Power to dB_ - Converts power to decibels. The result will be an error if the value is less than or equal to zero.
  * _dB to Amplitude_ - Converts decibels to amplitude.
  * _Amplitude to dB_ - Converts amplitude to decibels. The result will be an error if the value is less than or equal to zero.

1 The unit of the input for this function is determined by the 'Angle Units' parameter e.g. degrees, radians, etc.
2 Using a negative exponent i.e. pow(x, -2) will produce an error value since negative exponents are undefined according to the GLSL specifications.
**Note:** This TOP supports 3D Textures and 2D Texture Arrays.
[functionTOP_Class](https://docs.derivative.ca/FunctionTOP_Class "FunctionTOP Class")

## Parameters - Function Page
- Re-Range Integers `rerange` - ⊞ - Applies a scale and shift to the input values before the function is calculated i.e. input = (input * rerange2) + rerange1. **Note:** This feature only affects integer texture formats and is not used on floating point formats.
  * Re-Range Integers `rerange1` -
  * Re-Range Integers `rerange2` -

- Function RGBA `funcrgba` - ⊞ - Applies the selected function to the R, G, B, and A channels.
  * x Input `input` -
  * Constant Value `constant` -
  * sqrt(x) Square Root `sqrt` -
  * abs(x) Absolute Value `abs` -
  * sign(x) Sign `sign` -
  * cos(x) Cosine `cos` -
  * sin(x) Sine `sin` -
  * tan(x) Tangent `tan` -
  * acos(x) Arccosine `acos` -
  * asin(x) Arcsine `asin` -
  * atan(x) Arctan ( Input1 ) `atan` -
  * atan2(x,y) Arctan ( Input1 / Input2 ) `atan2` -
  * cosh(x) Hyperbolic Cosine `cosh` -
  * sinh(x) Hyperbolic Sine `sinh` -
  * tanh(x) Hyperbolic Tangent `tanh` -
  * log10(x) Log Base 10 `log10` -
  * log2(x) Log Base 2 `log2` -
  * logN(x) Log Base N `logn` -
  * ln(x) Natural Log `ln` -
  * exp(x) e ^ Input1 `exp` -
  * exp2(x) 2 ^ Input1 `exp2` -
  * exp10(x) 10 ^ Input1 `exp10` -
  * pow(x) Base ^ Input1 `powb` -
  * pow(x) Input1 ^ Exponent `powe` -
  * pow(x,y) Input1 ^ Input2 `powxy` -
  * dB to Power `dbtopow` -
  * Power to dB `powtodb` -
  * dB to Amplitude `dbtoamp` -
  * Amplitude to dB `amptodb` -

- Function RGB `funcrgb` - ⊞ - Applies the selected function to the R, G, and B channels.
  * x Input `input` -
  * Constant Value `constant` -
  * sqrt(x) Square Root `sqrt` -
  * abs(x) Absolute Value `abs` -
  * sign(x) Sign `sign` -
  * cos(x) Cosine `cos` -
  * sin(x) Sine `sin` -
  * tan(x) Tangent `tan` -
  * acos(x) Arccosine `acos` -
  * asin(x) Arcsine `asin` -
  * atan(x) Arctan ( Input1 ) `atan` -
  * atan2(x,y) Arctan ( Input1 / Input2 ) `atan2` -
  * cosh(x) Hyperbolic Cosine `cosh` -
  * sinh(x) Hyperbolic Sine `sinh` -
  * tanh(x) Hyperbolic Tangent `tanh` -
  * log10(x) Log Base 10 `log10` -
  * log2(x) Log Base 2 `log2` -
  * logN(x) Log Base N `logn` -
  * ln(x) Natural Log `ln` -
  * exp(x) e ^ Input1 `exp` -
  * exp2(x) 2 ^ Input1 `exp2` -
  * exp10(x) 10 ^ Input1 `exp10` -
  * pow(x) Base ^ Input1 `powb` -
  * pow(x) Input1 ^ Exponent `powe` -
  * pow(x,y) Input1 ^ Input2 `powxy` -
  * dB to Power `dbtopow` -
  * Power to dB `powtodb` -
  * dB to Amplitude `dbtoamp` -
  * Amplitude to dB `amptodb` -

- Function R `funcr` - ⊞ - Applies the selected function to the R (red) channel.
  * x Input `input` -
  * Constant Value `constant` -
  * sqrt(x) Square Root `sqrt` -
  * abs(x) Absolute Value `abs` -
  * sign(x) Sign `sign` -
  * cos(x) Cosine `cos` -
  * sin(x) Sine `sin` -
  * tan(x) Tangent `tan` -
  * acos(x) Arccosine `acos` -
  * asin(x) Arcsine `asin` -
  * atan(x) Arctan ( Input1 ) `atan` -
  * atan2(x,y) Arctan ( Input1 / Input2 ) `atan2` -
  * cosh(x) Hyperbolic Cosine `cosh` -
  * sinh(x) Hyperbolic Sine `sinh` -
  * tanh(x) Hyperbolic Tangent `tanh` -
  * log10(x) Log Base 10 `log10` -
  * log2(x) Log Base 2 `log2` -
  * logN(x) Log Base N `logn` -
  * ln(x) Natural Log `ln` -
  * exp(x) e ^ Input1 `exp` -
  * exp2(x) 2 ^ Input1 `exp2` -
  * exp10(x) 10 ^ Input1 `exp10` -
  * pow(x) Base ^ Input1 `powb` -
  * pow(x) Input1 ^ Exponent `powe` -
  * pow(x,y) Input1 ^ Input2 `powxy` -
  * dB to Power `dbtopow` -
  * Power to dB `powtodb` -
  * dB to Amplitude `dbtoamp` -
  * Amplitude to dB `amptodb` -

- Function G `funcg` - ⊞ - Applies the selected function to the G (green) channel.
  * x Input `input` -
  * Constant Value `constant` -
  * sqrt(x) Square Root `sqrt` -
  * abs(x) Absolute Value `abs` -
  * sign(x) Sign `sign` -
  * cos(x) Cosine `cos` -
  * sin(x) Sine `sin` -
  * tan(x) Tangent `tan` -
  * acos(x) Arccosine `acos` -
  * asin(x) Arcsine `asin` -
  * atan(x) Arctan ( Input1 ) `atan` -
  * atan2(x,y) Arctan ( Input1 / Input2 ) `atan2` -
  * cosh(x) Hyperbolic Cosine `cosh` -
  * sinh(x) Hyperbolic Sine `sinh` -
  * tanh(x) Hyperbolic Tangent `tanh` -
  * log10(x) Log Base 10 `log10` -
  * log2(x) Log Base 2 `log2` -
  * logN(x) Log Base N `logn` -
  * ln(x) Natural Log `ln` -
  * exp(x) e ^ Input1 `exp` -
  * exp2(x) 2 ^ Input1 `exp2` -
  * exp10(x) 10 ^ Input1 `exp10` -
  * pow(x) Base ^ Input1 `powb` -
  * pow(x) Input1 ^ Exponent `powe` -
  * pow(x,y) Input1 ^ Input2 `powxy` -
  * dB to Power `dbtopow` -
  * Power to dB `powtodb` -
  * dB to Amplitude `dbtoamp` -
  * Amplitude to dB `amptodb` -

- Function B `funcb` - ⊞ - Applies the selected function to the B (blue) channel.
  * x Input `input` -
  * Constant Value `constant` -
  * sqrt(x) Square Root `sqrt` -
  * abs(x) Absolute Value `abs` -
  * sign(x) Sign `sign` -
  * cos(x) Cosine `cos` -
  * sin(x) Sine `sin` -
  * tan(x) Tangent `tan` -
  * acos(x) Arccosine `acos` -
  * asin(x) Arcsine `asin` -
  * atan(x) Arctan ( Input1 ) `atan` -
  * atan2(x,y) Arctan ( Input1 / Input2 ) `atan2` -
  * cosh(x) Hyperbolic Cosine `cosh` -
  * sinh(x) Hyperbolic Sine `sinh` -
  * tanh(x) Hyperbolic Tangent `tanh` -
  * log10(x) Log Base 10 `log10` -
  * log2(x) Log Base 2 `log2` -
  * logN(x) Log Base N `logn` -
  * ln(x) Natural Log `ln` -
  * exp(x) e ^ Input1 `exp` -
  * exp2(x) 2 ^ Input1 `exp2` -
  * exp10(x) 10 ^ Input1 `exp10` -
  * pow(x) Base ^ Input1 `powb` -
  * pow(x) Input1 ^ Exponent `powe` -
  * pow(x,y) Input1 ^ Input2 `powxy` -
  * dB to Power `dbtopow` -
  * Power to dB `powtodb` -
  * dB to Amplitude `dbtoamp` -
  * Amplitude to dB `amptodb` -

- Function A `funca` - ⊞ - Applies the selected function to the A (alpha) channel.
  * x Input `input` -
  * Constant Value `constant` -
  * sqrt(x) Square Root `sqrt` -
  * abs(x) Absolute Value `abs` -
  * sign(x) Sign `sign` -
  * cos(x) Cosine `cos` -
  * sin(x) Sine `sin` -
  * tan(x) Tangent `tan` -
  * acos(x) Arccosine `acos` -
  * asin(x) Arcsine `asin` -
  * atan(x) Arctan ( Input1 ) `atan` -
  * atan2(x,y) Arctan ( Input1 / Input2 ) `atan2` -
  * cosh(x) Hyperbolic Cosine `cosh` -
  * sinh(x) Hyperbolic Sine `sinh` -
  * tanh(x) Hyperbolic Tangent `tanh` -
  * log10(x) Log Base 10 `log10` -
  * log2(x) Log Base 2 `log2` -
  * logN(x) Log Base N `logn` -
  * ln(x) Natural Log `ln` -
  * exp(x) e ^ Input1 `exp` -
  * exp2(x) 2 ^ Input1 `exp2` -
  * exp10(x) 10 ^ Input1 `exp10` -
  * pow(x) Base ^ Input1 `powb` -
  * pow(x) Input1 ^ Exponent `powe` -
  * pow(x,y) Input1 ^ Input2 `powxy` -
  * dB to Power `dbtopow` -
  * Power to dB `powtodb` -
  * dB to Amplitude `dbtoamp` -
  * Amplitude to dB `amptodb` -

- Base Value `baseval` - Supplies the base value for functions like 'Log Base N' and 'Base ^ Input'
- Exponent Value `expval` - Supplies the exponent value for the function 'Input ^ Base'.
- Constant Value `constval` - Allows setting the output to a specific constant value using the 'Constant' function.
- Angle Units `angunit` - ⊞ - Determines whether the input values are measured in degrees, radians, etc for functions that require an angle input e.g. sine, cosine, etc.
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -

- Replace Errors `replace` - When enabled, output values that would otherwise be invalid will be replaced with the value of the 'Error Value' parameter. For example, when using the log function, the output will be replaced whenever the input value is less than zero.
- Error Value `errval` - The output value to use when an input error is detected e.g. log(-1).

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
Extra Information for the Function TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
