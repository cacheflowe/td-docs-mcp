---
url: https://docs.derivative.ca/CPlusPlus_SOP
category: SOPs
title: CPlusPlus_SOP
---

# CPlusPlus SOP
## Summary

The CPlusPlus SOP allows you to make custom SOP operators by writing your own plugin using C++.
See [Write a CPlusPlus Plugin](https://docs.derivative.ca/Write_a_CPlusPlus_Plugin "Write a CPlusPlus Plugin") and the other articles in the [C++ category](https://docs.derivative.ca/Category:C%2B%2B "Category:C++") for more detailed information on how to make .dll for use with this SOP.
The C++ code can be written for GPU or CPU loading. The ease of developing C++ code for either of these two options are fairly similar. Nevertheless, by setting the “`directToGPU`” flag within the C++ code, only one of these modes is recognized as a valid mode. Different classes are dedicated for each of these two modes, so bear in mind that setting the “`directToGPU`” flag to “`true`” or “`false`” requires different classes and functions to be called within either of `execute()` or `executeVBO()`.
In CPU mode, the geometry data can be added one at a time or all at once. As well, in CPU mode the CPlusPlus SOP can use wired SOP inputs and SOP to DAT, SOP to CHOP, or SOP output OPs as well. Additionally DAT, CHOP, and TOP 'non-wired' input operators can be used as custom parameters. In this case, the custom parameters must be first handled in the C++ code to be able to accept any input from the other operators.
The GPU direct mode is similar to CPU mode, but it cannot use any output SOPs downstream or be accessed by SOP to DAT or SOP to CHOP operators. In GPU direct mode the data is added to the VBO buffers immediately which improves the performance through faster updating, however the size of the vertices and face array indices must be known prior to filling the buffers.
Example for CPlusPlus SOP as a Visual Studio project in Windows are available in `C:/Program Files/Derivative/TouchDesigner/Samples/CPlusPlus/SimpleShapesSOP` or your custom TouchDesigner installation folder. (NOTE: On macOS it is here: `TouchDesigner.app/Contents/Resources/tfs/Samples/CPlusPlus/SimpleShapesSOP`)
**Custom Parameters** - Custom Parameters can be automatically created by the C++ SOP `.dll`. This custom parameter page can be removed, edited, or appended to from within the `setupParameters()` function in SimpleShapes.cpp. The defined custom parameters can be enabled or disabled depending on whether they are valid for a specific task or not.
**Geometry Data** - Geometry within the C++ SOP code can be defined by any algorithm or even imported from external files. The possible geometries are triangular meshes and particle systems. Note that if your original geometry has polygons with more than 3 vertices, they must be converted to triangles with known and valid vertex indices, before being added to the list of triangles.
The geometry data for exporting to TouchDesigner can have point, normal, and texture coordinates, RGBA colors, triangle information in case of meshes and/or particle systems, as well as custom attributes with an arbitrary name, float or integer type, and up to 4 components (ie. Cd0, Cd1, Cd2, Cd3).
[cplusplusSOP_Class](https://docs.derivative.ca/CplusplusSOP_Class "CplusplusSOP Class")

## Parameters - Load Page
- Plugin Path `plugin` - The path to the plugin you want to load.
- Re-Init Class `reinit` - When this parameter is On, it will delete the instance of the class created by the plugin, and create a new one.
- Re-Init Class `reinitpulse` - Instantly reinitialize the class.
- Unload Plugin `unloadplugin` - When this parameter goes above 1, it will delete the instance of the class created by the plugin and unload the plugin. If multiple SOPs have loaded the same plugin they will all need to unload it to release the file.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the CPlusPlus SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
