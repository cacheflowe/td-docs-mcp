---
url: https://docs.derivative.ca/Sprinkle_POP
category: POPs
title: Sprinkle_POP
---

# Sprinkle POP
## Summary

The Sprinkle POP creates points either on the surface of the input POP or within the volume of the input POP.
You create points based on the Method menu. The Per Primitive method creates points on the surface of primitives (triangles or quads). It keeps the distribution of points approximately constant per primitive no matter their size. (There is currently no method to create points on a surface that is constant per-area). The Volume method creates points randomly within a closed volume. (You will get some approximations if the volume is not closed.)
The Number of Points parameter is an approximate upper-limit number, the Volume (Deterministic) method produces a more accurate number of points (TBD).
By default, for every point it creates, it also creates a Point Primitive. The latter is useful if you are rendering the points directly, but may not be needed for other purposes (like you are copying to each point). Turn off Create Point Primitives if you don't need primitives, you just want a points list, and you wish to save memory.
It can leverage [Hardware Ray Tracing](https://docs.derivative.ca/Hardware_Ray_Tracing "Hardware Ray Tracing") in volume mode (point generation only, not for input attributes interpolation).
See also [Point Generator POP](https://docs.derivative.ca/Point_Generator_POP "Point Generator POP"), [Random POP](https://docs.derivative.ca/Random_POP "Random POP")
[sprinklePOP_Class](https://docs.derivative.ca/SprinklePOP_Class "SprinklePOP Class")

## Parameters - Sprinkle Page
- Create Point Primitives `createpointprim` - Enable creating point primitives
- Seed `seed` - Numerical value that initializes the randomization.
- Method `method` - ⊞ - How to sprinkle points - on peimitives like triangles/quads, or inside closed volumes formed by primitives like triangles/quads.
  * Per Primitive `perprim` -
  * Volume `volume` -
  * Volume (Deterministic) `volumedeterministic` -
  * Volume (Non-Deterministic) `volnondeterministic` -
  * Volume `vol` -

- Number of Points `numpoints` - Sets the number of points. In the case of volume sprinkle, this is the max number of points, it might require a higher number of attempts per point to reach it.
- Attempts per Point `attemptsperpoint` - For volume sprinkle, the number of attempts to try to get a point inside the mesh.
- Ray Direction Mode `raydirmode` - ⊞ - To determine if point is inside or outside, cast rays from in random direction or in constant direction.
  * Constant `constant` -
  * Random `random` -

- Ray Direction `raydir` - ⊞ - Constant direction to cast rays to determine if candidate point is inside or outside.
  * Ray Direction `raydirx` -
  * Ray Direction `raydiry` -
  * Ray Direction `raydirz` -

- Hardware Ray Tracing `hwraytracing` - ⊞ - Selects mode for Hardware Ray Tracing if supported
  * Off `off` -
  * Fast Build (Dynamic Geometry) `fastbuild` -
  * Fast Trace (Static Geometry) `fasttrace` -

- Point Attribute Scope `pointattrscope` - ⊞ - The Point attribute scope to blend.
  * * `*` -

- Primitive Attribute Scope `primattrscope` - ⊞ - The Primitive attribute scope to blend.
  * * `*` -

- Vertex Attribute Scope `vertattribscope` - ⊞ - Vertex attributes to sample when sprinkling.
  * * `*` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Sprinkle POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
