---
url: https://docs.derivative.ca/Extrude_POP
category: POPs
title: Extrude_POP
---

# Extrude POP
## Summary

The Extrude POP is a simple operator that gives apparent "thickness" to triangles or quads. It copies the triangle or quad at a specifiable separation (Distance), optionally shrinks it to give a taper (Inset), and adds quads for the sides. You must pass it to a [Normal POP](https://docs.derivative.ca/Normal_POP "Normal POP") to render it with faceted shading.
[extrudePOP_Class](https://docs.derivative.ca/ExtrudePOP_Class "ExtrudePOP Class")

## Parameters - Extrude Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Distance `distance` - Sets the distance to extrude
- Use Distance Attribute `usedistanceattr` - Enables extrusion distance to be driven by an attribute.
- Distance Attribute `distanceattr` - The attribute to use to set the extrude distance.
- Inset `inset` - Applies a scaling factor to extruded geometry.
- Keep Faces Connected `keepconnected` - When on, faces are extruded as a group instead of individually. Useful in particular when extruding an input group.
- Max Primitives per Point `maxprimsperpoint` - Used to allocate temporary storage when Keep Faces Connected is on, it should be set to the maximum number a primitives a point can be a part of in the input geometry.
- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Extrude POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
