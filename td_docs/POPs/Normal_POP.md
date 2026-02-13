---
url: https://docs.derivative.ca/Normal_POP
category: POPs
title: Normal_POP
---

# Normal POP
## Summary

The Normal POP lets you create “normal vectors” and “tangent vectors” based on the incoming set of triangles or quads.
You can create normals or tangents as point attributes, vertex attributes or primitive attributes.
You can choose from several strategies for computing normals and tangents, based on each point being a member of several primitives.
You usually use the P position attribute to compute the normals and tangents, but you can use any vec3 attribute.
The results are placed in the N and (optionally) T attributes, but you can name the new attribute anything.
If the incoming geometry already has normal or tangent vectors, you can choose to do nothing, re-compute values, error, or delete the attributes.
Because this runs on the GPU that needs pre-determined sizes, you need to set the Max Number of Primitives per Point, the default 6 being typically sufficient.
[normalPOP_Class](https://docs.derivative.ca/NormalPOP_Class "NormalPOP Class")

## Parameters - Normals Page
- Normals Action `nml` - ⊞ - Choose what to do regarding normals.
  * No Action `noaction` -
  * Always Compute `alwayscompute` -
  * Compute if it doesn't exist `computeifnone` -
  * Remove `remove` -

- Input Position Attribute `inputposattrn` - Input Position attribute used to calculate normals.
- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- Normals Weighting `nmlweighting` - ⊞ - For point normals, choose how to weight the normals of the primitives the point is a part of.
  * Average `average` -
  * Angle Weighted `angleWeighted` -
  * Area Weighted `areaweighted` -

- Compute Normals Technique `compnmltech` - ⊞ - Specify which technique to use to calculate point normals.
  * Atomic Float (if supported) `atomicfloat` -
  * Atomic Comp Swap `atomiccompswap` -
  * Loop over Primitives Per Point `loopprims` -

- Max Number of Primitives per Point `maxprimsperpoint` - Used to allocate temporary storage with the "Loop over Primitives Per Point" method, it should be set to the maximum number of primitives a point can be a part of in the input geometry.
- Angle `angle` - For vertex normals, the threshold angle between faces above which the shared edge vertices don't share normals.
- Normal Output Attribute Scope `outputattrscopen` - ⊞ - Output attribute scope for the normal.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.i012 `Color.i012` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `overrideautoattrn` - When on, overrides the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attrtypen` - ⊞ - The normal output attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * dir `dir` -
  * dbl dir `ddir` -

- Components `attrnumcompsn` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `attrdefaultvaln` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `attrdefaultvaln0` -
  * Default Value `attrdefaultvaln1` -
  * Default Value `attrdefaultvaln2` -
  * Default Value `attrdefaultvaln3` -

## Parameters - Tangents Page
- Tangents Action `tang` - ⊞ - Sets the tangent operation.
  * No Action `noaction` -
  * Always Compute `alwayscompute` -
  * Compute if it doesn't exist `computeifnone` -
  * Remove `remove` -

- Input Position Attribute `inputposattrt` - Input Position attribute used to calculate tangents.
- Input Normal Attribute `inputnormalattr` - Input normal attribute used to calculate tangents.
- Input Texture Coord Attribute `inputtexattrib` - Input texture coordinate attribute used to calculate tangents.
- Compute Tangents Technique `comptangtech` - ⊞ - Specify which technique to use to calculate tangents.
  * Atomic Float (if supported) `atomicfloat` -
  * Atomic Comp Swap `atomiccompswap` -

- Tangent Output Attribute Scope `outputattrscopet` - ⊞ - Output attribute scope for the tangent.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `overrideautoattrt` - When on, overrides the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attrtypet` - ⊞ - The tangent attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * Color `color` -
  * Color (double) `dcolor` -
  * Direction `dir` -
  * Direction (double) `ddir` -

- Components `attrnumcompst` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `attrdefaultvalt` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `attrdefaultvalt0` -
  * Default Value `attrdefaultvalt1` -
  * Default Value `attrdefaultvalt2` -
  * Default Value `attrdefaultvalt3` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Normal POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
