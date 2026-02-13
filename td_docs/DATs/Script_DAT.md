---
url: https://docs.derivative.ca/Script_DAT
category: DATs
title: Script_DAT
---

# Script DAT
## Summary

The Script DAT runs a script each time the DAT cooks and can build/modify the output table based in the optional input tables. The Script DAT is created with a [docked](https://docs.derivative.ca/Docking "Docking") (attached) DAT that contains three Python methods: `cook`, `onPulse`, and `setupParameters`. The `cook` method is run each time the Script DAT cooks. The `setupParameters` method is run whenever the Setup Parameter button on the Script page is pressed. The `onPulse` method is run whenever a custom pulse parameter is pushed.
Refer to Help -> Python Examples, and Help -> [Operator Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets").
Note: Because the Script DAT can get data from anywhere, it's difficult to determine what it procedurally depends on. So every time that any Script OP runs it will add to a list of operators, parameters, nodes etc that it depends upon, and when they change, the Script OP will re-cook. The list is reset when a `.toe` restarts.
See also: [Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Script TOP](https://docs.derivative.ca/Script_TOP "Script TOP")
[scriptDAT_Class](https://docs.derivative.ca/ScriptDAT_Class "ScriptDAT Class")

## Parameters - Script Page
- Callbacks DAT `callbacks` - Specifies the DAT which holds the callbacks. See [scriptDAT_Class](https://docs.derivative.ca/ScriptDAT_Class "ScriptDAT Class") for usage.
- Setup Parameters `setuppars` - Clicking the button runs the `setupParameters()` callback function.

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
Extra Information for the Script DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
