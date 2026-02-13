---
url: https://docs.derivative.ca/WebSocket_DAT
category: DATs
title: WebSocket_DAT
---

# WebSocket DAT
## Summary

The WebSocket DAT receives and parses [WebSocket](http://en.wikipedia.org/wiki/WebSocket) messages. WebSockets are fast an efficient two way communication protocol used by web servers and clients. Each message is parsed and appended as a row in the DAT's table. The table is FIFO "first-in first-out" and limited to parameter-set number of lines. An optional script may be run for each packet received. Secure (tls) websocket servers are also supported. Connections to different WebSocket sites are supported without requiring manual header setup.
The WebSocket DAT prints status and error messages to the TouchDesigner text console. The text console can be enabled by setting the environment variable TOUCH_TEXT_CONSOLE=1 (see: <https://docs.derivative.ca/Variables#System_Environment_Variables>). The text console will open the next time TouchDesigner is launched.
For SocketIO support see the [SocketIO DAT](https://docs.derivative.ca/SocketIO_DAT "SocketIO DAT").
See also: [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT")
Example project: [chat with WebSockets](http://www.derivative.ca/Forum/viewtopic.php?p=30301)
[websocketDAT_Class](https://docs.derivative.ca/WebsocketDAT_Class "WebsocketDAT Class")

## Parameters - Connect Page
- Active `active` - While on, the DAT receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost.
- Network Address `netaddress` - The network address of the server computer. This address is a standard WWW address, such as `foo` or `foo.bar.com`. You can put an IP address (e.g. `100.123.45.78`). If you put `localhost`, it means the other end of the connection is on the same computer.
- Network Port `port` - The port in which the DAT will accept messages. Port 443 implies a secure connection. If attempting a secure connection not using port 443 then a "wss://" prefix is required on the Network Address parameter.
- Connection Timeout `timeout` - Time in milliseconds the WebSocket DAT will wait to connect to the server. Note: this is an upper limit and the connection may fail before the connection timeout is reached.

## Parameters - Received Messages Page
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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the WebSocket DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
