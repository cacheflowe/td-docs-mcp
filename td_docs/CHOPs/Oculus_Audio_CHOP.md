---
url: https://docs.derivative.ca/Oculus_Audio_CHOP
category: CHOPs
title: Oculus_Audio_CHOP
---

# Oculus Audio CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The Oculus Audio CHOP uses the Oculus Audio SDK to take a mono sound channel and create a spatialized stereo pair or channels for that sound.
See also: [Audio Render CHOP](https://docs.derivative.ca/Audio_Render_CHOP "Audio Render CHOP")
[oculusaudioCHOP_Class](https://docs.derivative.ca/OculusaudioCHOP_Class "OculusaudioCHOP Class")

## Parameters - Setup Page
- Active `active` - When enabled, will actively spatialize the audio input.
- Head Object COMP `headobject` - A COMP that represents the listener's (ie. head) transform. Must be a COMP that contains transform data, such as a Geometry or Camera COMP.
- Source Object COMP `sourceobject` - A COMP that represents the audio source's transform. Must be a COMP that contains transform data, such as a Geometry or Camera COMP.
- Minimum Range `minrange` - The minimum attenuation range of the audio source (in meters).
- Maximum Range `maxrange` - The maximum attenuation range of the audio source (in meters)
- Diameter `diameter` - The virtual diameter of the audio source. By default the diameter is 0 which means the audio source is just a point in space.
- Band Hint `bandhint` - ⊞ - If the audio source content is known, this parameter can be set to improve overall sound quality.
  * None `none` -
  * Wide Band `wide` - Used to help mask certain artifacts for wideband audio sources with a lot of spectral content, such as music, voice andnoise.
  * Narrow Band `narrow` - Used for narrowband audio sources that lack broad spectral content such as pure tones (sine waves, whistles).

- Reflections and Reverb `reflectrevert` - When enabled, audio reflection and reverb will be enabled.
- Attenuation `attenuation` - ⊞ - Select attentuation calculation between the audio source and listener (head).
  * None `none` - Soujnd is not attenuated
  * Fixed `fixed` - Attenuate based on a fixed value. This fixed value is set using the Attenuation Scale parameter.
  * Inverse Square `inversesequare` - Attenuation calculated based on inverse square.

- Attenuation Scale `attenuationscale` - Set the fixed attenuation value when in Fixed Attenuation mode.
- Box Room Mode `boxroommode` - Enables box room calculations for reverberation.
- Room Size `roomsize` - ⊞ - Sets the size of the box room.
  * X `roomsizex` -
  * Y `roomsizey` -
  * Z `roomsizez` -

- Room Left Reflect `roomleftrelfect` - Reflection level for the left of the box (ie. what percentage of the audio is reflected back).
- Room Right Reflect `roomrightrelfect` - Reflection level for the right of the box (ie. what percentage of the audio is reflected back).
- Room Bottom Reflect `roombottomrelfect` - Reflection level for the bottom of the box (ie. what percentage of the audio is reflected back).
- Room Top Reflect `roomtoprelfect` - Reflection level for the top of the box (ie. what percentage of the audio is reflected back).
- Room Front Reflect `roomfrontrelfect` - Reflection level for the front of the box (ie. what percentage of the audio is reflected back).
- Room Back Reflect `roombackrelfect` - Reflection level for the back of the box (ie. what percentage of the audio is reflected back).

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

## Info CHOP Channels
Extra Information for the Oculus Audio CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
