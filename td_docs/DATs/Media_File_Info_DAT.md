---
url: https://docs.derivative.ca/Media_File_Info_DAT
category: DATs
title: Media_File_Info_DAT
---

# Media File Info DAT
## Summary

The Media File Info DAT encapsulates the essential metadata for a Media File. Metadata information like the codec, frame rate, audio sample rate, resolution etc is outputted.
A media file can be inputted to the DAT by either specifying the File path, or by referencing a [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") or [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP").
[mediafileinfoDAT_Class](https://docs.derivative.ca/MediafileinfoDAT_Class "MediafileinfoDAT Class")

## Parameters - Media Info Page
- File `file` - The path and name of the image or movie file to load. Image and movie formats are those found in [File Types](https://docs.derivative.ca/File_Types "File Types"). You can specify files on the internet using `http://` ...
- TOP/CHOP `topchop` - Reference to a [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") or [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP") to read file information from.
- Reload Pulse `reloadpulse` - Change from 0 to 1 to force the file to reload, useful when the file changes or did not exist at first.
- File Open Timeout `opentimeout` - The time (in milliseconds) TouchDesigner will wait for a file to open. If the Disk Open Timout is reached, the Media File Info will stop waiting and output nothing. If the file still isn't opened the next time the DAT cooks, it'll wait again, and do the same. It'll keep doing this until the file is opened, or the open fails.
- Transpose `transpose` - The output will be changed from row per item to column per item.

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
Extra Information for the Media File Info DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
