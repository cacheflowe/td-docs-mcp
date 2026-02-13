---
url: https://docs.derivative.ca/Noise_CHOP
category: CHOPs
title: Noise_CHOP
---

# Noise CHOP
## Summary

The Noise CHOP makes an irregular wave that never repeats, with values approximately in the range -1 to +1.
It generates both smooth curves and noise that is random each sample. It uses the same math as the [Noise SOP](https://docs.derivative.ca/Noise_SOP "Noise SOP").
You can create several curves with different shapes, and you can adjust period, amplitude, harmonics and more.
Optionally, an input can be connected. It is assumed that the input contains 1 to 3 channels representing X, Y and Z coordinates of points in space, and are used to sample anywhere in 3D noise space. One index in the input produces one sample in the output.
All noise functions work identically with [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing") on and off, with the exception of Harmonic Summation and Brownian whose methods cannot be limited to 1 in Time Slice mode. When the [Timeline](https://docs.derivative.ca/Timeline "Timeline") wraps around to frame 1, the noise functions will continue uninterrupted.
[noiseCHOP_Class](https://docs.derivative.ca/NoiseCHOP_Class "NoiseCHOP Class")

## Parameters - Noise Page
- Type `type` - ⊞ - The noise function used to generate noise. The functions available are:
  * Sparse `sparse` - Produces high quality, continuous noise based on Sparse Convolution.
  * Hermite `hermite` - Quicker than Sparse, but produces lower quality noise.
  * Harmomic Summation `harmonic` - Sparse noise with the ability to control the frequency step of the harmonics. Slowest type.
  * Brownian `brownian` - Works like a bug in random flight. With Num of Integrals at 2, its acceleration is changed randomly every frame.
  * Random `random` - (White Noise) Every sample is random and unrelated to any other sample. It is the same as "white noise" in audio.
  * Alligator `alligator` - Cell Noise.

- Seed `seed` - Any number, integer or non-integer, which starts the random number generator. Each number gives completely different noise patterns, but with similar characteristics.
- Period `period` - The approximate separation between peaks of a noise cycle. It is expressed in Units. Increasing the period stretches the noise pattern out.
Period is the opposite of frequency. If the period is 2 seconds, the base frequency is 0.5 cycles per second, or 0.5Hz for short. Hz refers to Hertz, the electrical and audio engineer of the 19th century, not the car guy.
If the Type is set to Random, setting this to zero will produce completely random noise. Otherwise, the period should be greater than zero.
- Period Unit `periodunit` - Select the units to use for this parameter, Samples, Frames, Seconds, or Fraction.
- Harmonics `harmon` - The number of higher frequency components to layer on top of the base frequency. The higher this number, the bumpier the noise will be (as long as roughness is not set to zero). 0 harmonics give the base shape.
Harmonics with a base frequency of 0.1Hz will by default produce harmonics at 0.2Hz, 0.4Hz, 0.8Hz, etc. (up to the number of harmonics specified by the Harmonics parameter).
- Harmonic Spread `spread` - The factor by which the frequency of the harmonics are increased. It is normally 2. A spread of 3 and a base frequency of 0.1Hz will produce harmonics at 0.3Hz, 0.9Hz, 2.7Hz, etc. This parameter is only valid for the Harmonic Summation type.
- Roughness `rough` - Controls the effect of the higher frequency noise. When roughness is zero, all harmonics above the base frequency have no effect. At one, all harmonics are equal in amplitude to the base frequency. When roughness is between one and zero, the amplitude of higher harmonics drops off exponentially from the base frequency.
The default roughness is 0.5. This means the amplitude of the first harmonic is 0.5 of the base frequency, the second is 0.25, the third is 0.125. The harmonics are added to the base to give the final shape. The Harmonics parameter and the Roughness parameter must both be non-zero to see the harmonic effects.
- Exponent `exp` - Pushes the noise values toward 0, or +1 and -1. (It raises the value to the power of the exponent.) Exponents greater than one will pull the channel toward zero, and powers less than one will pull peaks towards +1 and -1. It is used to reshape the channels.
- Num of Integrals `numint` - Defines the number of times to integrate (see the Area CHOP p. 114) the Brownian noise. Higher values produce smoother curves with fewer features. Values beyond 4 produce somewhat identical curves. This parameter is only valid for the Random noise type.
- Amplitude `amp` - Defines the noise value's amplitude (a scale on the values output).
- Reset `reset` - Only available if operator's `Time Slice` Parameter is on. Toggling this parameter will reset the noise calculation and hold the value until the parameter is released again.
- Reset Pulse `resetpulse` - Only available if operator's `Time Slice` Parameter is on. Pulsing this parameter will reset the noise calculation.

## Parameters - Transform Page
The Translate, Rotate, Scale and Pivot parameters let you sample in a different part of the 3D noise space. Imagine a different noise value for every XYZ point in space. Normally, the Noise CHOP samples the noise space from (0,0,0) along the X-axis in steps of 2/period. `/tx /ty /tz /rx /ry /rx /sx /sy /sz /px /py /pz`     By changing the transform, you are translating, rotating and scaling the line along which the Noise CHOPs samples the noise space. A slight Y-rotation is like walking in a straight path in the mountains, recording your altitude along the way, then re-starting from the same initial location, walking in a slightly different direction. Your altitude starts off being similar but then diverges.
- Transform Order `xord` - ⊞ - Changing the Transform Order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - XYZ translation values.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - XYZ rotation, in degrees.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - XYZ scale to shrink or enlarge the transform.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - XYZ pivot to apply the above operations around.
  * X `px` -
  * Y `py` -
  * Z `pz` -

## Parameters - Constraints Page
- Constraint `constraint` - ⊞ - Constraint and its parameters allows the noise curve to start and/or end at selected values. The mean value may also be enforced. **Note:** This only works when Time Slice is Off because time slicing has no pre-determined start/end.
  * None `none` - No constraints set.
  * Start Value `start` - Sets the noise starting position to the value set in 'Starting Value' parameter below.
  * End Value `end` - Sets the noise ending position to the value set in 'Ending Value' parameter below.
  * Mean Value `offset` - Sets the noise mean position to the value set in the 'Mean Value' parameter below.
  * Start/End Values `endpoints` - Set the starting and ending position of the noise separately using the parameters below.

- Starting Value `constrstart` - Value for the starting position.
- Ending Value `constrend` - Value for the ending position.
- Mean Value `constrmean` - Value for the mean value of the noise.
- Normalize `normal` - Ensures that all noise curves fall between -1 and 1. Applied before the Amplitude parameter. Only valid for Random and Harmonic Summation noise types, since Hermite and Sparse noise are always normalized. Normalizing random noise occurs between integrations, producing a more controlled curve. **Note:** This only works when Time Slice is Off because time slicing has no pre-determined start/end.

## Parameters - Channel Page
- Channel Names `channelname` - You can creates many channels with simple patterns like "`chan[1-20]`", which generates 20 channels from chan1 to chan20. See the section, Common CHOP Parameters for a description of this and all Options. See [Scope and Channel Name Matching](https://docs.derivative.ca/CHOP_Common_Page#Scope "CHOP Common Page") Options. Each channel has a unique seed, so all channels will be different with the same parameter settings.
- Start `start` - Start of the interval, expressed in Units (seconds, frames or samples).
- Start Unit `startunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- End `end` - End of the interval, expressed in Units (seconds, frames or samples).
- End Unit `endunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Sample Rate `rate` - The sample rate of the channels, in samples per second. Default: `me.time.rate`
- Extend Left `left` - ⊞ - The left extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - The right extend conditions (before/after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Default Value `defval` - The value used for the Default Value extend condition.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Noise CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

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
