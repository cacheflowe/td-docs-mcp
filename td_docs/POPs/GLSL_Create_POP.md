---
url: https://docs.derivative.ca/GLSL_Create_POP
category: POPs
title: GLSL_Create_POP
---

# GLSL Create POP
## Summary

This POP is deprecated and will be removed. Use GLSL Advanced POP with or without Topology POP to create primitives with GLSL instead.
[glslcreatePOP_Class](https://docs.derivative.ca/GlslcreatePOP_Class "GlslcreatePOP Class")

## Parameters - GLSL Page
- Compute Shader `computedat` -
- Primitive Type `primtype` - ⊞ -
  * Triangles `triangle` -
  * Quads `quads` -
  * Lines `lines` -
  * Points `points` -

- Max Number of Primitives `maxprims` -
- Indirect `indirect` -
- Number of Threads `numthreadsmode` - ⊞ -
  * Auto `auto` -
  * Manual `manual` -

- Work Group Size `workgroupsize` - ⊞ -
  * Work Group Size `workgroupsizex` -
  * Work Group Size `workgroupsizey` -
  * Work Group Size `workgroupsizez` -

- Dispatch Size `dispatchsize` - ⊞ -
  * Dispatch Size `dispatchsizex` -
  * Dispatch Size `dispatchsizey` -
  * Dispatch Size `dispatchsizez` -

- POPs `pops` -

## Parameters - Vectors Page
- Vector `vec` -
- Name `vec0name` -
- Type `vec0type` - ⊞ -
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

- Value `vec0value` - ⊞ -
  * Value `vec0valuex` -
  * Value `vec0valuey` -
  * Value `vec0valuez` -
  * Value `vec0valuew` -

## Parameters - Samplers Page
- Sampler `sampler` -
- Name `sampler0name` -
- TOP `sampler0top` - ⊞ -
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
  * Nearest Pixel `nearest` -
  * Interpolate Pixels `linear` -

## Parameters - Arrays Page
- Array `array` -
- Name `array0name` -
- Type `array0type` - ⊞ -
  * float `float` -
  * vec2 `vec2` -
  * vec3 `vec3` -
  * vec4 `vec4` -

- CHOP `array0chop` -

## Parameters - Matrices Page
- Matrix `matrix` -
- Name `matrix0name` -
- Matrix `matrix0value` -

## Parameters - Atomic Counters Page
- Atomic Counter `ac` -
- Name `ac0name` -
- Initial Value `ac0singlevalue` -

## Parameters - Constants Page
- Constant `const` -
- Name `const0name` -
- Value `const0value` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the GLSL Create POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
