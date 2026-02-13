---
url: https://docs.derivative.ca/Sync_In_CHOP
category: CHOPs
title: Sync_In_CHOP
---

# Sync In CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Sync In CHOP and [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") are used to keep timelines in two or more TouchDesigner processes within a single frame of each other. One process will contain a [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") while one or more other processes contain Sync In CHOPs. The processes with Sync In CHOPs should have their **Realtime flag checked off** , as their frame rates will be determined by the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP"). Also note, all monitors (including all clients and server) should be set to the **same rate**. Note that unplugging or re-adding monitors may sometime change previously configured settings.
The CHOPs synchronize by pausing their own timeline until all Sync In/Out CHOPs have cooked. The [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") will be ahead of the Sync In CHOPs. If any CHOPs fail to communicate, the others will timeout, causing all processes to run slowly.
Client machines may come online at any point, or be switched off as desired, as the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") will adjust accordingly, either timing out, temporarily or permanently banning individual clients as specified.
In addition any extra CHOP channels sent through the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") is received by the Sync In CHOPs.
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
An [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT"), pointing to the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP"), provides a detailed list of all clients:
The columns are:
  * `pid`: process id of the client
  * `address`: ip and port number
  * `machine_name`: client machine name
  * `filename`: name of the `.toe` file the client resides in
  * `op_path`: full operator path to the client
  * `include`: when 1, the Sync Out CHOPs waits for a reply, when 0, it is ignored.
  * `timeout_total`: The total number of times the Sync Out CHOP stalled waiting for this client
  * `timeout_consecutive`: The running number of times the Sync Out CHOP stalled waiting for this client.
  * `steady_total`: The total number of times the Sync Out CHOP received a reply in time.
  * `steady_consecutive`: The running number of times the Sync Out CHOP received a reply in time:
  * `reply`: The last reply from the client, all clients should have the same increasing value.

Similarly, an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") will reveal further information: [Info CHOP Channels](#Info_CHOP_Channels)
##  Example Files
Here are two simple example files that use Sync In and Out CHOPs. You would run the SyncServer.toe only once, and run the SyncClient.toe for every machine you want to display on. Note that you may need to adjust the [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") located at /perform to output to your desired monitor. Also note that [Hardware Frame Lock](https://docs.derivative.ca/Hardware_Frame_Lock "Hardware Frame Lock") is not enabled in these examples, so if you want to use that feature you'll need to turn that parameter on in the [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") for SyncClient.toe as well.
[File:SyncServer.toe](https://docs.derivative.ca/File:SyncServer.toe "File:SyncServer.toe")
[File:SyncClient.toe](https://docs.derivative.ca/File:SyncClient.toe "File:SyncClient.toe")
##  Intermittent Connections
Whenever a client replies, it is immediately assumed reliable, and waited upon, by the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") each frame thereafter. When a client times-out a number of times in a row, however, it is continuously ignored by the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP"), until it replies on time again. This also applies to clients that have stopped communicating altogether. The number of consecutive timeouts is controlled by the `Client Timeouts (consecutive)` parameter and is reflected by the `timeout_consecutive` [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") column.
##  Fixing Dropped frames on Client
If a particular client is dropping frames, inspect the Sync Out CHOP on the server side with an info DAT. Look at the column for timeout_consecutive. As well take note of the info chop channel for the sync in CHOP called sync_incompletes. If one or both of these attributes are increasing, try adjusting the TimeOut parameter on the sync CHOP. Increasing this value has been known to remedy this issue.
##  Banning
If a client produces unreliable communication, sometimes steady, sometimes timing out, then it can be permanently ignored by enabling `Ban Clients` and setting the `Total Timeouts` accordingly. Once a client timeouts a certain number of times, its Info DAT `include` column reports `banned` and it will always be ignored, even if it starts responding in time again.
##  Resetting
Whenever the Sync Out CHOP first starts any and all clients are accepted, and nothing is banned. Pressing `Clear Stats` in the [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") also returns to this state, clearing all banned lists, and totals, even in the remote client [Info CHOPs](https://docs.derivative.ca/Info_CHOP "Info CHOP").

See also [Syncing Multiple Computers](https://docs.derivative.ca/Syncing_Multiple_Computers "Syncing Multiple Computers") and [Hardware Frame Lock](https://docs.derivative.ca/Hardware_Frame_Lock "Hardware Frame Lock").
[syncinCHOP_Class](https://docs.derivative.ca/SyncinCHOP_Class "SyncinCHOP Class")

## Parameters - Sync In Page
- Active `active` - Whether or not the CHOP is currently attempting to synchronize itself to a [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP").
- Multicast Address `multicastaddress` - An IP address to communicate on (224.0.0.1).
- Network Port `port` - The network port associated with the address.
- Timeout (msec) `timeout` - The maximum amount of time the CHOP will wait for synchronization signals from the other Sync CHOPs. This value is expressed in milliseconds.

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
Extra Information for the Sync In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Sync In CHOP Info Channels
  * sync_incompletes - This number is constant when the system is in sync, and will climb up each time the number of clients responding does not match the expected number. **When all is steady, the number does not change**.

  * sync_totaldelay - The total amount of time spent waiting for the Sync Out CHOP. (milliseconds).

  * sync_lastdelay - The amount of time waiting for the Sync Out CHOP for the last message (milliseconds).

  * sync_serial - The last serial index sent from the Sync Out CHOP. Increases each message sent.

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
