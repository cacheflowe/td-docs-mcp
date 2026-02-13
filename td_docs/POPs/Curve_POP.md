---
url: https://docs.derivative.ca/Curve_POP
category: POPs
title: Curve_POP
---

# Curve POP
## Summary

The Curve POP is used to generate a curve in XY (Z=0) that can be used as a lookup curve for a [Lookup Attribute POP](https://docs.derivative.ca/Lookup_Attribute_POP "Lookup Attribute POP") or elsewhere. It is a "function" in that the `P(0)` X-value steps forward uniformly from point to point, while the `P(1)` Y-value takes on different interpolated shapes. The curve it generates is also in an attribute `Curve`, which you can use instead of `P(1)` for clarity.
Like the [S Curve CHOP](https://docs.derivative.ca/S_Curve_CHOP "S Curve CHOP"), it defaults to an ease-in ease-out curve, but the Curve POP lets you add multiple segments (sequential blocks) that enable a greater range of curves. The curve can be made of several segments defined by [Sequential Blocks](https://docs.derivative.ca/index.php?title=Sequential_Blocks&action=edit&redlink=1 "Sequential Blocks \(page does not exist\)") of parameters, each with its own start and end values and Curve Type.
The Curve Type includes Constant, Linear, the Eases and Bezier.
The Alpha and Beta values affect the curve, where Alpha makes it more- or less-sloped, and Beta makes it more biased to the start or end of the segment. When Bezier is selected, Slope In and Slope Out affect the slopes at the end-points of the segment.
More generally, we treat the 2 axes as U and V. The curves can output as points-only, a linestrip, or as an RGBA color curves.
Because the U values can start and end at any value, you can normalize the curve so the U values (`P(0)`) are between 0 and 1.
The curve can be extended to double length and made symmetric using the Symmetric toggle.
The Lookup page lets you apply the curve as a lookup without first converting anything to points. This preerves maximum accuracy, and avoids interpolation problems when a lookup curve sharply steps from one value to another as may occur between two segments. In this case you attach an input POP where you want to modify one or more attributes with the curve. In this mode it behaves similar to the [Lookup Attribute POP](https://docs.derivative.ca/Lookup_Attribute_POP "Lookup Attribute POP").
Tip: If you want specific points to exactly hit your U keyframe values, make sure your (Number of Points - 1) is divisible evenly by your U values.
See also [S Curve CHOP](https://docs.derivative.ca/S_Curve_CHOP "S Curve CHOP"), [Line POP](https://docs.derivative.ca/Line_POP "Line POP"), [Lookup Attribute POP](https://docs.derivative.ca/Lookup_Attribute_POP "Lookup Attribute POP"), [Pattern POP](https://docs.derivative.ca/Pattern_POP "Pattern POP")
[curvePOP_Class](https://docs.derivative.ca/CurvePOP_Class "CurvePOP Class")

## Parameters - Curve Page
- Total Length `totallength` - Determines the number of points.
- Output Curve `outputcurve` - ⊞ - Selects the type of primitive to output.
  * Points `points` -
  * Line Strips `linestrip` -
  * Color Strip `colorstrip` -

- Normalize U `normalizeu` - Normalize all the U values so their range is 0 to 1.
- Symmetric `symmetric` - Enable mirroring the curve segments.
- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Start U `startu` - Start U position for the first segment.
- Segment `seg` - Start of Sequential Parameter Blocks for creating curve segments.
- Curve Type `seg0type` - ⊞ - The interponation type of the curve between the start and end of the segment.
  * Constant `constant` -
  * Linear `linear` -
  * Ease In `easein` -
  * Ease Out `easeout` -
  * Ease In Ease Out `easeinout` -
  * Bezier `bezier` -

- U `seg0u` - Sets the segments end U.
- Specify Start Value `seg0specstartval` - When set, the segment has a start value, otherwise it is a continuation of the previous segment.
- Start Value `seg0startval` - When set, the segment has a start value, otherwise it is a continuation of the previous segment.
- End Value `seg0endval` - The value at the end of a curve segment.
- Alpha `seg0alpha` - One paramter that affects the curve, usually a form of steepness.
- Beta `seg0beta` - A second paramter that affects the curve, usually a form of bias to the start or end of a curve segment.
- Slope in `seg0slopein` - Bezier slope factor for the incoming curve segment.
- Slope Out `seg0slopeout` - Bezier slope factor for the outgoing curve segment.

## Parameters - Lookup Page
- Apply Lookup `applylookup` - The Lookup page lets you apply the curve as a lookup without first converting anything to points.
- Lookup Index Attribute `lookupindexattr` - Attribute to use as the index for the lookup.
- From Low High `fromlow` - ⊞ - Reranges the attribute value.
  * From Low High `fromlow` -
  * From High `fromhigh` - Reranges the index attribute value.

- To Low High `tolow` - ⊞ - Reranges the input lookup attribute value.
  * To Low High `tolow` -
  * To High `tohigh` - Sets high value on the output range.

- Extend Left and Right `extendleft` - ⊞ - What happens when the lookup samples outside of the range.
  * Hold `hold` -
  * Slope `slope` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Extend Left and Right `extendleft` -
  * Extend Right `extendright` - What happens when the lookup samples the curves outside its U range.

- Lookup `lookup` - Start of Sequential Parameter Blocks of lookups.
- Multiply `lookup0multiply` - A multiplier that is applied to the lookup result.
- Add `lookup0add` - A value you add to the result of a lookup.
- Combine Operation `lookup0combineop` - ⊞ - After a value is retrieved doing the lookup, it can be added or multiplied with an attribute.
  * Set `set` -
  * Add `add` -
  * Multiply `mult` -
  * Minimum `min` -
  * Maximum `max` -

- Output Attribute Scope `lookup0outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `lookup0overrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `lookup0attrtype` - ⊞ - The lookup attribute type.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * dir `dir` -
  * dbl dir `ddir` -

- Components `lookup0attrnumcomps` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `lookup0attrdefaultval` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `lookup0attrdefaultval0` -
  * Default Value `lookup0attrdefaultval1` -
  * Default Value `lookup0attrdefaultval2` -
  * Default Value `lookup0attrdefaultval3` -

- Extend Right `extendright` - ⊞ -
  * Hold `hold` -
  * Slope `slope` -
  * Cycle `cycle` -
  * Mirror `mirror` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Curve POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
