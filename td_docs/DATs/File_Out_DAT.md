---
url: https://docs.derivative.ca/File_Out_DAT
category: DATs
title: File_Out_DAT
---

# File Out DAT
## Summary

The File Out DAT allows you to write out DAT contents to a `.dat` file or a `.txt` file. A `.dat` file is one of the [File Types](https://docs.derivative.ca/File_Types "File Types") of TouchDesigner that is used to hold the arrays of the [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT").
When the File Out DAT has 0 inputs, it can be triggered to send text by using the `send` command.
If 'Append' is off, a new file is written every time, if 'Append' is on, the file is appended to, and the file handle remains open.
[fileoutDAT_Class](https://docs.derivative.ca/FileoutDAT_Class "FileoutDAT Class")

## Parameters - File Out Page
- File `file` - The filesystem path and name of the file to be written.
- N `n` - Using `me.par.n` (or $N in [Tscript](https://docs.derivative.ca/Tscript "Tscript")) in the filename (in the File parameter) in conjuction with the N parameter here gives a method of incrementing file names. The N parameter must manually be incremented each time. Exporting a [Count CHOP](https://docs.derivative.ca/Count_CHOP "Count CHOP") which increments each time you want to save out a new file is an easy way to do this.
- Write File `write` - Press this button to write the file once.
- Append (txt Only) `append` - Appends the text into the file instead of overwriting the file contents completely.

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
Extra Information for the File Out DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
