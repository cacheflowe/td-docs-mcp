---
url: https://docs.derivative.ca/Alembic_In_POP
category: POPs
title: Alembic_In_POP
---

# Alembic In POP
## Summary

The Alembic In POP loads and plays back [Alembic](http://www.alembic.io/) file geometry sequences.
The supported Alembic primitives are polymesh, curves, and points for geometry. As well, Alembic transformations are supported.
Polymesh primitives are imported as triangles or quads for faces of 3 or 4 vertices respectively, and as a close lined strip for faces with greater than 4 vertices.
For Alembic files that contain animation, use the Time parameter and pay attention to the Unit menu to control it in frames, seconds, or whatever you like.
An Alembic archive may contain one or more object paths for one or multiple geometries. It is possible to view these objects all at once or select them separately using the 'Object Path' parameter menu. If separate selected objects contain duplicate attributes (ie. sharing a name) but associated with a different attribute class (eg. vertex vs. point), then the duplicate attribute will be converted to a vertex attribute.
Each object in an Alembic file schema may possess standard or custom attributes. The standard attributes are normal (`N`), velocity (`V`), and texture coordinates (`Tex`). Multiple custom attributes may live in an Alembic schema with more flexible names and types. Most Alembic attributes are supported but not all convert one-to-one into a POP format:
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
[alembicPOP_Class](https://docs.derivative.ca/AlembicPOP_Class "AlembicPOP Class")

## Parameters - Alembic Page
- Alembic File `file` - The file path to the Alembic file.
- Object Path `objectpath` - ⊞ - Specify which geometry object to be loaded. Each geometry object can represent a hierarchies of multiple geometries. It is also possible to choose the "All Objects" (ie. "*") option from the list of available objects. This option is selected by default.
  * * `*` -
  * /box_object1/color1 `/box_object1/color1` -

- Transform `xform` - ⊞ - Select which transform is applied if the transform data is available from the input Alembic file.
  * None `none` - No transformation is applied to the geometry(s), they reside at the origin.
  * Static Local Transformation `staticlocalxform` - Applies the static local transformation for the selected geometry objects from the Object Path.
  * Static World Transformation `staticworldxform` - Applies the static world transformation of the selected geometry objects from the Object Path up to their parents transformation.
  * Dynamic Transformation `dynamicxform` - In the case that the Alembic file includes dynamic or animated geometries the transformation is applied to the selected geometries. This option performs both local and world transformation (if available) for the given geometry.

- Time `time` - ⊞ - Specify which part of the Alembic samples sequence is loaded. The time unit menu converts the current time units to the selected unit. The available options are Frames, Seconds, Indices, and Fraction.
  * Time `time` - Specify which part of the Alembic samples sequence is loaded.
  * Time Unit `timeunit` - The time unit menu converts the current time units to the selected unit. The available options are Frames, Seconds, Indices, and Fraction.

- FPS `fps` - Specify the rate used for sample calculation for reading from the Alembic file.
- Interpolation `interp` - ⊞ - Interpolate between the samples/keyframes in the Alembic file. This parameter only works if the selected geometries are defined as dynamic and the transformation information are available from the input Alembic file.
  * None `none` - No interpolation is performed between each samples.
  * Linear Interpolation `interp` - Smooth interpolation between each two samples is calculated.

- Unload `loadfile` - Toggling the unload to "on" will unload the file and close it. By setting it to "off", the file will be loaded again. When the file is unloaded it can be overwritten by other applications or deleted.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Alembic In POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
