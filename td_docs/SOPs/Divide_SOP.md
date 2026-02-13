---
url: https://docs.derivative.ca/Divide_SOP
category: SOPs
title: Divide_SOP
---

# Divide SOP
## Summary

The Divide SOP divides incoming polygonal geometry. It will smooth input polygons, dividing polygons, as well as sub-divide input polygons using the Bricker option. Bricker is also useful for polygon faces with more than four edges to chop them up into quads and triangles allowing for proper shading when using deformation tools.
[divideSOP_Class](https://docs.derivative.ca/DivideSOP_Class "DivideSOP Class")

## Parameters - Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Convex Polygons `convex` - When checked, this option will convex all incoming polygons to the maximum number of sides as specified in the field below. This is useful for reducing the number of sides of polygons that are concave and not shading properly, e.g. to generate triangles from all incoming geometry, check this option and change the Maximum Edges field below to `3`. You will see that all of the polygons are reduced to three sides maximum (triangles).
- Maximum Edges `numsides` - Input value determines the maximum number of edges that all of the input polygons will be reduced to if they exceed this number. Sets the maximum number of sides for convexed polygons. There must be at least three sides. Using small numbers in the range of 3-6 gives the best results; the resulting polygons are not so long and thin. If input polygons have fewer edges than specified, no change will be executed on those polygons.
- Triangulate Non-Planar `planar` - Triangulates any non-planar polygons.
- Smooth Polygons `smooth` - If checked, this feature will divide the polygons which are adjacent to each other and are not flat, as in the corners of a box. The threshold of the smoothing and the amount of polygon divisions that are added are controlled by the fields below.
All incoming geometry must have shared points for Smooth Polygons to work. You may have to pass the geometry through a [Facet SOP](https://docs.derivative.ca/Facet_SOP "Facet SOP") > Consolidate Points to achieve this. For example, to create a dice from a box, add a [Box SOP](https://docs.derivative.ca/Box_SOP "Box SOP") followed by a Facet SOP> Consolidate Points then through the Divide SOP with Smooth Polygons enabled; set the Weight fields set to: `4,0.5` and the Divisions set to: `2`.
- Weight `weight` - ⊞ - Determines the localization effect of the added polygons. You can isolate the divisions to where there are edges in the geometry with values greater than 1 enhancing the edges by smoothing out the angle transitions. Values less than 1 tend to put the divisions in the flatter areas of the source geometry and alter the shape of the geometry considerably by pulling in the edges.
  * `weight1` -
  * `weight2` -

- Divisions `divs` - Determine the level of sub-divisions for the Smooth Polygons option. A value of `1` doubles the number of polygons at the corners, a value of `2` will add twice as much sub-division. Values of `3` and greater may add a substantial number of polygons and should be used with care - you can exponentially increase the complexity.
- Bricker Polygons `brick` - Selecting this option divides the input polygon geometry into grid-like squares, though the output is not a mesh. Brickering creates new polygons. It can be used to divide a surface so that it deforms more naturally when wrapped on another surface using a [Creep SOP](https://docs.derivative.ca/Creep_SOP "Creep SOP"), or twisted with a [Lattice SOP](https://docs.derivative.ca/Lattice_SOP "Lattice SOP").
It can also be used to divide a planar surface into smaller pieces to apply point colors using a [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"). The size and location of the square divisions created by brickering is determined by the following three options.
- Size `size` - ⊞ - Sets the size of the bricker grid divisions in each of the three axes.
  * X `sizex` -
  * Y `sizey` -
  * Z `sizez` -

- Offset `offset` - ⊞ - Sets the XYZ offset of the grid divisions to the **Source** geometry (the **Brickering Grid** is moved).
  * X `offsetx` -
  * Y `offsety` -
  * Z `offsetz` -

- Angle `angle` - ⊞ - Determines the angle relative to XYZ axes, at which Bricker Polygons are created.
  * X `anglex` -
  * Y `angley` -
  * Z `anglez` -

- Remove Shared Edges `removesh` - Eliminates any common edges.
- Compute Dual `dual` - Convert the polyhedron into its point/face dual.Convert the polyhedron into its point/face dual.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Divide SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
