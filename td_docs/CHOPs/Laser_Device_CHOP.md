---
url: https://docs.derivative.ca/Laser_Device_CHOP
category: CHOPs
title: Laser_Device_CHOP
---

# Laser Device CHOP
## Summary

The Laser Device CHOP can send laser points to supported laser devices: EtherDream, Helios, and ShowNET. The devices can be connected to a laser using an ILDA cable, except in the case of ShowNET when an onboard DAC is used. Applications of the Laser Device CHOP include displaying computer-generated shape animations or other special effects of a light show.
See [Lasers](https://docs.derivative.ca/Lasers "Lasers") for an overview of lasers with TouchDesigner.
**Input/Output Channels:**
  * **x:** the point's X position, between -1 and 1.
  * **y:** the point's Y position, between -1 and 1.
  * **r:** the point's red color component, between 0 and 1.
  * **g:** the point's green color component, between 0 and 1.
  * **b:** the point's blue color component, between 0 and 1.
  * **i:** the point's color intensity, between 0 and 1.
  * **user1:** Optional user field 1.
  * **user2:** Optional user field 2.
  * **user3:** Optional user field 3. Not supported by EtherDream.
  * **user4:** Optional user field 4. Not supported by EtherDream.

Large changes in RGB values from sample-to-sample will likely be visibly correct as lasers generally can switch on-off quickly.
Blanking (all-off) occurs when the incoming RGB CHOP channels are all zero, or the Red Scale, Green Scale, and Blue Scale parameters are all zero.
An issue you may run into is IP discovery for the EtherDream for which you can use the [EtherDream DAT](https://docs.derivative.ca/EtherDream_DAT "EtherDream DAT").
Helios/ShowNET both have auto-populating menus for attached devices.
See also: [Laser CHOP](https://docs.derivative.ca/Laser_CHOP "Laser CHOP"), [EtherDream DAT](https://docs.derivative.ca/EtherDream_DAT "EtherDream DAT"), [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP")
[laserdeviceCHOP_Class](https://docs.derivative.ca/LaserdeviceCHOP_Class "LaserdeviceCHOP Class")

## Parameters - Laser Device Page
- Active `active` - When enabled, the CHOP will connect to the specified device and send points to it.
- Type `type` - ⊞ - Specify the type of laser device.
  * EtherDream `etherdream` - Send to an [EtherDream](https://ether-dream.com/) device. EtherDream devices are network-based and will require an IP/port to use.
  * Helios `helios` - Send to a Helios device. When selected the Device menu will auto-populate with any connected devices. Scan can be pulsed to re-scan for any newly connected devices.
  * ShowNET `shownet` - Send to a ShowNET device. When selected the Device menu will auto-populate with any ShowNET devices on the network. For ShowNET, the device menu will update automatically.

- Device `device` - Menu to select the named devices in the case of Helios and ShowNET.
- Scan `scan` - Scan for Helios devices. **Note:** there should not be any active Helios device connections when this scan is performed, otherwise they will be closed by the scanning process.
- Network Address `netaddress` - The network address of the EtherDream device to send the packets to. EtherDream IP can be found be polling devices on the network using the [EtherDream DAT](https://docs.derivative.ca/EtherDream_DAT "EtherDream DAT").
- Network Port `port` - The port to send the EtherDream packets to.
- Local Address `localaddress` - Specify an IP address to send from. This is useful when the system has multiple NICs (Network Interface Card) and you want to select which one to use.
- Queue Time `queuetime` - Determines the queue size of the Helios/EtherDream point buffer and the corresponding time required to drain it. It is often useful to reduce this value when sending fewer points.
- Queue Units `queueunits` - ⊞ - The units of queue time.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- X Scale `xscale` - Allows the input x values to be scaled by the specified factor.
- Y Scale `yscale` - Allows the input y values to be scaled by the specified factor.
- Red Scale `redscale` - Allows the input r values to be scaled by the specified factor.
- Green Scale `greenscale` - Allows the input g values to be scaled by the specified factor.
- Blue Scale `bluescale` - Allows the input b values to be scaled by the specified factor.
- Intensity Scale `intensityscale` - Allows the input intensity values (i) to be scaled by the specified factor.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Info CHOP Channels
Extra Information for the Laser Device CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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

## Operator Inputs
  * Input 0:  -
