---
url: https://docs.derivative.ca/Touch_Out_CHOP
category: CHOPs
title: Touch_Out_CHOP
---

# Touch Out CHOP
## Summary

The Touch Out CHOP can be used to create high speed connection between two TouchDesigner processes. Data is sent over TCP/IP. The Touch Out CHOP (server) sends it's data to a [Touch In CHOP](https://docs.derivative.ca/Touch_In_CHOP "Touch In CHOP") (client). The Touch Out CHOP is similar to a [Pipe Out CHOP](https://docs.derivative.ca/Pipe_Out_CHOP "Pipe Out CHOP") but highly optimized for TouchDesigner-to-TouchDesigner communication. For interfacing with other software or devices, see the [Pipe Out CHOP](https://docs.derivative.ca/Pipe_Out_CHOP "Pipe Out CHOP").
To receive network data from another "server" computer (e.g. from a TouchDesigner Touch Out CHOP running remotely), a connection must be established between the server and the Touch In CHOP before data is sent. You must supply the Server Address and Port from which to receive incoming data to a channel. The server should be listening for connections on the port that this CHOP is using. Multiple Touch In CHOPs (clients) can receive data from a single Touch Out CHOP (server).
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[touchoutCHOP_Class](https://docs.derivative.ca/TouchoutCHOP_Class "TouchoutCHOP Class")

## Parameters - Touch Out Page
- Protocol `protocol` - ⊞ - Selects which network protocol to use to transfer data. Different protocol's have methods of connecting and using the address parameter. For more information refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article.
  * Streaming (TCP/IP) `streaming` -
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Address `address` - The address to use, not all protocls require an address to be specified on the sending side.
- Network Port `port` - The network port to use.
- Active `active` - When Off, data is not sent.
- Max Queue Size `maxsize` - Limits the number of events waiting to be sent. This prevents overflows if the connection is too slow.
- Max Queue Size Unit `maxsizeunit` - Choose between using Samples, Frames, or Seconds as the units for the Max Queue Size parameter.
- Cook Every Frame `cookalways` - Specifies that this CHOP should be cooked every frame regardless of CHOPs below it are cooking.
- Resend Names `resendnames` - Resends all the channel names. Generally you don't need to use this parameter, but it is provided just in-case.
- Use Synced Ports `syncports` - ⊞ - This parameter lets you send the the data in a single global pipe if required. This can be important if various data streams must be sent in frame sync. For more information, refer to [Touch In/Out Synced Ports](https://docs.derivative.ca/Touch_In/Out_Synced_Ports "Touch In/Out Synced Ports").
  * Off `off` - Uses separate ports for each port number assigned.
  * On `on` - Uses a single global pipe for all Touch Out CHOPs using this Transfer Port Type. The global pipe uses port 10500 internally to send all the global port type data together at once. The Network Port parameter is still used to determine which Touch In CHOP gets the data on the receiving side. Note that since a single port is used (10500), only one process on a machine can be serving Synced Port data.

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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Touch Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Touch Out CHOP Info Channels
  * connected -

  * num_clients -

  * queue_size -

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
