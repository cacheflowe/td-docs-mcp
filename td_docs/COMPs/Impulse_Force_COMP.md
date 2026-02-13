---
url: https://docs.derivative.ca/Impulse_Force_COMP
category: COMPs
title: Impulse_Force_COMP
---

# Impulse Force COMP
## Summary

An Impulse Force COMP will create a force in the simulation that can be applied for 1 frame using the Pulse Force parameter. In the real world, impulse forces are forces applied over a very short duration, however in [Bullet](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics") this is somewhat simplified, and they are instead applied instantly (for a single frame). Examples of impulse forces are kicking a ball or shooting a cannon. The velocities of the affected bodies are changed in an instant by the impulse force, and after that instant the force no longer has an effect unless applied again.
The resulting velocity of the bodies after the impulse force is applied is the same as the [Force COMP](https://docs.derivative.ca/Force_COMP "Force COMP") with the same values if the Force COMP is applied for exactly 1 second. For example, if 10N of Impulse Force is applied to a body with mass 5kg then the resulting velocity will be 10N / 5kg * 1sec = 2m/s.
See also: [Bullet Dynamics](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics"), [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP"), [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"), [Force COMP](https://docs.derivative.ca/Force_COMP "Force COMP"), [Constraint COMP](https://docs.derivative.ca/Constraint_COMP "Constraint COMP"), [Bullet Solver CHOP](https://docs.derivative.ca/Bullet_Solver_CHOP "Bullet Solver CHOP").
[impulseforceCOMP_Class](https://docs.derivative.ca/ImpulseforceCOMP_Class "ImpulseforceCOMP Class")

## Parameters - Force Page
- Pulse Force `pulse` - Pulse for the impulse force. When pulsed, on the next frame it will apply the impulse force.
- Force `force` - ⊞ - The linear force in Newtons to be applied when the node is pulsed.
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
- Global Shortcut `opshortcut` - Specifies a name you can use anywhere at all as the path to that component. See [Global OP Shortcut](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut").
- Shortcut `iop0shortcut` - Specifies a name you can use anywhere inside the component as a path to "Internal OP" below. See [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").
- OP `iop0op` - The path to the Internal OP inside this component. See [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").
- Node View `nodeview` - ⊞ - Determines what is displayed in the node viewer, also known as the [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer"). Some options will not be available depending on the Component type ([Object Component](https://docs.derivative.ca/Object_Component "Object Component"), [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component"), Misc.)
  * Default Viewer `default` - Displays the default viewer for the component type, a 3D Viewer for Object COMPS and a Control Panel Viewer for Panel COMPs.
  * Operator Viewer `opviewer` - Displays the node viewer from any operator specified in the Operator Viewer parameter below.

- Operator Viewer `opviewer` - Select which operator's node viewer to use when the Node View parameter above is set to Operator Viewer.
- Keep in Memory `keepmemory` - Used only for [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component") this keeps the panel in memory to it doesn't reload every time it is displayed.
- Enable Cloning `enablecloning` - Control if the OP should be actively cloneing. Turning this off causes this node to stop cloning it's 'Clone Master'.
- Enable Cloning Pulse `enablecloningpulse` - Instantaneously clone the contents.
- Clone Master `clone` - Path to a component used as the Master [Clone](https://docs.derivative.ca/Clone "Clone").
- Load on Demand `loadondemand` - Loads the component into memory only when required. Good to use for components that are not always used in the project.
- External .tox `externaltox` - Path to a `.tox` file on disk which will source the component's contents upon start of a `.toe`. This allows for components to contain networks that can be updated independently. If the `.tox` file can not be found, whatever the `.toe` file was saved with will be loaded.
- Reload .tox on Start `reloadtoxonstart` - When on (default), the external .tox file will be loaded when the .toe starts and the contents of the COMP will match that of the external .tox. This can be turned off to avoid loading from the referenced external .tox on startup if desired (the contents of the COMP are instead loaded from the .toe file). Useful if you wish to have a COMP reference an external .tox but not always load from it unless you specifically push the Re-Init Network parameter button.
- Reload Custom Parameters `reloadcustom` - When this checkbox is enabled, the values of the component's [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters") are reloaded when the [.tox](https://docs.derivative.ca/.tox ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](https://docs.derivative.ca/.tox ".tox").
- Reload Built-In Parameters `reloadbuiltin` - When this checkbox is enabled, the values of the component's built-in parameters are reloaded when the [.tox](https://docs.derivative.ca/.tox ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](https://docs.derivative.ca/.tox ".tox").
- Save Backup of External `savebackup` - When this checkbox is enabled, a backup copy of the component specified by the External `.tox` parameter is saved in the `.toe` file. This backup copy will be used if the External `.tox` can not be found. This may happen if the `.tox` was renamed, deleted, or the `.toe` file is running on another computer that is missing component media.
- Sub-Component to Load `subcompname` - When loading from an External `.tox` file, this option allows you to reach into the `.tox` and pull out a COMP and make that the top-level COMP, ignoring everything else in the file (except for the contents of that COMP). For example if a `.tox` file named `project1.tox` contains `project1/geo1`, putting `geo1` as the Sub-Component to Load, will result in `geo1` being loaded in place of the current COMP. If this parameter is blank, it just loads the `.tox` file normally using the top level COMP in the file.
- Re-Init Network `reinitnet` - This button will re-load from the external `.tox` file (if present), followed by re-initializing itself from its master, if it's a clone.
