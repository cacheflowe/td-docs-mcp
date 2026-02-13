---
url: https://docs.derivative.ca/Attribute_SOP
category: SOPs
title: Attribute_SOP
---

# Attribute SOP
## Summary

The Attribute SOP allows you to manually rename and delete point, vertex, and primitive attributes.
The top portion of each parameter page deals with the deleting of a specifc type of attributes.
For example: `Cd Alpha`
[Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") - Deletion accepts general pattern matching when determining which attributes to delete. For example:

> `*` = Delete all attributes
> `Cd` = Delete the Cd attribute
> `Cd Alpha` = Delete Cd & Alpha attributes
> `a*` = Delete all attributes beginning with _a_
> `* ^Cd` = Delete all attributes except Cd

**Note:** You should never delete just one of the following attributes, but always keep/delete them together. This is because TouchDesigner's capture/deform system expects these three attributes to occur together. Deleting a subset of the three will cause errors as they are interdependent: `pCapt (point attribute), pCaptPath, pCaptData (detail attribute)`
See also: [Attribute Create SOP](https://docs.derivative.ca/Attribute_Create_SOP "Attribute Create SOP").
The next section of each page deals with renaming attributes. Specify the name of the original incoming attribute in the 'From Attribute' parameter, and the new name you want it renamed to in the 'To Attribute' parameter.
[attributeSOP_Class](https://docs.derivative.ca/AttributeSOP_Class "AttributeSOP Class")

## Parameters - Point Page
- Delete Attributes `ptdel` - ⊞ - Use the field to specify the point attributes to delete. Simply enter a list of the attributes (separated by spaces) to delete, for example entering:`Cd Alpha`. You can also use the dropdown menu on the right to select them.
  * * `*` -

- Point Rename `pt` - Sequence of point renames
- From Attribute `pt0from` - Specify the attribute you wish to rename, or select it from the dropdown menu on the right.
- To Attribute `pt0to` - Enter the new name for the attribute here.

## Parameters - Vertex Page
These tabbed pages are identical to the `Point` page except that they deal with vertex and primitive attributes of the input geometry.
- Delete Attributes `vertdel` - ⊞ - Use the field to specify the vertex attributes to delete. Simply enter a list of the attributes (separated by spaces) to delete, for example entering:`uv N`. You can also use the dropdown menu on the right to select them.
  * * `*` -

- Vertex Rename `vert` - Sequence of vertex renames
- From Attribute `vert0from` - Specify the attribute you wish to rename, or select it from the dropdown menu on the right.
- To Attribute `vert0to` - Enter the new name for the attribute here.

## Parameters - Primitive Page
Accepts geometry of all types.
- Delete Attributes `primdel` - ⊞ - Use the field to specify the primitive attributes to delete. Simply enter a list of the attributes (separated by spaces) to delete, for example entering:`Cd creaseweight`. You can also use the dropdown menu on the right to select them.
  * * `*` -

- Prim Rename `prim` - Sequence of primitive renames
- From Attribute `prim0from` - Specify the attribute you wish to rename, or select it from the dropdown menu on the right.
- To Attribute `prim0to` - Enter the new name for the attribute here.

## Parameters - Detail Page
- Delete Attributes `attrdel` - ⊞ - Use the field to specify the detail attributes to delete. Simply enter a list of the attributes (separated by spaces) to delete. You can also use the dropdown menu on the right to select them.
  * * `*` -

- Detail Rename `attr` - Sequence of detail renames
- From Attribute `attr0from` - Specify the attribute you wish to rename, or select it from the dropdown menu on the right.
- To Attribute `attr0to` - Enter the new name for the attribute here.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Attribute SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
