---
url: https://docs.derivative.ca/OAK_Device_CHOP
category: CHOPs
title: OAK_Device_CHOP
---

# OAK Device CHOP
## Summary

The OAK Device CHOP serves as the main interface to an OAK camera. It also implements many of the features of the Timer CHOP such as timer counters, pulses, and custom Python callbacks.
###
Basic Usage
Before starting TouchDesigner, connect any OAK Devices to the computer via USB or Power over Ethernet (PoE). If you connect any devices while TouchDesigner is running, you should pulse the Refresh Device List parameter on the OAK Device CHOP. Next, customize the Python createPipeline callback and pulse the start parameter to start the camera. It's ok if you save a project while a camera is running. The camera will know to automatically start when the project opens next time.
###
Resolution and ISP Scale
The `depthai` python module has an enum for RGB resolution: [dai.ColorCameraProperties.SensorResolution](https://docs.luxonis.com/projects/api/en/latest/references/python/?highlight=dai.ColorCameraProperties.SensorResolution#depthai.ColorCameraProperties.SensorResolution). This enum currently includes THE_1080_P, THE_1200_P, THE_4_K, and many others. These options may not necessarily be compatible with your OAK hardware. The most commonly available RGB resolution is 1080p. You can save on bandwidth by selecting a lower resolution via the ISP scale. Selecting (2, 3) with THE_1080_P will result in a 1280x720 image.
###
Configs
The DepthaiTestSuite.toe project includes several base components which help control settings of an OAK camera by sending messages via an OAK Device CHOP. For example, the oakDeviceConfig base enables the user to set the XLinkChunkSize, logging level, and infrared laser settings of a device. The oakCameraControl base helps control RGB camera settings. The oakStereoDepthConfig base helps control stereo depth settings. It is possible to use these configs while the camera is running.
###
Optimizing Latency and FPS
Luxonis has a tutorial on [low latency](https://docs.luxonis.com/projects/api/en/latest/tutorials/low-latency/). In some cases such as streaming 4K video, you'll want to set [XLinkChunkSize](https://docs.luxonis.com/projects/api/en/latest/references/python/?highlight=xlinkchunksize#depthai.GlobalProperties.xlinkChunkSize:~:text=disables%20consistent%20timesyncing-,setXLinkChunkSize,-\(self%3A) to zero. This can be done with the oakDeviceConfig.
When creating `depthai` pipelines, it's possible to set FPS targets for various nodes such as the [ColorCamera](https://docs.luxonis.com/projects/api/en/latest/components/nodes/color_camera/) node. In general, the FPS cannot be changed after the pipeline has been loaded on the camera. You should pick high FPS values, but keep in mind that if you push these numbers too high, you may see the effective FPS as shown by an Info CHOP begin to fall.
See Also: [OAK-D](https://docs.derivative.ca/OAK-D "OAK-D"), [OAK Select CHOP](https://docs.derivative.ca/OAK_Select_CHOP "OAK Select CHOP"), [OAK Select TOP](https://docs.derivative.ca/OAK_Select_TOP "OAK Select TOP")
[oakdeviceCHOP_Class](https://docs.derivative.ca/OakdeviceCHOP_Class "OakdeviceCHOP Class")

## Parameters - OAK Page
- Active `active` -
- Sensor `sensor` - Select the available OAK Device from the dropdown.
- Refresh Sensor List `refreshpulse` - Refresh the list of available Sensors.
- Initialize `initialize` - Initialize is the signal to get the OAK Device into a ready state: The `onInitialize()` callback is run and on succesfully concluding will run the `createPipeline()` callback. It indicates that its ready by turning the `ready` channel on.
- Start `start` -
- Play `play` - The built-in Play parameter can toggle whether or not TouchDesigner processes the new messages it receives from the camera. For example, suppose multiple OAK Select CHOPs or TOPs are connected to the same OAK Device CHOP. By toggling play off, you will make all the OAK Select operators continue to receive whatever their most recently received message was, ignoring any new messages.
- Go to Done `gotodone` -
- Callbacks DAT `callbacks` - The path to the DAT containing callbacks for this OAK Device CHOP.

## Parameters - Stream In Page
The built-in page named Stream In helps with sending RGBA 8-bit images from TouchDesigner to an OAK camera. You can specify a TOP, a stream name, and a sending frequency in Hertz. If the stream name is blank, nothing will be sent. When sending images to the OAK, TouchDesigner will convert the input image to BGR format. This is convenient because most of the neural networks which can be run on the OAK camera expect the input images to be BGR format. If you require the image to be something else, you should use the [ImageManip](https://docs.luxonis.com/projects/api/en/latest/components/nodes/image_manip/) node in your `depthai` pipeline to change the format.
- Stream `stream` - Sequence of stream info parameters
- Name `stream0name` - Specify the name of the stream that can receive textures. The stream needs to be created in the depthai pipeline by creating a XLinkIn node: `pipeline.create(dai.node.XLinkIn)`
- Frequency (Hz) `stream0frequency` - Specify the frequency at which a texture is being send to the OAK device.
- TOP `stream0top` - Specify the TOP operator that contains the texture to be send to the stream.

## Parameters - Outputs Page
- Initializing `outinit` - Outputs channel `initializing` = 1 while the OAK Device is initalizing (i.e. while the callback `onInitialize()` returns non-zero).
- Initialize Fail `outinitfail` - Outputs channel `initialize_fail` = 1 if the OAK Device ran into an error while initializing or creating the pipeline.
- Ready `outready` - Outputs channel `ready` which is 1 after an Initialize and before a Start.
- Running `outrunning` - Outputs channel `running` which is 1 after a Start and before the Done.
- Done `outdone` - Outputs channel `done` = 1 when done or complete.
- Timer Count `outtimercount` - ⊞ -
  * Off `off` -
  * Seconds `seconds` -
  * Frames `frames` -
  * Samples `samples` -
  * All `all` -

- Running Time Count `outrunningcount` - ⊞ - Outputs the "wall-clock" time since Start occurred, no matter if the device's `Play` parameter was turned off or not. Will stop counting when the `Done` state has been reached.
  * Off `off` -
  * Seconds `seconds` -
  * Frames `frames` -
  * Samples `samples` -
  * All `all` -

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
Extra Information for the oakdevice CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
