---
url: https://docs.derivative.ca/Box_SOP
category: SOPs
title: Box_SOP
---

# Box SOP
## Summary

The Box SOP creates cuboids. These can be used as geometries by themselves, or they can be sub-divided for use with the Lattice SOP.
If it has an input then it will create a box that bounds the incoming geometry. Otherwise, the parameters determine the size and location of the box.
[boxSOP_Class](https://docs.derivative.ca/BoxSOP_Class "BoxSOP Class")

## Parameters - Page
- Orient Bounds `orientbounds` - Available only when an input is connected to the Box SOP to set bounds for the box. When Orient Bounds = On it will rotate the geometry to match the orientation of the input SOP used for bounds.
- Modify Bounds `modifybounds` - Available only when an input is connected to the Box SOP to set bounds for the box. When Modify Bounds = On to enable the transform parameters below to further modify the position and scale of the bounds.
- Rotate Order `rord` - ⊞ - Sets the order in which the rotations are applied.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Size `size` - ⊞ - Size of the Box or Cube along the X, Y, and Z axes.
  * X `sizex` -
  * Y `sizey` -
  * Z `sizez` -

- Center `t` - ⊞ - These X,Y, and Z Values determine where the center of the Box is located.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the Box along the X, Y, and Z axes.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - Adjusts the uniform scale of the box.
- Reverse Anchors `reverseanchors` - Invert the direction of anchors.
- Anchor U `anchoru` - Set the point in X about which the geometry is positioned, scaled and rotated.
- Anchor V `anchorv` - Set the point in Y about which the geometry is positioned, scaled and rotated.
- Anchor W `anchorw` - Set the point in Z about which the geometry is positioned, scaled and rotated.
- Use Divisions `dodivs` - If checked, it divides the box into the number of Divisions specified below. Boxes divided in this way do not appear when rendered because the Divisions consist of open polygons.
- Divisions `divs` - ⊞ - The number of divisions in X, Y, and Z to split this Box into.
  * X `divsx` -
  * Y `divsy` -
  * Z `divsz` -

- Enforcement Bars `rebar` - Places four diagonal crossbars in each division of the Box.
- Consolidate Corner Points `consolidatepts` - Merges the corner points together. Instead of the box being composed of 6 separate faces (resulting in 4 points per corner and a total of 24 points), the corner points are merged together and the box is composed of 8 points.
- Texture Coordinates `texture` - ⊞ - Determines how the texture coordinates are applied to the box.
  * Off `off` -
  * Box Inside `boxinside` -
  * Face Inside `faceinside` -
  * Cube Map Inside `cubemapinside` -
  * Box Outside `boxoutside` -
  * Face Outside `faceoutside` -
  * Cube Map Outside `cubemapoutside` -

- Compute Normals `normals` - Checking this option on will compute surface normals.

Uses
To create boxes.
You can use the points as an input geometry for the Lattice and Spring SOPs.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Box SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
