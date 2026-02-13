---
url: https://docs.derivative.ca/Gesture_CHOP
category: CHOPs
title: Gesture_CHOP
---

# Gesture CHOP
## Summary

The Gesture CHOP records a short segment of the first input and loops this segment in time with options as specified in the Gesture Page. The second input defines the "listen" input. The third input is used to reset the gesture.
**Tip** : The `gestureCapture` component in the palette is much more powerful and flexible to capture and record channels, and has full UI.
In the Gesture CHOP, when the first channel of the listen input goes above zero, the Gesture CHOP begins recording the first input's channels. While listen is on, the input channels are output exactly as is. When the listen is turned off, the recorded segment of the channels is processed (trimmed and blended). While listen is off, the recorded segment is looped continuously.
The Gesture CHOP determines the number of beats that the listen was on for; this defines the period of the loop. If the beat frequency changes, the period will change with it.
If "Fit to Nearest Cycle" is Off, the beats are ignored and the gesture length is exactly the time it took to record - the recorded segment will be looped back with a period equal to the recorded length. When On, the captured gesture will be extended or trimmed to be a multiple of the beats per cycle.
[gestureCHOP_Class](https://docs.derivative.ca/GestureCHOP_Class "GestureCHOP Class")

## Parameters - Gesture Page
- Play Mode `playmode` - ⊞ - Controls the gesture playback.
  * Locked to Timeline `locked` - This mode locks the gesture position to the [Timeline](https://docs.derivative.ca/Timeline "Timeline").
  * Sequential `sequential` - This mode continually plays the gesture regardless of the timeline position. Reset and Reset Condition parameters below are enabled to allow some control.

- Fit to Nearest Cycle `fitmethod` - When on the captured gesture will be extended or trimmed to be a multiple of the Beats Per Cycle.
- Beats per Cycle `numbeats` - Specifies the number of beats to cycle the recorded animation around. If the recorded animation is longer than a multiple of the Beats Per Cycle, it will loop at that multiplied length.
- Step Output `step` - If on, the cycled animation will adjust up or down each iteration to avoid jumps when looping to the beginning. For example, it would turn a simple 0-1 ramp gesture into a continuously increasing line.
- Step Reset `stepreset` - When On and you re-record a gesture, the step will be zeroed.
- Blend Time `blend` - How much of the recorded segment to use as a blend region. The blend region is used to blend the beginning of the segment to the end so that a seemless loop is produced.
- Blend Time Unit `blendunit` -
- Interpolate Samples `interp` - If on, recorded samples are interpolated when scaling occurs, otherwise the nearest sample is selected.
- Speed `speed` - Scales the rate of playback for the segment.
- Speed Unit `speedunit` -
- Reset Condition `resetcondition` - ⊞ - This menu determines how the Reset input (the third input) triggers a reset of the channel(s).
  * Off to On `offtoon` - Channels are reset when the Reset input goes off to on.
  * While On `on` - Channels are reset when the Reset input goes on. The channel will hold the reset value until the input turns off.
  * On to Off `ontooff` - Channels are reset when the Reset input goes on to off.
  * While Off `off` - Channels are reset when the Reset input goes off. The channel will hold the reset value until the input turns on.

- Reset `reset` - Resets the gesture while On when in **Sequential** Play Mode.
- Reset Pulse `resetpulse` - Resets the gesture.

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
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Gesture CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
