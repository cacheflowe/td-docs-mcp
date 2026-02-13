---
url: https://docs.derivative.ca/Alembic_SOP
category: SOPs
title: Alembic_SOP
---

# Alembic SOP
## Summary

The Alembic SOP loads and plays back [Alembic](http://www.alembic.io/) file geometry sequences.
The supported Alembic primitives are polymesh, curves, and points for geometry. As well, Alembic transformations are supported.
For Alembic files that contain animation, use the Time parameter and pay attention to the Unit menu to control it in frames, seconds, or whatever you like.
An Alembic archive may contain one or more object paths for one or multiple geometries. It is possible to view these objects all at once or select them separately using the 'Object Path' parameter menu.
Each object in an Alembic file schema may possess standard or custom attributes. The standard attributes are normal (`N`), velocity (`V`), and texture coordinates (`UV`). Multiple custom attributes may live in an Alembic schema with more flexible names and types. The custom attribute types can be any of the following:
  * float arrays
  * integer arrays
  * 2d or 3d vectors of floats
  * matrix with 16 float elements

The conversion between the Alembic geometries scopes to the TouchDesigner attributes types are shown in the table below:
---
**Alembic Scope** |  **TouchDesigner Attribute**
Varying, Vertex |  Point
Facevarying |  Vertex
Uniform, Constant |  Primitive
The Alembic SOP lets you load geometry to either the CPU or the GPU. While using the GPU is much faster, it has some limitations:
  * In GPU direct mode you can not connect additional SOPs downstream.
  * In GPU direct mode, when there are multiple objects with different sets of attributes, a default value is used for the missing attributes of each objects. For example, if one geometry has normal data and another one doesn’t, the x, y, and z elements of normal vector for the geometry with the missing normal attribute will be set to 0, 0, 1 respectively.

[alembicSOP_Class](https://docs.derivative.ca/AlembicSOP_Class "AlembicSOP Class")

## Parameters - Page
- Alembic File `file` - The file path to the Alembic file.
- Object Path `objectpath` - Specify which geometry object to be loaded. Each geometry object can represent a hierarchies of multiple geometries. It is also possible to choose the "All Objects" option from the list of available objects. This option is selected by default.
- Time `time` - Specify which part of the Alembic samples sequence is loaded. The time unit menu converts the current time units to the selected unit. The available options are Frames, Seconds, and Fraction.
- Time Unit `timeunit` -
- Transform `xform` - ⊞ - Select which transform is applied if the transform data is available from the input Alembic file.
  * None `none` - No transformation is applied to the geometry(s), they reside at the origin.
  * Static Local Transformation `transform` - Applies the static local transformation for the selected geometry objects from the Object Path.
  * Static World Transformation `transform` - Applies the static world transformation of the selected geometry objects from the Object Path up to their parents transformation.
  * Dynamic Transformation `transform` - In the case that the Alembic file includes dynamic or animated geometries the transformation is applied to the selected geometries. This option performs both local and world transformation (if available) for the given geometry.

- Interpolation `interp` - ⊞ - Interpolate between the samples/keyframes in the Alembic file. This parameter only works if the selected geometries are defined as dynamic and the transformation information are available from the input Alembic file.
  * None `none` - No interpolation is performed between each samples.
  * Smooth Interpolation `interpT` - Smooth interpolation between each two samples is calculated.

- Straight to GPU `straightgpu` - Load the geometry directly to the GPU. This options is much faster than the default loading to CPU, however you can not use the geometry output to other SOPs or access the geometry data in the [SOP to CHOP](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP") or [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"). It is recommended that the Alembic file have the normals and UVs baked into the file since you can not add them via SOPs in TouchDesigner.
- Compute Normal `compnml` - Creates normals for the input geometry.
- Unload `loadfile` - Toggling the unload to "on" will unload the file and close it. By setting it to "off", the file will be loaded again. When the file is unloaded it can be overwritten by other applications or deleted.

## Info CHOP Channels
Extra Information for the Alembic SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Alembic SOP Info Channels
  * start_time -

  * end_time -

###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
