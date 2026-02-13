---
url: https://docs.derivative.ca/UDT_Out_DAT
category: DATs
title: UDT_Out_DAT
---

# UDT Out DAT
## Summary

**NOTE This DAT has been removed from TouchDesigner 2021 Official builds and later.**
The UDT Out DAT is used for sending information over a [UDT](https://docs.derivative.ca/UDT "UDT") connection between remotely located computers.
Send messages using the [udtoutDAT_Class](https://docs.derivative.ca/UdtoutDAT_Class "UdtoutDAT Class"). Handle received messages using the callback DAT attached to the [UDT In DAT](https://docs.derivative.ca/UDT_In_DAT "UDT In DAT"). See [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols").
Although it is an 'Out' node, it can receive reply messages from the machine(s) it sends to. The messages will appear in the DAT's contents (just like the [UDT In DAT](https://docs.derivative.ca/UDT_In_DAT "UDT In DAT")).
[Tscript](https://docs.derivative.ca/Tscript "Tscript") uses the `send` Command to initiate the data output.
See also: [UDT In DAT](https://docs.derivative.ca/UDT_In_DAT "UDT In DAT")
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[udtoutDAT_Class](https://docs.derivative.ca/UdtoutDAT_Class "UdtoutDAT Class")

## Parameters - Connect Page
- Protocol `protocol` - ⊞ - Selects the network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Fast Streaming `faststreaming` -
  * Reliable Messaging `reliablemsging` -

- Port `port` - The network port to send to.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Row/Callback Format `format` - ⊞ - Determines how the incoming data is parsed.
  * One Per Byte `perbyte` - One row is added to the table per byte received.
  * One Per Line `perline` - One row is added to the table per line received.
  * One Per Message `permessage` - One row is added to the table per message received.

- Active `active` - This check box enables the connection.

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
