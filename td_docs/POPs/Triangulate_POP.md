---
url: https://docs.derivative.ca/Experimental:Triangulate_POP
category: POPs
title: Triangulate_POP
---

#  Triangulate POP

## Summary

[triangulatePOP_Class](https://docs.derivative.ca/TriangulatePOP_Class "TriangulatePOP Class")

The Triangulate POP converts each closed line strip into a set of triangles that fill the interior of the line strip.

The default assumes that all line strips are convex. Set Mode to Convex and Concave if you are not certain all line strips are convex.

Open line strips and other primitive types are passed through unmodified. It supports inputs with a combination of primitive types and open and close line strips, and everything that is not a closed line strip passes through. Quads pass through.

The Modes menu: Convex only - it runs highly parallel (fast). Convex and Concave - it can get very slow for longer line strips. Max Verts per Line Strip need to be set accordingly, Max iterations can be set to limit number of iterations (leaving some closed line strips partially triangulated)

See also [Polygonize POP](https://docs.derivative.ca/Polygonize_POP "Polygonize POP"), [Trace POP](https://docs.derivative.ca/Trace_POP "Trace POP")

## Parameters - Triangulate Page

- Mode `mode` - ⊞ -
  * Convex Only `convex` -
  * Convex and Concave (Slower) `concave` -

- Max Verts per Input Line Strip `lsmaxverts` -
- Max Iterations `setmaxiter` - ⊞ -
  * Max Iterations `setmaxiter` -
  * Max Iterations `maxiter` -

## Parameters - Common Page

- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs

  * Input 0:  -

## Info CHOP Channels

Extra Information for the Triangulate POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").

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
