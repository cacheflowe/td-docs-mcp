---
url: https://docs.derivative.ca/Copy_SOP
category: SOPs
title: Copy_SOP
---

# Copy SOP
## Summary

The Copy SOP lets you make copies of the geometry of other SOPs and apply a transformation to each copy.
It also allows you to copy geometry to points on an input template.
[copySOP_Class](https://docs.derivative.ca/CopySOP_Class "CopySOP Class")

## Parameters - Copy Page
Specifies a subset of template primitives from which to copy onto. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Source Group `sourcegrp` - Specifies a subset of input primitives to copy from. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Template Group `templategrp` - Specifies a subset of template primitives from which to copy onto. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Number of Copies `ncy` - Sets number of Copies to be made of the source. For a template input, it specifies the number of copies to be placed at each point of the template.
- Primitives per Point `nprims` - Defines how many primitives to copy from each point.
- Rotate to Normal `nml` - Only used when a template input is specified. If the template is a sphere, and the first input is a circle, a circle is placed at each point of the sphere. With this option on, all the circles will re-orient to face the surface of the sphere (a default sphere has normals radiating outwards from the center).
If an up attribute exists on the template geometry, then this will be used (along with the normal) to fully define the rotates for the copies. An up attribute is created with the Point SOP.
- Transform Cumulative `cum` - Each transformation "builds" on the location left by the one before it. Transformations are cumulative as the Copy SOP produces new copies.
- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations. The Transform Order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the order of the rotations within the overall transform order.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference.
  * X `px` -
  * Y `py` -
  * Z `pz` -

- Uniform Scale `scale` - Uniform Scale allows you to shrink or enlarge geometry along all three axes simultaneously.
- Normals Maintain Length `vlength` - Vector type attributes (i.e. normals, velocity) maintain the same length under transforms. i.e. When geometry is scaled, the normals remain constant in length.
- Create Output Groups `newg` - If selected, this creates a group for each copy number, and places each primitive created at that stage into it.
- Copy Groups `copyg` - Defines the base name of the groups created.
- Look At `lookat` - Orients the copied geometry to lookat, or point to, the [object](https://docs.derivative.ca/Object "Object") component specified in the parameter.
- Up Vector `upvector` - ⊞ - When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat object passes through the Y axis of the target object.
  * X `upvectorx` -
  * Y `upvectory` -
  * Z `upvectorz` -

## Parameters - Stamp Page
Stamping is allowed in any parameter in TouchDesigner. The only requirement is that the stamped parameter is upstream in some fashion from the Copy SOP doing the stamping.
- Stamp Inputs `stamp` - When enabled, it will Stamp proceeding variables for each input copied.
- Copy `copy` - Sequence of stamp variables
- Param `copy0param` - Token of each stamp variable. Stamped parameters are accessible via the global `fetchStamp()` method in the [td Module](https://docs.derivative.ca/Td_Module "Td Module") in python, or `param()` in tscript. See the example, below.
- Value `copy0value` - Value of each stamp variable. Stamped parameters are accessible via the global `fetchStamp()` method in the [td Module](https://docs.derivative.ca/Td_Module "Td Module") in python, or `param()` in tscript. See the example, below.

## Parameters - Attributes Page
This page allows you to determine how point attributes on template geometry affect attributes on the source geometry. The template attribute can modify the source in four ways:
  * Set - Override the source attribute.
  * Multiply - Multiply the source attribute.
  * Add - Get Added to the source attribute.
  * Sub - Get Subtracted from the source attribute.

The template point attributes are able to affect point, primitive, or vertex attributes in the source geometry simply by entering values in the appropriate fields.
- Use Template Point Attribs `doattr` - Enables the parameters below to allow template point attributes to be applied to the copied source geometry.
- Copy to Point `setpt` - ⊞ - Copy the attributes to the source geometry's points.
  * * `*` -

- Copy to Primitive `setprim` - ⊞ - Copy the attributes to the source geometry's primitives.
  * * `*` -

- Copy to Vertex `setvtx` - ⊞ - Copy the attributes to the source geometry's vertices.
  * * `*` -

- Multiply Point `mulpt` - ⊞ - Multiply the attributes with the source geometry's point attributes.
  * * `*` -

- Multiply Primitive `mulprim` - ⊞ - Multiply the attributes with the source geometry's primitive attributes.
  * * `*` -

- Multiply Vertex `mulvtx` - ⊞ - Multiply the attributes with the source geometry's vertex attributes.
  * * `*` -

- Add Point `addpt` - ⊞ - Add the attributes to the source geometry's point attributes.
  * * `*` -

- Add Primitive `addprim` - ⊞ - Add the attributes to the source geometry's primitive attributes.
  * * `*` -

- Add Vertex `addvtx` - ⊞ - Add the attributes to the source geometry's vertex attributes.
  * * `*` -

- Subtract Point `subpt` - ⊞ - Subtract the attributes from the source geometry's point attributes.
  * * `*` -

- Subtract Primitive `subprim` - ⊞ - Subtract the attributes from the source geometry's primitive attributes.
  * * `*` -

- Subtract Vertex `subvtx` - ⊞ - Subtract the attributes from the source geometry's vertex attributes.
  * * `*` -

Tips
You can use the `me.copyTotal` python member to calculate the degrees of rotation for a given number of copies. For example, if you have 28 copies, you can set the rotation to be: `360/me.copyTotal` - this would automatically give you 12.8571 degrees, evenly spacing your 28 copies around the full circumference of the circle.
Using a Particle SOP as the Template object, you can copy objects defined in the Copy Data input to each particle template. This allows you, for example, to copy a Bee to each particle to create a swarm of bees.
Make a series of copies about an axis, and skin them to achieve lathe-like effects, similar to the results achieved with the Revolve SOP.

## Examples
###
Creating Stamped Geometry
  1. Place a Circle SOP, and set its type to Polygon.
  2. Set the number of Divisions in the Circle to: `fetchStamp("sides",3)` The method `fetchStamp()` returns the value of the global parameter sides. If it is not yet defined it will return a value of 3.
  3. Append a Copy SOP, and set the Number of Copies to `5`; and set Translate X to: `2.5` .
  4. In the Stamp page of the Copy SOP, turn on Stamp Inputs. Set Param 1 to: `sides` and `me.copyIndex+3`[![CopySOPStampPage.png](https://docs.derivative.ca/images/d/d9/CopySOPStampPage.png)](https://docs.derivative.ca/File:CopySOPStampPage.png)
  5. This creates a triangle on the first stamped copy; a square on the next; a pentagon on the third, and so on. The geometry for each copy is cooked separately.

[![CopySOPStampExample.png](https://docs.derivative.ca/images/0/02/CopySOPStampExample.png)](https://docs.derivative.ca/File:CopySOPStampExample.png)
You can set multiple stamp Params at once and they can be used anywhere in the ancestry of the copy's input.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Copy SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
