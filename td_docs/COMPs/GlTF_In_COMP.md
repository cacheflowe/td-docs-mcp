---
url: https://docs.derivative.ca/GlTF_In_COMP
category: COMPs
title: GlTF_In_COMP
---

# glTF In COMP

## Summary

The glTF In COMP imports meshes, animations, blend shapes, textures from a glTF 2.0 file (.gltf or .glb). glTF 1.0 files are not supported.

There are two main glTF file extensions:
  * _.gltf_ : ASCII formatted JSON structure, often with external texture files stored on disk, and an external .bin file for the buffer data.
  * _.glb_ : A self-contained binary of the JSON scene structure, textures, and buffer data in a single lightweight compressed file.

[glTF (Graphics Library Transmission Format)](https://www.khronos.org/gltf/) is an open-standard 3D file format created by the Khronos Group. It is designed for efficient loading of 3D models, sometimes referred to as the JPEG of 3D file formats. glTF uses JSON format to describe the scene and its structure with accessors to buffers that contain the actual scene data (eg. positions, attributes etc.), which is formatted to allow for seamless GPU copy. The buffer data can either be stored internally (like in the case of .glb files), or externally in a separate .bin file. Because the underlying data is separate from the scene structure, it allows the scene structure to be much more human-readable in its JSON format.

For best render results, it is recommended to select a Working Color Space (rather than Passthrough) in the [Preferences Dialog](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog"). The glTF In COMP has additional color space controls on import with its Geometry Color Space and Materials Color Space parameters. See also: [Color Space Workflows](../Interoperability/Color_Space_Workflows.md "Color Space Workflows").

### Importing

The glTF In COMP imports only a single scene. For importing of multiple scenes within a single project, multiple glTF In COMPs must be used with the desired scene selected via the Scene parameter.

The glTF In COMP import is split into two stages: **asset creation** and **network generation**.

On import, assets including meshes, blend shapes, animations, and textures will all be created and stored internally within the glTF In COMP. After import, these can then be selected via Import Select OPs, the OP type being dependent on the desired asset type (eg. Import Select POP for mesh prim assets). In most cases, Import Select OPs do not need to be manually created by the user, as they will be automatically created during the network generation stage of the import.

After asset creation, network generation will occur inside the glTF In COMP, closely following the hierarchy/structure defined in the glTF file, with Geometry COMPs representing glTF nodes nested according to the children layout. Skeleton nodes will not be nested and will instead of wired.

**Important:** the network generation stage modifies the internal network of the glTF In COMP, which may include overwriting user-made changes. And if using the **Full Replacement** Import Method, then all changes will be overwritten. **Merge with Existing** Import Method can be used to merge user changes with the newly generated network on import. But if only the assets themselves have changed, then the network generation stage of import can be skipped altogether using the **Reload Assets** Import Method, which is ideal for maintaining user network changes. However, if there are any structural/hierarchical changes to the node structure in the file then using Reload Assets may break the import.

### Asset Types

**Meshes** : meshes will be split up by mesh primitive, with each primitive having its own separate Import Select POP contained within an additional Geometry COMP (_primN_) that will also contain its material (ie. PBR MAT). If the mesh contains any blend shapes then they will be generated alongside the mesh prim's Import Select POP and wired together into a Blend POP, with default weights set via parameter (but if animated, these default values will be overriden, although they can still be selected via the _default_weight_ asset via the Import Select CHOP Blend Shape parameter). If the mesh is animated or has a skeleton/skin, then a Skin Deform POP will be created and added to the internal POP wired chain.

**Animation channels** : When there are animations in the glTF file, use the controls on the Play page to initialize, start and guide the animation. Also, create an Info CHOP and attach it to the glTF In COMP to watch its animation timing. The Info CHOP channels are similar to those of the Timer CHOP. An Import Select CHOP will be created at the root and will automatically export to parameter paths using the `nodepath:par` channel name structure.

**Textures** : Texture assets will all be contained within the `touchTextures` COMP at the root level. These will be referenced by Select TOPs and used in PBR MATs within the network as necessary. The TOPs will be named according to their role in the PBR MAT (eg. "basecolor" or "normal") for ease of identification. In glTF, Metallic and roughness are always combined together into a single texture, with metallic values in the blue channel, and roughness values in the green channel. In some glTF files, ambient occlusion will be the red channel of the metallic/roughness, rather than its own texture. Note that texture channel selection is done on the PBR MAT itself using the Channel Source parameter, only visible by expanding the texture map's parameters using `>>`.

### Extensions

The glTF In COMP's Info DAT can be used to get a list of extensions that are required/used by the glTF file. Supported extensions:
  * [_KHR_lights_punctual_](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_lights_punctual/README.md): imports lights into the scene as Light COMPs.
  * [_KHR_materials_emissive_strength_](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_materials_emissive_strength/README.md): applies an extra scalar multiplier to the PBR MAT's Emit parameter.
  * [_KHR_materials_unlit_](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_materials_unlit/README.md): the material will use an unlit shading model (ie. no PBR rendering model applied) and the output color buffer will be the base color.
  * [_KHR_materials_specular_](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_materials_specular/README.md): **(not fully supported)** specular factor and texture will be imported and used as Specular Level on the PBR MAT; if it exists, the Specular Color texture will be imported but not used by the PBR MAT.
  * [_KHR_materials_pbrSpecularGlossiness_](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness/README.md): **(not fully supported)** if they exist, the Diffuse and Specular/Glossiness textures will be imported but not used by the PBR MAT.

See also: [glTF](https://docs.derivative.ca/GlTF "GlTF") [Blender](https://docs.derivative.ca/Blender "Blender")

[gltfinCOMP_Class](GlTF_In_COMP_Class.md "GltfinCOMP Class")

## Parameters - glTF In Page
- glTF File `file` - Select a glTF 2.0 (.gltf or .glb) file to import. The file will not import until the Import parameter is pulsed. Note: glTF 1.0 is not supported.
- Scene `scene` - ⊞ - Select the glTF scene to import from the file. The menu will auto-populate with available scenes once a glTF file is filled in on the glTF File parameter (no need to pulse Import to fill in the menu).
  * default `default` -
- Import Method `importmethod` - ⊞ - Select the method for importing.
  * Full Replacement `full` - Fully rebuilds the network inside the glTF In COMP and reloads the assets from the glTF file. Primary use case is as a clean rebuild and when internal changes are no longer needed.
  * Merge with Existing `merge` - Merges any changes in the glTF file with the existing contents of the glTF In COMP. Primary use case is to import structural changes from the file (eg. node hierarchy), while maintaining user changes to the internal network.
  * Reload Assets (Import Selects) `reload` - Assets that are loaded into Import Select operators (geos, textures, animations) are reloaded into the existing glTF In COMP's network from the glTF file. Primary use case is to load asset changes from the file in cases where there are not structural changes to the node hierarchy (ie. changes that require network update/generation). No network generation occurs when Reload Assets is selected.
- Auto Import `autoimport` - When enabled, the glTF In COMP will automatically trigger an import if any of the following parameters change: glTF File, Scene, Sample Rate, Cameras, Quaternion Channels, or Material Color Space. **Note:** an import will not be triggered if the file itself is changed or overwritten.
- Import `imp` - When pulsed, will clear the entire internal network of the glTF In COMP, import the glTF file scene, and generate all the necessary nodes.
- Cameras `cameras` - When enabled, the glTF In COMP will import any cameras in the file. Note: the change will not take effect unless Auto Import is enabled or the Import parameter is pulsed.
- Quaternion Channels `quats` - When enabled, the glTF In COMP will import additional Quaternion channels (`q[xyzw]`) in the animation. Although they are not used directly via exporting to pars, they are needed for smooth playback (ie. interpolation/slerp) when the sample index is between frame values; without the Quaternion channels, the resulting interpolated rotation values may cause strange or glitchy behavior in the mesh. Similarly, they are also needed when exporting glTF in order to achieve the best accuracy, and to prevent any issues with rotational interpolation. When providing animation channels to a [glTF Out COMP](https://docs.derivative.ca/GlTF_Out_COMP "GlTF Out COMP"), Quaternion channels (`q[xyzw]`) will always take preference over Euler angle channels (`r[xyz]`), if they exist.
- Shadows `shadows` - When enabled, the glTF In COMP will enable enable hard shadows for all imported Light COMPs, with all internal Geo COMPs used as shadow casters.
- Geometry Color Space `geocolorspace` - ⊞ - Select the color space for imported mesh assets (ie. Import Select POPs) with a Color attribute.
  * sRGB `srgb` -
  * sRGB - Linear `srgblinear` -
  * Rec.601 (NTSC) `rec601ntsc` -
  * Rec.709 `rec709` -
  * Rec.2020 `rec2020` -
  * DCI-P3 `dcip3` -
  * DCI-P3 (D60) `dcip3d60` -
  * Display P3 (D65) `displayp3d65` -
  * ACES2065-1 `aces2065-1` -
  * ACEScg `acescg` -
  * Passthrough `passthrough` -
- Material Color Space `matcolorspace` - ⊞ - Select the color space for any imported PBR MATs.
  * sRGB `srgb` -
  * sRGB - Linear `srgblinear` -
  * Rec.601 (NTSC) `rec601ntsc` -
  * Rec.709 `rec709` -
  * Rec.2020 `rec2020` -
  * DCI-P3 `dcip3` -
  * DCI-P3 (D60) `dcip3d60` -
  * Display P3 (D65) `displayp3d65` -
  * ACES2065-1 `aces2065-1` -
  * ACEScg `acescg` -
  * Passthrough `passthrough` -
- Keep Parameter Values `keepparams` - When enabled, any parameter conflicts during update will keep the user changes. When disabled, any user changes to parameters may be overwritten.
- Keep Connections `keepconnections` - When enabled, any wiring/connection conflicts during update will keep the user changes. When disabled, any user changes to wiring/connections may be overwritten.
- Callbacks DAT `callbacks` - The Callbacks DAT will execute during import or update allowing for modification and customization of the imported operators and resulting network.

## Parameters - Play Page
- Animation `animation` - Specifies the animation name (if any is specified) to playback from the imported glTF file.
- Shift Animation Start `shiftanimationstart` - A toggle to specify whether to shift the animation to the start of animation indicated in the importing file.
- Sample Rate Mode `sampleratemode` - ⊞ - Select between using the 'File FPS' embedded in the glTF file or setting a 'Custom' sample rate.
  * File FPS `filefps` -
  * Custom `custom` -
- Sample Rate `samplerate` - Set the sample rate when the "Sample Rate Mode" parameter above is set to 'Custom'.
- Play Mode `playmode` - ⊞ - A menu to specify the method used to play the animation.
  * Locked to Timeline `lockedtotimeline` - This mode locks the animation position to the timeline. The parameters Play, Speed, Index, Cue and Cue Point, are disabled in this mode since the timeline is directly tied to animation position.
  * Specify Index `specifyindex` - This mode allows the user to specify a particular index (position) in the animation using the Index parameter below. Use this mode for random access to any location in the animation.
  * Sequential `sequential` - This mode continually plays regardless of the timeline position (the Index parameter is disabled). Play, Speed, Cue, and Cue Point parameters below are enabled to allow some control. The default is set to this value.
  * Output Full Range `outputfullrange` -
- Initialize `initialize` - Resets the animation to its initial state.
- Start `start` - Resets the animation to its initial state and starts playback.
- Play `play` - Animation plays when On and stops when Off. This animation playback control is only available when Play Mode is Sequential.
- Speed `speed` - This is a speed multiplier which only works when Play Mode is Sequential. A value of 1 is the default playback speed. A value of 2 is double speed, 0.5 is half speed and so on. Negative values will play backwards.
- Cue `cue` - Jumps to and holds at the Cue Point when set to 1. Only available when Play Mode is Sequential.
- Cue Pulse `cuepulse` - Jumps to the Cue Point when pulsed. Only available when Play Mode is Sequential.
- Cue Point `cuepoint` - Set any index in the animation as a point to jump to. Only available when Play Mode is Sequential.
- Cue Point Unit `cuepointunit` - ⊞ - Select what type of unit to specify the Cue Point with.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -
  * I `indices` -
- Index `index` - This parameter explicitly sets the animation position when Play Mode is set to Specify Index. The units menu on the right lets you specify the index in the following units: Index, Frames, Seconds, and Fraction (percentage)
- Index Unit `indexunit` - ⊞ -
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -
- Trim `trim` - A toggle to enable the Trim Start and Trim End parameters.
- Trim Start `tstart` - Sets an in point from the beginning of the animation, allowing you to trim the starting index of the animation. The units’ menu on the right let you specify this position by index, frames, seconds, or fraction (percentage).
- Trim Start Unit `tstartunit` - ⊞ - Specifies a unit type for Trim Start. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -
- Trim End `tend` - Sets an end point from the end of the movie, allowing you to trim the ending index of the animation. The units’ menu on the right let you specify this position by index, frames, seconds, or fraction (percentage).
- Trim End Unit `tendunit` - ⊞ - Specifies a unit type for Trim End. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -
- Extend Left `textendleft` - ⊞ - Determines how the animation behaves before the start of the animation (or Trim Start position if it is used).
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -
- Extend Right `textendright` - ⊞ - Determines how the animation behaves after the end of the animation (or Trim End position if it is used).
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

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

The Pre-Xform parameter page applies a transform to the object component the same way connecting another [Object](../Glossary/Object.md "Object") as a parent of this node does. The transform is applied to the left of the [Xform](https://docs.derivative.ca/Object_COMP_Xform_Page "Object COMP Xform Page") page's parameters. In terms of matrix math, if we use the 'multiply on the right' (column vector) convention, the equation would be `preXForm * xform * Position`.
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

The Display parameter page controls the component's [material](https://docs.derivative.ca/index.php?title=Material&action=edit&redlink=1 "Material \(page does not exist\)") and [rendering](../Glossary/Rendering.md "Rendering") settings.
- Material `material` - Selects a [MAT](../MATs/MAT.md "MAT") to apply to the geometry inside.
- Render `render` - Whether the Component's geometry is visible in the [Render TOP](../TOPs/Render_TOP.md "Render TOP"). This parameter works in conjunction (logical AND) with the Component's [Render Flag](../Glossary/Render_Flag.md "Render Flag").
- Draw Priority `drawpriority` - Determines the order in which the Components are drawn. Smaller values get drawn after larger values. The value is compared with other Components in the same parent Component, or if the Component is the top level one listed in the Render TOP's 'Geometry' parameter, then against other top-level Components listed there. This value is most often used to help with [Transparency](https://docs.derivative.ca/Transparency "Transparency").
- Pick Priority `pickpriority` - When using a [Render Pick CHOP](../CHOPs/Render_Pick_CHOP.md "Render Pick CHOP") or a [Render Pick DAT](../DATs/Render_Pick_DAT.md "Render Pick DAT"), there is an option to have a 'Search Area'. If multiple objects are found within the search area, the pick priority can be used to select one object over another. A higher value will get picked over a lower value. This does not affect draw order, or objects that are drawn over each other on the same pixel. Only one will be visible for a pick per pixel.
- Wireframe Color `wcolor` - ⊞ - Use the R, G, and B fields to set the Component's color when displayed in wireframe shading mode.
  * Red `wcolorr` -
  * Green `wcolorg` -
  * Blue `wcolorb` -
- Light Mask `lightmask` - By default all lights used in the [Render TOP](../TOPs/Render_TOP.md "Render TOP") will affect geometry renderer. This parameter can be used to specify a sub-set of lights to be used for this particular geometry. The lights must be listed in the [Render TOP](../TOPs/Render_TOP.md "Render TOP") as well as this parameter to be used.

## Parameters - Extensions Page

The Extensions parameter page sets the component's python extensions. Please see [extensions](../Glossary/Extensions.md "Extensions") for more information.
- Re-Init Extensions `reinitextensions` - Recompile all extension objects. Normally extension objects are compiled only when they are referenced and their definitions have changed.
- Init Extensions On Start `initextonstart` - Perform a Re-Init automatically when TouchDesigner Starts
- Extension `ext` - Sequence of info for creating extensions on this component
- Object `ext0object` - A number of class instances that can be attached to the component.
- Name `ext0name` - Optional name to search by, instead of the instance class name.
- Promote `ext0promote` - Controls whether or not the extensions are visible directly at the component level, or must be accessed through the `.ext` member. Example: `n.Somefunction` vs `n.ext.Somefunction`

## Parameters - Common Page

The Common parameter page sets the component's [node viewer](../Glossary/Node_Viewer.md "Node Viewer") and [clone](../Glossary/Clone.md "Clone") relationships.
- Parent Shortcut `parentshortcut` - Specifies a name you can use anywhere inside the component as the path to that component. See [Parent Shortcut](../Glossary/Parent_Shortcut.md "Parent Shortcut").
- Global OP Shortcut `opshortcut` - Specifies a name you can use anywhere at all as the path to that component. See [Global OP Shortcut](../Glossary/Global_OP_Shortcut.md "Global OP Shortcut").
- Internal OP `iop` - Sequence header for internal operators.
- Shortcut `iop0shortcut` - Specifies a name you can use anywhere inside the component as a path to "Internal OP" below. See [Internal Operators](../Glossary/Internal_Operators.md "Internal Operators").
- OP `iop0op` - The path to the Internal OP inside this component. See [Internal Operators](../Glossary/Internal_Operators.md "Internal Operators").
- Node View `nodeview` - ⊞ - Determines what is displayed in the node viewer, also known as the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer"). Some options will not be available depending on the Component type ([Object Component](../Glossary/Object_Component.md "Object Component"), [Panel Component](../Glossary/Panel_Component.md "Panel Component"), Misc.)
  * Default Viewer `default` - Displays the default viewer for the component type, a 3D Viewer for Object COMPS and a Control Panel Viewer for Panel COMPs.
  * Operator Viewer `opviewer` - Displays the node viewer from any operator specified in the Operator Viewer parameter below.
- Operator Viewer `opviewer` - Select which operator's node viewer to use when the Node View parameter above is set to Operator Viewer.
- Enable Cloning `enablecloning` - Control if the OP should be actively cloneing. Turning this off causes this node to stop cloning it's 'Clone Master'.
- Enable Cloning Pulse `enablecloningpulse` - Instantaneously clone the contents.
- Clone Master `clone` - Path to a component used as the Master [Clone](../Glossary/Clone.md "Clone").
- Load on Demand `loadondemand` - Loads the component into memory only when required. Good to use for components that are not always used in the project.
- Enable External .tox `enableexternaltox` - When on (default), the external .tox file will be loaded when the .toe starts and the contents of the COMP will match that of the external .tox. This can be turned off to avoid loading from the referenced external .tox on startup if desired (the contents of the COMP are instead loaded from the .toe file). Useful if you wish to have a COMP reference an external .tox but not always load from it unless you specifically push the Re-Init Network parameter button.
- Enable External .tox Pulse `enableexternaltoxpulse` - This button will re-load from the external `.tox` file (if present).
- External .tox Path `externaltox` - Path to a `.tox` file on disk which will source the component's contents upon start of a `.toe`. This allows for components to contain networks that can be updated independently. If the `.tox` file can not be found, whatever the `.toe` file was saved with will be loaded.
- Reload Custom Parameters `reloadcustom` - When this checkbox is enabled, the values of the component's [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters") are reloaded when the [.tox](../Glossary/.tox.md ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](../Glossary/.tox.md ".tox").
- Reload Built-In Parameters `reloadbuiltin` - When this checkbox is enabled, the values of the component's built-in parameters are reloaded when the [.tox](../Glossary/.tox.md ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](../Glossary/.tox.md ".tox").
- Save Backup of External `savebackup` - When this checkbox is enabled, a backup copy of the component specified by the External `.tox` parameter is saved in the `.toe` file. This backup copy will be used if the External `.tox` can not be found. This may happen if the `.tox` was renamed, deleted, or the `.toe` file is running on another computer that is missing component media.
- Sub-Component to Load `subcompname` - When loading from an External `.tox` file, this option allows you to reach into the `.tox` and pull out a COMP and make that the top-level COMP, ignoring everything else in the file (except for the contents of that COMP). For example if a `.tox` file named `project1.tox` contains `project1/geo1`, putting `geo1` as the Sub-Component to Load, will result in `geo1` being loaded in place of the current COMP. If this parameter is blank, it just loads the `.tox` file normally using the top level COMP in the file.
- Relative File Path Behavior `relpath` - ⊞ - Set whether the child file paths within this COMP are relative to the .toe itself or the .tox, or inherit from parent.
  * Use Parent's Behavior `inherit` - Inherit setting from parent.
  * Relative to Project File (.toe) `project` - The path, when specified as a relative path, will be relative to the .toe file.
  * Relative to External COMP File (.tox) `externaltox` - The path, when specified as a relative path, will be relative to the .tox file. When no external COMP file is specified, or when Enable External .tox is not toggled on, this doesn't have any impact.
- Parameter Color Space `parmcolorspace` - ⊞ - Controls how all color parameters on this node are interpreted. Only available when a [Working Color Space](https://docs.derivative.ca/Working_Color_Space "Working Color Space") is active for the project. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space.
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
