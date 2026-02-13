---
url: https://docs.derivative.ca/Line_Metrics_POP
category: POPs
title: Line_Metrics_POP
---

# Line Metrics POP
## Summary

You can add metrics attributes to Line Strips. They can be created as point attribute or the vertex attributes.
This gives good information about the points and the context they are in. For each point you can get the direction to the next and previous points, or the distance back to the start of the line strip, or the line strip number it is in… things useful for Math POPs or Lookup POPs.
A convenience of the Line Metrics POP is to give nice values to awkward situations like co-incident points (two or more consecutive points in the same location), especially direction vectors. That’s what the Continuous Direction parameter does. It would work with Direction to Next, Direction to Previous, and do nice things to the Tangent vectors by keeping them in line.
[linemetricsPOP_Class](https://docs.derivative.ca/LinemetricsPOP_Class "LinemetricsPOP Class")

## Parameters - Neighbor Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -

- Displacement to Next `dispnext` - ⊞ - Whether to output an attribute with the displacement to the next vertex in the line strip.
  * Displacement to Next `dispnext` -
  * Displacement to Next Attrib Name `dispnextname` - Specifies the attribute scope used to output the Displacement to Next attribute

- Displacement to Previous `dispprev` - ⊞ - Whether to output an attribute with the displacement to the previous vertex in the line strip.
  * Displacement to Previous `dispprev` -
  * Displacement to Previous Attrib Name `dispprevname` - Specifies the attribute scope used to output the Displacement to Previous attribute

- Distance to Next `distnext` - ⊞ - Whether to output an attribute with the distance to the next vertex in the line strip.
  * Distance to Next `distnext` -
  * Distance to Next Attrib Name `distnextname` - Specifies the attribute scope used to output the Distance to Next attribute

- Distance to Previous `distprev` - ⊞ - Whether to output an attribute with the distance to the previous vertex in the line strip.
  * Distance to Previous `distprev` -
  * Distance to Previous Attrib Name `distprevname` - Specifies the attribute scope used to output the Distance to Previous attribute

- Direction to Next `dirnext` - ⊞ - Whether to output an attribute with the direction to the next vertex in the line strip.
  * Direction to Next `dirnext` -
  * Direction to Next Attrib Name `dirnextname` - Specifies the attribute scope used to output the Direction to Next attribute

- Direction to Previous `dirprev` - ⊞ - Whether to output an attribute with the direction to the previous vertex in the line strip.
  * Direction to Previous `dirprev` -
  * Direction to Previous Attrib Name `dirprevname` - Specifies the attribute scope used to output the Direction to Previous attribute

- Tangent `tangent` - ⊞ - Output a tangent attribute for each point.
  * Tangent `tangent` -
  * Tangent Attrib Name `tangentname` - Attribute scope for the tangent.

- Curvature `curvature` - ⊞ - Whether to output an attribute containing the curvature.
  * Curvature `curvature` -
  * Curvature Attrib Name `curvaturename` - Sets the attribute scope when computing curvature

- Angle per Distance `angleperdist` - ⊞ - Whether to output Angle per Distance.
  * Angle per Distance `angleperdist` -
  * Angle per Distance Attrib Name `angleperdistname` - Attribute Name for Angle per Distance.

- Continuous Direction `continuousdir` - Enable returning continuous directions for co-incident points
- Max Neighbors `maxneighbors` - When computing Direction vector, how far to look when points are in same position as next or previous points.

## Parameters - Line Strip Page
- Distance from Start `diststart` - ⊞ - Whether to output an attribute with the distance from the start of the line strip.
  * Distance from Start `diststart` -
  * Distance from Start Attrib Name `diststartname` - Specifies the attribute scope used to output the Distance from Start attribute

- Distance from End `distend` - ⊞ - Whether to output an attribute with the distance from the end of the line strip.
  * Distance from End `distend` -
  * Distance from End Attrib Name `distendname` - Specifies the attribute scope used to output the Distance from End attribute

- Distance from Start Normalized `diststartnorm` - ⊞ - Whether to output an attribute with the normalized distance from the start of the line strip.
  * Distance from Start Normalized `diststartnorm` -
  * Distance from Start Normalized Attrib Name `diststartnormname` - Specifies the attribute scope used to output the Distance from Start Normalized attribute

- Distance from End Normalized `distendnorm` - ⊞ - Whether to output an attribute with the normalized distance from the end of the line strip.
  * Distance from End Normalized `distendnorm` -
  * Distance from End Normalized Attrib Name `distendnormname` - Specifies the attribute scope used to output the Distance from End Normalized attribute

- Line Strip Length `primlen` - ⊞ - Enable addition of line strip length attribute.
  * Line Strip Length `primlen` -
  * Line Strip Length Attrib Name `primlenname` - Name of the attribute for the line strip length.

- Length Attrib Primitive Attribute `primlenprim` - When on, the attribute created for the length of the line strip is a primitive attribute.

## Parameters - Index Page
- Vert Index in Line Strip `pointindex` - ⊞ - Output the vertex index for each point, assuming unique.
  * Vert Index in Line Strip `pointindex` -
  * Vert Index Attrib Name `pointindexname` - The name of the vertex index attribute.

- Number of Verts in Line Strip `numverts` - ⊞ - Outputs attribute for number of vertices in current point's like strip.
  * Number of Verts in Line Strip `numverts` -
  * Number of Verts Attrib Name `numvertsname` - Name for the Number of Verts in Line Strip attribute.

- Vert Index in Line Strip Normalized `vertindexnorm` - ⊞ - Output the vertex index normalized to 0-1 for each point, assuming unique.
  * Vert Index in Line Strip Normalized `vertindexnorm` -
  * Vert Index Normalized Attrib Name `vertindexnormname` - The name of the vertex index normalized attribute.

- Line Strip Index `linestripindex` - ⊞ - Enable addition of line strip index attribute.
  * Line Strip Index `linestripindex` -
  * Line Strip Index Attrib Name `linestripindexname` - Attribute name for the index of the line strip.

- Line Strip Index Normalized `lsindexnorm` - ⊞ - Enable addition of normalized line strip index attribute.
  * Line Strip Index Normalized `lsindexnorm` -
  * Line Strip Index Normalized Attrib Name `lsindexnormname` - Attribute name for the normalized index of the line strip.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Line Metrics POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
