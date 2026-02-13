---
url: https://docs.derivative.ca/Noise_POP
category: POPs
title: Noise_POP
---

# Noise POP
## Summary

The Noise POP affects every point with a noise field, which can be thought of as smooth, randomly-rising and falling values in 3D space.
By default the Noise POP moves every point's `P` attribute a distance in X, Y and Z based on the point's position in the noise space. You can visualize the field by sending a [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP") into a Noise POP. Turn on the toggle parameter Compute Point Normals to see proper shading.
The Type menu lets you choose between Simplex, Perlin in 2-4 dimensions. Simplex has the least grid-like field appearance. The Period determines the approximate distance between two peaks in each dimension (if you set Harmonics to 0).
Harmonics adds more detail by adding to the field another half-period noise field, and recursively for the number of "harmonics". Harmonic Spread is the ratio of period of one applied harmonic to the next. Furthermore the entire noise field can be translated, rotated or scaled via the Transform page.
The noise field value averages 0 in X, Y and Z. The Amplitude and Exponent parameters affect the magnitude of the resulting value, and the Offset is added to the resulting noise values.
**Output attributes** - On the Output page, you can output and name the raw noise values to an attribute named `Noise` by default. Because the Noise Size menu parameter on the Noise page defaults to Scalar, the `Noise` attribute is a single scalar float.
If the Noise Size menu parameter is set to Vector, the `Noise` attribute is a 3-component float, or 4 if the Parameter Size is set to 4.
On the Output page you can also output several math functions that are derived from the noise field, like Gradient and Curl.
The Gradient is the rate-of-change of a scalar noise around each point in X Y and Z (aka the "first order derivative") and is a float3 named `NoiseGradient`
Curl is an expression of how much the slope twists around each point. A 3D Curl is a float3 named `NoiseCurl`. A 2D Curl is float2 named `NoiseCurl2`
If Combine Operation is Add (default) or Multiply, a float3 noise is always applied to `P`, even though the noise may be set to scalar. With Combine Attribute Scope, the noise can be applied to any scalar or vector attribute (one component to 4 components), and output to any new or existing attribute.
With Combine Entity you can instead combine the `NoiseCurl` with any attribute.
With Noise Size set to Vector, changing the Parameters Size to 2, 3 or 4 gives you individual parameter controls of Amplitude, Exponent and Offset per X Y Z W dimension.
To animate the noise, put something like `absTime.seconds` in any of the Translate or Translate 4D parameters on the Transform page.
**Per-point mapping of parameters** - The Noise POP has a Map page, which allows every point to get a different value for Amplitude, Offset, Exponent, Period, Harmonic Spread and Harmonic Gain parameters. In this mechanism, a separate attribute in the input contains values that override (or add to / multiply by) the parameter value. See [Mapping POP Attributes to Parameters](https://docs.derivative.ca/Mapping_POP_Attributes_to_Parameters "Mapping POP Attributes to Parameters").
See also [Random POP](https://docs.derivative.ca/Random_POP "Random POP").
[noisePOP_Class](https://docs.derivative.ca/NoisePOP_Class "NoisePOP Class")

## Parameters - Noise Page
- Noise Lookup Attribute `noiselookupattrib` - Point input attribute to use when computing the noise.
- Type `type` - ⊞ - Determines the noise type.
  * Perlin 2D (GPU) `perlin2d` -
  * Perlin 3D (GPU) `perlin3d` -
  * Perlin 4D (GPU) `perlin4d` -
  * Simplex 2D (GPU) `simplex2d` -
  * Simplex 3D (GPU) `simplex3d` -
  * Simplex 4D (GPU) `simplex4d` -

- Noise Size `noisesize` - ⊞ - Number of noise components to compute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Seed `seed` - Numerical value that initializes the randomization.
- Period `period` - Period (scale) of the noise field.
- Harmonics `harmon` - The number of higher frequency components to layer on top of the base frequency. 0 harmonics give the base shape.
- Harmonic Spread `spread` - The factor by which the frequency of a harmonic increases relative to the previous harmonic.
- Harmonic Gain `gain` - Amplitude of the Harmonics layered on top of the base frequency.
- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Amplitude `amp` - The noise values amplitude (a scale on the values output).
- Exponent `exp` - Sets the exponent. The internal value is raised by the power of the exponent
- Offset `offset` - Adds an offset to the resulting value.
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.

## Parameters - Transform Page
- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the order of the rotations within the overall transform order.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - Translate the points through the noise space.
  * Translate `tx` -
  * Translate `ty` -
  * Translate `tz` -

- Rotate `r` - ⊞ - Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees.
  * Rotate `rx` -
  * Rotate `ry` -
  * Rotate `rz` -

- Scale `s` - ⊞ - These three fields scale the Source geometry in the three axes.
  * Scale `sx` -
  * Scale `sy` -
  * Scale `sz` -

- Pivot `p` - ⊞ - The pivot point for the transform rotates and scales.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

- Translate 4D `t4d` - Translates the points through the 4th noise dimension.

## Parameters - Output Page
- Noise `noise` - ⊞ - Enable the addition of the noise attribute.
  * Noise `noise` -
  * Noise Output Attribute Scope `noiseoutputattscope` - Output attribute scope for the noise, and based on the Noise Size parameter.

- Gradient `gradient` - ⊞ - Whether to output the noise gradient.
  * Gradient `gradient` -
  * Gradient Output Attribute Scope `gradientoutputattrscope` - Attribute Scope for the noise gradient output. Gradient is the rate of change of the noise function in X, Y and Z.

- Curl 3D `curl3d` - ⊞ - Whether to output the 3D curl of the noise.
  * Curl 3D `curl3d` -
  * Curl 3D Output Attribute Scope `curl3doutputattscope` - Sets the attribute scope when outputting 3D curl noise

- Curl 2D `curl2d` - ⊞ - Whether to output the 2D curl of the noise.
  * Curl 2D `curl2d` -
  * Curl 2D Output Attribute Scope `curl2doutputattscope` - Sets the attribute scope when outputting 2D curl noise

- Combine Operation `combineop` - ⊞ - Specify how to combine the output value with the combine attribute value.
  * None `none` -
  * Add `add` -
  * Multiply `mult` -
  * Translate along Normal `translatealongnormal` -

- Combine Entity `combineentity` - ⊞ - Specify which computed value to use for the combine operation.
  * Noise `noise` -
  * Curl 3D `curl3d` -
  * Curl 2D `curl2d` -

- Combine Attribute Scope `combineattrscope` - Input attribute scope for the combine operation.
- Output Attribute Scope `outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `overrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attrtype` - ⊞ - The output attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * Color `color` -
  * Color (double) `dcolor` -
  * Direction `dir` -
  * Direction (double) `ddir` -

- Components `attrnumcomps` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `attrdefaultval` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `attrdefaultval0` - Default value(s) of the attribute.
  * Default Value `attrdefaultval1` - Default value(s) of the attribute.
  * Default Value `attrdefaultval2` - Default value(s) of the attribute.
  * Default Value `attrdefaultval3` - Default value(s) of the attribute.

- Compute Point Normals `computenormals` - Whether to compute point normals as a post operation.
- Mode `mode` - ⊞ - Selects the shape of the field.
  * Performance `performance` -
  * Quality `quality` -

## Parameters - Map Page
- Mapping `map` - Start of Sequential Parameter Blocks for attribute-to-parameter mapping.
- OP `map0op` - Source OP for parameter mapping. The default of _in0 means the input POP.
- Element `map0element` - The attribute (or component of an attribute) that will be mapped to a parameter per-point.
- Parameter `map0parm` - ⊞ - Parameter on the current POP that will be mapped from the Element (the attribute).
  * period (Period) `period` -
  * offset (Offset) `offset` -
  * amp (Amplitude) `amp` -
  * exp (Exponent) `exp` -
  * spread (Harmonic Spread) `spread` -
  * gain (Harmonic Gain) `gain` -

- Combine Operation `map0combineop` - ⊞ - Combine operation for attribute value with parameter value.
  * Set `set` -
  * Multiply `mult` -
  * Add `add` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Noise POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
