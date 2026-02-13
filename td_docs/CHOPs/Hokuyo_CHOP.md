---
url: https://docs.derivative.ca/Hokuyo_CHOP
category: CHOPs
title: Hokuyo_CHOP
---

# Hokuyo CHOP

## Summary

The Hokuyo CHOP is used for communication with Hokuyo laser scanners (serial or ethernet interface): [Hokuyo Products](http://www.hokuyo-aut.jp/search/)
The Hokuyo CHOP will work with all serial or ethernet Hokuyo laser scanners, though the only laser scanners tested in-house are the URG-04LX-UG01 (Serial), UST-10LX (Ethernet) and the UST-20LX (Ethernet).
It can be used with the [Blob Track CHOP](https://docs.derivative.ca/Blob_Track_CHOP "Blob Track CHOP") to detect objects in its field. See the Snippet for Blob Track.
All of a computer's available serial ports can be found in the Device Manager under the Windows operating system. Their names begin with 'COM'. Example: COM1, COM2, COM3, etc.
The Hokuyo CHOP outputs the measurement data from the laser scan in meters, either in Polar or Cartesian Coordinates. The laser scan is done counter clockwise over N degrees (defined by the device, eg. URG-04LX-UG01 is 240 degrees, UST-10LX is 270 degrees) and returns the distance to the first object hit by the laser at that point.
The Hokuyo laser scanners have an angular resolution that specifies the number of data points returned from a full scan. For the URG-04LX-UG01 there is a data point every ~0.3515 degrees, so over a 240 degree scan there is a total of 682 data points. For the UST-10LX there is a data point every 0.25 degrees, so over a 270 degree scan there is a total of 1080 data points. The Hokuyo laser scanners also have a start and end step that define a total detection range.
The UST-20LX and UST-10LX have the same measurement parameters as the UTM-30LX in the chart below. The UST-20LX ethernet model will also work like the UST-10LX.
For a visualization of the scan and a table of device specific numbers, see the image below:
[![Scan info.jpg](https://docs.derivative.ca/images/0/08/Scan_info.jpg)](https://docs.derivative.ca/File:Scan_info.jpg)
If the Hokuyo device is an ethernet model like the UTM-30LX-EW, make sure Window Firewall is not blocking it. Each install of TD will need to be allowed through the firewall separately. This commonly catches people out with networking OPs, as sometimes the Windows “allow TD to network” dialog doesn’t open on first connection attempt. A quick disabling of the firewall will let you test this theory.
See also [Serial DAT](https://docs.derivative.ca/Serial_DAT "Serial DAT"), [serialDAT_Class](https://docs.derivative.ca/SerialDAT_Class "SerialDAT Class"), [Arduino](https://docs.derivative.ca/Arduino "Arduino")
[hokuyoCHOP_Class](https://docs.derivative.ca/HokuyoCHOP_Class "HokuyoCHOP Class")

## Parameters - Connect Page
- Active `active` - This enables the connection to the Hokuyo sensor.
- Interface `interface` - ⊞ - Select the device interface.
  * Serial `serial` - Enables serial communication, and the Serial Port parameter.
  * Ethernet `ethernet` - Enables ethernet communication, and the Network Address parameter.

- Serial Port `port` - Selects the COM port that the serial connection will use. Default port names 1 through 8 are available in the popup menu, though any name can be manually entered in this field.
- Network Address `netaddress` - The network address of the laser scanner to connect to. The default address of a UST-10LX device is 192.168.0.10.
- High Sensitivity `highsensitivity` - This check box enables the high sensitivity mode on the sensor. High Sensitivity mode increases the detection ability of the laser scanner, but with a higher chance of measurement error. Only available on serial devices.
- Motor Speed `motorspeed` - Modifies the motor speed of the laser scanner. This should be used when running multiple laser scanners in the same environment. Different motor speeds across multiple laser scanners will avoid light interference between them. Only available on serial devices.
- Start Step `startstep` - Specifies the first data point of the laser scan. Start step must be a number between first and last measurement point, and must be less than or equal to the end step parameter. Refer to the above table to get device specific first/last measurement points. This parameter defaults to 0, the start step of the UST-10LX and other ethernet lasers. For the URG-04LX-UG01 and other similar devices the start step must be 44 or greater.
- End Step `endstep` - Specifies the last data point of the laser scan. End step must be a number between first and last measurement point, and must be greater than or equal to the start step parameter. Refer to the above table to get device specific first/last measurement points. This parameter defaults to 1080, the end step of the UST-10LX and other ethernet lasers. For the URG-04LX-UG01 and other similar devices the end step must be 725 or fewer.
- Output `output` - ⊞ - Outputs the scan data in either Polar or Cartesian coordinates.
  * Polar Coordinates `polarcoords` - Outputs the distance to the first object hit at each specific scan angle, in degrees.
  * Cartesian Coordinates `cartesiancoords` - Outputs x, y coordinates of each detected object from the counter clockwise scan, with the center of the device as the origin.

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
Extra Information for the Hokuyo CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Hokuyo CHOP Info Channels
  * incoming_data_packets -

  * data_packets_per_second -

  * dropped_data_packets -

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
