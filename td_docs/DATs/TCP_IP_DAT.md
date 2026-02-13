---
url: https://docs.derivative.ca/TCP/IP_DAT
category: DATs
title: TCP/IP_DAT
---

# TCP/IP DAT
## Summary

The TCP/IP DAT is used for sending and receiving information over a TCP/IP connection between two remotely located computers. It captures all the messages without any queuing or buffering, and allows you to send it any messages you want.
Send messages using the [tcpipDAT_Class](https://docs.derivative.ca/TcpipDAT_Class "TcpipDAT Class"). Handle received messages using the callback DAT attached to the TCP/IP DAT. See [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols").
This DAT can be used to intercept all the raw information being sent from a Pipe Out CHOP for example. The [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP") and [Pipe Out CHOP](https://docs.derivative.ca/Pipe_Out_CHOP "Pipe Out CHOP") also communicate through a TCP/IP connection, though they use a specific syntax.
See also [Peer Class](https://docs.derivative.ca/Peer_Class "Peer Class"), [UDP In DAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT"), [UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT").
For Tscript. see Tscript `send` Command.
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[tcpipDAT_Class](https://docs.derivative.ca/TcpipDAT_Class "TcpipDAT Class")

## Parameters - Connect Page
- Connection Mode `mode` - ⊞ - Specify if this operator is communicating as a **client** or a **server**.
  * This Operator is Client `client` -
  * This Operator is Server `server` -

- Network Address `address` - If this node is communicating as a client, this should be the IP address of the server.
- Port `port` - The network port to listen on or connect to, depending on of the node is the server or client respectively.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Row/Callback Format `format` - ⊞ - Determines how the incoming data is parsed into the table.
  * One Per Byte `perbyte` - One row is added to the table per byte received.
  * One Per Line `perline` - One row is added to the table per line received. The end of a line is delimited by \n, \r or a null character (\0).
**Note: In this format messages will not be logged until one of those characters are received.**
  * One For All Received Data `all` - One row is added to the table per message received. Since TCP/IP is a stream-based protocol, the end of a 'message' is arbitrary. It is simply the contents of the last read operation from the socket. If you are reading a custom message format, you'll likely need to build up a full message from multiple reads from the socket in Python.

- Active `active` - This check box enables the connection.

## Parameters - Received Data Page
- Callbacks DAT `callbacks` - The Callbacks DAT will execute once for each message received.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Script DAT parameter.
  * Specified Operator `op` - The script is executed from the component specified in the Component parameter below.

- From Operator `fromop` - The component who's state change will trigger the DAT to execute its script when Execute from is set to On Panel Change. This component is also the path that the script will be executed from if the Execute from parameter is set to Specified Component.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a script command, here is an example: `opparm -c /serial1 clear`
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
Extra Information for the TCP/IP DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific TCP/IP DAT Info Channels
  * connections -

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
