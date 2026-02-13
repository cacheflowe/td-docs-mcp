---
url: https://docs.derivative.ca/Pipe_Out_CHOP
category: CHOPs
title: Pipe_Out_CHOP
---

# Pipe Out CHOP
## Summary

The Pipe Out CHOP can be used to transmit data out of TouchDesigner to other processes running on a remote machine using a network connection. If the other process is another TouchDesigner process, a [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP") in that process can be used to receive the data. Multiple PipeIn CHOPs can connect to a PipeOut CHOP.
For more information on how to connect two TouchDesigner processes running on different machines with a Pipe In and Pipe Out CHOP, see the [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP").
**NOTE:** For TouchDesigner-to-TouchDesigner communication of channel data, see the [Touch In CHOP](https://docs.derivative.ca/Touch_In_CHOP "Touch In CHOP") and [Touch Out CHOP](https://docs.derivative.ca/Touch_Out_CHOP "Touch Out CHOP") which offer optimized and [Time Sliced](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") data transfer.
**TIP:** The [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT") or [UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT") is the preferred way to send script commands and other data packets over the network.
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
See also [OSC Out CHOP](https://docs.derivative.ca/OSC_Out_CHOP "OSC Out CHOP"), [Shared Mem Out CHOP](https://docs.derivative.ca/Shared_Mem_Out_CHOP "Shared Mem Out CHOP").
[pipeoutCHOP_Class](https://docs.derivative.ca/PipeoutCHOP_Class "PipeoutCHOP Class")

## Parameters - PipeOut Page
- Connection Mode `mode` - ⊞ - Set operation as server or client.
  * This Operator is Client `client` -
  * This Operator is Server `server` -

- Server Address `address` - The computer name or IP address of the server computer. This address is a standard WWW address, such as '`foo`' or '`foo.bar.com`'. You can use an IP address (e.g. `100.123.45.78`) or the computer's network name can be entered. If you put "`localhost`", it means the other end of the pipe is on the same computer.
- Server Port `port` - The network port to use.
- Active `active` - When Off, data is not sent.
- Send Input `sendinput` - On/off toggle for sending the data connected to the Pipe Out CHOP's input.
- Send Current Sample Only `sendsingle` - This parameter is only enabled if the Pipe Out CHOP is not [time sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing") (See Common Page of parameters). If On, it only sends the current frame's sample. If Off, it sends all data between this frame and the last frame TouchDesigner cooked at. The difference arises when TouchDesigner is not cooking 60 frames per second and is skipping frames. If playback skips by 3 animation frames between screen draws, the On case sends only one frame of data, and the Off case sends 3 frames of data (a "[Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)")" in TouchDesigner-speak).
- Single Sample `sample` - ⊞ - In single sample mode, this parameter determines which sample to send; the sample at frame 1 or the current sample.
  * Current Frame `scur` -
  * Frame 1 `sstart` -

- Send All Data `upload` - When the button is pressed, sends all the channel names and their data once in one burst.
- Script `script` - Use these parameters to send a one-time textport command through the pipe.
- Send Script `sendscript` - Use these parameters to send a one-time textport command through the pipe.
- Cook Every Frame `cookalways` - Turn this on to make sure this CHOP gets processed every frame. Usually CHOPs do not get processed every frame unless they are directly involved with some aspect of the geometry being displayed.
- Send Monitor Pulses `pulse` - Sends pulses (a single null character) once a frame, to monitor the connection. This keeps the connection active, and keeps the Pipe In CHOP aware of the connection status so it can properly report its state.
- Echo Messages to Console `echo` - Print all outgoing data to the Console which can be opened from the Dialogs menu. See this option in the [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP") for more details.
- Callbacks DAT `callbacks` - Path to a DAT containing callback methods for each event sent. See [pipeoutCHOP_Class](https://docs.derivative.ca/PipeoutCHOP_Class "PipeoutCHOP Class") for usage.

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
Extra Information for the Pipe Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Pipe Out CHOP Info Channels
  * connected -

  * num_connected -

  * num_cached -

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
