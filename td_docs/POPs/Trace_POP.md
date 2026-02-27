---
url: https://docs.derivative.ca/Experimental:Trace_POP
category: POPs
title: Trace_POP
---

#  Trace POP
## Summary

[tracePOP_Class](https://docs.derivative.ca/TracePOP_Class "TracePOP Class")

The Trace POP reads a TOP image and traces it, generating line strips around areas exceeding a certain brightness threshold. You can control the threshold using the Threshold parameter, and compare it with the pixel value determined by the Channel menu, by default the brightness.
The line strips can be triangulated into triangular surfaces, ore left in its basic (fastest but least useful) form as 2-point lines.
The resolution of the resulting line strips or triangle meshes can be reduced using the Resolution Multiplier parameter.
You can smooth the line strips using the Smooth Edge Distance parameter which is similar to the snoothing in the [Line Smooth POP](https://docs.derivative.ca/Line_Smooth_POP "Line Smooth POP").
The Extend menu determines is the line strips continue around the border or are separates as open line strips.
The Winding will make outer line strips that are counter-clockwise, and line strips enclosed in them to be clockwise.
The output is -.5 to .5 in X (`P(0)`) but it can be re-ranged with the ReRange P parameters.
You may need to adjust the Max Num Line Strips parameter or the Man Num Verts parameter (since these numbers need to be pre-determined for the GPU to avoid overflows).
See also [Polygonize POP](https://docs.derivative.ca/Polygonize_POP "Polygonize POP"), [Triangulate POP](https://docs.derivative.ca/Triangulate_POP "Triangulate POP"), [Extrude POP](https://docs.derivative.ca/Extrude_POP "Extrude POP")
## Parameters - Trace Page
- Input Attribute Scope `inputattrscope` -
- Use Position Attribute `posattrib` -
- TOP `top` -
- Channel `channel` - ⊞ -
  * Luminance `luminance` -

  * Red `red` -

  * Green `green` -

  * Blue `blue` -

  * Alpha `alpha` -

  * RGB Average `rgbaverage` -

  * RGBA Average `average` -

  * RGB Maximum `rgbmax` -

  * RGBA Maximum `max` -

- Resolution Multiplier `resmult` -
- Inside `inside` - ⊞ -
  * Below/Equal to Threshold `below` -

  * Above Threshold `above` -

- Threshold `threshold` -
- Extend `extend` - ⊞ -
  * Hold `hold` -

  * Zero `zero` -

- Output `twodimensions` - ⊞ -
  * Contour (Lines) `contour` -

  * Contour (Line Strips) `contourls` -

  * Surface (Triangles) `surface` -

- Unique Points `uniquepoints` -
- Winding `winding` - ⊞ -
  * Natural `natural` -

  * Counter ClockWise `ccw` -

- Smoooth Edge Distance `smooth` - ⊞ -
  * Smoooth Edge Distance `smooth` -

  * Smooth Edge Distance `filterdist` -

- ReRange P `rerangep` -
- Map to Low `tolow` - ⊞ -
  * Map to Low `tolow0` -

  * Map to Low `tolow1` -

- Map to High `tohigh` - ⊞ -
  * Map to High `tohigh0` -

  * Map to High `tohigh1` -

- Normal `normal` - ⊞ -
  * None `none` -

  * Point `point` -

  * Primitive `prim` -

- Texture Coordinates `texture` -
- Fraction of Max Allocation `allocfract` -
- Max Num Line Strips `setmaxnumls` - ⊞ -
  * Max Num Line Strips `setmaxnumls` -

  * Max Num Line Strips `maxnumls` -

- Max Num Verts per Line Strip `setmaxnumvertsperls` - ⊞ -
  * Max Num Verts per Line Strip `setmaxnumvertsperls` -

  * Max Num Verts per Line Strip `maxnumvertsperls` -

- Copy Topology Info Back to CPU `cpureadback` -


## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.


## Operator Inputs
  * Input 0:  -



## Info CHOP Channels
Extra Information for the Trace POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
