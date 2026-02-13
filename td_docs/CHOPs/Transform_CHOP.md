---
url: https://docs.derivative.ca/Transform_CHOP
category: CHOPs
title: Transform_CHOP
---

# Transform CHOP
## Summary

The Transform CHOP takes transformations in various formats, applied operations to them, and outputs them in various formats. It can be used to:
  * Change the position and orientation of an object.
  * Convertion transforms one format to another format.
  * Convert a set of transform channels with a certain transform order into an equivalent set of channels with a different transform order.
  * Change the direction, starting point and scale of motion capture data or other data being calibrated to match other reference frames.

( See also the [Transform XYZ CHOP](https://docs.derivative.ca/Transform_XYZ_CHOP "Transform XYZ CHOP") for doing transforms on XYZ positions and vectors. )
Three transform formats exists:
  * Transform with Euler angles for rotation. These are defined by channels with suffixes: `tx ty tz, rx ry rz, sx sy sz` and an optional transform and rotate order `xord and rord`.
  * Transform with Quaternion for rotation. These are defined by channels with suffixes: `tx ty tz, qx qy qx qw, sx sy sz` and an optional transform order `xord`.
  * A 4x4 or 3x3 matrix. These are defined by channels with suffixes: `m00, m10, m20, m30, m01, m11... m33`. Where the notation is `m[_row_][_col_]`. The matrix should be be in column-major order, that is to say, the translate portion should be in`m03, m13, m23`. The 4th row and column can be omitted to use a 3x3 matrix instead. Unlike the other formats, this format can not have arbitrary missing channels. Either 9 channels for 3x3 or 16 channels for 4x4 matrices must be provided.

The first two transform formats can be specified with missing channels, in which case default values will be used. 0s for translates and rotates, 1s for scale, and (0,0,0,1) for quaternion.
Frequently the input channels come from an [Object CHOP](https://docs.derivative.ca/Object_CHOP "Object CHOP") or [Parameter CHOP](https://docs.derivative.ca/Parameter_CHOP "Parameter CHOP"). Examples are:
  * geo1:tx geo1:ty geo1:tz geo1:rx ...
  * headtx headty headtz headrx
  * tx ty tz rx ... (what you would get from a Parameter CHOP)
  * cam1:m00 cam1:m10 cam1:m20 .... cam1:m33

### Multiple Transform Sets
Any of the above defines a transformation matrix. Multiple transform 'sets' can be specified by channels having different prefixes. Different sets using different formats can be all in the same CHOP. Formats can not be mixed within a set though. Each set will be combined with sets from the other input, and the transform on the 'Transform' page to create final transforms for each set.
If no inputs are connected to the CHOP, it will output the transform generated from the 'Transform' page.
If inputs are connected, the output will contain the same number of samples as the first input. Samples will be combined between the inputs 1:1, that is, the start/end range and the sample rate of the inputs are ignored. If the second input contains less samples than the first one, the extend conditions for that CHOP will be used to determine values for the samples coming from the 2nd CHOP that are out of range.
If multiple sets are provided, they will be matched 1st-to-1st set, 2nd-to-2nd set. If there are less sets in the second input than the first one, then it will loop over the sets. E.g if the first input as 5 sets and the second input as 2 sets, the matching will be 1st-to-1st, 2nd-to-2nd, 3rd-to-1st, 4th-to-2nd and 5th-to-1st.
### Order of Operation
The inputs will be combined together first, then the result from that will be combined with the transform defined on the 'Transform' page.
The channels of a Transform CHOP are frequently exported back to objects.
[transformCHOP_Class](https://docs.derivative.ca/TransformCHOP_Class "TransformCHOP Class")

## Parameters - Input Page
This page defines what the incoming channels' transform order is assumed to be. Using the incoming channels and the transform order here, a matrix for the incoming channels in built. It is then multiplied by the transformation matrix defined by the Transform page and output.
Any missing translation, rotation or scale channels will default to zero (or one in the case of scale).
- Custom Input Orders `custinputorders` - This allows the input order, if provided, to be ignored and overridden by a custom order chosen by the following two parameters.
- Transform Order `inxord` - ⊞ - Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `inrord` - ⊞ - As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Input 0 Pre Operation `input0preop` - ⊞ - Operation(s) to apply on the transforms on Input 0, before they are combined with other transforms.
  * None `none` - No operation is applied.
  * Invert `invert` - Invert the transform.
  * Transpose `transpose` - Transpose the transform. This only has an effect for matrix format transforms.
  * Invert Transpose `inverttranspose` - Invert and Transpose the transform. The transpose will only be done if the input is a matrix format transform.

- Input 1 Pre Operation `input1preop` - ⊞ - Operation(s) to apply on the transforms on Input 1, before they are combined with other transforms.
  * None `none` - No operation is applied.
  * Invert `invert` - Invert the transform.
  * Transpose `transpose` - Transpose the transform. This only has an effect for matrix format transforms.
  * Invert Transpose `inverttranspose` - Invert and Transpose the transform. The transpose will only be done if the input is a matrix format transform.

- Input Operation `inputoperation` - ⊞ - The operation that should be applied between transforms coming from Input 0 and Input 1. Refer to the main description of this node for an explanation of how multiple samples and/or transform sets are combined between the two inputs.
  * Input 0, then Input 1 `input0input1` - The operation will be `input1 * input0`. It it ordered this way since ultimately the transform is applied to a position/vector in the form input1 * input0 * Position, so the input0 operation is done first.
  * Input 1, then Input 0 `input1input0` - The operation will be `input1 * input0`.
  * Quaternion Lerp `quatlerp` -
  * Quaternion Slerp `quatslerp` -

- Input Weight `inputweight` - Specify the Blend weight for the above 'Input Operation'

## Parameters - Transform Page
This page defines an additional transform that can be combined with the transform created by combining the inputs, if any. If the node has no inputs connected then the transform generated from this page will be what is output from this node.
- Transform Order `xord` - ⊞ - See description from earlier Transform Order parameter.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - See description from earlier Rotate Order parameter.
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

- Xform Matrix/CHOP/DAT `xformmatrixop` -
- Multiply Order `multiplyorder` - ⊞ - Controls how the input transform(s) are combined with the transform specified on this page. The below two descriptions use a multiply "vector on the right" convention (column vectors).
  * Input, then Transform Page `inputxformpage` - The transforms will be combined as `Transform Page * Input`.
  * Transform Page, then Input `xformpageinput` - The transforms will be combined as `Input * Transform Page`.

- Look At `lookat` - Allows you to generate your transform channels by specifying an object you would like to Look At, or point to. The generated transform channels will be such that when you transform an object using it, it will make the object face your intended Look At Object. This is useful if, for instance, you want a camera to follow another object's movements. The Look At parameter points the object in question at the other object's origin.
**Tip:** To designate a centre of interest for the camera that doesn't appear in your scene, create a Null object and disable its display flag. Then Parent the Camera to the newly created Null object, and tell the camera to look at this object using the Look At parameter. You can direct the attention of the camera by moving the Null object with the Select state. If you want to see both the camera and the Null object, enable the Null object's display flag, and use the Select state in an additional Viewport by clicking one of the icons in the top-right corner of the TouchDesigner window.
- Up Vector `upvector` - ⊞ - When orienting an object, the Up Vector is used to determine where the positive Y axis points.
  * Up Vector `upvectorx` -
  * Up Vector `upvectory` -
  * Up Vector `upvectorz` -

- Forward Direction `forwarddir` - ⊞ - Sets which axis and direction is considered the forward direction.
  * +X `posx` -
  * -X `negx` -
  * +Y `posy` -
  * -Y `negy` -
  * +Z `posz` -
  * -Z `negz` -

- Pre Operation `preop` - ⊞ - Operation(s) to apply on the transform generated by Transform/Rotate/Scale/Pivot parameters, before it is combined with other transforms. Done before combining with the Xform Matrix and Look At.
  * None `none` - No operation.
  * Invert `invert` - Invert the transform.

- Operation `operation` - ⊞ - Controls how the input transform(s) are combined with the transform specified on this page. The below two descriptions use a multiply "vector on the right" convention (column vectors).
  * Input, then Transform Page `inputxformpage` -
  * Transform Page, then Input `xformpageinput` -
  * Quaternion Lerp `quatlerp` -
  * Quaternion Slerp `quatslerp` -

- Weight `weight` - Specify the Blend weight for the above 'Operation'

## Parameters - Output Page
This page controls what information is output from the node.
- Post Operation `postop` - ⊞ - Optionally applied one last operation to the final generated transform before it is output.
  * None `none` - No operation.
  * Invert `invert` - Invert the transform.
  * Transpose `transpose` - Transpose the transform. This only has an effect for matrix format transforms.
  * Invert Transpose `inverttranspose` - Invert and Transpose the transform. The transpose will only be done if the input is a matrix format transform.

- Output `output` - ⊞ - Specify the format the transform will be output in.
  * Transform (Euler) `transform` - The standard Translate, Rotate and Scale channels. t[xyz], r[xyz], s[xyz]. Will also include xord and rord channels for Transform and Rotate Order, unless 'Include Order Channels' is turned off.
  * Transform (Quaternion) `transformquat` - Translate, Quaternion (for rotation) and Scale channels. t[xyz], q[xyzw], s[xyz]. Will also include xord channel for Transform Order, unless 'Include Order Channels' is turned off.
  * 4x4 Matrix `mat` - 16 channels for a 4x4 matrix. The channels will be output in column-by-column order. That is, with the last 4 channels being the 'translate' portion of the matrix.
  * 3x3 Matrix `mat3` - 9 channels for a 3x3 matrix. This includes the rotation and the scale, but not the translation.
  * Position `position` - The final position of the transform in space. This doesn't include any orientation information.

- Determinant `determ` - When outputting a matrix, it's determinant can also be output by enabling this parameter.
- Un-matched Channels `unmatchedchans` - ⊞ - Controls how channels that don't match the naming convention for the various transform format are treated.
  * Warn `warn` - Give a warning if transform channels that don't match any of the naming convenstions are found.
  * Ignore `ignore` - Ignore (give no warning) if channels that don't match the naming convention are found.
  * Delete `delete` - Delete all channels that don't match any of the naming conventions.

- Custom Output Orders `custoutputorders` - By default the output transforms will use the orders given on teh Transform page. Enabling this allows for custom orders to be used for the transform that is output. This doesn't change the transform itself, but the values of the channels will likely change since they are combined in a different order to obtain the same overall transform.
- Transform Order `outxord` - ⊞ - See description from earlier Transform Order parameter.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `outrord` - ⊞ - See description from earlier Rotate Order parameter.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Include Order Channels `includeorderchans` - Specified if the 'xord' and 'rord' channels should be output from this node. 'xord' will be output for 'Transform (Euler)' and 'Transform (Quaternion)' modes. 'rord' will be output for the 'Transform (Euler)' mode. The matrix and position modes do not include orders.
- Continuous Rotations `continuousrotations` - In the case the input has multiple samples, this will attempt to keep rotations of neighbouring samples continuous. Basically, it tries to avoid 360 degree jumps. 360-> 361 instead of 360 -> 1 (which is the same two rotations.
- Use Rotation Hint `usehint` - An initial rotation hint given in r[xyz] degrees to try to stay continuous against. Turning this on and using the Hint parameter below allows you to specify approximate starting values for the rotation channels produced. This allows you to change the rotation channel solution to a specific starting point (e.g. for camera output control).
- Hint `hint` - ⊞ - Specify approximate starting values for the rotation channels produced.
  * Hint `hintx` -
  * Hint `hinty` -
  * Hint `hintz` -

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
  * Input 0:  - One or more transform sets, as defined by the allowable formats described at the start of the article.

  * Input 1:  - One or more transform sets, as defined by the allowable formats described at the start of the article.

## Info CHOP Channels
Extra Information for the Transform CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
