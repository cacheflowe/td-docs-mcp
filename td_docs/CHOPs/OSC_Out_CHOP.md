---
url: https://docs.derivative.ca/OSC_Out_CHOP
category: CHOPs
title: OSC_Out_CHOP
---

# OSC Out CHOP
## Summary

The OSC Out CHOP sends all input channels to a specified network address and port. Each channel name and associated data is transmitted together to the specified location. TouchDesigner time stamps all outgoing Open Sound Control messages with the time of the outgoing frame relative to the system time when the first message was sent. OSC CHOPs in TouchDesigner use the UDP transport protocol.
OSC Out will either send all the channels each cook or it will only send each channel depending on if it has changed at all since the last time it was sent. This is determined by the Send Events Every Cook flag.
OSC bundles allows you to send a group of messages in a single command rather than as separate, individual messages. The [OSC Out DAT](https://docs.derivative.ca/OSC_Out_DAT "OSC Out DAT") has a `sendOSC()` function that will accept a list of messages and send as a bundle.
See also [OSC In CHOP](https://docs.derivative.ca/OSC_In_CHOP "OSC In CHOP"), [OSC Out DAT](https://docs.derivative.ca/OSC_Out_DAT "OSC Out DAT"), [OSC In DAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT"), [iOS and OSC](https://docs.derivative.ca/IOS_and_OSC "IOS and OSC"), [Touch Out CHOP](https://docs.derivative.ca/Touch_Out_CHOP "Touch Out CHOP"), [UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT"), [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[oscoutCHOP_Class](https://docs.derivative.ca/OscoutCHOP_Class "OscoutCHOP Class")

## Parameters - OSC Out Page
- Active `active` - While On, the CHOP sends information to the network port. When Off, data is not sent.
- Protocol `protocol` - ⊞ - Selects the network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -
  * Reliable Messaging (UDT Library) `reliablemsging` -

- Network Address `netaddress` - The network address of the server computer. This address is a standard WWW address, such as 'foo' or 'foo.bar.com'. You can put an IP address (e.g. 100.123.45.78). If you put "localhost", it means the other end of the pipe is on the same computer.
- Network Port `port` - The port which OSC Out will send packets to.
- Local Address `localaddress` - Specify an IP address to send from, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use.
- Max Queue Size `maxsize` - Specifies the maximum number of messages OSC Out will try to send at a single time.
- Max Queue Size Unit `maxsizeunit` - Select the units to use for this parameter, Samples, Frames, or Seconds
- Cook Every Frame `cookalways` - Specifies that this CHOP should be cooked every frame regardless of CHOPs below it are cooking.
- Numeric Format `numericformat` - ⊞ - Choose the data format to send data between 32-bit integer, 32-bit float, or 64-bit double.
  * Int (32 bit) `int` -
  * Float (32 bit) `float` -
  * Double (64 bit) `double` -

- Data Format `format` - ⊞ - Specify how to format the outgoing messages.
  * Sample `sample` - Sends the current sample in each channel.
  * Time Slice `timeslice` - Sends all samples of the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") in each channel.
  * Transpose `transpose` - Sends the first sample in each channel transposed together into a single multi-sample channel.

- Max Message Bytes `maxbytes` - Limits the size of the outgoing message packets and splits up the message accordingly.
- Send Events Every Cook `sendevents` - When on, OSC Out will send all channels every cook regardless if the value has changed. When off, OSC Out only sends data which has changed.

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
Extra Information for the OSC Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
