---
url: https://docs.derivative.ca/SocketIO_DAT
category: DATs
title: SocketIO_DAT
---

# SocketIO DAT
## Summary

The SocketIO DAT connects to a [Socket.IO](https://docs.derivative.ca/Socket.IO "Socket.IO") server at the specified URL.
The SocketIO DAT has 4 inputs in the following order ([example](https://docs.derivative.ca/File:SocketioDAT_inputs.png)):
  1. **Additional headers** in table format with two columns, structured as name/value pairs. Equivalent to [extraHeaders](http://socket.io/docs/v3/client-initialization/#extraheaders) option.
  2. **Server events** to listen to in table format, structured as a single column of event names. When the server emits any of these events the `onReceiveEvent` callback will be triggered.
  3. **Additional query parameters** in table format with two columns, structured as name/value pairs. Equivalent to [query](http://socket.io/docs/v3/client-initialization/#query) option.
  4. **Authentication parameters** in table format with two columns, structured as name/value pairs. Typical socket.io auth usage requires a _token_ entry. Equivalent to [auth](http://socket.io/docs/v3/client-initialization/#auth) option.

The SocketIO DAT can also emit events to the server. This is done using the python `emit` method. Acknowledgement callbacks are not supported.
The SocketIO DAT is built with [socket.io's C++ Client API](https://github.com/socketio/socket.io-client-cpp) v3.1.0 and works with socket.io v3 or v4 servers.
The SocketIO DAT prints socket.io status messages to the TouchDesigner text console. The text console can be enabled by setting the environment variable `TOUCH_TEXT_CONSOLE=1` (see: <https://docs.derivative.ca/Variables#System_Environment_Variables>). The text console will open the next time TouchDesigner is launched.
See also: [WebSocket DAT](https://docs.derivative.ca/WebSocket_DAT "WebSocket DAT"), [Web Client DAT](https://docs.derivative.ca/Web_Client_DAT "Web Client DAT")
[socketioDAT_Class](https://docs.derivative.ca/SocketioDAT_Class "SocketioDAT Class")

## Parameters - Connect Page
- Active `active` - When enabled, the SocketIO DAT is actively listening for events from the server, and can also emit events.
- Reset `reset` - Disconnects the connection and then reconnects.
- URL `url` - The URL of the socket.io server.
- Verify Certificate (TLS) `verifycert` - Enables TLS (transport layer security) certificate verification.
- Reconnect Delay `delay` - The delay in milliseconds between reconnection attempts.

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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the SocketIO DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
