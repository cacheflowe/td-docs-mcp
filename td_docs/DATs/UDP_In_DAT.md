---
url: https://docs.derivative.ca/UDP_In_DAT
category: DATs
title: UDP_In_DAT
---

# UDP In DAT
## Summary

The UDP In DAT is used for receiving information over a UDP connection between two remotely located computers. It captures all the messages without any queuing or buffering, and allows you to send it any messages you want. Once this DAT has received a message it can reply to the sender using the 'send' command. Using the send command before it has received a message will not work because it doesn't know where to send data yet. When in multicast mode it doesn't send out a multicast message, it sends a reply directly to the originator for the last multicast message it got.
See also [Peer Class](https://docs.derivative.ca/Peer_Class "Peer Class"), [UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT"), [Touch In DAT](https://docs.derivative.ca/Touch_In_DAT "Touch In DAT") and [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[udpinDAT_Class](https://docs.derivative.ca/UdpinDAT_Class "UdpinDAT Class")

## Parameters - Connect Page
- Protocol `protocol` - ⊞ - Select which protocol to use, refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `address` - The multi-cast IP address to listen for.
- Port `port` - The network port to listen on.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Row/Callback Format `format` - ⊞ - Determines how the incoming data is parsed.
  * One Per Byte `perbyte` - One row is added to the table per byte received.
  * One Per Line `perline` - One row is added to the table per line received. The end of a line is delimited by \n, \r or a null character (\0).
  * One Per Message `permessage` - One row is added to the table per message received.

- Active `active` - This check box enables the connection.

## Parameters - Received Data Page
- Callbacks DAT `callbacks` - The Callbacks DAT will execute once for each message coming in. See [udpinDAT_Class](https://docs.derivative.ca/UdpinDAT_Class "UdpinDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute from is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute from parameter is set to Specified Operator.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a python script `op(_"opname"_).par.clear.pulse()`
- Bytes Column `bytes` - Outputs the raw bytes of the message in a separate column.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * From Language `language` - pick extension from DATs script language.
  * Custom Extension `custom` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Info CHOP Channels
Extra Information for the UDP In DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific UDP In DAT Info Channels
  * messages_pending -

###
## Common DAT Info Channels
  * num_rows - Number of rows in this DAT.

  * num_cols - Number of columns in this DAT.

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
