---
url: https://docs.derivative.ca/Touch_In_CHOP
category: CHOPs
title: Touch_In_CHOP
---

# Touch In CHOP
## Summary

The Touch In CHOP can be used to create a high speed connection between two TouchDesigner processes via CHOPs.
Data is sent over TCP/IP. The Touch In CHOP (client) receives its data from a [Touch Out CHOP](https://docs.derivative.ca/Touch_Out_CHOP "Touch Out CHOP") (server). The Touch In CHOP is similar to a [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP") but highly optimized for TouchDesigner-to-TouchDesigner communication. For interfacing with other software or devices, see the [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP") or the [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT").
To receive network data from another "server" computer (e.g. from a Touch Out CHOP running remotely), a connection must be established between the server and the Touch In CHOP before data is sent.
The data is received as time slices, and can be used to eliminate frame dropping if the sender or receiver is not running at its target frame rate. See [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing") and the [Time Slice CHOP](https://docs.derivative.ca/Time_Slice_CHOP "Time Slice CHOP"). Can also be run non-time sliced to receive full channel data.
To analyze the timing of the messages coming in, attach an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") to the Touch In CHOP. It will show the internal queue size and whether it is dropping or missing data (`queue_advanced_total` and `queue_retarded_total` should not be increasing, and `queue_length` should not be zero).
**NOTE for Windows OS - If experiencing connection issues, confirm Windows Firewall is disabled for TouchDesigner.**
See also: [OSC In CHOP](https://docs.derivative.ca/OSC_In_CHOP "OSC In CHOP")
[touchinCHOP_Class](https://docs.derivative.ca/TouchinCHOP_Class "TouchinCHOP Class")

## Parameters - Touch In Page
- Protocol `protocol` - ⊞ - Selects which network protocol to use to transfer data. Different protocol's have methods of connecting and using the address parameter. For more information refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article.
  * Streaming (TCP/IP) `streaming` -
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Address `address` - The computer name or IP address of the server computer. You can use an IP address (e.g. `100.123.45.78`) or the computer's network name can be used directly. If you put "`localhost`", it means the other end of the pipe is on the same computer.
- Network Port `port` - The network port of the server.
- Active `active` - While on, the CHOP receives information from the pipe or server. While off, no updating occurs. Data sent by a server is lost, but a pipe will store the data until Active is turned on again. If in Network mode, turning this parameter on initiates a connection, and turning it off breaks the connection.
- Queue Target `queuetarget` - The target queue length the CHOP will attempt to maintain.
- Queue Target Unit `queuetargetunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Queue Variance `queuevariance` - The range around the Queue Target that's acceptable. If the queue's length is within the target and variance range, the CHOP will not bother to adjust the queue length.
- Queue Variance Unit `queuevarianceunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Maximum Queue `maxqueue` - The maximum size of the queue when full. Incoming samples will be dropped if the maximum queue is reached.
- Max Queue Unit `maxqueueunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Queue Adjust Time `adjusttime` - Specifies how often to repeat/drop a samples in order to get closer to the queue target range. If the value = 1 and the units = seconds, then it will try to repeat/drop a sample once per second to maintain the queue target set in the Minimum Target and Maximum Target parameters above.
- Adjust Unit `adjusttimeunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Recover Outside Range `recover` - If the queue size goes outside of the target size range for more than the 'adjust time', then if this option is on it will stop delivering new data or throw away a lot of data, until queue size is back in the middle of the min/max target. If this option is of the queue size will be slowly inched towards the target size instead (by dropping or repeating single frames every once in a while).
- Use Synced Ports `syncports` - ⊞ - This parameter lets you send the the data in a single global pipe if required. This can be important if various data streams must be sent in frame sync. For more information, refer to [Touch In/Out Synced Ports](https://docs.derivative.ca/Touch_In/Out_Synced_Ports "Touch In/Out Synced Ports").
  * Off `off` - Uses separate ports for each port number assigned.
  * On `on` - Uses a single global pipe for all Touch Out CHOPs using this Transfer Port Type. The global pipe uses port 10500 internally to send all the global port type data together at once. The Network Port parameter is still used to determine which Touch In CHOP gets the data on the receiving side.

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
Extra Information for the Touch In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Touch In CHOP Info Channels
  * read_index -

  * time_queue_under_min_target -

  * time_queue_over_max_target -

  * queue_retarded_total -

  * queue_advanced_total -

  * queue_recover_total -

  * queue_size_start -

  * queue_added -

  * queue_size_end -

  * queue_bumped -

  * read_repeat -

  * read_filled -

  * frames_received -

  * send_receive_diff -

  * local_clock_rate -

  * remote_clock_rate -

  * remote_elapsed_time -

  * remote_frame -

  * remote_frame_lag -

  * remote_frame_range -

  * io_errors -

  * connected -

  * names_resent -

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
