---
url: https://docs.derivative.ca/Histogram_POP
category: POPs
title: Histogram_POP
---

# Histogram POP
## Summary

The Histogram POP takes an attribute from its input, creates an output with one attribute (Count attribute) and a specified number of points (Number of Bins parameter), and for each input point, adds 1 to one of the bins. This gives a "frequency distribution".
It divides the entire range of values (Input Range parameter) into a series of intervals, and then counts how many values fall into each interval (bin).
Values of the input that are outside the lower and upper range of the bins can be ignored, clamped to the min or max, or added to two extra bins that count values out of range.
It can also output the interval start values into a separate attribute `BinValue`.
By it nature, it works on a single component of a vector attribute, such as `P(1)`. You may want to first convert a vector to a float using length() in an Math POP.
You can histogram point attributes or primitive attributes.
The result is often viewed with a [POP to CHOP](https://docs.derivative.ca/POP_to_CHOP "POP to CHOP"), or with the popViewer component which can show an attribute as a graph.
The Histogram POP takes all the values of a single component attribute, for example `P(1)` and for each input point, adds 1 to a bin of the output. The output has N bins which is actually N points with one attribute `Count`. The user specifies the value that the first bin represents, and the value that the last bin represents, and using N, the Histogram POP determines the low and high values represented by each bin. Count starts at 0 for all bins, and the appropriate bin gets incremented by 1 for each input points.
See also: [Accumulate POP](https://docs.derivative.ca/Accumulate_POP "Accumulate POP"), [Analyze POP](https://docs.derivative.ca/Analyze_POP "Analyze POP"), [ReRange POP](https://docs.derivative.ca/ReRange_POP "ReRange POP")
[histogramPOP_Class](https://docs.derivative.ca/HistogramPOP_Class "HistogramPOP Class")

## Parameters - Histogram Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Input Attribute Scope `inputattrscope` - Scalar input attribute or vector attribute component.
- Use Input Range `useinputrange` - Specify teh range of the input attribute values. Default range is 0 to the number of bins.
- Input Range `inputrange` - ⊞ - When used, the input range gets divided in to Number of Bins.
  * Input Range `inputrange1` -
  * Input Range `inputrange2` -
  * Input Range `inputrangemin` -
  * Input Range `inputrangemax` -

- Output Bin Value `outputbinval` - Whether to output a separate attribute with the bin values, when using an input range.
- Quantize `quantize` - ⊞ - Convert values into a finite set of discrete levels.
  * Floor `floor` -
  * Round `round` -
  * Ceiling `ceiling` -

- Outside Range `outsiderange` - ⊞ - Determines the behavior outside the input range.
  * Clamp `clamp` -
  * Discard `discard` -
  * Extra Out-of-Range Bins `extrabins` -

- Number of Bins `numbins` - The number of bins to sort the attribute values in.
- Count Attribute `countattr` - Sets the attribute scope when outputting the count attribute
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Histogram POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
