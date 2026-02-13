---
url: https://docs.derivative.ca/Math_Mix_POP
category: POPs
title: Math_Mix_POP
---

# Math Mix POP
## Summary

The Math Mix POP can do a series of math operations in one node. It is a simpler version of the [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP"). Each sequential block on Math Mix's Combine page is an operation that can combine one, two or three attributes. There are over 70 different operations to choose from, such as A + B, sin(A), or mix(A, B, C). Scope A, Scope B and Scope C are parameters containing attribute names of the incoming POPs.
**Handling Inputs** : It allows multiple inputs, but unlike Math Combine, all inputs' attributes are auto-named. The first input's attributes have their names unchanged, but the second input's attributes are prefixed with `in1_`, such as `in1_Tex`. Attribute names are prefixed with `in2_` etc for the other inputs. These attribute names appear in the menus to the right of each Scope A B and C on the Combine page.
On the Inputs page, Math Mix lets you choose whether you are operating on point, vertex or primitive attributes.
Inputs that are a single-point are treated as constant values and can be combined with multi-point POPs.
Otherwise, when the input's sizes (number of points) don’t match, it gives you a choice of erroring, warning or ignoring the mis-match, and a choice of how to make them align.
**Combine** page (same for both Math Combine and Math Mix):
Each sequential block is like a mini-equation that lets you operate on one, two or three attributes, and put the result in the same or another attribute.
  * **Operation** - There are over 70 possible operations.
  * Scope A - an attribute, or components of attributes like `P(1) P(2)`, or its equivalent `P.yz`
  * Scope B - an attribute (if applicable)
  * Scope C - an attribute (if applicable)
  * Result Scope (an existing attribute name, components, or a new attribute name)

For A, B and C you can also put constant numbers, or constant vectors like `.3 .4 .5`.
Also on the **Uniforms** page you can specify temporary attributes that have constant values that also can be used on the Combine page.
Scope A, B or C can contain an attribute name, or individual "**components** " of a "vector attribute". A vector attribute is a 2- 3- or 4-value attribute. (e.g. The second component of a float3 vector `.3 .4 .5` is `.4`.)
Since we can put in the Scope A, B or C things like `P(0) P(2) N(0)`, you can actually mix and **reorder components** and put the results in any (other) component combination of one attribute.
Attribute menu - From the Scope A, B and C's menu on their right you can choose from the incoming attributes, the new attributes you created in Math Mix, and also via the **>** at the bottom of the menu the set of very useful **built-in attributes** (they all start with a `_`. Built-in attributes include the point index, normalized indexes, the time slice step time, Pi (3.14157), [Dimensions](https://docs.derivative.ca/Dimension "Dimension"), number of points, etc.
The Result Scope parameter directs the results of an operation to an attribute. You specify the name of the attribute you want to create or over-write, and it will do its best to figure out its properties - type and size. It visually shows in italics what attribute that a block would be writing to, without you explicitly specifying.
It handles combining floats with floats, floats with vectors, and vectors with vectors.
You can specify groups of points/vertices to operate on, others being untouched or left at default values.
**Output** page - lets you keep or delete temporary attributes:
  *     * Delete Attributes - which ones to delete from the output
    * Delete New Attributes toggle

Note that on the **Common** page you can select to output only the attributes that were affected in the POP, useful for cases where you want to output one attribute per POP.
**Pseudocode** - Note the pop-up info (middle-click on the node) contains pseudocode of the operations in this POP, for easier understanding of what the POP is doing.
**Angles** are in degrees, but the Angle Units menu parameter lets you express angles in radians, cycles or degrees.
It uses the primitives and vertices of the first input and other inputs' primitives and vertices are ignored.
Optimized - Note that any attribute you select on the Inputs page does not copy the attribute data - it remains as a reference to the attribute arrays of the incoming POPs.
Attaching an Info DAT will show you raw GLSL code that is generated.
See also [Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP"), [Math POP](https://docs.derivative.ca/Math_POP "Math POP"), [ReRange POP](https://docs.derivative.ca/ReRange_POP "ReRange POP"), [Quantize POP](https://docs.derivative.ca/Quantize_POP "Quantize POP"), [Limit POP](https://docs.derivative.ca/Limit_POP "Limit POP")
See also [Experimental:Math Mix Combine Functions](https://docs.derivative.ca/index.php?title=Experimental:Math_Mix_Combine_Functions&action=edit&redlink=1 "Experimental:Math Mix Combine Functions \(page does not exist\)")
[mathmixPOP_Class](https://docs.derivative.ca/MathmixPOP_Class "MathmixPOP Class")

## Parameters - Inputs Page
- Length Mismatch `lengthmismatchnotif` - ⊞ - Length mis-match motification action.
  * Length Mismatch `lengthmismatchnotif` -
  * Length Mismatch Action `lengthmismatchaction` - Specify which attribute values to use when sampling outside of the input range.

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Angle Units `angleunit` - ⊞ - Any angles in parameters are expressed in degrees (0-360 is one rotation), radians (0-2*pi) or cycles (0-1 is one rotation).
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -

- Input `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POP `input0pop` - Input POP for the current input.
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

## Parameters - Uniforms Page
- Vector `vec` - Start of Sequential Parameter Blocks to define uniform variables.
- Name `vec0name` - The name of the uniform.
- Type `vec0type` - ⊞ - The number of components for the array.
  * float `float` -
  * float2 `float2` -
  * float3 `float3` -
  * float4 `float4` -
  * double `double` -
  * double2 `double2` -
  * double3 `double3` -
  * double4 `double4` -
  * int `int` -
  * int2 `int2` -
  * int3 `int3` -
  * int4 `int4` -
  * uint `uint` -
  * uint2 `uint2` -
  * uint3 `uint3` -
  * uint4 `uint4` -

- Value `vec0value` - ⊞ - Vector value.
  * Value `vec0value0` -
  * Value `vec0value1` -
  * Value `vec0value2` -
  * Value `vec0value3` -

- Pre-Multiply RGB by Alpha `premultcolor` - Enable RGB values pre-multiplication with the Alpha.
- Color `color` - Start of Sequential Parameter Blocks for color uniforms.
- Name `color0name` - The name of the color uniform.
- RGB `color0rgb` - ⊞ - RGB Color.
  * RGB `color0rgbr` -
  * RGB `color0rgbg` -
  * RGB `color0rgbb` -

- Alpha `color0alpha` - Alpha value.

## Parameters - Combine Page
- Combine `comb` - Start of Sequential Parameter Blocks for combines.
- Operation `comb0oper` - ⊞ - Selects the combine operation to perform.
  * None `none` -
  * A `copya` -
  * abs(A) `abs` -
  * sign(A) `sign` -
  * sqrt(A) `sqrt` -
  * A * A `square` -
  * 1 / A `inverse` -
  * floor(A) `floor` -
  * round(A) `round` -
  * ceil(A) `ceil` -
  * int(A) `int` -
  * fract(A) `fract` -
  * normalize(A) `normalize` -
  * exp10(A) `exp10` -
  * exp2(A) `exp2` -
  * exp(A) `exp` -
  * log10(A) `log10` -
  * log2(A) `log2` -
  * ln(A) `ln` -
  * sin(A) `sin` -
  * cos(A) `cos` -
  * tan(A) `tan` -
  * asin(A) `asin` -
  * acos(A) `acos` -
  * atan(A) `atan` -
  * degrees(A) `degrees` -
  * radians(A) `radians` -
  * length(A) `length` -
  * compadd(A) `compadd` -
  * compsub(A) `compsub` -
  * compmult(A) `compmult` -
  * compdiv(A) `compdiv` -
  * compavg(A) `compavg` -
  * compmin(A) `compmin` -
  * compmax(A) `compmax` -
  * A + B `add` -
  * A - B `asubb` -
  * B - A `bsuba` -
  * A * B `mult` -
  * A / B `adivb` -
  * B / A `bdiva` -
  * A ** B `apowerb` -
  * logB(A) `logba` -
  * avg(A, B) `avg` -
  * min(A, B) `min` -
  * max(A, B) `max` -
  * mod(A, B) `mod` -
  * int(A / B) `intadivb` -
  * A > B `gt` -
  * A >= B `gte` -
  * A < B `lt` -
  * A <= B `lte` -
  * A == B `eq` -
  * A != B `ne` -
  * atan2(A, B) `atan2` -
  * dot(A, B) `dot` -
  * angle(A, B) `angle` -
  * cross(A, B) `cross` -
  * reflect(A, B) `reflect` -
  * A + B * C `aaddbmultc` -
  * A * B + C `amultbaddc` -
  * A + B + C `aaddbaddc` -
  * A * B * C `amultbmultc` -
  * rangefrom(A, B, C) `rangefrom` -
  * rangeto(A, B, C) `rangeto` -
  * mix(A, B, C) `mix` -
  * A if C else B `ifelse` -
  * loop(A, B, C) `loop` -
  * zigzag(A, B, C) `zigzag` -
  * clamp(A, B, C) `clamp` -
  * smoothstep(A, B, C) `smoothstep` -
  * B <= A < C `bltealtc` -
  * B < A <= C `bltaltec` -
  * B < A < C `bltaltec` -
  * B <= A <= C `bltaltec` -
  * refract(A, B, C) `refract` -
  * dbtopow(A) `dbtopow` -
  * powtodb(A) `powtodb` -
  * dbtoamp(A) `dbtoamp` -
  * amptodb(A) `amptodb` -
  * RGBtoHSV(A) `rgbtohsv` -
  * HSVtoRGB(A) `hsvtorgb` -

- Scope A `comb0scopea` - Attribute scope for operand A.
- Scope B `comb0scopeb` - Attribute scope for operand B.
- Scope C `comb0scopec` - Attribute scope for operand C.
- Result Scope `comb0result` - ⊞ - Operation result output attribute scope.
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * N `N` -
  * Tex `Tex` -

## Parameters - Output Page
- Delete Attributes `delattrs` - Attributes to delete from output.
- Delete New Attributes `delnewattrs` - Enable removal of attributes created by the operator
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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Math Mix POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
