---
url: https://docs.derivative.ca/Audio_Devices_DAT
category: DATs
title: Audio_Devices_DAT
---

# Audio Devices DAT
## Summary

The Audio Devices DAT provides information about all detected audio devices including driver, direction (input or output), label, and name that can be referenced in the [Audio Device In CHOP](https://docs.derivative.ca/Audio_Device_In_CHOP "Audio Device In CHOP") and [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP").
You can also set it to display all available audio devices.
It runs a callback script when a change in audio devices has been detected and returns a list of names corresponding to the changed devices.
[audiodevicesDAT_Class](https://docs.derivative.ca/AudiodevicesDAT_Class "AudiodevicesDAT Class")

## Parameters - Audio Devices Page
- Driver `driver` - ⊞ - Menu of available drivers, table will only include devices belonging to selected driver.
  * default (DirectSound/CoreAudio) `default` -
  * ASIO `asio` -
  * DataPath (RGBEASY) `datapath` -
  * Blackmagic `blackmagic` -
  * AJA `aja` -
  * Deltacast `deltacast` -

- All Drivers `alldrivers` - While on, the table will display devices from all available drivers.
- Input Devices `input` - Toggle to include input devices.
- Output Devices `output` - Toggle to include output devices.
- Callbacks DAT `callbacks` - Runs this script once for each change to the table (ie. device state change).

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
Extra Information for the Audio Devices DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
