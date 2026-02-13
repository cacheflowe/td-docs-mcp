---
url: https://docs.derivative.ca/TOP_to_POP
category: POPs
title: TOP_to_POP
---

# TOP to POP
## Summary

Position and Active is a shortcut for P in RGB, and alpha is set to 1 for active pixels (pixels with a valid attribute value).
The First RGBA Contains menu lets you treat the RGBA in different ways, including as depth maps, point clouds, height maps.
Using Custom you specify which attribute and components you expect in the RGBA of the TOP, so max 4 could be `P(0) Color(2) N(1) P(2)`.
When you Use Dimension all pixels are active since the resolution matches the TOP When using the other modes you can end up with unused pixels (you have 40 points, fit to square gives you 7x7, so you end up with 9 unused pixels), alpha is only set to 1 for used pixels.
[toptoPOP_Class](https://docs.derivative.ca/ToptoPOP_Class "ToptoPOP Class")

## Parameters - Inputs Page
- First RGBA Contains `rgba` - ⊞ - Determines how the TOP's pixels should be interpreted.
  * Color (RGBA) `color` -
  * Position and Active (RGBA) `pactive` -
  * Position (RGB) `pos` -
  * Depth `depth` -
  * Height (R) `height` -
  * Custom `custom` -

- Max Number of Points `maxpointsenable` - ⊞ - Enable the setting of the max number of points when First RGBA Contains is set to Position.
  * Max Number of Points `maxpointsenable` -
  * Number of Points `maxpoints` - Sets the max number of points when the automatic max number of points is overriden.

- TOP `input` - Start of Sequential Parameter Blocks for TOPs to convert.
- TOP `input0top` - Sets reference to a TOP to convert.
- Channel Scope `input0chanscope` - ⊞ - Color channels to sample.
  * r `r` -
  * g `g` -
  * b `b` -
  * a `a` -

- Attribute Scope `input0attrscope` - ⊞ - A list of attributes to be created according to the channel scope.
  * P `P` -
  * P.i01 `P.i01` -

- Filter `input0filter` - ⊞ - The TOP pixel filtering.
  * Nearest Pixel `nearest` -
  * Interpolate Pixels `linear` -
  * High Quality Resize `highquality` -

- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- New Attribute Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * New Attribute Name `attr0name` -
  * Custom Name `attr0customname` - The name of the new cutom attribute.

- Attribute Type `attr0type` - ⊞ - Determines the type.
  * Attribute Type `attr0type` -
  * Components `attr0numcomps` - The number of components in the new custom attribute.

- Default Value `attr0defaultval` - ⊞ - The value of the new custom attribute if it cannot be computed.
  * Default Value `attr0defaultval0` -
  * Default Value `attr0defaultval1` -
  * Default Value `attr0defaultval2` -
  * Default Value `attr0defaultval3` -

## Parameters - Detail Page
- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Lines `lines` -
  * Line Strips `linestrips` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals `quads` -

- Line X/Y/Z `line` - ⊞ - Specifies whether to enable Lines in the X/Y/Z axis.
  * Line X/Y/Z `linex` -
  * Line X/Y/Z `liney` -
  * Line X/Y/Z `linez` -

- Plane XY/YZ/ZX `plane` - ⊞ - Plane orientation.
  * Plane XY/YZ/ZX `planex` -
  * Plane XY/YZ/ZX `planey` -
  * Plane XY/YZ/ZX `planez` -

- Unique Points `uniquepoints` - Enable not sharing points between primitives.
- Center `t` - ⊞ - The center of the output geometry.
  * Center `tx` -
  * Center `ty` -
  * Center `tz` -

- Override Size `overridesize` - ⊞ - When on, overrides the automatic size, which is 1 in X with the size in Y respecting the input TOP aspect ratio.
  * Override Size `overridesizex` -
  * Override Size `overridesizey` -
  * Override Size `overridesizez` -

- Size `size` - ⊞ - The geometry 3D size.
  * Size `sizex` -
  * Size `sizey` -
  * Size `sizez` -

- Override Resolution `overrideres` - ⊞ - When on, overrides the automatic resolution, which is the input TOP resolution.
  * Override Resolution `overrideresx` -
  * Override Resolution `overrideresy` -
  * Override Resolution `overrideresz` -

- Resolution `res` - ⊞ - Overriden resolution.
  * Resolution `resx` -
  * Resolution `resy` -
  * Resolution `resz` -

- Pixel Sampling Location `pixelsamplingloc` - ⊞ - Sets where the pixels are sampled.
  * Edge to Edge `edgetoedge` -
  * Pixel Centered `pixelcentered` -

- Texture Coordinates `texture` - ⊞ - Sets the attribute class where the texture coordinates should be created.
  * None `none` -
  * Point `point` -
  * Vertex `vert` -

- Append Dimension `dimension` - ⊞ - Always add a dimension, or only add a dimesion when its size is 2 or more.
  * When Rows Cols Slices > 1 `morethanone` -
  * Always for Rows Cols `rowscolsalways` -
  * Always for Rows Cols Slices `rowscolsslicesalways` -

## Parameters - Depth Page
- Rerange from Low High `rerangefromlow` - ⊞ - Range for input values.
  * Rerange from Low High `rerangefromlow` -
  * Rerange from High `rerangefromhigh` -

- Rerange to Low High `rerangetolow` - ⊞ - Range for output values.
  * Rerange to Low High `rerangetolow` -
  * Rerange to High `rerangetohigh` -

- Camera `camera` - Specify the camera component.
- Override Camera View `overridecamera` - When on, overrides the View settings from the selected camera object.
- View Angle Method `viewanglemethod` - ⊞ - Sets the method to convert the depth TOP.
  * Horizontal FOV `horfov` -
  * Vertical FOV `vertfov` -
  * Focal Lengths `focallengths` - Determines the camera's focal lengths.

- FOV Angle `fov` - Determines the camera's field of view angle.
- Focal Length (Fx, Fy) `focallengths` - ⊞ -
  * Focal Length (Fx, Fy) `focallengthsx` -
  * Focal Length (Fx, Fy) `focallengthsy` -

- Optical Center (Cx, Cy) `center` - ⊞ - The location of the center of the camera for the depth projection.
  * Optical Center (Cx, Cy) `centerx` -
  * Optical Center (Cx, Cy) `centery` -

- Delete Near Points `deletenear` - Enable removal of points that are close to the camera.
- Near Depth `depthnear` - Depth of the near clipping plane.
- Delete Far Points `deletefar` - Enable removal of points that are far from the camera.
- Far Depth `depthfar` - Depth of the far clipping plane.
- Line Strip Behavior `linestripbehavior` - ⊞ - What to do when points of a line strip are deleted.
  * Delete Point of Line Strip `delpointoflinestrip` -
  * Split Line Strip `splitlinestrip` -
  * Delete Line Strip `dellinestrip` -

## Parameters - Height Page
- Displacement Scale `dispscale` - Sets the displacement scale when the pixels are interpreted as heights values

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.
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

## Info CHOP Channels
Extra Information for the TOP to POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
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
