---
url: https://docs.derivative.ca/Pipe_In_CHOP
category: CHOPs
title: Pipe_In_CHOP
---

# Pipe In CHOP
## Summary

The Pipe In CHOP allows users to input from custom devices into CHOPs. It is implemented as a TCP/IP network connection.
The connection can be from a user-written program that outputs to the Pipe In CHOP's port, or from another TouchDesigner process, where the data is coming from a [Pipe Out CHOP](https://docs.derivative.ca/Pipe_Out_CHOP "Pipe Out CHOP").
Regular channel data sent to Pipe In outputs has CHOP channels (channel names with floating point values every frame). Mixed with it can be TouchDesigner scripting commands that get executed when they arrive.
**TIP:** The [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT") or [UDP In DAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT") is the preferred way to send script commands and other data packets over the network.
This node differs from the [Touch In CHOP](https://docs.derivative.ca/Touch_In_CHOP "Touch In CHOP") as it functions using a stream of commands, instead of a simple stream of channel data like the [Touch In CHOP](https://docs.derivative.ca/Touch_In_CHOP "Touch In CHOP"). Information comes in in various commands which are documented in the files located in your installation directory `C:/Program Files/Derivative/TouchDesigner*/touch/docs/pipe`.
To receive network data from another "server" computer (e.g. from a TouchDesigner Pipe Out CHOP running remotely), a connection must be established between the server and the Pipe In CHOP before data is sent. You must supply the Server Address and Port from which to receive incoming data to a channel. The server should be listening for connections on the port that this CHOP is using.
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
See also [Shared Mem In CHOP](https://docs.derivative.ca/Shared_Mem_In_CHOP "Shared Mem In CHOP").
[pipeinCHOP_Class](https://docs.derivative.ca/PipeinCHOP_Class "PipeinCHOP Class")

## Parameters - PipeIn Page
- Connection Mode `mode` - ⊞ - Set operation as server or client.
  * This Operator is Client `client` -
  * This Operator is Server `server` -

- Server Address `address` - The network address of the server computer. This address is a standard WWW address, such as '`foo`' or '`foo.bar.com`'. You can use an IP address (e.g. `100.123.45.78`) or the computer's network name can be entered. If you put "`localhost`", it means the other end of the pipe is on the same computer.
- Server Port `port` - The network port of the server.
- Active `active` - While On, the CHOP receives information from the pipe or server. While Off, no updating occurs. Data sent by a server is lost, but a pipe will store the data until Active is turned on again. If in Network mode, turning this parameter on initiates a connection, and turning it off breaks the connection.
- Queued `queued` - When checked on, the network queuing is enabled. See the following parameters.
- Minimum Target `mintarget` - The lower end of the queue target range. The Pipe In CHOP will try to maintain a queue length greater than or equal to this value.
- Min Unit `mintargetunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Maximum Target `maxtarget` - The upper end of the queue target range. The Pipe In CHOP will try to maintain a queue length less than or equal to this value.
- Max Unit `maxtargetunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Maximum Queue `maxqueue` - The maximum size of the queue when full. Incoming samples will be dropped if the maximum queue is reached. **This also affects the maximum number of script commands that can be queued up before they start gettting dropped.**
- Max Queue Unit `maxqueueunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Queue Adjust Time `adjusttime` - Specifies how often to repeat/drop a samples in order to get closer to the queue target range. If the value = 1 and the units = seconds, then it will try to repeat/drop a sample once per second to maintain the queue target set in the Minimum Target and Maximum Target parameters above.
- Adjust Unit `adjusttimeunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Reset Channels `reset` - Discards and clears all channels and incoming data.
- Allow Incoming Scripts `allowscripts` - Incoming script commands will be ignored unless this parameter is turned On. Turning it Off is more secure.
- Echo Messages to Console `echo` - ⊞ - Print all incoming commands (not channel data) to the Console which can be opened from the Dialogs menu. A good way to test a connection is to put "`echo X`" commands in the incoming stream.
  * Off `off` -
  * Full Messages to Console `on` -
  * All Events to Console `raw` -

- Callbacks DAT `callbacks` - Path to a DAT containing callbacks for each event received. See [pipeinCHOP_Class](https://docs.derivative.ca/PipeinCHOP_Class "PipeinCHOP Class") for usage.

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
Extra Information for the Pipe In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Pipe In CHOP Info Channels
  * connected -

  * num_connected -

  * queue_size -

  * queue_retarded_total -

  * queue_advanced_total -

  * time_under_target -

  * time_over_target -

  * queue_bumped -

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
