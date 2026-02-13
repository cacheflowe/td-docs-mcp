---
url: https://docs.derivative.ca/Perform_DAT
category: DATs
title: Perform_DAT
---

# Perform DAT
## Summary

The Perform DAT logs various performance times in a [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") format. These benchmarks are similar to those reported by the [Performance Monitor](https://docs.derivative.ca/Performance_Monitor_Dialog "Performance Monitor Dialog").
[performDAT_Class](https://docs.derivative.ca/PerformDAT_Class "PerformDAT Class")

## Parameters - Perform Page
- Active `active` - ⊞ - Turns logging on/off. The DAT will continuously log while Active is On.
  * Active `active` -
  * Active Pulse `activepulse` -

- Trigger Mode `triggermode` - ⊞ - Offers two options for when to trigger a refresh of the logs.
  * When Frame Length Exceeds Threshold `threshold` - Use the Trigger Threshold parameter below to set a maximum frame time to wait before refreshing the log.
  * When a Frame is Dropped `droppedframe` - Refresh the log as soon as a frame is dropped.

- Trigger Threshold `triggerthreshold` - This is the amount of time, in milliseconds, that a frame must exceed to cause the DAT to log and output the frame's timing. For example to see what happens when a frame takes more that 33 ms to cook, put this parameter to 33.
- Cook Time `logcook` - Logs the cook time of operators.
- Export Time `logexport` - Logs time spent exporting CHOP channels.
- Viewport Draw Time `logviewport` - Logs time to draw 3D geometry and SOP viewers.
- Movie Time `logmovie` - Logs time taken to read video and audio from movie files.
- Draw Channels Time `logdrawchannels` - Logs time to draw channels in CHOP viewers.
- Object View Time `logobjectview` - Logs time to draw objects in 3D viewers.
- Custom Panel Time `logcustompanel` - Logs time taken by custom panels build with [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component").
- MIDI Time `logmidi` - Logs time spent on MIDI.
- Graphics Time `loggraphics` - Logs various graphics system calls, such as time spent waiting for the graphics card, calls to the graphic driver, converting TOP data to CHOPs, etc.
- Frame Length `logframelength` - Logs total frame time in milliseconds (ms).
- Misc `logmisc` - Logs miscellaneous times that do not fit into other categories.
- Script `logscript` - Logs time spent running scripts.
- Render `logrender` - Logs time spend by Render or Renderpass TOPs.
- Callbacks DAT `callbacks` - A path to the Callbacks DAT. Newly created Perform DATs include a docked Callbacks DAT.
- Clear `clear` - Clears the contents of the DAT.
- Active Pulse `activepulse` - Use resetpulse button to grab a single frame snapshot.

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
Extra Information for the Perform DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
