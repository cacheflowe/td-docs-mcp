---
url: https://docs.derivative.ca/Parameter_Execute_DAT
category: DATs
title: Parameter_Execute_DAT
---

# Parameter Execute DAT
## Summary

The Parameter Execute DAT runs a script when a [parameter](https://docs.derivative.ca/Parameter "Parameter") of any operator changes state. There are 4 ways a parameter can trigger the script: if its value, expression, export, or enable state changes.
Parameter Execute DATs are created with [default python method placeholders](https://docs.derivative.ca/ParameterexecuteDAT_Class#Callbacks "ParameterexecuteDAT Class"). Unlike other execute DATs, the Parameter Execute DAT does not cook the node that it is watching, to avoid issues with recursive updates.
[parameterexecuteDAT_Class](https://docs.derivative.ca/ParameterexecuteDAT_Class "ParameterexecuteDAT Class")

## Parameters - Parameter Execute Page
- Active `active` - While on, the DAT will respond to the Parameter that is referenced.
- Execute from `executeloc` - ⊞ - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) Determines the location the script is run from.
  * Current Node `current` - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) The script is executed from the current node location.
  * This Node `here` - The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - This operator is also the path that the script will be executed from if the Execute From parameter is set to _Specified Operator_.
- OPs `op` - Specify which operator(s) the triggering parameter belongs to.
- Parameters `pars` - Specify which parameter(s) to monitor for triggering the script.
- Value Change `valuechange` - The onValueChange() method executes when the parameter value specified changes value in any way. It is called once each frame.
- Values Changed `valueschanged` - The onValuesChanged() method executes at end of frame with complete list of individual parameter changes. The changes are a list of named tuples, where each tuple is (Par, previous value)
- On Pulse `onpulse` - The onPulse() method executes when a 'pulse' type parameter is pulsed by clicking on it or via the [Par](https://docs.derivative.ca/Par_Class "Par Class").pulse() method.
- Expression Change `expressionchange` - The onExpressionChange() method executes whenever the specified parameter's expression changes. For example, changing the expression from `me.time.frame` to `me.time.seconds` will trigger the script.
- Export Change `exportchange` - The onExportChange() method executes if the export path to the specified parameter changes. For example, if the parameter is being exported to from /chopname/chan1 and that is changed so /chopname2/chan2 is now exporting to it, then the script will be triggered.
- Enable Change `enablechange` - The onEnableChange() method executes if the specified parameter goes from being disabled to enabled.
- Mode Change `modechange` - The onModeChange() method executes if the specified [parameter's mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode") changes between the available constant, expression, export or bind mode.
- Custom `custom` - Monitor [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters").
- Built-In `builtin` - Monitor Built-In parameters.
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
Extra Information for the Parameter Execute DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
