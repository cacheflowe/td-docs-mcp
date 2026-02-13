---
url: https://docs.derivative.ca/Body_Track_CHOP
category: CHOPs
title: Body_Track_CHOP
---

# Body Track CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.
**Hardware:** This operator uses the [Augmented Reality (AR) SDK](https://docs.nvidia.com/deeplearning/maxine/ar-sdk-programming-guide/index.html) of the Nvidia Maxine system and requires a 20, 30, 40 or 50 series Nvidia RTX GPU.
**The models for this operator are not included with TouchDesigner. To use this operator you will need to download the 0.8.7 version AR SDK for your GPU from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.

**The Body Track CHOP can track bounding boxes and 34 key points of one or more human bodies, with optional joint angles, in 2D or 3D.
The input image is taken from a provided TOP and can be of any resolution or format, and either a still image or video.
The coordinates of the detected features are given in u, v positions relative to the bottom-left corner of the input image. By default, the values range from 0 to 1, but the 'Aspect Correct' parameter can be enabled to scale the values so that they can be used as 3D coordinates while maintaining the aspect ratio of the original image.
[bodytrackCHOP_Class](https://docs.derivative.ca/BodytrackCHOP_Class "BodytrackCHOP Class")

## Parameters - BodyTrack Page
- Active `active` - Enables the body tracking features.
- Model Folder `modelfolder` - The location of the AI model files used for body detection. By default these files are located in the Config/Models folder.
- TOP `top` - A path to the TOP operator that provides the image to perform body tracking on.
- High Performance `highperformance` - Enable high performance while sacrificing quality. This is only available when Keypoints are on.
- Bounding Boxes `bbox` - Output channels that describe a bounding box around the detected body. The channels give the u and v positions of the center of the body as well as the width and height of the box. The positions are relative to the bottom-left corner of the input image.
- Bounding Box Confidence `bboxconfidence` - Outputs a channel that describes the level of certainty that the AI model has detected a body in the input image. Higher numbers indicate greater confidence.
- Keypoints `keypoints` - Outputs either the UV or XYZ positions of the body's keypoints, depending on whether Body 3D is enabled.
- Keypoints Confidence `keypointsconfidence` - Outputs a channel that describes the level of certainty that the AI model has detected for each keypoint on a body. Higher numbers indicate greater confidence.
- Rotations `rotations` - Output rx, ry, and rz values for each keypoint on the body. (0,0,0) indicates that the body is oriented directly towards the camera. Values can range from +/- 180 degrees.
- Body 3D `body3d` - If keypoints are enabled, output XYZ positions instead of UV positions for each keypoint.
- Field of View (Horz) `fov` - If Body 3D is enabled, fov is the Field of View of the camera which produced the image given to the Body Track.
- Aspect Correct UVs `aspectcorrectuv` - Rescales the u and v positions so that they have the correct aspect ratio of the input image. This is useful when using the u, v positions as 3D coordinates rather than as image positions.
- Mirror U Positions `flipskelu` - Flips the u-coordinate of the UVs so that 1.0 becomes 0. and 0. becomes 1.
- People Tracking `peopletracking` - Track multiple people within the input image. Each person will have a persistent ID which is accessible with the Bounding Boxes toggle.
- Max Bodies `maxbodies` - The maximum number of people for the Maxine SDK to track. After the new maximum target tracked limit is met, any new targets will be discarded. This parameter does not affect the number of output channels from the CHOP. There is no maximum to this parameter; however, the current version of the SDK can only track a maximum of 8 people at a time.
- Shadow Tracking Age `shadowtrackingage` - Once a previously tracked body is no longer detected, an internal integer will be reset and incremented by one for each frame. The shadow tracking age is the threshold of this integer after which the body is discarded and no longer tracked. This property is measured in the number of frames, and the default is 90.
- Probation Age `probationage` - This option is the length of the tracker's probationary period. After a body reaches this age, it is considered to be valid and is appointed an ID. This will help with false positives, where false bodies are detected only for a few frames. This is measured by the number of frames, and the default is 10.

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
Extra Information for the CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
