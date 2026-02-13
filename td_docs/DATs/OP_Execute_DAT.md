---
url: https://docs.derivative.ca/OP_Execute_DAT
category: DATs
title: OP_Execute_DAT
---

# OP Execute DAT
## Summary

The OP Execute DAT runs a script when the state of an [operator](https://docs.derivative.ca/Operator "Operator") changes.
OP Execute DATs are created with default python method placeholders. For each monitored condition in the parameters, there is a [matching python method](https://docs.derivative.ca/OpexecuteDAT_Class "OpexecuteDAT Class") in the DAT. When a condition is turned on in the parameters, each time that condition is satisfied the corresponding python method will be executed.
[opexecuteDAT_Class](https://docs.derivative.ca/OpexecuteDAT_Class "OpexecuteDAT Class")

## Parameters - OP Execute Page
- Active `active` - While on, the DAT will respond to the OP that is referenced.
- Execute from `executeloc` - ⊞ - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) Determines the location the script is run from.
  * Current Node `current` - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) The script is executed from the current node location.
  * This Node `here` - The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The path that the script will be executed from if the Execute From parameter is set to _Specified Operator_.
- Monitor OPs `op` - Specify which operators to monitor to trigger the scripts.
- Pre Cook `precook` - The `onPreCook()` method is triggered before the operator is cooked.
- Post Cook `postcook` - The `onPostCook()` method is triggered after the operator is cooked.
- Destroy `opdelete` - The `onDestroy()` method is triggered when the operator is deleted.
- Flag Change `flagchange` - The `onFlagChange()` method is triggered when one of the operator's [Flags](https://docs.derivative.ca/index.php?title=Flags&action=edit&redlink=1 "Flags \(page does not exist\)") changes state. This includes all the flags in the Common Flags list of an [OP_Class](https://docs.derivative.ca/OP_Class#Common_Flags "OP Class"), plus all the python accessible flags listed in [COMP_Class](https://docs.derivative.ca/COMP_Class#Common_Flags "COMP Class"), [SOP_Class](https://docs.derivative.ca/SOP_Class#Common_Flags "SOP Class"), [CHOP_Class](https://docs.derivative.ca/CHOP_Class#Common_Flags "CHOP Class").
- Wire Change `wirechange` - The `onWireChange()` method is triggered when the operator's inputs are rewired (connected, disconnected, swapped).
- Name Change `namechange` - The `onNameChange()` method is triggered when the name of the operator is changed.
- Path Change `pathchange` - The `onPathChange()` method is triggered when the path of the operator is changed.
- UI Change `uichange` - The `onUIChange()` method is triggered when operator is resized or moved in the network editor.
- Number Children Change `numchildrenchange` - The onNumChildrenChange() method is triggered if the number of children an operator has changes. Only works with [Component](https://docs.derivative.ca/Component "Component") type operators.
- Child Rename `childrename` - The `onChildRename()` method is triggered if a child of the operator is renamed.
- Current Child Change `currentchildchange` - The `onCurrentChildChange()` method is triggered if a child of the operator is made current in a network. Only works with Component type operators.
- Extension Change `extensionchange` - The `onExtensionChange()` method is triggered when an extension of the operator is changed.
- Edit.. `edit` - Clicking this opens a text editor to edit text in the DAT.

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
Extra Information for the OP Execute DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
