---
url: https://docs.derivative.ca/Inverse_Curve_CHOP
category: CHOPs
title: Inverse_Curve_CHOP
---

# Inverse Curve CHOP
## Summary

The Inverse Curve CHOP calculates an inverse kinematics simulation for [bone objects](https://docs.derivative.ca/Bone_COMP "Bone COMP") using a curve object.
The Inverse Curve CHOP will stretch and position a set of bones to follow a curve defined by another set of [objects](https://docs.derivative.ca/Object "Object") (guide).
Specify the first and last bone in the chain with Bone Start / Bone End.
Specify the Guide by listing them in order, space separated, in the Guide Components field. This parameter also accepts patterns and wildcards. Example: `null[1-5] null17 null4`. You can also specify bones in this group as well.
The CHOP will then create a set of rotate and bone-length channels for each bone. Additionally, the CHOP will also output 3 translate channels for the first bone in the chain. It will also setup the export links automatically, so you just have to turn on the export flag for this CHOP.
The way the CHOP solves this system is by creating a guide curve between the supplied Guide objects. Use the Interpolation and Order parameters to define what type of curve it will use. By default, the control vertices of the curve will be the centroids of the object. The curve is also given orientation, by adopting the orientation of each guide object. The bones line up their X axes with this orientation.
You can view this curve by using the [Inverse Curve SOP](https://docs.derivative.ca/Inverse_Curve_SOP "Inverse Curve SOP"). Just supply it with the name of the Inverse Curve CHOP and it will extract the geometry for viewing/debugging purposes. It actually will contain 3 curves (the original guide, and the guide displaced in +X and +Y). These curves can be skinned with a [Skin SOP](https://docs.derivative.ca/Skin_SOP "Skin SOP") for better feedback, etc.
The span parameters can be used to trim out the beginning and end of the guide curve if so needed. For example Span 0.3 0.7 will lay the bones along the middle 40% of the curve.
In the rare case that the user has setup a curve with all the X axes (twists) pointing along the same direction of the curve, then the Up Vector parameter is used to break the tie, so to speak. However, this curve setup is likely degenerate to start with and should be avoided by twisting all the objects 90 degrees.
[inversecurveCHOP_Class](https://docs.derivative.ca/InversecurveCHOP_Class "InversecurveCHOP Class")

## Parameters - Inverse Curve Page
- Guide Components `guide` - The set of objects describing the curve.
- Bone Start `bonestart` - The first bone in the chain to place.
- Bone End `boneend` - The last bone in the chain to place.
- Span `span` - ⊞ -
  * `span1` - The beginning fraction of the guide curve to align to.
  * `span2` - The end fraction of the guide curve to align to.

- Interpolation `interpolation` - ⊞ - The type of guide curve to create with the guide components.
  * Polygonal Curve `polygon` - Create a polygon, with a vertex at each guide component.
  * Bezier Curve `bezier` - Create a Bezier curve, with a control point at each guide component.
  * NURBS Curve `nurbs` - Create a NURBs curve, with a control point at each guide component.

- Order `order` - The curve order when using NURBs or Bezier interpolation.
- Up Vector `upvector` - ⊞ - Control bone twist with this parameter.
  * X `upvectorx` - X component of up vector.
  * Y `upvectory` - Y component of up vector.
  * Z `upvectorz` - Z component of up vector.

- Map Exports `mapexports` - Export the calculated transform values directly onto the bone chain parameters.

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
Extra Information for the Inverse Curve CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
