---
url: https://docs.derivative.ca/Object_CHOP
category: CHOPs
title: Object_CHOP
---

# Object CHOP
## Summary

The Object CHOP compares two objects and outputs channels containing their raw or relative positions and orientations. The information that can be output is:
  * Position of one object relative to another
  * Rotation of one object relative to another
  * Bearing of one object relative to another
  * Single Bearing Angle between two objects
  * Distance between the origin of two objects
  * Inverse Square of the Distance between two objects

The optional two inputs allow you to compare X,Y,Z points in world space with objects or each other. The inputs are expected to have three channels containing XYZ points (three channels with the suffix x, y and z). Alternatively, they can be in the standard transform formats as described by the [Transform CHOP](https://docs.derivative.ca/Transform_CHOP "Transform CHOP") help. These inputs replace the target and/or reference objects. Object and points can be compared with each other, but "Rotation" mode will always return zero.
See also the [SOP to CHOP](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP") and the [Parameter CHOP](https://docs.derivative.ca/Parameter_CHOP "Parameter CHOP"). They retrieve other information from [objects](https://docs.derivative.ca/Object "Object") and [SOPs](https://docs.derivative.ca/SOP "SOP").
[objectCHOP_Class](https://docs.derivative.ca/ObjectCHOP_Class "ObjectCHOP Class")

## Parameters - Object Page
- DAT Table `dat` - Uses a [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") to specify the target and reference objects to use. The first column will be the target objects while the second column will be the reference objects. No headers are used.
- Target Object `target` - The object that is being compared to the position of the reference object. The Target Object can be expressed as a text string. This can be useful when the object name needs to be a variable - it allows you to type in a name which may include expressions or variables.
- Reference Object `reference` - The object that acts as the origin of the comparison. The Reference Object can be expressed as a text string.
- Swap Target/Reference `swaptargetreference` - Swap the objects defined above in the Target Object and Reference Object parameters.

## Parameters - Output Page
- Compute `compute` - ⊞ - Specify the information to output from the objects as described in the parameters below. Except for 'measurements', these match the standard transform formats as described by the [Transform CHOP](https://docs.derivative.ca/Transform_CHOP "Transform CHOP").
  * Transform (Euler) `transform` - A transform using euler (rx ry rz) for the rotation.
  * Transform (Quaternion) `transformquat` - A transform using quaternion (qx qy qz qw) for the rotation.
  * 4x4 Matrix `mat` - A 4x4 transform matrix.
  * 3x3 Matrix `mat3` - A 3x3 transform matrix. This includes scale/rotation but no translation.
  * Measurements `measure` - Enables the toggles below to select what to measure. Measurements give you one object's position relative to another. You get the XYZ of the origin of the Target Object relative to the origin and rotation of the Reference Object. That is, you get the XYZ of the target object's origin as if you were at the 0,0,0 location (origin) of the Reference Object, looking down the Reference Object's Z-axis.

- Position `translate` - The displacement from the reference object to the target object.
- Rotation `rotate` - The orientation difference from the reference object to the target object.
- Scale `scale` - The scale difference from reference object to the target object.
- Quaternion `quat` - The quaternion from reference object to the target object.
- Bearing `bear` - The rotation necessary for the reference object to be facing the target object.
- Single Bearing Angle `singlebear` - An angle representing where the target object is relative to the reference object. Zero degrees is directly in front, 90 degrees is beside and 180 degrees is behind.
- Distance `distance` - The distance between the two objects.
- Inverse Square Distance `invsqr` - The inverse squared distance between the two objects, useful for modeling electric forces, audio dropoff and gravity.
- Transform Order `xord` - ⊞ - The transform order to use for Rotation, Scale, Transform, Bearing, or Single Bearing Angle Compute modes.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - The rotation order to use for Rotation, Scale, Transform, Bearing, or Single Bearing Angle Compute modes.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Include Order Channels `includeorderchans` - Turn on to include channels for Transform Order and Rotate Order.
- Bearing Reference `bearingref` - ⊞ - Bearing requires a direction to use as a reference base.
  * X Axis `x` -
  * Y Axis `y` -
  * Z Axis `z` -
  * Bearing Vector `vector` -

- Bearing Vector `bearing` - ⊞ - An arbitrary base direction for the bearing calculation.
  * X `bearingx` -
  * Y `bearingy` -
  * Z `bearingz` -

- Point Scope X `tscopex` - When one of the optional point inputs is connected, this determines which channels represent X, Y and Z.
- Point Scope Y `tscopey` - When one of the optional point inputs is connected, this determines which channels represent X, Y and Z.
- Point Scope Z `tscopez` - When one of the optional point inputs is connected, this determines which channels represent X, Y and Z.
- Append Attributes `appendattribs` - Adds a rotate attribute to any rotation channels the Object CHOP creates.
- Smooth Rotation `smoothrotate` - When on outputs a smooth rotation curve without graphical jumps at 0, 90, etc.

## Parameters - Channel Page
- Channel Names `nameformat` - ⊞ - Sets how the created channels are named.
  * Channel Name `channel` - Automatically names channels. **For example** : `tx, ty, tz`.
  * Target and Channel Names `target` - Names channels with target prefix. **For example** : if target = `obj1`, then `obj1:tx, obj1:ty, obj1:tz`.
  * Reference and Channel Names `reference` - Names channels with reference parameter prefix. Behaves like Target and Channel Names above but uses the name of the reference object.

- Output Range `outputrange` - ⊞ - The start and end time of the desired interval of the object path.
  * Current Frame `currentframe` - Output a single sample at the current frame.
  * Current Time Slice `timeslice` - Span of samples covering the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)").
  * Start / End `startend` - Uses range defined by the Start / End parameters below.

- Cook Past Values (slow) `cookpast` - If the project has skipped one or more frames, this will attempt to cook it's inputs at multiple previous frames to avoid discontinuities in it's calculations.
- Start `start` - The start time of the desired interval of the object path.
- Start Unit `startunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- End `end` - The end time of the desired interval of the object path.
- End Unit `endunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Extend Left `left` - ⊞ - The extend condition before the CHOP interval. They are:
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - Extend condition after the interval. Same options as Extend Left.
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Default Value `defval` - The value used for the Default Value extend condition.
**Note:** When creating rotation channels, the [Transform CHOP](https://docs.derivative.ca/Transform_CHOP "Transform CHOP") and Object CHOP will select values which minimize frame-to-frame discontinuity. The graphs will appear continuous and free of 180 degree shifts.

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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Object CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
