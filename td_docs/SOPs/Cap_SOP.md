---
url: https://docs.derivative.ca/Cap_SOP
category: SOPs
title: Cap_SOP
---

# Cap SOP
## Summary

The Cap SOP is used to close open areas with flat or rounded coverings. Meshes are capped by extending the mesh in either the U or V direction (e.g. a NURBS tube). Faces are capped by appending a separate face or hull cap.
[capSOP_Class](https://docs.derivative.ca/CapSOP_Class "CapSOP Class")

## Parameters - Page
- Group `group` - Specify the Primitive Group to apply the caps to. See [Group SOP](https://docs.derivative.ca/Group_SOP "Group SOP") to create primitive groups.

## Parameters - U Caps Page
- Preserve NURB Shape U `pshapeu` - When capping a NURBS surface, use this option to preserve the original surface by clamping it at the point of capping.
- First U Cap `firstu` - ⊞ - Select an option from the menu:
  * No End Cap `none` - Leave this side of the primitive unaffected.
  * End Cap Faceted `facet` - Cap by creating a face of a similar type which uses unique points.
  * End Cap Shared `share` - Cap by creating a face of a similar type which shares points with the original primitive.
  * End Cap Rounded `round` - Cap by creating / extending a mesh containing a number of concentric circular regions. This creates a bullet or domed shaped cap.
  * End Cap Tangential `tangent` -

- Divisions `divsu1` - Number of cross sections in the rounded cap.
- Scale `scaleu1` - Affects the height of the rounded cap (both positive and negative).
- Last U Cap `lastu` - ⊞ - Similar to First Cap U / V, but builds a cap on the other end of the primitive in the opposite direction.
  * No End Cap `none` -
  * End Cap Faceted `facet` -
  * End Cap Shared `share` -
  * End Cap Rounded `round` -
  * End Cap Tangential `tangent` -

- Divisions `divsu2` - Number of cross sections in the rounded cap.
- Scale `scaleu2` - Affects the height of the rounded cap (both positive and negative).

## Parameters - V Caps Page
- Preserve NURB Shape V `pshapev` - When capping a NURBS surface, use this option to preserve the original surface by clamping it at the point of capping.
- First V Cap `firstv` - ⊞ - Select an option from the menu:
  * No End Cap `none` - Leave this side of the primitive unaffected.
  * End Cap Faceted `facet` - Cap by creating a face of a similar type which uses unique points.
  * End Cap Shared `share` - Cap by creating a face of a similar type which shares points with the original primitive.
  * End Cap Rounded `round` - Cap by creating / extending a mesh containing a number of concentric circular regions. This creates a bullet or domed shaped cap.
  * End Cap Tangential `tangent` -

- Divisions `divsv1` - Number of cross sections in the rounded cap.
- Scale `scalev1` - Affects the height of the rounded cap (both positive and negative).
- Last V Cap `lastv` - ⊞ - Similar to First Cap U / V, but builds a cap on the other end of the primitive in the opposite direction.
  * No End Cap `none` -
  * End Cap Faceted `facet` -
  * End Cap Shared `share` -
  * End Cap Rounded `round` -
  * End Cap Tangential `tangent` -

- Divisions `divsv2` - Number of cross sections in the rounded cap.
- Scale `scalev2` - Affects the height of the rounded cap (both positive and negative).

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Cap SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
