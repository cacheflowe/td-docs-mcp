---
url: https://docs.derivative.ca/Oculus_Rift_CHOP
category: CHOPs
title: Oculus_Rift_CHOP
---

# Oculus Rift CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The Oculus Rift CHOP connects to an [Oculus Rift](https://docs.derivative.ca/Oculus_Rift "Oculus Rift") device and outputs several useful sets of channels that can be used to integrate the Oculus Rift into projects.
You can view the detected orientation of the device and put the rotation values directly into other operators. To help decrease latency, prediction can be used to guess what the orientation will be at some point in the future.
The raw sensor data is also available, with options for both sensor acceleration and angular velocity.
The devices calibration parameters are another option. These can be used to generate the projection matrices and distortion shaders, although both of these are already available (see below and [Oculus Rift TOP](https://docs.derivative.ca/Oculus_Rift_TOP "Oculus Rift TOP")). This data is constant, but may differ on future devices.
The last two things the Oculus Rift CHOP can output are the left and right eye projection matrices. These can be (and will need to be) passed into a camera's "Custom Projection" parameter in order to provide a proper 3D experience with the Oculus Rift. For convenience, the channels are aligned to be passed in directly by reference.
Without an Oculus Rift device connected the CHOP uses default values and will output channels corresponding to the Oculus Rift Developer Kit device. This allows you to design something for the Oculus Rift without actually having one.
See also [Oculus Rift](https://docs.derivative.ca/Oculus_Rift "Oculus Rift")
[oculusriftCHOP_Class](https://docs.derivative.ca/OculusriftCHOP_Class "OculusriftCHOP Class")

## Parameters - Setup Page
- Active `active` - When on, this CHOP will update it's data when it cooks.
- Output `output` - ⊞ - Switches between three different output modes.
  * HMD `hmd` - Can output orientation, acceleration, angular velocity and device info.
  * Left Controller `leftcontroller` - Output channels correspond to inputs from the Left Oculus Controller.
  * Right Controller `rightcontroller` - Output channels correspond to inputs from the Right Oculus Controller.
  * Left Projection Matrix `leftmatrix` - Output channels correspond to the projection matrix for the left eye.
  * Right Projection Matrix `rightmatrix` - Output channels correspond to the projection matrix for the right eye.

- Orientation `orientation` - When on, the output channels will include sensor orientation.
- Re-Center `recenter` - Resets the xyz positional components and the y orientation component of the tracking space for the HMD and controllers using the HMD's current tracking position.
- Acceleration `acceleration` - When on, the output channels will include acceleration.
- Velocity `velocity` - When on, the output channels will include velocity.
- Device Info `deviceinfo` - When on, the output channels will include device info.
- Controller Buttons `controllerbuttons` - When on, the output channels will include controller button states.
- Near `near` - Specifies the distance of the near clipping plane for the projection matrix.

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

- Export Table `exporttable` -

## Info CHOP Channels
Extra Information for the Oculus Rift CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
