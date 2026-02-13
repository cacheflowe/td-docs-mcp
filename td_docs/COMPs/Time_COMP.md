---
url: https://docs.derivative.ca/Time_COMP
category: COMPs
title: Time_COMP
---

# Time COMP
## Summary

The Time Component allows each component to have its own timeline (clock). The Time Component contains a network of operators that can drive a [Timeline](https://docs.derivative.ca/Timeline "Timeline"), drive animations in [Animation COMPs](https://docs.derivative.ca/Animation_COMP "Animation COMP"), or be used to drive any custom time-based system. The Time Component's parameters define the speed, range, various options for the time system.
The Time Component is often used in TouchDesigner to allow a component to have its own timeline / clock, this is called [Component Time](https://docs.derivative.ca/Component_Time "Component Time"). It is useful for holding some parts of your system stationary while others are allowed to play forward. A Time Component's location must be in the `/local` network of a [Component](https://docs.derivative.ca/Component "Component") for the Time Component to create a **Component Time**.
To add Component Time to a component, right-click on the component and select **Add Component Time...** from the popup menu, this will add the following Time Component `/_comppath_/local/time`.
The Time Component's predefined network is [Cloned](https://docs.derivative.ca/Clone "Clone") from Master Component `/sys/local/time`. The Time Component's network can be modified if the path in the Clone parameter is removed.
[timeCOMP_Class](https://docs.derivative.ca/TimeCOMP_Class "TimeCOMP Class")

## Parameters - Time Page
- Play `play` - Controls the playback of the Time Component. 0 = stop, 1 = play.
- Rate `rate` - Sets the frame per second for the Time Component.
- Start `start` - Sets the start frame for the Time Component. The **Start** and **End** parameters determine the overall length of the Time Component.
- End `end` - Sets the end frame for the Time Component. The **Start** and **End** parameters determine the overall length of the Time Component.
- Range Limit `rangelimit` - ⊞ - This menu controls how the playback loops:
  * Loop `loop` - The timeline will loop when it reaches Range End frame.
  * Hold `hold` - The timeline will stop (hold) when it reaches Range End frame.

- Range Start `rangestart` - Sets the start frame of the working range. The working range is a subset of the start/end range which can be used to focus work on a smaller section of time. The playhead will only playback the frames/beats that are inside this working range.
- Range End `rangeend` - Sets the end frame of the working range. The working range is a subset of the start/end range which can be used to focus work on a smaller section of time. The playhead will only playback the frames/beats that are inside this working range.
- Reset Frame `resetframe` - Place holder to specify which frame to jump to (Obsolete).
- Signature `signature` - ⊞ - Specifies the time signature. The first number is the number of beats per measure and the second number indicates the type of note that constitutes one beat. See [Time Signature - Wikipedia](http://en.wikipedia.org/wiki/Time_signature) for additional information.
  * `signature1` -
  * `signature2` -

- Tempo `tempo` - Sets the bpm for the Time Component.
- Run Independently `independent` - When checked on, this Time COMP's time will not be dependant on parent Time Components found in the network hierarchy. For example, starting/pausing other Time COMP's higher in the hierarchy will not start/pause a Time COMP whose **Run Independently** parameter is on.

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

## Info CHOP Channels
Extra Information for the Time COMP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Time COMP Info Channels
  * fps -

  * start -

  * end -

  * rstart -

  * rend -

  * bpm -

  * sig1 -

  * sig2 -

  * play -

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
