---
url: https://docs.derivative.ca/OAK_Select_CHOP
category: CHOPs
title: OAK_Select_CHOP
---

# OAK Select CHOP
## Summary

The OAK Select CHOP is like a [Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP") combined with a [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP"), and any of the other hardware-specific CHOPs. The basic operation involves providing an [OAK Device CHOP](https://docs.derivative.ca/OAK_Device_CHOP "OAK Device CHOP") and a stream name. In the simplest case, the stream's data will show up as well-named channels. For example, [ImgDetections](https://docs.luxonis.com/projects/api/en/latest/components/messages/img_detections/) messages indicating the 2D coordinates and labels of detected objects will show up as CHOP channels without any manual coding. In more complex cases such as hand landmark tracking, the stream may be of [NNData](https://docs.luxonis.com/projects/api/en/latest/components/messages/nn_data/) or [Buffer](https://docs.luxonis.com/projects/api/en/latest/components/messages/buffer/) type, requiring the user to implement a callback and parse the data.
[oakselectCHOP_Class](https://docs.derivative.ca/OakselectCHOP_Class "OakselectCHOP Class")

## Parameters - OAK Page
- Active `active` - Toggle whether the OAK Select CHOP cooks.
- OAK Device CHOP `chop` - An OAK Device CHOP running a depthai pipeline.
- Stream `stream` - The name of the stream to be received.
- Queue Size `queuesize` - For memory efficiency, this parameter controls the number of messages TouchDesigner reuses when receiving messages from OAK. See "Queue Size" below.
- Max Items `maxitems` - This parameter helps the OAK Select CHOP output a consistent number of channels. When running an image detection pipeline, the number of detected items will vary from frame to frame, but we want TouchDesigner to output a consistent number of channels.
- Output Format `outputformat` - ⊞ - The default option "Items As Separate Channels" enables time-slicing while "Items as Separate Samples" does not. If the stream is one which automatically fills in the CHOP, then "Items as Separate Samples" is a useful way to make the CHOP output **Max Items** samples consistently.
  * Items As Separate Channels `itemsaschannels` -
  * Items As Separate Samples `itemsassamples` -

- Use First Sample Only `firstsample` - Only use the most recently received message with the OAK Select CHOP. For example, for an IMU stream which is sending very high-frame rate data, toggling this parameter will only show the latest sample.
- Sample Rate `rate` - The sample rate of the CHOP. The default sample rate is `me.time.rate`.
- Callbacks DAT `callbacks` - Specifies the DAT which holds the callbacks.
- Setup Parameters `setuppars` - Clicking the button runs the setupParameters() callback function.

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
## Info CHOP Channels
Extra Information for the oakselect CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
