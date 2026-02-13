---
url: https://docs.derivative.ca/Subdivide_SOP
category: SOPs
title: Subdivide_SOP
---

# Subdivide SOP
## Summary

The Subdivide SOP takes an input polygon surface (which can be piped into one or both inputs), and divides each face to create a smoothed polygon surface using a Catmull-Clark subdivision algorithm. Especially useful for avoiding the angular appearance often associated with polygonal models - without adding lots of extra geometry to the entire object. For best results, polygons should be convex and relatively uniform in distribution.
Subdivision surfaces also allows you to create the smoothed surface based on a polygon control shape. As the control shape changes, so does the smooth shape within.
[subdivideSOP_Class](https://docs.derivative.ca/SubdivideSOP_Class "SubdivideSOP Class")

Creases and Cracks
###
Creases
Creases control the strength of pull of the polygon faces on the subdivision surfaces, much like a magnet drawing the surface towards the reference polygon. They can be applied selectively using the Creases field to specify an input group to use.
Creases work by controlling the strength of the pull of the polygon faces on the subdivision surfaces, like a magnet drawing the surface towards the reference polygon. The figure below shows the result of setting the Crease Weight to `0, 1, 2` reading from left to right. As the weight increases so the pull effect strengthens and the shape approaches the reference polygon.
[![Subdivision-Creases.gif](https://docs.derivative.ca/images/5/5e/Subdivision-Creases.gif)](https://docs.derivative.ca/File:Subdivision-Creases.gif)

###
The Crease Algorithm
If there is a second input:      If the Override button is enabled, each edge defined in the second input will have its edge crease weight set to the value of the override.     If the vertex attribute "`creaseweight`" exists on the second input, each matching edge in the input will have its crease weight set to the maximum of the vertex attributes for any shared edges.     If the primitive attribute "`creaseweight`" exists on the second input, each polygon in the second input will set matching edges to the appropriate weights.
If there is no second input:      If an override is specified, the value of the override is used for all edges in the sub-divided surface.     If the vertex attribute "`creaseweight`" exists, this attribute will be used to define the crease weights on the edges of the surface.     If the primitive attribute "`creaseweight`" exists, this attribute will be used to define the crease weights for the subdivision surface.
When defining crease weights on shared edges, the maximum of the weights of the shared edges is used. For example, if two polygons share an edge and the primitive attribute is used, the maximum of the crease weight will be used for the shared edge.

###
Closing Cracks
Cracks can be closed by either Pull Cracks Closed or Stitch Cracks Together, so only one of these two options can be chosen at a time from the Surrounding Faces parameter. Bias applies only to Pulling, and is disabled when Stitching is chosen.
A crack is formed by a single edge on the non-subdivided area and multiple edges on the subdivided area. The Surrounding Faces menu determines what will will happen to the single edge on the non-subdivided area, and in more generally, to the polygon containing this edge.
If No Edge Division is chosen and cracks are pulled closed, all the points on the subdivided edges are pulled (i.e. moved) to the closest points on the non-subdivided edges. Bias is disabled, when No Edge Division is specified.
If cracks are pulled with the Divide Edges option, the non-subdivided edge is split into many sections, so that each each point on the non-subdivided edge now corresponds to a new point on the subdivided edge. Then, points on the newly divided edge are joined with the points on the subdivided boundary. A Bias of `1` will place these joined points along the subdivided boundary. A Bias of `0` will place them along the non- subdivided boundary (and values between 0 and 1 will place them somewhere inbetween).
Pulling cracks with the Triangulate option will do exactly the same thing as Divide Edges, except it will also triangulate the non-subdivided polygon. This is desirable because pulling the non-subdivided boundary towards the curved subdivided boundary will likely generate a non-planar polygon, so Triangulate will divide this polygon into smaller (planar) ones. Pulling cracks with a Bias of `1` and triangulating usually produces the nicest results.
The Triangulate option is necessary because the [Divide SOP](https://docs.derivative.ca/Divide_SOP "Divide SOP") is not designed to handle (very) non-planar polygons.
The Stitch Cracks Together option, on the other hand, inserts new polygons (triangles) to close up the cracks. When No Edge Division is chosen, many triangles are created, each having one vertex on one point of the non-subdivided edge.
When Divide Boundary Edges is chosen, the non-subdivided edge is divided, so there are more points available to be used for triangles. The resulting triangles are more regularly shaped (not as long and skinny). The Triangulate option will again triangulate the non-subdivided polygon, although this option is less likely to be used becuase this polygon should remain planar during stitching.

## Parameters - Page
- Group `subdivide` - Subset of input to use as a polygonal mesh to subdivide. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Creases `creases` - This field allows you to specify a subset of the second input to use as creases. The elements of the second input specified by the Creases field are used as creases. Each edge in a crease polygon corresponds to the edge in the polygon mesh which has the same point numbers. Point position is irrelevant. For polygon edges to be classified as the same edge, they must share the same points. Merely being physically close is not sufficient.
The primitive attribute `creasesharpness` is used to determine the sharpness of the specified creases unless overridden.
- Depth `iterations` - How many iterations to subdivide. Higher numbers give a smoother surface.
- Override Crease Weight Attribute `overridecrease` - Determine if the crease sharpness should be determined by the primitive or vertex `creaseweight` attribute or by overridden by this SOP.
- Crease Weight `creaseweight` - If the crease weight is overriden, this is the weight used.
**Tip:** The default is to have the **Override Crease Weight Attribute** enabled. So you can simply set a value which applies to all the creases. You can, however, set a crease attribute using the Vertex or Primitive SOPs which allows for more control.
- Generate Resulting Creases `outputcrease` - If any creases are sharper than the Depth, they will be left over in the resulting geometry. With this parameter enabled, these left over creases are created with the appropriate primitive attribute values, and placed in the specified group.
- New Group `outcreasegroup` - Name of the group to place the generated creases into.
- Close Cracks `closeholes` - ⊞ - Choose how gaps are handled in the output geometry.
  * Do Not Close `noclose` - Don't close cracks.
  * Pull Cracks Closed `pull` - Move points on boundary of subdivided area in order to close cracks formed during the subdivision.
  * Stitch Cracks Together `stitch` - Add polygons (triangles) to close the cracks caused by subdividing.

- Surrounding Faces `surroundpoly` - ⊞ - Choose how to handle the polygons on either side of a crack when pulling or stitching it closed.
  * No Edge Division `nodiv` - When No Edge Division is chosen, many triangles are created, each having one vertex on one point of the non-subdivided edge.
  * Divide Edges `edges` - Divides edges surrounding the subdivided area when pulling or stitching cracks by inserting new polygons (triangles) to close up the cracks.
  * Triangulate `triangulate` - Does exactly the same thing as Divide Edges, except it also triangulates the non-subdivided polygon. This is desirable because pulling the non-subdivided boundary towards the curved subdivided boundary will likely generate a non-planar polygon, so Triangulate will divide this polygon into smaller (planar) ones. Pulling cracks with a Bias of 1 and triangulating usually produces the nicest results.

- Bias `bias` - Determines which points are moved when pulling crack closed.
  * 0 means move points on subdivided area to meet boundary.
  * 1 means move points on boundary to meet subdivided area.

## Example
Below, a Subdivide SOP is used to create a subdivision surface from a [Box SOP](https://docs.derivative.ca/Box_SOP "Box SOP"). The Depth of the subdivision is set to 2. The [Facet SOP](https://docs.derivative.ca/Facet_SOP "Facet SOP") consolidates the points so that the box faces are treated as a unit.
[![SubdivisionSOPeg.gif](https://docs.derivative.ca/images/8/8a/SubdivisionSOPeg.gif)](https://docs.derivative.ca/File:SubdivisionSOPeg.gif)

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Subdivide SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
