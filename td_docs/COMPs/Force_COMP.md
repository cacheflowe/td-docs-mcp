---
url: https://docs.derivative.ca/Force_COMP
category: COMPs
title: Force_COMP
---

# Force COMP
## Summary

Force COMPs are used to added forces to a physics solver's simulation. [Bullet](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics") supports linear/rotational forces and impulse forces (see Force page) and [Flex](https://docs.derivative.ca/Flex "Flex") supports force fields (see Force Field page).
###
Active Force
Active forces are enabled using the Active toggle parameter on the Force page.
An active force will create a force in the simulation that is applied over time. An active force can either be applied globally by being referenced on the [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP"), or it can be applied locally by being referenced on an individual [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"). The active force applies its force each frame, and the force applied over 1 second is equivalent to an impulse force of the same value applied in a single frame.
The units for the force and torque parameters are in Newtons (N), equivalent to kg*m/s^2. This means that if a force of 10N is applied to an actor with mass equal to 5kg and no initial velocity, then after 1 second the velocity of that actor will be 2m/s => 10N / 5kg * 1 sec = 2m/s. If all the parameters were the same, but instead it was an impulse force, then the velocity would still be 2m/s. However, the impulse force's velocity would change instantaneously and stop increasing (unless pulsed again) whereas with the active force the velocity will continue to increase after 1 second.
The center of mass is assumed to be center of the bounding box of the mass. By default, if a body is not constrained and not colliding, the force will not cause the body to rotate, unless the Relative Position parameter is set to a non-zero value. If Relative Position is set to +1 in X and the force is +1 in Y, it will cause the body to rotate counter-clockwise around the Z-axis and translate in Y.
If the Torque is set to +1 in Z, it will cause the body to only rotate counter-clockwise in the Z-axis (a positive Z rotation), and not translate.
To apply force/torque to specific bodies use a Feedback CHOP (see [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP") or [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP")) and **force[xyz]** and **torque[xyz]** channels.
###
Impulse Force
Impulse forces are applied through the Impulse Force pulse parameter.
An impulse force pulse will create a force in the simulation that is applied for 1 frame. In the real world, impulse forces are forces applied over a very short duration, however in [Bullet](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics") this is somewhat simplified, and they are instead applied instantly (for a single frame). Examples of impulse forces are kicking a ball or shooting a cannon. The velocities of the affected bodies are changed in an instant by the impulse force, and after that instant the force no longer has an effect unless applied again.
The resulting velocity of the bodies after the impulse force is applied is the same as an active force with the same values if the active force is applied for exactly 1 second. For example, if 10N of impulse force is applied to a body with mass 5kg then the resulting velocity will be 10N / 5kg * 1sec = 2m/s.
###
Force Field
Force fields are enabled through the Active parameter on the Force Field page.
Force fields are spherical with a radius defined through the Radius parameter. Positive strength pushes bodies outward and negative strength pulls bodies inward.

See also: [Flex](https://docs.derivative.ca/Flex "Flex"), [Bullet Dynamics](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics"), [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP"), [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"), [Constraint COMP](https://docs.derivative.ca/Constraint_COMP "Constraint COMP"), [Bullet Solver CHOP](https://docs.derivative.ca/Bullet_Solver_CHOP "Bullet Solver CHOP"), [Nvidia Flex TOP](https://docs.derivative.ca/Nvidia_Flex_TOP "Nvidia Flex TOP"), [Nvidia Flex Solver COMP](https://docs.derivative.ca/Nvidia_Flex_Solver_COMP "Nvidia Flex Solver COMP").
[forceCOMP_Class](https://docs.derivative.ca/ForceCOMP_Class "ForceCOMP Class")

## Parameters - Force Page
- Active `active` - Toggle the active force on/off in the simulation
- Force `force` - ⊞ - The linear force in Newtons that will be applied.
  * X `forcex` -
  * Y `forcey` -
  * Z `forcez` -

- Relative Position `relpos` - ⊞ - The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque.
  * X `relposx` -
  * Y `relposy` -
  * Z `relposz` -

- Torque `torque` - ⊞ - The rotational force in Newtons that will be applied.
  * X `torquex` -
  * Y `torquey` -
  * Z `torquez` -

- Impulse Force `impulse` - Applies an impulse force in the simulation for 1 frame with the above parameters.
## Parameters - Force Field Page
- Active `ffactive` - Toggle the force field on/off in the simulation
- Strength `strength` - The strength of the force field. Positive strength pushes bodies outward and negative strength pulls bodies inward.
- Radius `radius` - The radius of the force field.
- Linear Falloff `falloff` - Applies linear falloff to the strength of the force field based on the distance from the center.

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
- Node View `nodeview` - ⊞ - Determines what is displayed in the node viewer, also known as the [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer"). Some options will not be available depending on the Component type ([Object Component](https://docs.derivative.ca/Object_Component "Object Component"), [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component"), Misc.)
  * Default Viewer `default` - Displays the default viewer for the component type, a 3D Viewer for Object COMPS and a Control Panel Viewer for Panel COMPs.
  * Operator Viewer `opviewer` - Displays the node viewer from any operator specified in the Operator Viewer parameter below.

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
Extra Information for the Force COMP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
