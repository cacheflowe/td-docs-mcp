---
url: https://docs.derivative.ca/OptiTrack_In_CHOP
category: CHOPs
title: OptiTrack_In_CHOP
---

# OptiTrack In CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The OptiTrack In CHOP is used to receive tracking data over the network data from [OptiTrack](http://www.optitrack.com) sytems. Currently the only data that is received is Rigid Body data. This node was previously called the NatNet In CHOP.
[optitrackinCHOP_Class](https://docs.derivative.ca/OptitrackinCHOP_Class "OptitrackinCHOP Class")

## Parameters - OptiTrack In Page
- Active `active` - While on, the CHOP receives information, while off no updating occurs.
- Connection Type `connectiontype` - ⊞ - Set this to the connection mode the server is set to.
  * Multicast `mutlicast` -
  * Unicast `unicast` -

- Network Address `netaddress` - The computer name or IP address of the server computer. You can use an IP address (e.g. `100.123.45.78`) or the computer's network name can be used directly. If you put "`localhost`", it means the other end of the pipe is on the same computer. When using Multicast mode this should still be set to the server's address, not the multicast address. The server will negotiate the multicast address with the client and make it connect to it automatically.
- Local Address `localaddress` - In cases where your computer has multiple network cards and IP address, this tells the node which local IP address to bind to for it's communication. For example say you have a WIFI connection whose IP address is 192.168.0.100 and a ethernet connection whose IP address is 24.100.200.50. If you want the node to communicate over the WIFI you can put 192.168.0.100 or 192.168.0.* into this parameter. If you want the node to communicate via the ethernet you'd set this to 24.100.200.50 or 24.100.200.* (or even 24.100.*.* etc.). Systems with a single network connection can leave this parameter blank.
- Command Port `commandport` - The command network port of the server.
- Data Port `dataport` - The data port of the server.
- Rate `rate` - The rate at which the data should be queried.
- Reset `resetpulse` - Reset the data in this node.

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
Extra Information for the OptiTrack In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific OptiTrack In CHOP Info Channels
  * connected -

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
