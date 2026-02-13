---
url: https://docs.derivative.ca/Touch_Out_DAT
category: DATs
title: Touch_Out_DAT
---

# Touch Out DAT
## Summary

The Touch Out DAT sends full DAT tables across the network to the [Touch In DAT](https://docs.derivative.ca/Touch_In_DAT "Touch In DAT") in another TouchDesigner process, as opposed to messages with the other network based DATs. It is an extremely powerful mechanism to sync data between TouchDesigner processes.
See also [UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT").
[touchoutDAT_Class](https://docs.derivative.ca/TouchoutDAT_Class "TouchoutDAT Class")

## Parameters - Touch Out Page
- Protocol `protocol` - ⊞ - Select which protocol to use, refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Streaming (TCP/IP) `streaming` -
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -

- Network Address `address` - For multi-cast protocol, this is the multi-cast address to listen for. For UDT protocol this is the IP address of the server.
- Port `port` - The port the packets will be sent over.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Active `active` - While on, the DAT sends data to the network port. While Off, no updating occurs.
- Redundant Sends `redendantsends` - The maximum number of times the same data will be consecutively sent.
- Resend Data `resend` - Send the current data regardless of how many times it has been sent.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * frag `frag` -
  * glsl `glsl` -
  * html `html` -
  * md `md` -
  * py `py` -
  * rtf `rtf` -
  * tsv `tsv` -
  * txt `txt` -
  * vert `vert` -
  * xml `xml` -
  * From Language `languageext` - pick extension from DATs script language.
  * Custom Extension `customext` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Touch Out DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Touch Out DAT Info Channels
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
