---
url: https://docs.derivative.ca/Kinect_Azure_CHOP
category: CHOPs
title: Kinect_Azure_CHOP
---

# Kinect Azure CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows 10 April 2018 or newer** operating system.
**Hardware:** [Kinect Azure System Requirements](https://docs.microsoft.com/en-us/azure/kinect-dk/system-requirements)
The Kinect Azure CHOP can be used to obtain body tracking information, including joint positions and rotations, and IMU sensor data from a Microsoft Kinect Azure camera or a Kinect compatible [Orbbec](https://docs.derivative.ca/Orbbec "Orbbec") Camera (Femto Mega, Femto Bolt, etc).
This CHOP requires a [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP") to connect to the camera and to configure the camera's settings. Not all configuration settings support body tracking e.g. Passive IR depth mode. Body tracking can only be used by one hardware type at a time (Microsoft or Orbbec). If more than one hardware type tries to use body tracking in a project, only the first node to be cooked will be enabled.
Use the Max Players parameter to determine how many players you would like the camera to track. The TOP will automatically assign any bodies that are discovered by the device to the available player spaces. Due to the system used to detect player skeletons from the depth camera image, body tracking data can lag multiple frames behind the image data. To more closely synchronize body and image data, use the 'Sync Body Tracking To Image' option on the primary [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP") that is controlling the device (synchronization will increase lag in the image capture).
For a diagram of the joints tracked and their hierarchy, visit [Microsoft's Kinect Azure SDK](https://docs.microsoft.com/en-us/azure/kinect-dk/body-joints).
Acceleration and rotation data from the camera's IMU sensor can be obtained by enabling the 'IMU Channels' parameter.
See also [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP"), [Kinect Azure Select TOP](https://docs.derivative.ca/Kinect_Azure_Select_TOP "Kinect Azure Select TOP").
[kinectazureCHOP_Class](https://docs.derivative.ca/KinectazureCHOP_Class "KinectazureCHOP Class")

## Parameters - Kinect Azure Page
- Active `active` - Enable to disable the capturing of body tracking data. The primary [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP") must also be active to receive data.
- Kinect Azure TOP `top` - The name of the [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP") that is connected to the camera.
- Max Players `maxplayers` - The number of player skeletons that should be tracked by the device. If the camera does not find enough skeletons, then the extra channels will be set to zero.
- Relative Bone Rotations `relbonerotations` - Include rotation data for all bone in the skeleton. Rotation is measured in degrees around the XYZ axes relative to the bone's parent.
- Absolute Bone Rotations `absbonerotations` - Include absolute rotation data for all bone in the skeleton. Rotation is measured in degrees around the XYZ axes relative to the world.
- Bone Lengths `bonelengths` - Include channels for the length of each bone. A bone's length is the distance between a joint and its parent joint. See the [Kinect Azure SDK](https://docs.microsoft.com/en-us/azure/kinect-dk/system-requirements) for a diagram of the joint heirarchy.
- World Space Positions `worldspace` - Include channels for the bone's absolute world position in meters.
- Color Image Positions `colorspace` - Include channels for the skeleton positions in UV coordinates of the Color Image.
- Depth Image Positions `depthspace` - Include channels for the skeleton positions in UV coordinates of the Depth Image.
- Aspect Correct UVs `aspectcorrectuv` - Scale the image space positions to that they match the aspect ratio of the corresponding camera.
- Mirror Image V Positions `flipimagev` - Flip the v coordinate of the image space positions so that 0,0 would be in the top-left corner. This was the default behaviour prior to version 2020.44130.
- Mirror U Positions `flipskelu` - Mirror's the U coordintate of Color Image Positions and Depth Image Positions above which is useful when those images have been flipped in U (x axis flip like a mirror).
- Bone Confidence `confidence` - The confidence that the sensor has that a joint's position and rotation is correct. It can be one of the following values:
  * 0 - The joint is out of range (too far from the camera)
  * 1 - The joint cannot be seen by the sensor and is predicted based on the neighbouring joints
  * 2 - Medium confidence. The sensor is reasonably confident of the joint's position/rotation. This is currently the highest level of confidence the sensor will produce.
  * 3 - High confidence. Reserved for future use.

- IMU Channels `imuchans` - Include temperature, acceleration and rotation data from the camera's IMU sensor.

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
Extra Information for the Kinect Azure CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
