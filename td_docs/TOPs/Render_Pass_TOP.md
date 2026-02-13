---
url: https://docs.derivative.ca/Render_Pass_TOP
category: TOPs
title: Render_Pass_TOP
---

# Render Pass TOP
## Summary

The Render Pass TOP is used along with a [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") to achieve multipass rendering. It can build upon its inputs render by using the existing depth/color information in the framebuffers, or it can optionally clear one or both of the depth/color buffers before it does its render.
[renderpassTOP_Class](https://docs.derivative.ca/RenderpassTOP_Class "RenderpassTOP Class")

## Parameters - Render Pass Page
- Render/RenderPass TOP `renderinput` - The network path to the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") used as input. This parameter can be used as an alternate to connecting a Render or Render Pass TOP to the Render Pass's input connector. Makes it easier to select a render from another network.
- Camera `camera` - Specifies which [Cameras](https://docs.derivative.ca/Camera_COMP "Camera COMP") to look through when rendering the scene.
- Geometry `geometry` - Specifies which [Geometry](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") will be included in the rendered scene. You can use [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") to specify objects using patterns. Example: `geo* ^geo7` will render all Geometry components whose names start with `geo` except `geo7`.
- Lights `lights` - Specifies which [Lights](https://docs.derivative.ca/Light_COMP "Light COMP") will be used to render the scene. You can use [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") here as well.
- Clear to Camera Color `cleartocamcolor` - Clears the values that are currently in the color buffer (coming from the TOP that is wired to the input of this node).
- Clear Depth Buffer `cleardepth` - Clears the values that are currently in the depth buffer (coming from the TOP that is wired to the input of this node).
- Positive Sides `posside` - ⊞ - When Render Mode is Cube Map, specify which sides if the cube map are rendered, +X, +Y, or +Z.
  * Positive Sides `possidex` -
  * Positive Sides `possidey` -
  * Positive Sides `possidez` -

- Negative Sides `negside` - ⊞ - When Render Mode is Cube Map, specify which sides if the cube map are rendered, -X, -Y, or -Z.
  * Negative Sides `negsidex` -
  * Negative Sides `negsidey` -
  * Negative Sides `negsidez` -

- Transparency `transparency` - ⊞ - Refer to to the same parameter in the [Render TOPs](https://docs.derivative.ca/Render_TOP "Render TOP") help page.
  * Sorted Draw with Blending `sortedblending` -
  * Order Independent Transparency `orderind` -
  * Alpha-to-Coverage `alphatocoverage` -

- Depth Peel `depthpeel` - Refer to to the same parameter in the [Render TOPs](https://docs.derivative.ca/Render_TOP "Render TOP") help page.
- Transparency/Peel Layers `transpeellayers` - Refer to to the same parameter in the [Render TOPs](https://docs.derivative.ca/Render_TOP "Render TOP") help page.

## Parameters - Advanced Page
- Render `render` - Enables rendering; 1 = on, 0 = off.
- Dither `dither` - Dithers the rendering to help deal with banding and other artifacts created by precision limitations of 8-bit displays.
- Color Output Needed `coloroutputneeded` - This is an optimization if you don't actually need the color result from this pass. Turning this off avoids a copy from the offscreen render buffer to the TOP's texture. When anti-aliasing is enabled turning this off will also avoid 'resolving' the anti-aliasing.
- Draw Depth Only `drawdepthonly` - This will cause the render to only draw depth values to the depth buffer. No color values will be created. To make use of the depth buffer, use the [Depth TOP](https://docs.derivative.ca/Depth_TOP "Depth TOP").
- Allow Blending for Extra Buffers `allowbufblending` - ⊞ - Controls if blending (as enabled by the MAT common page setting) will be enabled for extra buffers beyond the first one. Often the extra buffers are used to write other types of information such as normals or positions, where blending wouldn't be desirable.
  * Off `off` -
  * On `on` -
  * Use Input Setting `useinput` -

- Cull Face `cullface` - ⊞ - Front Faces, Back Faces, Both Faces, Neither. Will cause the render to avoid rendering certain polygon faces depending on their orientation to the camera. Refer to [Back-Face Culling](https://docs.derivative.ca/Back-Face_Culling "Back-Face Culling") for more information.
  * Neither `neither` -
  * Back Faces `backfaces` -
  * Front Faces `frontfaces` -
  * Both Faces `bothfaces` -

- Override Material `overridemat` - This allows you to specific a material that will be applied to every Geometry that is rendered in the Render TOP. It is useful for pre-processing passes where we are outputting infoformation about the geometry rather then lighting them and outputting RGB.
- Polygon Depth Offset `polygonoffset` - This feature pushes the polygons back into space a tiny fraction. This is useful when you are rendering two polygons directly ontop of each other and are experiencing [Z-Fighting](https://docs.derivative.ca/Z-Fighting "Z-Fighting"). Refer to [Polygon Depth Offset](https://docs.derivative.ca/Polygon_Depth_Offset "Polygon Depth Offset") for more information. This is also an important feature when doing shadows.
- Offset Factor `polygonoffsetfactor` - Refer to to the same parameter in the [Render TOPs](https://docs.derivative.ca/Render_TOP "Render TOP") help page.
- Offset Units `polygonoffsetunits` - Refer to to the same parameter in the [Render TOPs](https://docs.derivative.ca/Render_TOP "Render TOP") help page.
- Display Overdraw `overdraw` - This feature visually shows the overdraw in the scene. Refer to the [Early Depth-Test](https://docs.derivative.ca/Early_Depth-Test "Early Depth-Test") article for more information. In particular the Analyzing Overdraw section.
- Overdraw Limit `overdrawlimit` - This value quantizes the outputted color value to some # of overdraws. Refer to the [Early Depth-Test](https://docs.derivative.ca/Early_Depth-Test "Early Depth-Test") for more information.

## Parameters - Crop Page
- Crop Left `cropleft` - Positions the left edge of the rendered image.
- Crop Left Unit `cropleftunit` - ⊞ - Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio).
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- Crop Right `cropright` - Positions the right edge of the rendered image.
- Crop Right Unit `croprightunit` - ⊞ - Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio).
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- Crop Bottom `cropbottom` - Positions the bottom edge of the rendered image.
- Crop Bottom Unit `cropbottomunit` - ⊞ - Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio).
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

- Crop Top `croptop` - Positions the top edge of the rendered image.
- Crop Top Unit `croptopunit` - ⊞ - Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio).
  * P `pixels` -
  * F `fraction` -
  * A `fractionaspect` -

## Parameters - Samplers Page
- Sampler `sampler` -
- Name `sampler0name` - This is the sampler name that the GLSL program will use to sample from this TOP. The samplers need to be declared as the same dimensions as the TOP (sampler2D for a 2D TOP, sampler3D for 3D TOP).
- TOP `sampler0top` - ⊞ - This is the TOP that will be referenced by the above sampler name above it.
- Extend U `sampler0extendu` - ⊞ -
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Extend V `sampler0extendv` - ⊞ -
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Extend W `sampler0extendw` - ⊞ -
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Filter `sampler0filter` - ⊞ -
  * Nearest `nearest` -
  * Linear `linear` -
  * Mipmap Linear `mipmaplinear` -

- Anisotropic Filter `sampler0anisotropy` - ⊞ -
  * Off `off` -
  * 2x `2x` -
  * 4x `4x` -
  * 8x `8x` -
  * 16x `16x` -

## Parameters - Vectors Page
- Vector `vec` -
- Uniform Name `vec0name` - The uniform name, as declared in the shader.
- Value `vec0value` - ⊞ -
  * Value `vec0valuex` -
  * Value `vec0valuey` -
  * Value `vec0valuez` -
  * Value `vec0valuew` -

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
Extra Information for the Render Pass TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
