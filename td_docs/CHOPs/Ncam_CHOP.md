---
url: https://docs.derivative.ca/Ncam_CHOP
category: CHOPs
title: Ncam_CHOP
---

# Ncam CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Ncam CHOP receives camera tracking data from an external [Ncam Reality system](https://www.ncam-tech.com/) for use in virtual production. The data is received over a network using the TCP protocol and includes information on the camera's position, orientation and optical properties. This data can be used in a [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") to render content from a virtual environment that is synced to the movement of a physical camera. An [Ncam TOP](https://docs.derivative.ca/Ncam_TOP "Ncam TOP") can also be used to receive image data from the camera and to composite it with the rendered content.
For additional tracking solutions, see the [Stype CHOP](https://docs.derivative.ca/Stype_CHOP "Stype CHOP") and [FreeD CHOP](https://docs.derivative.ca/FreeD_CHOP "FreeD CHOP").
[ncamCHOP_Class](https://docs.derivative.ca/NcamCHOP_Class "NcamCHOP Class")

## Parameters - Network Page
- Active `active` - Turn off this parameter to stop receiving data from the Ncam system.
- Protocol `protocol` - ⊞ - A parameter for future options.
  * TCP `tcp` - The network protocol used to send data from the Ncam system to TouchDesigner. Only TCP is currently supported.

- Network Address `netaddress` - The network address of the Ncam server that is sending the data.
- Network Port `port` - The network port to connect to on the Ncam server.

## Parameters - Channels Page
These parameters control how the data from the Ncam server is presented in CHOP channels.
- Camera View `cameraview` - ⊞ - Select how the camera's orientation and position are outputted.
  * Translation & Rotation (TR) `trs` -
  * Matrix `matrix` -
  * TR & Matrix `both` -
  * Off `off` -

- Camera Projection `cameraproj` - ⊞ - Select how the camera's projection settings are outputted.
  * Field of View (FOV) `fov` -
  * Matrix `matrix` -
  * FOV & Matrix `both` -
  * Off `off` -

- Camera Properties `cameraprops` - ⊞ - Controls the output of additional camera properties like zoom and focus. These properties can either be normalized (0 to 1) or in their native physical units.
  * Normalized `normalized` -
  * Physical `physical` -
  * Both `both` -
  * Off `off` -

- Timecode `timecode` - ⊞ - Select whether the embedded timecode is presented as a single counter or in separate hour, minute, second and frame channels.
  * HH:MM::SS::FF `on` -
  * Timecode `timecode` -
  * Both `both` -
  * Off `off` -

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
Extra Information for the Ncam CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Ncam CHOP Info Channels
  * tracking_packets -

  * optical_packets -

  * distort_packets -

  * film_packets -

  * depth_packets -

  * packets_dropped -

  * incomplete_packets -

  * packets_skipped -

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
