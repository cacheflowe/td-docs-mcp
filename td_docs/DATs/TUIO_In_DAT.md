---
url: https://docs.derivative.ca/TUIO_In_DAT
category: DATs
title: TUIO_In_DAT
---

# TUIO In DAT
## Summary

The TUIO In DAT receives and parses [TUIO](https://www.tuio.org/?tuio11) messages (received over network) into columns in the table. TUIO packets OSC bundles, so TUIO data can also be viewed in its more raw form in an [OSC In DAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT"). It currently uses the TUIO 1.1 protocol. The TUIO 2.0 protocol is not yet supported.
[tuioinDAT_Class](https://docs.derivative.ca/TuioinDAT_Class "TuioinDAT Class")

## Parameters - Connect Page
- Protocol `protocol` - ⊞ - Select which protocol to use, refer to the [Network Protocols](https://docs.derivative.ca/Network_Protocols "Network Protocols") article for more information.
  * Messaging (UDP) `msging` -
  * Multi-Cast Messaging (UDP) `multicastmsging` -
  * Reliable Messaging (UDT Library) `reliablemsging` -

- Network Address `address` - For multi-cast protocol, this is the multi-cast address to listen for.
- Port `port` - The port which TUIO In will accept packets on.
- Shared Connection `shared` - Use the same connection as other networking DATs using the same network protocol.
- Active `active` - While on, the DAT receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost.

## Parameters - Received Messages Page
- Callbacks DAT `callbacks` - The Callbacks DAT will get callbacks for TUIO events. See [tuioinDAT_Class](https://docs.derivative.ca/TuioinDAT_Class "TuioinDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location (for example, where 'cc' points to).
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute from is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute from parameter is set to Specified Operator.

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
Extra Information for the TUIO In DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific TUIO In DAT Info Channels
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
