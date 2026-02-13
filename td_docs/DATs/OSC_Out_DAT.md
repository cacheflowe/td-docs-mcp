---
url: https://docs.derivative.ca/OSC_Out_DAT
category: DATs
title: OSC_Out_DAT
---

# OSC Out DAT
## Summary

The OSC Out DAT is used for sending information over a OSC connection between remotely located computers. Use the [`.sendOSC()`](https://docs.derivative.ca/OscoutDAT_Class "OscoutDAT Class") python method to output the OSC messages.
OSC bundles allows you to send a group of messages in a single command rather than as separate, individual messages. The OSC Out DAT `sendOSC()` function will accept a list of messages and send as a bundle when you set the kwarg `asBundle=True`. Bundles were created as a performance optimization for real-time control of synthesizers with a large number of parameters. (thx Jesse Gilbert)
See also [OSC](https://docs.derivative.ca/OSC "OSC"), [OSC In DAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT"), [OSC In CHOP](https://docs.derivative.ca/OSC_In_CHOP "OSC In CHOP"), [OSC Out CHOP](https://docs.derivative.ca/OSC_Out_CHOP "OSC Out CHOP"), [iOS and OSC](https://docs.derivative.ca/IOS_and_OSC "IOS and OSC"), [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols"), [Sync](https://docs.derivative.ca/Sync "Sync").
**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**
[oscoutDAT_Class](https://docs.derivative.ca/OscoutDAT_Class "OscoutDAT Class")

## Parameters - Connect Page
- Active `active` - While on, the DAT receives/sends information from/to the network port. While Off, no updating occurs. Data sent to the port is lost.
- Protocol `protocol` - ⊞ - Selects the network protocol to use. Refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -
  * Reliable Messaging (UDT Library) `reliablemsging` -

- Network Address `address` - The network address of the target computer when using UDP. For multi-cast this is the multi-cast address to send to. This address is a standard WWW address, such as 'foo' or 'foo.bar.com'. You can put an IP address (e.g. 100.123.45.78). If you put "localhost", it means the other end of the pipe is on the same computer.
- Port `port` - The network port to send to.
- Local Address `localaddress` - Specify an IP address to send from, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- OSC Address Scope `addscope` - To reduce which channels are generated, you can use channel name patterns to include or exclude channels. For example, `^*accel*` will exclude accelerometer channels coming in from an iOS or iPhone app like mrmr. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") for the syntax of the possible channel name patterns.
- Include Type Tag `typetag` - Includes the argument list type tag in each message. It includes the parameter type keywords (in case the parsing application needs to identify parmameter types).
- Split Bundle into Messages `splitbundle` - When On, each message contained within a bundle is given its own row.
- Split Message into Columns `splitmessage` - When On, OSC address and arguments are given individual columns, otherwise they are included in the message column.
- Bundle Timestamp Column `bundletimestamp` - When On, each bundle timestamp value is included in a column.

## Parameters - Received Messages Page
- Callbacks DAT `callbacks` - The Callbacks DAT will execute once for each message received.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute from is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator.
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
Extra Information for the OSC Out DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific OSC Out DAT Info Channels
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
