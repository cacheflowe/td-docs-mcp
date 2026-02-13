---
url: https://docs.derivative.ca/Animation_COMP
category: COMPs
title: Animation_COMP
---

# Animation COMP
## Summary

The Animation Component is a special component used for creating keyframe animation channels. The component contains a pre-defined network utilizing a [Keyframe CHOP](https://docs.derivative.ca/Keyframe_CHOP "Keyframe CHOP") and a number of [Table DATs](https://docs.derivative.ca/Table_DAT "Table DAT") to define the animated [CHOP](https://docs.derivative.ca/CHOP "CHOP") channels.
The [Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor") is the user interface for creating and editing the animation of the Animation Component.
The Animation Component has both in and out CHOP connectors.
**Animation Component Inputs**
With no input connected, the Animation Component's index loops over the time range of the channels. The CHOP input can be used to manually control the index of the animated channels. For example, if the channels are keyed from frame 1 to 600, you can connect an input to the component and manually drive the animation output by feeding it a number between 1 and 600 (indexes outside the range will use the channel extend conditions).
Using the Keyframe CHOP's Index Units menu, you can drive the animation with numbers expressed in seconds, samples, or a fraction where 0 is the start and 1 is the end.
**Animation Component Outputs**
The CHOP output gives access to the animation channel's current value. CHOPs can be directly connected or a [Null CHOP](https://docs.derivative.ca/Null_CHOP "Null CHOP") may be appended for [exporting](https://docs.derivative.ca/CHOP_Export "CHOP Export") the channels to parameters. The current channel values can also be viewed by turning on the Animation Component's [node viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer").
[![AnimationCOMPTimesliced.png](https://docs.derivative.ca/images/f/fe/AnimationCOMPTimesliced.png)](https://docs.derivative.ca/File:AnimationCOMPTimesliced.png)
[animationCOMP_Class](https://docs.derivative.ca/AnimationCOMP_Class "AnimationCOMP Class")

###
Using the Animation Component
Keyframing any parameter, attribute, or data in TouchDesigner begins with an Animation Component. You can create an Animation COMP from;
  * The [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog")
  * Right-click on any parameter of an OP. **RMB - > Keyframe Parameter in... -> New Animation** to create a new Animation COMP

To open the Animation Editor, right-click on an Animation COMP and select **Edit Animation...** to open that animation in the editor. You can also change any pane to **Animation Editor** type and the Editor will open whilst pointing to the last Animation COMP that was scoped.
Then you can create and keyframe animation channels. Refer to the [Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor") for instructions on keyframing.
[![AnimationCOMPEdit.png](https://docs.derivative.ca/images/a/af/AnimationCOMPEdit.png)](https://docs.derivative.ca/File:AnimationCOMPEdit.png)

## Parameters - Animation Page
- Time Reference `timeref` - The location the Animation COMP looks to for its time information. This is used for default channel range and rate when the Type parameter on the Range page is set to **Timeline**.
- Play Mode `playmode` - ⊞ - Specifies the method used to playback the animation or allows the output the entire animation curve.
  * Locked to Timeline `locked` - This mode locks the animation position to the timeline. Scrubbing or jumping in the timeline will change the animation position accordingly. The parameters Play, Speed, Cue, and Cue Point are disabled in this mode since the timeline is directly controlling the animation's position.
  * Use Input Index `input` - This mode allows the user to specify a particular position in the animation using the index input on the Animation COMP (the CHOP input to the Animation COMP). The Input Index Unit parameter can be used to change the units of the input channel. Use this mode for random access to any location in the animation for maximum flexibility.
  * Sequential `sequential` - This mode continually plays regardless of the timeline position (the Index parameter is disabled). Reset and Speed parameters below are enabled to allow some control.
  * Output Full Range `outputrange` - This option outputs the entire animation channel range. This is useful for using the Animation COMP to create custom lookup curves/channels.

- Play `play` - Animation plays when On and stops when Off. This animation playback control is only available when Play Mode is _Sequential_.
- Speed `speed` - This is a speed multiplier which only works when Play Mode is _Sequential_. A value of 1 is the default playback speed. A value of 2 is double speed, 0.5 is half speed and so on. Negative values will play the animation backwards.
- Cue `cue` - Jumps to Cue Point when set to 1. Only available when Play Mode is Sequential.
- Cue Pulse `cuepulse` - Instantly jumps to the Cue Point.
- Cue Point `cuepoint` - Set any index in the animation as a point to jump to. Only available when Play Mode is Sequential.
- Cue Point Unit `cuepointunit` - Units used when setting the Cue Point parameter.
- Input Index Unit `inputindexunit` - ⊞ - When Play Mode is set to **Use Input Index** use this menu to choose the units for the index input channel. For example, choose between setting the index with frames or seconds. The Units X option sets the index to use the key information directly from the key DAT table inside the Animation COMP, disregarding any custom settings found in the attributes DAT table.
  * Samples `samples` -
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * X Units `xunits` -

- Cyclic Range `cyclic` - ⊞ - Adapts the range of the animation for cyclic or non-cyclic input indices. When using a cyclic input index the lookup value for index 0.0 and 1.0 result in the same value. To avoid this, set Cyclic Range to Yes and the lookup will cycle smoothly.
  * Automatic `auto` - Checks the right extend condition of each channel (Assumes type cycle and mirror are cyclic lookups).
  * Yes `yes` - Cycles the output when index is outside the animation range.
  * No `no` - Does not cycle the output when index is outside the animation range.

- Specify Edit Attributes `specifyedit` - Turn this on to enable the edit attributes parameter below.
- Edit Origin `editorigin` - Changes the origin of the animation channel edits. This does not change the data stored in the key DAT table, but it does effect the channels display in the graph and playback of the animation.
- Edit Rate `editrate` - Changes the rate of the animation channel edits. This does not change the data stored in the key DAT table, but it does effect the channels display in the graph and playback of the animation.
- Edit Animation... `editanimation` - Clicking this button will open this Animation COMP in the Animation Editor.

## Parameters - Range Page
- Type `rangetype` - ⊞ - Set the working range for the Animation COMP.
  * Timeline `timeline` - Uses the range set in the timeline specified by the Time Reference parameter on the previous Animation parameter page.
  * Custom `custom` - Set a custom range using the Start and End parameters below.

- Start `start` - Start of the Custom range, expressed in units seconds, frames or samples.
- Start Unit `startunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- End `end` - End of the Custom range, expressed in units seconds, frames or samples.
- End Unit `endunit` - Select the units to use for this parameter, Samples, Frames, or Seconds.
- Trim Left `tleft` - ⊞ - Determines the output of the channels when past the 'End' position. Does not affect Play Mode = Output Full Range, to manipulate the [Extend Conditions](https://docs.derivative.ca/Extend_Conditions "Extend Conditions") of that mode adjust the Extend parameters of the [Keyframe CHOP](https://docs.derivative.ca/Keyframe_CHOP "Keyframe CHOP") inside the Animation COMP.
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Trim Right `tright` - ⊞ - Determines the output of the channels when before the 'Start' position. Does not affect Play Mode = Output Full Range, to manipulate the [Extend Conditions](https://docs.derivative.ca/Extend_Conditions "Extend Conditions") of that mode adjust the Extend parameters of the [Keyframe CHOP](https://docs.derivative.ca/Keyframe_CHOP "Keyframe CHOP") inside the Animation COMP.
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Trim Default `tdefault` - The value used for the Default Value trim conditio above.

## Parameters - Extensions Page
The Extensions parameter page sets the component's python extensions. Please see [extensions](https://docs.derivative.ca/Extensions "Extensions") for more information.
- Re-Init Extensions `reinitextensions` - Recompile all extension objects. Normally extension objects are compiled only when they are referenced and their definitions have changed.
- Init Extensions On Start `initextonstart` - Perform a Re-Init automatically when TouchDEsigner Starts
- Extension `ext` - Sequence of info for creating extensions on this component
- Object `ext0object` - A number of class instances that can be attached to the component.
- Name `ext0name` - Optional name to search by, instead of the instance class name.
- Promote `ext0promote` - Controls whether or not the extensions are visible directly at the component level, or must be accessed through the `.ext` member. Example: `n.Somefunction` vs `n.ext.Somefunction`

## Parameters - Common Page
The Common parameter page sets the component's [node viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer") and [clone](https://docs.derivative.ca/Clone "Clone") relationships.
- Parent Shortcut `parentshortcut` - Specifies a name you can use anywhere inside the component as the path to that component. See [Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut").
- Global OP Shortcut `opshortcut` - Specifies a name you can use anywhere at all as the path to that component. See [Global OP Shortcut](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut").
- Internal OP `iop` - Sequence header for internal operators.
- Shortcut `iop0shortcut` - Specifies a name you can use anywhere inside the component as a path to "Internal OP" below. See [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").
- OP `iop0op` - The path to the Internal OP inside this component. See [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").
- Operator Viewer `opviewer` - Select which operator's node viewer to use when the Node View parameter above is set to Operator Viewer.
- Enable Cloning `enablecloning` - Control if the OP should be actively cloneing. Turning this off causes this node to stop cloning it's 'Clone Master'.
- Enable Cloning Pulse `enablecloningpulse` - Instantaneously clone the contents.
- Clone Master `clone` - Path to a component used as the Master [Clone](https://docs.derivative.ca/Clone "Clone").
- Load on Demand `loadondemand` - Loads the component into memory only when required. Good to use for components that are not always used in the project.
- Enable External .tox `enableexternaltox` - When on (default), the external .tox file will be loaded when the .toe starts and the contents of the COMP will match that of the external .tox. This can be turned off to avoid loading from the referenced external .tox on startup if desired (the contents of the COMP are instead loaded from the .toe file). Useful if you wish to have a COMP reference an external .tox but not always load from it unless you specifically push the Re-Init Network parameter button.
- Enable External .tox Pulse `enableexternaltoxpulse` - This button will re-load from the external `.tox` file (if present).
- External .tox Path `externaltox` - Path to a `.tox` file on disk which will source the component's contents upon start of a `.toe`. This allows for components to contain networks that can be updated independently. If the `.tox` file can not be found, whatever the `.toe` file was saved with will be loaded.
- Reload Custom Parameters `reloadcustom` - When this checkbox is enabled, the values of the component's [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters") are reloaded when the [.tox](https://docs.derivative.ca/.tox ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](https://docs.derivative.ca/.tox ".tox").
- Reload Built-In Parameters `reloadbuiltin` - When this checkbox is enabled, the values of the component's built-in parameters are reloaded when the [.tox](https://docs.derivative.ca/.tox ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](https://docs.derivative.ca/.tox ".tox").
- Save Backup of External `savebackup` - When this checkbox is enabled, a backup copy of the component specified by the External `.tox` parameter is saved in the `.toe` file. This backup copy will be used if the External `.tox` can not be found. This may happen if the `.tox` was renamed, deleted, or the `.toe` file is running on another computer that is missing component media.
- Sub-Component to Load `subcompname` - When loading from an External `.tox` file, this option allows you to reach into the `.tox` and pull out a COMP and make that the top-level COMP, ignoring everything else in the file (except for the contents of that COMP). For example if a `.tox` file named `project1.tox` contains `project1/geo1`, putting `geo1` as the Sub-Component to Load, will result in `geo1` being loaded in place of the current COMP. If this parameter is blank, it just loads the `.tox` file normally using the top level COMP in the file.
- Relative File Path Behavior `relpath` - ⊞ - Set whether the child file paths within this COMP are relative to the .toe itself or the .tox, or inherit from parent.
  * Use Parent's Behavior `inherit` - Inherit setting from parent.
  * Relative to Project File (.toe) `project` - The path, when specified as a relative path, will be relative to the .toe file.
  * Relative to External COMP File (.tox) `externaltox` - The path, when specified as a relative path, will be relative to the .tox file. When no external COMP file is specified, or when Enable External .tox is not toggled on, this doesn't have any impact.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Animation COMP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common COMP Info Channels
  * num_children - Number of children in this component.

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
