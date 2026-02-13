---
url: https://docs.derivative.ca/Polypatch_SOP
category: SOPs
title: Polypatch_SOP
---

# Polypatch SOP
## Summary

The Polypatch SOP creates a smooth polygonal patch from a mesh primitive or a set of faces (polygons, NURBS or Bezier curves).
[polypatchSOP_Class](https://docs.derivative.ca/PolypatchSOP_Class "PolypatchSOP Class")

## Parameters - Polypatch Page
- Group `group` - Subset of input to use. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Basis `basis` - ⊞ - Select spline type: Cardinal or BSpline.
  * Cardinal `cardinal` -
  * BSpline `bspline` -

- Connectivity `connecttype` - ⊞ - This option is used to select how the points of the created surface are connected.
  * Rows `rows` - Creates horizontal lines, which are open polygons.
  * Columns `cols` - Creates vertical lines, which are open polygons.
  * Rows and Columns `rowcol` - Both rows and columns, all open polygons.
  * Triangles `triangles` - Build the grid with triangles.
  * Quadrilaterals `quads` - Default grid connection - four-sided quadrilaterals.
  * Alternating Triangles `alttriangles` - Generates triangles that are opposed; similar to the Triangles option.
  * Inherit from Source `inheritconnect` - When this connectivity option is selected, the output mesh will have the same connectivity as the input hull mesh.

- U Wrap `closeu` - ⊞ - Settings for wrapping in U direction.
  * Off `nonewu` - Do not wrap in U/V.
  * On `wu` - Wrap in U/V.
  * If Primitive does `ifprimwu` - Wrap in U/V if the input primitive does.

- V Wrap `closev` - ⊞ - Settings for wrapping in V direction.
  * Off `nonewv` - Do not wrap in U/V.
  * On `wv` - Wrap in U/V.
  * If Primitive does `ifprimwv` - Wrap in U/V if the input primitive does.

- U Clamp (First) `firstuclamp` - ⊞ - Settings for clamping first end in U.
  * Off `firstuclampoff` - Do not clamp the first/last end in the U/V direction.
  * On `firstuclampon` - Clamp the first/last end in the U/V direction.
  * If primitive does `firstuclampifprim` - Clamp the first/last end in the U/V direction if the input primitive does.

- U Clamp (Last) `lastuclamp` - ⊞ - Settings for clamping last end in U.
  * Off `lastuclampoff` - Do not clamp the first/last end in the U/V direction.
  * On `lastuclampon` - Clamp the first/last end in the U/V direction.
  * If primitive does `lastuclampifprim` - Clamp the first/last end in the U/V direction if the input primitive does.

- V Clamp (First) `firstvclamp` - ⊞ - Settings for clamping first end in V.
  * Off `firstvclampoff` - Do not clamp the first/last end in the U/V direction.
  * On `firstvclampon` - Clamp the first/last end in the U/V direction.
  * If primitive does `firstvclampifprim` - Clamp the first/last end in the U/V direction if the input primitive does.

- V Clamp (Last) `lastvclamp` - ⊞ - Settings for clamping last end in V.
  * Off `lastvclampoff` - Do not clamp the first/last end in the U/V direction.
  * On `lastvclampon` - Clamp the first/last end in the U/V direction.
  * If primitive does `lastvclampifprim` - Clamp the first/last end in the U/V direction if the input primitive does.

- Output Divisions `divisions` - ⊞ - The number of divisions in the output surface. Use more divisions for a smoother surface.
  * X `divisionsx` -
  * Y `divisionsy` -

- Output Polygons `polys` - Force polygonal rather than mesh output.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Polypatch SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
