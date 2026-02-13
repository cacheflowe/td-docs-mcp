---
url: https://docs.derivative.ca/GLSL_Copy_POP
category: POPs
title: GLSL_Copy_POP
---

# GLSL Copy POP
## Summary

The GLSL Copy POP lets you make copies of the geometry of the first input POP, and apply custom GLSL code to each copy.
If the template input (second input) is not connected, the "number of copies" parameter determines the number of copies.
If the template input is connected, the number of copies is determined by the number of points in the template. A copy is created at each point.
One compute compute shader is run for each element type (points, vertices, primitives) of a copy. Attributes to output are specified in the Output Attributes parameter. A valid points compute shader is required.
For vertices, a custom compute shader is optional, the default compute shader updates the index buffer and copies the input vertex attributes to the output.
For primitives, a custom compute shader is optional, the default compute shader updates extra buffers required for line strips, primitive groups, and copies the input primitive attributes to the output.
See default commented shader DATs for available helper functions and example usage.
**Refer to the[Write GLSL POPs](https://docs.derivative.ca/Write_GLSL_POPs "Write GLSL POPs") article for more info on using this POP.**
[glslcopyPOP_Class](https://docs.derivative.ca/GlslcopyPOP_Class "GlslcopyPOP Class")

## Parameters - GLSL Page
- Number of Copies `ncy` - Sets the number of copies.
- Points Compute Shader `ptcomputedat` - DAT containing the point compute shader code.
- Point Output Attributes `ptoutputattrs` - ⊞ - Input point attributes modified by the shader.
  * * `*` -

- Verts Compute Method `vertcomputemethod` - ⊞ - Vertex compute shader method.
  * Default `default` -
  * Custom Shader `custom` -

- Verts Compute Shader `vertcomputedat` - DAT containing the vertex compute shader.
- Vert Output Attributes `vertoutputattrs` - ⊞ - Input vertex attributes modified by the shader.
  * * `*` -

- Prim Compute Method `primcomputemethod` - ⊞ - Primitive compute shader method.
  * Default `default` -
  * Custom Shader `custom` -

- Prim Compute Shader `primcomputedat` - DAT containing the primitive compute shader.
- Prim Output Attributes `primoutputattrs` - ⊞ - Input primitive attributes modified by the shader.
  * * `*` -

- Append Dimension `dimension` - ⊞ - Always add a dimension, or only add a dimesion when its size is 2 or more.
  * When Template Points / Copies > 1 `morethanone` -
  * Always `always` -

- TDSimplexNoise() `simplexnoise` - ⊞ - Sets the implementation to use for a simplex noise method that can be called in the shader.
  * Performance `performance` -
  * Quality `quality` -

## Parameters - Create Attributes Page
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- New Attribute Class `attr0class` - ⊞ - The attribute class for the new attribute.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- New Attribute Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * New Attribute Name `attr0name` -
  * Custom Name `attr0customname` - The name of the new cutom attribute.

- New Attribute Type `attr0type` - ⊞ - Determines the type.
  * New Attribute Type `attr0type` -
  * New Attribute Number of Components `attr0numcomps` - Number of components of the new attribute.

- Array `attr0isarray` - Attribute is an array, for example 5 float3 values is an array of size 5.
- Array Size `attr0arraysize` - Array Size of the new attribute.
- Matrix Attribute `matattr` - Start of Sequential Parameter Blocks to create new matrix attributes.
- Matrix Attribute Class `matattr0class` - ⊞ - Determines the attribute class where the matrix attribute can be created.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

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

## Parameters - POP Buffers Page
- Buffer `buffer` - Start of Sequential Parameter Blocks for POP attribute buffers.
- POP `buffer0pop` - POP to select the attribute from.
- Attribute Class `buffer0attrclass` - ⊞ - Attribute class for the attribute for the current buffer block.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Attribute `buffer0attr` - Name of attribute for current buffer block.
- Name `buffer0name` - Name to be used in the shader for the POP attribute buffer.

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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the GLSL Copy POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
