---
url: https://docs.derivative.ca/Stype_In_CHOP
category: CHOPs
title: Stype_In_CHOP
---

# Stype In CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Stype CHOP reads camera tracking information sent from a [Stype](https://docs.derivative.ca/Stype "Stype") (**RedSpy**) device using the Stype HF protocol. The CHOP outputs channels that can be used to control a virtual camera and implement lens distortion via the [Stype TOP](https://docs.derivative.ca/Stype_TOP "Stype TOP").
The channels exported by the Stype CHOP are:       _connected_ - 1 or 0, indicating whether the CHOP has received valid Stype messages within the last 500ms      _recording_ - 1 or 0, indicating the recording status on the Stype Kit (see Stype protocol for more information)      _focus_distance_ - 1 or 0, indicating how the focus field is used (see Stype protocol for more information)      _hours, minutes, seconds, frames_ - timecode, may be zero if time information is not present      _tx, ty, tz_ - camera position, can be connected to the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") Translate parameters      _rx, ry, rz_ - camera rotation, can be connected to the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") Rotate parameters      _fov_ - camera field of view, can be connected to the [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") FOV Angle parameter      _padded_fov_ - field of view expanded by the padding parameter, can be used in [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") FOV Angle parameter      _aspect_ - aspect ratio of the camera      _focus_ - camera focus from 0 (closest) to 1 (infinite), can be used to simulate depth of field      _zoom_ - camera zoom from 0 (wide) to 1 (tele)      _centerx, centery_ - offset of the camera sensor in mm, used by the [Stype TOP](https://docs.derivative.ca/Stype_TOP "Stype TOP") for calculating lens correction      _k1, k2_ - radial lens distortion parameters, used by the [Stype TOP](https://docs.derivative.ca/Stype_TOP "Stype TOP") for calculating lens correction      _pawidth, paheight_ - size of the sensor in mm, used by the [Stype TOP](https://docs.derivative.ca/Stype_TOP "Stype TOP") for calculating lens correction
For more information or to diagnose connection problems, an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") can be connected to see if any packets have been dropped or skipped.
**NOTE:** This CHOP works with [Stype](https://www.stype.tv) hardware. For more information refer to the [Stype](https://docs.derivative.ca/Stype "Stype") article.
See also [Stype TOP](https://docs.derivative.ca/Stype_TOP "Stype TOP").
[stypeCHOP_Class](https://docs.derivative.ca/StypeCHOP_Class "StypeCHOP Class")

## Parameters - Stype Page
- Protocol `protocol` - ⊞ - The network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -
  * Reliable Messaging (UDT Library) `reliablemsging` -

- Network Address `netaddress` - When using Multicast, this is the address that Stype will listen for packets on.
- Network Port `port` - The port which the Stype CHOP will accept packets on. The default for the protocol is 6301, but this should be set to match the current hardware output settings.
- Local Address `localaddress` - When the sending machine is equipped with multiple network adapters, this parameter can be used to choose which adapter to send the data from by specifying its IP address here.
- Active `active` - While on, the CHOP receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost.
- Padding `padding` - A value from 0 to 1 indicating the percentage to increase the field of view in case the given lens distortion requires samples outside of the normal render area. It is used to calculate the padded field of view and can be used to calculate the resolution of the render node.

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
Extra Information for the Stype CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Stype CHOP Info Channels
  * valid_packets -

  * unrecognized_packets -

  * corrupt_packets -

  * missing_packets -

  * dropped_packets -

  * last_packet_num -

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
