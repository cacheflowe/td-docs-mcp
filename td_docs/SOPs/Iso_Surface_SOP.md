---
url: https://docs.derivative.ca/Iso_Surface_SOP
category: SOPs
title: Iso_Surface_SOP
---

# Iso Surface SOP
## Summary

The Iso Surface SOP uses implicit functions to create 3D visualizations of isometric surfaces found in Grade 12 Functions and Relations textbooks.
An implicit function is defined so that it = 0. For example with:
```
x2 + y2 = r2

```

the implicit function is:
```
f(x, y) = x2 + y2 - r2 = 0

```

[isosurfaceSOP_Class](https://docs.derivative.ca/IsosurfaceSOP_Class "IsosurfaceSOP Class")

## Parameters - Page
- Implicit Function `func` - Enter the function for implicit surface building here.
Example 1: `(me.curPos.x**2) / (4*4) - (me.curPos.y**2) / (3*3) + me.curPos.z`
This formula creates a hyperbolic paraboloid, or saddle shape.
Example 2: `(me.curPos.x**2) / 0.1 + (me.curPos.y**2) / 2 + (me.curPos.z**2) / 6 - 1`
This formula creates an ellipsoid.
- Minimum Bound `min` - ⊞ - Determines the minimum clipping plane boundary for display of iso surface.
  * X `minx` -
  * Y `miny` -
  * Z `minz` -

- Maximum Bound `max` - ⊞ - Determines maximum clipping plane boundary for display of iso surfaces.
  * X `maxx` -
  * Y `maxy` -
  * Z `maxz` -

- Divisions `divs` - ⊞ - The density, or resolution of the iso surface polygons in X, Y and Z.
  * X `divsx` -
  * Y `divsy` -
  * Z `divsz` -

- Compute Normals `normals` - Adds normals to the surface.

## Example
The action of the Iso Surface sop is conceptually simple - it takes a user specified expression in R3 (a mathematical term meaning, "having three dimensions, each taking a Real value), and creates a surface where the function goes from being positive to being negative. In the case of the default expression ( `me.curPos[0] * me.curPos[0] + me.curPos[1] * me.curPos[1] + me.curPos[2] * me.curPos[2] - 1` ), the expression is less than zero within a unit sphere, and greater than zero outside. As the sop cooks, it marches through the bounding volume specified (by default from -1 to +1 in X, Y and Z), and creates geometry where the expression equals zero.
This may seem like a difficult way to define a sphere, but there's much potential beyond this simple example using the rich array of mathematical functions (see the Expressions section). A simple illustration is with the `noise()` function. Try inputing the following expression.
[![TouchGeometry20.gif](https://docs.derivative.ca/images/4/4e/TouchGeometry20.gif)](https://docs.derivative.ca/File:TouchGeometry20.gif)

## Info CHOP Channels
Extra Information for the Iso Surface SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
