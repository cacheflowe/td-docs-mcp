---
url: https://docs.derivative.ca/Random_POP
category: POPs
title: Random_POP
---

# Random POP
## Summary

The Random POP takes its input and either (1) generates a new attribute containing random values, or (2) sets, adds or multiplies an existing attribute by a random value for each point.
The random values can be applied to point, vertex or primitive attributes.
By default, the random values are uniformly distributed between 0 and 1, but there is a variety of alternate distributions controlled with the Type menu. These include Gaussian (also known as Normal) distribution (where most points are near the center of the range), two values randomly chosen with a fraction probability of each (Two Values), a random Direction vector (within a certain cone angle) which always has length of 1, random float3 vectors within a unit Sphere, and Exponential which is an exponential dropoff above 0 separately in each axis.
The random values can be generated within a specified range (Value A and Value B), and then optionally clamped between two values.
There is an option to generate 2 or more points for every input point to increase the density of points around the source points. (Extra Points per Source Point)
The random values can also be restricted to certain point, vertex or primitive Groups.
Tip: You can get random distributions radially around a point by using the [Projection POP](https://docs.derivative.ca/Projection_POP "Projection POP") by generating random numbers in polar space and converting to Cartesian.
**Per-point mapping of parameters** - The Random POP has a Map page, which allows every point to get a different value for Amplitude, Offset, Exponent, Period, Value A and B and other parameters. In this mechanism, a separate attribute in the input contains values that override (or add to / multiply by) the parameter value. See [Mapping POP Attributes to Parameters](https://docs.derivative.ca/Mapping_POP_Attributes_to_Parameters "Mapping POP Attributes to Parameters").
See also [Point Generator POP](https://docs.derivative.ca/Point_Generator_POP "Point Generator POP"), [Noise POP](https://docs.derivative.ca/Noise_POP "Noise POP")
[randomPOP_Class](https://docs.derivative.ca/RandomPOP_Class "RandomPOP Class")

## Parameters - Random Page
- Extra Points per Source Point `extrapts` - Determines how many additional random points are generated per input point.
- Type `type` - ⊞ - Determines the random type.
  * Constant `constant` -
  * Two Values `twovalues` -
  * Uniform (Continuous) `uniform` -
  * Uniform (Discrete) `uniformdiscrete` -
  * Direction `direction` -
  * Inside Sphere `insidesphere` -
  * Normal (Gaussian) `normal` -
  * Exponential `exponential` -
  * Log-Normal `lognormal` -
  * Cauchy-Lorentz `cauchylorentz` -
  * Custom Ramp `customramp` -
  * None `none` -
  * Gaussian (Normal) `gaussian` -

- CHOP `chop` - When the distribution type is Custom Ramp, the CHOP to use for the custom ramp.
- Random Size `randomsize` - ⊞ - Number of random components.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Seed `seed` - Numerical value that initializes the randomization.
- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Amplitude `amp` - For certain types of random values, the random values amplitude (a scale on the values output).
- Exponent `exp` - Sets the exponent. The internal value is raised by the power of the exponent
- Offset `offset` - Adds an offset to the resulting value.
- Value A `valuea` - One of two values determining the random numbers that are output.
- Value B `valueb` - One of two values determining the random numbers that are output.
- Value B Probability `valuebproba` - The probability that the numbers will be biased toward value B vs A.
- Clamp Value `clamp` - Whether to clamp the output value between a minimum and a maximum.
- Clamp Min `minval` - Minimum output value.
- Clamp Max `maxval` - Maximum output value.
- Cone Direction `conedir` - ⊞ - When random distribution is direction, specifies the cone direction.
  * Cone Direction `conedirx` -
  * Cone Direction `conediry` -
  * Cone Direction `conedirz` -

- Cone Angle `coneangle` - When random distribution is direction, specifies the cone angle around the cone direction.
- Combine Operation `combineop` - ⊞ - Specify how to combine the output value with the combine attribute value.
  * Set `set` -
  * Add `add` -
  * Multiply `mult` -
  * Translate along Normal `translatealongnormal` -

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

- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Compute Point Normals `computenormals` - Whether to compute point normals as a post operation.

## Parameters - Map Page
- Mapping `map` - Start of Sequential Parameter Blocks for attribute-to-parameter mapping.
- OP `map0op` - Source OP for parameter mapping. The default of _in0 means the input POP.
- Element `map0element` - The attribute (or component of an attribute) that will be mapped to a parameter per-point.
- Parameter `map0parm` - ⊞ - Parameter on the current POP that will be mapped from the Element (the attribute).
  * amp (Amplitude) `amp` -
  * exp (Exponent) `exp` -
  * offset (Offset) `offset` -
  * valuea (Value A) `valuea` -
  * valueb (Value B) `valueb` -
  * valuebproba (Value B Probability) `valuebproba` -
  * stepval (Step Value) `stepval` - The minimum difference between two random values for uniform discrete mode.
  * minval (Clamp Min) `minval` -
  * maxval (Clamp Max) `maxval` -
  * conedir (Cone Direction) `conedir` -
  * conedirx `conedirx` -
  * conediry `conediry` -
  * conedirz `conedirz` -
  * coneangle (Cone Angle) `coneangle` -

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
Extra Information for the Random POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
