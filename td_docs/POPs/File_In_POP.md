---
url: https://docs.derivative.ca/File_In_POP
category: POPs
title: File_In_POP
---

# File In POP

## Summary

The File In POP reads a file and converts it into a POP in GPU memory.

File formats:
  * `.obj` The Wavefront Object File Format supports faces (polygons) and line strips (`f` and `l` tags). Triangulation occurs for polygons with more than 3 sides. It supports texture UV coordinates (Texcoord) and normals. (it uses [tinyobj](https://github.com/tinyobjloader/tinyobjloader) internally)
  * `.ply` The Stanford Triangle Format supports faces (polygons) through the `vertex_indices` property in the `face` element. Polygons with 3 and 4 sides are converted to triangles and quadrelateral primitives in POPs. Polygons with more than 4 sides are converted to closed line strips. `red`, `green`, `blue`, `alpha` or `r`, `g`, `b`, `a` vertex elements will be read as Point `Color` within POPs.

Older formats are supported as well such as:
  * `.tog` TouchDesigner Geometry files are exports of other geometry types in a native TouchDesigner format
  * `.bhclassic` Houdini binary geometry format.
  * `.hclassic` Houdini ASCII geometry format.

You can use `http://` URL prefix when specifying a supported file accessible on the network.

Some file formats can be read by both the File In POP and [Point File In POP](Point_File_In_POP.md "Point File In POP"), with the difference being the File In POP only imports attributes and elements listed above. This is a list of files that both OPs can read.
  * `.ply` file format can contain custom attribute data
  * `.obj` file format

See also: [Point File In POP](Point_File_In_POP.md "Point File In POP"), [Alembic In POP](Alembic_In_POP.md "Alembic In POP"), [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP"), [USD COMP](../COMPs/USD_COMP.md "USD COMP"), [pop File Format](https://docs.derivative.ca/Pop_File_Format "Pop File Format")

[fileinPOP_Class](File_In_POP_Class.md "FileinPOP Class")

## Parameters - File In Page
- Geometry File `file` - Contains the full pathname of the geometry file to be read in.
- Flip Primitive Faces `flipfacing` - Enable flipping the primitive faces of the geometry.
- Refresh `refresh` - ⊞ - In some modes like Circle, the points can be in a fixed patter or be random.
  * Refresh `refresh` -
  * Refresh Pulse `refreshpulse` - Force a check on the file to re-read if it has changed.
- Input Color Space `inputcolorspace` - ⊞ - Override / set the color space, or use the color space in the file, or assume default if there is none.
  * Automatic `automatic` -
  * sRGB `srgb` -
  * sRGB - Linear `srgblinear` -
  * Rec.601 (NTSC) `rec601ntsc` -
  * Rec.709 `rec709` -
  * Rec.2020 `rec2020` -
  * Rec.2020 ST2084PQ `rec2020st2084pq` -
  * Rec.2020 HLG `rec2020hlg` -
  * DCI-P3 `dcip3` -
  * DCI-P3 (D60) `dcip3d60` -
  * Display P3 (D65) `displayp3d65` -
  * Display P3 (D65) - Linear `displayp3d65linear` -
  * ACES2065-1 `aces2065-1` -
  * ACEScg `acescg` -
  * ACESproxy `acesproxy` -
  * Passthrough `passthrough` -
- Input Reference White `inputreferencewhite` - ⊞ - Color space to use for the incoming data.
  * Default For Color Space `default` -
  * Standard (SDR) `sdr` -
  * High (HDR) `hdr` -
  * UI `ui` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels

Extra Information for the File In POP can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

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
