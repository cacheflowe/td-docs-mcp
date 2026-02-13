---
url: https://docs.derivative.ca/BlackTrax_CHOP
category: CHOPs
title: BlackTrax_CHOP
---

# BlackTrax CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The BlackTrax CHOP will provide motion tracking data from [BlackTrax Motion Tracking Systems](http://blacktrax.cast-soft.com) is a vision-based real-time tracking system developed by [CAST Software](http://cast-soft.com/) that specializes in large-scale performances. BlackTrax Beacons ("BTBeacons") are attached to performers or rigid objects, and the BlackTrax system accurately tracks the Beacon's position, rotation, velocity, and acceleration.
The BlackTrax CHOP will accept tracking data from [BlackTrax Motion Tracking Systems](http://blacktrax.cast-soft.com/). See [BlackTrax](https://docs.derivative.ca/BlackTrax "BlackTrax").
The BlackTrax CHOP works in conjunction with the BlackTrax system. BlackTrax tracks up to 85 BlackTrax Beacons and sends data regarding their position, rotation, velocity, and acceleration to TouchDesigner inside [RTTrPM Packets](https://rttrp.github.io/RTTrP-Wiki/RTTrPM.html). Each Beacon can have up to 3 LEDs attached, which can also be independently tracked in TouchDesigner. Each Beacon will have an ID that is specified in BlackTrax software and that Beacon ID must be mapped correctly to CHOP channels in TouchDesigner using the Mapping Table. Alternatively if the IDs are incremental then the "From Max Beacons" option in "Output Format" can be used.
### Server Settings
The server software should be set to send data in the WYSIWYG coordinate system (which should be the default). Rotations should be sent in Euler angles, not Quaternions. TouchDesigner should support both endian settings, but it's best to leave those as their default values.
See also [BlackTrax](https://docs.derivative.ca/BlackTrax "BlackTrax"), [PosiStageNet CHOP](https://docs.derivative.ca/PosiStageNet_CHOP "PosiStageNet CHOP")
[blacktraxCHOP_Class](https://docs.derivative.ca/BlacktraxCHOP_Class "BlacktraxCHOP Class")

## Parameters - BlackTrax Page
- Active `active` - While on, the CHOP receives information sent to the network port. While Off, no updating occurs.
- Port `port` - The port that will accept packets.
- Protocol `protocol` - ⊞ - The network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `netaddress` - When using Multicast, this is the address that will listen for packets.
- Sample Rate `samplerate` - Sets the sample rate of this CHOP.
- Output Format `outputformat` - ⊞ - Specifies the format for the CHOP channels (ie. how many beacons to add). "From Mapping Table" adds one beacon to the CHOP for every row in the mapping table. "From Max Beacons" adds the number specified in the "Max Beacons" parameter.
  * From Mapping Table `fromtable` -
  * From Max Beacons `frombeacons` -

- Max Beacons `maxbeacons` - Specifies how many beacons to add to the CHOP. Used with the "From Max Beacons" output format.
- Centroid `centroid` - When enabled, adds beacon translation and rotation channels.
- Velocity `velocity` - When enabled, adds beacon velocity channels.
- Acceleration `acceleration` - When enabled, adds beacon acceleration channels.
- LEDs `leds` - When enabled, adds position channels for each LED in the beacon.
- Reset Channels `reset` - Clears any stored beacons and removes any stale data while On.
- Reset Pulse `resetpulse` - Instantly clears any stored beacons and removes any stale data.
- Mapping Table `mappingtable` - A DAT table that maps beacon IDs to CHOP channels (beacon0, beacon1, etc.). The first row will map to beacon0, second row to beacon1, etc. Beacon ID is a unique non-negative integer and is specified within BlackTrax applications.
Below is an example of a mapping table that is tracking 3 beacons with IDs 10, 11, and 12. In this example 10 is mapped to beacon0, 11 is mapped to beacon1, and 12 is mapped to beacon2.
[![Beacon setup example.jpg](https://docs.derivative.ca/images/9/93/Beacon_setup_example.jpg)](https://docs.derivative.ca/File:Beacon_setup_example.jpg)

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
Extra Information for the BlackTrax CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
