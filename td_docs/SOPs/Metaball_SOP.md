---
url: https://docs.derivative.ca/Metaball_SOP
category: SOPs
title: Metaball_SOP
---

# Metaball SOP
## Summary

The Metaball SOP creates metaballs and meta-superquadric surfaces. Metaballs can be thought of as spherical force fields whose surface is an implicit function defined at any point where the density of the force field equals a certain threshold. Because the density of the force field can be increased by the proximity of other metaball force fields, metaballs have the unique property that they change their shape to adapt and fuse with surrounding metaballs. This makes them very effective for modeling organic surfaces. For example, below we have a metaball. The surface of the metaball exists whenever the density of the metaball's field reaches a certain threshold:
[![MetaExample1.jpg](https://docs.derivative.ca/images/9/92/MetaExample1.jpg)](https://docs.derivative.ca/File:MetaExample1.jpg)
When two or more metaball force fields are combined, as in the illustration below, the resulting density of the force fields is added, and the surface extends to include that area where the force fields intersect and create density values with a value of one. For more information on metaballs, see [Metaballs](https://docs.derivative.ca/Metaball "Metaball").
[![MetaExample2.jpg](https://docs.derivative.ca/images/8/80/MetaExample2.jpg)](https://docs.derivative.ca/File:MetaExample2.jpg)
###
Level of Detail for Metaball Display
You can change the level of detail of the metaball and NURBS display by adjusting the Level of Detail parameter in the Display Option Dialog > Viewport page > Level of Detail option. To open the Display Options Dialog, press "p" in a SOP viewport.

###
Better Metaball Shading Tip
Accurate metaball normals will be computed if the normal attribute exists when conversion to polygons is done. Thus, to get improved shading on polygonized metaballs, it's a good idea to add the normal attribute (i.e. use a [Facet SOP](https://docs.derivative.ca/Facet_SOP "Facet SOP")) before converting the metaballs.
[metaballSOP_Class](https://docs.derivative.ca/MetaballSOP_Class "MetaballSOP Class")

## Parameters - Page
- Modify Bounds `modifybounds` - Available only when an input is connected to the Metaball SOP to set bounds for the metaball. When Modify Bounds = On the transform parameters below will further modify the position and radius of the bounds.
- Radius `rad` - ⊞ - Controls the radius of the metaball field.
  * X `radx` -
  * Y `rady` -
  * Z `radz` -

- Center `t` - ⊞ - Metaball center in X, Y and Z.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Weight `metaweight` - Defines the weight of the Metaball iso-surface within metaball field. An increase in weight makes the density of the metaball greater, and thus the defined implicit surface of it and surrounding metaballs will be enlarged.
- Kernel Function `kernel` - There are four different metaball interpretations: Wyvill, Elendt, Blinn and Links. See the [Geometry](https://docs.derivative.ca/Category:Geometry "Category:Geometry") articles for illustrations of the differences between these.
- XY Exponent `expxy` - The XY Exponent determines inflation / contraction in the X and Y axes.
- Z Exponent `expz` - The Z Exponent determines inflation / contraction in the Z axis.
- Compute Normals `normals` - Creates normals on the geometry.
###
What is an Exponent?
In the instance of metaballs, the exponent determines the inflation towards "squarishness" or contraction towards "starishness" as described below:
  * Value > 1 - Results in metaballs that appear more like a "star".
  * Value < 1 - Results in metaballs that appear more "squarish".
  * Value = 1 - Results in metaballs that appear spherical.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Metaball SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
