---
url: https://docs.derivative.ca/CPlusPlus_DAT
category: DATs
title: CPlusPlus_DAT
---

# CPlusPlus DAT
## Summary

The CPlusPlus DAT allows you to make custom DAT operators by writing your own plugin using C++.
Using the CPlusPlus DAT, you can create either a Table or Text DAT output depending what type you specify at the time of creation. See [Write a CPlusPlus Plugin](https://docs.derivative.ca/Write_a_CPlusPlus_Plugin "Write a CPlusPlus Plugin") and the other articles in the [C++ category](https://docs.derivative.ca/Category:C%2B%2B "Category:C++") for more detailed information on how to make .dll for use with this DAT. Note that regardless of the type of DAT node (i.e. Table or Text), all the names for searching the cells and assigned texts have to be a encoded as a valid UTF-8.
Example for CPlusPlus DAT as a Visual Studio project in Windows are available in `C:/Program Files/Derivative/TouchDesigner/Samples/CPlusPlus/DAT` or your custom TouchDesigner installation folder. (NOTE: On macOS it is here: `TouchDesigner.app/Contents/Resources/tfs/Samples/CPlusPlus/DAT`
**Custom Parameters** - Custom Parameters can be automatically created by the C++ DAT `.dll`. This custom parameter page can be removed, edited, or appended to from within the `setupParameters()` function in CPlusPlusDATExample.cpp. The defined custom parameters can be enabled or disabled depending on whether they are valid for a specific task or not.)
[cplusplusDAT_Class](https://docs.derivative.ca/CplusplusDAT_Class "CplusplusDAT Class")

## Parameters - Load Page
- Plugin Path `plugin` - The path to the plugin you want to load.
- Re-Init Class `reinit` - When this parameter is On 1, it will delete the instance of the class created by the plugin, and create a new one.
- Re-Init Class `reinitpulse` - Instantly reinitialize the class.
- Unload Plugin `unloadplugin` - When this parameter goes above 1, it will delete the instance of the class created by the plugin and unload the plugin. If multiple DATs have loaded the same plugin they will all need to unload it to release the file.
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
Extra Information for the CPlusPlus DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
