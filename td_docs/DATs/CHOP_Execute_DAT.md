---
url: https://docs.derivative.ca/CHOP_Execute_DAT
category: DATs
title: CHOP_Execute_DAT
---

# CHOP Execute DAT
## Summary

The CHOP Execute DAT will run its script when the channel values of a specified CHOP change. You can specify which channels to look at, and trigger based on their values changing in various ways. The script gets called for every sample that changes, so when rendering one frame, it may get called 2 or more times per channel, depending on how many frames forward TouchDesigner has stepped (see [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing")).
CHOP Execute DATs are created with [default python method placeholders](https://docs.derivative.ca/ChopexecuteDAT_Class "ChopexecuteDAT Class"). For each monitored condition in the parameters, there is a matching python method in the DAT. When a condition is turned on in the parameters, each time that condition is satisfied the corresponding python method will be executed.
[chopexecuteDAT_Class](https://docs.derivative.ca/ChopexecuteDAT_Class "ChopexecuteDAT Class")

## Parameters - CHOP Execute Page
- Active `active` - While on, the DAT will respond to the CHOP that is referenced.
- Execute from `executeloc` - ⊞ - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) Determines the location the script is run from.
  * Current Node `current` - ([Tscript](https://docs.derivative.ca/Operator_Language "Operator Language") only) The script is executed from the current node location.
  * This Node `here` - The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
  * Specified Operator `op` - The script is executed from the component specified in the Component parameter below.

- From Operator `fromop` - The path that the script will be executed from if the Execute From parameter is set to _Specified Operator_.
- CHOP `chop` - The CHOP whose channel change will trigger the DAT to execute its script.
- Channel `channel` - Which channel will trigger change.
- Off to On `offtoon` - The onOffToOn() method executes when the channel specified switches from off to on, called at the first "on" frame.
- While On `whileon` - The whileOn() method executes when the channel specified is on. It is called once each frame.
- On to Off `ontooff` - The onOnToOff() method executes when the channel specified switches from on to off, called at the first "off" frame.
- While Off `whileoff` - The whileOff() method executes when the channel specified is off. It is called once each frame.
- Value Change `valuechange` - The onValueChange() method executes when the channel specified changes value in any way. It is called once each frame.
- While Off/On Frequency `freq` - ⊞ - Enabled when using the While On or While Off options above. Determines if the DAT executes For Every Sample or Once Per Frame.
  * Execute For Every Sample `everysample` -
  * Execute Once Per Frame `onceperframe` -

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
Extra Information for the CHOP Execute DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
