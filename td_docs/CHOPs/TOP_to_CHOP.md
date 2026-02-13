---
url: https://docs.derivative.ca/TOP_to_CHOP
category: CHOPs
title: TOP_to_CHOP
---

# TOP to CHOP
## Summary

The TOP to CHOP converts pixels in a [TOP](https://docs.derivative.ca/TOP "TOP") image to [CHOP](https://docs.derivative.ca/CHOP "CHOP") channels. Each pixel color element (RGBA) is placed in a separate channel. Depending on the parameter options, the node will either create a single set of channels for the whole image or it can create a separate set of channels for each scanline (row).
A single pixel, rows of pixels, columns of pixels or rectangular regions can be extracted from the image. It is therefore important to be aware of how many pixels your source image is composed of.
The Exclude NaN and Active Mask parameters can be used to skip certain pixels so they are not included in the chop channels.
There is an optional input which supplies UV coordinates to sample the image. The input CHOP must contain 2 channels, for U and V. The first channel is always assumed to be U. The channels produced (red, green, blue and alpha) will be exactly as long as the input channel's length, with a value for each UV coordinate.
If you are grabbing pixels from a [Depth TOP](https://docs.derivative.ca/Depth_TOP "Depth TOP"), you will only get a single channel (the depth). This will be placed in the R channel.
[toptoCHOP_Class](https://docs.derivative.ca/ToptoCHOP_Class "ToptoCHOP Class")

## Parameters - Image Page
- TOP `top` - Specify the TOP operator whose image will be sampled.
- Download Type `downloadtype` - ⊞ - Gives the option for a delayed data download from the GPU, which is much faster and does not stall the render.
  * Immediate (Slow) `immediate` -
  * Next frame (Fast) `nextframe` -

- Red `r` - The prefix for channels created from the red pixels of the source image. If multiple red channels are created, they will have a numeric suffix that matches the vertical scanline number of the image e.g. `r0` - `r4`.
- Green `g` - The prefix for channels created from the green pixels of the source image. If multiple green channels are created, they will have a numeric suffix that matches the scanline number of the image e.g. `g0` - `g4`.
- Blue `b` - The prefix for channels created from the blue pixels of the source image. If multiple blue channels are created, they will have a numeric suffix that matches the scanline number of the image e.g. `b0` - `b4`.
- Alpha `a` - The prefix for channels created from the alpha pixels of the source image. If multiple alpha channels are created, they will have a numeric suffix that matches the scanline number of the image e.g. `a0` - `a4`.
- Output Color Space `outputcolorspace` - ⊞ - Controls what color space the data will be converted to before output. If the output (file/SDI/ST2110 etc) supports metadata, will also attempt to include the color space in that. Some output forms only support a limited number of color spaces in their metadata. If the color space is unknown to the output form, then no metadata will be included.
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

- Output Reference White `outputreferencewhite` - ⊞ - When converting the color values to the Working Color Space for output, this controls how they should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Output Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, and the project Working Color Space is HDR while the Output Color Space is SDR: then a color of (1, 1, 1), which is 80 nits in the HDR color space, will be converted to be (0.66, 0.66, 0.66), which is 80 nits still in the SDR Output Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
  * Standard (SDR) `sdr` - Will treat the Output Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Output Color Space as HDR for it's reference white value.

- Output as Single Channel Set `singleset` - Controls whether a channel is created for each scanline, or whether all scanlines are appended into a single channel set. A channel set refers to one CHOP channel per color channel of the source image e.g. 4 channels for an RGBA image.
- Exclude NaNs `excludenans` - When enabled, pixels that have a NaN value in any of their channels will be skipped and not added to the CHOP channel.
- Active Channel `activechannel` - ⊞ - When enabled, only pixels that have a non-zero value in the selected active channel will be added to the CHOP channel.
  * None `none` -
  * Red `red` -
  * Green `green` -
  * Blue `blue` -
  * Alpha `alpha` -

- RGBA Units `rgbaunit` - ⊞ - Scales the output to lie in the range 0-1, 0-255 or 0-65535.
  * 0 to 1 `u1` -
  * 0 to 255 `u256` -
  * 0 to 65535 `u65536` -

## Parameters - Crop Page
- Crop `crop` - ⊞ - Specifies what to extract from the image.
  * Pixel (U,V) `pixel` - Extract a single pixel at the given U and V value.
  * Row (U) `row` - Extract a single row at the given U value, cropped by the V Start and V End on the left and right.
  * Column (V) `col` - Extract a single column at the given V value, cropped by the U Start and U End on the bottom and top.
  * Rows and Columns `block` - Extract multiple rows and multiple columns, bound by the U/V Start/End parameters.
  * Full Image `full` - Extract the full image.

- UV Units `uvunits` - ⊞ - Specifies the units for the following 4 parameters. The parameters can use the local variables `$NR` and `$NC` for the number of rows and columns.
  * 0 to 1 `norm` -
  * Pixels `pixel` -

- U Start `ustart` - Starting point for sampling in U. Values outside the range of the image are determined by the image's extend conditions, in the extend page.
- U End `uend` - Ending point for sampling in U.
- V Start `vstart` - Starting point for sampling in V.
- V End `vend` - Ending point for sampling in V.
- Interpolate `interp` - ⊞ - Determines the interpolation method when UV sampling with an input CHOP.
  * Nearest Sample `nearest` -
  * Linear `linear` -

## Parameters - Extend Page
- Image Left `imageleft` - ⊞ - The image extend conditions when sampling the image with U less than 0.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Default Color `default` -

- Image Right `imageright` - ⊞ - The image extend conditions for U greater than 1.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Default Color `default` -

- Image Bottom `imagebottom` - ⊞ - The image extend conditions for V less than 0.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Default Color `default` -

- Image Top `imagetop` - ⊞ - The image extend conditions for V greater than 1.
The extend conditions are:
  * Hold `hold` - Use the first or last pixel value.
  * Cycle `cycle` - Loop back to the other side of the image.
  * Mirror `mirror` - Zig-zag back into the image.
  * Default Color `default` - Use a default color specified below.

- Default Color `defcolor` - ⊞ - The color to use when outside the bounds of the image, and the Default Color extend condition is set.
  * Red `defcolorr` -
  * Green `defcolorg` -
  * Blue `defcolorb` -
  * Alpha `defcolora` -

## Parameters - Channel Page
- Start `start` - The start position of the channel, expressed in units set by the units menu to the right (samples, frames or seconds). The channel length is determined by the number of pixels in each scanline that is converted into a channel.
- Start Unit `startunit` - ⊞ - Select the units to use for this parameter, Samples, Frames, or Seconds.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

- Extend Right `right` - ⊞ - The right extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter

- Default Value `defval` - The value used for the Default Value extend condition.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).
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

## Operator Inputs
  * Input 0:  -
