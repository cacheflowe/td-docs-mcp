---
url: https://docs.derivative.ca/Lookup_Attribute_POP
category: POPs
title: Lookup_Attribute_POP
---

# Lookup Attribute POP
## Summary

The Lookup Attribute POP in its simplest form takes an attribute of the first input (the Lookup Index Attribute(s)) with values in the 0-1 range, and for each point of the first input, uses the value as an index into attributes of the second input (the Value Attributes of the lookup curve). It outputs those looked-up values into new or existing attributes (Output Attribute Scope).
The lookup curve (second input) can be the output of a [Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP"), for example.
If the index is 0, it pulls values from the first point of the lookup curve, and if the index is 1 it pulls from the last sample of the lookup curve. Alternately, if the Lookup Index Units menu is set to Point Index, the lookup index is expressed as a point number of the lookup curve, going from 0 to number_of_points-1.
If the index is out of range, the Extend Left and Right menus determine what to do to the index before doing the lookup, such as holding it at 0 or 1, or cycling the value between 0 and 1.
Sequential blocks let you lookup and output more than one attribute. In each block you can re-range the value before putting it in the specified output attribute.
See also [Lookup Texture POP](https://docs.derivative.ca/Lookup_Texture_POP "Lookup Texture POP"), [Lookup Channel POP](https://docs.derivative.ca/Lookup_Channel_POP "Lookup Channel POP"), [Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP") (Lookup page).
[lookupattributePOP_Class](https://docs.derivative.ca/LookupattributePOP_Class "LookupattributePOP Class")

## Parameters - Lookup Attribute Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Lookup Index Attribute(s) `lookupindexattr` - Attribute(s) to use as the index(es) for the lookup(s).
- Lookup Index Units `indexunit` - ⊞ - Units for lookup index attribute.
  * Normalized (0-1) `normalized` -
  * Point Index `pointindex` -

- Cyclic Index `cyclic` - When enabled, the index wraps so the end connects back to the start, letting the full range map evenly across the cycle.
- Interpolate `interpolate` - When on, the input can be interpolated between the input elements' attribute values. When off, the nearest element value is used.
- From Low High `indexfromlow` - ⊞ - Reranges the index attribute value.
  * From Low High `indexfromlow` -
  * From High `indexfromhigh` - Reranges the index attribute value.

- To Low High `indextolow` - ⊞ - Reranges the index attribute value.
  * To Low High `indextolow` -
  * To High `indextohigh` - Sets high value on the output range.

- Extend Left and Right `extendleft` - ⊞ - What happens when the lookup samples outside of the range.
  * Hold `hold` -
  * Slope `slope` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Extend Left and Right `extendleft` -
  * Extend Right `extendright` - What happens when the lookup samples the POP beyond the maximum number of elements.

- Lookup `lookup` - Start of Sequential Parameter Blocks of lookups.
- Value Attributes `lookup0valueattr` - Sets the looked-up value attribute scope.
- From Low High `lookup0fromlow` - ⊞ - Reranges the index attribute value.
  * From Low High `lookup0fromlow` -
  * From High `lookup0fromhigh` - Reranges the value resulting from the lookup.

- From High `lookup0fromhigh` -
- To Low High `lookup0tolow` - ⊞ - Reranges the output attribute value.
  * To Low High `lookup0tolow` -
  * To High `lookup0tohigh` - Sets high value on the output range.

- To High `lookup0tohigh` -
- Output Attribute Scope `lookup0outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.i012 `Color.i012` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -
  * Color.rgb `Color.rgb` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Lookup Attribute POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
