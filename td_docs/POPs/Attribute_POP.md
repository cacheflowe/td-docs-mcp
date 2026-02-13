---
url: https://docs.derivative.ca/Attribute_POP
category: POPs
title: Attribute_POP
---

# Attribute POP
## Summary

The Attribute POP lets you:
  * Create new attributes
  * Rename attributes
  * Duplicate attributes
  * Delete attributes
  * Create matrix attributes

Refer to [Attribute](https://docs.derivative.ca/Attribute "Attribute").
When you create a new attribute, you specify:
  * the name (choose from built-in pre-defined names, or create your own)
  * the type (float, double, int, uint)
  * the number of components in the attribute (1, 2, 3 or 4 only). Examples:
    * A float type with 3 components is therefore a float3.
    * A double with 2 components is a double2.
    * An int with 4 components is an ivec4.
    * A uint with 3 components is a uint3.
  * arrays of the above, for example create a array of 8 float3, appearing as float3[8]. The array length can be anything.
  * the default value for each component of the attribute

New attributes can also be matrices (done on the Matrix page), like creating a mat4x4.
[attributePOP_Class](https://docs.derivative.ca/AttributePOP_Class "AttributePOP Class")

## Parameters - Create Page
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Group `group` - If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Notification if Attribute Exists `notificationifexists` - ⊞ - Whether to display a notification if the attribute already exists on the input.
  * Ignore `ignore` -
  * Warning `warning` -
  * Error `error` -

- Override if Attribute Exists `overrideifexists` - When on, overrides an input attribute if a new attribute created by this POP has the same name.
- Pre-Multiply RGB by Alpha `premultcolor` - Enable RGB values pre-multiplication with the Alpha.
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- Name `attr0name` - ⊞ - Choose to create a predefined attribute or a custom attribute.
  * Custom `custom` -
  * N `n` -
  * Color `color` -
  * Tex `tex` -
  * PointScale `pointscale` -
  * LineWidth `linewidth` -
  * Name `attr0name` -
  * Custom Name `attr0customname` - The name of the new custom attribute.

- Custom Name `attr0customname` - The name of the new custom attribute.
- Type `attr0type` - ⊞ - Determines the type.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * dir `dir` -
  * dbl dir `ddir` -
  * Type `attr0type` -
  * Number of Components `attr0numcomps` - Number of components of the new attribute.

- Number of Components `attr0numcomps` - ⊞ -
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Array `attr0isarray` - Attribute is an array, for example 5 float3 values is an array of size 5.
- Array Size `attr0arraysize` - Nunber of elements in the array.
- Value `attr0value` - ⊞ - Attribute value.
  * Value `attr0value0` - Attribute value(s).
  * Value `attr0value1` - Attribute value(s).
  * Value `attr0value2` - Attribute value(s).
  * Value `attr0value3` - Attribute value(s).

## Parameters - Matrix Page
- Matrix Attribute `matattr` - Start of Sequential Parameter Blocks to create new matrix attributes.
- Matrix Name `matattr0name` - The name of the matrix attribute.
- Rows `matattr0numrows` - Number of rows in the matrix - 2, 3 or 4.
- Columns `matattr0numcols` - Number of columns in the matrix - 2, 3 or 4.
- Array `matattr0isarray` - ⊞ - Attribute is an array, for example 5 float3 values is an array of size 5.
  * Array `matattr0isarray` -
  * Array Size `matattr0arraysize` - Nunber of elements in the array of matrices.

- Qualifier `matattr0qualifier` - ⊞ - Additional detail on how the attribute should be interpreted.
  * None `none` -
  * Transform Matrix `transformMatrix` -

## Parameters - Rename Page
- Rename Attribute `ren` - Start of Sequential Parameter Blocks to rename attributes.
- From Attribute `ren0from` - The attribute to rename.
- To Attribute `ren0to` - Sets the new attribute name.

## Parameters - Duplicate Page
- Duplicate Attribute `dup` - Start of Sequential Parameter Blocks to duplicate attributes.
- Duplicate Attribute `dup0name` - Name of attribute to duplicate.
- New Attribute Name `dup0new` - Name of new attribute being duplicated.

## Parameters - Delete Page
- Delete Point Attributes `deletepoint` - ⊞ - List of Point attributes to delete.
  * * `*` -

- Delete Vertex Attributes `deletevert` - ⊞ - List of Vertex attributes to delete.
  * * `*` -

- Delete Primitive Attributes `deleteprim` - ⊞ - List of Primitive attributes to delete.
  * * `*` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.
- Parameter Color Space `parmcolorspace` - ⊞ - Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](https://docs.derivative.ca/Color_Space "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space.
  * sRGB `srgb` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
  * sRGB - Linear `srgblinear` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.601 (NTSC) `rec601ntsc` - [Rec.601](https://en.wikipedia.org/wiki/Rec._601) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.709 `rec709` - [Rec.709](https://en.wikipedia.org/wiki/Rec._709) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.2020 `rec2020` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 `dcip3` - [DCI-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 (D60) `dcip3d60` - [DCI-P3 "D60 sim"](https://en.wikipedia.org/wiki/DCI-P3) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) `displayp3d65` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACES2065-1 `aces2065-1` - [ACES 2065-1](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACEScg `acescg` - [ACEScg](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Passthrough `passthrough` - When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.

- Parameter Reference White `parmreferencewhite` - ⊞ - When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space selected.
  * Use Parent Panel `useparent` - Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
  * Standard (SDR) `sdr` - Will treat the Parameter Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Parameter Color Space as HDR for it's reference white value.
  * UI `ui` - Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Attribute POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
