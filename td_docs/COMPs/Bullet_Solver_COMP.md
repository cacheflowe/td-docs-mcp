---
url: https://docs.derivative.ca/Bullet_Solver_COMP
category: COMPs
title: Bullet_Solver_COMP
---

# Bullet Solver COMP
## Summary

In a [Bullet Dynamics](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics") system, the Bullet Solver COMP is analogous to the world/simulation in which actors/bodies (ie. [Actor COMPs](https://docs.derivative.ca/Actor_COMP "Actor COMP")) operate. A Bullet Solver COMP contains any number of actors/bodies (Actor COMPs) or forces ([Force COMP](https://docs.derivative.ca/Force_COMP "Force COMP")/[Impulse Force COMP](https://docs.derivative.ca/Impulse_Force_COMP "Impulse Force COMP")), and as the name suggests it also uses the [Bullet Physics API](https://pybullet.org/wordpress/) to step through the simulation.
The Bullet Solver COMP runs a Bullet simulation based on some simulation parameters (eg. linear multiplier or angular multiplier) and updates the transformations of the Actor COMPs contained within it as the simulation progresses forward. The simulation can be paused, slowed down, sped up, or restarted using the parameters on the COMP.
The Bullet Solver COMP simulation operates in a vacuum, so there will be no air resistance applied to any actors in the simulation. The simulation is stepped at the given sample rate, and the Actor COMP transform is updated accordingly. These transformations are the same results displayed in the [Bullet Solver CHOP](https://docs.derivative.ca/Bullet_Solver_CHOP "Bullet Solver CHOP").
The Actor COMPs referenced by the Bullet Solver COMP do not need to be inside its network. They can be anywhere as long as they are not already referenced by another Bullet Solver COMP.
See also: [Bullet Dynamics](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics"), [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"), [Force COMP](https://docs.derivative.ca/Force_COMP "Force COMP"), [Impulse Force COMP](https://docs.derivative.ca/Impulse_Force_COMP "Impulse Force COMP"), [Constraint COMP](https://docs.derivative.ca/Constraint_COMP "Constraint COMP"), [Bullet Solver CHOP](https://docs.derivative.ca/Bullet_Solver_CHOP "Bullet Solver CHOP").
[bulletsolverCOMP_Class](https://docs.derivative.ca/BulletsolverCOMP_Class "BulletsolverCOMP Class")

## Parameters - Solver Page
- Actors `actors` - The Actor COMPs to include in the simulation. These actors cannot already be a part of another Bullet Solver COMP.
- Global Forces `forces` - The Force COMPs to include in the simulation. These forces are global forces and will be applied to all non-static actors in the simulation.
- Gravitational Acceleration `gravity` - ⊞ - Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass.
  * X `gravityx` -
  * Y `gravityy` -
  * Z `gravityz` -

- Dimension `dimension` - ⊞ - The dimension of the simulation. The options in this menu can also be recreated using the linear/angular multiplier parameters.
  * 1D `1d` - Actor is constrained to linear velocity only on the X axis, with no angular velocity (linmult 1,0,0 and angmult 0,0,0)
  * 2D `2d` - Actor is constrained to linear velocity only on the XY plane, with angular velocity only around the Z axis (linmult 1,1,0 and angmult 0,0,1)
  * 3D `3d` - Actor is not constrained and can move in any direction: X, Y, or Z. Similarly, the Actor can also rotate in any direction: X, Y, or Z (linmult 1,1,1 and angmult 1,1,1)

- Linear Multiplier `linmult` - ⊞ - A multiplier for the linear velocities of the actors in the simulation. For example, if linmult is (0, 1, 1) then the actors can move linearly at normal speed on the Y and Z axes but cannot move in the X direction. These values are multiplied internally by the values from dimension. For example, if the dimension is 2D and linmult is (0, 1, 1) then the only direction the actors can move is along the Y axis because 2D is constraining on the Z and this parameter is constraining on the Y.
  * X `linmultx` -
  * Y `linmulty` -
  * Z `linmultz` -

- Angular Multiplier `angmult` - ⊞ - A multiplier for the angular velocities of the actors in the simulation. For example, if angmult is (1, 0, 0) then the actors can only rotate on the X axes. These values are multiplied internally by the values from dimension. So, if dimension is 2D and angmult is (1, 0, 0) then the actor will not be able to rotate in any direction because 2D constrains rotation only to the Z axis, and this parameter is constraining it only to the X axis.
  * X `angmultx` -
  * Y `angmulty` -
  * Z `angmultz` -

- Initialize Sim and Collision Shapes `initall` - Resets all bodies to their initial state (ie. position, orientation, velocity) and recreates their collision shapes. This parameter is equivalent to pulsing each Actor COMP's "Initialize Actor". Creating collision shapes can be time consuming in certain cases, so if it's not need then Initialize Sim should be used instead. Collision shapes need to be recreated if any of the SOPs used to create the collision shape change, or if the instancing OP changes.
- Initialize Sim `init` - Reset all bodies to their initial state (ie. position, orientation, velocity). This will not begin stepping through the simulation, it will only initialize. **NOTE:** This will not reset the collision shapes of any Actor COMPs, "Initialize Sim and Collision Shapes" above or "Initialize Actor" on the Actor COMP should be used for that.
- Start Sim `start` - Initialize the simulation and run it (begin stepping).
- Play `play` - Play the simulation. Will step through the simulation when toggled on, but will not when it is toggled off (ie. it will be paused).
- Sample Rate `rate` - The sample rate of the simulation. The sample rate affects the timestep, which is 1/rate
- Simulation Speed `simspeed` - The speed of the simulation. It is a multiplier for the size of the timestep to slow down or speed up the simulation.
- Feedback CHOP `feedback` - (see also: [Bullet Solver CHOP](https://docs.derivative.ca/Bullet_Solver_CHOP "Bullet Solver CHOP")) A reference to a CHOP to feedback. The Bullet Solver COMP will take the transform/velocity channels from the CHOP and override the respective actor's transform or velocity at the beginning of the next simulation step.
If you feedback a Bullet Solver CHOP that has no change to the channel values in it, the simulation will act as normal as nothing is being overriden. This allows you do things like the example below. For example, to negate the velocity of every actor in a simulation you could use a Bullet Solver CHOP, put that into a Switch CHOP with the second input being the same CHOP only with the velocity channels negated. Then export a button pulse to the switch index and put the Switch CHOP into the Feedback CHOP parameter. Then, when the button is pressed for a single frame (pulsed) the velocities will be overridden and negated. The only channels required to feedback are the actor_id and body_id channels, all other channels are optional. The channel names should all be the same as in the Bullet Solver CHOP. In addition to the channels outputted in the Bullet Solver CHOP, force and torque can also be used. The channel names are **force[xyz]** and **torque[xyz]**. **NOTE:** scale cannot be used for feedback.
- Perform Contact Test `contacttest` - Enables contact testing for all bodies in the simulation. Contact testing is used for the colliding and total_collisions channels on the Bullet Solver CHOP. Without this parameter enabled those channel values will not update. **NOTE:** Contact testing can be slow for lots of bodies.
- Always Simulate `alwayssim` - When enabled the Bullet Solver COMP will simulate (ie. cook) every frame.
- Callbacks DAT `callbacks` - A reference to a DAT with python callbacks. The available callbacks are: `onCollision(solverComp, collisions)`, `onFrameStart(solverComp)`, `onFrameEnd(solverComp)`, `onInit(solverComp)`, `onStart(solverComp)`. A DAT with these callbacks will be automatically created and referenced when a Bullet Solver COMP is created. `onCollision(solverComp, collisions)` passes a list of all collisions occuring, and requires that Perform Contact test be enabled. `collisions` is a list of named tuples (`bodyA` and `bodyB`). `bodyA` and `bodyB` are the two bodies participating in the collision. `bodyA` and `bodyB` are Python Body Objects (see [Body Class](https://docs.derivative.ca/Body_Class "Body Class")).
## Parameters - Xform Page
The Xform parameter page controls the object component's transform in world space.
- Transform Order `xord` - ⊞ - This allows you to specify the order in which the changes to your Component will take place. Changing the Transform Order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as `T * R * S * Position`.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - This allows you to set the transform order for the Component's rotations. As with transform order (above), changing the order in which the Component's rotations take place will alter the Component's final position. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows `R = Rz * Ry * Rx`
  * Rx Ry Rz `xyz` - `R = Rz * Ry * Rx`
  * Rx Rz Ry `xzy` - `R = Ry * Rz * Rx`
  * Ry Rx Rz `yxz` - `R = Rz * Rx * Ry`
  * Ry Rz Rx `yzx` - `R = Rx * Rz * Ry`
  * Rz Rx Ry `zxy` - `R = Ry * Rx * Rz`
  * Rz Ry Rx `zyx` - `R = Rx * Ry * Rz`

- Translate `t` - ⊞ - This allows you to specify the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - Theis specifies the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - This specifies the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - The Pivot point edit fields allow you to define the point about which a Component scales and rotates. Altering the pivot point of a Component produces different results depending on the transformation performed on the Component.
For example, during a scaling operation, if the pivot point of an Component is located at `-1, -1, 0` and you wanted to scale the Component by `0.5` (reduce its size by 50%), the Component would scale toward the pivot point and appear to slide down and to the left.
[![Objects17.gif](https://docs.derivative.ca/images/6/60/Objects17.gif)](https://docs.derivative.ca/File:Objects17.gif)
In the example above, rotations performed on an Component with different pivot points produce very different results.
  * X `px` -
  * Y `py` -
  * Z `pz` -

- Uniform Scale `scale` - This field allows you to change the size of an Component uniformly along the three axes.

> **Note:** Scaling a camera's channels is not generally recommended. However, should you decide to do so, the rendered output will match the Viewport as closely as possible when scales are involved.

- Parent Transform Source `parentxformsrc` - ⊞ - _**NOTE:** This parameter replaces the previous '**Constrain To'** parameter._ Use 'Parent Transform Source' and to specify what initial position is used for this object. Can be one of "Parent (Hierarchy)", "Specify Parent Object", or "World Origin".
  * From Parent Object (Hierarchy) `hierarchy` -
  * Specify Parent Object `specify` -
  * World Origin `worldorigin` -

- Parent Object `parentobject` - Allows the location of the object to be constrained to any other object whose path is specified in this parameter.
- Look At `lookat` - Allows you to orient this Component by naming another 3D Component you would like it to Look At, or point to. Once you have designated this Component to look at, it will continue to face that Component, even if you move it. This is useful if, for instance, you want a camera to follow another Component's movements. The Look At parameter points the Component in question at the other Component's origin.

> **Tip:** To designate a center of interest for the camera that doesn't appear in your scene, create a Null Component and disable its display flag. Then Parent the Camera to the newly created Null Component, and tell the camera to look at this Component using the Look At parameter. You can direct the attention of the camera by moving the Null Component with the Select state. If you want to see both the camera and the Null Component, enable the Null Component's display flag, and use the Select state in an additional Viewport by clicking one of the icons in the top-right corner of the TouchDesigner window.

- Forward Direction `forwarddir` - ⊞ - Sets which axis and direction is considered the forward direction.
  * +X `posx` -
  * -X `negx` -
  * +Y `posy` -
  * -Y `negy` -
  * +Z `posz` -
  * -Z `negz` -

- Look At Up Vector `lookup` - ⊞ - When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat Component, for example, passes through the Y axis of the target Component.
  * Don't Use Up Vector - Use this option if the look at Component does not pass through the Y axis of the target Component.
  * Use Up Vector - This precisely defines the rotates on the Component doing the looking. The Up Vector specified should not be parallel to the look at direction. See Up Vector below.
  * Use Quaternions - Quaternions are a mathematical representation of a 3D rotation. This method finds the most efficient means of moving from one point to another on a sphere.
  * Don't use up vector `off` -
  * Use up vector `on` -
  * Use quaternions `quat` -
  * Use Roll `roll` -

- Path SOP `pathsop` - Names the SOP that functions as the path you want this Component to move along. For instance, you can name a SOP that provides a path for the camera to follow.
- Roll `roll` - Using the angle control you can specify a Component's rotation as it animates along the path.
- Position `pos` - This parameter lets you specify the Position of the Component along the path. The values you can enter for this parameter range from `0` to `1`, where `0` equals the starting point and `1` equals the end point of the path. The value slider allows for values as high as `10` for multiple "passes" along the path.
- Orient along Path `pathorient` - If this option is selected, the Component will be oriented along the path. The positive Z axis of the Component will be pointing down the path.
- Orient Up Vector `up` - ⊞ - When orienting a Component, the Up Vector is used to determine where the positive Y axis points.
  * X `upx` -
  * Y `upy` -
  * Z `upz` -

- Auto-Bank Factor `bank` - The Auto-Bank Factor rolls the Component based on the curvature of the path at its current position. To turn off auto-banking, set the bank scale to `0`.

## Parameters - Pre-Xform Page
The Pre-Xform parameter page applies a transform to the object component the same way connecting another [Object](https://docs.derivative.ca/Object "Object") as a parent of this node does. The transform is applied to the left of the [Xform](https://docs.derivative.ca/Object_COMP_Xform_Page "Object COMP Xform Page") page's parameters. In terms of matrix math, if we use the 'multiply on the right' (column vector) convention, the equation would be `preXForm * xform * Position`.
- Apply Pre-Transform `pxform` - Enables the transformation on this page.
- Transform Order `pxord` - ⊞ - Refer to the documentation on Xform page for more information.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `prord` - ⊞ - Refer to the documentation on Xform page for more information.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `pt` - ⊞ - Refer to the documentation on Xform page for more information.
  * X `ptx` -
  * Y `pty` -
  * Z `ptz` -

- Rotate `pr` - ⊞ - Refer to the documentation on Xform page for more information.
  * X `prx` -
  * Y `pry` -
  * Z `prz` -

- Scale `ps` - ⊞ - Refer to the documentation on Xform page for more information.
  * X `psx` -
  * Y `psy` -
  * Z `psz` -

- Pivot `pp` - ⊞ - Refer to the documentation on Xform page for more information.
  * X `ppx` -
  * Y `ppy` -
  * Z `ppz` -

- Uniform Scale `pscale` - Refer to the documentation on Xform page for more information.
- Reset Transform `preset` - This button will reset this page's transform so it has no translate/rotate/scale.
- Commit to Main Transform `pcommit` - This button will copy the transform from this page to the main Xform page, and reset this page's transform.
- Xform Matrix/CHOP/DAT `xformmatrixop` - This parameter can be used to transform using a 4x4 matrix directly. For information on ways to specify a matrix directly, refer to the [Matrix Parameters](https://docs.derivative.ca/Matrix_Parameters "Matrix Parameters") page. This transform will be applied after the regular Pre-Transform transformation. That is, it'll be applied in the oder XformMatrix * PreXForm * Position.

## Parameters - Render Page
The Display parameter page controls the component's [material](https://docs.derivative.ca/index.php?title=Material&action=edit&redlink=1 "Material \(page does not exist\)") and [rendering](https://docs.derivative.ca/Rendering "Rendering") settings.
- Material `material` - Selects a [MAT](https://docs.derivative.ca/MAT "MAT") to apply to the geometry inside.
- Render `render` - Whether the Component's geometry is visible in the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP"). This parameter works in conjunction (logical AND) with the Component's [Render Flag](https://docs.derivative.ca/Render_Flag "Render Flag").
- Draw Priority `drawpriority` - Determines the order in which the Components are drawn. Smaller values get drawn after larger values. The value is compared with other Components in the same parent Component, or if the Component is the top level one listed in the Render TOP's 'Geometry' parameter, then against other top-level Components listed there. This value is most often used to help with [Transparency](https://docs.derivative.ca/Transparency "Transparency").
- Pick Priority `pickpriority` - When using a [Render Pick CHOP](https://docs.derivative.ca/Render_Pick_CHOP "Render Pick CHOP") or a [Render Pick DAT](https://docs.derivative.ca/Render_Pick_DAT "Render Pick DAT"), there is an option to have a 'Search Area'. If multiple objects are found within the search area, the pick priority can be used to select one object over another. A higher value will get picked over a lower value. This does not affect draw order, or objects that are drawn over each other on the same pixel. Only one will be visible for a pick per pixel.
- Wireframe Color `wcolor` - ⊞ - Use the R, G, and B fields to set the Component's color when displayed in wireframe shading mode.
  * Red `wcolorr` -
  * Green `wcolorg` -
  * Blue `wcolorb` -

- Light Mask `lightmask` - By default all lights used in the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") will affect geometry renderer. This parameter can be used to specify a sub-set of lights to be used for this particular geometry. The lights must be listed in the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") as well as this parameter to be used.

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

- Parameter Color Space `parmcolorspace` - ⊞ - Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space.
  * sRGB `srgb` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
  * sRGB - Linear `srgblinear` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.601 (NTSC) `rec601ntsc` - [Rec.601](https://en.wikipedia.org/wiki/Rec._601) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.709 `rec709` - [Rec.709](https://en.wikipedia.org/wiki/Rec._709) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.2020 `rec2020` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 `dcip3` - [DCI-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 (D60) `dcip3d60` - [DCI-P3 "D60 sim"](https://en.wikipedia.org/wiki/DCI-P3) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) `displayp3d65` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACES2065-1 `aces2065-1` - [ACES 2065-1](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACEScg `acescg` - [ACEScg](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Passthrough `passthrough` - When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.

- Parameter Reference White `parmreferencewhite` - ⊞ - When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space selected.
  * Use Parent Panel `useparent` - Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
  * Standard (SDR) `sdr` - Will treat the Parameter Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Parameter Color Space as HDR for it's reference white value.
  * UI `ui` - Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## Info CHOP Channels
Extra Information for the Bullet Solver COMP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Bullet Solver COMP Info Channels
  * initializing -

  * ready -

  * running -

  * done -

  * timer_fraction -

  * timer_seconds -

  * timer_index -

  * playing_seconds -

  * running_seconds -

  * length_seconds -

  * sample_rate -

  * index -

  * num_bodies -

  * num_active_bodies -

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
