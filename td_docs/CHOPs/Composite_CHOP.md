---
url: https://docs.derivative.ca/Composite_CHOP
category: CHOPs
title: Composite_CHOP
---

# Composite CHOP
## Summary

The Composite CHOP layers (blends) the channels of one CHOP on the channels of another CHOP. The first input is the base input and the second is the layer input. It is designed for blending static multi-frame motion channels. Blending time-sliced channels or single-frame channels should be done with the [Blend CHOP](https://docs.derivative.ca/Blend_CHOP "Blend CHOP").
Over the interval of the layer, the layer channels are blended with the base channels. The contribution of the layer is eased-in and eased-out according to the Start, Peak, Release and End parameters. The base is unaffected outside the interval of the layer.
The Effect parameter determines the amount of contribution of the layer.
If Base Hold is 0, the layer input will completely replace the base input when the effect is 1. If the Base Hold is 1, the layer will be added to the base.
The interval of the output starts at the minimum of the base and layer. The interval of the output ends at the maximum of the base and layer. The base's extend conditions are used if the layer lies outside the base.
**Note:** If the third input is supplied, the Effect page will be overridden by the third input's first channel, which should contain the effect values over the range of the layer.
[compositeCHOP_Class](https://docs.derivative.ca/CompositeCHOP_Class "CompositeCHOP Class")

## Parameters - Composite Page
- Base Hold `base` - Determines how much of the base to blend into the output at points where the layer has an effect.
- Match by `match` - ⊞ - Matches channels in the base input with ones in the layer input by either index or name.
  * Channel Number `index` -
  * Channel Name `name` -
  * Channel Union `union` -

- Quaternion Blend `quatrot` - Allows rotations with the quaternion attribute set to use spherical interpolation to produce smooth rotation blending (set in the Attribute CHOP).
- Shortest Path Rotation Blending `shortrot` - It better-handles the blending from one set of angles to another, taking into account 0 degrees is 360 degrees.
- Rotation Scope `rotscope` - Pattern (like *rx *ry *rz) that identifies which channels are rotations that should be handled specially as per the above option.
- Cycle Length `cyclelen` - Blend 0 degrees to this angle, generally 360.

## Parameters - Effect Page
- Effect `effect` - **Note:** If the third input is supplied, the Effect page will be overridden by the third input's first channel, which should contain the effect values over the range of the layer.
- Unit Values `relative` - ⊞ - Sets the meaning of the next four parameters - either Absolute values, Relative to the Start/End of the channel, or Relative to the Current Frame. The layer and base are never shifted.
  * Absolute `abs` -
  * Relative to Start/End `rel` -
  * Relative to Current Frame `cur` -

- Start `start` - The beginning of the composite interval. Effect is zero at the start.
- Start Unit `startunit` -
- Peak `peak` - Where the composite operation reaches maximum effect.
This value is held until the release point.
- Peak Unit `peakunit` -
- Release `release` - The point at which the effect begins to fall back towards zero.
- Release Unit `releaseunit` -
- End `end` - The end of the composite operation's effect. The effect reduces to zero again.
- End Unit `endunit` -
- Rise Shape `risefunc` - ⊞ - How to interpolate from one CHOP to another. It is the shape of the segment between the Start and Peak indices.
  * Linear `lin` -
  * Ease in `ei` -
  * Ease out `eo` -
  * Ease in Ease out `cos` -
  * Cubic `cub` -
  * Add `add` -
  * Hold Previous `holdprev` -

- Fall Shape `fallfunc` - ⊞ - How to interpolate from one CHOP to another. It is the shape of the segment between the Release and End.
  * Linear `lin` -
  * Ease in `ei` -
  * Ease out `eo` -
  * Ease in Ease out `cos` -
  * Cubic `cub` -
  * Add `add` -
  * Hold Previous `holdprev` -

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
Extra Information for the Composite CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
