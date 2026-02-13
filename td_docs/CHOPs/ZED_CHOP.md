---
url: https://docs.derivative.ca/ZED_CHOP
category: CHOPs
title: ZED_CHOP
---

# ZED CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The ZED CHOP reads positional and plane tracking from the ZED camera. It can additionally use a UV to find plane in the room, and return information about that plane such as it's size/orientation either relative to the camera, or the room itself.
When the Camera Transform parameter is enabled, we provide the plane orientation data as well as the following.
---
**Channel Name** |  **Description**
`camera:tx`, `camera:ty`, `camera:tz` | Camera translation vector
`camera:rx`, `camera:ry`, `camera:rz` | Camera rotation vector
When Body Tracking is enabled, the Body 3D parameter enables `tx tz tz` positions values for each joint (i.e. `p1/body/shoulder_l:tx` is the position x component of the left shoulder for the first tracked body), the Body 2D parameter enables `u v` coordinates. The following are the supported body landmarks for 18, 34, and 38 joints listed in the [ZED Body Tracking](https://www.stereolabs.com/docs/body-tracking) documentation.
The ZED CHOP supports multiple body tracking with the Max Bodies parameter. Each of the previous as well as following channel names can be prepended with `p#` indicating which body this pertains to, i.e. the `p3/body/neck:tx` channel indicates the neck position x component for the third tracked body.
---
**Number of Joints** |  **Channel Names**
18 |  `neck`, `nose`, `eye_[lr]`, `ear_[lr]`, `shoulder_[lr]`, `elbow_[lr]`, `wrist_[lr]`, `hip_[lr]`, `knee_[lr]`, `ankle_[lr]`
34 |  `pelvis`, `spine_lower`, `spine_upper`, `neck`, `head`, `nose`, `eye_[lr]`, `ear_[lr]`, `collar_[lr]`, `shoulder_[lr]`, `elbow_[lr]`, `wrist_[lr]`, `hand_[lr]`, `hand_tip_[lr]`, `hand_thumb_[lr]`, `hip_[lr]`, `knee_[lr]`, `ankle_[lr]`, `heel_[lr]`, `foot_[lr]`,
38 |  `pelvis`, `spine_lower`, `spine_middle`, `spine_upper`, `neck`, `nose`, `eye_[lr]`, `ear_[lr]`, `collar_[lr]`, `shoulder_[lr]`, `elbow_[lr]`, `wrist_[lr]`, `hand_pinky_[lr]`, `hand_middle_[lr]`, `hand_index_[lr]`, `hand_thumb_[lr]`, `hip_[lr]`, `knee_[lr]`, `ankle_[lr]`, `big_toe_[lr]`, `heel_[lr]`, `small_toe_[lr]`, `_[lr]`,
The following are channels containing information per tracked body.
---
**Channel Name** |  **Description**
`id` | Body ID
`tracked` | Whether a body is being actively tracked (0 or 1)
`moving` | Whether a body is moving (0 or 1)
`vel_x`, `vel_y`, `vel_z` | Velocity of tracked body
The Bounding Boxes parameter enables channels for bounding box positions.
When Body 2D is enabled `bbox2d:[xywh]` channels indicate the bottom left (x,y) coordinate with the width and height of the bounding box as well as `bbox2d:[uv], bbox2d:norm[wh]` provide it in UV coordinates.
When Body 3D is enabled both the bounding box `bbox3d` and head bounding box `headbbox3d` are provided.
**NOTE:** This CHOP works with the [Stereolabs ZED](https://www.stereolabs.com/zed/) hardware. For more information and to know what ZED SDK to install refer to the [ZED](https://docs.derivative.ca/ZED "ZED") article.
See also [ZED TOP](https://docs.derivative.ca/ZED_TOP "ZED TOP"), [ZED POP](https://docs.derivative.ca/ZED_POP "ZED POP") and [ZED SOP](https://docs.derivative.ca/ZED_SOP "ZED SOP").
[zedCHOP_Class](https://docs.derivative.ca/ZedCHOP_Class "ZedCHOP Class")

## Parameters - ZED Page
- Active `active` - When 'On' data is captured from the ZED camera.
- ZED TOP `zedtop` - The name of the primary [ZED TOP](https://docs.derivative.ca/ZED_TOP "ZED TOP") that is configuring the camera. The primary TOP controls which camera the CHOP receives data from.
- Camera Transform `cameratransform` - Enables transformation, which returns the position and rotation of the camera.
- Camera Transform `resetcameratransform` - Zeros out the current camera position, effectively makes the current position the new origin.
- Plane Orientation `planeorientation` - Enables plane at point, which returns the position of the plane corresponding the UV coordinate.
- Get Plane `getplane` - Returns the camera position relative to the initial position of the camera. A `tx`, `ty`, `tz` triplet of channels will be output for the position of the camera in meters. An `rx`, `ry`, `rz` triplet will be output for the orientation.
- Pulse `getplanepulse` - Instantly returns the camera position relative to the initial position of the camera.
- Plane Reference Frame `planereferenceframe` - ⊞ - Controls if the panel coordinates will be given relative to the camera or the world.
  * World `world` - Plane position outputs are relative to the initial position of the camera.
  * Camera `camera` - Plane position outputs are relative to the previous position of the camera.

- Plane Point U `planepointu` - Sets the U coordinate of the point in the image to extract plane position.
- Plane Point V `planepointv` - Sets the V coordinate of the point in the image to extract plane position.
- Plane Position `planeposition` - Returns `tx`, `ty`, and `tz` position channels of the center of the plane.
- Plane Rotation `planerotation` - Returns `rx`, `ry`, and `rz` rotation channels for the plane.
- Plane Normal `planenormal` - Returns `nx`, `ny`, and `nz` normal channels of the plane.
- Plane Size `planesize` - Returns size of the bounding rectangle of the plane.
- Body Tracking `bodytracking` - ⊞ - Body tracking allows for tracking human skeletons that are found in the video frame. Each mode uses an AI model that will need to be trained one for your GPU. This will take several minutes, but only needs to be done once per model per machine, as long as the GPU isn't changed. For models where the 'Joint Mode' parameter is disabled, the outputs will be 'Absolute'.
  * Off `off` - Body Tracking is disabled.
  * Skeleton - 18 Joints `skeleton18` - Tracks an 18 joint skeleton as described in [this article](https://www.stereolabs.com/docs/body-tracking/).
  * Skeleton - 34 Joints `skeleton34` - Tracks an 34 joint skeleton as described in [this article](https://www.stereolabs.com/docs/body-tracking/). The positions and rotations are relative to the parent joints, as described in that article, where the 0 joint is the 'root' joint.

- Max Bodies `maxbodies` - The maximum number of bodies that will be tracked.
- Body 3D `body3d` - Enable to output 3D positions. Rotations will be included if the Joint Mode is set to 'Relative'.
- Joint Mode `jointmode` - ⊞ - Controls if the joint values are given in absolute in scene or relative to each other.
  * Absolute Position `absolute` - Absolute XYZ positions of each in space, given in meters.
  * Relative, with Orientation `relative` - 3D skeleton positions and rotations in heriachical terms, each relative to a parent joint.

- Body 2D `body2d` - 2D normalized UV coordinates for each joint, giving their position within the image.
- Aspect Correct UVs `aspectcorrectuv` - Corrects the UV coordinate using the aspect ratio. For a 2x1 aspect ratio, a normalized coordinate of (0.25, 0.25) will cover a quarter of the width and an eighth of the height, not a quarter of the height. This mode is useful when performing orthographic rendering or using the Fraction Aspect unit within TOPs.
- Bounding Boxes `boundingboxes` - Enable bounding boxes. Head bounding box is only enabled when Body 3D is enabled.

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

## Info CHOP Channels
Extra Information for the ZED CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
