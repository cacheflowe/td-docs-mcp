---
url: https://docs.derivative.ca/CHOP_to_SOP
category: SOPs
title: CHOP_to_SOP
---

# CHOP to SOP
## Summary

The CHOP to SOP takes CHOP channels and generates 3D polygons in a SOP. It reads sample data from a [CHOP](https://docs.derivative.ca/CHOP "CHOP") and converts it into point positions and point attributes. This makes it complementary to the [SOP to CHOP](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP"). The Channels created by the [SOP to CHOP](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP") can be modified and then re-inserted into the SOP network via a CHOP to SOP.
By default, the SOP is a line from (`-1 0 0`) to (`1 0 0`) containing one point for every sample in the CHOP.
It matches the input channels to the Channel Scope (`tx ty tz`) where possible. If `tx` or `ty` or `tz` don’t match anything, it just uses the value from the default line, and it only shows a Warning.
The simplest thing to do is to send it a channel named `ty`, which will make a 3D curve that looks like the CHOP curve.
This does what a [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP") with a `op('wave1')['chan1'].eval(0)` function can do, but is much faster.
By using point groups from the incoming SOP, the channels can be inserted only into the group's points.
The CHOP to SOP also supports custom attributes. If the user maps a channel to an attribute that is not found, that attribute is added to the points. Currently, all custom attributes are floats and of size = 1.
In its default state it will attempt to replace the point positions (`P(0) P(1) P(2)`) with the channels named `tx ty` and `tz`.
The channel and attribute scope are first expanded into individual names and matched on a 1 to 1 basis. If you are filling P it doesn't matter if you specify `t[xyz]` or `tx ty tz`, both will replace `P(0) P(1) P(2)`, which can be collapsed to `P`.
For example: Add custom attributes "Scale", "Twist" or "Roll" to the backbone's points with a CHOP to SOP.
If you connect a SOP to its input, it will use the SOP as a starting geometry versus the default line.
[choptoSOP_Class](https://docs.derivative.ca/ChoptoSOP_Class "ChoptoSOP Class")

## Parameters - Page
- Group `group` - Modify only the points within this point group. If blank, all points are modified. Accepts patterns, as described in: [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- CHOP `chop` - Specifies which CHOP Network / CHOP contains the sample data to fetch.
- Start Position `startpos` - ⊞ - Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes.
  * X `startposx` -
  * Y `startposy` -
  * Z `startposz` -

- End Position `endpos` - ⊞ - Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes.
  * X `endposx` -
  * Y `endposy` -
  * Z `endposz` -

- Channel Scope `chanscope` - The names to use to modify the attributes.
- Attribute Scope `attscope` - A string list of attributes to modify in the SOP. List of Common Attributes:
  * `**P**`- Point position (X, Y, Z) - 3 values
  * `**Pw**`- Point weight - 1 value
  * `**Cd**`- Point color (red, green, blue, alpha) - 4 values
  * `**N**`- Point normal (X, Y, Z) - 3 values
  * `**uv**`- Point texture coordinates (U, V, W) - 3 values

See [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)") for a complete listing of attributes.
- Organize by Attribute `organize` - Instead of using the point index, use the value of this attribute as the index to use when looking up into the CHOP.
- Mapping `mapping` - ⊞ - Determines how the CHOP samples are mapped to the geometry points.
  * One Sample to Each Point `onetoone` - The samples are simply mapped 1-to-1, each sample is mapped to the next point in order.
  * Resample CHOP to Fit SOP `scale` - If there are more or less CHOP samples than points in the geometry, then the CHOP channels are resampled to interpolate values for all the geometry points.

- Compute Normals `compnml` - Creates normals on the geometry.
- Compute Tangents `comptang` - Creates tangents on the geometry.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the CHOP to SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
