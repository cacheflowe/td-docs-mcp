---
url: https://docs.derivative.ca/Attribute_CHOP
category: CHOPs
title: Attribute_CHOP
---

# Attribute CHOP
## Summary

The Attribute CHOP adds, removes or updates attributes of the input CHOP. Currently there is only one attribute type, a "quaternion". This attribute type is used to group rotation channel triplets (rx,ry,rz) together.
Rotations sometimes need to be grouped together since interpolations on independent X, Y and Z rotations do not produce smooth results. Rotations often need Quaternion interpolation to rotate through the most direct path.
Operations such as resampling and blending recognize the rotation triplet with the "quaternion" attribute. They blend or resample the rotation channels using "spherical linear interpolation". Ordinary interpolation can produce poor blending results, whereas quaternion blending produces the shortest rotation path between two sets of rotations.
See some of the CHOPs that use the attribute: the [Join CHOP](https://docs.derivative.ca/Join_CHOP "Join CHOP"), [Composite CHOP](https://docs.derivative.ca/Composite_CHOP "Composite CHOP") and [Interpolate CHOP](https://docs.derivative.ca/Interpolate_CHOP "Interpolate CHOP"). Other CHOPs may quietly use the Quaternion attribute, such as the [Object CHOP](https://docs.derivative.ca/Object_CHOP "Object CHOP"), [Stretch CHOP](https://docs.derivative.ca/Stretch_CHOP "Stretch CHOP") and the [Resample CHOP](https://docs.derivative.ca/Resample_CHOP "Resample CHOP").
The Scope is needed to specify the channels that will be grouped.
[attributeCHOP_Class](https://docs.derivative.ca/AttributeCHOP_Class "AttributeCHOP Class")

## Parameters - Quaternion Page
- Function `slerp` - ⊞ - The function to perform on the attributes:
  * Pass Through `pass` - Leaves the attributes untouched.
  * Replace `replace` - Erases previous attributes and replaces them with the new ones.
  * Append `append` - Keeps previous attributes and combines them with the new attributes. If an attribute already exists on a channel and append attempts to overwrite it, an error will occur.
  * Remove `remove` - Removes all scoped channels' attributes.

- Rotate Order `rord` - ⊞ - Sets the rotation order of the rotation triplet.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

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
Extra Information for the Attribute CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
