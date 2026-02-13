---
url: https://docs.derivative.ca/GLSL_POP
category: POPs
title: GLSL_POP
---

# GLSL POP
## Summary

This POP allows you to modify input attributes with GLSL. It works on a single attribute class at a time, Points, Verts or Primitives, and doesn't allow to change the number of input elements (Points, Verts or Primitives).
**Refer to the[Write GLSL POPs](https://docs.derivative.ca/Write_GLSL_POPs "Write GLSL POPs") article for more info on using this POP.**
See also [GLSL Advanced POP](https://docs.derivative.ca/GLSL_Advanced_POP "GLSL Advanced POP")
[glslPOP_Class](https://docs.derivative.ca/GlslPOP_Class "GlslPOP Class")

## Parameters - GLSL Page
- Compute Shader `computedat` - Points to the DAT holding the Compute Shader. Drag & Drop a DAT here, or manually enter the path to the DAT.
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Number of Threads `numthreadsmode` - ⊞ - Selects how to set the number of threads for the custom compute shader dispatch.
  * Auto `auto` -
  * Number of Elements in Other Input `otherinputelements` -
  * Manual Number of Elements `numelems` - Sets the number of elements when the number of threads is set to Manual Number of Elements.
  * Number of Elements from Attribute `numelemsattrib` -
  * Manual `manual` -

- Threads Input `threadsinput` - Determines the input index that contains the number of elements.
- Number of Elements `numelems` -
- POP `numelemspop` - POP reference when setting the number of elements from an attribute.
- Num Elements Attrib `numelemsclass` - ⊞ - Sets the attribute class where the number of elements can be found.
  * Num Elements Attrib `numelemsclass` -
  * Num Elements Attrib `numelemsattr` - The attribute to use for the number of elements. The first value is used.

- Work Group Size `workgroupsize` - ⊞ - Specifies the workgroup size when manually setting the number of threads.
  * Work Group Size `workgroupsizex` -
  * Work Group Size `workgroupsizey` -
  * Work Group Size `workgroupsizez` -

- Dispatch Size `dispatchsize` - ⊞ - Determines the number of thread groups to launch in each dimension.
  * Dispatch Size `dispatchsizex` -
  * Dispatch Size `dispatchsizey` -
  * Dispatch Size `dispatchsizez` -

- Output Attributes `outputattrs` - ⊞ - The list of input attributes that will be allocated and can be written to.
  * * `*` -

- Output Access `outputaccess` - ⊞ - Controls whether the attribute buffers can only be read from or read from and written to.
  * Write Only `writeonly` -
  * Read-Write `readwrite` -

- Initialize Output Attributes `initoutputattrs` - Copy input attributes values for existing attributes, set the attributes values to their defaults for new attributes. It's a separate compute shader dispatch happening before the POP custom compute shader dispatch.
- Copy Previous Pass Output to Input `prevpassoutput` - Enable copying the previous pass outputs to the next pass inputs.
- Passes `npasses` - Number of shader passes.
- Input `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POPs `input0pops` - Allows to specify additional input POPs besides connected POPs.
- TDSimplexNoise() `simplexnoise` - ⊞ - Sets the implementation to use for a simplex noise method that can be called in the shader.
  * Performance `performance` -
  * Quality `quality` -

## Parameters - Create Attributes Page
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- New Attribute Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * New Attribute Name `attr0name` -
  * Custom Name `attr0customname` - The name of the new cutom attribute.

- New Attribute Type `attr0type` - ⊞ - Determines the type.
  * New Attribute Type `attr0type` -
  * New Attribute Number of Components `attr0numcomps` - Number of components of the new attribute.

- Array `attr0isarray` - Attribute is an array, for example 5 float3 values is an array of size 5.
- Array Size `attr0arraysize` - Array Size of the new attribute.
- Value `attr0value` - ⊞ - Attribute value.
  * Value `attr0value0` - Attribute value(s).
  * Value `attr0value1` - Attribute value(s).
  * Value `attr0value2` - Attribute value(s).
  * Value `attr0value3` - Attribute value(s).

- Matrix Attribute `matattr` - Start of Sequential Parameter Blocks to create new matrix attributes.
- Custom Matrix Name `matattr0name` - Determines the new matrix attribute name.
- Rows `matattr0numrows` - Number of rows in the matrix - 2, 3 or 4.
- Columns `matattr0numcols` - Number of columns in the matrix - 2, 3 or 4.
- Array `matattr0isarray` - Attribute is an array, for example 5 float3 values is an array of size 5.
- Array Size `matattr0arraysize` - Nunber of elements in the array of matrices.
- Qualifier `matattr0qualifier` - ⊞ - Additional detail on how the attribute should be interpreted.
  * None `none` -
  * Transform Matrix `transformMatrix` -

## Parameters - Colors Page
- Pre-Multiply RGB by Alpha `premultcolor` - Enable RGB values pre-multiplication with the Alpha.
- Color `color` - Start of Sequential Parameter Blocks for color uniforms.
- Name `color0name` - The name of the color uniform.
- RGB `color0rgb` - ⊞ - RGB Color.
  * RGB `color0rgbr` -
  * RGB `color0rgbg` -
  * RGB `color0rgbb` -

- Alpha `color0alpha` - Alpha value.

## Parameters - Vectors Page
- Vector `vec` - Start of Sequential Parameter Blocks to define uniform variables.
- Name `vec0name` - The name of the vector uniform.
- Type `vec0type` - ⊞ - The number of components for the array.
  * float `float` -
  * vec2 `vec2` -
  * vec3 `vec3` -
  * vec4 `vec4` -
  * double `double` -
  * dvec2 `dvec2` -
  * dvec3 `dvec3` -
  * dvec4 `dvec4` -
  * int `int` -
  * ivec2 `ivec2` -
  * ivec3 `ivec3` -
  * ivec4 `ivec4` -
  * uint `uint` -
  * uvec2 `uvec2` -
  * uvec3 `uvec3` -
  * uvec4 `uvec4` -

- Value `vec0value` - ⊞ - Vector value.
  * Value `vec0valuex` -
  * Value `vec0valuey` -
  * Value `vec0valuez` -
  * Value `vec0valuew` -

## Parameters - Samplers Page
- Sampler `sampler` - Start of Sequential Parameter Blocks for Samplers to read from the shader.
- Name `sampler0name` - The name of the sampler uniform.
- TOP `sampler0top` - ⊞ - Sets reference to a TOP to sample.
- Extend U `sampler0extendu` - ⊞ - Controls what is returned from the texture sampling functions when the U texture coordinates are outside [0-1] range.
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Extend V `sampler0extendv` - ⊞ - Controls what is returned from the texture sampling functions when the V texture coordinates are outside [0-1] range.
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Extend W `sampler0extendw` - ⊞ - Controls what is returned from the texture sampling functions when the W texture coordinates are outside [0-1] range.
  * Hold `hold` -
  * Zero `zero` -
  * Repeat `repeat` -
  * Mirror `mirror` -

- Filter `sampler0filter` - ⊞ - Controls the pixel filtering on the input image of the TOP.
  * Nearest Pixel `nearest` -
  * Interpolate Pixels `linear` -

## Parameters - Arrays Page
- Array `array` - Start of Sequential Parameter Blocks for array uniforms.
- Name `array0name` - The name of the array uniform.
- Type `array0type` - ⊞ - The number of components for the array.
  * float `float` -
  * vec2 `vec2` -
  * vec3 `vec3` -
  * vec4 `vec4` -

- CHOP `array0chop` - The CHOP for the current uniform.
- Array Type `array0arraytype` - ⊞ - The type of uniform array, array or sampler.
  * Uniform Array `uniformarray` -
  * Texture Buffer `texturebuffer` -

## Parameters - Matrices Page
- Matrix `matrix` - Start of Sequential Parameter Blocks of matrix uniforms.
- Name `matrix0name` - The name of the matrix uniform.
- Matrix `matrix0value` - Sets a reference to a matrix to pass to the shader.

## Parameters - Temp Buffers Page
- Temp Buffer `tempbuffer` - Start of Sequential Parameter Blocks forTemporary buffers used to pass information to the shader as uniforms.
- Name `tempbuffer0name` - The name of the temporary buffer.
- Initial Value `tempbuffer0initval` - Initial value for the current temporary buffer.

## Parameters - Constants Page
- Constant `const` - Start of Sequential Parameter Blocks for Specialization Constants.
- Name `const0name` - The name of the constant.
- Value `const0value` - Constant value.

## Parameters - Collisions Page
- Name `asname` - The name for the acceleration structure uniform.
- Collision POP `colpop` - The POP to use to create an acceleration structure for use with hardware raytracing in the shader.
- Build Flag `buildflag` - ⊞ - When using the ray query features with a collision POP, specify whether to try to optimize for build time or trace time.
  * Fast Build (Dynamic Geometry) `fastbuild` -
  * Fast Trace (Static Geometry) `fasttrace` -

- Opaque Collision Geometry `opaquecolgeo` - When using an acceleration structure, specify whether the collision geometry is treated as opaque (only the closest hit is returned) or not.

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

## Info CHOP Channels
Extra Information for the GLSL POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
