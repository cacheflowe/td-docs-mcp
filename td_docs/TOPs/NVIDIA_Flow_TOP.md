---
url: https://docs.derivative.ca/NVIDIA_Flow_TOP
category: TOPs
title: NVIDIA_Flow_TOP
---

# NVIDIA Flow TOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.
**Hardware:** This operator only works with **Nvidia GPUs**.
NVIDIA Flow is a volumetric fluid based simulation of a burning gas system. The user controls the 3 main factors of temperature, fuel, and smoke to create fire and smoke simulations.
The Nvidia Flow TOP calculates the Flow simulation and renders it. It requires a [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP") to emit gas into the Flow simulation.
See also [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP"), [Nvidia Flow](https://docs.derivative.ca/Nvidia_Flow "Nvidia Flow").
Read more here [Nvidia Flow Artist Tools](https://docs.nvidia.com/gameworks/content/artisttools/Flow/index.html)
[flowTOP_Class](https://docs.derivative.ca/FlowTOP_Class "FlowTOP Class")

## Parameters - Setup Page
- Initialize `initialize` - Initializes the simulation.
- Start `start` - Starts the simulation playback.
- Play `play` - The simulation only steps forward when Play = On, when off the simulation is paused.
- Camera `camera` - Specify the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") to view the simulation from. Note: Must be camera with Projection = Perspective.
- Flow Emitters `emitters` - Specify the [Nvidia Flow Emitter COMPs](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP") to include in the simulation.
- Sim Position `simposition` - ⊞ - The position of the simulation volume's center, in the world. The simulation cannot extend outside of the volume.
  * X `simpositionx` -
  * Y `simpositiony` -
  * Z `simpositionz` -

- Sim Size `simsize` - ⊞ - The size of the simulation volume in the world. The simulation cannot extend outside of the volume. Also controls the size of simulation blocks, so the total number of blocks in the volume stays the same. Smaller size blocks will require more blocks for the same size simulation. This increases accuracy but makes the simulation more taxing on the GPU as there are more blocks to calculate.
  * X `simsizex` -
  * Y `simsizey` -
  * Z `simsizez` -

- Mem Usage `memusage` - Controls relative memory usage, the fraction of the total simulation blocks that will be allocated. Most simulations will not fill the simulation volume uniformly, so only a small value is needed. High values will cause extremely high memory usage.
- Show Blocks `showblocks` - Displays the simulation blocks being used. Useful for debugging or optimizing your Flow simulation. Also shows the edges of the simulation volume.
- Show Emit Bounds `showemitbounds` - Displays the bounds of the emitters.
- Show Shapes `showshapes` - Displays the shapes of the emitters.
- Speed `speed` - Controls the update rate of the simulation.
- Max Simulation Steps `maxsteps` - Maximum number of simulation steps per update. A higher number of steps will increase quality for fast moving object at the cost of performance.
- Render Mode `rendermode` - Provides two debug render modes in addition to the default of Density. Debug Density gives a "rainbow" render, where density is mapped to a colour, and Dubug Velocity converts velocity xyz to an rgb colour.

## Parameters - Settings Page
- Gravity `gravity` - ⊞ - Gravity direction for use with Buoyancy parameter, where amount controls strength of buoyancy force.
  * X `gravityx` -
  * Y `gravityy` -
  * Z `gravityz` -

- Velocity Damping `veldamping` - Higher values reduce velocity faster. Uses exponential decay curve.
- Velocity Fade `velfade` - Compared to damping, fade reduces low velocity values faster. Fade velocity rate is in units per second.
- Vel MacCormack Blend `velmaccormackblend` - Higher values make a sharper appearance, but with more artifacts.
- Smoke Damping `smokedamping` - Higher values reduce smoke faster. Uses exponential decay curve.
- Smoke Fade `smokefade` - Compared to damping, fade reduces low smoke values faster. Fade velocity rate is in units per second.
- Smoke MacCormack Blend `smokemaccormackblend` - Higher values make a sharper appearance, but with more artifacts.
- Temp Damping `tempdamping` - Higher values reduce temperature faster. Uses exponential decay curve.
- Temp Fade `tempfade` - Compared to damping, fade reduces low temperature values faster. Fade velocity rate is in units per second.
- Fuel Damping `fueldamping` - Higher values reduce fuel faster. Uses exponential decay curve.
- Fuel Fade `fuelfade` - Compared to damping, fade reduces low fuel values faster. Fade velocity rate is in units per second.
- Vorticity Strength `vortstrength` - Controls amount of rotation turbulence as a multiplier, a value of 0 will result in no vorticity. High values increase turbulent flow while low values increase laminar flow.
- Vorticity from Velocity `vortfromvel` - Amount of vorticity added from velocity.
- Vorticity from Smoke `vortfromsmoke` - Amount of vorticity added from smoke.
- Vorticity from Temp `vortfromtemp` - Amount of vorticity added from temperature.
- Vorticity from Fuel `vortfromfuel` - Amount of vorticity added from fuel.
- Vorticity Constant `vortconstant` - The baseline vorticity in the simulation.
- Ignition Temp `ignitiontemp` - Specify the minimum temperature required for combustion.
- Burn per Temp `burnpertemp` - Control how much fuel is burned for a given temperature level. Lower Burn per Temp may result in some fuel not burning completely at a certain temperature.
- Smoke per Burn `smokeperburn` - Controls amount of smoke generated for each unit of combustion (per burn).
- Temp per Burn `tempperburn` - Controls amount of temperature generated for each unit of combustion (per burn).
- Fuel per Burn `fuelperburn` - Controls amount of fuel used for each unit of combustion (per burn).
- Buoyancy `buoyancy` - Works in conjunction with the parameter Gravity above which sets a vector for use by Buoyancy. Higher values result in greater effect by the Gravity parameter.
- Cooling Rate `coolingrate` - The rate of cooling in the system, exponential.
- Expansion `expansion` - Controls the amount the system's gaseous volume expands.
- Velocity Alloc Weight `velallocweight` - If zero, block allocation and deallocation depend on an internal threshold and weighting of Velocity. If non-zero, block allocation and deallocation will be affected by the value of Velocity Alloc Threshold.
- Velocity Alloc Threshold `velallocthreshold` - If Velocity Alloc Weight is non-zero, block allocation and deallocation is based on this value. In particular, if the velocity magnitude is below this threshold, the block will be deallocated, unless smoke and fuel thresholding (see below) are active.
- Smoke Alloc Weight `smokeallocweight` - If zero, block allocation and deallocation depend on an internal threshold and weighting of Smoke density. If non-zero, smoke density affects block allocation and deallocation based on the value of Smoke Alloc Threshold.
- Smoke Alloc Threshold `smokeallocthreshold` - If Smoke Alloc Weight is non-zero, block allocation and deallocation is based on this value. In particular, if the Smoke density is below this threshold, the block will be deallocated, unless velocity and fuel thresholding are active.
- Fuel Alloc Weight `fuelallocweight` - If zero, block allocation and deallocation depend on an internal threshold and weighting of fuel density. If non-zero, fuel density affects block allocation and deallocation based on the value of Fuel Alloc Threshold.
- Fuel Alloc Threshold `fuelallocthreshold` - If Fuel Alloc Weight is non-zero, block allocation and deallocation is based on this value. In particular, if the Smoke density is below this threshold, the block will be deallocated, unless velocity and smoke thresholding are active.

## Parameters - Volume Shadow Page
- Enable `enableshadow` - Enables Volume shadow rendering for the simulation. Shadowing generates light intensity values that overwrite the "burn" channel of the grid. Values range from 0 to 1, where 0 is fully shadowed. Shadow visibilty can be controlled by enabling 'Override Emitter Intensity Mask' or by adjusting the 'Burn Intensity Mask', 'Burn Alpha Mask', and 'Burn Color Mask' in [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP")
- Draw Debug `drawshadowdebug` - Displays the volume shadow blocks being used. Useful for debugging or optimizing.
- Override Emitter Intensity Mask `overrideemitter` - Automatically adjusts the emitters' render material, so volume shadows are visible. Will override 'Burn Intensity Mask' and 'Intensity Bias' of emitters.
- Light `light` - The light source used to generate volume shadow. The light should be a shadow caster. Only the position and orientation of the light are used, color and intensity are ignored.
- Shadow Resolution `shadowresolution` - The resolution of the shadow map volume texture. The texture is allocated as a cube, so there will be space for shadowresolution^3 blocks.
- Min Memory Usage `shadowminusage` - The initial fraction of volume shadow blocks to allocate memory for.
- Max Memory Usage `shadowmaxusage` - The maximum fraction of volume shadow blocks to allocate memory for.
- Intensity Scale `shadowintensityscale` - Scales how dark the shadow will be.
- Min Intensity `shadowminintensity` - A lower limit for shadow intensity.
- Burn Blend Mask `shadowburnmask` - Allows the burn value in the simulation to control the blend strength of the shadow. Postive values mean burn increases the blend strength, negative values mean burn decreases the blend strength
- Smoke Blend Mask `shadowsmokemask` - Allows the smoke value in the simulation to control the blend strength of the shadow. Postive values mean smoke increases the blend strength, negative values mean smoke decreases the blend strength
- Temp Blend Mask `shadowtempmask` - Allows the temperature value in the simulation to control the blend strength of the shadow. Postive values mean temp increases the blend strength, negative values mean temp decreases the blend strength
- Fuel Blend Mask `shadowfuelmask` - Allows the fuel value in the simulation to control the blend strength of the shadow. Postive values mean fuel increases the blend strength, negative values mean fuel decreases the blend strength
- Blend Bias `shadowblendbias` - An offset that increases or decreases the blend strength by a constant amount. Parts of the grid with a blend value over 1 will have shadows. Parts of the grid with blend value under 1 will not have shadows. Blend values between 0 and 1 scale the strength of shadow.

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
  * Input 0: Background Image - Texture the Flow simulation will be overlayed onto.
  * Input 1: Depth Map - A [Depth TOP](https://docs.derivative.ca/Depth_TOP "Depth TOP") to obscure parts of the Flow Simulation.

## Info CHOP Channels
Extra Information for the Nvidia Flow TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Nvidia Flow TOP Info Channels
  * initializing -

  * ready -

  * running -

  * done -

  * timer_seconds -

  * playing_seconds -

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
