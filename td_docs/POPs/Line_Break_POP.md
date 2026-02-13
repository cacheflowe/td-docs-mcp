---
url: https://docs.derivative.ca/Line_Break_POP
category: POPs
title: Line_Break_POP
---

# Line Break POP
## Summary

The Line Break POP creates new line strips from the points and line strips of its input.
It can create a set of line strips using an attribute, default named `LineBreak`, where it steps through all the points of the input and a new line strip is started if the `LineBreak` attribute is 1. If `LineBreak` is 0, it continues the line to include current point.
Alternately, It can use a point attribute `LineStripIndex` (same attribute name as Line Metrics creates) to make separate line strips.
It can also split a line strip based on a point being farther that a specified distance from the previous point.
It can split a line strip every N points.
It can simply create one line strip from its input points.
See also [Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP"), [Convert POP](https://docs.derivative.ca/Convert_POP "Convert POP")
[linebreakPOP_Class](https://docs.derivative.ca/LinebreakPOP_Class "LinebreakPOP Class")

## Parameters - Line Break Page
- Mode `connecmode` - ⊞ - When on, use the input line strips' connectivity otherwise use only the input points order.
  * No Connectivity `noconnec` -
  * One Line Strip (point order) `onelinestrip` -
  * Input Line Strips `inputlinestrips` -

- Line Break Attribute `uselinebreak` - ⊞ - When on, the attribute will contain 1 for line breaks, 0 for non-line breaks.
  * Line Break Attribute `uselinebreak` -
  * Line Break Attribute `linebreakname` - Name of the attribute to use to create line breaks.

- Line Strip Index Attribute `uselinestripindex` - ⊞ - When on, the attribute will contain integers where points with same integer are part of one line strip..
  * Line Strip Index Attribute `uselinestripindex` -
  * Line Strip Index Attribute `linestripindexname` - Line strip index attribute name.

- Use Input Line Breaks `useinputlinebreaks` - Use a line break attribute of teh input to determine breaks between line strips.
- Every N Points `everyn` - Enable addition on line breaks every N points
- N `n` - N value when Every N Points is enabled.
- By Distance Threshold `bydistancethreshold` - Whether to create line breaks using a distance threshold between two points.
- Distance Threshold `distancethreshold` - Determines the minimum distance between points to add new line breaks
- Distance Threshold Attribute `distancethresholdattr` - Determines the scope of the attribute used to compute the distances between points
- Output Line Break Attribute `outputlinebreakattr` - Whether to output a LineBreak attribute.
- Output Lines `outputlines` - Whether to output Line Strip or Lines primitive (determined by the Line Type menu)
- Line Type `linetype` - ⊞ - Specifies whether lines should be made of line strip primitives or lines primitives.
  * Line Strip `linestrip` -
  * Lines `lines` -

- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Line Break POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
