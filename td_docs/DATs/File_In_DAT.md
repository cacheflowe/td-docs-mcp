---
url: https://docs.derivative.ca/File_In_DAT
category: DATs
title: File_In_DAT
---

# File In DAT
## Summary

The File In DAT reads in `.txt` text files and `.dat` table files. It will attempt to read any other file as raw text. The file can be located on disk or on the web. Use `http://` when specifying a URL.
See also [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT"), [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT").
[fileinDAT_Class](https://docs.derivative.ca/FileinDAT_Class "FileinDAT Class")

## Parameters - File In Page
- File `file` - The filesystem path and name of the file to load. Accepts `.txt` files for regular text and `.dat` files for text in table format.
- Convert Text to Table `converttable` - Converts the contents of the DAT from regular text to table-formatted text (tab-delimited text, each <tab> is a new column in the table).
- Refresh `refresh` - Reload the file when this parameter is set to On.
- Refresh Pulse `refreshpulse` - Instantly reload the file from disk.

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
Extra Information for the File In DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
