---
url: https://docs.derivative.ca/OpenVR_CHOP
category: CHOPs
title: OpenVR_CHOP
---

# OpenVR CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The OpenVR CHOP receives positional data, frame rendering info, and action data from the [OpenVR](https://docs.derivative.ca/OpenVR "OpenVR") SDK. Each CHOP can output in one of 5 modes: Sensors, Projection Matrices, Trackers, Frame Timings, Actions and Skeletons.
### Actions
Actions are described in more details in [OpenVR Actions](https://docs.derivative.ca/OpenVR_Actions "OpenVR Actions").
### Getting Sensor Data at Higher Rates
By default when running a VR system the file will be throttled to the speed of the VR devices refresh rate by the OpenVR SDK. This helps ensure the low latency output required for a good VR experience. If only controllers/Vive trackers are being used for tracking in a non-VR situation, the file can run and sample those devices at a higher sample rate as long as no [OpenVR TOP](https://docs.derivative.ca/OpenVR_TOP "OpenVR TOP") in the project. If an [OpenVR TOP](https://docs.derivative.ca/OpenVR_TOP "OpenVR TOP") is present anywhere in the project, then playback will be throttled to the VR devices refresh rate.
See also [OpenVR](https://docs.derivative.ca/OpenVR "OpenVR"), [OpenVR TOP](https://docs.derivative.ca/OpenVR_TOP "OpenVR TOP"), [OpenVR SOP](https://docs.derivative.ca/OpenVR_SOP "OpenVR SOP"), [Audio Render CHOP](https://docs.derivative.ca/Audio_Render_CHOP "Audio Render CHOP")
[openvrCHOP_Class](https://docs.derivative.ca/OpenvrCHOP_Class "OpenvrCHOP Class")

## Parameters - Setup Page
- Active `active` - Control if this node is querying data from the OpenVR driver.
- Output `output` - ⊞ - Controls what kind of category of data will be output from this node.
  * Sensor `sensor` - Output data such as sensor orientation and general information such as render resolution.
  * Projection Matrices `projmatrices` - Output the projection matrices for each eye.
  * Trackers `trackers` - Output tracker states/transforms. This can both include Vive Trackers as well as just the transforms of controllers.
  * Frame Timings `frametimings` - General information regarding frame rendering.
  * Actions `actions` - The action channels as defined by the [OpenVR Actions](https://docs.derivative.ca/OpenVR_Actions "OpenVR Actions") in used by the system.
  * Skeletons `skeletons` - Hand skeletal information, as descibed [here](https://github.com/ValveSoftware/openvr/wiki/Hand-Skeleton). Note that 'Finger Tip Bones' is not supported anymore in OpenVR.

- Max Trackers `maxtrackers` - The maximum number of trackers whose data should be output from this node.
- First Tracker `firsttracker` - The first tracker number to be output. For example if this is set to 2 and Max Trackers is 2, then data for trackers 2 and 3 will be output.
- Orientation `orientation` - When doing 'Sensor' output, controls if the orientation channels will be output. By default the units for orientation are 1 unit = 1 meter.
- General Info `generalinfo` - When doing 'Sensor' output, controls of general information channels will be output, such as render resolution and play area size.
- Near `near` - When outputting 'Projection Matrices', controls the near plane the projection matrix will be built with.
- Far `far` - When outputting 'Projection Matrices', controls the far plane the projection matrix will be built with.
- Unit Scale `unitscale` - OpenVR by default works in a scale where 1 unit = 1 meter. This parameter allows the scale to be changed incase a scene is imported with a different scale.
- Custom Actions `customactions` - Turn on to allow specifying a custom [OpenVR Actions](https://docs.derivative.ca/OpenVR_Actions "OpenVR Actions") manifest file.
- Action Manifest `actionmanifest` - A path to a [OpenVR Actions](https://docs.derivative.ca/OpenVR_Actions "OpenVR Actions") manifest file. By default this is using the same manifest OpenVR uses when Custom Actions is disabled.
- Use Legacy Names `uselegacynames` - Use legacy channel naming convention coming from the Action Manifest. This should stay off unless loading existing old files.
- Skeleton Range `skeletonrange` - ⊞ - Controls the range of motion of the skeleton values.
  * With Controller `withcontroller` - Output skeleton taking into account the shape of the controller. The skeleton will look like it's holding the controller.
  * Without Controller `withoutcontroller` - Output the skeleton as if the controller dose not exist. This allows the skeleton to create a fully closed fist.

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
Extra Information for the OpenVR CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
