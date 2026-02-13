---
url: https://docs.derivative.ca/Monitors_DAT
category: DATs
title: Monitors_DAT
---

# Monitors DAT
## Summary

The Monitors DAT is a table of data about all currently detected monitors with information on the resolution, screen positioning, monitor name and description, GPU, and a flag indicating whether it is a primary monitor or not.
You can also set it to display the overall bounds of all the detected monitors.
It runs a callback script when a change in the monitors has been detected. These changes can be that a monitor was plugged in, a monitor was unplugged, the resolution of a monitor has changed, or the primary monitor has changed.
The Monitor DAT returns top/bottom values in lower-left origin coordinates, (0,0) is the lower-left corner of the monitor.
[monitorsDAT_Class](https://docs.derivative.ca/MonitorsDAT_Class "MonitorsDAT Class")

## Parameters - Monitors Page
- Callbacks DAT `callbacks` - Runs this script once for each change to the table (ie. monitor state change). See [monitorsDAT_Class](https://docs.derivative.ca/MonitorsDAT_Class "MonitorsDAT Class") for usage.
- Bounds `bounds` - While on, an additional "bounds" row will be added to the table. The dimensions correspond to a bounding box around all the detected monitors. In this row, "primary" refers to the index in the table of the primary monitor.
- Monitors `monitors` - ⊞ - Specify which monitors to report information about.
  * All `all` -
  * Primary `primary` -
  * Non-Primary `nonprimary` -
  * Affinity `affinity` -
  * None `none` -

- Units `units` - ⊞ - Specify if the numbers are reported in Native Pixel units or DPI Scaled units.
  * Native `native` -
  * DPI Scaled `dpiscaled` -

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
Extra Information for the Monitors DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
