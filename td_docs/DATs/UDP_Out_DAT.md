---
url: https://docs.derivative.ca/UDP_Out_DAT
category: DATs
title: UDP_Out_DAT
---

# UDP Out DAT
## Summary

The UDP Out DAT is used to send information over a UDP connection to/from a remotely-located computer. Use the `sendBytes()` or `send()` methods of the [udpoutDAT_Class](https://docs.derivative.ca/UdpoutDAT_Class "UdpoutDAT Class") to send messages.
Although is it an 'Out' node, it can receive reply messages from the machine(s) it sends to. The messages will appear in the DAT's contents (just like the [UDP In DAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT")).
See also [UDP In DAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT"), [Touch Out DAT](https://docs.derivative.ca/Touch_Out_DAT "Touch Out DAT") and [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[udpoutDAT_Class](https://docs.derivative.ca/UdpoutDAT_Class "UdpoutDAT Class")

## Parameters - Connect Page
- Active `active` - This check box enables the connection.
- Protocol `protocol` - ⊞ - Selects the network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `address` - You can put an IP address (e.g. 100.123.45.78), or a machine name to send to. If you put "localhost", it means the other end of the pipe is on the same computer. If you are using multi-cast you should put the multi-cast address you want to send to here.
- Port `port` - The network port to send to.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Row/Callback Format `format` - ⊞ - Determines how the incoming data is parsed.
  * One Per Byte `perbyte` - One row is added to the table per byte received.
  * One Per Line `perline` - One row is added to the table per line received. The end of a line is delimited by \n, \r or a null character (\0).
  * One Per Message `permessage` - One row is added to the table per message received.

- Local Address `localaddress` - Specify an IP address to send from, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use.
- Local Port Mode `localportmode` - ⊞ - Choose between automatically or manually selecting local port to use.
  * Automatic `automatic` -
  * Manual `manual` -

- Local Port `localport` - When the above parameter is set to 'Manual', enter the port number to use here.

## Parameters - Received Data Page
- Callbacks DAT `callbacks` - The Callbacks DAT will execute once for each message coming in.
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
Extra Information for the UDP Out DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific UDP Out DAT Info Channels
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
