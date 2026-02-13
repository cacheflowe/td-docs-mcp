---
url: https://docs.derivative.ca/Render_Pick_DAT
category: DATs
title: Render_Pick_DAT
---

# Render Pick DAT
## Summary

The Render Pick DAT lets you get information about the 3D surface at any pixel of any 3D render, allowing you to implement multi-touch on a 3D rendered scene. It samples a rendering (from a [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or a [Render Pass TOP](https://docs.derivative.ca/Render_Pass_TOP "Render Pass TOP")) and returns 3D information from the geometry at the specified pick locations.
You feed it a DAT with minimum three columns: `select`, `u` and `v`. A [Multi Touch In DAT](https://docs.derivative.ca/Multi_Touch_In_DAT "Multi Touch In DAT") is usually connected to the Render Pick DAT, where the Multi Touch In DAT points to a container that is displaying the output of the Render TOP.

You can pick from multiple cameras simultaneously. You can specify a `camera` which allows the pick to occur from the point of a view other than the first camera listed in the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP"). The value in the column can either be a path (relative to the Render Pick DAT, or absolute) to a Camera COMP, or it can be an integer index, started at 0. If it's an index it will select the camera to use if there are multiple cameras listed in the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP"), or if there are cameras listed in the 'Custom Pick Camera(s)' parameter. This is useful for various [Multi-Camera Rendering](https://docs.derivative.ca/Multi-Camera_Rendering "Multi-Camera Rendering") setups, and cases such as VR where your picking isn't coming from the point of view of your eye cameras, but instead hand controllers.
The pick location is a u,v (horizontal, vertical) coordinate placed in the table that you connect to the Render Pick DAT input. Each row of the input table represents one pick point to be sampled, except for the first row which contains column headings `select`, `u` and `v` (plus any other unused columns you want). The `select`, `u` and `v` columns are what you would get from a [Panel CHOP](https://docs.derivative.ca/Panel_CHOP "Panel CHOP"). The u and v values goes 0 to 1 left to right and bottom to top, no matter what the aspect ratio of the render is.
When Strategy is Always, that u,v location is always sampled and the results are displayed in the corresponding row in the Render Pick DAT output.
The output table will show the path of the geometry that was picked, its position (in a choice of reference frames), surface normal (excluding bump mapping), distance from camera, texture UV coordinate, color, alpha and instance id. It properly picks surfaces with deforming vertices.
There are some examples here:
  * [geoPanel](https://docs.derivative.ca/Palette:geoPanel "Palette:geoPanel") in the palette.
  * [multiTouch](https://docs.derivative.ca/Palette:multiTouch "Palette:multiTouch") in the palette under Techniques.

See also the single-sample [Render Pick CHOP](https://docs.derivative.ca/Render_Pick_CHOP "Render Pick CHOP").
[renderpickDAT_Class](https://docs.derivative.ca/RenderpickDAT_Class "RenderpickDAT Class")

## Parameters - Render Pick Page
- Strategy `strategy` - ⊞ - Decides when to update values based on pick interactions.
  * While Select `select` - Continuously updates values when being selected/picked.
  * Hold First Picked `holdfirst` - Holds the values first returned when geometry picked.
  * Hold Last Picked `holdlast` - Holds the values last returned when geometry picked. This differs from the Continuous strategy in that it will hold the last values picked on geometry if the pick starts sampling empty space (no geometry in that part of the scene). Alternatively, using the Continuous strategy the values will be cleared to zero if the pick starts sampling empty space.
  * Always `always` - Continuously updates values at the location picked.

- Clear Previous Pick on New Pick `clearprev` - This parameter is only enabled when the Strategy is set to Hold Last Picked. When this is on, starting a new pick on empty space will clear the values. When off, the last values will be held if the pick starts on empty space.
- Response Time `responsetime` - ⊞ - Determines when the values are updated.
  * Next Cook (Faster) `nextcook` - The values are captured on the current frame and updated next frame. Results are from the previous frame, but much faster cook times.
  * This Cook (Slower) `thiscook` - The values are captured and updated in the current frame.

- Pick Radius `pickradius` - Controls the radius of the search area for the pick. If nothing is found at the pick's center it will keep searching for geometry in the search area defined by the Pick Radius.
- Pick Radial Step `pickradstep` - Used to reduce the searching within the search area. The search area is sampled at locations that correspond to 'spokes' outwards from the center pick point.
- Pick Circular Step `pickcirstep` - Used to reduce the searching within the search area. The search area is sampled at locations that correspond to 'rings' outwards from the center pick point.
- Render/RenderPass TOP `rendertop` - Specifies which scene to pick on, and which camera to pick from. By default the first camera listed in the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") will be used for picking. Another camera can be specified with the 'Custom Pick Camera(s)' parameter, and multiple different cameras can be selected using the `camera` input column.
- Custom Pick Camera(s) `custompickcameras` - Picking can be done from the viewport of custom camera(s) by specifying one or more [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") here. If this parameter is blank the cameras from the Render TOP are used. To pick from the viewpoint of multiple different cameras, a `camera` column must be specified in the input DAT.
- Allow Multi-Camera Rendering `allowmulticamera` - [Multi-Camera Rendering](https://docs.derivative.ca/Multi-Camera_Rendering "Multi-Camera Rendering") is a faster way to render multiple passes at the same time, and is thus a speed improvement for doing many picks at the same time. This feature may not work correctly for some older [GLSL MATs](https://docs.derivative.ca/GLSL_MAT "GLSL MAT") made in 088 though, so this parameter allows forcing off this speed improvement if necessary. Generally it should be left on though.
- Use Pickable Flags `usepickableflags` - When turned on only geometry whose [Pickable Flag](https://docs.derivative.ca/Flag "Flag") is on can be selected by the Render Pick DAT. The Pickable Flag is found on all [Object](https://docs.derivative.ca/Object "Object") components.
- Include Non-Pickable Objects `includenonpickable` - Includes the non-pickable objects in the picking algorithm such that non-pickable objects may occlude pickable objects. For example, if there is only one pickable object in the scene with lots of additional non-pickable geometry is present, turning this parameter on will prevent the pickable object from being selected if it is behind a non-pickage object (occluded by the non-pickage object).
- Merge Input DAT `mergeinputdat` - Appends input table to the Render Pick DATs columns.
- Activate Callbacks `activatecallbacks` - Enables Callback DAT for each pick event.
- Callbacks DAT `callbacks` - Path to a DAT containing callbacks for pick event received.

## Parameters - Options Page
- Fetch Position `position` - ⊞ - Returns the position of the point picked on the geometry. Columns _tx, ty, tz_.
  * No `no` - Do not return position values.
  * In SOP Space `sopspace` - Return position of point picked in SOP transform space.
  * In World Space `worldspace` - Return position of point picked in world transform space.
  * In Camera Space `cameraspace` - Return position of point picked in camera transform space.
  * Relative to Object `relativetoobj` - Return position of point picked relative to object specified in **Reference Object** parameter.

- Fetch Normal `normal` - ⊞ - Returns the normals of the point picked on the geometry. Columns _nx, ny, nz_.
  * No `no` - Do not return normal values.
  * In SOP Space `sopspace` - Return normals of point picked in SOP transform space.
  * In World Space `worldspace` - Return normals of point picked in world transform space.
  * In Camera Space `cameraspace` - Return normals of point picked in camera transform space.
  * Relative to Object `relativetoobj` - Return normals of point picked relative to object specified in **Reference Object** parameter.

- Reference Object `referenceobj` - Object used when fetching position or normals **Relative to Object**.
- Fetch Point Color `color` - Returns the point color of the point picked on the geometry. Columns _cr, cg, cb, ca_.
- Fetch Texture UV `uv` - Returns the texture coordinates of the point picked on the geometry. Columns _mapu, mapv, mapw_.
- Fetch Depth `depth` - Returns the depth of the point picked on the geometry. This value a non-linear ratio of the point's position between the near and far planes of the [Depth Buffer](https://docs.derivative.ca/index.php?title=Depth_Buffer&action=edit&redlink=1 "Depth Buffer \(page does not exist\)"). Column is _depth_.
- Fetch Instance ID `instanceid` - Returns the Instance ID of the object. This will always be 0 if instancing is off. Column is _instance_.
- Custom Attrib 1 `customattrib1` - Specify which custom attributes to return from the object.
- Custom Attrib 1 Type `customattrib1type` - The type of attribute is selected from this menu.
- Custom Attrib 2 `customattrib2` - Specify which custom attributes to return from the object.
- Custom Attrib 2 Type `customattrib2type` - The type of attribute is selected from this menu.
- Custom Attrib 3 `customattrib3` - Specify which custom attributes to return from the object.
- Custom Attrib 3 Type `customattrib3type` - The type of attribute is selected from this menu.
- Custom Attrib 4 `customattrib4` - Specify which custom attributes to return from the object.
- Custom Attrib 4 Type `customattrib4type` - The type of attribute is selected from this menu.

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
Extra Information for the Render Pick DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
