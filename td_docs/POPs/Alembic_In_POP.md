---
url: https://docs.derivative.ca/Alembic_In_POP
category: POPs
title: Alembic_In_POP
---

# Alembic In POP

## Summary

The Alembic In POP loads and plays back [Alembic](http://www.alembic.io/) file geometry and multi-frame sequences.

The supported Alembic primitives are polymesh, curves, and points for geometry. As well, Alembic transformations are supported.

Polymesh primitives are imported as triangles or quads for faces of 3 or 4 vertices respectively, and as a closed line strip for faces with greater than 4 vertices.

For Alembic files that contain animation, use the controls on the Play page. Press Start to run and loop it. Press Cue and then scrub the Cue Time parameter to scrub the full range of the animation. With Cue off, you can adjust Speed and pause with Play. Alternately set Play Mode to Specify Index and change the Index parameter to control the current animation position expressed as fraction, seconds, frame or index (the frame number internal to the `.abc` file).

An Alembic archive may contain one or more object paths for one or multiple geometries. It is possible to view these objects all at once or select them separately using the 'Object Path' parameter menu. If separate selected objects contain duplicate attributes (ie. sharing a name) but associated with a different attribute class (eg. vertex vs. point), then the duplicate attribute will be converted to a vertex attribute.

Each object in an Alembic file schema may possess standard or custom attributes. The standard attributes are normal (`N`), velocity (`V`), and texture coordinates (`Tex`). Multiple custom attributes may live in an Alembic schema with more flexible names and types.

Caveat - Most Alembic attributes are supported but not all convert one-to-one into a POP format:
  * 16-bit int attributes (eg. Int16, V2s, P3s, etc.) are converted to 32-bit int.
  * 64-bit attributes (eg. Uint64, Int64, V2d, etc.) are converted to double, which is the only 64-bit attribute that POPs currently support.
  * Attributes with > 4 components (eg. Box3f, M33f, M44f etc.) are packed as an array of vec4's. If there is an array of these attributes then they will be packed together back-to-back. Eg. M44f has 16 components and will be imported as float4[4], and M44f[2] will be imported as float4[8] with M44f[0] first followed by M44f[1].

List of **unsupported** attributes:
  * String/WString
  * 8-bit and 16-bit float color
  * Bool
  * UChar/Char

The conversion between the Alembic geometries scopes to the TouchDesigner attributes types are shown in the table below:
---
**Alembic Scope** |  **TouchDesigner Attribute**
Varying, Vertex |  Point
Facevarying |  Vertex
Uniform, Constant |  Primitive
See also [Alembic](../Interoperability/Alembic.md "Alembic"), [Alembic Out POP](https://docs.derivative.ca/Alembic_Out_POP "Alembic Out POP"), [File In POP](File_In_POP.md "File In POP"), [File Out POP](File_Out_POP.md "File Out POP")

[alembicPOP_Class](AlembicPOP_Class.md "AlembicPOP Class")

## Parameters - Alembic Page
- Alembic File `file` - The file path to the Alembic file.
- Object Path `objectpath` - ⊞ - Specify which geometry object to be loaded. Each geometry object can represent a hierarchies of multiple geometries. It is also possible to choose the "All Objects" (ie. "*") option from the list of available objects. This option is selected by default.
  * * `*` -
  * /box_object1/color1 `/box_object1/color1` -
- Load Type `loadtype` - ⊞ - Select whether to load the file on this frame or next. Loading next frame will significantly reduce overall cook time.
  * Immediate (Slow) `immediate` - Loads the Alembic file on this frame, meaning the current cook will bear the brunt of the entire file load/read/write.
  * Next Frame (Fast) `nextframe` - Begins the Alembic file load on this frame asynchronously, finishing and synchronizing the file load on the next cook. This will vastly reduce the overall cook time, as the Alembic load can be done asynchronously between the two cooks.
- Transform `xform` - ⊞ - Select which transform is applied if the transform data is available from the input Alembic file.
  * None `none` - No transformation is applied to the geometry(s), they reside at the origin.
  * Static Local Transformation `staticlocalxform` - Applies the static local transformation for the selected geometry objects from the Object Path.
  * Static World Transformation `staticworldxform` - Applies the static world transformation of the selected geometry objects from the Object Path up to their parents transformation.
  * Dynamic Transformation `dynamicxform` - In the case that the Alembic file includes dynamic or animated geometries the transformation is applied to the selected geometries. This option performs both local and world transformation (if available) for the given geometry.
- Interpolation `interp` - ⊞ - Interpolate between the samples/keyframes in the Alembic file. This parameter only works if the selected geometries are defined as dynamic and the transformation information are available from the input Alembic file.
  * None `none` - No interpolation is performed between each samples.
  * Linear Interpolation `interp` - Smooth interpolation between each two samples is calculated.
- Unload `loadfile` - Toggling the unload to "on" will unload the file and close it. By setting it to "off", the file will be loaded again. When the file is unloaded it can be overwritten by other applications or deleted.

## Parameters - Play Page
- Shift Animation Start `shiftanimationstart` - A toggle to specify whether to shift the animation to the start of animation indicated in the importing file.
- Sample Rate Mode `sampleratemode` - ⊞ - Sets the sample rate source.
  * File FPS `filefps` -
  * Custom `custom` -
- Sample Rate `samplerate` - Sets the custom sample rate.
- Play Mode `playmode` - ⊞ - Pause or play the geometry animation.
  * Locked to Timeline `lockedtotimeline` -
  * Specify Index `specifyindex` -
  * Sequential `sequential` -
- Initialize `initialize` - Resets the animation to its initial state.
- Start `start` - Start playback of animation sequence.
- Cue `cue` - ⊞ - A toggle to jump to Cue Point when it is set to ON and it stays at that position. Only available when Play Mode is Sequential.
  * Cue `cue` -
  * Cue Pulse `cuepulse` - Triggers animation jump to the Cue Point
- Cue Point `cuepoint` - ⊞ - Set any index in the animation as a point to jump to.
  * Cue Point `cuepoint` -
  * Cue Point Unit `cuepointunit` - Specifies a unit type for Cue Point
- Play `play` - Enable playback.
- Index `index` - ⊞ - This parameter explicitly sets the animation position when Play Mode is set to Specify Index. The units’ menu on the right lets you specify the index in the following units: Index, Frames, Seconds, and Fraction (percentage).
  * Index `index` -
  * Index Unit `indexunit` - Specifies a unit type for Index. Changing this will convert the previous unit to the selected unit.
- Speed `speed` - Playback speed.
- Trim `trim` - Enable the Trim Start and Trim End parameters.
- Trim Start `tstart` - ⊞ - The time to consider the starting time of 0.
  * Trim Start `tstart` -
  * Trim Start Unit `tstartunit` - Sets the trim time unit.
- Trim End `tend` - ⊞ - TTGrime the end of the animation.
  * Trim End `tend` -
  * Trim End Unit `tendunit` - Sets the trim time unit.
- Extend Left `textendleft` - ⊞ - Determines how the parent COMP handles animation positions that lie before the Trim Start position.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -
- Extend Right `textendright` - ⊞ - Determines how the parent COMP handles animation positions that lie after the Trim End position.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels

Extra Information for the Alembic In POP can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

###

## Common POP Info Channels

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
