---
url: https://docs.derivative.ca/Clip_DAT
category: DATs
title: Clip_DAT
---

# Clip DAT
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Clip DAT contains information about motion clips that are manipulated by a [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP") and [Clip Blender CHOP](https://docs.derivative.ca/Clip_Blender_CHOP "Clip Blender CHOP"). The Clip DAT can hold any command or script text, which can be triggered based on the settings on the Execute parameter page (This is where the Clip DAT and the Text DAT are different). The Clip DAT's script is triggered by specified clips being played through a [Clip Blender CHOP](https://docs.derivative.ca/Clip_Blender_CHOP "Clip Blender CHOP").
[clipDAT_Class](https://docs.derivative.ca/ClipDAT_Class "ClipDAT Class")

## Parameters - Text Page
- Edit.. `edit` - Clicking this opens a text editor to add/edit/delete text from the DAT.
- File `file` - The path and name of the file to load. Accepts .txt and .dat files. The file can be read in from disk or from the web. Use http:// when specifying a URL.
- Reload File `reload` - When set to 1, reloads the file into the DAT.

## Parameters - Execute Page
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * This Node `here` - The script is executed from the Text DAT itself.
  * Specified Component `comp` - The script is executed from the component specified in the Component parameter below.

- Clip `clip` - Points to the [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP") which will trigger the script when run in a [Clip Blender CHOP](https://docs.derivative.ca/Clip_Blender_CHOP "Clip Blender CHOP").
- Component `component` - The path that the script will be executed from if the Execute From parameter is set to _Specified Component_.
- Execute on Frame (First) `framefirst` - Executes the script once, the first time the specified index of the clip is played in a clipblender. Even if the clip is looping in a clipblender, the script will only be executed once.
- Execute on Frame (Loop) `frameloop` - Executes the script everytime the specified index of the clip is played in a clipblender. When a clip is looping, the script will run each time through the loop.
- Execute on Exit `exit` - Executes the script when a clipblender exits the specified clip.
- Print State `printstate` - Print debug information to the textport.

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
Extra Information for the Clip DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
