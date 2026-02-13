---
url: https://docs.derivative.ca/Ray_POP
category: POPs
title: Ray_POP
---

# Ray POP
## Summary

The Ray POP casts a ray from each points of the input, in the direction defined by the Ray Attribute, and outputs new attributes that report what each ray hits.
The second input is the set of triangles and quads that the rays are tested against. The Ray POP can count the number of primitives it hit as it transmits through all primitive in its line, and the distance to the closest primitive.
It can output properties of the primitive it hit - its primitive index, the barymetric position on the primitive it hit, and the values of any attributes on the primitive it hit.
It can also output information about rays that are reflected. Assuming the Collision Geometry is a closed surface, the Ray POP can report whether it is located inside or outside the volume.
It can be put into a mode where it outputs line strips representing the rays that it casts, intersects and reflects.
By default, the Ray POP projects the points on the collision mesh, Scale is a 0 to 1 multiplier between original position and projected position, Lift is also a control to move the point along the ray but in absolute units (to move points inside or outside a bit from the collision surface.
It can leverage [Hardware Ray Tracing](https://docs.derivative.ca/Hardware_Ray_Tracing "Hardware Ray Tracing").
See also [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP") (has ray functions)
[rayPOP_Class](https://docs.derivative.ca/RayPOP_Class "RayPOP Class")

## Parameters - Ray Page
- Ray Attribute `rayattrib` - Ray direction attribute.
- Negate Ray `negateray` - Negates the direction of the ray.
- Number of Bounces `numbounces` - The number of bounces for the rays.
- Connect Points `connectpoints` - When doing multiple bounces, for each input point whether to connect the intersections as a line strip.
- Limit Ray Length `limitraylength` - ⊞ - The ray length will be limited.
  * Limit Ray Length `limitraylength` -
  * Ray Distance Max Attrib `raydistancemaxattr` - Help Not Available.

- Trim Ray `trimray` - ⊞ - Option to trim ray line strip.
  * Trim Ray `trimray` -
  * Trim Distance Attrib `trimdistanceattr` - Specifies the attribute to use to trim rays.

- Hardware Ray Tracing `hwraytracing` - ⊞ - Selects mode for Hardware Ray Tracing if supported
  * Off `off` -
  * Fast Build (Dynamic Geometry) `fastbuild` -
  * Fast Trace (Static Geometry) `fasttrace` -

- Opaque Geometry `opaque` - When using hardware raytracing, specify whether the collision geometry is treated as opaque (only the closest or the first hit is returned) or not.
- Any Hit `anyhit` - Whether to return the first hit, not guaranteed to be the closest or the farthest one.
- Hit Normal `hitnormal` - ⊞ - Generate normal attribute at hit locations.
  * Hit Normal `hitnormal` -
  * Hit Normal Name `hitnormalname` - Name of the normal attribute for the ray hit location on the surface.

- Reflected Ray `doreflectedray` - ⊞ - Whether to output an attribute containing the reflected ray direction.
  * Reflected Ray `doreflectedray` -
  * Reflected Ray Name `reflectedrayname` - Reflected ray attribute name.

- Point Intersection Distance `dist` - ⊞ - Whether to output an attribute with the distance between the original point and the intersection with the collision geometry.
  * Point Intersection Distance `dist` -
  * Point Intersection Distance Name `distname` - Intersection distance output attribute name.

- Farthest Hit `farhit` - ⊞ - Whether to output an attribute with the farthest hit position.
  * Farthest Hit `farhit` -
  * Farthest Hit Name `farhitname` - Determines the scope of the attribute used to output the farthest hit position.

- Number of Hits `numhits` - ⊞ - The Number of hits for rays passing through all the primitives in the ray direction.
  * Number of Hits `numhits` -
  * Number of Hits Name `numhitsname` - The name of the Number of Hits attribute.

- Inside `inside` - ⊞ - Outputs an attribute containing 0 for rays stating outside a volume (a closed polygon surface), or 1 for rays originating inside a volume.
  * Inside `inside` -
  * Inside Name `insidename` - Inside attribute name. Value is 0 if inside closed mesh, 1 if outside.

- Hit Primitive Index `hitprimindex` - ⊞ - Generate primitive index at hit locations.
  * Hit Primitive Index `hitprimindex` -
  * Hit Primitive Index Name `hitprimindexname` - Name of the primitive index attribute.

- Barycentric Coordinates `barycoords` - ⊞ - Whether to output an attribute with the barycentric coordinates of the intersection point.
  * Barycentric Coordinates `barycoords` -
  * Barycentric Coordinates Name `barycoordsname` - Barycentric coordinates name.

- Scale `scale` - Intersection scaling factor.
- Lift `lift` - This value offsets the point from the collision geometry in the direction of its normal.
- Hit Point Attr Scope `hitpointattrscope` - ⊞ - Point attributes to sample on the collision geometry.
  * * `*` -

- Hit Primitive Attr Scope `hitprimattrscope` - ⊞ - Primitive attributes to sample on the collision geometry.
  * * `*` -

- Hit Vertex Attr Scope `hitvertattrscope` - ⊞ - Vertex attributes to sample on the collision geometry.
  * * `*` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Ray POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
