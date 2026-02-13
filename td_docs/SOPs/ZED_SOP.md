---
url: https://docs.derivative.ca/ZED_SOP
category: SOPs
title: ZED_SOP
---

# ZED SOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The ZED SOP uses the ZED to scan and create geometry by moving it around the room or an object of interest. To know what ZED SDK we are using, refer to the [ZED](https://docs.derivative.ca/ZED "ZED") article.
See [ZED TOP](https://docs.derivative.ca/ZED_TOP "ZED TOP"), [ZED CHOP](https://docs.derivative.ca/ZED_CHOP "ZED CHOP"), [ZED POP](https://docs.derivative.ca/ZED_POP "ZED POP") and [ZED](https://docs.derivative.ca/ZED "ZED").
[zedSOP_Class](https://docs.derivative.ca/ZedSOP_Class "ZedSOP Class")

## Parameters - Page
- ZED TOP `zedtop` - The name of the primary [ZED TOP](https://docs.derivative.ca/ZED_TOP "ZED TOP") that is configuring the camera. The primary TOP controls which camera the SOP receives data from.
- Sample `sample` - While enabled the ZED camera samples points in space. Once disabled it will generate the surface from the points, as well as any normal or texture attributes.
- Reset `reset` - Clears the extracted geometry and resets spatial mapping.
- Reset Pulse `resetpulse` - Triggers the Reset immediately on button release (button-up). This can be accessed in python using the pulse() method.
- Preview `preview` - ⊞ - Select level of detail of the preview when camera samples.
  * No Preview `nopreview` - No preview is shown when camera samples.
  * Limited Preview `limited` - The level of detail of the preview is limited.
  * Full Preview `full` - Preview displays all available points.

- Maximum Memory `maxmemory` - Sets the maximum memory used for spatial mapping.
- Resolution `resolution` - Sets the spatial mapping resolution used by the camera. A smaller resolution creates a detailed geometry and higher resolution keeps only bigger vairiations in geometry.
- Range `range` - Sets distance range of objects that will be extracted after spatial mapping from the camera. A smaller depth range will use objects close to the camera and higher depth range will use objects that are farther from the camera.
- Normals `normals` - When enabled, the extracted geometry will have normals.
- Texture `texture` - The spatial mapping texture and texture coordinates of the mesh will be created when enabled. The spatial mapping texture can be retrieved using the ZED TOP.
- Filter `filter` - ⊞ - Set the filtering level of the mesh.
  * Low `low` - Small holes in the geometry will be removed.
  * Medium `medium` - Geometry will be smoothed.
  * High `high` - The number of traingles in the geometry will be reduced and the geometry will be smoothed.

- Consolidate Points `consolidatepts` - When enabled, redundant points that are closed together will be merged.

## Info CHOP Channels
Extra Information for the ZED SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
