---
url: https://docs.derivative.ca/Sort_SOP
category: SOPs
title: Sort_SOP
---

# Sort SOP
## Summary

The Sort SOP allows you to sort points and primitives in different ways. Sometimes the primitives are arranged in the desired order, but the point order is not. There are many possible combinations. To sort vertices, use the [Primitive SOP](https://docs.derivative.ca/Primitive_SOP "Primitive SOP").
[sortSOP_Class](https://docs.derivative.ca/SortSOP_Class "SortSOP Class")

## Parameters - Point Page
- Point Sort `ptsort` - ⊞ - Sort the points in the input geometry, according to the following criteria:
  * No change `none` - No sorting is applied.
  * By vertex order `vtxord` - Order points in same order as vertices.
  * By x `byx` - Sort according to X position.
  * By y `byy` - Sort according to Y position.
  * By z `byz` - Sort according to Z position.
  * Reverse `rev` - Reverse the point order.
  * Random `seed` - Randomize point order using the specified seed without changing the point positions.
  * Shift `shift` - Shift points by the amount specified on the Offset parameter.
  * Proximity to Point `prox` - Sort points by their proximity to the specified point.
  * Along Vector `vector` - Sorts points along either a user or object-defined vector.
  * Distance to Object `object` - Sorts points based on distance to the object specified in the Vector Object parameter.
  * Closest Neighbour `neighbour` - Reorders points based on next closest. Slow nxn search.

- Seed `pointseed` - The random seed when Point Sort is set to Random.
- Offset `pointoffset` - Shift point order by the amount specified on the offset line.
- Point `pointprox` - ⊞ - The X, Y and Z coordinates to reference when sorting by Proximity to Point.
  * X `pointproxx` -
  * Y `pointproxy` -
  * Z `pointproxz` -

- Vector Object `pointobj` - Sort points along a vector defined by the object's transformation values.
- Vector `pointdir` - ⊞ - Allows you to specify a unique vector along which points can be sorted.
  * X `pointdirx` -
  * Y `pointdiry` -
  * Z `pointdirz` -

## Parameters - Primitive Page
- Primitive Sort `primsort` - ⊞ - Sort the primitives according to the following criteria:
  * No change `none` - No sorting is applied.
  * By x `byx` - Sort according to X position.
  * By y `byy` - Sort according to Y position.
  * By z `byz` - Sort according to Z position.
  * By Type `bytype` -
  * Reverse `rev` - Reverse primitive order.
  * Random `seed` - Randomize primitive order using the specified seed without changing the primitive positions.
  * Shift `shift` - Shift primitives by the amount the specified on the Offset parameter.
  * Proximity to Point `prox` - Sort primitives by their proximity to the specified point.
  * Along Vector `vector` - Sorts primitives along either a user or object-defined vector.
  * Distance to Object `object` - Sorts primitive based on distance to the object specified in the Vector Object parameter.

- Seed `primseed` - Random seed when sorting by Random.
- Offset `primoffset` - Shift primitive order by the amount specified on the offset line.
- Point `primprox` - ⊞ - The X, Y and Z coordinates to reference when sorting by Proximity to Point.
  * X `primproxx` -
  * Y `primproxy` -
  * Z `primproxz` -

- Vector Object `primobj` - Sort primitives along a vector defined by the object's translation.
- Vector `primdir` - ⊞ - Allows you to specify a unique vector along which primitives can be sorted.
  * X `primdirx` -
  * Y `primdiry` -
  * Z `primdirz` -

## Parameters - Particle Page
Particles are sorted on a per-particle system basis. That is if you have a SOP with 2 different particle system primitives, they are sorted independently of each other.
- Particle Sort `partsort` - ⊞ - Sort the primitives according to the following criteria:
  * No change `none` - No sorting is applied.
  * By x `byx` - Sort according to X position.
  * By y `byy` - Sort according to Y position.
  * By z `byz` - Sort according to Z position.
  * Reverse `rev` - Reverse particle order.
  * Shift `shift` - Shift particles by the amount the specified on the Offset parameter.
  * Proximity to Point `prox` - Sort particle by their proximity to the specified point.
  * Along Vector `vector` - Sorts particles along either a user or object-defined vector.
  * Distance to Object `object` - Sorts particles based on distance to the object specified in the Vector Object parameter.

- Reverse Results `partreverse` - Reverses the result from the Particle Sort as defined above.
- Offset `partoffset` - Shift particle order by the amount specified on the offset line.
- Point `partprox` - ⊞ - The X, Y and Z coordinates to reference when sorting by Proximity to Point.
  * X `partproxx` -
  * Y `partproxy` -
  * Z `partproxz` -

- Vector Object `partobj` - Sort particles along a vector defined by the object's translation.
- Vector `partdir` - ⊞ - Allows you to specify a unique vector along which particles can be sorted.
  * X `partdirx` -
  * Y `partdiry` -
  * Z `partdirz` -

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Sort SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
