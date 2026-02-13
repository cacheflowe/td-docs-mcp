---
url: https://docs.derivative.ca/Touch_In_DAT
category: DATs
title: Touch_In_DAT
---

# Touch In DAT
## Summary

The Touch In DAT receives full tables across the network from the [Touch Out DAT](https://docs.derivative.ca/Touch_Out_DAT "Touch Out DAT"), as opposed to messages with the other network based DATs.
See also [UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT").
[touchinDAT_Class](https://docs.derivative.ca/TouchinDAT_Class "TouchinDAT Class")

## Parameters - Touch In Page
- Protocol `protocol` - ⊞ - Select which protocol to use, refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Streaming (TCP/IP) `streaming` -
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `address` - For multi-cast protocol, this is the multi-cast address to listen for. For UDT protocol this is the IP address of the server.
- Port `port` - The port receiving the packets.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Active `active` - While on, the DAT receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost.

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
Extra Information for the Touch In DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Touch In DAT Info Channels
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
