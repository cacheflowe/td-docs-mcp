---
url: https://docs.derivative.ca/FreeD_In_CHOP
category: CHOPs
title: FreeD_In_CHOP
---

# FreeD In CHOP
## Summary

The FreeD CHOP reads incoming camera tracking data sent over a network using the FreeD protocol and outputs CHOP channels that can be used to control a virtual 3D camera. FreeD is not exclusive to any particular tracking system, but is frequenty used as an interchange protocol since it is supported by a wide range of hardware and software. However, as an older standard, it is lower precision and does not contain len distortion data like [Stype](https://docs.derivative.ca/Stype_In_CHOP "Stype In CHOP") or [Ncam](https://docs.derivative.ca/Ncam_CHOP "Ncam CHOP"), so it is recommended to use the hardware specific protocol when possible. Examples of hardware and software that support FreeD are [Viz Virtual Studio](https://www.vizrt.com/products/viz-virtual-studio) and [Panasonic PTZ cameras.](https://na.panasonic.com/us/ar-vr-virtual-set-production-with-panasonic-robotic-ptz-camera)
The channels exported by the FreeD CHOP are:       _camera_id_ - a number from 0 - 255 that can be used to store an id number for the camera      _tx, ty, tz_ - camera position, can be connected to the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") Translate parameters      _rx, ry, rz_ - camera rotation, can be connected to the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") Rotate parameters      _focus_ - a 24-bit positive integer (0-16 million) in arbitrary units that relates to the focus ring on a camera lens. Applications can interpret this value according to the hardware in use.      _zoom_ - a 24-bit positive integer (0-16 million) in arbitrary units that relates to the zoom ring on a camera lens. Applications can interpret this value according to the hardware in use.      _user_ - a 16-bit positive integer (0 - 65k) that can be used by the camera system to send custom user-defined data
**Note:** The FreeD CHOP only processes the 'D1' camera position and orientation message that is part of the FreeD protocol. All other message types will be ignored.
If the incoming network stream contains data for more than one camera, the Camera ID parameter can be used to select data from only one camera. If the Camera ID parameter is blank, then whatever data is received most recently will be shown - this could result in the data switching between cameras.
For more information or to diagnose connection problems, an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") can be connected to see if any packets have been dropped, skipped, or filtered out.
[freedCHOP_Class](https://docs.derivative.ca/FreedCHOP_Class "FreedCHOP Class")

## Parameters - FreeD Page
- Active `active` - While On, the CHOP receives FreeD information sent to the network port. While Off, no updating occurs.
- Protocol `protocol` - ⊞ - The network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `netaddress` - When using Multicast, this is the address that FreeD will listen for packets on.
- Network Port `port` - The port which FreeD will accept packets on.
- Local Address `localaddress` - ⊞ - Specify an IP address to receive on, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use.
  * 192.168.1.10 `192.168.1.10` -
  * 127.0.0.1 `127.0.0.1` -

- Camera ID `cameraid` - This parameter can be used to select a specific camera when there are multiple streams of incoming data. To select the camera, the parameter value should match the incoming value in the camera_id channel. If the parameter is blank, no filter will be applied and the channels will display whatever camera data was received last.

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
Extra Information for the FreeD CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific FreeD CHOP Info Channels
  * valid_packets -

  * unrecognized_packets -

  * corrupt_packets -

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
