---
url: https://docs.derivative.ca/Resample_SOP
category: SOPs
title: Resample_SOP
---

# Resample SOP
## Summary

The Resample SOP will resample one or more primitives into even length segments. It only applies to polygons so when presented with a NURBS or Bzier curve input, it first converts it to polygons using the Level of Detail parameter.
[resampleSOP_Class](https://docs.derivative.ca/ResampleSOP_Class "ResampleSOP Class")

## Parameters - Page
- Group `group` - Allows you to specify which primitives or group of primitives to resample. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Level of Detail `lod` - If the geometry you are performing this operation on is made up of something other than polygons (e.g. a NURBS circle), this parameter determines how detailed the conversion to polygons will be. The higher the level of detail, the more precise the resampling process.
- Resample by Polygon Edge `edge` - This toggle allows the resampling to be done on a per-edge basis of the polygon rather than on the polygon as a whole. This means that corners will be preserved in the resampling. When this parameter is enabled, the Measure Method will be disabled. If the Segment Length is specified, only edges which are longer than the specified length will be subdivided. Each edge will be evenly subdivided so that the maximum length of each subdivision is less than or equal to the length specified.
If the Maximum Segments is chosen, the edges will not be split into more segments than are specified. If the length parameter is turned off, then each edge will be split into the specified number of segments.
- Method `method` - ⊞ - Specifies how the geometry is segmented.
  * Even Length Segments `dist` - Even-length measures are made along the original input

    [![TouchGeometry199.gif](https://docs.derivative.ca/images/6/65/TouchGeometry199.gif)](https://docs.derivative.ca/File:TouchGeometry199.gif)
  * Even X Segments `x` - * Even X spaced Segments

    [![TouchGeometry209.gif](https://docs.derivative.ca/images/f/ff/TouchGeometry209.gif)](https://docs.derivative.ca/File:TouchGeometry209.gif)
  * Even Y Segments `y` - Similar to X, but along Y axis.
  * Even Z Segments `z` - Similar to X, but along Z axis.

- Measure `measure` - ⊞ - Specifies how to measure along curved spline sections.
  * Along Arc `arc` - This method of measurement divides the curve itself into even length segments.
  * Along Chord `chord` - This method creates straight even-length segments between the evaluated points on the primitive. This is faster but not as accurate.

[![TouchGeometry202.gif](https://docs.derivative.ca/images/a/a5/TouchGeometry202.gif)](https://docs.derivative.ca/File:TouchGeometry202.gif)
- Maximum Segment Length `dolength` - When this option is enabled, it overrides the value of the Arc/Chord length and allows you to specify your own values for the length of the segments in the resampled geometry. Smaller values produce smoother interpolation.
- Length `length` - This parameter lets you specify the Arc/Chord length for the resampled geometry.
- Maximum Segments `dosegs` - When enabled, allows you to override the maximum number of segments used in the resampled geometry.
- Segments `segs` - Lets you specify the number of segments used when measuring along arc.
When both Maximum Segment Length and Maximum Segments are selected, the resultant polygon is constrained to a fixed length which may be shorter than the original input curve.
When only Maximum Segments is selected, the segments span the full distance of the original input curve.
When neither option is selected, the input curve is merely converted to a polygon.
- Maintain Last Vertex `last` - If selected, the primitive's final CV is included in the resampled polygon, even if the final resulting edge is shorter then the given segment length.

## Example
To create a constant length flag with the Resample SOP:
  1. Create a number of horizontal lines using a [Grid SOP](https://docs.derivative.ca/Grid_SOP "Grid SOP"): Primitive Type: Polygon; Connectivity: Rows; Size: 3, 1
  2. Append a [Group SOP](https://docs.derivative.ca/Group_SOP "Group SOP"): Group: group1; Entity: Points; Number: Enable; Pattern: 0-99:1,10
  3. Append a [Spring SOP](https://docs.derivative.ca/Spring_SOP "Spring SOP"): Source Group: group1; Forces/Wind: 1, 0, 0; Turbulence: 1, 0, -1
  4. Clip each line to a constant length by appending a Resample SOP: Maximum Segments On; Segments: 15
  5. Appending a [Skin SOP](https://docs.derivative.ca/Skin_SOP "Skin SOP") whose parameters can stay at the default, and enable the Points display in the Viewport options.
  6. Click Play to view the result. Adjust the view as necessary.
  7. Toggle the display SOP back and forth between the Spring SOP and the Skin SOP. Notice how the lines are stretched and deformed from their original length by the forces acting on them in the Spring SOP. After resampling, they are a constant length.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Resample SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
