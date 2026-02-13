---
url: https://docs.derivative.ca/OSC_In_CHOP
category: CHOPs
title: OSC_In_CHOP
---

# OSC In CHOP
## Summary

The OSC In CHOP is used to accept Open Sound Control Messages. OSC In can be used to accept messages from either a 3rd party application which adheres to the Open Sound Control specification (<http://www.cnmat.berkeley.edu/OpenSoundControl/>). OSC In is based on a connection-less system, meaning that it can accept multiple messages for any number of sources at the same time. The user must specify a port number which OSC In will look for incoming messages. This port must not have anything running on it before OSC In attempts to use it. OSC CHOPs in TouchDesigner use the UDP transport protocol.
See also [OSC In DAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT"), [OSC Out CHOP](https://docs.derivative.ca/OSC_Out_CHOP "OSC Out CHOP"), [iOS and OSC](https://docs.derivative.ca/IOS_and_OSC "IOS and OSC"), [Touch In CHOP](https://docs.derivative.ca/Touch_In_CHOP "Touch In CHOP").
There are options which allow the user to adjust the default message queuing system to optimize it for their specific network conditions and usage needs. The Min/Max Target size specifies a range which the queue attempts to keep the buffer size at in seconds. Increasing the Queue Adjust Time will determine how long the queue can be outside that range before it tries to correct it.
If the user wishes to use OSC In to detect when messages are arriving, there is a Pulse Mode toggle which will read a single sample of any incoming message when it arrives and displays the pulse reset values any other time. This is useful for syncing beats between TouchDesigner and another applications.
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[oscinCHOP_Class](https://docs.derivative.ca/OscinCHOP_Class "OscinCHOP Class")

## Parameters - OSC In Page
- Active `active` - While on, the CHOP receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost.
- Protocol `protocol` - ⊞ - The network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `netaddress` - When using Multicast, this is the address that OSC In will listen for packets on.
- Network Port `port` - The port which OSC-In will accept packets on.
- Local Address `localaddress` - Specify an IP address to receive on, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use.
- OSC Address Scope `oscaddressscope` - To reduce which channels are generated, you can use channel name patterns to include or exclude channels. For example, `^*accel*` will exclude accelerometer channels coming in from an iPhone or iOS app like mrmr. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") for the syntax of the possible channel name patterns.
- Use Global Rate `useglobalrate` - When on, the CHOP will sample at the _global_ sample rate specified by TouchDesigner.
- Default Sample Rate `samplerate` - When Use Global Rate is off, this parameter is used to determine the sample rate of this CHOP.
- Queued `queued` - Turn this on to enable queuing to help avoid lost messages. Use the parameters below to setup the queue behavior.
- Queue Variance `queuevariance` - The range around the Queue Target that's acceptable. If the queue's length is within the target and variance range, the CHOP will not bother to adjust the queue length.
- Queue Variance Unit `queuevarianceunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Maximum Queue `maxqueue` - The maximum size of the queue when full. Incoming samples will be dropped if the maximum queue is reached.
- Max Queue Unit `maxqueueunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Queue Adjust Time `adjusttime` - Specifies how often to repeat/drop a samples in order to get closer to the queue target range. If the value = 1 and the units = seconds, then it will try to repeat/drop a sample once per second to maintain the queue target set in the Minimum Target and Maximum Target parameters above.
- Adjust Unit `adjusttimeunit` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Strip Prefix Segments `stripsegments` - Strip a number of prefixes from the incoming address. Example: An address of /a/b/c/d/e with 3 segments removed would show d/e (or d_e as a final channel name).
- Reset Channels `resetchannels` - Deletes all channels when set to On, new channels will not be added until Reset Channels is turned Off.
- Reset Channels Pulse `resetchannelspulse` - Instantly deletes all channels.
- Reset Values `resetvalues` - Resets all channel values to 0 when On, channel values will not be updated until Reset Values is turned Off.
- Reset Channels Pulse `resetchannelspulse` - Instantly resets all channels to 0.

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
Extra Information for the OSC In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific OSC In CHOP Info Channels
  * queue_length -

  * time_queue_under_min_target -

  * time_queue_over_max_target -

  * queue_retarded_total -

  * queue_advanced_total -

  * total_bumped -

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
