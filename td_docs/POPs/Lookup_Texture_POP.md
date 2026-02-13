---
url: https://docs.derivative.ca/Lookup_Texture_POP
category: POPs
title: Lookup_Texture_POP
---

# Lookup Texture POP
## Summary

The Lookup Texture POP in its simplest form takes two attributes (the Lookup Attribute U and the Lookup Attribute V) with values in the 0-1 range and for each point, uses the attribute value as an index into the pixels of a TOP, pulling the four RGBA values, and placing those values into POP attributes.
If the U index is 0, it pulls values from the first column of the TOP, and if the index is 1 it pulls from the last column of the TOP. If the Lookup Index Units menu is set to Pixel Index, The lookup index can be expressed as pixel number, going from 0 to imagewidth-1.
If the index is out of range, the Extend Left and Right menus determine what to do to the index before doing the lookup, such as holding it at 0 or 1, or cycling the value between 0 and 1.
The Output Attribute Scope parameter determine what to do with each of the RGBA pixel values when they are retrieved - you can re-range the value before putting it in the specified output attribute.
You can lookup into a 3D texture TOP by including an attribute component name in the Lookup Attribute W parameter.
See also [Lookup Attribute POP](https://docs.derivative.ca/Lookup_Attribute_POP "Lookup Attribute POP"), [Lookup Channel POP](https://docs.derivative.ca/Lookup_Channel_POP "Lookup Channel POP"), [Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP") (Lookup page)
[lookuptexturePOP_Class](https://docs.derivative.ca/LookuptexturePOP_Class "LookuptexturePOP Class")

## Parameters - Lookup Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- TOP `top` - TOP to use for lookup.
- Lookup Index Units `indexunit` - ⊞ - Units for lookup index attribute.
  * Lookup Index Units `indexunit0` -
  * Lookup Index Units `indexunit1` -
  * Lookup Index Units `indexunit2` -

- Pixel Centered Sampling Location `pixelcentered` - ⊞ - Enable input remapping to sample pixels centers.
  * Pixel Centered Sampling Location `pixelcentered0` - Enable the addition of a half pixel offset when using normalized lookup indices.
  * Pixel Centered Sampling Location `pixelcentered1` -
  * Pixel Centered Sampling Location `pixelcentered2` -

- Cyclic Index `cyclic` - ⊞ - When enabled, the index wraps so the end connects back to the start, letting the full range map evenly across the cycle.
  * Cyclic Index `cyclic0` -
  * Cyclic Index `cyclic1` -
  * Cyclic Index `cyclic2` -

- Input Extend Mode `inputextend` - ⊞ - What happens when the lookup index attribute is outside of the valid range (0 to 1 for normalized, 0 to numPixels-1 for Pixel Index)
  * Input Extend Mode `inputextend0` - If sampling with your U, V and W outside the texture 0 to 1 range, how to treat the image: as if it is repeating the image outside its range, mirroring it, holding its edge colors, zero.
  * Input Extend Mode `inputextend1` -
  * Input Extend Mode `inputextend2` -

- Interpolate `interpolate` - When on, the TOP can be interpolated between pixels. When off, the nearest pixel used.
- Use Depth Offset `usedepthoffset` - Enable using the texture's depth offset for Texture 3D TOPs.
- Channel Mask `channelmask` - Allows to choose which color channels to sample in the TOP.
- From Low `fromlow` - ⊞ - Reranges the index attribute value.
  * From Low `fromlow0` -
  * From Low `fromlow1` -
  * From Low `fromlow2` -
  * From Low `fromlow3` -

- From High `fromhigh` - ⊞ - Reranges the value resulting from the lookup.
  * From High `fromhigh0` -
  * From High `fromhigh1` -
  * From High `fromhigh2` -
  * From High `fromhigh3` -

- To Low `tolow` - ⊞ - Sets low value on the output range.
  * To Low `tolow0` -
  * To Low `tolow1` -
  * To Low `tolow2` -
  * To Low `tolow3` -

- To High `tohigh` - ⊞ - Sets high value on the output range.
  * To High `tohigh0` -
  * To High `tohigh1` -
  * To High `tohigh2` -
  * To High `tohigh3` -

- Output Attribute Scope `outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `overrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attrtype` - ⊞ - The output attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * Color `color` -
  * Color (double) `dcolor` -
  * Direction `dir` -
  * Direction (double) `ddir` -

- Components `attrnumcomps` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `attrdefaultval` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `attrdefaultval0` - Default value(s) of the attribute.
  * Default Value `attrdefaultval1` - Default value(s) of the attribute.
  * Default Value `attrdefaultval2` - Default value(s) of the attribute.
  * Default Value `attrdefaultval3` - Default value(s) of the attribute.

- Lookup Index Attribute U `lookupindexattr0` - Attribute to use as the index for the U coordinate of the lookup.
- Lookup Index Attribute V `lookupindexattr1` - Attribute to use as the index for the V coordinate of the lookup.
- Lookup Index Attribute W `lookupindexattr2` - Attribute to use as the index for the W coordinate of the lookup.
- Lookup Index Offset `lookupindexoffset` - ⊞ - Offset for the lookup index.
  * Lookup Index Offset `lookupindexoffset0` -
  * Lookup Index Offset `lookupindexoffset1` -
  * Lookup Index Offset `lookupindexoffset2` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Lookup Texture POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
