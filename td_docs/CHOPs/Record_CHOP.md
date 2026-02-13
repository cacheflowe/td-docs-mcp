---
url: https://docs.derivative.ca/Record_CHOP
category: CHOPs
title: Record_CHOP
---

# Record CHOP
## Summary

The Record CHOP takes the channels coming in the first (Position) input, converts and records them internally, and outputs the stored channels as the CHOP output. The optional second (Active) input is used to enable and disable the recording.
During recording, the Record CHOP uses only the values of the first input at the current frame. The Type determines how the input values are converted.
**Tip** : The [Trail CHOP](https://docs.derivative.ca/Trail_CHOP "Trail CHOP") also records the last window of samples, and more powerfully, the gestureCapture component in the Palette gives more control over multi-captures and smoothing channel data.
If Record is set to Auto Range, and the Active input goes on, and TouchDesigner is playing, then any existing storage array is cleared, and the channels are recorded in a new storage array until Active goes off. This behaves like a sampler.
The [Mouse In CHOP](https://docs.derivative.ca/Mouse_In_CHOP "Mouse In CHOP") and [Keyboard In CHOP](https://docs.derivative.ca/Keyboard_In_CHOP "Keyboard In CHOP") are often attached to the Position and Active inputs respectively of the Record CHOP to perform the recording of channels from mouse movements, enabled by pressing a keyboard key (see the [Keyboard In CHOP](https://docs.derivative.ca/Keyboard_In_CHOP "Keyboard In CHOP")).
Record Segment is useful for recording trails, snakes, and other models that use a time-history of motion.
See the [Time Slice CHOP](https://docs.derivative.ca/Time_Slice_CHOP "Time Slice CHOP") for input smoothing.
[recordCHOP_Class](https://docs.derivative.ca/RecordCHOP_Class "RecordCHOP Class")

## Parameters - Control Page
- Record `record` - ⊞ - When and how much to record:
  * Off `off` - Leaves the output unmodified.
  * On `on` - Always records when playing forward. When the active input is in the off state the input is maintained at its current values.
  * Add `add` - Adds (offsets) to an existing set of channels previously recorded in the Record CHOP. The channels are left unmodified while the Active input is in the off state.
  * Auto Range `auto` - Creates an interval based on Active on/off.

- Record Input `sample` - ⊞ - Determines whether record should sample the time slice or the current frame. You would generally want to use Current Time Slice, for audio, as all frames will be evaluated.
If the interval is set to be the Current Frame, it will always cook (only look at) the current frame (things downstream still cook regardless of this setting however). Thus, it should generally not be used for audio, but rather fro things like device input, because it interpolates the values between the captured frames.
  * Current Frame `scur` -
  * Current Time Slice `sslice` -

- Interpolation `interp` - ⊞ - Determines how to compute missed input samples using interpolation. Using Hold Previous Value does just that; Linear and Cubic interpolation will create a mathematical blend of values in a linear (straight line between values in time), or cubic (smooth round-off curve between beginning and ending values).
  * Hold Previous Value `hold` -
  * Linear `linear` -
  * Cubic `cubic` -

- Record Output `output` - ⊞ - Determines the frame range that gets output from the CHOP.
  * Full Range `full` - The frame range grows from the moment and frame you start recording. Samples get recorded over when TouchDesigner goes over a frame a second time. Press Reset Channels to start again.
  * Current Frame `curframe` - Outputs the current frame only.
  * Current Frame at Frame 1 `frame1` - Outputs the current frame but shifts it to frame 1. If the channels are not changing value, it reduces the amount of cooking that takes place.
  * Current Time Slice `slice` - Outputs the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") of samples only.
  * Segment `segment` - Outputs a sliding window of samples defined by the Record Segment start/end length.

- Record Segment `segment` - ⊞ - The data gets recorded in a fixed-range interval and the most recent data gets recorded at the end of the interval and the remaining samples get shifted toward the start of the interval. This is useful for making snakes.
  * `segment1` -
  * `segment2` -

- Record Segment Unit `segmentunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Reset Channels `reset` - The current output is cleared and all subsequent channels will commence single sample lengths.
- Reset Condition `resetcondition` - ⊞ - Enabled when a CHOP is connected to the Record CHOP's 3rd input (ie. Input 2). Determines what condition is required to trigger a reset using this input.
  * Off to On `offtoon` - Resets the recording when the input channel goes from Off to On ie. 0 to 1.
  * While On `on` - Resets the recording when the input channel is On ie. 1.
  * On to Off `ontooff` - Resets the recording when the input channel goes from On to Off ie. 1 to 0.
  * While Off `off` - Resets the recording when the input channel is Off ie. 0.

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
Extra Information for the Record CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
