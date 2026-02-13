---
url: https://docs.derivative.ca/UDT_In_DAT
category: DATs
title: UDT_In_DAT
---

# UDT In DAT
## Summary

**NOTE This DAT has been removed from TouchDesigner 2021 Official builds and later.**
The UDT In DAT is used for receiving information over a [UDT](https://docs.derivative.ca/UDT "UDT") connection between two remotely located computers. It captures all the messages without any queuing or buffering, and allows you to send it any messages you want. UDT Streaming is a reliable, streaming, connection orientated protocol. A single server can send to multiple clients at the same time.
Handle received messages using the callback DAT attached to the UDT In DAT. Send replies using the [udtinDAT_Class](https://docs.derivative.ca/UdtinDAT_Class "UdtinDAT Class").
See also [Peer Class](https://docs.derivative.ca/Peer_Class "Peer Class"), [UDT Out DAT](https://docs.derivative.ca/UDT_Out_DAT "UDT Out DAT"), [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[udtinDAT_Class](https://docs.derivative.ca/UdtinDAT_Class "UdtinDAT Class")

## Parameters - Connect Page
- Protocol `protocol` - ⊞ - Select which protocol to use, refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Fast Streaming `faststreaming` -
  * Reliable Messaging `reliablemsging` -

- Network Address `address` - You can put an IP address to listen on (224.0.0.1). This parameter is only needed for multicast protocols.
- Port `port` - The network port the listen on.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Row/Callback Format `format` - ⊞ - Determines how the incoming data is parsed into the table.
  * One Per Byte `perbyte` - One row is added to the table per byte received.
  * One Per Line `perline` - One row is added to the table per line received.
  * One Per Message `permessage` - One row is added to the table per message received.

- Active `active` - This check box enables the connection.

## Parameters - Received Data Page
- Callbacks DAT `callbacks` - The Callbacks DAT will execute once for each message coming in. See [udtinDAT_Class](https://docs.derivative.ca/UdtinDAT_Class "UdtinDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location
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
