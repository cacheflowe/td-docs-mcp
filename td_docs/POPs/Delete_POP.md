---
url: https://docs.derivative.ca/Delete_POP
category: POPs
title: Delete_POP
---

# Delete POP
## Summary

The Delete POP removes (or keeps) points or primitives using 5 methods found on the Attribute, Thin, Pattern, Group and Bounding pages. You can choose to delete points or primitives. On the Attribute page you can delete based on the values of point or primitive attributes. On the Thin page you can delete based on parameter-defined ranges, steps or randomly. You can delete based on patterns using [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") on the Pattern page. You can delete based on point or primitive groups on the Group page. You can delete based on bounding ranges on any attribute on the Bounding page.
Four of the methods let you build the logic using sequential blocks of parameters. For example on the Attribute page, one block selects `P(0) > 0` and another that selects `P(1) < 0` and ANDed together they will delete points in a quarter of the space. Otherwise is common to build an attribute in a [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP") and use it in the Delete POP.
When deleting primitives, if points or vertices are no longer used, they are deleted. When deleting points, the vertices and primitives that use them can be deleted in part or entirely. Deleted points can cause like strips to be split, trimmed or deleted entirely.
For pattern matching on the Pattern page, see [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
Note: Deleting attributes can be done with the [Attribute POP](https://docs.derivative.ca/Attribute_POP "Attribute POP"), the [Select POP](https://docs.derivative.ca/Select_POP "Select POP") and all the Math POPs.
See also [Group POP](https://docs.derivative.ca/Group_POP "Group POP"). The [Field POP](https://docs.derivative.ca/Field_POP "Field POP") also can delete points.
[deletePOP_Class](https://docs.derivative.ca/DeletePOP_Class "DeletePOP Class")

## Parameters - Delete Page
- Operation `invert` - ⊞ - Inverts the selection of elements being deleted.
  * Delete Selected `dele` -
  * Delete Non-Selected `keep` -
  * Delete Selected `delete` -

- Entity `entity` - ⊞ - Sets the attribute class to use.
  * Primitives `primitive` -
  * Points `point` -

- Line Strip Behavior `linestripbehavior` - ⊞ - What to do when points of a line strip are deleted.
  * Delete Point of Line Strip `delpointoflinestrip` -
  * Split Line Strip `splitlinestrip` -
  * Delete Line Strip `dellinestrip` -

- Copy Topology Info Back to CPU `cpureadback` - Enable copying the point count and topology information held on the GPU to the CPU.

## Parameters - Attribute Page
- Attribute `attr` - Start of Sequential Parameter Blocks to create new attributes.
- Combine `attr0combine` - ⊞ - Specify how to combine the current attribute condition block with the one above.
  * And `and` -
  * Or `or` -
  * Exclusive Or `xor` -
  * Not And `nand` -
  * Not Or `nor` -

- Attribute `attr0inattr` - Name of attribute for conditions.
- Function `attr0func` - ⊞ - Comparison function used to determine which elements are selected based on its attribute value.
  * < `lt` -
  * <= `lte` -
  * > `gt` -
  * >= `gte` -
  * == `eq` -
  * != `ne` -

- Value `attr0value` - Attribute value.
- Invert `attr0invert` - Invert the selection resulting from the current conditions in the block.

## Parameters - Thin Page
- Enabled `thinenabled` - Enable thinning by index range, index step or random index.
- Thin Out Range `thinoutrange` - Enable index-based point filtering.
- Thin Range Start `thinrangestart` - Determines the starting index for range-based point filtering.
- Thin Range Length `thinrangelength` - Determines the number of points being filtered by index range.
- Thin Step `thinstep` - Filters every Nth point.
- Thin Random `thinrandom` - Determines the proportion of points randomly filtered.
- Thin Random Seed `thinrandomseed` - Sets the random seed for points being randomly filtered.
- Invert `thininvert` - Invert the selection resulting from the current conditions in the block.

## Parameters - Pattern Page
- Pattern `pattern` - Start of Sequential Parameter Blocks for index-matching pattern.
- Combine `pattern0combine` - ⊞ - Specify how to combine the current pattern block with the one above.
  * And `and` -
  * Or `or` -
  * Exclusive Or `xor` -
  * Not And `nand` -
  * Not Or `nor` -

- Pattern `pattern0pattern` - ⊞ - Index-matching pattern. see Pattern Expansion in wiki.
  * * `*` -
  * 0-50 `0-50` -
  * 0-50:2 `0-50:2` -
  * [*] `[*]` -
  * [*:4] `[*:4]` -
  * [0-49] `[0-49]` -
  * [0-49:2] `[0-49:2]` -
  * ^[*:4] `^[*:4]` -
  * [*:5:7] `[*:5:7]` -
  * [1,4,9] `[1,4,9]` -
  * 1 4 [7-9] `1 4 [7-9]` -

- Invert `pattern0invert` - Invert the selection resulting from the current conditions in the block.

## Parameters - Group Page
- Group `group` - Start of Sequential Parameter Blocks for input groups, specifying a group name in this field will cause this POP to act only upon the group specified.
- Combine `group0combine` - ⊞ - Specify how to combine the current group block with the one above.
  * And `and` -
  * Or `or` -
  * Exclusive Or `xor` -
  * Not And `nand` -
  * Not Or `nor` -

- Group `group0name` - The name of the group to use.
- Invert `group0invert` - Invert the selection resulting from the current conditions in the block.

## Parameters - Bounding Page
- Bound `bound` - Start of Sequential Parameter Blocks for bounding volumes.
- Combine `bound0combine` - ⊞ - Specify how to combine the current bounding volume block with the one above.
  * And `and` -
  * Or `or` -
  * Exclusive Or `xor` -
  * Not And `nand` -
  * Not Or `nor` -

- Attribute `bound0inattr` - Name of position attribute for bounding volume.
- Bounding Type `bound0type` - ⊞ - The type of bounding volume, Sphere or Box.
  * Bounding Box `boundingbox` -
  * Bounding Sphere `boundingsphere` -

- Translate `bound0translate` - ⊞ - These three fields translate the bound in the three axes.
  * Translate `bound0translatex` -
  * Translate `bound0translatey` -
  * Translate `bound0translatez` -

- Rotate `bound0rotate` - ⊞ - The rotation of the bounding volume.
  * Rotate `bound0rotatex` -
  * Rotate `bound0rotatey` -
  * Rotate `bound0rotatez` -

- Scale `bound0scale` - ⊞ - The scale of the bounding volume.
  * Scale `bound0scalex` -
  * Scale `bound0scaley` -
  * Scale `bound0scalez` -

- Invert `bound0invert` - Invert the selection resulting from the current conditions in the block.
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
Extra Information for the Delete POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
