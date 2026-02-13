---
url: https://docs.derivative.ca/Info_DAT
category: DATs
title: Info_DAT
---

# Info DAT
## Summary

The Info DAT gives you string information about a node. Only some nodes contain additional string information which can be accessed by the Info DAT.
[infoDAT_Class](https://docs.derivative.ca/InfoDAT_Class "InfoDAT Class")

## Parameters - Info Page
- Operator `op` - The [path](https://docs.derivative.ca/Network_Path "Network Path") to the operator that the Info DAT is getting information from. You can drag & drop any node onto this path, or type the path directly into the field.
- Passive `passive` - If this option is off, the Info DAT will update automatically when the information changes. If on, the data may or may not be out-of-date, and the Info DAT may require a forced cook to update its contents. This parameter can by useful to prevent unnecessary cooking.

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
Extra Information for the Info DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
