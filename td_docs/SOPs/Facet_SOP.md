---
url: https://docs.derivative.ca/Facet_SOP
category: SOPs
title: Facet_SOP
---

# Facet SOP
## Summary

The Facet SOP lets you control the smoothness of faceting of a given object. It also lets you consolidate points or surface normals.
The Facet SOP, like [Divide SOP](https://docs.derivative.ca/Divide_SOP "Divide SOP"), works as a pipeline to change geometry in stages. For this reason, Compute Normals appears twice. For example, you can compute surface normals before making vertices (the points of each polygon) unique, which gives you the unusual result of smooth shading and unique point, as the normals get computed while the points are still shared.
[facetSOP_Class](https://docs.derivative.ca/FacetSOP_Class "FacetSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Make Normals Unit Length `unit` - Checking this option will normalize the length of normals to a length of one unit.
- Compute Normals `prenml` - Checking this option means that the surface normals will be computed. Where points are shared between polygons, smooth shading results, and where points are not shared (unique), faceted edges result. If you compute normals at this stage, they are computed based on the incoming geometry.
- Unique Points `unique` - Makes each vertex have a unique point. The result of selecting this option is that all vertices are made into unique points, thus making all edges hard, with no smooth shading.
- Consolidate `cons` - ⊞ - Consolidate eliminates the redundancy of having many points that are close to each other, by merging them together to form a fewer set of common points. Consolidate is useful for cleaning up an edge that may appear between adjacent polygons that have been merged.
  * No Consolidate `none` - No consolidation.
  * Consolidate Points Slow `points` -
  * Consolidate Points Fast `fpoints` -
  * Consolidate Normals Slow `normals` -
  * Consolidate Normals Fast `fnormals` -

- Distance `dist` - Points and normals less than this distance apart will be consolidated, or have their normals averaged, based on the setting in the Consolidate menu.
Usually very small numbers, such as `0.01` should be used here. If the value is `0.0`, then points must be in exactly the same position (co-incident) in order to be considered for the consolidation/averaging function.
- Remove Inline Points `inline` - Removes points that lie inline with its neighboring points.
- Distance `inlinedist` - Set the distance threshold for removing inline points when the above parameter is On.
- Orient Polygons `orientpolys` - Orients all polygons so they have the same winding direction.
- Cusp Polygons `cusp` - Most of the time, you want some polygons to be smooth shaded and others to be faceted. Usually polygons that meet at low angles should be smooth shaded, and polygon edges that meet at sharper angles should be faceted.
- Cusp Angle `angle` - Cusping allows you to specify the threshold angle at which the edges become faceted. A good typical value is 20.
- Remove Degenerate `remove` - Sometimes (not often) your geometry can get messed up, where there are points hanging around that are not used for anything, or there are primitives that don't make sense. This option checks for these cases and removes them.
- Compute Normals `postnml` - Again, allows you to compute the normals after the consolidation or cusping stages. You should select this if you have set either the Cusp or Consolidate option.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Facet SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
