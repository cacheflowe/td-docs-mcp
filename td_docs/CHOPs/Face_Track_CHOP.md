---
url: https://docs.derivative.ca/Face_Track_CHOP
category: CHOPs
title: Face_Track_CHOP
---

# Face Track CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.
**Hardware:** This operator uses the Augmented Reality (AR) SDK of the Nvidia Maxine system and requires a 20, 30, 40 or 50 series Nvidia RTX card to operate.
**The models for this operator are not included with TouchDesigner. To use this operator you will need to download the 0.8.7 version AR SDK for your GPU from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.

**The Face Track CHOP can detect faces and facial landmark points in an image, as well as the direction the face is looking relative to the camera. Using a compatible 3D Morphable Face Model (3DMM) and the [Face Track SOP](https://docs.derivative.ca/Face_Track_SOP "Face Track SOP"), it can also be used to fit and animate a 3D mesh to the detected face.
The input image is taken from a provided TOP and can be of any resolution or format, and either a still image or video. If multiple faces are present in an image, the CHOP will attempt to track the largest one detected.
The coordinates of the detected features are given in u, v positions relative to the bottom-left corner of the input image. By default, the values range from 0 to 1, but the 'Aspect Correct' parameter can be enabled to scale the values so that they can be used as 3D coordinates while maintaining the aspect ratio of the original image.
**Tip** : Look at the several examples of the Face Track CHOP/SOP in [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets").
To align a 3D rendering of the points with the original input image, set the 'Projection' of your [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") to 'Orthographic', the 'Ortho Origin' parameter to 'Bottom-Left', and the 'Ortho Width' to 1, while also enabling 'Aspect Correct' on the Face Track CHOP.
To use the mesh fitting features you will need a compatible face mesh file in the Nvidia '`nvf`' format. We recommend using the `face_model2.nvf` file that is now included in the `Config/Models` folder inside your TouchDesigner installation. **Note:** Mesh files generated for previous versions of TouchDesigner will no longer work.
See also: [Face Track SOP](https://docs.derivative.ca/Face_Track_SOP "Face Track SOP")
[facetrackCHOP_Class](https://docs.derivative.ca/FacetrackCHOP_Class "FacetrackCHOP Class")

## Parameters - FaceTrack Page
- Active `active` - Enables the face tracking features.
- Model Folder `modelfolder` - The location of the AI model files used for face detection. By default these files are located in the Config/Models folder.
- Mesh File `meshfile` - The 3D morphable mesh file in Nvidia 'nvf' format to use in mesh fitting. When available, the fitted mesh can be accessed with a [Face Track SOP](https://docs.derivative.ca/Face_Track_SOP "Face Track SOP").
- TOP `top` - A path to the TOP operator that will provides the image to perform face tracking on.
- Bounding Boxes `bbox` - Output channels that describe a bounding box around the detected face. The channels give the u and v positions of the center of the face as well as the width and height of the box. The positions are relative to the bottom-left corner of the input image.
- Bounding Box Confidence `bboxconfidence` - Outputs a channel that describes the level of certainty that the AI model has detected a face in the input image. Higher numbers indicate greater confidence.
- Rotations `rotations` - Output rx, ry, and rz values that indicate how the face is oriented in the image. (0,0,0) indicates that the face is oriented directly towards the camera. Values can range from +/- 180 degrees as the subject turns away from the camera.
- Number of Landmarks `landmarks` - ⊞ -
  * None `none` - The number of facial landmark points to output. Points are numbered beginning from 1 and always represent a fixed feature on the face such as the chin, eyebrow, nose, etc. Positions are given as u and v coordinates relative to the bottom-left corner of the input image.
  * 68 (Multi-PIE Mark-ups) `num68` - A standard set of facial landmark features used in AI research. [See Reference Diagram.](https://www.researchgate.net/figure/The-68-Multi-PIE-landmarks-scheme-and-the-landmarks-selected-for-our-method-marked-by-the_fig1_311741971)
  * 126 `num126` - An extended set of landmark features.

- Landmark Confidence `landmarkconfidence` - Adds a confidence value for each landmark feature. Higher values indicate the feature is more likely to be accurate.
- Mesh Transform `meshtransform` - Enable to output translate, rotate and scale channels for the fitted face mesh. This feature requires a valid 3D morphable face mesh file (see notes above). The values from these channels can be used to transform the mesh produced by an attached [Face Track SOP](https://docs.derivative.ca/Face_Track_SOP "Face Track SOP") so that it aligns with the input image. By default the fitted mesh is pre-transformed to align with the image, but if 'Pre-Transform' is disabled in the SOP, these values can be used instead for more control and speed.
- Aspect Correct UVs `aspectcorrectuv` - Rescales the the u and v positions so that they have the correct aspect ratio of the input image. This is useful when using the u, v positions as 3D coordinates rather than as image positions.

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
Extra Information for the Face Track CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
