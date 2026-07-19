---
url: https://docs.derivative.ca/Release_Notes
category: General
title: Release_Notes
---

# Release Notes

Current Official **[Build 2025.33070 Download](https://derivative.ca/release/202533070/75035)** - **July 16 2026** - Release Notes

See our **[2025 Official Announcement](https://derivative.ca/community-post/2025-official-update/73153)** for the highlights of this release.

##  Known Issues

  * When using HDR Window Pixel Formats (see [Color Space](https://docs.derivative.ca/Color_Space "Color Space")), displaying HDR content as TOP backdrop can result in parts of the network editor being hard to view due to bad alpha blending. Turning off 'Display > Backdrop TOPs' in the network's right-clickmenu avoids this issue.

Please report all issues to the **[Bugs Forum](https://forum.derivative.ca/c/bugs/8)**.

##  Backward Compatibility

We try to make upgrading to new TouchDesigner branches as painless as possible, but sometimes changes are made that are not compatible with the features in older builds. Please review all [Backward Compatibility Issues](https://docs.derivative.ca/Release_Notes/2025.30000#Backward_Compatibility_Issues "Release Notes/2025.30000") as preparation for moving your projects to 2025.30000.

##  Build 2025.33070 Jul 16, 2026

Hotfix for 2025.33060 Phong MAT bug, please use this build in place of 2025.33060.

NOTE: **[Blob Track TOP](../TOPs/Blob_Track_TOP.md "Blob Track TOP") now tracks unlimited blobs with Non-Commercial license!**

###  New Features

**Python**
  * [Python](Python.md "Python") - Upgraded to Python 3.11.15
  * Upgraded most of the Python packages TouchDesigner ships with to the latest version.

**glTF**

[glTF](https://docs.derivative.ca/GlTF "GlTF") (Graphics Library Transmission Format) is a royalty-free specification for the efficient transmission and loading of 3D scenes and models by engines and applications. It is a feature-rich pathway from [Blender](https://docs.derivative.ca/Blender "Blender") to TouchDesigner. glTF minimizes the size of 3D assets and the processing needed to unpack and use them.
  * [glTF In COMP](../COMPs/GlTF_In_COMP.md "GlTF In COMP") - Load .`gltf` or `.glb` files into TouchDesigner, cameras, lights, animations and materials supported.
  * [glTF Out COMP](https://docs.derivative.ca/GlTF_Out_COMP "GlTF Out COMP") - Write out geometry as `.glb` or `.gltf` files to export to other applications or projects.

**POP**
  * [Script POP](https://docs.derivative.ca/Script_POP "Script POP") - A versatile and powerful new operator to create POP geometry and data with python. Check out the new [Operator Snippets](../Learn/OP_Snippets.md "OP Snippets") for it. It can build points, primitives and vertices with all types of attributes in various ways, stage it on the CPU and upload to the GPU. It can take its input POPs, process and output their data.
  * [DAT to POP](../POPs/DAT_to_POP.md "DAT to POP") - A full upgrade making this POP much more complete from data expressed in multiple DAT tables, making it another versatile way to build POPs. You can now send POP data on a round trip from [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") and then back through DAT to POP with its full data intact. Check out its Operator Snippets.
    * Can now specify primitive attributes, vertex attributes, detail attributes from multiple DATs. Attribute can now be generated automatically from the column names.
    * Load primitives, vertices and [dimensions](../Glossary/Dimension.md "Dimension") from DATs.
  * [`.pop` File Format](https://docs.derivative.ca/Pop_File_Format "Pop File Format") - A `.pop` file is a new native [File Type](../Interoperability/File_Types.md "File Types") and is an exact lossless representation of a POP's output. It is created with the [File Out POP](../POPs/File_Out_POP.md "File Out POP") or by right-clicking a POP node and selecting Save Geometry. Drag-drop the file to a network to create a [File In POP](../POPs/File_In_POP.md "File In POP"). A `.pop` file preserves all primitive types, attributes, groups and [Dimension](../Glossary/Dimension.md "Dimension").
  * locking POPs - POP operators can now be locked like other operators (with the lock flag on the node), freezing the content in memory. It gets included it in the project `.toe` file when saved. It is the exact same format as a `.pop` file. Be careful - like with TOPs, locking POPs can make `.toe` files very large.
  * **POP Rotations** - A massive list of new features to better support rotations and quaternions in POPs as been added.
    * [Copy POP](../POPs/Copy_POP.md "Copy POP") - Now supports quaternion attributes. In addition to transforming positions, normals, and transform matrices, any rotation transforms will now apply to input quaternions as well.
      * Can now assign quaternion attributes to the 'Template Rotate Attribute' parameter.
    * [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") / [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") -
      * Added support for transforming vectors with quaternions using the A * B operations on matrix/vector/quaternion attributes. For example, A * B : quaternion attribute * vector = rotated_vector.
      * Added support for quaternion product operations (quaternion x quaternion and quaternion x float3).
      * It's now possible to multiply transform matrices together.
      * Added _axisanglequat()_ in the Operation drop down menu on the Combine page to output quaternions. Note: There is a Operator Snippet for the [Particle POP](../POPs/Particle_POP.md "Particle POP") showing how to use this!
    * [Line Metrics POP](../POPs/Line_Metrics_POP.md "Line Metrics POP") - New Orientation page of parameters allow you to output the tangent–normal–binormal frame orientation along the line strips.
      * You can also output an attribute containing the tangent-normal-binormal frame orientation as a rotation matrix, or a transform matrix including the position.
      * New parameter 'Input Seed Orientation' which enables using an input attribute to define the initial orientation at each line‑strip starting point, using either quaternions or transform matrices.
    * [Skin Deform POP](../POPs/Skin_Deform_POP.md "Skin Deform POP") - Cam now transform quaternion attributes.
    * [Trail POP](../POPs/Trail_POP.md "Trail POP") - Can now output the tangent–normal–binormal frame orientation along the line trips.
    * [Transform POP](../POPs/Transform_POP.md "Transform POP") - Now supports quaternion attributes. In addition to transforming positions, normals, and transform matrices, any rotation transforms will now apply to input quaternions as well.
    * [Lookup Attribute POP](../POPs/Lookup_Attribute_POP.md "Lookup Attribute POP") - Can now interpolate quaternion and transform matrix attributes.
  * [Circle POP](../POPs/Circle_POP.md "Circle POP") - Can now output Vertex Normals and Vertex Tangents.
  * [Copy POP](../POPs/Copy_POP.md "Copy POP") - Added a new 'Template Matrix Order' parameter to set the template transform order between matrix and parameters.
  * [Neighbor POP](../POPs/Neighbor_POP.md "Neighbor POP") - Added 'Random' Distribution for neighbors 'By Distance'.
  * [Normal POP](../POPs/Normal_POP.md "Normal POP") - Added support for other primitive types. Closed line strips are now treated as polygons, open line strips and other primitive types get default values (N (0,0,1) T (1,0,0,1)).
  * [Pattern POP](../POPs/Pattern_POP.md "Pattern POP") - Added new 'Phase Step per Cycle' parameter to specify a phase offset per cycle.
  * [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") can now output the dimensions.
  * [Sphere POP](../POPs/Sphere_POP.md "Sphere POP") - Added 'Lines' to 'Geodesic Connectivity'.
  * [Sort POP](../POPs/Sort_POP.md "Sort POP") - Added new parameter to output 'Sorted Index Attribute' instead of reordering the points.
  * [Triangulate POP](https://docs.derivative.ca/Triangulate_POP "Triangulate POP") - Added 'Connect Holes' toggle and related parameters to correctly triangulate nested line strips. All line strips should be in the XY plane, holes line strips should have their winding order be clockwise and enclosing line strips counter clockwise.

**TOP**
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - When reading NotchLC codec files with 'Decode Pixel Format' set to 'Best', it will now use a 16-bit float pixel format.
  * [Touch Out TOP](../TOPs/Touch_Out_TOP.md "Touch Out TOP") / [Touch In TOP](../TOPs/Touch_In_TOP.md "Touch In TOP") - Added support for [NotchLC](https://docs.derivative.ca/NotchLC "NotchLC") encoded streams.

**CHOP**
  * [ST2110 Device CHOP](../CHOPs/ST2110_Device_CHOP.md "ST2110 Device CHOP") - Added new parameter to control the 'PTP Announce Interval' for Blackmagic devices.
  * [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP") - High-frequency MIDI events with timestamps - MIDI events arriving faster than the timeline frame rate (typically 60 frames per second) can be captured and represented as CHOP channels that are set to 1000 samples per second.
    * Added ability to process high frequency MIDI events via the new 'Mode' and 'Resample Mode' menus. 'Simplified' toggle behavior is now a part of this 'Mode' menu.
    * Added 'Note-On Only Channels' parameter for MIDI channels that only send Note On events, allowing for Note Off events to automatically be appended.

**DAT**
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") and [MIDI Event DAT](../DATs/MIDI_Event_DAT.md "MIDI Event DAT") - columns and callbacks representing high-frequency MIDI event timestamps - Five columns express the timestamp of the MIDI events coming from the operating system including the actual timestamp number coming from the operating system, the time of the event within the current [timeslice](../Glossary/Time_Slicing.md "Time Slicing") in milliseconds, and the absolute time of the event expressed in integer milliseconds.
  * [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") can now output the dimensions.
  * [Table DAT](../Glossary/Table_DAT.md "Table DAT") - New right-click menu option to jump to the operator path contained in the cell.

**Misc**
  * [RenderStream](https://docs.derivative.ca/RenderStream "RenderStream") - Upgraded to RenderStream 3.0. Added [working color space](../Interoperability/Color_Space_Workflows.md "Color Space Workflows") support.
  * Allow [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") 100G card to use each device for both input and output at the same time.
  * Improved timecode capture for [AJA](../Interoperability/AJA.md "AJA") ST2110 devices.
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") - Fixed incorrect handling of color space in the [CPlusPlus TOP](../TOPs/CPlusPlus_TOP.md "CPlusPlus TOP") in one case.

###  Palette

  * [Palette:callbacksHelper](https://docs.derivative.ca/Palette:callbacksHelper "Palette:callbacksHelper") - Fixed an issue where Edit Callbacks pulse stopped working.
  * [Palette:kantanMapper](../Interoperability/Palette_kantanMapper.md "Palette:kantanMapper") - Fixed groups not being correctly created and causing errors.
  * [Palette:projectorBlend](../Interoperability/Palette_projectorBlend.md "Palette:projectorBlend") - Shader cleanup, additional blend modes, and per projector blacklift added.
  * [Palette:tdPyEnvManager](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager") - v1.4.5 - Improved error reporting for CLI activation failures and added more reliable Windows DLL dependency loading for linked Python environments.
    * Fixed an issue related to the use of relative paths for folders that aren't children of the project folder.
  * [Palette:recorder](https://docs.derivative.ca/Palette:recorder "Palette:recorder") - 0.1.13 - Fixed internal menu setting which kept TDVS > recorder COMP from exporting movies.
  * **POPs > Gaussian Splats** - A new group of components for working with Gaussian Splats, look in Palette > POPs folder.
    * [Palette:gsLoader](https://docs.derivative.ca/Palette:gsLoader "Palette:gsLoader") - Loads Gaussian Splats in .spz or .ply file formats.
    * [Palette:gsTransform](https://docs.derivative.ca/Palette:gsTransform "Palette:gsTransform") - Translate, rotate, scale your Gaussian Splats.
    * [Palette:gsGeo](https://docs.derivative.ca/Palette:gsGeo "Palette:gsGeo") - This geometry component takes in splat data (from gsLoader or a [Point File In POP](../POPs/Point_File_In_POP.md "Point File In POP")) and applies the necessary materials to it so you can render your Gaussian Splats in any [Render TOP](../TOPs/Render_TOP.md "Render TOP").
    * [Palette:gsScene](https://docs.derivative.ca/Palette:gsScene "Palette:gsScene") - A pre-built setup that includes a gsGeo, cameraViewport, and Render TOP to render a complete 3D Gaussian Splat scene.

###  Bug Fixes and Improvements

**COMP**
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") / [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") - Numerous bug fixes.
    * Fixed a crash which could occur for some CHOPs and fixed issue which could cause crashes or corrupt data when using large CHOPs or DATs.
    * Fixed gradually degraded performance for some components.
    * Fixed an issue which could cause corrupt TOP output after configuration changed.
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") - Fixed an issue which could cause a hang after switching between loaded components.
  * [USD COMP](../COMPs/USD_COMP.md "USD COMP") - Improvements
    * Fixed empty or incomplete imported node hierarchy in some cases.
    * Fixed incorrect render flag settings which sometimes resulted in geometry not being rendered.
    * -Fixed importing of Emit texture maps.
    * Added support for Alpha (ie. opacity) texture maps.
  * [Window COMP](../Glossary/Window_COMP.md "Window COMP") - 'Escape on Close' parameter setting now also applies when using 'Open as Separate Window'.

**POP**
  * [Circle POP](../POPs/Circle_POP.md "Circle POP") - Fixed incorrect last point primitive with 'Point Primitives' Connectivity and fixed duplicated point with 'Surface' Connectivity and 'Closed' On.
  * [Convert POP](../POPs/Convert_POP.md "Convert POP") - Improvements working with Line Strips and a bug fix for uninitalized attributes.
    * 'Triangles, Quads and Lines to Line Strips' now copies vertex attributes from the input.
    * 'Unique and Reorder Points by Prim/Vertex Order' now preserves closed line strips.
    * - Fixed allocating vertex and primitive attributes left uninitialized for 'To Unique Lines' mode. Vertex and primitive attributes from the input now properly get discarded.
  * [Copy POP](../POPs/Copy_POP.md "Copy POP") - Improvements
    * The CopyId attribute can be added when 'Num Copies' is set to one.
    * Fixed 'Template Rotate Order' not working.
    * Fixed vertex and primitive Direction attributes not rotating when using a 'Template Matrix Transform'.
  * [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") - Changed DMX Channel sequence block summary to contain the Attribute/Constant values.
  * [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Improved output smoothness and resolved issues with send rate not reaching desired rate (viewable via packet_rate on [Info DAT](../DATs/Info_DAT.md "Info DAT")).
  * [Facet POP](../POPs/Facet_POP.md "Facet POP") - 'Unique Points' now preserves closed line strips.
  * [Feedback POP](../POPs/Feedback_POP.md "Feedback POP") - Fixed crashes happening in some cases when viewers in feeback loop are active.
  * [Group POP](../POPs/Group_POP.md "Group POP") - Fixed broken Primitive to Point Group conversion.
  * [Line POP](../POPs/Line_POP.md "Line POP") - Now sets a vertex budget _per line strip_ for resampling by distance or by keyframe.
  * [Line Divide POP](../POPs/Line_Divide_POP.md "Line Divide POP") / [Line Smooth POP](../POPs/Line_Smooth_POP.md "Line Smooth POP") / [Line Resample POP](../POPs/Line_Resample_POP.md "Line Resample POP") - The vertices budget for resampling by distance or curvature is now _per line strip_ not in total.
    * [Line Divide POP](../POPs/Line_Divide_POP.md "Line Divide POP") / [Line Smooth POP](../POPs/Line_Smooth_POP.md "Line Smooth POP") - Now sets a vertex budget _per line strip_ for Dividing edges by distance or curvature.
  * [[Math Mix POP / [Math ombine POP](https://docs.derivative.ca/index.php?title=Math_ombine_POP&action=edit&redlink=1 "Math ombine POP \(page does not exist\)") - Fixed performance issue with changing numeric values in attributes scopes.
  * [Neighbor POP](../POPs/Neighbor_POP.md "Neighbor POP") - Fixed incorrect output after disconnecting and reconnecting second input.
  * [Normal POP](../POPs/Normal_POP.md "Normal POP") - Fixed Normals now computed correctly when 'Normals Weighting' is 'Area Weighted' and 'Compute Normals Technique' is 'Loop over Primitives Per Point'.
  * [Proximity POP](../POPs/Proximity_POP.md "Proximity POP") - Fixed crash when 'Max Lines per Point' was set to a negative number. Also fixed incorrect output after disconnecting and reconnecting the second input.
  * [Subdivide POP](../POPs/Subdivide_POP.md "Subdivide POP") - Fixed 'Crease Weight' effect broken for boundary points of an open mesh.
  * [Trail POP](../POPs/Trail_POP.md "Trail POP") - Fixed broken column connectivity for inputs with the topology known on the GPU.
  * [Transform POP](../POPs/Transform_POP.md "Transform POP") - Improvements and bugs fixed.
    * Can now map the 'XForm Matrix' parameter to a point matrix attribute.
    * Weighted transform and transform parameter mapping now works on vertex attributes.
    * Fixed vertex attributes not being transformed with the 'XForm Matrix'.
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") - Fixed issue of `POP_Buffer` info not pointing to the input CUDA stream.

**TOP**
  * [TOP](../TOPs/TOP.md "TOP") - Fixed some shader compilation stutters that can happen when the resolution changes on some TOPs.
  * [TOP](../TOPs/TOP.md "TOP") - Fixed issue where TOPs operating on 3D textures would not work correctly when a [Color Space Workflows](https://docs.derivative.ca/Color_Space "Color Space") is active.
  * [Cache TOP](../TOPs/Cache_TOP.md "Cache TOP") - Fixed possible crash when pre-filling the cache.
  * [Layout TOP](../TOPs/Layout_TOP.md "Layout TOP") - Fixed bug where setting exact rows and columns didn't work when there was only one input.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - Fixed a crash that can occur when a larger resolution NotchLC encode occurs after a lower resolution one in the same Movie File Out TOP.
  * [Notch TOP](../TOPs/Notch_TOP.md "Notch TOP") - Added support for Notch's new subregion rendering via Crop page/parameters.
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Fixed issue where devices weren't connecting when switching between Auto-Detect and Specify IP device source mode.
  * [Render TOP](../TOPs/Render_TOP.md "Render TOP") - Fixed a crash that can occur when opening a project that is using Image Outputs.
  * [Render TOP](../TOPs/Render_TOP.md "Render TOP") / [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP") - Added range checking for TDImageLoad/TDImageStore() calls, for safety.
  * [ST2110 Device CHOP](../CHOPs/ST2110_Device_CHOP.md "ST2110 Device CHOP") - Support for Deltacast IP devices has been deprecated and will be removed in future builds.
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Fixed many parameters to better support [Ximea](https://www.ximea.com/) cameras.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Fixed audio pop that would occur for non-integer framerates on [AJA](../Interoperability/AJA.md "AJA") devices.

**CHOP**
  * [Audio Render CHOP](../Interoperability/Audio_Render_CHOP.md "Audio Render CHOP") - Fixed a crash that occurred when using 'Custom Setup' output format.
  * [Cross CHOP](../CHOPs/Cross_CHOP.md "Cross CHOP") - Fixed an issue where the CHOP would have no channels if the first input was empty.
  * [Laser Device CHOP](../CHOPs/Laser_Device_CHOP.md "Laser Device CHOP") / Etherdream - Fixed artifacts in laser output, regression introduced in build 2025.32460.
  * [Render Pick CHOP](../CHOPs/Render_Pick_CHOP.md "Render Pick CHOP") - Fixed incorrectly loaded parameters on the Common page which could lead to a hang.

**DAT**
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") - Fixed an issue where incorrect MIDI interface name would cause the DAT to attempt opening the port each frame.
  * [Render Pick DAT](../DATs/Render_Pick_DAT.md "Render Pick DAT") - Fixed incorrectly loaded parameters on the Common page which could lead to a hang.
  * [TUIO In DAT](../DATs/TUIO_In_DAT.md "TUIO In DAT") - Fixed issue of previous touch event data being cleared resulting in IDs being lost.
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT") - Added new 'Local Address' parameter.
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT") / [WebSocket DAT](../Interoperability/WebSocket_DAT.md "WebSocket DAT") - Fixed receiving of empty ping/pong messages.

**Misc**
  * Fixed pulsing of momentary-type parameters, you can now use .pulse() on them.
  * When more than 3 new [Custom Operator](../Interoperability/Custom_Operators.md "Custom Operators") Plugins are detected, a confirm dialog to allow all of them at once is now shown. Allows for easier installation of many plugins.
  * When a node is renamed with docked operators that share base name, a dialog to automatically rename the base name of the docked operators is shown.
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") Improvements for working with CPlusPlus OPs
    * `OP_CommonAPIVersion` increased to '2' due to several non-backwards compatible additions to the API.
    * Added ability to specify label for each of the custom operator's input connectors.
    * Added ability to create section headers and extended multi-size parameter options.
    * Removed `OpenGL32.lib` dependency from the CPlusPlus example projects.
    * Added ability to specify custom parameter help text. To see the parameter's help, rollover the parameter while holding the Alt key.
    * Added ability to save and load arbitrary blob data into the project file via new callbacks `saveData()` and `loadData()`.
  * [Script TOP](../TOPs/Script_TOP.md "Script TOP") / [Script POP](https://docs.derivative.ca/Script_POP "Script POP") / [Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP") / [Script DAT](../DATs/Script_DAT.md "Script DAT") / [Script SOP](../SOPs/Script_SOP.md "Script SOP") - Fixed an issue where updating the input wouldn't cause a cook when the script operator wasn't visible, even with `CookLevel.ON_CHANGE` or `CookLevel.ALWAYS`.

##  Build 2025.32820 May 06, 2026

UPDATE: **[Blob Track TOP](../TOPs/Blob_Track_TOP.md "Blob Track TOP") now tracks unlimited blobs with Non-Commercial license!**

###  New Features

**POP**
  * The Math Mix and Math Combine POPs' Combine page now shows a simple, one-line math summary of each sequential block, which you can expand to the usual editable parameters that make up the block, making for much more easier-reading of these powerful POPs.
  * [POPs Array Attributes](../Glossary/Array_Attribute.md "Array Attribute") - Several POPs now support iterating over array attribute elements using the `_name_[:]`syntax when specifying th array attribute. ([Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP"), [Math POP](../POPs/Math_POP.md "Math POP"), [Limit POP](../POPs/Limit_POP.md "Limit POP"), [ReRange POP](../POPs/ReRange_POP.md "ReRange POP"), [Lookup Attribute POP](../POPs/Lookup_Attribute_POP.md "Lookup Attribute POP"), [Lookup Channel POP](../POPs/Lookup_Channel_POP.md "Lookup Channel POP"), [Lookup Texture POP](../POPs/Lookup_Texture_POP.md "Lookup Texture POP"), [Quantize POP](../POPs/Quantize_POP.md "Quantize POP"), [Normalize POP](../POPs/Normalize_POP.md "Normalize POP"), [Random POP](../POPs/Random_POP.md "Random POP"), [Noise POP](../POPs/Noise_POP.md "Noise POP")). See OP Snippets for examples, including its POP CONCEPTS "array attributes math".
  * [POPs](../POPs/POP.md "POP") Python functions - Added new `point()`, `prim()`, `vert()` Python functions to access a single point attribute value. `delayed=True` gets it one frame delayed to not block the GPU/CPU.
  * [Analyze POP](../POPs/Analyze_POP.md "Analyze POP") - Added toggle to output 'Max Verts per Line Strip'.
  * [CPlusPlus POP](../POPs/CPlusPlus_POP.md "CPlusPlus POP") - Can now access TOP cudaArray memory via `getCUDAArray()`.
  * [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") - when extracting Primitives, an optional column Number of Vertices shows the number of vertices per primitive, and you can optionally hide the vertex list.

**TOP**
  * [Blob Track TOP](../TOPs/Blob_Track_TOP.md "Blob Track TOP") - Removed the 2 blob limit for Non-Commercial licenses so you can track any number of blobs with all licenses.
  * [CPlusPlus TOP](../TOPs/CPlusPlus_TOP.md "CPlusPlus TOP") - Can now access POP buffers in CUDA memory from POPs.
  * [Layout TOP](../TOPs/Layout_TOP.md "Layout TOP") - Added new toggle parameters to reverse the row and column direction order and new menu parameters to select between max and exact sizes for rows and columns. Also, fixed 'Grid Columns' align mode to correctly display the grid when the number of columns was larger than the hardware's limit for texture samplers accessible by a shader.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - Added 'EXR Compression Method' and 'EXR Compression Quality' parameters to allow for selecting between ZIP, DWAA, and DWAB compression methods.
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Added new parameters to set the Orbbec logging severity for the console and log file.

**DAT**
  * [JSON DAT](../DATs/JSON_DAT.md "JSON DAT") - Added Double Quotes option to 'Output Format'.
  * [Keyboard In DAT](../DATs/Keyboard_In_DAT.md "Keyboard In DAT") - Added support for the OEM 102 key on international 102-key keyboards.

**MAT**
  * [GLSL MAT](../MATs/GLSL_MAT.md "GLSL MAT") - Added `vec4 TDProjTextureLod(int lightIndex, vec2 coord, float lod)` and `ivec3 TDProjTextureSize(int lightIndex)`.

**SDK**
  * [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") - Upgrade to SDK 16.0. Added support for the new 100G [[[1]](https://docs.derivative.ca/Blackmagic_Design#ST2110_Support%7CST2110)] card.
  * [CUDA](../Interoperability/CUDA.md "CUDA") - Upgrade to CUDA 12.9.1.
  * [NDI](../Interoperability/NDI.md "NDI") - Upgrade to NDI 6.3.1.

**Misc**
  * Added [drag/drop subscribers](https://docs.derivative.ca/Drag-and-Drop#dragDropExt_Subscribers "Drag-and-Drop") for external file handlers.
    * Add a subscriber registry to /sys dragDropExt and expose Subscribe() for external COMPs.
    * Route supported file drops through built-in loaders and also forward them to matching subscribers.
    * Allow unsupported file types to be forwarded to subscribers when /sys has no built-in handler.
    * Normalize drop metadata used during routing and keep duplicate subscriptions from being added.

###  Python

  * [AbsTime Class](../Python/AbsTime_Class.md "AbsTime Class").timecode - Added a new member for fetching a [Timecode Class](../TOPs/Timecode_Class.md "Timecode Class") representation of AbsTime.
  * [SequenceBlock_Class](../Python/SequenceBlock_Class.md "SequenceBlock Class").summary - A text summary of the block if defined by the operator, blank otherwise. (Example in [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") Combine sequence to bring up resultant formulas).

###  Palette

  * [Palette:logger](https://docs.derivative.ca/Palette:logger "Palette:logger") - v2.7.0 - Refactor of parameter to Python Logger object sync, better parenting with default TDAppLogger and internal loggers.
  * [Palette:moviePlayer](https://docs.derivative.ca/Palette:moviePlayer "Palette:moviePlayer") / [Palette:movieEngine](https://docs.derivative.ca/Palette:movieEngine "Palette:movieEngine") - Fixed audio offset default to be -0.15, and permitted File to be an expression.

###  Bug Fixes and Improvements

**COMP**
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") / [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") - Fixed an issue which could cause TouchEngine processes to hang. Additionally fixed issue which could cause corrupt content in TOP inputs.
  * [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP") - Fixed 'Blend POP' set to Off on Blend Shape import, should be set to Proportional.
  * [Replicator COMP](../Glossary/Replicator_COMP.md "Replicator COMP") - `onRemoveReplicant` callback will now be called for all operators when 'Recreate All Operators' parameter is pulsed.

**POP**
  * [POPs](../POPs/POP.md "POP") - 'Copy Topology Back to CPU' ([Convert POP](../POPs/Convert_POP.md "Convert POP") etc) now also updates Max Verts per Line

Strip.
  * [POPs](../POPs/POP.md "POP") - Now showing actual number of verts for longest line strip (Max Verts Per Line Strip) when there is a mismatch with cpu side number (most likely when Topology info is on GPU but not only).
  * [CHOP to POP](../POPs/CHOP_to_POP.md "CHOP to POP") - Fixed array attributes not parsed correctly when using precise names, also parsing bugs for attributes with trailing underscore.
  * [CPlusPlus POP](../POPs/CPlusPlus_POP.md "CPlusPlus POP") - Error if an attribute that uses a reserved name doesn't match the required size/numComponents etc. of the reserved attribute. N, P are examples of this.
  * [CPlusPlus POP](../POPs/CPlusPlus_POP.md "CPlusPlus POP") - Clean up leftover attributes from previous cooks that aren't in the latest cook when using CUDA buffers.
  * [DAT to POP](../POPs/DAT_to_POP.md "DAT to POP") - Fixed a crash happening with some empty DATs.
  * [Delete POP](../POPs/Delete_POP.md "Delete POP") - Fixed bug when deleting point of line strip that could cause downstream POPs bugs.
  * [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") - Added a block summary at the top of each DMX Channel sequence block.
  * [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Fixed sending to sACN universes greater than 32767.
  * [Extrude POP](https://docs.derivative.ca/Extrude_POP "Extrude POP") - Fixed extruded closed line strips producing an extra point.
  * [Facet POP](../POPs/Facet_POP.md "Facet POP") - Fixed a crash happening in some cases when input has primitive or vertex normals and ‘Compute Point Normals’ is On.
  * [Field POP](../POPs/Field_POP.md "Field POP") - Fixed pivot transform error.
  * [Particle POP](../POPs/Particle_POP.md "Particle POP") - A birth‑rate inaccuracy when the rate is less than 1 per frame is fixed
  * [Switch POP](../POPs/Switch_POP.md "Switch POP") - fixed **Error when blending between inputs with attribute of type (u)int**
  * [GLSL POP](../POPs/GLSL_POP.md "GLSL POP") / [GLSL Advanced POP](../POPs/GLSL_Advanced_POP.md "GLSL Advanced POP") - Fixed synchronization issue with acceleration structure when 'Initialize Output Attributes' is On.
  * [Line POP](../POPs/Line_POP.md "Line POP") and [Point POP](../POPs/Point_POP.md "Point POP") - Fixed issue with attribute qualifier not assigned with custom attribute names.
  * [Ray POP](../POPs/Ray_POP.md "Ray POP") - When an attribute is on points, vertices and primitives of the collision geometry with the same name, vertices attribute will be sampled for consistency with viewer/render.
  * [Skin POP](../POPs/Skin_POP.md "Skin POP") - Max Verts Per Line Strip input info now only used for allocation, actual max always calculated from the actual line strips preveningt bugs with when mode is all line strips.
  * [Text POP](https://docs.derivative.ca/Text_POP "Text POP") - Fixed font file input and issues on macOS.
  * [TOP to POP](../POPs/TOP_to_POP.md "TOP to POP") - Added support for swizzling in input attribute scope. Also fixed 'Position and Active' mode to display points with alpha values larger than 0 but less than 1.
  * [Triangulate POP](https://docs.derivative.ca/Triangulate_POP "Triangulate POP") - Added toggle to remove triangles with 0 area. Also fixed a crash when input doesn't have P attribute.

8 [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") - Fixed overcooking in Specify Index mode, fixed user reported crash on toe file load when using Instant load type and Specify Index, Fixed an attribute crash with particles. Minor tweaks to par ranges and defaults.

**TOP**
  * [Constant TOP](../TOPs/Constant_TOP.md "Constant TOP") - Fixed incorrect parameter disabling for the 'Combine with Input' parameter.
  * [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP") - Fixed threaded compilation never finishing if the shader has an error during the preprocessor stage.
  * [Layout TOP](../TOPs/Layout_TOP.md "Layout TOP") - Fixed incorrect output resolution when there is only one input and the 'Output Resolution' parameter isn't set to 'Use Input'.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - Fixed 4:4:4:4 ProRes files not working correctly in some cases.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - Fixed movies being output with 1 frame missing in some cases for NotchLC and other non-Nvidia encoded codecs.
  * [NDI Out TOP](../TOPs/NDI_Out_TOP.md "NDI Out TOP") - Attempt to fix crash that can occur when starting up an NDI Out TOP on macOS.
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Numerous bug fixes and improvements.
    * Added new parameters to set the Orbbec logging severity for the console and log file.
    * Fixed outputs to use correctly scaled images when the resolution was over the resolution limit for Non-commercial licenses.
    * Fixed crash that occurred while closing TouchDesigner.
    * Fixed [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") to show gyro and accel data when connected to camera by specifying IP address.
  * [Spectrum TOP](../TOPs/Spectrum_TOP.md "Spectrum TOP") - Fixed issue where the Inverse Transform wouldn't remain properly normalized under certain UI operations.
  * [Substance TOP](../TOPs/Substance_TOP.md "Substance TOP") - Fixed incorrect output in some cases.
  * [Text TOP](../TOPs/Text_TOP.md "Text TOP") - Fixed 'Stroke' mode not working on macOS.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Added check to avoid letting the output queue grow to larger than 4 frames for [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") devices. Additionally fixed memory leak when using 'Regular' memory mode with Blackmagic devices.

**CHOP**
  * [Audio Play CHOP](../CHOPs/Audio_Play_CHOP.md "Audio Play CHOP") - Fixed issue which could cause a crash or hang on macOS.
  * [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") - Fixed sending to sACN universes greater than 32767.
  * [Laser CHOP](../CHOPs/Laser_CHOP.md "Laser CHOP") - Fixed sporadic crash with certain inputs.
  * [Pangolin CHOP](../CHOPs/Pangolin_CHOP.md "Pangolin CHOP") - Fixed choppy sending of data when used in [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine").
  * [POP to CHOP](../CHOPs/POP_to_CHOP.md "POP to CHOP") - Added support for swizzling, `Tex.i01` entry in dropdown menu now works as expected.

**DAT**
  * [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") - Can now optionaly output numVerts column for primitives.
  * [Table DAT](../Glossary/Table_DAT.md "Table DAT") - File paths now properly use their parent's relative file behavior.
  * [Text DAT](../Glossary/Text_DAT.md "Text DAT") - Fixed home key behavior on wrapped lines with multibyte UTF characters.

**Misc**
  * [Palette:lister](https://docs.derivative.ca/Palette:lister "Palette:lister") and [Component Editor Dialog](https://docs.derivative.ca/Component_Editor_Dialog "Component Editor Dialog") - Mac command-key shortcuts work properly
  * [NDI](../Interoperability/NDI.md "NDI") - Fixed hang on close that can occur when using an NDI HX source.
  * [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") - Fixed issue which prevented [Drag-and-Drop](https://docs.derivative.ca/Drag-and-Drop "Drag-and-Drop") in [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine").
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") - Improvements
    * Added `outputBufferCandidate` to `POP_GetBufferInfo`.
    * Now have the ability to query parameter values from nodes they are referencing.
    * Fixed `localTransform` and `worldTransform` not updating correctly for `OP_ObjectInput`.
  * [Sequential Parameters](../Glossary/Sequential_Parameters.md "Sequential Parameters") Block summary added - A text summary of the block if defined by the operator, blank otherwise. Example [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") 'Combine' sequnce to bring up resultant formulas.
  * Header parameters - Displays the parameter evaluation in addition to the label. Allows for dynamic content in the header. This feature is accessible through the "info" field when editing Header parameters in the Component Editor.
  * Fixed rendering of colored emojis in parameter inputs (on Windows OS).
  * Fixed direction of X axis labels in 3D viewers.
  * Fixed keyboard inputs on macOS, option+arrow moves word by word, cmd+arrow moves to beginning or end of line, option+del/backspace deleting words.
  * Fixed regression crash when rendering large strings of text in DAT cells.
  * Better binding conversion between int/float/menu types.
  * Fixed wrong wire being disconnected via right-click pop-up menu if the cursor is hovering over a different wire when 'Disconnect' is clicked.
  * Fixed pulsing of buttons in private components.
  * Added Twemoji as the default emoji font on MacOS, fixing an issue with emoji's not being rendered in Geo Text COMP, Text COMP, and some modes of the Text TOP.
  * Adjusted the text alignment for text overlays in POP viewers.
  * Increased thickness of axes lines in geo viewers.
  * Fixed a bug importing modules from DATs

##  Build 2025.32460 Mar 10, 2026

Hotfix for 2025.32440 ray tracing bug, please use this build in place of 2025.32440.

###  New Features

**POP**

Four new POPs and some improvements. Check their snippets.
  * [Text POP](https://docs.derivative.ca/Text_POP "Text POP") - A new POP with almost all the features of the [Text POP](https://docs.derivative.ca/Text_POP "Text POP"), [Text COMP](../COMPs/Text_COMP.md "Text COMP") and [Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP"), but bringing you text as 3D line strips and triangles.
  * [Trace POP](https://docs.derivative.ca/Trace_POP "Trace POP") - A new POP derived from the [Polygonize POP](../POPs/Polygonize_POP.md "Polygonize POP") but specialized for tracing 2D inputs and optimized for outputting line strips.
  * [Triangulate POP](https://docs.derivative.ca/Triangulate_POP "Triangulate POP") - A new POP to triangulate closed line strips. It operates in two modes; 1) Convex only, highly parallel 2) Convex and Concave, currently can get very slow for longer line strips.
  * [Alembic Out POP](https://docs.derivative.ca/Alembic_Out_POP "Alembic Out POP") - A new POP writes POP contents to an Alembic `.abc` file. It can make `.abc` files containing multi-frame animation, built in and custom attributes, as well multiple POPs as separate Alembic objects within one file.
  * [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") - Added a new 'Load Type' parameter for delayed (ie. next frame) loading that greatly reduces the overall cook time. Added new 'Play' page with extended playback controls similar to those on the [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP") and [USD COMP](../COMPs/USD_COMP.md "USD COMP").
  * [Cache POP](../POPs/Cache_POP.md "Cache POP") - Added a 'Always Cook' toggle to force cooking.
  * [Convert POP](../POPs/Convert_POP.md "Convert POP") - New "To Unique Lines" mode that converts Triangle and Quads edges to lines, and line strips to lines, ensuring there are no overlapping lines.
  * [Extrude POP](https://docs.derivative.ca/Extrude_POP "Extrude POP") - Can extrude line strips now.
  * [File In POP](../POPs/File_In_POP.md "File In POP") - Added new toggle parameters for 'Load Color' and 'Triangulate Faces'.
  * [Line Resample POP](../POPs/Line_Resample_POP.md "Line Resample POP") - Added the option to do cardinal interpolation to make curves smoother.
  * [Neighbor POP](../POPs/Neighbor_POP.md "Neighbor POP") - Now works with all primitive types when 'Neighbors Type' = Connected.
  * [Particle POP](../POPs/Particle_POP.md "Particle POP") - It is now possible to randomize particle spawn position or time with new 'Jitter Birth Position' and 'Jitter Births During Frame' parameters.
  * [Phaser POP](https://docs.derivative.ca/Phaser_POP "Phaser POP") - A new 'Extend Input' menu parameter has been added to specify the output behavior when the 'Fraction' parameter is outside the 0-1 range.
  * [Polygonize POP](../POPs/Polygonize_POP.md "Polygonize POP") - New updates, the Polygonize POP is now only meant for 3D inputs, for 2D inputs see the new [Trace POP](https://docs.derivative.ca/Trace_POP "Trace POP").
    * Now accepts POPs with dimension as input
    * New menu parameter to select TOP channel
    * Can now ReRange the output `P`
    * Can output texture coordinates that match the incoming image.
  * [Rectangle POP](../POPs/Rectangle_POP.md "Rectangle POP") - Added options for vertex normals.
  * [SOP to POP](../POPs/SOP_to_POP.md "SOP to POP") - Added more options to convert to POP primitives - like always produce line strips, or triangles.

**TOP**
  * Added option for ‘Input Color Space’ = Rec.709 - Gamma 2.4, this is found in numerous TOP generators such as [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP"), [NDI In TOP](../TOPs/NDI_In_TOP.md "NDI In TOP"), [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") etc.
  * [Constant TOP](../TOPs/Constant_TOP.md "Constant TOP") - Added new 'Output Type' and 'Slices' parameters to generate 3D textures and 2D Array textures directly in the Constant TOP.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - New features
    * Added a new 'Encode Splitting' parameter to explicitly control multiple GPU engine usage during encoding.
    * Added a 'Spatial AQ' control parameter. The default is Temporal AQ which looks at how the frames change over time to decide how to encode them. This new Spatial AQ mode looks at the complexity within a frame to determine encoding.
    * Added a 'Lookahead Frames' control.
    * 'Preset' parameter renamed to 'Quality Mode'. Added 'Ultra-High' quality mode option.
    * 'Bit Rate Mode' parameter renamed to 'Rate Control Mode'. Added 'Constant QP' rate control mode.
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Exposed Orbbec camera intrinsic and distortion parameters as Python members.
  * [ST2110 Out TOP](../TOPs/ST2110_Out_TOP.md "ST2110 Out TOP") - Added support for 'Fill+Key' output for [AJA](../Interoperability/AJA.md "AJA") IP25 devices.

**CHOP**
  * [OSC Out CHOP](../CHOPs/OSC_Out_CHOP.md "OSC Out CHOP") - Added new options to 'Data Format' called "Transpose By Name" that will group messages based on their root name (when channels contain "/": eg. "A/B/C" A is the root).
  * [RenderStream In CHOP](../CHOPs/RenderStream_In_CHOP.md "RenderStream In CHOP") - Added 'Resend Schema' pulse parameter to manually resend the schema to Disguise.
  * [RenderStream In CHOP](../CHOPs/RenderStream_In_CHOP.md "RenderStream In CHOP") - Added 'Save Schema JSON' controls for saving out the current schema.
  * [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP") - 14-Bit controller format is now supported when 'Simplified Output' parameter is toggled on. And 'Controller Format' menu has been moved to the 'Source' page.

**DAT**
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") - 14-bit controller messages are now consolidated into a single event message instead of two separate messages for the MSB and LSB.

###  Python

  * Allow `ui.options['font.mono.face']` to point to disk files.
  * [renderpickDAT Class](../DATs/Render_Pick_DAT_Class.md "RenderpickDAT Class").`pick()` - Fixed a crash and added a python error if the current [Render TOP](../TOPs/Render_TOP.md "Render TOP")/[Render Pass TOP](../TOPs/Render_Pass_TOP.md "Render Pass TOP") is invalid.

###  Palette

  * [Palette:camSchnappr](../Interoperability/Palette_camSchnappr.md "Palette:camSchnappr") - Fixed canvas output parameters not being properly enabled.
  * [Palette:domeViewer](https://docs.derivative.ca/Palette:domeViewer "Palette:domeViewer") - v0.6.1 - Added culled face on dome floor so that it can be looked through from the outside.
  * [Palette:kantanMapper](../Interoperability/Palette_kantanMapper.md "Palette:kantanMapper") - Fixed freeform shape 'Softedge' enable button texture.
  * [Palette:tdPyEnvManager](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager") - v1.4.1 - Various bug fixes and improvements
    * Fixed multi requirements path normalization on macOS.
    * Reduced duplicate mode-switch logging and aligned context/export metadata.
    * Updated CLI with latest features.
    * Fixed context persistence to avoid YAML writes when TOML context is active.
  * [Widgets](../Glossary/Widgets.md "Widgets") - v2.3.5 - Fixed some lost values and defaults.

###  Bug Fixes and Improvements

**COMP**
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") / [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") - Improvments and bug fixes
    * Added support for [Dimension](../Glossary/Dimension.md "Dimension") of POPs.
    * Fixed an issue which could cause a hang in TouchEngine.
    * Fixed an issue which could cause corrupt texture output if TouchEngine restarted.
    * Fixed an issue which could cause flickering when using TOPs.
  * [Time COMP](../Glossary/Time_COMP.md "Time COMP") - Absolute times now match absTime values (ie, paused when timeline pauses).

**POP**
  * [POPs](../POPs/POP.md "POP") - Fixed bypassed POPs keeping references to disconnected inputs.
  * [POPs](../POPs/POP.md "POP") - Attributes Python references - Fixed issue with parameters bound to POP attributes not being updated correctly.
  * [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") - Fixed importing of primitive UV and Normal attributes.
  * [Box POP](../POPs/Box_POP.md "Box POP") - Fixed an issue with setting num points too low when corner radius = 0.5.
  * [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") - Fixed reproducible hang when toggling 'Active' off in certain input cases.
  * [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Fixed crash that could occur when unicasting to many different netaddresses.
  * [Facet POP](../POPs/Facet_POP.md "Facet POP") - Fixed crash when using spatial grid modes and input point count info is on GPU, or when using groups.
  * [Line Smooth POP](../POPs/Line_Smooth_POP.md "Line Smooth POP") - Fixed resampling artefacts.
  * [Polygonize POP](../POPs/Polygonize_POP.md "Polygonize POP") - **Backward Compatibility Warning** - Width is now 1, height and depth varies when aspect ratio is not cube (previously height was fixed to 1).
  * [Proximity POP](../POPs/Proximity_POP.md "Proximity POP") - Fixed crash when second input has 0 points but still contains a P attribute.
  * [Trail POP](../POPs/Trail_POP.md "Trail POP") - Fixed the trail double-transforming when cooking a second time during a frame. Restored lost time slices. We now interpolate the transform for dropped frames whether 'Fill Missed Frames' is enabled or not. The result is more smooth trails.
  * Fixed broken hardware raytracing that could affect [GLSL POP](../POPs/GLSL_POP.md "GLSL POP"), [GLSL Advanced POP](../POPs/GLSL_Advanced_POP.md "GLSL Advanced POP"), [Ray POP](../POPs/Ray_POP.md "Ray POP"), [Sprinkle POP](../POPs/Sprinkle_POP.md "Sprinkle POP") (in volume mode).

**TOP**
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - Fixed incorrect output when playing back back ProRes 4:4:4:4 that doesn't have a width that is a multiple of 16 on Windows.
  * [Nvidia Upscaler TOP](https://docs.derivative.ca/Nvidia_Upscaler_TOP "Nvidia Upscaler TOP") / [Nvidia Background TOP](https://docs.derivative.ca/Nvidia_Background_TOP "Nvidia Background TOP") / [Nvidia Denoise TOP](https://docs.derivative.ca/Nvidia_Denoise_TOP "Nvidia Denoise TOP") - Fixed an issue where a rendering might have appeared black when using the TOP output as a material texture.
  * [ST2110 In TOP](../TOPs/ST2110_In_TOP.md "ST2110 In TOP") - Audio input now works correctly for [AJA](../Interoperability/AJA.md "AJA") devices.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Fixed memory leak when using 'Regular' memory mode with [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") devices.
  * [ZED TOP](../TOPs/ZED_TOP.md "ZED TOP") - Fixed `roimask` parameter name, improper orientation of region of interest mask, and issue where the mask was not updating when TOP was re-enabled.

**CHOP**
  * [Audio Binaural CHOP](../CHOPs/Audio_Binaural_CHOP.md "Audio Binaural CHOP") - Fixed zero output for non-Ambisonics input cases.
  * [Audio VST CHOP](../CHOPs/Audio_VST_CHOP.md "Audio VST CHOP") - Fixed instabilities with certain plugins (notably Omnisphere.vst3).
  * [Audio VST CHOP](../CHOPs/Audio_VST_CHOP.md "Audio VST CHOP") - Fixed a crash with Neutone VST3 when opening GUI.
  * [Count CHOP](../CHOPs/Count_CHOP.md "Count CHOP") - Fixed the 'Count Down' pulse increasing the count erroneously in certain configurations.
  * [Laser Device CHOP](../CHOPs/Laser_Device_CHOP.md "Laser Device CHOP") - Fixed crash using Helios devices when deactivating or deleting the CHOP.
  * [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP") - Improved warnings for 14-bit controller format when the selected controller index is in the reserved LSB index range. Also improved the behavior of the 'Controller Index' and 'Note Scope' parameter values which are now interpreted based on the state of the '1 Based Index' toggle.
  * [MIDI Out CHOP](../CHOPs/MIDI_Out_CHOP.md "MIDI Out CHOP") - The 14-bit controller format behavior has been updated to better fit the MIDI specification.
    * The single byte index range 64-95 now sends a single event, instead of an MSB+LSB event.
    * Events cannot be sent on the reserved LSB index range 32-63.
  * [Pattern CHOP](../CHOPs/Pattern_CHOP.md "Pattern CHOP") - Make behavior between Windows and macOS more consistent for 'Random' mode.
  * [Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP") - Fixed issue of `copyNumpyArray()` resetting the sample rate of the CHOP.
  * [Speed CHOP](../Glossary/Speed_CHOP.md "Speed CHOP") - Fixed NaN output issue that would sometimes occur when 'Limit' was set to Zigzag and the Minimum and Maximum limits flipped.
  * [Timeline CHOP](../CHOPs/Timeline_CHOP.md "Timeline CHOP") - Absolute times now match absTime values (ie, paused when timeline pauses).
  * [Touch Out CHOP](../CHOPs/Touch_Out_CHOP.md "Touch Out CHOP") - Fixed issue which caused TouchDesigner to silently quit on macOS sometimes.
  * [Trigger CHOP](../CHOPs/Trigger_CHOP.md "Trigger CHOP") - Fixed issue of new triggers not being properly ignored during attack stage when 'Multi Trigger' parameter was set to Ignore During Attack.

**DAT**
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") - When the 14-bit Values parameter is toggled on, single 7-bit controller events received within index range 0-63 will not be outputted since the range is reserved for 14-bit events.
  * [OP Find DAT](../DATs/OP_Find_DAT.md "OP Find DAT") - 'Node Position' menu added to determine how the values for nodeX/nodeY are calculated (center or bottom left as set in the Preferences Dialog).
  * [Text DAT](../Glossary/Text_DAT.md "Text DAT") - Fixed highlighting of python docstrings when the function def is split over multiple lines.

**MAT**
  * [Line MAT](../MATs/Line_MAT.md "Line MAT") - Removed 'Line Taper Strength' parameter which was always disabled and never used.
  * [Line MAT](../MATs/Line_MAT.md "Line MAT") - The point alpha is now taken into account when rendering points.

**Misc**
  * Adjusted auto homing near/far plane calculations to reduce flickering on large scenes.
  * New viewer text overlays for vertex points and vertex primitive order.
  * Added text scale to origin axes.
  * Fixed a bug restoring camera on viewers using non-default homing directions.
  * Restart vertices are now ignored when drawing text attribute overlays. Restart vertices are special vertices in line strips that don't actually get rendered but just indicate the end of the primitive in the vertex buffer.
  * Upgraded web install process to provide ONNX 1.23.2 when requested.
  * Fixed `par.pulse()` method on bound non-pulse parameters (ie. push, sliders, etc).
  * Fixed UTF8 encoding in callback output.
  * Fixed issues with fallback fonts for various text nodes ([Text TOP](../TOPs/Text_TOP.md "Text TOP"), [Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP") etc.).
  * Checkerboard showing transparent area around images in [TOP](../TOPs/TOP.md "TOP") viewers is now darker.
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") - Fixed corrupted value returned by `myNodeInfo.opPath` in some cases

###  Backward Compatibility Changes

**BACKWARD COMPATIBILITY ISSUE**
  * **BACKWARD COMPATIBILITY WARNING** - [Polygonize POP](../POPs/Polygonize_POP.md "Polygonize POP") - Now only accepts 3D input, use [Trace POP](https://docs.derivative.ca/Trace_POP "Trace POP") for 2D.
  * **BACKWARD COMPATIBILITY WARNING** - [Polygonize POP](../POPs/Polygonize_POP.md "Polygonize POP") - Width is now 1, height and depth varies when aspect ratio is not cube (previously height was fixed to 1).

##  Build 2025.32280 Jan 20, 2025

  * Hotfix for 2025.32260, please use this build in place of 2025.32260.

###  New Features

  * [Text COMP](../COMPs/Text_COMP.md "Text COMP") - Now supports colored glyphs e.g. emojis.
  * [Convert POP](../POPs/Convert_POP.md "Convert POP") - New 'To Unique Lines' mode that converts Triangle and Quads edges to lines, and line strips to lines, ensuring there are no overlapping lines.
  * [Fit TOP](../TOPs/Fit_TOP.md "Fit TOP") - New 'Justify Horizontal' and 'Justify Vertical' parameters added to align the fit in various ways.
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Added support for PTP for IDS Peak devices.
  * [Count CHOP](../CHOPs/Count_CHOP.md "Count CHOP") - New 'Zigzag Min/Max' mode in the 'Limit' parameter menu which will count back and forth between the Min and Max settings.
  * [Phaser CHOP](../CHOPs/Phaser_CHOP.md "Phaser CHOP") - Added a new 'Extend Input' menu to specify the output behavior when the time input is outside the 0-1 range.
  * [ST2110 Device CHOP](../CHOPs/ST2110_Device_CHOP.md "ST2110 Device CHOP") - Added support for [AJA](../Interoperability/AJA.md "AJA") devices (AJA IP25 card specifically).
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") - New '14 Bit Values' option which logs 14 bit controller values. This is identical to the [MIDI Event DAT](../DATs/MIDI_Event_DAT.md "MIDI Event DAT") parameter with the same name.
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") / [CPlusPlus TOP](../TOPs/CPlusPlus_TOP.md "CPlusPlus TOP") / [CPlusPlus DAT](../DATs/CPlusPlus_DAT.md "CPlusPlus DAT") / [CPlusPlus SOP](../SOPs/CPlusPlus_SOP.md "CPlusPlus SOP") / [CPlusPlus CHOP](../CHOPs/CPlusPlus_CHOP.md "CPlusPlus CHOP") - New `appendFileSave()` function to allow for FileSave type parameters.
  * [CPlusPlus POP](../POPs/CPlusPlus_POP.md "CPlusPlus POP") - New `getPOP()` and `appendPOP()` members added.

###  New Palette

  * [Palette:cppParsTemplateGen](https://docs.derivative.ca/Palette:cppParsTemplateGen "Palette:cppParsTemplateGen") - v0.1.5 - Added support for FileSave parameter.
  * [Palette:popMenu](https://docs.derivative.ca/Palette:popMenu "Palette:popMenu") - Fixed table input and table output.
  * [Palette:tdPyEnvManager](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager") - v1.3.8 - Multiple improvements and bug fixes.
    * The default context file is now switched to YAML. An extraPaths key (`extraPaths: []`) was added and can receive a list of relative or absolute paths as well as paths containing env variables to be resolved. Those paths are prepended during startup, after the main vEnv or Conda env was linked. By mindful of priority order.
    * The TDPyEnvManager COMP parameters were reworked to be shared and more uniform between Python vEnv and Conda Env modes.
    * Added support for installing multiple req files during autosetup from .yaml file with `autoSetupReqs: []`.
    * Helper: Added support for reading TDPyEnvManager Context from pyproject.toml file.
    * Fixed possible double linking on init.
    * Fixed possible issue on init when loading from context.
  * [Thread Manager](https://docs.derivative.ca/Thread_Manager "Thread Manager") - v1.1.7 - Fixed possible thread lock and keeping threads alive in case of caught exception.
  * [Palette:xyScope](https://docs.derivative.ca/Palette:xyScope "Palette:xyScope") - Converted to POPs and added polar sample view.

###  Bug Fixes and Improvements

**COMP**
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") / [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") - Fixed issues which could cause lost output in some circumstances.
  * [Text COMP](../COMPs/Text_COMP.md "Text COMP") - Improvments, bug fixes.
    * Enabled support for colored glyphs e.g. emojis.
    * Disabled Shift+Space shortcuts while editing text to avoid unintentionally pausing the timeline.
    * Fixed missing panel value key updates when editing in multiline mode.
    * Fixed a bug selecting unicode characters in text that uses formatting codes.
  * [USD COMP](../COMPs/USD_COMP.md "USD COMP") - Fixed a crash.

**POP**
  * [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") - Improvements
    * Improved 'Linear Interpolation' mode to also perform interpolation between all point positions (not just Dynamic Transforms at the Object level).
    * Improved per-object overhead and decrease cook time, most noticeably for Alembic files containing a large numbers of objects.
    * Fixed setting of Tex and Color attributes in cases where those attributes are not present in all imported objects.
  * [Convert POP](../POPs/Convert_POP.md "Convert POP") - New 'To Unique Lines' mode that converts Triangle and Quads edges to lines, and line strips to lines, ensuring there are no overlapping lines.
  * [CPlusPlus POP](../POPs/CPlusPlus_POP.md "CPlusPlus POP") - Fixed some members of `OP_POPInput` not being filled in properly. Also added new members `getPOP()` and `appendPOP()`.
  * [Delete POP](../POPs/Delete_POP.md "Delete POP") - We now allocate less points or primitives on certain conditions.
  * [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Fixed incorrect packet sequence values (see: Info DAT last_sequence) when sending via Art-Net or sACN that can cause lag on the receiving side, or prevent the display of packets altogether.
  * [Neighbor POP](../POPs/Neighbor_POP.md "Neighbor POP") - 'Connected' mode now works with all primitive types.
  * [Null POP](../POPs/Null_POP.md "Null POP") - Fixed a problem displaying different attribute overlays in a Null POP and its input.

**TOP**
  * [Edge TOP](../TOPs/Edge_TOP.md "Edge TOP") - The 'Comp Over Input' parameter has been renamed to 'Combine With Input' and compositing operations have been moved to the new 'Output' page. Additionally on this page find new 'Operation' and 'Swap Order' parameters to specify how the edge and input are combined.
  * [Fit TOP](../TOPs/Fit_TOP.md "Fit TOP") - New 'Justify Horizontal' and 'Justify Vertical' parameters added to align the fit in various ways.
  * [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP") - Threaded compiles will now avoid a stall if another edit is done before the current compile is done.
  * [Layout TOP](../TOPs/Layout_TOP.md "Layout TOP") - Fixed "GPU Mem this TOP" usage not clearing when there are zero inputs.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - For now, limit use of the NVIDIA hardware decoder to only allow 8 nodes at one time due to a hang that occurs when more are used.
  * [Notch TOP](../TOPs/Notch_TOP.md "Notch TOP") - Fixed updating of exposed color property values via parameter.
  * [Ouster Select TOP](../TOPs/Ouster_Select_TOP.md "Ouster Select TOP") - Fixed a crash that occurred from connecting to an empty [Ouster TOP](../TOPs/Ouster_TOP.md "Ouster TOP").
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Improved thread synchronization performance issues. Also fixed a crash for USB connections on macOS Apple Silicon systems.
  * [Switch TOP](../TOPs/Switch_TOP.md "Switch TOP") - Fixed broken renders when Output Resolution, Output Aspect, or Pixel Format were not assigned to 'Use Input' for 3D texture type inputs.
  * [Syphon Spout In TOP](../TOPs/Syphon_Spout_In_TOP.md "Syphon Spout In TOP") / [Syphon Spout Out TOP](../TOPs/Syphon_Spout_Out_TOP.md "Syphon Spout Out TOP") - Parameter dependency fix when Spout/Syphon sender names changed.
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Improvements and bug fixes.
    * Added support for PTP for IDS Peak devices.
    * 'Allow Fallback Selection' now stops a camera from being selected if the 'Device' parameter is blanked out.
    * Fixed regression in performance in this operator.
    * Fixed dynamic/manual Capture for FLIR Spinnaker cameras not working quite right.

**CHOP**
  * [Audio Device In CHOP](../CHOPs/Audio_Device_In_CHOP.md "Audio Device In CHOP") / [Audio Device Out CHOP](../Interoperability/Audio_Device_Out_CHOP.md "Audio Device Out CHOP") - Fixed issue which prevented audio input or output under [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine").
  * [Audio VST CHOP](../CHOPs/Audio_VST_CHOP.md "Audio VST CHOP") - Fixed a hang on load with the [Omnisphere](https://www.spectrasonics.net/products/omnisphere/overview.php) VST3 plugin.
  * [Count CHOP](../CHOPs/Count_CHOP.md "Count CHOP") - New 'Zigzag Min/Max' mode in the 'Limit' parameter menu which will count back and forth between the Min and Max settings.
  * [DMX In CHOP](../CHOPs/DMX_In_CHOP.md "DMX In CHOP") - Fixed receiving Art-Net in 'Packet Per Channel' mode when specifying a universe greater than 16. Also fixed reporting of last_sequence value for Art-Net and sACN.
  * [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") - Fixed incorrect packet sequence values (see: Info DAT last_sequence) when sending via Art-Net or sACN that can cause lag on the receiving side, or prevent the display of packets altogether.
  * [Laser CHOP](../CHOPs/Laser_CHOP.md "Laser CHOP") - Fixed a hang.
  * [Phaser CHOP](../CHOPs/Phaser_CHOP.md "Phaser CHOP") - Added a new 'Extend Input' menu to specify the output behavior when the time input is outside the 0-1 range.
  * [Shuffle CHOP](../CHOPs/Shuffle_CHOP.md "Shuffle CHOP") - Updated the CHOP's extend condition to be inherited from the input CHOP, instead of setting to HOLD, HOLD. Also fixed a crash when the input has zero channels.
  * [ST2110 Device CHOP](../CHOPs/ST2110_Device_CHOP.md "ST2110 Device CHOP") - Added support for [AJA](../Interoperability/AJA.md "AJA") devices (AJA IP25 card specifically).

**DAT**
  * [EtherDream DAT](../DATs/EtherDream_DAT.md "EtherDream DAT") - Fixed crash on Poll.
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") - New '14 Bit Values' toggle which logs 14 bit controller values. Is identical to the [MIDI Event DAT](../DATs/MIDI_Event_DAT.md "MIDI Event DAT") parameter with the same name.
  * [MIDI Event DAT](../DATs/MIDI_Event_DAT.md "MIDI Event DAT"), [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT") - Updated the `onReceiveCallback()` arguments to be a MIDIEvent NamedTuple, which includes a value14 entry for 14-bit values.
  * [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") - Outputting vertices list is now optional with new 'Vertices' parameter.
  * [Table DAT](../Glossary/Table_DAT.md "Table DAT") - Fixed clipping artifact when text exceeds the cell width.
  * [Video Devices DAT](../DATs/Video_Devices_DAT.md "Video Devices DAT") - IDS Peak now correctly shows 'idspeak' for it's Driver. Fixed a crash that can occur when 'All Drivers' is selected.

**MAT**
  * [GLSL MAT](../MATs/GLSL_MAT.md "GLSL MAT") - Fixed 'BoneIndices' and 'BoneWeights' not working for SOPs if declared on the 'Attributes' page.
  * [GLSL MAT](../MATs/GLSL_MAT.md "GLSL MAT") - Threaded compiles will now avoid a stall if another edit is done before the current compile is done.
  * [Line MAT](../MATs/Line_MAT.md "Line MAT") - Point alpha now taken into account when rendering points.

**Misc**
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") / [CPlusPlus TOP](../TOPs/CPlusPlus_TOP.md "CPlusPlus TOP") / [CPlusPlus DAT](../DATs/CPlusPlus_DAT.md "CPlusPlus DAT") / [CPlusPlus SOP](../SOPs/CPlusPlus_SOP.md "CPlusPlus SOP") / [CPlusPlus CHOP](../CHOPs/CPlusPlus_CHOP.md "CPlusPlus CHOP") - Added new `appendFileSave()` function to allow for FileSave type parameters.
  * Fixed some cases where Skinned Deforms were not working correctly.
  * Fixed a bug displaying some POP attributes as vectors in the viewer.
  * 3D viewers - Changed shortcut key for setting 'Angled' homing direction from 'a' to 'l'.
  * Fix issue which caused some events to be ignored while an open or save dialog was open on Windows.
  * [macOS](https://docs.derivative.ca/MacOS "MacOS") - Removed the grey border added on macOS 26 for windows without a titlebar.

##  Build 2025.32050 Dec 10, 2025

###  New Python

  * [TOP Class](../TOPs/TOP_Class.md "TOP Class").`cudaMemory()` - Added `pixelFormat` keyword argument to specify the pixel format of the CUDA memory block. Useful when colorspace settings force format for TOPs.

###  New Palette

  * [Palette:stoner](../Interoperability/Palette_stoner.md "Palette:stoner") - Fix for external project component to not be registered making edits not possible.
  * [Palette:tdPyEnvManager](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager") - v1.3.1 - EXPERIMENTAL: Adding autoSetup support. When a context file is present (with key autoSetup set to true), the TDPyEnvManager will setup environment and requirements during TouchDesigner startup sequence. This is a blocking call.
    * Tweaking fileHandler behaviour to not leave an empty file in CWD.
    * In Conda mode, a warning is logged and a dialog is opening if a space is found in the resolved install path.
    * Samples update.
  * [TDAbleton](../Interoperability/TDAbleton.md "TDAbleton") - v2.6.5
    * Revert Rack device changes due to bad loading on some old projects
    * Improved error messages for install
    * Clean up clip info pars
    * Fix clip overcooking in abletonTrack
    * Add SetClipInfo function to abletonTrack (see wiki)
    * Fix clip slot error when changing from midi to no midi
    * Make Connect par affect abletonMapper and abletonRacks OSC

###  Bug Fixes and Improvements

  * [Bluefish444](../Interoperability/Bluefish444.md "Bluefish444") - Updated to SDK version 6.6.1.4. [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") / [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP")
  * [OpenColorIO TOP](../TOPs/OpenColorIO_TOP.md "OpenColorIO TOP") - Updated to v2.5.0
  * [Ouster](https://docs.derivative.ca/Ouster "Ouster") - Rebuilt node using Ouster Sensor SDK 0.15.0. Adds support for newer hardware with version 3+ firmware. - [Ouster TOP](../TOPs/Ouster_TOP.md "Ouster TOP")

**COMP**
  * [CHOP](../Glossary/CHOP.md "CHOP") - Fixed a regression where pattern matching wouldn't work properly with renaming. Fixed for [Rename CHOP](../Glossary/Rename_CHOP.md "Rename CHOP") as well as Common page renaming.
  * [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP") / [Light COMP](../Glossary/Light_COMP.md "Light COMP") - Fixed a bug that unintentionally disabled the Pre-Transform during viewer updates.
  * [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP") - Fixed all black meshes on import in some cases.

**POP**
  * [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") - Fixed an attribute import bug - Tex (float[3]) was incorrectly converted to Tex (float3[3]), but will now correctly be converted to Tex (float3). Also fixed incorrect attribute data on import in some other cases.
  * [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") - Some new features and numerous bug fixes.
    * Added support for an input DMXFixtureGap primitive attribute that overrides the 'Channel Gap' parameter.
    * Fixed 'Quantize Universe By Fixture' not correctly pushing fixtures to the next universe when they don't fit.
    * Fixed incorrect layout with use of the 'Fixture Channel Gap' parameter when using the DMXFixtureNetAddress attribute.
    * Fixed sporadic hang/crash when using DMXFixtureNet, DMXFixtureSubnet, DMXFixtureUniverse, DMXFixtureChannel, or DMXFixtureNetAddress attributes.
    * Fixed a crash when selecting an invalid attribute.
  * [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Fixed a memory leak and an issue with send rate.
  * [Switch POP](../POPs/Switch_POP.md "Switch POP") - Fixed a bug where setting 'Length Mismatch' to "Error" would permanently stop its inputs from cooking.

**TOP**
  * [Anti Alias TOP](../TOPs/Anti_Alias_TOP.md "Anti Alias TOP") - Fixed this TOP not working correctly when a working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") is active.
  * [Circle TOP](../TOPs/Circle_TOP.md "Circle TOP") / [Ramp TOP](../TOPs/Ramp_TOP.md "Ramp TOP") / [Rectangle TOP](../TOPs/Rectangle_TOP.md "Rectangle TOP") / [Text TOP](../TOPs/Text_TOP.md "Text TOP") - When input texture is composited with 'Over' operation, the alpha is clamped. This makes it consistent with [Composite TOP](../TOPs/Composite_TOP.md "Composite TOP").
  * [Layer Mix TOP](../TOPs/Layer_Mix_TOP.md "Layer Mix TOP") - Optimized wired inputs to stop cooking when opacity is zero.
  * [Layer Mix TOP](../TOPs/Layer_Mix_TOP.md "Layer Mix TOP") - Fixed a hang that could occcur when using 'Bypass' parameter and and bug that incorrectly evaluated the WxH resolution on the Common page when using Output Resolution size mode. **Note:** The latter fix could introduce backwards compatibility issues for networks depending on Layer Mix TOP's final resolution.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - Fixed FPS being reported slightly wrong in some cases.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - Fixed 4K files output using ProRes not showing online previews correctly (such as on Dropbox).
  * [NVIDIA Background TOP](../TOPs/NVIDIA_Background_TOP.md "NVIDIA Background TOP") - Fixed background artifacts and added a new mode options to segment chairs as foreground or background.
  * [NVIDIA Background TOP](../TOPs/NVIDIA_Background_TOP.md "NVIDIA Background TOP") / [NVIDIA Denoise TOP](../TOPs/NVIDIA_Denoise_TOP.md "NVIDIA Denoise TOP") / [NVIDIA Upscaler TOP](../TOPs/NVIDIA_Upscaler_TOP.md "NVIDIA Upscaler TOP") - Updated bounds checking condition for input image resolution
  * [OpenColorIO TOP](../TOPs/OpenColorIO_TOP.md "OpenColorIO TOP") - Added a Display transform option to the Pre-Xform page. Renamed option to 'Inverse Display' and removed the Direction parameter. Fixed a few missing entries from each menu.
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Fixed supported properties failing to populate fully for the 'Properties CHOP' parameter.
  * [Ramp TOP](../TOPs/Ramp_TOP.md "Ramp TOP") - Fixed flickering issue that can occur in some cases.
  * [Render TOP](../TOPs/Render_TOP.md "Render TOP") - Simplified the 'Anti Alias' menu to have less options. The low/medium/high differences did not do anything since the change to Vulkan graphics API in 2022 (previously supported on OpenGL).
  * [Screen Grab TOP](../TOPs/Screen_Grab_TOP.md "Screen Grab TOP") - Now works correctly when using a working [Color Space](https://docs.derivative.ca/Color_Space "Color Space").
  * [Shared Mem In TOP](../TOPs/Shared_Mem_In_TOP.md "Shared Mem In TOP") / [Shared Mem Out TOP](../TOPs/Shared_Mem_Out_TOP.md "Shared Mem Out TOP") - Now works correctly with [Color Spaces](https://docs.derivative.ca/Color_Space "Color Space").
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Added some advanced controls for IDS Peak cameras and added support for manual capture triggering and Presets.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - [Bluefish444](../Interoperability/Bluefish444.md "Bluefish444") cards are now enabled and added support for Timecode output for BlueFish devices.

**CHOP**
  * [Audio File In CHOP](../CHOPs/Audio_File_In_CHOP.md "Audio File In CHOP") - 'Open Timeout' is now respected when downloading a remote file via the file path.
  * [DMX In CHOP](../CHOPs/DMX_In_CHOP.md "DMX In CHOP") - Fixed incorrect reporting of `packet_rate` value when receiving sACN or KiNET.
  * [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") - Fixed not sending at correct rate (specified by the parameter) when in 'Packet Per Channel' mode.
  * [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") - Fixed a stall when sending to an invalid mDNS address (regression from build 2025.31550).
  * [Lag CHOP](../Glossary/Lag_CHOP.md "Lag CHOP") - Added new 'Snap' parameter which allows to snap the lag value to the input CHOPs values when within threshold.
  * [LFO CHOP](../CHOPs/LFO_CHOP.md "LFO CHOP") / [Noise CHOP](../CHOPs/Noise_CHOP.md "Noise CHOP") - Fixed an issue where updating the 'Channel Name' parameter would create extra channels.

**DAT**
  * [DMX Map DAT](https://docs.derivative.ca/DMX_Map_DAT "DMX Map DAT") - Fixed incorrect **dmxfixture** and **channelname** values when referencing a [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") that merges multiple [DMX Fixture POPs](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") together.
  * [SocketIO DAT](../Interoperability/SocketIO_DAT.md "SocketIO DAT") - Added 2 new table inputs for specifying 'Query Parameter' and 'Auth' connection options.
  * [Text DAT](../Glossary/Text_DAT.md "Text DAT") - Fixed slowdown or freeze when generating info text on large DATs.
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT") / [WebSocket DAT](../Interoperability/WebSocket_DAT.md "WebSocket DAT") - Fixed increased CPU load for idle connections (regression from build 2025.31550).

**MAT**
  * [GLSL MAT](../MATs/GLSL_MAT.md "GLSL MAT") - Added `#define TD_SHADOW_MAP_RENDER` define when the material is used inside a shadow map rendering operation in a [Light COMP](../Glossary/Light_COMP.md "Light COMP").

**Misc**
  * [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") - Fixed an issue which caused some internal events to be lost in TouchEngine.
  * Fixed crash that occurs sometimes when creating Color attributes for POPs. Likely occurred in other cases of changing color space for parameters as well.
  * Fixed poor performance if an unsupported [Window Pixel Format](../Interoperability/Color_Space_Workflows.md#Working_Color_Space_2 "Color Space Workflows") is selected.
  * Fixed Drag-n-drop callback acceptance of text-only and other python generated drag items.
  * Fixed case where some 3rd party applications would stop responding to mouse interactions after interacting with TouchDesigner's UI.

###  Operator Snippets and Examples

  * A number of POP snippets were updated.
  * We recommend redownloading [POP Examples Files](https://www.dropbox.com/scl/fo/dvvqnl61dgmicxoebl4sy/AFuNixO4WWcAbyM5KkUi9F4?rlkey=f152v4uuzou81c7477w1yf6im&st=zzro8oie&dl=0) as we continue to update and improve them with each release.

##  Build 2025.31760 Nov 17, 2025

###  Hotfix for 2025.31740

  * [Feedback TOP](../TOPs/Feedback_TOP.md "Feedback TOP") - Fixed regression that broke the 'Reset' parameter in 3025.31740.

###  New Python

  * [WebsocketDAT Class](../DATs/WebSocket_DAT_Class.md "WebsocketDAT Class")`.sendFrame`/`.sendBinary` - Fixed a long stall on send in certain cases.

###  New Palette

  * [Palette:popDialog](https://docs.derivative.ca/Palette:popDialog "Palette:popDialog") - Fixed edit mode so undos aren't created. Fixed edge case esc/enter behavior.
  * [TDAbleton](../Interoperability/TDAbleton.md "TDAbleton") - 2.6.4
    * Eliminated int size error in OSC3.
    * Fixed channel deletes in ableton components.
    * Fixed updating of arrangement clips when new clips are added in Live.
    * Fixed bad OSC ports on load in Max Devices.
    * Fixed file descriptor problem on mac by using selectors.
    * Fixed some craziness in rack in/out controls.
  * [Widgets](../Glossary/Widgets.md "Widgets") - v2.2.8
    * Widget label parameter mapping fix for 'Scalefit' parameter.

###  Bug Fixes and Improvements

  * Updated to SDK v1.0.0.136 - [Notch TOP](../TOPs/Notch_TOP.md "Notch TOP")
  * Fixed crash that can occur when using some POPs, in particular the [ReRange POP](../POPs/ReRange_POP.md "ReRange POP").

**COMP**
  * [Actor COMP](../COMPs/Actor_COMP.md "Actor COMP") - Fixed incorrect xform initialization when instancing in some cases.
  * [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP") - Removed non-applicable viewer options from shortcuts and right-click menu.
  * [Light COMP](../Glossary/Light_COMP.md "Light COMP") - Fixed 'Custom Shadow Maps' not working correctly.

**POP**
  * [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") - Changed Tex attribute to always be imported as a float3.
  * [CPlusPlus POP](../POPs/CPlusPlus_POP.md "CPlusPlus POP") - Fixed the 'SampleShapesPOP' example that did not work when no inputs were connected.
  * [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Fixed send rate using timeline rate rather than the 'Rate' parameter value.

**TOP**
  * [Monochrome TOP](../TOPs/Monochrome_TOP.md "Monochrome TOP") - New 'Clamp to [0,1]' parameter to disabling clamping the output to [0,1] always.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - Fixed output resolution not being correct when deinterlacing is enabled.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") / [Point File In TOP](../TOPs/Point_File_In_TOP.md "Point File In TOP") - New option for adding a Callbacks DAT with `onPreloadDone()` callback.
  * [Notch TOP](../TOPs/Notch_TOP.md "Notch TOP") - Updated to SDK v1.0.0.136
    * Automatically convert between TouchDesigner's and the Notch Block layer's working color spaces.
    * Added support for exposed generic float arrays (previously only Pos/EulerScale, Matrix 4x4, and Pos/Quat/Scale were supported).
  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Changed Specify IP toggle parameter to 'Device Source' menu parameter. Also fixed ethernet device being destroyed when using IP address while ethernet device has already been created from Device menu parameter.
  * [Script TOP](../TOPs/Script_TOP.md "Script TOP") - Fixed cooking of downstream nodes with `CookLevel::ALWAYS` and `CookLevel::WHEN_USED`
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Fixed 'Allow Fallback Selection' parameter not working when set to Off.

**CHOP**
  * [Audio Movie CHOP](../CHOPs/Audio_Movie_CHOP.md "Audio Movie CHOP") - New `preload()` method that should be used when preloading a [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") that is using audio.
  * [Audio VST CHOP](../CHOPs/Audio_VST_CHOP.md "Audio VST CHOP") - Added 'Mode' parameter that allows for selection of plugin modes available within the .vst3 file.
  * [Delay CHOP](../CHOPs/Delay_CHOP.md "Delay CHOP") - Added new Reset toggle and pulse parameters. Resetting clears the delay memory, and when reset toggle is on, it matches the input CHOP.
  * [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") - Allow merging of DMX Channel blocks with different Value Sources (ie. Attribute vs. Constant)
  * [DMX In CHOP](../CHOPs/DMX_In_CHOP.md "DMX In CHOP") - Fixed a hang on closing TouchDesigner when using the destaddress column or when 'Discard Broadcast Packets' is enabled.
  * [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") / [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") - Fixed send rate using timeline rate rather than the 'Rate' parameter value.
  * [Filter CHOP](../Glossary/Filter_CHOP.md "Filter CHOP") - Fixed an issue that would occur with filter type 'Left Half Box' and 'Filter Per Sample' toggled on, where the output would differ based on the 'Time Slice' parameter value despite it being disabled.
  * [Pattern CHOP](../CHOPs/Pattern_CHOP.md "Pattern CHOP") - Fixed regression that broke the Pattern CHOP's `me.chanIndex`.
  * [Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP") - Fixed cooking of downstream nodes with `CookLevel::ALWAYS` and `CookLevel::WHEN_USED`
  * [Trigger CHOP](../CHOPs/Trigger_CHOP.md "Trigger CHOP") - Added 'Release' pulse parameter to instantly send the CHOP into Release stage. Also added new 'Reset' toggle and pulse parameters. Instantly completes the envelope.

**DAT**
  * [Script DAT](../DATs/Script_DAT.md "Script DAT") - Fixed cooking of downstream nodes with `CookLevel::ALWAYS` and `CookLevel::WHEN_USED`
  * [Web Client DAT](../Interoperability/Web_Client_DAT.md "Web Client DAT") - Fixed a hang when setting 'Maximum Lines' to 0 in Request Table Output mode.
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT") - Fixed encoding of 'pars' and 'uri' string values in the request dictionary that's passed into onHTTPRequest.

**SOP**
  * [Script SOP](../SOPs/Script_SOP.md "Script SOP") - Fixed cooking of downstream nodes with `CookLevel::ALWAYS` and `CookLevel::WHEN_USED`

**Misc**
  * Fixed bug that prevented the grid scale text from drawing if the origin was turned off.
  * Fixed crash when trying to display POP overlays without a P buffer.
  * Fixed a problem with 3D viewers not syncing when adaptive homing is disabled.
  * Fixed a problem with TOP point view settings not updating correctly.
  * Fixed issues correctly displaying double and integer POP attribute overlays.
  * Fixed a problem with nodes not updating their file paths when a parents path behavior changes.

##  Build 2025.31550 Oct 30, 2025

###  Release Highlights

####  Point Operators - POPs

#####  Introduction to POPs - 3D Geometry on the GPU

Introducing [POPs](../POPs/POP.md "POP"), aka Point Operators! POPs are a new family of operators that run on the GPU and create or modify 3D data. Points are the building blocks of polygons, lines, line strips, spline curves, point clouds, particle systems, any 3D geometrical shape and any form of data points.

Every POP contains a set of points with a set of Point Attributes. The most common attribute is Position (`P`), the position in 3D space of the points. The POP may have other attributes like Color (`Color` - with a red, green, blue and alpha component) and Normal (`N` - a direction vector with 3 components). The points can also have extra user-defined attributes or can get attributes automatically-generated from certain POP operators.

To learn about POPs, please visit our **[Learning About POPs](https://www.notion.so/3f7645a368a043f99cd143e2382b8ab0?pvs=25)** article here for an in-depth look at what's behind this exciting new OP family. Download the [POPs Examples Package](https://www.dropbox.com/scl/fo/dvvqnl61dgmicxoebl4sy/AFuNixO4WWcAbyM5KkUi9F4?rlkey=f152v4uuzou81c7477w1yf6im&st=zzro8oie&dl=0) to learn and try out a bunch of examples.

#####  Import/Export Geometry and Points

We have many ways to get your data into POPs. The [File In POP](../POPs/File_In_POP.md "File In POP") loads simple geometry in .obj and .classic/.bhclassic formats and the [Point File In POP](../POPs/Point_File_In_POP.md "Point File In POP") handles common point cloud file formats (.obj, .ply, .fits, .exr, .xyz, .pts, .csv, .txt). You can also use the [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP"), [USD COMP](../COMPs/USD_COMP.md "USD COMP"), and new [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") to bring those formats into POPs, including any animation in the files.

The new [File Out POP](../POPs/File_Out_POP.md "File Out POP") allows you to write out POP contents either as a single file or as file sequences! This includes point, geometry and scene file types. You can record a sequence of .obj or .exr files by setting the 'Type' parameter to 'File Sequence'. Some file formats have fixed attributes that the File Out POP looks for such as the .spz and .obj file formats, while other files types allow arbitrary attribute writing of attributes such as .exr and .ply formats.

#####  Geometry and POP node viewers)[")]

The [Geometry Viewer](../Interoperability/Geometry_Viewer.md "Geometry Viewer") and POP Node Viewers have a number of new display options added for working with POPs and geometry in general. These options can be found in the viewer's right-click menu.
  * POP Points - Display an overlay dot for each point in the scene (POPs only), keyboard shortcut 'd' to toggle this on and off.
  * Display Attribute Text - Display attribute data or indices as text overlayed on the geometry (POPs only).
  * Display Attribute Vector - Display multi-dimension attribute data as vector arrows overlayed on the geometry (POPs only). If the selected attribute is less than 3 dimensions, the missing dimensions will be assumed as 0. Attribute values are normalized so that vectors with smaller magnitudes will appear as smaller arrows.
  * Display Attribute Dots - Display single dimension attributes as a colored dot with a ring of red relative to the magnitude of the value. The smallest value in the scene appears as a solid blue dot and the largest value as a solid red dot.
  * Display Attribute Colors - Display multi-dimension attribute data as a colored dot (POPs only). The attribute is not normalized to preserve the color value which means attributes greater than one will appear solid white on most monitors.
  * The [Display Options](https://docs.derivative.ca/Display_Options "Display Options") dialog also has new options on the 'POP Overlays' page. Here you'll now find settings for Scale Attribute Overlays, Scale in Screen Space, Thin Attribute Range, and Thin Attribute Percentage.
  * In the 'Grids & Overlays' submenu, you'll find a collection of helpful new overlays, such as bounding box, axis and plane bounding projections, axis scale, and a toggle for grid.

####  Hardware Device Support

#####  New DMX Workflows with POPs

Data can also flow from POPs directly to other operator families, like Channel Operators (CHOPs) and then on to lasers, DMX or other external systems. While DMX was previously handled in TouchDesigner exclusively by the DMX In and Out CHOPs, we have introduced a set of new DMX POP operators enabling powerful new workflows for lighting, LEDs and anything operating on DMX.

First we introduce the [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") which lets you setup all the channels in your fixture's profile. Each point and primitive in the DMX Fixture POP's input will represent a copy of this fixture, inherently giving you a position in 3D space for every fixture in your setup. From here, the DMX Fixture POP will construct all the channels and universes required to address all your fixtures. Second, the new [DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") takes one or more DMX Fixture POPs, merges all the universes and sends the data out to your DMX, Art-Net, sACN, KiNET, or FTDI devices. A third new operator, the [DMX Map DAT](https://docs.derivative.ca/DMX_Map_DAT "DMX Map DAT"), is useful for visualizing DMX universe and channel layouts and can be helpful for troubleshooting channel conflicts between DMX fixtures. You'll find a DMX Map DAT docked to every DMX Out POP ready to help.

Last but not least, a new [Pan Tilt CHOP](../CHOPs/Pan_Tilt_CHOP.md "Pan Tilt CHOP") has been introduced to make it easier to control lighting fixture's pan and tilt controls directly, something that previously wasn't trivial using raw rotational values in CHOPs.

#####  Laser Upgrades

  * [Laser CHOP](../CHOPs/Laser_CHOP.md "Laser CHOP") - For this release the laser point generation process was overhauled, with improvements to blanking calculations, image sharpness/uniformity, point repeating, general stability, and taking input directly from POPs. The Laser CHOP was developed with the help of [LaserAnimation Sollinger](https://laseranimation.com/en/) who guided us in speccing and implementing the necessary parameters, especially in regards of the blanking timing settings.
    * The new Laser CHOP introduces the notion of Corner Points. Previously, everything could've been considered a "Corner Point", but now with the use of input attributes/channels (`LasCorner` and `lascorner`), corner points can be selected. In contrast, all non-Corner Points are considered Guide Points. Corner Points are repeatable to enable sharper and more defined lines. Guide Points are never repeated and only serve to guide the laser along a desired path, while at the same time not consuming extra points from the laser device's point buffer because they do not follow the same repeating rules as Corner Points.
    * Additionally, there are extra input attributes/channels that allow for extra per-Corner Point control on point repeating: "`LasCornerHoldAdd`" (SOP/POP) or "`lascornerholdadd`" (CHOP) and "`LasCornerHoldLookupFactor`" (SOP/POP) or "`lascornerholdlookupfactor`" (CHOP)
    * A new 'Closed Shape Overlap' parameter adds overlapping points at the start/end of a shape to create a more uniform shape by removing hot-spots (like those introduced by start point hold time for example) via color interpolation.
    * A new 'Interpolate Colors' parameter enables color interpolation between points.
  * [Pangolin CHOP](../CHOPs/Pangolin_CHOP.md "Pangolin CHOP") - Added support for using POPs an an input. Also added 'Zone' attribute override for POP inputs.
  * [Laser Device CHOP](../CHOPs/Laser_Device_CHOP.md "Laser Device CHOP") - Helios SDK Updated - Added an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") channel that reports whether the device supports extended frames. If extended frames are supported on the device, then there is now support for full 16-bit color and position, as well up to 4 optional user channels (user1, user2, user3, user4).

#####  Stereolabs ZED Cameras

ZED Operators received an SDK Update and an overhaul to their workflow to make it more consistent with other camera devices.
  * [ZED](../Interoperability/ZED.md "ZED") - ZED CHOP, ZED POP and ZED SOP now must point to a ZED TOP to access the camera, this is a **Backward Compatibility Issue** in which old files will need to be updated to this new setup that leverages the ZED TOP. A new [ZED Select TOP](../TOPs/ZED_Select_TOP.md "ZED Select TOP") let's you select different image streams from a [ZED TOP](../TOPs/ZED_TOP.md "ZED TOP") so you can work with multiple streams at once.
  * [ZED](../Interoperability/ZED.md "ZED") - Updated the SDK to 5.0.2 and added access to a number of new features. This now supports Blackwell NVIDIA GPUs (Geforce 5xxx), but no longer supports Pascal NVIDIA GPUs (Geforce 1xxx, P-series Quadros).
  * [ZED TOP](../TOPs/ZED_TOP.md "ZED TOP") - New Features
    * Support for new image type called 'Mask', that provides a single mask from detection bodies with tracking ID as pixel value.
    * Added support for SVO2/SVO file playback via 'File' parameter. SVO2/SVO are Stereolabs ZED file formats which let you record data from ZED cameras and play it back later with full access to all the data and image types.
    * Added support for network streaming data from another machine using ZED native streaming.
    * Added a new parameter 'Disable Self Calibration' that disables automatic self-calibration process that occurs when opening the camera by default.
  * [ZED CHOP](../CHOPs/ZED_CHOP.md "ZED CHOP") - New Features
    * Added support for 38 joint body tracking.
    * Support for 2D, 3D and head 3D bounding boxes in ZED CHOP by turning on the 'Bounding Boxes' toggle.

#####  Orbbec Cameras

  * [Orbbec TOP](../TOPs/Orbbec_TOP.md "Orbbec TOP") - Upgraded the Orbbec SDK to 1.10.16 which this is compatible with Orbbec Femto Mega firmware v1.3.0+.
    * Upgraded Kinect Azure wrapper (K4A) to 1.10.3.
    * Orbbec SDK now has support for Intel-based Macs, previously it was for Apple Silicon only.

#####  ST2110

ST2110 is a set of industry standards defining professional media over an IP network, delivering uncompressed video and audio streams, timing data, and ancillary data streams using existing network infrastructure technology.
  * [ST2110 In TOP](../TOPs/ST2110_In_TOP.md "ST2110 In TOP") / [ST2110 Out TOP](../TOPs/ST2110_Out_TOP.md "ST2110 Out TOP") - New input/output TOPs for ST2110 devices such as the Blackmagic IP range and Deltacast DELTA-ip-ST2110.
  * [ST2110 Device CHOP](../CHOPs/ST2110_Device_CHOP.md "ST2110 Device CHOP") - A new CHOP used to configure the ST2110 NIC (DHCP/IP Settings). The ST2110 TOPs reference this node to determine the available channels to send data out of the configured NIC.

#####  Serial Devices

  * [Serial Devices DAT](../DATs/Serial_Devices_DAT.md "Serial Devices DAT") - A new DAT that lists the available serial ports and identifies if a port is in use or not.

####  Color Space Workflow

  * [Color Space Workflows](../Interoperability/Color_Space_Workflows.md "Color Space Workflows") - A new 'Color' tab in the Preferences Dialog exposes [Color Space](https://docs.derivative.ca/Color_Space "Color Space") controls. _These settings are saved per-project_ , so a change in any settings on this page requires saving the project.toe file and restarting the project. See articles [Color Space](https://docs.derivative.ca/Color_Space "Color Space") and [Color Space Workflows](../Interoperability/Color_Space_Workflows.md "Color Space Workflows") for details and usage.
    * Set the project's working color space between **sRGB Linear** , **ACEScg** , **DCI-P3 Linear** , **Rec. 2020 Linear** , or **ACES 2065-1**. Passthrough is the default which doesn't change anything in TouchDesigner's color behavior from older versions, this will keep old projects working the same as before.
    * Set the Window Pixel format to **SDR 8-bit** , **SDR 10-bit** , **HDR 10-bit** , or **HDR 16-bit Float**.
    * Separate settings for 'Reference White Nits' for both SDR and HDR.
    * A setting for 'UI Reference White' controls TouchDesigner's interface and more generally [Panel COMPs](../Glossary/Panel_Component.md "Panel Component") to set their reference white brightness.
    * When working with HDR Window Pixel Formats, all content viewers, node viewers etc. will be displayed in HDR making if easy to preview your work.

####  3D Texture Support

  * Most TOPs now natively support 3D Textures and 2D Arrays. Feeding one of the following TOPs a 3D Texture source will now perform that operation on the 3D Texture.
    * List of TOPs - Add, Blur, Channel Mix, Chroma Key, Composite, Constant, Convolve, Cross, Difference, Displace, Edge, Emboss, Feedback, Flip, Function, HSV Adjust, HSV to RGB, Inside, Lens Distort, Level, Limit, Luma Blur, Luma Level, Math, Matte, Mirror, Mono, Multiply, Noise, Outside, Over, Remap, Reorder, Screen, Slope, Subtract, Reorder, Threshold, Under.
    * [TOP to CHOP](../CHOPs/TOP_to_CHOP.md "TOP to CHOP") and [TOP to POP](../POPs/TOP_to_POP.md "TOP to POP") also work with 3D Textures or 2D Arrays.

####  New Operators

New Operators not mentioned above are highlighted here.
  * [Layer Mix TOP](../TOPs/Layer_Mix_TOP.md "Layer Mix TOP") - The new Layer Mix TOP lets you composite unlimited image layers in a layer stack with individual adjustment controls for each layer. To avoid clutter and unneeded parameters, you can select only the adjustment controls you want by enabling them. You can also specify a background plate to composite your layers over.
  * [Render Simple TOP](../TOPs/Render_Simple_TOP.md "Render Simple TOP") - A new TOP to render geometry without needing extra scene objects like a camera or lights.
  * [NVIDIA RTX Video TOP](https://docs.derivative.ca/NVIDIA_RTX_Video_TOP "NVIDIA RTX Video TOP") - A new TOP that leverages the NVIDIA RTX Video SDK for AI-enhanced video processing. This custom TOP enables RTX Video Super Resolution and RTX Video HDR effects to improve sharpness, clarity, and automatically convert SDR video to HDR within TouchDesigner workflows.

####  Pattern Matching

Some parameters in TouchDesigner are used to specify multiple operators, multiple channels, multiple points, etc. For example, the Render TOP allows for multiple lights, geometry COMPs and cameras to be specified in its parameters. The Join CHOP and Composite TOP accept multiple CHOPs and TOPs respectively. A parameter that is a "pattern" allows you to specify several names and/or specify "wild cards" which will match all or parts of the names of operators, channels, point indexes etc. Some examples, 1) `r[xyz]` matches channels rx, ry and rz, 2) `*foot*` matches each channel that has "foot" in it, with anything or nothing before or after it.

We are introducing an new update to [Pattern Matching](../Glossary/Pattern_Matching.md "Pattern Matching") that is consistent throughout the product. Refer to the [Pattern Matching](../Glossary/Pattern_Matching.md "Pattern Matching") documentation for details on the usage. Note: There is a 'Legacy Features' section below. Some uses of it are obsolete but we have legacy modes that allow older patterns and files to continue to work as-is.

The new **Pattern Matching** includes many improvements outlined here:
  * **String patterns**
    * Now all string patterns use the same pattern matching so you get consistent results. Previously, some nodes would be able to match `geo[2-3,5]` while others couldn't (ie. [Render TOP](../TOPs/Render_TOP.md "Render TOP")), now they all can.
    * Any string pattern can now use Set Notation for matching (if shown as supported [this table](../Glossary/Pattern_Matching_Support.md "Pattern Matching Support")).
      * Now _space separated patterns_ are consistently treated as OR, whereas previously these was different for different parameters.
      * **Recommended:** Use "`&`" and "`|`" symbols for more explicit syntax, for example: `^fit5 & ^fit5` and `^fit5 | ^fit6` are more explicit and preferred versus `^fit5 ^fit6`
  * **Index patterns** - Functionally index pattern matching works similar to the previous notation except ranges are now surrounded by a brackets, _not_ should use ^, improvements to take notation, and now supports set matching for non ordered.
    * Index patterns used to be differentiated by not having any square brackets, i.e. `0-10:2,3`. Now they also use brackets which is more consistent with string patterns, ie. `[0-10:2]` would be valid for both a new index and string pattern.
    * Using ^ instead of ! for _not_ , for example: `^5` versus `!5` (in SOPs you were even able to use ! and ^ together, i.e. `^!50-70`, not possible in new matching).
    * 'Take' notation has changed. We used to say `0-15:2,3` for "Take the first 2 of every 3 points, i.e. 0,1,3,4,6,7...), now we use `[0-15:2:4]`
    * Take notation now supports `[*:2]` notation, take every second entry from "*" which ranges from 0-maximum number of points (similarly for ordered ranges from 0-10 in that order).
    * POPs indices exclusively use the new syntax. Set matching is supported for non ordered ranges (such as those in [Primitive POP](../POPs/Primitive_POP.md "Primitive POP")).
  * **Set Matching** - The pattern matching rules above can be used in conjunction with [set operator notation](../Glossary/Pattern_Matching.md#Set_Operator_Notation "Pattern Matching") for more expressive selection. Basic, Operator and Index Patterns (i.e. `/project/geo1`, `t?`, `chan*`, `blend[2-6:2]`) create sets and |, &, ~ can apply set operations between them.
  * **Additional Notes**
    * Any string pattern should have been updated (except those that were old/deprecated).
    * POPs all use the new index pattern matching described above.
    * The [Delete CHOP](../CHOPs/Delete_CHOP.md "Delete CHOP"), [Reorder CHOP](../CHOPs/Reorder_CHOP.md "Reorder CHOP") and [Sort CHOP](../CHOPs/Sort_CHOP.md "Sort CHOP") have a 'Legacy Pattern Matching' toggle for using older style index pattern matching for backward compatibility.
    * SOPs Index pattern matching have been left unchanged.

####  Metadata support

  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - Added support for Exif metadata writing for .png, .jpeg and .tiff file formats.
  * [Audio File Out CHOP](../CHOPs/Audio_File_Out_CHOP.md "Audio File Out CHOP") - Added support for writing metadata to .wav, .mp3, .ogg, .aiff audio file formats.
  * [Media File Info DAT](../DATs/Media_File_Info_DAT.md "Media File Info DAT") - Added support to read Exif metadata.
  * Added new member `.metadata` to [Media File Info DAT](../DATs/Media_File_Info_DAT.md "Media File Info DAT"), [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") and [Audio File In CHOP](../CHOPs/Audio_File_In_CHOP.md "Audio File In CHOP").

####  Operator New Features

There are over 100 additional new features added to TouchDesigner operators in this release. Below we list everything ordered by OP family.

#####  COMP Features

  * [Button COMP](../COMPs/Button_COMP.md "Button COMP") - New parameters to adjust the text on the button's label, including 'Scale Text to Fit', 'Font Size', 'Line Spacing', and 'Text Padding'.
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") - Added new "Allow UI" parameter which controls the ability of components (.tox files) loaded in the Engine COMP to open floating windows (using Window COMPs).
  * [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP") / [USD COMP](../COMPs/USD_COMP.md "USD COMP") - Added an 'Import POPs' parameter which will create POPs in place of SOPs when importing geometry. The default is 'On' to import using POPs.
  * [Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP") - New 'Face Camera' parameter to make text face the camera regardless of orientation.
    * Added depth-based scaling parameters (similar to the [Line MAT](../MATs/Line_MAT.md "Line MAT")) to control text scaling based on distance from the camera.
    * Added 'Width Affected by FOV/OrthoWidth' parameter (similar to the Line MAT) to make sizing field-of-view independent.
    * Added 'Lift Towards Camera' parameter.
    * 'Width Affected by FOV' and 'Lift Towards Cam' parameters work with Orthographic camera type.
    * 'Face Camera' behavior rotates about the anchor point of the layout box.
    * All of the above new features work independently for each camera. For example, with the 'Face Camera' parameter toggled on, the text will face each camera it is viewer from.
  * [List COMP](../COMPs/List_COMP.md "List COMP") - New attribute `topFill` controls the way a Background TOP will fill: `fillMode.STRETCH`, `HORIZONTAL`, `VERTICAL`, `BEST`, `NATIVE`, `OUTSIDE`

For example
```
def onInitRow(comp, row, attribs):
	attribs.top = op('out1')
	if (row%2 == 0):
		attribs.topFill = FillMode.VERTICAL
	else:
		attribs.topFill = FillMode.HORIZONTAL
	return
```

  * [Panel COMPs](../Glossary/Panel_Component.md "Panel Component") - All Panel Components received these updates.
    * On the Look parameter page, a new 'TOP Fill' menu option 'Fill Outside' fills the available area by cropping rather than stretching the image.
    * On the Drag/Drop parameter page you'll find:
      * In the 'When Dragging This' parameter menu there is now an option to 'Fill Custom Parameter' to easily fill a single parameter without need of setting up a callback.
      * 'Built-In Drop Options' toggle controls whether or not built-in options are included when dropping onto this node.
  * [Text COMP](../COMPs/Text_COMP.md "Text COMP") - New Features
    * Added 'Placeholder Text' that is displayed when the text contents are empty.
    * Added new parameters adjusting drop shadows, including control over color, alpha, and offset.
  * [Window COMP](../Glossary/Window_COMP.md "Window COMP") - New features
    * Added parameters to control 'Output Color Space' and 'Output Reference White' when [Working Color Space](https://docs.derivative.ca/Color_Space "Color Space") is set to a color space other than 'Passthrough'.
    * A 'Prevent Display Sleep' toggle parameter has been added to keep your display from going to sleep regardless of power saving modes set on the system.
    * Renamed "monitor" to "display" in parameters, menus and warnings.

#####  TOP Features

  * Composite TOPs can now use Justify Horizontal and/or Justify Vertical parameters when 'Pre-Fit Overlay' is set to Fit Vertical, Fit Horizontal or Fit Best modes. Which justify parameters are enabled depends on the mode selected, for example Fit Vertical can only be justified horizontally and Fit Horizontal can only be justified vertically. This has been added to the following TOPs: [Composite TOP](../TOPs/Composite_TOP.md "Composite TOP") / [Over TOP](../TOPs/Over_TOP.md "Over TOP") / [Cross TOP](../TOPs/Cross_TOP.md "Cross TOP") / [Difference TOP](../TOPs/Difference_TOP.md "Difference TOP") / [Add TOP](../TOPs/Add_TOP.md "Add TOP") / [Inside TOP](../TOPs/Inside_TOP.md "Inside TOP") / [Multiply TOP](../TOPs/Multiply_TOP.md "Multiply TOP") / [Screen TOP](../TOPs/Screen_TOP.md "Screen TOP") / [Subtract TOP](../TOPs/Subtract_TOP.md "Subtract TOP") / [Under TOP](../TOPs/Under_TOP.md "Under TOP") / [Outside TOP](../TOPs/Outside_TOP.md "Outside TOP")
  * [Corner Pin TOP](../TOPs/Corner_Pin_TOP.md "Corner Pin TOP") - Added 'Mapping' parameter to the 'Extract' page for option between Bilinear and Perspective extraction.
  * [CPlusPlus TOP](../TOPs/CPlusPlus_TOP.md "CPlusPlus TOP") - Added `TOP_Output::getSuggestedOutputDesc()` to help decide what resolution the node should output based on the 'Common' page parameters.
  * [Displace TOP](../TOPs/Displace_TOP.md "Displace TOP") - New 'Aspect Correct' parameter added for mapping the displace weights to be aspect correct.
  * [Math TOP](../TOPs/Math_TOP.md "Math TOP") - A new 'Fix Invalid Values' menu was added to handle bad pixel values, allowing for conversion of _NaNs_ to Zero and _Infs_ to One.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - New features.
    * The 'Index' parameter can now be a negative number. When negative the index will cycle back through the movie.
    * Added 'Pre-Download HTTP Addresses' parameter. This was the default behavior before, but now can be turned off.
    * Added support for reading some forms of `.ktx` files.
    * Added 'HLG Peak Nits' parameter to control the peak nits for HLG encoded content.
    * 'Hardware Decode' now defaults to On.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - New features.
    * Added support for VVC (Versatile Video Coding), also known as H.266.
    * Added support for encoding AV1 codec video (on newer NVIDIA GPUs).
    * Added support for encoding AAC codec audio.
    * Added support for encoding Opus codec audio.
    * Added 'Stereo Mode' and 'Spherical Mode' parameters to write out metadata for stereo and spherical video content.
    * Added 'Leading Zeros Digits' parameter to specify the minimum number of suffix digits that the filename will have. If the sequence number is less than this number, then leading zeros are appended so that the total number of suffix digits is at least this value.
  * [Noise TOP](../TOPs/Noise_TOP.md "Noise TOP") - Derivatives are now supported for Simplex 4D and Perlin 4D noise by turning on the 'Gradient' toggle on the Output page. For derivatives of 4D noise types, the 'Alpha' parameter will be disabled and the alpha channel will have the 4th component of the derivative.
  * [NVIDIA Background TOP](../TOPs/NVIDIA_Background_TOP.md "NVIDIA Background TOP") / [NVIDIA Denoise TOP](../TOPs/NVIDIA_Denoise_TOP.md "NVIDIA Denoise TOP") / [NVIDIA Upscaler TOP](../TOPs/NVIDIA_Upscaler_TOP.md "NVIDIA Upscaler TOP") - Upgraded to latest version of NVIDIA Maxine SDK. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. Requires Video Effects SDK for your GPU to be installed from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.
  * [OpenVR TOP](../TOPs/OpenVR_TOP.md "OpenVR TOP") - Is now [Color Space](https://docs.derivative.ca/Color_Space "Color Space") aware when used in a project with working color space set.
  * [Point File In TOP](../TOPs/Point_File_In_TOP.md "Point File In TOP") - Is now [Color Space](https://docs.derivative.ca/Color_Space "Color Space") aware when used in a project with working color space set.
  * [Render TOP](../TOPs/Render_TOP.md "Render TOP") - A few new parameters have been added.
    * Added a new 'Render' pulse parameter to render one frame when the 'Render' toggle parameter is turned off.
    * Added a new 'Background Color' parameter, which is combined with the [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP")'s Background Color to determine the final Background Color of the render.
    * For working with UV Unwrap workflows with POPs, a new 'UV Unwrap POP Coord Attribute' parameter has been added.
  * [Scalable Display TOP](../TOPs/Scalable_Display_TOP.md "Scalable Display TOP") - Added new parameter 'Apply Camera Offset' to use the camera offsets in [Scalable Atlas](https://www.scalabledisplay.com/products/scalable-atlas/) files.
  * [Script TOP](../TOPs/Script_TOP.md "Script TOP") - Added parameter 'Modify Outside of Cook' which when 'On' allows the TOP's output to be updated by an external script.
  * [Syphon Spout In TOP](../TOPs/Syphon_Spout_In_TOP.md "Syphon Spout In TOP") / [Syphon Spout Out TOP](../TOPs/Syphon_Spout_Out_TOP.md "Syphon Spout Out TOP") - Upgraded to SDK 2.007.014 which adds support for Sender FPS in [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") when enabled in the Spout Settings dialog.
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Extended device support and improvements.
    * Added support for Timecode over HDMI on [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") cards, to access this timecode use an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") on the Video Device In TOP.
    * Added support for the IDS Peak SDK, to support newer [IDS cameras](https://en.ids-imaging.com/).
    * [AJA](../Interoperability/AJA.md "AJA") devices can now use the 'Sync to Input Frame' with multiple inputs.
    * Now possible to capture up to 16 audio channels for [Deltacast](../Interoperability/Deltacast.md "Deltacast") devices.
    * Added support for [Deltacast](../Interoperability/Deltacast.md "Deltacast") cards that don't have bi-directional connectors and fixed enumeration of these Deltacast boards.
    * Added support for 10-bit input on [Bluefish444](../Interoperability/Bluefish444.md "Bluefish444") devices, you'll also find this support in the [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP").
    * Added 'frames_displayed' [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") channel.
    * Improved performance when using 'Media Foundation' library and the pixel format of the data stream is NV12.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Improved device support.
    * Added support for Timecode over HDMI on [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") cards using the 'Timecode Object/CHOP/DAT' parameter.
    * Added support for synchronized output for [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") devices.
    * Added support for 10-bit output on [Bluefish444](../Interoperability/Bluefish444.md "Bluefish444") devices.
    * Device selection is now more portable between machines, using a device index if the exact device can't be found.
  * [Video Stream In TOP](../TOPs/Video_Stream_In_TOP.md "Video Stream In TOP") - 'Hardware Decode' now defaults to On.
  * [Video Stream Out TOP](../TOPs/Video_Stream_Out_TOP.md "Video Stream Out TOP") - Some tuning parameters and improvements.
    * New 'Ultra High Quality' option in the 'Quality' menu.
    * Added support for AAC audio codec for RTMP and SRT modes, as such, the default audio codec has been changed to AAC.
    * Added support for AV1 codec for RTMP output.
    * Added support for H265/HEVC codec for Enhanced RTMP.
    * Added support for Opus audio codec when using SRT output.
    * Added parameters to force the 'Mux Size' and the 'VBV Buffer Size'.
    * Reduced audio dropouts when connection is unstable.
  * [Web Render TOP](../TOPs/Web_Render_TOP.md "Web Render TOP") - updates and improvements.
    * Updated to Chromium 132.0
    * The option to 'Use Shared Textures' in chromium (cef) on windows is back.
    * New parameter for 'DPI Scaling'.
    * New parameter to specify a table to 'Modify Request Headers'.
    * **Backward Compatibility Issue** - Using the same cache with 2 Web Render TOPs is no longer supported, the second one will error.

#####  CHOP Features

  * [Audio File Out CHOP](../CHOPs/Audio_File_Out_CHOP.md "Audio File Out CHOP") - Added support for big-endian .aiff formats.
  * [Audio Movie CHOP](../CHOPs/Audio_Movie_CHOP.md "Audio Movie CHOP") - Added a 'Volume' parameter for convenience.
  * [Audio Render CHOP](../Interoperability/Audio_Render_CHOP.md "Audio Render CHOP") - Added added a new 'Simulation' mode that supports multiple sources and scene meshes. Scene meshes have properties for absorption, scattering and transmission all of which is fed into the simulation which calculates air absorption, occlusion, and reflections.
    * On the Meshes parameter page, the static 'Mesh Objects/POPs/SOPs' parameter now supports multiple OPs.
    * Added 'Auto' mode for baking reflections which will automatically rebake when any parameter change occurs that necessitates it.
    * Added 'Baked Data Variation' parameter to switch simulation modes between 'Static Listener' and 'Static Source', where baked reflection data is calculated in reference to whichever objects are set to be static.
    * Added new parameters for attenuation (note this only works when reflections are disabled).
  * [Body Track CHOP](../Interoperability/Body_Track_CHOP.md "Body Track CHOP") - Upgraded to latest version of NVIDIA Maxine SDK. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. Requires AR SDK for your GPU to be installed from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.
  * [Clock CHOP](../CHOPs/Clock_CHOP.md "Clock CHOP") - Added a 'Countdown' mode. For the first input, any missing values are assumed to be midnight January 1st of specified year. The second input is entirely optional, missing values are taken from current time.
  * [Count CHOP](../CHOPs/Count_CHOP.md "Count CHOP") - Improvements
    * Added 'Count Up' and 'Count Down' momentary parameters to allow counting with no input connected.
    * Non-timesliced mode now uses all channels of the Increment input, not just the first. This allows you to specify separate count increments for channels on the first input by supplying multiple channels into the Increment input.
  * [DMX In CHOP](../CHOPs/DMX_In_CHOP.md "DMX In CHOP") / [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") - Better support for serial and DMXKing devices.
  * [DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") - Added 'ArtSync Timeout' parameter to specify the time in milliseconds that ArtSync will wait for all ArtDmx packets to complete sending before sending the ArtSync packet. If they have not all been sent when the timeout is reached, then ArtSync will terminate and the ArtSync packet will not be sent. Additionally, a new frame of ArtDmx packets will be sent and a new ArtSync will be initiated.
  * [Face Track CHOP](../Interoperability/Face_Track_CHOP.md "Face Track CHOP") - Upgraded to latest version of NVIDIA Maxine SDK. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. Requires AR SDK for your GPU to be installed from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.
  * [File In CHOP](../CHOPs/File_In_CHOP.md "File In CHOP") - Channel names now preserved when reading a .chan file into a CHOP. **** BACKWARD COMPATIBILITY **** Chan files now preserve channel names instead of always defaulting to chan1, chan2, chan3, ...
  * [Hokuyo CHOP](../Interoperability/Hokuyo_CHOP.md "Hokuyo CHOP") - Added new 'Local Address' parameter, helpful for when a system has multiple network interface cards.
  * [Parameter CHOP](../CHOPs/Parameter_CHOP.md "Parameter CHOP") - Added 'Sequences' parameter to better parse [Sequential Parameters](../Glossary/Sequential_Parameters.md "Sequential Parameters").
  * [Render Pick CHOP](../CHOPs/Render_Pick_CHOP.md "Render Pick CHOP") - Added 'Name Format' and 'Type Suffix' parameters to provide POP friendly naming.
  * [RenderStream In CHOP](../CHOPs/RenderStream_In_CHOP.md "RenderStream In CHOP") - Added support for multiple Scenes and Schemas.
  * [Resample CHOP](../CHOPs/Resample_CHOP.md "Resample CHOP") - Added new parameter 'Use Last Frame Only' to trim to the input's last frame and perform the resample on that.
  * [Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP") - Added parameter 'Modify Outside of Cook' which when 'On' allows the CHOP's output to be updated by an external script.
  * [Speed CHOP](../Glossary/Speed_CHOP.md "Speed CHOP") - New 'Speed' parameter that allows generating values when no inputs are connected.
  * [Stretch CHOP](../CHOPs/Stretch_CHOP.md "Stretch CHOP") / [Resample CHOP](../CHOPs/Resample_CHOP.md "Resample CHOP") - New interpolation method 'Repeat Samples' that provides better spaced results when lengths are integer multiples of original.
  * [Timecode CHOP](../CHOPs/Timecode_CHOP.md "Timecode CHOP") - Added an option to set custom length from a [Timecode Class](../TOPs/Timecode_Class.md "Timecode Class") object. Also added 'Extend Left' parameter and changed the Cycle toggle to be a menu named 'Extend Right'.
  * [Trigger CHOP](../CHOPs/Trigger_CHOP.md "Trigger CHOP") - Added 'Enable Remap Length' and 'Remap Length' parameters which will re-time the total length of the envelope to the specified length. Note that held sustain length is not remapped, only Delay, Attack, Peak, and Release lengths are remapped.

#####  DAT Features

  * [DATs](../Glossary/DAT.md "DAT") - Since newlines are supported in DAT cells, display them as symbols and allow them to be selected/deleted/copied etc.
  * [DAT Execute DAT](../DATs/DAT_Execute_DAT.md "DAT Execute DAT") - A new `onTableChange` method does everything now, the other 4 legacy methods (`onRowChange`, `onColChange`, `onCellChange`, and `onSizeChange`) are now deprecated.
  * [Multi Touch In DAT](../Interoperability/Multi_Touch_In_DAT.md "Multi Touch In DAT") - New features
    * New parameter 'Occlude Panels by Hierarchy' - Enables filtering out multitouch events by Panel Depth Layer.
    * New parameter 'Occlude Panels by Depth Layer' - Only children of the specified panel will receive multitouch events. Touches on parent and sibling panels are ignored.
    * New parameter 'Occlude Panels Above Depth' - Multitouch events from panels with a Depth Layer larger than this value will be ignored.
  * [Render Pick DAT](../DATs/Render_Pick_DAT.md "Render Pick DAT") - Added 'Name Format' and 'Type Suffix' parameters to provide POP friendly naming.
  * [Table DAT](../Glossary/Table_DAT.md "Table DAT") - Performance optimizations to make large tables cook significantly faster. As well, in the DAT viewer's right-click menu you'll find a new option to toggle the 'Auto Resize Columns' behavior on/off.
  * [Web Client DAT](../Interoperability/Web_Client_DAT.md "Web Client DAT") - Added 'Web Form' toggle that enables construction of MIME-formatted request, similar to using mimeParts in [WebclientDAT Class](../DATs/Web_Client_DAT_Class.md "WebclientDAT Class").request. When enabled, the second input will be interpreted as MIME parts rather than the request body.

#####  MAT Features

  * **TriPlanar texturing** ...
    * [PBR MAT](../MATs/PBR_MAT.md "PBR MAT") / [Phong MAT](../MATs/Phong_MAT.md "Phong MAT") - Added new menu 'Texture Sampling Mode' to PBR MAT and Phong MAT with options Regular, Screen Space Coordinates and Triplanar.
    * For backward compatibility, a new 'Texture Sample Mode' menu found in all texture map's extended parameters has been added to select between regular texture coordinates, screen space coordinates, or the new tri-planar mapping coordinates. The 'Screen Space Coordinates' option previously found under the 'Texture Coord' menu is now located in this new 'Texture Sampling Mode' menu.
    * Triplanar texture mapping can be selected using the 'Triplanar Mapping' option in the new mode menu. When using this mode, first triplanar texture attributes need to be generated via the [Texture Map POP](../POPs/Texture_Map_POP.md "Texture Map POP").
    * [Texture Map POP](../POPs/Texture_Map_POP.md "Texture Map POP") - The option 'Triplanar Coordinates (Point)' found in the 'Texture Type' menu will generate triplanar texture attributes on the geometry for use with triplanar mapping in the MATs above.
  * [MAT](../MATs/MAT.md "MAT") - All MAT operators now have a bypass flag.
  * [Point Sprite MAT](../MATs/Point_Sprite_MAT.md "Point Sprite MAT") - New menu 'Sizing Model' allows the depth based scaling of the sprites to be either via the 'Constant/Attenuate' model's 'Attenuate Point Scale' parameter or 'Perspective Correct' scaling like most geo objects.
    * Added 'Size Affected by FOV/OrthoWidth' parameter for 'Perspective Correct' mode to make scaling FOV independent or dependent.
  * [GLSL MAT](../MATs/GLSL_MAT.md "GLSL MAT") - Added `TDImageStore_*()` / `TDImageLoad_*()` functions to work with Image Outputs from the [Render TOP](../TOPs/Render_TOP.md "Render TOP"). Required for color correct values when using a working [Color Space](https://docs.derivative.ca/Color_Space "Color Space").
  * [Line MAT](../MATs/Line_MAT.md "Line MAT") - New auto-cleanup of memory used by the Line MAT when it's not used for a while.

####  Operating System Specific

  * [macOS](https://docs.derivative.ca/MacOS "MacOS") - Minimum requirements now macOS 12.0 Monterey.
  * [macOS](https://docs.derivative.ca/MacOS "MacOS") - Added support for hardware accelerated H.264 and HEVC/H.265 encoding with the [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP").
  * Windows and macOS - A minimum of 4GB GPU memory is required, we recommend 8GB or more.

####  Python Tools

  * TouchDesigner's Python version has been updated to **3.11.10**

#####  Python Autocomplete and Help in VScode

  * [TDI Library](https://docs.derivative.ca/TDI_Library "TDI Library") - The TDI Library enables popup help and code-completion when working with python in Microsoft Visual Studio Code (VS Code). It contains the help documentation and Python description of all built-in TouchDesigner objects, classes and functions. In addition to help and auto-completion, using TDI library will eliminate error and warning indicators when using VS Code to edit TouchDesigner Python.

#####  Tool Components for working with Python in TouchDesigner

  * [Thread Manager](https://docs.derivative.ca/Thread_Manager "Thread Manager") - A new system component and a set of palette components designed to facilitate Python threading in TouchDesigner.
    * Read our [Introduction to the Thread Manager](https://derivative.ca/community-post/enhancing-your-python-toolbox-touchdesigner%E2%80%99s-thread-manager/72022) for a walkthrough.
  * [Palette:tdPyEnvManager](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager") - A component to sideload and manage python virtual environments, conda environments, and third-party packages and libraries.
    * Read our [Introduction to the Python Environment Manager](https://derivative.ca/community-post/introducing-touchdesigner-python-environment-manager-tdpyenvmanager/72024) here.
  * Depth Anything V2 Tutorial - Depth Anything V2 is a machine learning library that can create depth information for images and videos. Check out [this tutorial](https://derivative.ca/community-post/custom-integration-thread-manager-support-third-party-python-library/72023) which uses both the _ThreadManager_ and the _TDPyEnvManager_ to get Depth Anything V2 running in TouchDesigner.
  * [Palette:logger](https://docs.derivative.ca/Palette:logger "Palette:logger") - v2.6.1 - Major overall. Improved by always initializing a Logger object reducing initialization issues and now including a QueueHandler to work in conjunction with the [Thread Manager](https://docs.derivative.ca/Thread_Manager "Thread Manager") mentioned above.

###  New Python

  * Python version updated to 3.11.10
    * Updated all extra Python packages we ship with to the latest versions.
    * Upgraded to NumPy 2.1.2.
  * Added [box python package](https://pypi.org/project/python-box/).
  * Added [tzdata python package](https://pypi.org/project/tzdata/) so the 'zoneinfo' package works correctly out of the box.
  * Added [pygdft](https://pypi.org/project/pygdtf/) and [pymvr](https://pypi.org/project/pymvr/) Python packages to TouchDesigner.
  * Individual parameter disabling within a [ParGroup](../Glossary/ParGroup.md "ParGroup")
  * [AbsTime Class](../Python/AbsTime_Class.md "AbsTime Class") - `.frame` `.seconds` now pause with main timeline.
  * [Camera Class](../Python/Camera_Class.md "Camera Class")`.frameBounds` - Added a new 'padding' keyword expressed as a fraction of the viewport height e.g. 0.1 puts a minimum 10% padding around all sides.
  * [Camera Class](../Python/Camera_Class.md "Camera Class") / [ArcBall Class](../Python/ArcBall_Class.md "ArcBall Class") - Added errors for unexpected arguments and keywords.
  * [Color Class](../Python/Color_Class.md "Color Class")`.colorSpacePrimaries(workingColorSpace)` -> ColorSpacePrimaries - This is a static function which can be called without a Color instance. It returns a ColorSpacePrimaries named tuple, for the given WorkingColorSpace.

```
   Args:
           workingColorSpace - One of the 'WorkngColorSpace' enum values.
   Example:
           Color.workingColorSpace(WorkingColorSpace.ACES_CG)
```

  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.progressiveUnload()` - Now errors if no argument provided for splitting the unload over multiple frames.
  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.progressiveUnloader` - This member is of type ProgressiveUnload Class.
  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.findChildren()` now updates properly when searching by value.
  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.layout(ops, horizontal=False, vertical=False, gridRows=0)` - Added a method to automatically layout operators.
  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.findChildren(renamed=True)` - Returns a list of children whose names have been edited, ie. any non-default name.
  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.collapseSelected()` returns a reference to the created Base COMP.
  * [COMP Class](../Python/COMP_Class.md "COMP Class")`.progressiveUnload()` - A new method to progressively unload the COMP's children over multiple frames. All 'PerFrame' options can be specified together. Unloading will move to next frame when one of the criteria gets met.
    * Additionally a [COMP Class](../Python/COMP_Class.md "COMP Class")`.progressiveUnloader` member has been added to query the progress of the progressiveUnload operation. See [ProgressiveUnload Class](https://docs.derivative.ca/index.php?title=ProgressiveUnload_Class&action=edit&redlink=1 "ProgressiveUnload Class \(page does not exist\)") below.
    * [ProgressiveUnload Class](https://docs.derivative.ca/index.php?title=ProgressiveUnload_Class&action=edit&redlink=1 "ProgressiveUnload Class \(page does not exist\)") - This new class describes a specific instance of the `COMP.progressiveUnload()` method. Methods and members of this class are used to obtain progress information about the underway progressive unload operation, or modify it.
  * [geometryCOMP Class](../COMPs/Geometry_COMP_Class.md "GeometryCOMP Class")`.bounds` / [SOP_Class](../SOPs/SOP_Class.md "SOP Class")`.bounds` - New functions for returning the bounds of the contained geometry. The 'render' and 'display' now default to False in contrast to the legacy `computeBounds` function. For example, calling `OP.bounds()` with no keywords will now always return bounds regardless of the state of the render. The legacy computeBounds function has been deprecated.
  * [geometryCOMP Class](../COMPs/Geometry_COMP_Class.md "GeometryCOMP Class")`.computeBounds` - COMPs that are not 3D Objects (ie. Base COMP, Panel COMPs, etc) are no longer included in bounds when the recurse keyword is used.
  * [geotextCOMP Class](../COMPs/Geo_Text_COMP_Class.md "GeotextCOMP Class")`.layoutText()` - This function now creates a dependency so that OPs using it will automatically recook when the Geo Text COMP changes.
  * [geotextCOMP Class](../COMPs/Geo_Text_COMP_Class.md "GeotextCOMP Class")`.layoutText()` - Returned positions now include vertical alignment and padding.
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") / [CPlusPlus TOP](../TOPs/CPlusPlus_TOP.md "CPlusPlus TOP") / [CPlusPlus DAT](../DATs/CPlusPlus_DAT.md "CPlusPlus DAT") / [CPlusPlus SOP](../SOPs/CPlusPlus_SOP.md "CPlusPlus SOP") / [CPlusPlus CHOP](../CHOPs/CPlusPlus_CHOP.md "CPlusPlus CHOP").`opHelpURL` - New string member exposed allowing the operator's help page to point to a custom website URL.
  * [DAT Class](../Python/DAT_Class.md "DAT Class") / [Cell Class](../Python/Cell_Class.md "Cell Class") - Added boolean option _`wallTime`_to`.run()` method to specify if the delay options are to be based on elapsed frames or elapsed time.
  * [DAT Class](../Python/DAT_Class.md "DAT Class")`.csv` - Get or set the contents as csv format. Unlike `.text` format, `.csv` supports newlines in cells.
  * [DAT Class](../Python/DAT_Class.md "DAT Class") - Removed `textFormat` member from DAT class and moved to [textDAT Class](../DATs/Text_DAT_Class.md "TextDAT Class") and [scriptDAT Class](../DATs/Script_DAT_Class.md "ScriptDAT Class").
  * [datexecuteDAT Class](../DATs/DAT_Execute_DAT_Class.md "DatexecuteDAT Class").`sizeChanged` - Added to info argument.
  * [datexecuteDAT Class](../DATs/DAT_Execute_DAT_Class.md "DatexecuteDAT Class").`onRow(Col)HeadersChange` - Now provides _prevDAT_.
  * [datexecuteDAT Class](../DATs/DAT_Execute_DAT_Class.md "DatexecuteDAT Class").`onTableChanged(dat, prevDAT, info)` - Now includes DAT in its previous state as well as a description of which rows/columns were removed/added.
  * [datexecuteDAT Class](../DATs/DAT_Execute_DAT_Class.md "DatexecuteDAT Class").`onTableChanged()` info argument now contains:

```
  rowsChanged - a list of row indices with different contents
  rowsAdded   - the list of added *header* indices (in dat)
  rowsRemoved - the list of removed *header* indices (in prevDAT)
  colsChanged - a list of col indices with different contents
  colsAdded   - the list of added *header* indices (in dat)
  colsRemoved - the list of removed *header* indices (in prevDAT)
  cellsChanged - the list of cells that have changed content
  sizeChanged - bool, true if number of rows or columns changed
```

  * [Dependency Class](../Python/Dependency_Class.md "Dependency Class") - Using deepcopy on a `tdu.Dependency()` will now also copy over its `.callbacks` member.
  * [listCOMP Class](../Python/ListCOMP_Class.md "ListCOMP Class") - Rolling outside cells now shows popup help defined in table attribute.
  * [listCOMP Class](../Python/ListCOMP_Class.md "ListCOMP Class") - New members `displayColWidth` and `displayRowHeight` that return the actual row or height of a cell including any resizing.
  * [mediafileinfoDAT Class](../DATs/Media_File_Info_DAT_Class.md "MediafileinfoDAT Class")`.metadata` - Returns a dictionary of the metadata key value entries.
  * [Monitor Class](../Python/Monitor_Class.md "Monitor Class") - Added new `.connectedGPUName` and `.connectedGPUIndex` members.
  * [OP Class](../Python/OP_Class.md "OP Class").`enclosedBy` - List of all [Annotate COMPs](../Glossary/Annotate_COMP.md "Annotate COMP") enclosing this operator.
  * [OP Class](../Python/OP_Class.md "OP Class").`asType(<OP class> class, checkType=False)` - A new wrapper function overridden in TDI type checking. Returns itself.

```
  class - Expected type of this operator.
  checkType - (Optional) If True, raise an exception if this operator is not a member or subtype of class.
```

  * [Page Class](../Python/Page_Class.md "Page Class") / [Cell Class](../Python/Cell_Class.md "Cell Class") - Comparisons to 'None' vs None now work properly.
  * [Par Class](../SOPs/Par_Class.md "Par Class") - Comparisons now use parameter evaluations in all cases. **BACKWARD COMPATIBILITY** par1 == par2 would previously only return true if it were the same parameter object, now it compares their evaluation results.
  * [Par Class](../SOPs/Par_Class.md "Par Class")`.enablePar` - Get or set the single parameter's enable state within the [ParGroup](../Glossary/ParGroup.md "ParGroup"). For the entire ParGroup use ParGroup.enable or Par.enable. Can only be set on [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters").
  * [Par Class](../SOPs/Par_Class.md "Par Class") / [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.readOnly` - This member can now be set per parameter, not just the entire ParGroup as a whole.
    * **BACKWARD COMPATIBILITY** - ParGroup.readOnly now returns a tuple of individual values, not a single bool.
  * [Par Class](../SOPs/Par_Class.md "Par Class")`.isSamePar(x)` / [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.isSameParGroup(x)` - Returns True if argument passed refers to same parameter as object does. For example: `n.par.tx.isSamePar(p)` returns True if `p` is the same parameter as `n.par.tx`. Note this is different from using `==` which compares the parameter's evaluated values.
  * [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.enableExpr` - Now supports lambda format to enable individual parameter enabling within the ParGroup. Example: `n.parGroup.enableExpr = 'lambda x: x==2'`. #only enables third component
  * [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.enable` - This member now returns a tuple of values instead of a single value, as parameters are now individually enable-able.
    * **BACKWARD COMPATIBILITY** - The return type of `ParGroup.enable` is now a tuple, not a single bool.
  * [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.maxSize` - Returns the maximum number of parameter elements for this ParGroup.
  * [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.defaultSize` - Returns default number of parameter elements for this ParGroup.
  * [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.suffixes` - Returns a list of suffixes used to name the parameter elements of this ParGroup.
  * [Par Class](../SOPs/Par_Class.md "Par Class") / [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")`.sequenceBlock` - Returns the [sequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class") the object belongs to, or None.
  * [POP Class](../Python/POP_Class.md "POP Class")`.save()` - Method added for saving POP geometry, similar to SOP.save().
  * [Project Class](../Python/Project_Class.md "Project Class")`.defaultParameterColorSpace` - A new member that can be used to set the color space for newly created nodes.
  * [Timecode Class](../TOPs/Timecode_Class.md "Timecode Class")`.setLength` - Fixed setting by tdu.Timecode so it accounts for potential differences in FPS.
  * [TOP Class](../TOPs/TOP_Class.md "TOP Class")`.pixelFormatName` member added to get the pixel format menuName. For all python handling and parameter interactions this should be used instead of `pixelFormat`.
  * [TOP Class](../TOPs/TOP_Class.md "TOP Class")`.save()` now returns `FileSaveStatus Class[](https://docs.derivative.ca/FileSaveStatus_Class "FileSaveStatus Class")` python object which has methods and members for querying info regarding the save task. In particular, `isCompleted()` returns true if saving finished, useful for asynchronous mode.
  * [Run Class](../Python/Run_Class.md "Run Class") when executed from a DAT, Cell, or td, now remains persistent. Allows you to check the state after its completed.
  * Properly setup context '`me`', when executing a `run()` command. In some cases '`me`' value was set to root instead of the location the `run` command originated from. This could lead to permission errors trying to access neighboring content within a private component for example. **BACKWARD COMPATIBILITY** - '`me`' context no longer wrongly set to root in some cases.
  * [ParCollection Class](../Python/ParCollection_Class.md "ParCollection Class") / [ParGroupCollection Class](../Python/ParGroupCollection_Class.md "ParGroupCollection Class") is now iterable. You can iterate through all the parameters of an operator, a sequence or even a block:

```
   debug(list(n.par))
   debug(list(n.par.S.sequence.blockPars))
   debug(list(n.par.S.sequence[1].par))
   debug(list(n.parGroup))
   debug(list(n.par.S.sequence.blockParGroups))
   debug(list(n.par.S.sequence[1].parGroup))
```

  * [Sequence Class](../Python/Sequence_Class.md "Sequence Class")`.reorderBlocks(index1, index2..)` - Reorder the specified blocks leaving the rest in place.
  * [Sequence Class](../Python/Sequence_Class.md "Sequence Class")`.sortBlocks(key=lambda block: (`block.namePar` or `block[0]).eval()`, baseName=_, reverse=False)_`
    * key - A function that is passed to every block in the sequence to return a sortable value. By default it evaluates the block's main name parameters, if defined, else the first parameter of the block.
    * baseName - If specified, uses the parameter of each block with that baseName as the sort value.
    * reverse - If True, reverses the order of the sort.

```
For Example:
 .sortBlocks(baseName='value', reverse=True)  # sort on reverse *value parameters in the sequence
 .sortBlocks(key=lambda block: block.par.value)  # same as above
 .sortBlocks(key=lambda block: block.par.x + block.par.y)  # sort on combined x+y value of each block
```

  * [Sequence Class](../Python/Sequence_Class.md "Sequence Class")`.blockName` - Gets the basename of the parameter used to name each block. By default this would be 'Blockname'
  * [Sequence Class](../Python/Sequence_Class.md "Sequence Class")`.Sequence[name or index]` - Finds a block by its position or block name as described above.
  * [sequence Class](../Python/Sequence_Class.md "Sequence Class")`.moveBlock(blockFromIndex, blockToIndex, num=1)` - Moves the specified blocks, takes optional keyword '`num`' describing number of blocks to move.
  * [Sequence Class](../Python/Sequence_Class.md "Sequence Class") - moveBlock, insertBlock arguments can be names, integers, or SequenceBlock objects.
  * [sequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class")`.name` - Get the name of a particular block. This is the value of the parameter in the block with basename 'Blockname'. When blocks are added this parameter gets automatically updated with a unique value. This means, in addition to accessing a block by index (example: `n.seq.MySequence[3]`) you can also access it by name (example: `n.seq.MySequence['SectorJ']`).
  * [SequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class")`.namePar` - Returns parameter defining name of block, or None. (As opposed to .name which returns that parameter's value).
  * [SequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class")`.destroy()` replaces [Sequence Class](../Python/Sequence_Class.md "Sequence Class")`.destroyBlock(index)` which is now deprecated.
  * [SequenceCollection Class](../Python/SequenceCollection_Class.md "SequenceCollection Class") - Is now iterable. For example `[s for s in op('geo1').seq]` to iterate through all sequences of a particular OP.
  * [SysInfo Class](../Python/SysInfo_Class.md "SysInfo Class") - Added new members `.GPUName`, `.GPUID`, and `.GPUPlatformID`.
  * [textCOMP Class](../COMPs/Text_COMP_Class.md "TextCOMP Class")`.evalTextSize` now takes optional keywords _wordWrap_ and _pageWidth_ that can override the parameter values during this call.
  * [TOP Class](../TOPs/TOP_Class.md "TOP Class") - Improvements for 3D texture support.
    * Added support for `.numpyArray()` to download 3D textures.
    * `.numpyArray()` now downloads full Cube Maps.
    * `.cudaMemory()` now supports outputting data from 3D/2DArray/Cube textures.
  * [UI Class](../Python/UI_Class.md "UI Class") - New rollover members return the object currently being rolled over. One of: `ui.rolloverPar`, `ui.rolloverParGroup`, `ui.rolloverPage`, `ui.rolloverOp`, `ui.rolloverPanel` in that order.
    * [UI Class](../Python/UI_Class.md "UI Class")`.rolloverPar` / `.rolloverParGroup` - Returns Par/ParGroup currently under the mouse, including parameter labels.
    * [UI Class](../Python/UI_Class.md "UI Class")`.rolloverPage` - Returns the parameter dialog 'page' currently under the mouse, or None.
  * [UI Class](../Python/UI_Class.md "UI Class")`.messageBox()` - No longer is called recursively from [Execute DAT](../DATs/Execute_DAT.md "Execute DAT") Frame Start/End callbacks.
  * Optional keyword argument _alwaysOnTop_ added to several UI elements

```
   OP.openViewer(alwaysOnTop=False)
   OP.openParameters(alwaysOnTop=False)
   UI.openBookmarks(alwaysOnTop=False)
   UI.openTextport(alwaysOnTop=False)
   UI.openWindowPlacement(alwaysOnTop=False)
   UI.openPaletteBrowser(alwaysOnTop=False)
   UI.openMIDIDeviceMapper(alwaysOnTop=False)
   UI.openNewProject(alwaysOnTop=False)
   UI.openKeyManager(alwaysOnTop=False)
   UI.openErrors(alwaysOnTop=False)
   UI.openVersion(alwaysOnTop=False)
   UI.openPreferences(alwaysOnTop=False)
   UI.openBeat(alwaysOnTop=False)
```

  * [WebclientDAT Class](../DATs/Web_Client_DAT_Class.md "WebclientDAT Class").request - Added formParts keyword argument that accepts a list of WebFormPart namedtuples. formParts enables construction of a MIME-formatted request, allowing for multipart and form requests.
  * [TDStoreTools](https://docs.derivative.ca/TDStoreTools "TDStoreTools") - Improved error messaging and behavior of `DependList` and `DependDict`
  * [TDFunctions](https://docs.derivative.ca/TDFunctions "TDFunctions") - Improved error messaging and behavior of `createProperty`. **Backwards Compatibility** - using delattr to delete a property created by `createProperty` will now only set the value to None
  * [TDFunctions](https://docs.derivative.ca/TDFunctions "TDFunctions") - Fixed an issue with `applyParInfo` when source has a bind expression. Added `raiseExceptions` argument to that and `applyParDefaults`.
  * [td Module](https://docs.derivative.ca/Td_Module "Td Module") - Added boolean option _`wallTime`_to`.run()` method to specify if the delay options are to be based on elapsed frames or elapsed time.
  * [Tdu Module](https://docs.derivative.ca/Tdu_Module "Tdu Module").`parSummary(opType)` - Outputs a detailed summary of the built-in parameters.
  * [Tdu Module](https://docs.derivative.ca/Tdu_Module "Tdu Module").`tdu.isPointCloudFile()` - Added to identify if a file is a point cloud file.
  * Fixed hang when executing help() or other python commands that waited on user input to continue.
  * Fixed parent() expressions not updating on renames.
  * Extension changes
    * `onDestroyTD` called instead of __delTD__ when extension destroyed (still backward compatible).
    * `onPostInit` renamed to `onInitTD`
  * **NOTE:** These Python [preferences](https://docs.derivative.ca/Preferences "Preferences") are now off by default.
    * "Add Externally Installed Python Site-Packages to Search Path"
    * "Add Python User Site-Packages to Search Path"
  * [Optimized Python Expressions](https://docs.derivative.ca/Optimized_Python_Expressions "Optimized Python Expressions") - Optimized [Pattern CHOP](../CHOPs/Pattern_CHOP.md "Pattern CHOP")'s `.chanIndex` and `.sampleIndex`.

###  New Palette

  * [Palette:autoMediaPlayer](https://docs.derivative.ca/Palette:autoMediaPlayer "Palette:autoMediaPlayer") - Fix for repeating the last movie and better randomization in selection.
  * [Palette:callbacksHelper](https://docs.derivative.ca/Palette:callbacksHelper "Palette:callbacksHelper") - A new component in the Tools folder, simply drop this into your custom component to easily create a callback system for it.
  * [Palette:cameraViewport](https://docs.derivative.ca/Palette:cameraViewport "Palette:cameraViewport") - Version 1.2.2 - New parameter to externalize the transform into a DAT so it can be immune from cloning.
    * New preset sequences and a button to stop auto rotation.
    * Added 'Go' pulse button to jump to preset position. Removed unneeded reference to numpy.
    * Updated built-in lights and helpers to use POPs.
    * Added instance Id and custom attributes to pick callback.
    * New parameter to add padding around an object when framing.
    * Callback return value can now be used to indicate the event was handled and camera movement should not be initiated.
    * Pivot position is now saved to file. Fixed the 'Pivot Distance' parameter default.
    * Nodes [tagged](../Glossary/Tag.md "Tag") with 'cameraViewportExcludeBounds' are now excluded from bounding box calculations used for framing and homing.
    * New parameters to set the homing bounds manually.
    * Fixed a bug with updating the external camera transform.
    * Fixed Transform DAT being overwritten by storage on load.
  * [Palette:cornerPinPOP](https://docs.derivative.ca/Palette:cornerPinPOP "Palette:cornerPinPOP") - A new component mirroring the functionality of [Palette:cornerPinSOP](https://docs.derivative.ca/Palette:cornerPinSOP "Palette:cornerPinSOP") but using POPs instead.
  * [Palette:cppParsTemplateGen](https://docs.derivative.ca/Palette:cppParsTemplateGen "Palette:cppParsTemplateGen") - v0.1.3 - Fixed parameter variable name formatting when parameter name uses numbers or symbols.
    * v0.1.2 - Fixed namespace issue that was occurring with the latest CPlusPlus Custom OPs API.
  * [Palette:domeViewer](https://docs.derivative.ca/Palette:domeViewer "Palette:domeViewer") - v0.5.0 - Initial release. A new COMP inspired from Fred Tretout's InsideDome. Can be used to previz content for domes as well as easily generate the dome POP to design content with.
  * [Palette:gestureCapture](https://docs.derivative.ca/Palette:gestureCapture "Palette:gestureCapture") - v10.0.0 - Converted to use and output POPs.
  * [Palette:lister](https://docs.derivative.ca/Palette:lister "Palette:lister") - Added drag-to-size column headers.
    * Controlled by Sizeable Cols and Save Col Resizes parameters.
    * colDefine now has a "sizeable" row for every column.
    * Works best with a maximum of 1 stretchy column.
    * Includes a cleanup of the Select/Sort/Filter parameter page.
    * **sizeable** : old listers will require setting the "sizeable" row in the colDefine table for this feature to work.
    * **Column border** : listers using old listerConfig components will not have a border between column headers. This is controlled by the border settings on the _header_ component in listerConfig. Change _Right Border_ to Border A, then set color on _Border A_. Gray 0.4 is the default.
    * colDefine and look OPs now use "topFill" to define how TOPs in cells fill the cell.
    * Fixed an issue where column headers didn't use justify setting provided in the colDefine table.
  * [Palette:logger](https://docs.derivative.ca/Palette:logger "Palette:logger") - v2.6.4 - Major overall.
    * The logger object (self.Logger) is now always initialized. This prevents possible error where logging would fail because the logger was not initialized. This can however cause cases of silent logging, where the messages are added to a queue and not dequeued. See following point.
    * The logger is now initialized with a QueueHandler. The QueueHandler allow for messages to be queued and dequeued overtime. Messages can be queued safely from additional threads, and dequeued on the main TouchDesigner thread. When dequeued, messages are eventually passed to the extra handlers such as the StreamHandler (textport) or FileHandler.
    * A new dictionnary ExtraHandler is holding the handlers managed by the Logger COMP. When any of the managed handlers is updated, a new QueueListener is created to handle the future log messages and changes.
    * New methods to Add or Remove Extra Handlers are exposed. They should be used when a user want to add a custom handler and the log messages should be passed to this handler when dequeued.
    * New defaults and measures to avoid a case where a new Logger COMP reuse a logger instance caused by a perfect name match in the Logger name and hierarchy. This could happen in the past if a Logger was named “ABC” and pointing to a parent “project1”. The resulting logger name would be “project1.ABC” and this match could exist in another component when using multiple loggers. This should be mitigated by new defaults, but this is not entirely avoidable. Try to name your loggers without generic names.
    * Adding support for File rotation settings.
    * Code cleanup, removing unnecessary methods, various fixes.
  * [Palette:operatorPath](https://docs.derivative.ca/Palette:operatorPath "Palette:operatorPath") - 1.4.0 - Added 'Font File' parameter.
  * [Palette:particlesGpu](https://docs.derivative.ca/Palette:particlesGpu "Palette:particlesGpu") - Looping time to avoid bad distribution of hash function upwards of 24 hour runtime.
  * [Palette:pointRender](https://docs.derivative.ca/Palette:pointRender "Palette:pointRender") - v2.0.0 - Updated to POPs workflow.
  * [Palette:popDialog](https://docs.derivative.ca/Palette:popDialog "Palette:popDialog") - Added text entry modes including password, float, and int. Available in parameters or Open command.
  * [Palette:popMenu](https://docs.derivative.ca/Palette:popMenu "Palette:popMenu") 1.3.1 - Submenus will now work when timeline is paused.
  * [Palette:quadReproject](https://docs.derivative.ca/Palette:quadReproject "Palette:quadReproject") - v1.0.0 - Complete rework. Component is now almost exclusively relying on parSequences and expressions.
  * [Palette:searchReplace](https://docs.derivative.ca/Palette:searchReplace "Palette:searchReplace") - Fixed 'whole words' mode for search strings with special characters.
  * [TDAbleton](../Interoperability/TDAbleton.md "TDAbleton") - Version 2.6.3
    * Added separate MPE MIDI devices. The abletonMIDI component now has a default pitchbend channel option.
    * MIDI m4l devices now work with MPE.
    * Better arrangement clip information in abletonTrack Component output CHOP.
    * Added 'Arm for Recording' toggle to abletonTrack
    * Added looping info to clips
    * Fixed lingering errors when using "Update All Components"
    * Fixed long cooks in abletonTrack when a Live set has a long arrangement
    * Fixed demo to use "Auto Filter Legacy"
    * Fixed a single frame error on abletonTrack when going from arrangement clip to none. Increased OSC buffer size and improved log messages.
    * Ableton Component's sendOSC functions no longer work when 'Connect' parameter is off. If you need to override this in script, call sendOSC directly on the TDAbleton master component.
    * Firing an empty clip slot (from abletonClipSlot component) on a record-armed track will start recording a new clip.
  * [Palette:tdPyEnvManager](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager") - Initial release. A component to sideload and manage third-party python and conda environments. Read our [Introduction to the tdPyEnvManager](https://derivative.ca/community-post/introducing-touchdesigner-python-environment-manager-tdpyenvmanager/72024) for details.
  * [Thread Manager](https://docs.derivative.ca/Thread_Manager "Thread Manager") - First public release. A new system component and a set of palette components designed to facilitate Python threading in TouchDesigner. Read our [Introduction to the ThreadManager](https://derivative.ca/community-post/enhancing-your-python-toolbox-touchdesigner%E2%80%99s-thread-manager/72022) for more information.
  * [Palette:threadManagerClient](https://docs.derivative.ca/Palette:threadManagerClient "Palette:threadManagerClient") - A component which works with the Thread Manager COMP, the ThreadManagerClient is designed around it's callback DAT. Users should review the template code and adapt it to their own cases. The customized methods implemented in the ThreadManagerClient Callback are generating a TDTask that gets passed to the Thread Manager TDTask queue. While experienced developers can rely on the Thread Manager directly using `op.TDResources.ThreadManager`, users not familiar with threading should consider using the ThreadManager Client instead.
  * [Palette:treeLister](https://docs.derivative.ca/Palette:treeLister "Palette:treeLister") - Has the new lister topFill and sizable columns features.
  * [Palette:webBrowser](../Interoperability/Palette_webBrowser.md "Palette:webBrowser") - Better support for inputing unicode characters in languages like German and Japanese.
  * [Widgets](../Glossary/Widgets.md "Widgets") - v2.2.6 - New masterRadioMenu widget. Similar the Radio button but is a menu base type and operates with string values. Also includes ability to disable and hide items.
    * v2.2.5 - Button widget now uses Text COMP multiline mode offering better support for button names that require 2 lines.

###  Bug Fixes and Improvements

**SDK Updates**
  * Upgraded to Blackmagic SDK 14.4 - [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design")
  * Upgraded to Deltacast SDK/Driver 6.31.1 - [Deltacast](../Interoperability/Deltacast.md "Deltacast")
  * Upgraded to depthai 2.30.0 - [OAK-D](https://docs.derivative.ca/OAK-D "OAK-D")
  * Upgraded to NDI SDK 6.2.0 - [NDI](../Interoperability/NDI.md "NDI")
  * Upgraded to OpenCV 4.10.0 - [OpenCV](https://docs.derivative.ca/OpenCV "OpenCV")
  * Upgraded to OpenVR 2.5.1. - [OpenVR](../Interoperability/OpenVR.md "OpenVR")
  * Upgraded to Orbbec SDK 1.10.16. This is compatible with Orbbec Femto Mega firmware v1.3.0+. - [Orbbec](../Interoperability/Orbbec.md "Orbbec")
  * Upgraded to RealSense SDK v2.56.5 - [RealSense](../Interoperability/RealSense.md "RealSense")
  * Upgraded to RenderStream 2.0. - [RenderStream](https://docs.derivative.ca/RenderStream "RenderStream")
  * Upgraded to slugLibrary 7.2 - [Text COMP](../COMPs/Text_COMP.md "Text COMP"), [Text TOP](../TOPs/Text_TOP.md "Text TOP"), DAT viewers, etc.
  * Upgraded to Spout SDK 2.007.014 - [Syphon Spout In TOP](../TOPs/Syphon_Spout_In_TOP.md "Syphon Spout In TOP") / [Syphon Spout Out TOP](../TOPs/Syphon_Spout_Out_TOP.md "Syphon Spout Out TOP")
  * Upgraded to ZED SDK 5.0.2. Pascal GPUs are no longer supported with ZED. - [ZED](../Interoperability/ZED.md "ZED")
  * Upgraded to Helios SDK v11.0 with IDN adapter support - [Laser Device CHOP](../CHOPs/Laser_Device_CHOP.md "Laser Device CHOP") - [Helios](https://bitlasers.com/helios-laser-dac/)
  * Upgraded to latest version of Nvidia Maxine SDK. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. This update affects [NVIDIA Background TOP](../TOPs/NVIDIA_Background_TOP.md "NVIDIA Background TOP"), [NVIDIA Denoise TOP](../TOPs/NVIDIA_Denoise_TOP.md "NVIDIA Denoise TOP"), [NVIDIA Upscaler TOP](../TOPs/NVIDIA_Upscaler_TOP.md "NVIDIA Upscaler TOP"), [Body Track CHOP](../Interoperability/Body_Track_CHOP.md "Body Track CHOP"), and [Face Track CHOP](../Interoperability/Face_Track_CHOP.md "Face Track CHOP"). Requires runtime dependencies to be installed manually from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>, see operator help pages for more info.

**COMP Improvements**
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") - Improvements and bug fixes.
    * Improved the performance of TOP outputs.
    * Fixed connected multi-input OPs (eg Merge) losing connections during reload.
    * Fixed options for the 'Asset Paths' parameter functioning the wrong way around.
    * Change to [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") channels so `component_none` is 0 when `component_error` is 1 (eg after a failed load).
    * Fixed 'Ready When' = 'Component Running' mode so the output is updated when in the ready state.
    * Fixed issue which could leave an Engine COMP in an error state after loading a .tox failed.
    * Fixed a potential hang or crash when some errors occurred.
    * Fixed crash which could occur under GPU resource starvation.
  * [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP") - General improvements
    * Fixed [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") not cooking when using an animation, unless 'Children Cook Time' was enabled.
    * Fixed a bug where animation would not play forward when 'Extend Left' was set to "Hold".
    * Normalize bone weights of the imported assets.
  * [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP") - Fixed a crash which could happen when the parent's Geometry COMP was being disabled. Additionally fixed a crash related to the viewer bounding box and instancing.
  * [Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP") - Fixed top and bottom text padding when using a Specification DAT/CHOP. Also added warnings when Specification DAT append mode is used with incompatible features.
  * [Panel COMPs](../Glossary/Panel_Component.md "Panel Component") - Fixed bugs
    * Fixed an issue with the 'Use Vertical' option in 'Fixed Aspect' menu parameter. Also addressed aligning a row of children with simultaneous Fill and Fixed Aspect ratios.
    * Fixed 'Opacity' giving in darker results than expected.
  * [Parameter COMP](../COMPs/Parameter_COMP.md "Parameter COMP") - 'Labels' toggle to turn on/off parameter labels leaving only the active part of the parameter to the right of the label ie. the slider, toggle, button, field, etc.
  * [Text COMP](../COMPs/Text_COMP.md "Text COMP") - Improvements and bug fixes.
    * Improved layout of text when both 'Scale Text to Fit' and 'Word Wrap' are enabled together.
    * Copying text when in 'Select Only' mode no longer includes hidden formatting directives.
    * Fixed cursor movement and selection with formatting directives when using 'Select Only' mode.
    * Fixed a bug that removed leading line breaks in multi-line mode.
    * Fixed a bug selecting strings using python in single line mode.
  * [Window COMP](../Glossary/Window_COMP.md "Window COMP") - Improvements and bug fixes.
    * Added a warning if the specified monitor doesn't exist while the window is opened in perform mode.
    * Fixed issue which could cause the wrong OP to be used in [Perform Mode](../Glossary/Perform_Mode.md "Perform Mode") after using Open as Perform Window from a [Window COMP](../Glossary/Window_COMP.md "Window COMP")'s parameter dialog.
    * On macOS, when a window is sized to exactly fill one or all monitors and has no borders, it will open as a full-screen window, matching behaviour on Windows.
    * Removed notion of 'Stereo' from Window COMP and underlaying classes.

**POP Improvements** For a history of previous POPs development, you can refer to POPs sections in the [Experimental Release Notes](https://docs.derivative.ca/Release_Notes/Experimental "Release Notes/Experimental").

**TOP Improvements**
  * [Blur TOP](../TOPs/Blur_TOP.md "Blur TOP") - Fixed mipmaps not getting re-generated when it cooks. Fixed an issue that broke output when the output resolution was different than the input, this also fixes the Bloom COMP in the palette not working due to that.
  * [Convolve TOP](../TOPs/Convolve_TOP.md "Convolve TOP") - A Coefficients DAT has been docked for ease of use.
  * [Cache TOP](../TOPs/Cache_TOP.md "Cache TOP") - Bug fixes
    * Fixed a case where 'Reset' would create a (0,0,0,1) texture instead of (0,0,0,0).
    * Fixed 'Output Index' not returning correct index if the cache isn't full due to 'Replace Single' being used.
    * Fixed 'Pre-Fill' sometimes filling the wrong resolution.
  * [Chroma Key TOP](../TOPs/Chroma_Key_TOP.md "Chroma Key TOP") - Fixed a hang that can occur with this operator.
  * [Displace TOP](../TOPs/Displace_TOP.md "Displace TOP") - 'Vertical Source' parameter default value changed to Green.
  * [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP") - Fixed an issue where changing the texture dimension of the input didn't trigger the shader to recompile. Also improved errors when array uniforms are incorrectly assigned on the 'Vectors' page.
  * [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") - Bug fixes.
    * Fixed issue that can occur with 2 channel .exr files.
    * Fixed some cases where compressed format .dds files wouldn't be read properly.
  * [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") - Bug fixes.
    * Fixed GPU memory leak when using the Nvidia H.264 and HEVC/H.265 encoders.
    * Header DAT parameter is now disabled for formats that don't support it.
    * Fixed H264/H265 files producing artifacts when seeking.
    * Fixed an issue which prevented some third-party applications from recognizing the alpha channel in exported ProRes 4444.
    * Selecting YUV 4:4:4 (10-Bit) when exporting ProRes 4444 correctly allows the encoder to discard the alpha channel on macOS 13 and above.
  * [NDI In TOP](../TOPs/NDI_In_TOP.md "NDI In TOP") / [NDI Out TOP](../TOPs/NDI_Out_TOP.md "NDI Out TOP") - Upgraded to NDI 6.2.0.
  * [Noise TOP](../TOPs/Noise_TOP.md "Noise TOP") - Fixed this node always using it's input Pixel Format. Also the 'Derivative' parameter was renamed to 'Gradient'.
  * [OP Viewer TOP](../TOPs/OP_Viewer_TOP.md "OP Viewer TOP") - Fixed cook dependency warnings when appending anything to an OP Viewer TOP.
  * [OpenColorIO TOP](../TOPs/OpenColorIO_TOP.md "OpenColorIO TOP") - Fixed crash that occurred when choosing 'Working Color Space' but no Working Color Space was set in the project.
  * [Resolution TOP](../TOPs/Resolution_TOP.md "Resolution TOP") - Don't allow mipmap filtering on the input when 'High Quality Resize' is used.
  * [Script TOP](../TOPs/Script_TOP.md "Script TOP") - `copyNumpyArray` and `cudaCUDAMemory()` now support 3D, 2D Texture Array and Cube Map textures.
  * [Slope TOP](../TOPs/Slope_TOP.md "Slope TOP") - Default for 'Green' parameter changed to 'Vertical Luminance' and default for 'Blue' parameter changed to 'Neutral'.
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Fixed some issues with 8192x4320 resolution capture on [Deltacast](../Interoperability/Deltacast.md "Deltacast") cards. Also fixed an issue where some input formats would not be converted correctly to RGBA.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Bug Fixes
    * Fixed [Deltacast](../Interoperability/Deltacast.md "Deltacast") output not working correctly, including issues with 8K output.
    * Fixed [Deltacast](../Interoperability/Deltacast.md "Deltacast") device output not working correctly.
    * Fixed hang that occurs when turning on 'Sync Group' for [Blackmagic Design](../Interoperability/Blackmagic_Design.md "Blackmagic Design") devices and fixed older Blackmagic devices not working correctly.
  * [Video Stream In TOP](../TOPs/Video_Stream_In_TOP.md "Video Stream In TOP") - Improvements and bug fixes
    * Improved re-buffering behavior and added a new 'Force Re-buffer' pulse parameter to be able to force a re-buffer.
    * Avoid truncating the end of the file when streaming a non-realtime file source (ie. a complete file not a live-stream).
    * Added 'sample_rate' and 'true_length' [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") channels.
    * Fixed a bug that caused extra frame drops in some cases.
  * [Video Stream Out TOP](../TOPs/Video_Stream_Out_TOP.md "Video Stream Out TOP") - Fixed cases where 'Keyframe Interval' and 'B-Frame' parameters were ignored.
  * Added color space information to the TOP viewer's pixel color inspector.

**CHOP Improvements**
  * [CHOP](../Glossary/CHOP.md "CHOP") = Simplified CHOP Viewer 'Scope Tools' to a single string field for scope. Supports [Pattern Matching](../Glossary/Pattern_Matching.md "Pattern Matching").
  * [Audio Device In CHOP](../CHOPs/Audio_Device_In_CHOP.md "Audio Device In CHOP") / [Audio Movie CHOP](../CHOPs/Audio_Movie_CHOP.md "Audio Movie CHOP") / [Audio Stream In CHOP](../CHOPs/Audio_Stream_In_CHOP.md "Audio Stream In CHOP") / [Audio Web Render CHOP](../CHOPs/Audio_Web_Render_CHOP.md "Audio Web Render CHOP") - Default stereo channels are now output when the CHOP is in error state (ie. no device selected, no source found, etc.) to avoid network errors caused by missing channels downstream.
  * [Audio Device In CHOP](../CHOPs/Audio_Device_In_CHOP.md "Audio Device In CHOP") - Reduce pitch-shifts that this node can produce in the audio.
  * [Audio File In CHOP](../CHOPs/Audio_File_In_CHOP.md "Audio File In CHOP") - Fixed playback failing in Sequential mode if left playing for too long.
  * [Audio NDI CHOP](../CHOPs/Audio_NDI_CHOP.md "Audio NDI CHOP") - Fixed this node not getting data if the referenced [NDI In TOP](../TOPs/NDI_In_TOP.md "NDI In TOP") hasn't been used anywhere.
  * [Blob Track CHOP](../CHOPs/Blob_Track_CHOP.md "Blob Track CHOP") - Internal ID counting behavior improved. The final effect is that IDs ramp up in a much more controlled manner.
  * [Copy CHOP](../CHOPs/Copy_CHOP.md "Copy CHOP") - Fixed overcooking and crashing issues when copy/stamping parameters.
  * [CPlusPlus CHOP](../CHOPs/CPlusPlus_CHOP.md "CPlusPlus CHOP") - Fixed the OP_TimeInfo structure not having useful deltaFrames when in non-timeslice mode.
  * [Delay CHOP](../CHOPs/Delay_CHOP.md "Delay CHOP") - Better queueing behavior when frames skipped / max delay setup incorrectly.
  * [Feedback CHOP](../CHOPs/Feedback_CHOP.md "Feedback CHOP") - Reset on startup/initial cook similar to [Feedback TOP](../TOPs/Feedback_TOP.md "Feedback TOP").
  * [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") - Now updates more accurately when monitoring nodes controlled by scripts.
  * [Join CHOP](../CHOPs/Join_CHOP.md "Join CHOP") - Changed behaviour such that the first input to the CHOP doesn't need to be non-empty for the rest of the inputs to be joined.
  * [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP") - While using the CHOP with 'Simplified Output' = Off (ie. using non-simplified output), 1-based Index parameter was fixed for Note type MIDI messages by adding 1 to the index of the note, controller, velocity, aftertouch. This doesn't affect the channel number.**Backward Compatibility** - When loading older files, channel index for Note midi messages may be incremented by one if the 1 Based Index parameter was saved toggled to On in those older files.
  * [Noise CHOP](../CHOPs/Noise_CHOP.md "Noise CHOP") - Reset parameters now affect Random and Brownian ('Num of Integrals' = 0) modes as expected.
  * [Parameter CHOP](../CHOPs/Parameter_CHOP.md "Parameter CHOP") - Bug fixes
    * Fixed 'Rename' parameter menu issue where the menu would display names inconsistent with actual channel names.
    * Fixed 'pageindex' not returning a label nor updating on change.
  * [Timer CHOP](../CHOPs/Timer_CHOP.md "Timer CHOP") - Improvements and bug fixes.
    * New 'Run Values' parameter controls a subtle behavior of what the counters are on the frame when Start is pulsed and the `running` channel goes from 0 to 1. If the menu is set to Zero, the channels `timer_frames`, `timer_samples` and `timer_fraction` will be 0 when Start is pulsed. If set to One, `timer_frames` and `timer_samples` will be at one frame, and `timer_fraction` will also have stepped forward by a frame. These channels are always 0 when you Initialize.
    * Better spacing of Timer CHOP output in first timeslice to work better with non-timesliced OPs (such as the [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP")).
    * Fixed bug where Timer CHOP's python object didn't update after reaching the done state and returning to zero.
    * Fixed bad behavior when spaces were in [Info DAT](../DATs/Info_DAT.md "Info DAT") names.
    * Fixed growing cook delays when external time runs past timer length.
    * 'Defer Par Changes' parameter now defaults to off.
    * Round values to the nearest sample when units are seconds. (Fixes cases of 1 2/3 seconds not being over 100 frames).
    * [Timer CHOP](../CHOPs/Timer_CHOP.md "Timer CHOP") - **BACKWARD COMPATIBILITY** - The first segment was always one sample short, but has now been fixed.
  * [TOP to CHOP](../CHOPs/TOP_to_CHOP.md "TOP to CHOP") - Fixed 'Output as Single Channel Set' not working.
  * [Touch In CHOP](../CHOPs/Touch_In_CHOP.md "Touch In CHOP") / [Touch Out CHOP](../CHOPs/Touch_Out_CHOP.md "Touch Out CHOP") - The Touch In and Touch Out CHOPs work in non-timeslice mode now, sending multisample data.
  * Added menu with toggling behavior to CHOP Viewer scope tools.

**DAT Improvements**
  * [Audio Devices DAT](../DATs/Audio_Devices_DAT.md "Audio Devices DAT") / [Video Devices DAT](../DATs/Video_Devices_DAT.md "Video Devices DAT") - Now refreshes properly with fewer redundant intermediate callbacks.
  * [Execute DAT](../DATs/Execute_DAT.md "Execute DAT") - `onStart` now called after other initializing scripts during load.
  * [Folder DAT](../DATs/Folder_DAT.md "Folder DAT") - Fixed issue which caused files in subdirectories to be missed in some circumstances. Futhermore, when "All Extensions" is off, an empty value in the "Extensions" parameter matches files with no extension now.
  * [Media File Info DAT](../DATs/Media_File_Info_DAT.md "Media File Info DAT") - Added 'Pixel Aspect Ratio' to the list of information displayed and added a 'valid' row added to indicate if the entries in the value columns are valid. Also added python members for 'seconds' row and 'valid' row.
  * [NDI DAT](../DATs/NDI_DAT.md "NDI DAT") - Fixed a crash when used with cloning.
  * [Null DAT](../DATs/Null_DAT.md "Null DAT") - Fixed a bug that could cause text to disappear from read-only text DATs after clicking inside to select text.
  * [OP Find DAT](../DATs/OP_Find_DAT.md "OP Find DAT") - Now supports different aliases for toggle values (dor example: on/1/True off/0/False).
  * [Parameter DAT](../DATs/Parameter_DAT.md "Parameter DAT") - Fixed 'pageindex' not returning a label nor updating on change.
  * [Perform DAT](../DATs/Perform_DAT.md "Perform DAT") - Added 'Clear' parameter that lets you clear the DAT contents.
  * [Video Devices DAT](../DATs/Video_Devices_DAT.md "Video Devices DAT") - Fixed output not working for some drivers.
  * [Web Client DAT](../Interoperability/Web_Client_DAT.md "Web Client DAT") - In the `onResponse` callback, change "set-cookies" in the header to be a list instead of a single value.
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT") - Fixed `onWebSocketClose` callback not triggered on server de-activation or restart and also made a fix to WebSocket closing so that it correctly sends a 'Close Frame' to the client.
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT") - Fixed a hang using 'Restart' pulse with active WebSocket connections. Also fixed onWebSocketClose callback not being triggered in some cases.
  * [WebSocket DAT](../Interoperability/WebSocket_DAT.md "WebSocket DAT") - Fixed a crash when a message is received but there is no 'Callbacks DAT' referenced.
  * Fixed multiple issues with the cursor position in DATs after pressing shift-TAB.

**MAT Improvements**
  * [GLSL MAT](../MATs/GLSL_MAT.md "GLSL MAT") - Improved errors when array uniforms are incorrectly assigned on the 'Vectors' page.

**SOP Improvements**
  * [Alembic SOP](../SOPs/Alembic_SOP.md "Alembic SOP") - Fixed velocity attribute import for point primitives and fixed a crash that could occur dealing with velocities.
  * [Copy SOP](../SOPs/Copy_SOP.md "Copy SOP") / [LSystem SOP](../SOPs/LSystem_SOP.md "LSystem SOP") - Fixed overcooking and crashing issues when copy/stamping parameters.
  * [Skin SOP](../SOPs/Skin_SOP.md "Skin SOP") - Fixed a crash when input is invalid.
  * [Sphere SOP](../SOPs/Sphere_SOP.md "Sphere SOP") - The w texture coordinate is now zero when creating Equirectangular coordinates.
  * [ZED SOP](../SOPs/ZED_SOP.md "ZED SOP") - Added a backwards compatibility warning for ZED on startup for older projects - **BACKWARDS COMPATIBILITY ISSUE** - [ZED SOP](../SOPs/ZED_SOP.md "ZED SOP") - Now needs to point to a [ZED TOP](../TOPs/ZED_TOP.md "ZED TOP") to select it's camera source.

**Other Improvements**
  * [Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") - Bug fixes and improvements
    * New `opHelpURL` string member exposed, allowing the operator help page to point to a custom website
    * Custom Operators now support requesting TOP data on the CPU in different color spaces, when there is a working color space defined.
    * Added query for working color space primaries. `TD::getWorkingColorSpacePrimaries()`.
    * XYZW par type now supported.
    * Fixed issue with Custom Operators loading. POP plugins now are loaded as Custom Operators too.
    * Fixed new crash that will occur if a custom operator is loaded from ProjectDir/Plugins.
  * Script Operators [Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP") / [Script DAT](../DATs/Script_DAT.md "Script DAT") / [Script TOP](../TOPs/Script_TOP.md "Script TOP") / [Script SOP](../SOPs/Script_SOP.md "Script SOP") - New callback `onGetCookLevel` added to manually specify the cook behaviour of the operator.
  * Script Operators - Bug Fixes and improvements
    * Allow setting parameter values in the onSetupParameters() callback.
    * Added query for working color space primaries. `TD::getWorkingColorSpacePrimaries()`.
  * All Out operators now have an optional 'Select' parameter as an alternative to wired input.
  * [GLSL](../Glossary/GLSL.md "GLSL") - `TDCreateRotMatrix()` is now available in all GLSL shaders.
  * New console for Windows and macOS which captures low level messages more reliably, including error messages and output from subprocesses. The [Environment Variable](https://docs.derivative.ca/Variables "Variables") TOUCH_TEXT_CONSOLE no longer needed except to display messages before the TouchDesigner editor launches.
  * Oculus Rift folder and components in the [Palette](../Learn/Palette.md "Palette") renamed to use MetaQuest as base name.
  * Some changes to how .dmp files are created to obtain more information.
  * Horizontal camera tumble direction is now correctly flipped when the camera is upside down. This applies to built-in viewers, tdu.Camera class and the cameraViewport component.
  * Fixed re-opening a minimized parameter dialog, view etc, instead of doing nothing.
  * Fixed bug where Undo shortcuts were blocked when the mouse was over an active DAT, CHOP or TOP.
  * Fixed problem displaying UTF8 characters in the [Textport](../Glossary/Textport.md "Textport") when it is closed.
  * [macOS](https://docs.derivative.ca/MacOS "MacOS") - Stop playback during system sleep.
  * [macOS](https://docs.derivative.ca/MacOS "MacOS") - Folder parameters and ui.chooseFolder() now display a 'New Folder' button in the open dialog.
  * [Timecode](../Interoperability/Timecode.md "Timecode") - On macOS, fixed setting timecode from string when there are leading zeroes (eg. '08:08:08:08').
  * sys.executable now points to the included python executable, not TouchDesigner.
  * Fixed an issue where a python expression error in the 'Clone Master' parameter would prevent saving a component.
  * TouchDesigner and TouchPlayer now always begin with the timeline playing *unless* it is explicitly stopped in a startup script.
  * New Touch Tips added.

###  Operator Snippets

Introducing OP Snippets for POPs and more. There are snippets for almost all POPs and related inter-family operators, along with a bunch of new ones for other parts of TouchDesigner.

Recall there are three way to get to Snippets - right-click on names in the OP Create dialog, right-click -> Operator Snippets on any node, and the top menu bar Help -> Operator Snippets.

###  Backward Compatibility Issues

  * **BACKWARD COMPATIBILITY ISSUE** - [File In CHOP](../CHOPs/File_In_CHOP.md "File In CHOP") - .chan files now preserve channel names instead of always defaulting to chan1, chan2, chan3, ...
  * **BACKWARD COMPATIBILITY ISSUE** - [Timer CHOP](../CHOPs/Timer_CHOP.md "Timer CHOP") - The first segment was always one sample short, this has now been fixed.
  * **BACKWARD COMPATIBILITY ISSUE** - [ZED CHOP](../CHOPs/ZED_CHOP.md "ZED CHOP") - Now needs to point to a [ZED TOP](../TOPs/ZED_TOP.md "ZED TOP") to select it's camera source.
  * **BACKWARD COMPATIBILITY ISSUE** - [ZED SOP](../SOPs/ZED_SOP.md "ZED SOP") - Now needs to point to a [ZED TOP](../TOPs/ZED_TOP.md "ZED TOP") to select it's camera source.
  * **BACKWARD COMPATIBILITY ISSUE** - [ZED](../Interoperability/ZED.md "ZED") - Upgraded to ZED SDK 5.0.1, this update means Pascal GPUs are no longer supported with ZED.
  * **BACKWARD COMPATIBILITY ISSUE** - [Par Class](../SOPs/Par_Class.md "Par Class") - Comparisons now use parameter evaluations in all cases. par1 == par2 would previously only return true if it were the same parameter object, now it compares their evaluation results.
  * **BACKWARD COMPATIBILITY ISSUE** - [ParGroup](../Glossary/ParGroup.md "ParGroup")`.enable` and `.readOnly` members now returns a tuple of values instead of a single bool value, as Par's are now individually enable-able.
  * **BACKWARD COMPATIBILITY ISSUE** - [Par Class](../SOPs/Par_Class.md "Par Class") / [ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class") - `.readOnly` can now be set per Par, not just the entire ParGroup as a whole.
  * **BACKWARD COMPATIBILITY ISSUE** - 'me' context no longer wrongly set to root in some cases. When executing a run() command, in some cases 'me' value was set to root instead of the location the run command originated from. This could lead to permission errors trying to access neighbouring content within a private component for example.
  * **BACKWARD COMPATIBILITY WARNING** - [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") / [DMX Map DAT](https://docs.derivative.ca/DMX_Map_DAT "DMX Map DAT") - Changed channel values to go from range 1-512 rather than 0-511 to match the DMX512 addressing standard.
  * **BACKWARD COMPATIBILITY WARNING** - [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP") - While using the CHOP with 'Simplified Output' = Off (ie. using non-simplified output, 1-based Index parameter was fixed for Note type midi messages by adding 1 to the index of the note, controller, velocity, aftertouch. This doesn't affect the channel number. When loading older files, channel index for Note midi messages may be incremented by one if the 1 Based Index parameter was saved toggled to On in those older files.
  * **BACKWARD COMPATIBILITY WARNING** - [DMX Fixture POP](../POPs/DMX_Fixture_POP.md "DMX Fixture POP") - DMX Channel Names _must not include spaces_ now.
  * **BACKWARD COMPATIBILITY WARNING** - [POP](../POPs/POP.md "POP") - A number of POP parameters were renamed and extended in size. This may affect loaded values or expressions in previous toe or tox files.
For example some Random POP parameters (Amplitude, A, B, etc) were extended to have per-axis parameters (controlled by the size parameter), similar to the Noise POP. This required updating the RoyTimWorkshop file in the Examples folder. Please redownload the examples or be aware of these changes.
  * **BACKWARD COMPATIBILITY WARNING** - [TDFunctions](https://docs.derivative.ca/TDFunctions "TDFunctions") - Improved error messaging and behavior of `createProperty`. However, using delattr to delete a property created by `createProperty` will now only set the value to None.
  * **BACKWARD COMPATIBILITY WARNING** - `ui.rolloverPanel` now reverts back to None when no panel is currently being rolled over. Previously it would remain pointing to the last panel.
  * **BACKWARD COMPATIBILITY WARNING** - [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Using 'Sync Outputs' feature requires a Pro license.
  * **BACKWARD COMPATIBILITY WARNING** - [Ouster TOP](../TOPs/Ouster_TOP.md "Ouster TOP") - Updated node operates differently than previous versions and may require settings adjustments. Some features like image layout are no longer supported.

##  Experimental Builds 2025.30000 - Oct 08, 2025

For experimental release notes in this branch refer to [Experimental Release Notes](https://docs.derivative.ca/Release_Notes/Experimental "Release Notes/Experimental")

##  Official Builds 2023.10000 and earlier - Sep 22, 2025

For earlier Official Build release notes refer to [Official 2023.10000 Release Notes](https://docs.derivative.ca/Release_Notes/2023.10000 "Release Notes/2023.10000")

A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode"), or (2) a user-created [Panel](../Glossary/Panel.md "Panel") inside a [Window Component](../Glossary/Window_COMP.md "Window COMP"). The user-created windows can span [Multiple Monitors](../Glossary/Multiple_Monitors.md "Multiple Monitors") borderless, or be floating windows with borders, or popups.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

The Backdrop is the grid of node viewers that are visible behind the [Network](../Glossary/Network.md "Network"), set by turning on [Display Flags](../Glossary/Display_Flag.md "Display Flag") and the network RMB -> Display... Backdrop OPs.

MATs or Materials are an [Operator Family](../Glossary/Operator_Family.md "Operator Family") that applies a [Shader](../Glossary/Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

POPs (Point Operators) is a new [Operator Family](../Glossary/Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](../Glossary/Script.md "Script") or [GLSL](../Glossary/GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](../Glossary/Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

[OP Snippets](../Learn/OP_Snippets.md "OP Snippets") is a set of 700+ live examples of TouchDesigner operators. You can access snippets via the Help menu, or by right-clicking on network operators, or r-clicking on OP Create dialog items.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

The 3D data held in POPs and passed for rendering by the [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP").

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.

The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](../Glossary/Text_DAT.md "Text DAT") and referenced by a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

A surface type in [POPs](../POPs/POP.md "POP") and [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](../Glossary/Point.md "Point") and Primitives are part of the [Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

Each POP and SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](../Glossary/Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

A primitive in POPs that has 1 or more connected points.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

POP Topology is the relationship between geometric entities making up POPs, and refers to the POP's [Primitives](../Glossary/Primitive.md "Primitive"), the [Vertx / Vertices](../Glossary/Vertex.md "Vertex") of each Primitive, and the [Points](../Glossary/Point.md "Point") list that the Vertices refer to.

The width and height of an image in pixels. Most TOPs, like the [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") can set the image resolution. See [Aspect Ratio](../Glossary/TOP_Generator_Common_Page.md "TOP Generator Common Page") for the width/height ratio of an image, taking into account non-square pixels.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

To re-compute the output data of the [Operators](Operator.md "Operator"). An operator cooks when (1) its inputs change, (2) its [Parameters](../Glossary/Parameter.md "Parameter") change, (3) when the timeline moves forward in some cases, or (4) [Scripting](../Glossary/Script.md "Script") commands are run on the node. When the operator is a [Panel Component](../Glossary/Panel_Component.md "Panel Component"), it also cooks when a user interacts with it. When an operator cooks, it usually causes operators connected to its output to re-cook. When TouchDesigner draws the screen, it re-cooks all the [Dependencies](../Glossary/Dependency.md "Dependency") - the necessary operators in all [Networks](../Glossary/Network.md "Network"), contributing to a frame's total "cook time".

The term "Frame" is a measurement of time used (1) in the [Timeline](../Glossary/Timeline.md "Timeline"), (2) as a time-unit in CHOPs, and (3) as a time unit in movie files that are read into [TOPs](../TOPs/TOP.md "TOP") and written out from TOPs. The [Frame Rate](../Glossary/Frame_Rate.md "Frame Rate") is the frames per second (FPS).

Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off or the root timeline is paused.

shared points, normals on shared points, unique points, recalculate.

A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

Any floating window that is not a [Pane](../Glossary/Pane.md "Pane") or [Viewer](../Glossary/Viewer.md "Viewer").

A [CHOP](../Glossary/CHOP.md "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](../Glossary/Sample.md "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](../Glossary/Export.md "Export") to [Parameters](../Glossary/Parameter.md "Parameter").

An operator whose Bypass flag is set does nothing: All data going into its first input appears at its output unaffected.

The [Frames](../Glossary/Frame.md "Frame")-per-Second that TouchDesigner's [Timeline](../Glossary/Timeline.md "Timeline") runs at. Set with `project.cookRate`.

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](../Glossary/Network_Path.md "Network Path"), which determine the output of the operator.

samples-per-second of a [CHOP](../Glossary/CHOP.md "CHOP"). Each CHOP in your network has a sample rate. In contrast, the overall timeline has a [Frame Rate](../Glossary/Frame_Rate.md "Frame Rate"), which is the number of frames to [cook](../Glossary/Cook.md "Cook") and display per second, generally your monitor display frequency, default 60.

A Time Slice is the time from the last cook frame to the current cook frame. In CHOPs it is the set of short channels that contain the CHOP channels' samples between the last and the current cook frame.

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

POPs (Point Operators) is a new [Operator Family](../Glossary/Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](../Glossary/CHOP_Viewer.md "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](../Glossary/Parameter.md "Parameter").

A [Link](../Glossary/Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](../Glossary/Operator_Family.md "Operator Family").

The grey dashed lines between nodes is a Reference (or [Link](../Glossary/Link.md "Link")). A Reference is (1) a [Parameter Reference](../Glossary/Parameter_Reference.md "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](../Glossary/Export.md "Export"), node [Paths](../Glossary/Network_Path.md "Network Path") in parameters, and [expressions](../Glossary/Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](../Glossary/Wire.md "Wire") that connects nodes in the same [Operator Family](../Glossary/Operator_Family.md "Operator Family").

2D texture array or 3D gridof pixels.

Matching names using wildcard characters and bracketing. Useful in "[Select](../Glossary/Select_CHOP.md "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

TouchDesigner Component file, the file type used to save a [Component](../Glossary/Component.md "Component") of your TouchDesigner project.

The sub-[Family](../Glossary/Operator_Family.md "Operator Family") of [Component](../Glossary/Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](../Glossary/Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP") and [Light COMP](../Glossary/Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

Hierarchy relates components with other components. There are two groups of Hierarchy in TouchDesigner. 3D Object Components, and 2D Panel Components. Hierarchies let one component to be positioned relative to another. Each group can be connected via lines between the bottoms/tops of nodes in a network, or by placing one component inside the other.

applies to python objects, parameters, nodes.

is the [Procedural](../Glossary/Procedural.md "Procedural") mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](../Glossary/Cook.md "Cook").

A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](../Glossary/Root.md "Root"). This path is displayed at the top of every [Pane](../Glossary/Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](../Glossary/Folder.md "Folder").

Some operators have a DAT [docked](../Glossary/Docking.md "Docking") to them that contains some python functions. These functions, called "callbacks", get called when something in the operator changes.

In the [Animation component](../Glossary/Animation_COMP.md "Animation COMP") each keyframe specifies a channel's value at a specific time (or frame). A keyframe holds a value, slopes and accelerations, and an interpolation type. A channel's keyframes are used to interpolate and determine the values of all the samples of the channel.

Any component can be extended with its own Python classes which contain python functions and data.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](Python.md "Python") and the original [Tscript](../Glossary/Tscript.md "Tscript"). Scripts and single-line commands can also be run in the [Textport](../Glossary/Textport.md "Textport").

A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](../Glossary/Network_Path.md "Network Path").

Cloning makes multiple components match the contents of a master component. A [Component](../Glossary/Component.md "Component") whose Clone parameter is set will be forced to contain the same nodes, wiring and parameters as its master component. Cloning does not create new components as does the [Replicator COMP](../Glossary/Replicator_COMP.md "Replicator COMP").
