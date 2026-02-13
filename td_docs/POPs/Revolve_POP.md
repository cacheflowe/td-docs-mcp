---
url: https://docs.derivative.ca/Revolve_POP
category: POPs
title: Revolve_POP
---

# Revolve POP
## Summary

The Revolve POP generates a surface of revolution from any set of line strips. The points of the line strip are swept around a chosen axis, generating a mesh of points that are connected together according to the Connectivity menu.
The default Connectivity is quads, suitable for surface rendering, but the mesh can be connected as line strips in either direction, or simply unconnected points.
The axis can be the X Y or Z axis, but the default axis is formed by the first and last point of the line strip. (Auto-Pivot on)
Each line strip generates its own surface of revolution.
[revolvePOP_Class](https://docs.derivative.ca/RevolvePOP_Class "RevolvePOP Class")

## Parameters - Revolve Page
- Axis `axis` - ⊞ - The axis around which to revolve the input curve to create the output geometry.
  * Auto `auto` -
  * X `x` -
  * Y `y` -
  * Z `z` -

- Auto Pivot `autopivot` - Make the pivot axis be the line between the first point and the last point for each line strip.
- Pivot `p` - ⊞ - The pivot point for the transform rotates and scales.
  * Pivot `px` -
  * Pivot `py` -
  * Pivot `pz` -

- Connectivity `surftype` - ⊞ - Determines the primitive used to connect the points.
  * None `none` -
  * Point Prims `points` -
  * Rows `rows` -
  * Columns `cols` -
  * Rows and Columns `rowcol` -
  * Triangles `triangles` -
  * Alternating Triangles `alttriangles` -
  * Quadrilaterals `quads` -

- Divisions `divs` - The number of divisions.
- Texture Coordinates `texture` - ⊞ - Sets the attribute class where the texture coordinates should be created.
  * None `none` -
  * Point `pointNormals` -
  * Vertex `vertNormals` -

- Normal `normal` - ⊞ - Choose whether to create a normal attribute and the attribute class of the normal attribute.
  * None `none` -
  * Point `pointNormals` -
  * Vertex `vertNormals` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Revolve POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
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
