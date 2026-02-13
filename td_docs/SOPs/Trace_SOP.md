---
url: https://docs.derivative.ca/Trace_SOP
category: SOPs
title: Trace_SOP
---

# Trace SOP
## Summary

The Trace SOP reads an image file and automatically traces it, generating a set of faces around areas exceeding a certain brightness threshold. You can control this threshold and the resolution of the resulting faces.
[traceSOP_Class](https://docs.derivative.ca/TraceSOP_Class "TraceSOP Class")

## Parameters - Trace Page
- TOP Name `top` - Specify the TOP image to trace.
- Threshold `thresh` - Brightness level value adjusts where trace outline in image occurs.
- Add Point Texture `addtexture` - This option allows the generation of point texture coordinates (UVs). This may occasionally be necessary when the Convert to Poly option is enabled.
- Remove Borders `delborder` - When enabled, this option eliminates extraneous data along the edges of the original image so it isn't traced. This is useful for when "dirty" edges exist in the original image that you don't want traced.
- Compute Normals `normals` - Creates normals on the geometry.

## Parameters - Filters Page
- Border Width `bordwidth` - The number of pixels the removal border should be.
- Resample Shapes `doresample` - Determines level of refinement (number of points) for generating trace outlines.
- Step Size `step` - Value controlling trace outline refinement when Resample Shapes is checked.
- Smooth Shapes `dosmooth` - When this option is checked, the geometry is filtered to remove sharp corners.
- Corner Delta `corner` - Value controlling corner smoothing when `Smooth Shapes` is checked.
- Fit to Curves `fitcurve` - If selected, the geometry at this point is converted to two-dimensional Bzier curves. Flat edges are preserved in polygons.
- Fitting Error `error` - Value controlling accuracy of the above curve fitting process. For best results, the input should retain as many points as possible, i.e. do not select Smooth Shapes or Resample Shapes.
- Convert to Poly `convpoly` - This option will convert the above curves back into polygons.
- Level of Detail `lod` - This value controls the accuracy of the conversion back into polygons.
- Hole Faces `hole` - This will bridge all holes in the output so that they may be rendered properly. Bzier curves and polygons can be holed, but polygonal holing sometimes produces better results. You may want to use the Convert to Poly option before holing.

## Info CHOP Channels
Extra Information for the Trace SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
