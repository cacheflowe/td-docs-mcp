---
url: https://docs.derivative.ca/Sort_POP
category: POPs
title: Sort_POP
---

# Sort POP
## Summary

The Sort POP sorts the point list and/or the primitive list based on the position `P` or any attribute component. When sorting by `P` it can sort the points relative to a vector, or proximity to a point, or relative to a Geometry COMP's Z axis.
The Sort POP can also randomize the point order, or shift the point order (circularly in the point list, like first point becomes the second point and the last point becomes the first).
It can do the same operations to primitives.
It implements <https://gpuopen.com/fidelityfx-parallel-sort/>
[sortPOP_Class](https://docs.derivative.ca/SortPOP_Class "SortPOP Class")

## Parameters - Point Page
- Point Method `ptmethod` - ⊞ - Point sorting criteria.
  * No Change `none` -
  * By Attribute `byattrib` -
  * Random `seed` -
  * Proximity to Point `prox` -
  * Along Vector `vector` -
  * Relative to Object Z-axis `object` -

- Attribute `pointattr` - Attribute to use for sorting.
- Attrib is UInt `pointuint` - ⊞ - When sorting by attribute, allows to specify whether the attribute is an unsigned integer and what the max value is. Smaller max UInt require fewer passes to sort.
  * Not UInt Attrib `notuint` -
  * 4 bits UInt (max 16) `uint4` -
  * 8 bits UInt (max 256) `uint8` -
  * 12 bits UInt (max 4096) `uint12` -
  * 16 bits UInt (max 65,536) `uint16` -
  * 20 bits UInt (max 1 M) `uint20` -
  * 24 bits UInt (max 16 M) `uint24` -
  * 28 bits UInt (max 268 M) `uint28` -
  * 32 bits UInt (max 4 B) `uint32` -

- Seed `pointseed` - Seed for random number generator for randomly-ordered points.
- Point `pointprox` - ⊞ - Proximity Point.
  * Point `pointproxx` -
  * Point `pointproxy` -
  * Point `pointproxz` -

- Vector `pointdir` - ⊞ - When sorting points Along Vector, it takes the point position, finds the the closest point on a line through 0,0,0 in the direction of the vector, and then sorts along that line.
  * Vector `pointdirx` -
  * Vector `pointdiry` -
  * Vector `pointdirz` -

- Object `pointobj` - 3D Object to use when sorting points relative to Object Z-axis.
- Reverse `pointrev` - After sorting points, reverse their order.
- Shift `pointshift` - Enables offsetting on sorted points.
- Offset `pointoffset` - Shifts the point order by this offset.

## Parameters - Primitive Page
- Primitive Method `primmethod` - ⊞ - Primitive sorting criteria.
  * No Change `none` -
  * By Point Attribute `byptattrib` -
  * By Primitive Attribute `byprimattrib` -
  * Random `seed` -
  * Proximity to Point `prox` -
  * Along Vector `vector` -
  * Relative to Object Z-axis `object` -

- Attribute `primattr` - Attribute to use for sorting.
- Attrib is UInt `primuint` - ⊞ - When sorting by attribute, allows to specify whether the attribute is an unsigned integer and what the max value is. Smaller max UInt require fewer passes to sort.
  * Not UInt Attrib `notuint` -
  * 4 bits UInt (max 16) `uint4` -
  * 8 bits UInt (max 256) `uint8` -
  * 12 bits UInt (max 4096) `uint12` -
  * 16 bits UInt (max 65,536) `uint16` -
  * 20 bits UInt (max 1 M) `uint20` -
  * 24 bits UInt (max 16 M) `uint24` -
  * 28 bits UInt (max 268 M) `uint28` -
  * 32 bits UInt (max 4 B) `uint32` -

- Seed `primseed` - Seed for primitive ranomizer.
- Point `primprox` - ⊞ - Position when sorting by proximity to point.
  * Point `primproxx` -
  * Point `primproxy` -
  * Point `primproxz` -

- Vector `primdir` - ⊞ - When sorting primitives Along Vector, it takes the center of the primitive, finds the closest point on a line through 0,0,0 in the direction of the vector, and then sorts along that line.
  * Vector `primdirx` -
  * Vector `primdiry` -
  * Vector `primdirz` -

- Object `primobj` - 3D Object to use when sorting primitives relative to Object Z-axis.
- Reverse `primrev` - Reverse the order of primitives.
- Shift `primshift` - Enables offsetting on sorted primitives.
- Offset `primoffset` - Shifts the primitive order by this offset.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Sort POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
