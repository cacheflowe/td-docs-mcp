---
url: https://docs.derivative.ca/Text_DAT
category: DATs
title: Text_DAT
---

# Text DAT
## Summary

The Text DAT lets you edit free-form, multi-line ASCII text. It is used for scripts, GLSL shaders, notes, XML and other purposes. "Free-form text" is one of the two forms of DATs (the other being tables of rows and columns of cells, each cell containing a text string as in a [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT")).
Text can be typed into the DAT when its [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active") is on, or in an external text editor. The Text DAT can get its data from a file on disk or from a file on the web. Use `http://` when specifying a remote text file.
See also the Execute DATs which are specialized to run their text as a script: [CHOP Execute DAT](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT") runs its script when a CHOP channel changes, [DAT Execute DAT](https://docs.derivative.ca/DAT_Execute_DAT "DAT Execute DAT") when a DAT changes, [Execute DAT](https://docs.derivative.ca/Execute_DAT "Execute DAT") when you start or end your TouchDesigner process or want to run a script every frame, [Panel Execute DAT](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT") when a control panel changes, [Parameter Execute DAT](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT") when a parameter of a node changes, and [OP Execute DAT](https://docs.derivative.ca/OP_Execute_DAT "OP Execute DAT") when anything else about an operator changes, including creation and deletion of nodes in a component's network.
Use the [Web DAT](https://docs.derivative.ca/Web_DAT "Web DAT") to fetch via a URL query.
[textDAT_Class](https://docs.derivative.ca/TextDAT_Class "TextDAT Class")

## Parameters - File Page
- Edit.. `edit` - Clicking this opens a text editor to add/edit/delete text from the DAT.
- File `file` - The filesystem path and name of the file to load. Accepts `.txt` and `.dat` files.
- Sync to File `syncfile` - When On, loads the file from disk into the DAT when the projects starts. A filename must be specified. Turning on the option will load the file from disk immediately. If the file does not exist, it will be created the first time the DAT is updated. The file is monitored so that any changes made to the file will update the DAT, and any changes made to the DAT will be written to the file right away. If the file is removed, the DAT will retain its current contents.
- Load on Start `loadonstart` - When On, reloads the file from disk into the DAT when the projects starts.
- Load File `loadonstartpulse` - Instantly reloads the file.
- Write on Toe Save `write` - When On, writes the contents of the DAT out to the file on disk when the project is saved.
- Write File `writepulse` - Instantly write the file to disk.

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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Text DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
