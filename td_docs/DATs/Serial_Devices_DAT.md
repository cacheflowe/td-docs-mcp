---
url: https://docs.derivative.ca/Serial_Devices_DAT
category: DATs
title: Serial_Devices_DAT
---

# Serial Devices DAT
## Summary

Provide a list of connected serial devices which can be refreshed manually or at periodic intervals. A callback DAT is provided to react to addition/removal of devices.
[serialdevicesDAT_Class](https://docs.derivative.ca/SerialdevicesDAT_Class "SerialdevicesDAT Class")

## Parameters - Serial Devices Page
- Callbacks DAT `callbacks` - Runs this script once for each change to the table. See [serialdevicesDAT_Class](https://docs.derivative.ca/SerialdevicesDAT_Class "SerialdevicesDAT Class") for usage.
- Usage `usage` - ⊞ - Specify which serial devices to report information about based on their availability.
  * Any `any` - All serial devices will report information.
  * In Use `inuse` - Only serial devices that are occupied will report information.
  * Not In Use `notinuse` - Only serial devices that are unoccupied will report information.

- Refresh Pulse `refreshpulse` - Instantly poll for serial device changes and update the table.
- Enable Polling `enablepolling` - While on, poll for serial device changes periodically and update the table.
- Polling Time `pollingtime` - Time in seconds to wait for the next poll.

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
Extra Information for the can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP"). _[Info Channels Common Page](https://docs.derivative.ca/index.php?title=Info_Channels_Common_Page&action=edit&redlink=1 "Info Channels Common Page \(page does not exist\)")_
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
