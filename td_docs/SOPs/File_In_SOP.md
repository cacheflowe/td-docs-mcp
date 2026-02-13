---
url: https://docs.derivative.ca/File_In_SOP
category: SOPs
title: File_In_SOP
---

# File In SOP
## Summary

The File In SOP allows you to read a geometry file that may have been previously created in the Model Editor, output geometry from a SOP, or generated from other software such as [Houdini](http://www.sidefx.com). The geometry file can be read in from disk or from the web. Use http:// when specifying a URL.
[fileinSOP_Class](https://docs.derivative.ca/FileinSOP_Class "FileinSOP Class")

## Parameters - Page
- Geometry File `file` - Contains the full pathname of the geometry file to be read in.
Some of the geometry formats that can be read:
  * TouchDesigner : .tog
  * Houdini : .classic, .bhclassic
  * Common : .obj

- Flip Primitive Faces `flipfacing` - Flips the primitive faces of the geometry.
- Compute Normals if None Exist `normals` - Creates normals if the geometry does not have them.
- Refresh `refresh` - Reload the file when this parameter is set to On.
- Refresh Pulse `refreshpulse` - Instantly reload the file from disk.

## Info CHOP Channels
Extra Information for the File In SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
