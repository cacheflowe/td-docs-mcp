---
url: https://docs.derivative.ca/Execute_DAT
category: DATs
title: Execute_DAT
---

# Execute DAT
## Summary

The Execute DAT lets you edit scripts and run them based on conditions. It can be executed at the start or end of every frame, or at the start or end of the TouchDesigner process.
Execute DATs are created with [default python method placeholders](https://docs.derivative.ca/ExecuteDAT_Class "ExecuteDAT Class"). For each monitored condition in the parameters, there is a matching python method in the DAT. When a condition is turned on in the parameters, each time that condition is satisfied the corresponding python method will be executed.
Text can also can be passed into the Text DAT through the node's input, however this text will not be editable. Text can be created in the DAT via the [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer") or an external text editor.
See also [OP Execute DAT](https://docs.derivative.ca/OP_Execute_DAT "OP Execute DAT").
[executeDAT_Class](https://docs.derivative.ca/ExecuteDAT_Class "ExecuteDAT Class")

## Parameters - Execute Page
- Active `active` - While on, the DAT will respond to the events selected below.
- Execute from `executeloc` - ⊞ - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) Determines the location the script is run from.
  * Current Node `current` - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) The script is executed from the current node location.
  * This Node `here` - The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - This component is also the path that the script will be executed from if the Execute From parameter is set to _Specified Operator_.
- Start `start` - The onStart() method is executed when TouchDesigner starts. This method is never called in TouchEngine because components are loaded after TouchEngine has started.
- Create `create` - The create() method is executed when the node is created. This can be triggered on start, by loading a component from disk, by copying & pasting, or any other way a node can be created.
- Exit `exit` - The onExit() method is executed when the TouchDesigner process quits.
- Frame Start `framestart` - The onFrameStart() method is executed at the start of every frame.
- Frame End `frameend` - The onFrameEnd() method is executed at the end of every frame.
- Play State Change `playstatechange` - The onPlayStateChange() method is executed each time the play state changes, ie. pause or play is used on the timeline.
- Device Change `devicechange` - The onDeviceChange() method is executed each time devices are connected or disconnected from the computer. For example, plugging in MIDI devices, cameras, joysticks, etc.
**NOTE:** When using multiple Execute DATs with Start and Create functions, they are triggered in numbered-alphanumeric order of the DAT's names.
- Edit.. `edit` - Clicking this opens a text editor to edit text in the DAT.
**TIP:** To direct all "standard output" of python to a Text DAT, put this in the `start()` method: `sys.stdout = op('text1')`
To safely to this and restore standard output:
```
prev = sys.stdout
sys.stdout = op('text1')
sys.stdout = prev

```

## Parameters - File Page
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
Extra Information for the Execute DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
