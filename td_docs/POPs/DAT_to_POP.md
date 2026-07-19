---
url: https://docs.derivative.ca/DAT_to_POP
category: POPs
title: DAT_to_POP
---

# DAT to POP

## Summary

The DAT to POP converts DAT tables into POP geometry. Columns can be used to create attributes, primitives, groups, and dimensions, with each column providing the data needed for construction. The table must be structured as you get with POP to DAT, though for DAT to POP you don't need an `index` column as it is automatically implied.

The column headers need to be in the usual POP form. Vectors (like float3) must be expressed as one column per component of the vector, with headings, for example, `P(0)` or `Color(3)`. Arrays components must be in `MyArray[0]` etc form.

Attributes can be generated automatically from the DAT’s column names. They can also be generated manually using [sequential block](../Glossary/Sequential_Parameters.md#Sequence_Blocks "Sequential Parameters"). In each [sequential block](../Glossary/Sequential_Parameters.md#Sequence_Blocks "Sequential Parameters"), you need to specify an attribute to create. You can use `?` in `P(?)` to specify that columns `P(0)`, `P(1)` and `P(2)` will form a float3 vector `P`.

[dattoPOP_Class](DAT_to_POP_Class.md "DattoPOP Class")

## Parameters - Points Page
- Points DAT `pointsdat` - DAT containing point attributes.
- Create Point Primitives `createpointprim` - Enables creation of point primitives if no Primitive DAT is provided
- Convert All Excluding `cnvrtallpointcols` - ⊞ - Toggles automatic attribute creation from column names
  * Convert All Excluding `cnvrtallpointcols` - Toggles automatic attribute creation from column names
  * Exclude Columns `excludepointcols` - Columns to ignore when automatically converting to attributes
- Group Names Column `pointgroupnamescol` - Column containing the group information
- New Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- Select Columns by `attr0columnstype` - ⊞ - Specifies the columns selection method.
  * Name `name` -
  * Number `number` -
- Columns `attr0columns` - The pattern of DAT columns to convert to an attribute.
- Output Attribute Scope `attr0outputscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -
  * Tex.i01 `Tex.i01` -
- Override Automatic Attribute `attr0overrideauto` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attr0type` - ⊞ - Determines the type.
  * Attribute Type `attr0type` -
  * Components `attr0numcomps` - The number of components in the new custom attribute.
- Array `attr0isarray` - ⊞ - Attribute is an array, for example 5 float3 values is an array of size 5.
  * Array `attr0isarray` -
  * Array Size `attr0arraysize` - Number of elements in the array.
- Array Size `attr0arraysize` - Number of elements in the array.

## Parameters - Primitives Page
- Primitives DAT `primitivesdat` - DAT containing primitives and the primitive attributes.
- Prim Type `primtype` - ⊞ - Sets the primitive type source
  * From Column `fromcolumn` - Sets the primitive type from a specific DAT columns
  * Point Primitives `points` - Sets the primitive type to points
  * Lines `lines` - Sets the primitive type to lines
  * Triangles `triangles` - Sets the primitive type to triangles
  * Quads `quads` - Sets the primitive type to quadrilaterals
  * Line Strips `linestrips` - Sets the primitive type to line strips
- Type Column `primtypecol` - Column that contains the primitive type. Accepted values in that column are `point`, `line`, `triangle`, `quad` and `linestrip`.
- Vertices Column `primvertices` - Column that contains the primitive vertex indices
- Convert All Excluding `cnvrtallprimcols` - ⊞ - Toggles automatic attribute creation from column names
  * Convert All Excluding `cnvrtallprimcols` - Toggles automatic attribute creation from column names
  * Exclude Columns `excludeprimcols` - Columns to ignore when automatically converting to attributes
- Group Names Column `primgroupnamescol` - Column containing the group information
- New Attribute `primattr` -
- Select Columns by `primattr0columnstype` - ⊞ - Specifies the columns selection method.
  * Name `name` -
  * Number `number` -
- Columns `primattr0columns` - The pattern of DAT columns to convert to an attribute.
- Output Attribute Scope `primattr0outputscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * Tex.i01 `Tex.i01` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -
- Override Automatic Attribute `primattr0overrideauto` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `primattr0type` - ⊞ - Determines the type.
  * Attribute Type `primattr0type` -
  * Components `primattr0numcomps` - The number of components in the new custom attribute.
- Array `primattr0isarray` - ⊞ - Attribute is an array, for example 5 float3 values is an array of size 5.
  * Array `primattr0isarray` -
  * Array Size `primattr0arraysize` - Number of elements in the array.

## Parameters - Vertices Page
- Vertices DAT `verticesdat` - DAT containing vertex attributes.
- Convert All Excluding `cnvrtallvertcols` - ⊞ - Toggles automatic attribute creation from column names
  * Convert All Excluding `cnvrtallvertcols` - Toggles automatic attribute creation from column names
  * Exclude Columns `excludevertcols` - Columns to ignore when automatically converting to attributes
- New Attribute `vertattr` -
- Select Columns by `vertattr0columnstype` - ⊞ - Specifies the columns selection method.
  * Name `name` -
  * Number `number` -
- Columns `vertattr0columns` - The pattern of DAT columns to convert to an attribute.
- Output Attribute Scope `vertattr0outputscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * Tex.i01 `Tex.i01` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -
- Override Automatic Attribute `vertattr0overrideauto` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `vertattr0type` - ⊞ - Determines the type.
  * Attribute Type `vertattr0type` -
  * Components `vertattr0numcomps` - The number of components in the new custom attribute.
- Array `vertattr0isarray` - ⊞ - Attribute is an array, for example 5 float3 values is an array of size 5.
  * Array `vertattr0isarray` -
  * Array Size `vertattr0arraysize` - Number of elements in the array.

## Parameters - Details Page
- Details DAT `detailsdat` - DAT containing detail attributes.

## Parameters - Dimensions Page
- Dimensions DAT `dimensionsdat` - DAT containing dimensions.
- Dimension Column `dimcol` - Column containing the dimension information

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels

Extra Information for the DAT to POP can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

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
