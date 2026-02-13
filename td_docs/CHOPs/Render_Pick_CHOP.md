---
url: https://docs.derivative.ca/Render_Pick_CHOP
category: CHOPs
title: Render_Pick_CHOP
---

# Render Pick CHOP
## Summary

The Render Pick CHOP samples a rendering (from a [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or a [Render Pass TOP](https://docs.derivative.ca/Render_Pass_TOP "Render Pass TOP")) and returns 3D information from the geometry at that particular pick location. Values sampled can include position, normals, point color, texture coordinates, depth and the object's path. An [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") should be used to retrieve the object's path.
The pick location is specified through uv coordinates of the rendering. These uv coordinates can be selected by clicking on a [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") or explicitly setting them in the U and V parameters in the Render Pick CHOP.
Along with the geometric data returned, this node has two channels 'picked' and 'trigger' that inform the picked status. 'picked' will be 1 when an object has been found at the search location. 'trigger' will be 1 when both an object has been found, and the 'Picking By' condition has been met. That is, either the 'Panel Value' is 1, or the 'Select' parmeter is 'On.
See also the multi-sample [Render Pick DAT](https://docs.derivative.ca/Render_Pick_DAT "Render Pick DAT").
[renderpickCHOP_Class](https://docs.derivative.ca/RenderpickCHOP_Class "RenderpickCHOP Class")

## Parameters - Render Pick Page
- Strategy `strategy` - ⊞ - Decides when to update values based on pick interactions.
  * While Select `select` -
  * Hold First Picked `holdfirst` - Holds the values first returned when geometry picked.
  * Hold Last Picked `holdlast` - Holds the values last returned when geometry picked. This differs from the Continuous strategy in that it will hold the last values picked on geometry if the pick starts sampling empty space (no geometry in that part of the scene). Alternatively, using the Continuous strategy the values will be cleared to zero if the pick starts sampling empty space.
  * Always `always` -

- Clear Previous Pick on New Pick `clearprev` - This parameter is only enabled when the Strategy is set to Hold Last Picked. When this is on, starting a new pick on empty space will clear the values. When off, the last values will be held if the pick starts on empty space.
- Response Time `responsetime` - ⊞ - Determines when the values are updated.
  * Next Cook (Faster) `nextcook` - The values are captured on the current frame and updated next frame. Results are from the previous frame, but much faster cook times.
  * This Cook (Slower) `thiscook` - The values are captured and updated in the current frame.

- Pick Radius `pickradius` - Controls the radius of the search area for the pick. If nothing is found at the pick's center it will keep searching for geometry in the search area defined by the Pick Radius.
- Pick Radial Step `pickradstep` - Used to reduce the searching within the search area. The search area is sampled at locations that correspond to 'spokes' outwards from the center pick point.
- Pick Circular Step `pickcirstep` - Used to reduce the searching within the search area. The search area is sampled at locations that correspond to 'rings' outwards from the center pick point.
- Render/RenderPass TOP `rendertop` - Specifies which render to sample.
- Use Pickable Flags `usepickableflags` - When turned on only geometry whose [Pickable Flag](https://docs.derivative.ca/Flag "Flag") is on can be selected by the Render Pick CHOP. The [Pickable Flag](https://docs.derivative.ca/Pickable_Flag "Pickable Flag") is found on all [Object](https://docs.derivative.ca/Object "Object") components.
- Include Non-Pickable Objects `includenonpickable` - Includes the non-pickable objects in the picking algorithm such that non-pickable objects may occlude pickable objects. For example, if there is only one pickable object in the scene with lots of additional non-pickable geometry is present, turning this parameter on will prevent the pickable object from being selected if it is behind a non-pickage object (occluded by the non-pickage object).
- Picking by `pickingby` - ⊞ - Determines how the pick location is set.
  * Panel `panel` - Uses the Panel Component scoped in the **Panel** parameter. The uv position of the mouse on this component's control panel will be the uv position in the render that is sampled. The pick is active when the panel value specified by the **Panel Value** parameter is 1.
  * Parameters `parameters` - Uses the **U** , **V** , and **Pick** parameters below for picking.

- Panel `panel` - Specifies which panel component to use when picking by panel.
- Panel Value `panelvalue` - Specifies with panel value to use to trigger the pick when picking by panel.
- U `picku` - Sets the u coordinate when picking by parameters.
- V `pickv` - Sets the v coordinate when picking by parameters.
- Select `select` - When picking by parameters, picking is active when this parameter = 1.
- Activate Callbacks `activatecallbacks` - Enables Callback DAT for each pick event.
- Callbacks DAT `callbacks` - Path to a DAT containing callbacks for pick event received.

## Parameters - Options Page
- Fetch Position `position` - ⊞ - Returns the position of the point picked on the geometry. Channels _tx, ty, tz_.
  * No `no` - Do not return position values.
  * In SOP Space `sopspace` - Return position of point picked in SOP transform space.
  * In World Space `worldspace` - Return position of point picked in world transform space.
  * In Camera Space `cameraspace` - Return position of point picked in camera transform space.
  * Relative to Object `relativetoobj` - Return position of point picked relative to object specified in **Reference Object** parameter.

- Fetch Normal `normal` - ⊞ - Returns the normals of the point picked on the geometry. Channels _nx, ny, nz_.
  * No `no` - Do not return normal values.
  * In SOP Space `sopspace` - Return normals of point picked in SOP transform space.
  * In World Space `worldspace` - Return normals of point picked in world transform space.
  * In Camera Space `cameraspace` - Return normals of point picked in camera transform space.
  * Relative to Object `relativetoobj` - Return normals of point picked relative to object specified in **Reference Object** parameter.

- Reference Object `referenceobj` - Object used when fetching position or normals **Relative to Object**.
- Fetch Point Color `color` - Returns the point color of the point picked on the geometry. Channels _cr, cg, cb, ca_.
- Fetch Texture UV `uv` - Returns the texture coordinates of the point picked on the geometry. Channels _mapu, mapv, mapw_.
- Fetch Object Path `path` - Return the path to the object that is picked. This result requires and [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") with its **Node Path** parameter referecning the Render Pick CHOP.
- Fetch Depth `depth` - Returns the depth of the point picked on the geometry. This value a non-linear ratio of the point's position between the near and far planes of the [Depth Buffer](https://docs.derivative.ca/index.php?title=Depth_Buffer&action=edit&redlink=1 "Depth Buffer \(page does not exist\)"). Channel is _depth_.
- Fetch Instance ID `instanceid` - Returns the Instance ID of the object. This will always be 0 if instancing is off. Channel is _instance_.
- Custom Attrib 1 `customattrib1` - Specify which custom attributes to return from the object.
- Custom Attrib 1 Type `customattrib1type` - The type of attribute is selected from this menu.
- Custom Attrib 2 `customattrib2` - Specify which custom attributes to return from the object.
- Custom Attrib 2 Type `customattrib2type` - The type of attribute is selected from this menu.
- Custom Attrib 3 `customattrib3` - Specify which custom attributes to return from the object.
- Custom Attrib 3 Type `customattrib3type` - The type of attribute is selected from this menu.
- Custom Attrib 4 `customattrib4` - Specify which custom attributes to return from the object.
- Custom Attrib 4 Type `customattrib4type` - The type of attribute is selected from this menu.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).

## Info CHOP Channels
Extra Information for the Render Pick CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

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
