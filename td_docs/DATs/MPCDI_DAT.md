---
url: https://docs.derivative.ca/MPCDI_DAT
category: DATs
title: MPCDI_DAT
---

# MPCDI DAT
## Summary

The MPCDI DAT lets you load calibration data stored in the MPCDI format. Please refer to the [MPCDI](https://docs.derivative.ca/MPCDI "MPCDI") entry for a complete guide on TouchDesigners integration with the MPCDI Standard.
Use the `projection` and `cameraTransform` python members of this node in a [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") to make use of the camera information contained in the configuration file.
[mpcdiDAT_Class](https://docs.derivative.ca/MpcdiDAT_Class "MpcdiDAT Class")

## Parameters - MPCDI Page
- Configuration File `file` - Specify the location of the .mpcdi file.
- Reload Pulse `reloadpulse` - Instantly reloads the file.
- Output by `outputby` - ⊞ - The menu determines how to fill the DAT rows, with a single region or full buffers.
  * Single Region `single` -
  * Full Buffer `fullbuffer` -

- Buffer ID `bufferid` - Buffer ID to output.
- Region ID `regionid` - Region ID to output.
- Near `near` - Sets the near value.
- Far `far` - Sets the far value.

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
Extra Information for the MPCDI DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
