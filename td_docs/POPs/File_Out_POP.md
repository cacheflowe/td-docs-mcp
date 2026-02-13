---
url: https://docs.derivative.ca/File_Out_POP
category: POPs
title: File_Out_POP
---

# File Out POP
## Summary

The File Out POP allows you to write out POP contents to different file types. This includes point cloud and geometry file types.
You can record a sequence of files by setting the Type parameter to File Sequence. You can toggle the Record parameter which will start to create files or, when paused, add single files at a time with the Add Frame pulse parameter.
Some file formats have fixed attributes that File Out POP will look for such as the SPZ and OBJ file format. While other formats allow arbitrary point attribute writing such as the EXR and PLY file format. Only the OBJ format supports writing vertex attributes for Normal and Texture only, while no primitive attributes are written for any format.
  * `OBJ` - Requires `P(float3)`. Supports point and vertex Normals (`N` written as `vn`) and Texture (specified by Tex Coord Attrib parameter `vt`) attributes. Point Normals and Textures will be converted to vertex attributes while vertex attributes stay unchanged. Supports writing RGB Color attribute as an unofficial extension. Supports writing triangles and quads (`f`) and linestrips (`l`).
  * `SPZ` - Requires `P(float3)`, `Color(float4)`, `Scale(float3)`, and `Rot(float4)`. The spherical harmonics attribute `Sh` is optional and if present must be size 3, 8, or 15 corresponding with the [spherical harmonics degree](https://github.com/nianticlabs/spz?tab=readme-ov-file#spherical-harmonics)
  * `E57` - Requires `P(float3)`. Supports point `Color` and `N`.
  * `PLY` - Supports arbitrary point attribute writing. Support geometry writing.
  * `EXR` - Supports arbitrary point attribute writing.

When array attributes are written, if an array index is not specified (i.e. `Arr` instead of `Arr[4]`). It will loop through and replace `$i` in the output channel with the array index similar to Point File In POP.
FPS determines the number of files to output per second of the timeline.
[fileoutPOP_Class](https://docs.derivative.ca/FileoutPOP_Class "FileoutPOP Class")

## Parameters - File Out Page
- Type `type` - ⊞ - Choose to output to a single file per Record/Add, or a sequentially-named sequence of files while it is recording.
  * File `file` - Records a single file.
  * File Sequence `filesequence` - Records a sequence of files.

- Scene File Type `scenefiletype` - ⊞ - The Alembic Scene file type.
  * Alembic `abc` -

- Object File Type `objectfiletype` - ⊞ - The object file format type.
  * OBJ `obj` -
  * EXR `exr` -
  * PLY `ply` -
  * SPZ `spz` -
  * E57 `e57` -

- Unique Suffix `uniquesuff` - When enabled, me.fileSuffix will be a unique suffix when used in the file parameter.
- N `n` - N is the index used in me.fileSuffix. When unique suffix is enabled, N specifies the starting index to increment from when calculating a unique suffix/name.
- Leading Zeros Digits `leadingzerosdigits` - Specify the minimum number of suffix digits that the filename will have. If the sequence number is less than this number, leading zeros will be appended to total the number of suffix digits to be this value. Enabled only for File Sequences.
- File `file` - Sets the path and filename of the movie file that is saved out. The filename must include the file extension such as .obj/.exr etc.
- Limit Length `limitlength` - This can be used to automatically stop recording the file once it reaches a specified length.
- Length `length` - ⊞ - The length to stop recording the file at.
  * Length `length` -
  * Length Unit `lengthunit` - Help Not Available.

- Record `record` - When this parameter is set to 1, the file will be recording.
- Pause `pause` - Pauses the recording.
- Add Frame `addframe` - Adds a single frame to the output for each click of the button. Pause must be **On** to enable the Add Frame parameter.
- Max Active Saves `maxactive` - Specifies the maximum number of file saving tasks can be running at once.
- Include Primitives `includeprim` - This can be used to enable writing primtive data to the file.
- Tex Coord Attribute `texcoordattrib` - When writing out to geometry files including texture coordinates, the name of the texture attribute to use (doesn't have to be Tex).
- Attribute `attr` - Start of Sequential Parameter Blocks to create fields in the file from attributes.
- Attribute Name `attr0name` - Determines additional fields that can be created from attributes.
- Fields `attr0fields` - Determines additional fields that can be created from attributes.
- Output Color Space `outputcolorspace` - ⊞ - Override / set the color space, or use the color space in the file, or assume default if there is none.
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
  * ACES2065-1 `aces2065-1` -
  * ACEScg `acescg` -
  * ACESproxy `acesproxy` -
  * Passthrough `passthrough` -

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
Extra Information for the Box POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
