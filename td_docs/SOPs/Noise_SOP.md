---
url: https://docs.derivative.ca/Noise_SOP
category: SOPs
title: Noise_SOP
---

# Noise SOP
## Summary

The Noise SOP displaces geometry points using noise patterns. It uses the same math as the [Noise CHOP](https://docs.derivative.ca/Noise_CHOP "Noise CHOP").
[noiseSOP_Class](https://docs.derivative.ca/NoiseSOP_Class "NoiseSOP Class")

## Parameters - Noise Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Attribute `attribute` - ⊞ - This menu sets which attribute of the geometry the Noise SOP acts on.
  * Point Position `pos` - Noise is applied in the direction of the point normal. If no normal is specified, a normal is computed.
  * Point Normals `n` - Noise is applied to each component of the normal independently and then the vector is renormalized.
  * Point Diffuse Color `cd` - Noise is applied to each component of the color independently.
  * Point Alpha `alpha` - Noise is applied to alpha.
  * Point Texture UV `uv` - Noise is applied to each component uv independently.
  * Point Texture W `w` - Noise is applied to texture w.

- Type `type` - ⊞ - The noise function used to generate noise. The functions available are:
  * Sparse `sparse` - Produces high quality, continuous noise based on Sparse Convolution.
  * Hermite `hermite` - Quicker than Sparse, but produces lower quality noise.
  * Harmomic Summation `harmonic` - Sparse noise with the ability to control the frequency step of the harmonics. Takes the longest to compute.
  * Brownian `brownian` - Works like a bug in random flight. With Num of Integrals at 2, its acceleration is changed randomly every frame.
  * Random `random` - (White Noise) Every sample is random and unrelated to any other sample. It is the same as "white noise" in audio.
  * Alligator `alligator` - Cell Noise.

- Seed `seed` - Any number, integer or non-integer, which starts the random number generator. Each number gives completely different noise patterns, but with similar characteristics.
- Period `period` - The approximate separation between peaks of a noise cycle. It is expressed in Units. Increasing the period stretches the noise pattern out.
Period is the opposite of frequency. If the period is 2 seconds, the base frequency is 0.5 cycles per second, or 0.5Hz for short. Hz refers to Hertz, the electrical and audio engineer of the 19th century, not the car guy.
If the Type is set to Random, setting this to zero will produce completely random noise. Otherwise, the period should be greater than zero.
- Harmonics `harmon` - The number of higher frequency components to layer on top of the base frequency. The higher this number, the bumpier the noise will be (as long as roughness is not set to zero). 0 Harmonics give the base shape.
Harmonics with a base frequency of 0.1Hz will by default produce harmonics at 0.2Hz, 0.4Hz, 0.8Hz, etc. (up to the number of harmonics specified by the Harmonics parameter).
- Harmonic Spread `spread` - The factor by which the frequency of the harmonics are increased. It is normally 2. A spread of 3 and a base frequency of 0.1Hz will produce harmonics at 0.3Hz, 0.9Hz, 2.7Hz, etc.. This parameter is only valid for the Harmonic Summation type.
- Roughness `rough` - Controls the effect of the higher frequency noise. When Roughness is zero, all harmonics above the base frequency have no effect. At one, all harmonics are equal in amplitude to the base frequency. When Roughness is between one and zero, the amplitude of higher harmonics drops off exponentially from the base frequency.
The default roughness is 0.5. This means the amplitude of the first harmonic is 0.5 of the base frequency, the second is 0.25, the third is 0.125. The harmonics are added to the base to give the final shape. The Harmonics parameter and the Roughness parameter must both be non-zero to see the harmonic effects.
- Exponent `exp` - Pushes the noise values toward 0, or +1 and -1. (It raises the value to the power of the exponent.) Exponents greater than one will pull the channel toward zero, and powers less than one will pull peaks towards +1 and -1. It is used to reshape the channels.
- Number of Integrals `numint` - Defines the number of times to integrate (see the [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP")) the Brownian noise. Higher values produce smoother curves with fewer features. Values beyond 4 produce somewhat identical curves. This parameter is only valid for the Random noise type.
- Amplitude `amp` - Defines the noise value's amplitude (a scale on the values output).
- Keep Computed Normals `keepnormals` -

## Parameters - Transform Page
The Translate, Rotate, Scale and Pivot parameters let you sample in a different part of the 3D noise space. Imagine a different noise value for every XYZ point in space. Normally, the Noise SOP samples the noise space from (0,0,0) along the X-axis in steps of 2/period.
By changing the transform, you are translating, rotating and scaling the line along which the Noise SOPs samples the noise space. A slight Y-rotation is like walking in a straight path in the mountains, recording your altitude along the way, then re-starting from the same initial location, walking in a slightly different direction. Your altitude starts off being similar but then diverges.
- Transform Order `xord` - ⊞ - The menu attached to this parameter allows you to specify the order in which the transforms will take place. Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - The rotational matrix presented when you click on this option allows you to set the transform order for the rotations. As with transform order (above), changing the order in which the rotations take place will alter the final position.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - Translate the sampling plane through the noise space.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - Rotate the sampling plane in the noise space.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - Scale the sampling plane.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - Control the pivot for the transform of the sampling plane.
  * X `px` -
  * Y `py` -
  * Z `pz` -

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Noise SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
