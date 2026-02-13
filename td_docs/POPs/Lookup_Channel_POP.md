---
url: https://docs.derivative.ca/Lookup_Channel_POP
category: POPs
title: Lookup_Channel_POP
---

# Lookup Channel POP
## Summary

The Lookup Channel POP in its simplest form takes an attribute (the Lookup Attribute) with values in the 0-1 range and for each point, uses the attribute value as an index into the channels of a CHOP, pulling one interpolated value for each channel, and placing those values into POP attributes.
If the index is 0, it pulls values from the first sample of the CHOP, and if the index is 1 it pulls from the last sample of the CHOP. If the Lookup Index Units menu is set to Sample Index, the lookup index can be expressed as sample number, going from 0 to number_of_samples-1.
If the index is out of range, the Extend Left and Right menus determine what to do to the index before doing the lookup, such as holding it at 0 or 1, or cycling the value between 0 and 1.
Sequential blocks determine what to do with each of the channel values when they are retrieved - you can re-range the value before putting it in the specified output attribute.
See also [Lookup Texture POP](https://docs.derivative.ca/Lookup_Texture_POP "Lookup Texture POP"), [Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP") (Lookup page), [Lookup Attribute POP](https://docs.derivative.ca/Lookup_Attribute_POP "Lookup Attribute POP")
[lookupchannelPOP_Class](https://docs.derivative.ca/LookupchannelPOP_Class "LookupchannelPOP Class")

## Parameters - Lookup Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- CHOP `chop` - The CHOP to use for lookups.
- Lookup Index Attribute(s) `lookupindexattr` - Attribute(s) to use as the index(es) for the lookup(s).
- Lookup Index Units `indexunit` - ⊞ - Units for lookup index attribute.
  * Normalized (0-1) `normalized` -
  * Sample Index `sampleindex` -

- Cyclic Index `cyclic` - When enabled, the index wraps so the end connects back to the start, letting the full range map evenly across the cycle.
- Interpolate `interpolate` - When on, the CHOP can be interpolated between samples. When off, the nearest sample is used.
- Extend Left and Right `extendleft` - ⊞ - What happens when the lookup samples outside of the range.
  * Hold `hold` -
  * Slope `slope` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Extend Left and Right `extendleft` -
  * Extend Right `extendright` - What happens when the lookup samples the CHOP beyond the maximum samples.

- Lookup `lookup` - Start of Sequential Parameter Blocks of lookups.
- Channel Scope `lookup0chanscope` - Pattern of channel names to use to perform the lookup for the output attribute values.
- From Low `lookup0fromlow` - Reranges the value resulting from the lookup.
- From High `lookup0fromhigh` - Reranges the value resulting from the lookup.
- To Low `lookup0tolow` - Sets low value on the output range.
- To High `lookup0tohigh` - Reranges the output attribute value.
- Output Attribute Scope `lookup0outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `lookup0overrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `lookup0attrtype` - ⊞ - The output attribute's data type, default float.
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

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Lookup Channel POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
