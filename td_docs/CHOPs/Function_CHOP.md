---
url: https://docs.derivative.ca/Function_CHOP
category: CHOPs
title: Function_CHOP
---

# Function CHOP
## Summary

The Function CHOP provides more complicated math functions than found in the [Math CHOP](https://docs.derivative.ca/Math_CHOP "Math CHOP") : trigonometic functions, logarithmic functions and exponential functions, and also audio decibels (dB)-power-amplitude conversions.
Most of the functions require only one parameter, and they are applied as a unary operator to each input channel. Some functions take two parameters, and these require the use of the second input. The first parameter, X, is always a value from a channel in the first input. The second parameter, Y, is a value from a corresponding channel in the second input. Channels from each input are paired by name or index.
Since many of these functions can produce math errors, an error handling tab is provided for error handling and recovery. Errors can be handled by replacing the bad sample with a pre-defined value or by using the value of the previous sample. Alternatively, cooking can be aborted upon error for debugging networks.
Function types in decibels: as you would employ for audio or other signal strengths. -10dB means 1/10 the power, -20dB means 1/100 the power. It turns out that each 3dB means almost exactly double the power, so +12dB is 2*2*2*2 = 16 times the power. Power is proportional to the square of the amplitude. So -20dB means 1/10 the amplitude, and 6dB is double the amplitude.
[functionCHOP_Class](https://docs.derivative.ca/FunctionCHOP_Class "FunctionCHOP Class")

## Parameters - Function Page
- Function `func` - ⊞ - Which math function to apply to the channels. All of the functions are unary functions except for the binary functions 'arctan (Input1/Input2)' and 'Input1 ^ Input2'. In the cases of power functions, a negative base is inverted first to avoid imaginary numbers, and the result is negated.
  * sqrt(x) Square Root `sqrt` - Square Root of Input 1.
  * abs(x) Absolute Value `abs` - Absolute Value of Input 1.
  * sign(x) Sign `sign` - Sign of Input 1.
  * cos(x) Cosine `cos` - Cosine of Input 1.
  * sin(x) Sine `sin` - Sine of Input 1.
  * tan(x) Tangent `tan` - Tangent of Input 1.
  * acos(x) Arccosine `acos` - Arccosine of Input 1.
  * asin(x) Arcsine `asin` - Arcsine of Input 1.
  * atan(x) Arctan( Input1 ) `atan` - Arctan of Input 1.
  * atan2(y,x) Arctan( Input1 / Input2 ) `atan2` - Arctan of (Input 1 / Input 2).
  * cosh(x) Hyperbolic Cosine `cosh` - Hyperbolic Cosine of Input 1.
  * sinh(x) Hyperbolic Sine `sinh` - Hyperbolic Sine of Input 1.
  * tanh(x) Hyperbolic Tangent `tanh` - Hyperbolic Tangent of Input 1.
  * log10(x) Log base 10 `log` - Log base 10 of Input 1.
  * logN(x) Log base N `logb` - Log base Base Value of Input 1.
  * ln(x) Natural Log `ln` - Natural Log of Input 1.
  * pow(10,x) 10 ^ Input1 `pow10` - 10 to the power of Input 1.
  * exp(x) e ^ Input1 `exp` - e to the power of Input 1.
  * pow(x) Base ^ Input1 `powe` - Base value to the power of Input 1. If Base value is negative result is -((-Base Value) ^ Input 1)
  * pow(x) Input1 ^ Exponent `powb` - Input 1 to the power of Exponent value. If Input 1 is negative result is -((-Input 1) ^ Exponent Value).
  * pow(x,y) Input1 ^ Input2 `pow` - ((-Input 1) ^ Input 2)
  * dB to Power `dbtopower` - Decibel (Input 1) to amplitude.
  * Power to dB `powertodb` - Amplitude (Input 1) to decibel.
  * dB to Amplitude `dbtoamp` - Decibel (Input 1) to amplitude.
  * Amplitude to dB `amptodb` - Amplitude (Input 1) to decibel.

- Base Value `baseval` - The value of the base for 'Log base N' and 'Base ^ Input1'. parameter name `/baseval`
- Exponent Value `expval` - The value of the exponent for `'Input1 ^ Exponent'`. channel name `/expval`
- Angle Units `angunit` - ⊞ - For trigonometric functions, the angles can be measured in Degrees, Radians, or Cycles (0 to 1).
  * Degrees `deg` -
  * Radians `rad` -
  * Cycles `cycle` -

- Match by `match` - ⊞ - How to pair channels together from the two inputs for the binary functions, by name or by channel index.
  * Channel Number `index` -
  * Channel Name `name` -

## Parameters - Error Page
- Error Handling `error` - ⊞ - How to correct samples with math errors:
  * Abort With Error Message `abort` - Cooking aborts.
  * Replace With Specified Values `replace` - Values specified below.
  * Use The Previous Value `useprev` - Uses the last good result.

+ Infinity Value `pinfval` - Value to use when an infinity error occurs. Caused by sinh(), cosh() and tan().
- Infinity Value `ninfval` - Value to use when a negative infinity error occurs. Caused by sinh() and tan().
- Domain Error Value `domval` - Value to use when a domain error occurs. Caused by asin(), acos(), log10(), logN(), ln() and sqrt().
- Divide Error Value `divval` - Value to use when a divide by zero error occurs. Caused by pow(x,y).

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Function CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
