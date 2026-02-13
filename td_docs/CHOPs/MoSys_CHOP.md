---
url: https://docs.derivative.ca/MoSys_CHOP
category: CHOPs
title: MoSys_CHOP
---

# MoSys CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The MoSys CHOP receives data from a [MoSys](https://docs.derivative.ca/MoSys "MoSys") camera tracking system. The channels can be used to control a virtual [camera](https://docs.derivative.ca/Camera_COMP "Camera COMP") and to implement lens distortion via the [MoSys TOP](https://docs.derivative.ca/MoSys_TOP "MoSys TOP") as part of a virtual production system.
[mosysCHOP_Class](https://docs.derivative.ca/MosysCHOP_Class "MosysCHOP Class")

## Parameters - MoSys Page
- Active `active` - While on, the CHOP receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost.
- Protocol `protocol` - ⊞ - The network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `netaddress` - When using Multicast, this is the address that to listen for packets on.
- Network Port `port` - The port which MoSys CHOP will accept packets on.
- Local Address `localaddress` - Specify an IP address to receive on, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use.
- Camera ID `cameraid` - Used to filter out unwanted data packets when more than one camera is sending data to this machine. This parameter should be a number that matches the value in the camera id channel. Data received from cameras that do not match this id will be ignored. If this field is blank, the most recent data received each frame will be displayed regardless of what camera it comes from.
- Screen Width `screenwidth` - The width of the camera image in pixels. It is used to convert the focal distance received by the camera into a FOV value.

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
Extra Information for the can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP"). _[Info Channels Common Page](https://docs.derivative.ca/index.php?title=Info_Channels_Common_Page&action=edit&redlink=1 "Info Channels Common Page \(page does not exist\)")_
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
