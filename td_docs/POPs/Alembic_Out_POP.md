---
url: https://docs.derivative.ca/Experimental:Alembic_Out_POP
category: POPs
title: Alembic_Out_POP
---

#  Alembic Out POP
## Summary

The Alembic Out POP writes POP contents to an Alembic `.abc` file. It outputs points, vertices, and primitives similarly but not identically to the POPs structure. `.abc` files can contain multi-frame animation, built in and custom attributes, as well as merged multi-POPs within one file.
The Alembic Out POP requires one of the following POPs primitive types to be present.
  * Points are written as `OPoints`
  * Triangle and Quad primitives are written as `OPolyMesh`,
  * Line Strips and Lines are written as `OCurves` with curve type set to Linear.

**Note*** each input POP must contain a single primitive type (i.e. an input POP can have only Triangles or only Point Primitives, however not both).
TouchDesigner converts Line Strip data to a set of points and list of lengths as Alembic does not support vertex index references like they do for Triangles and Quads when exported to `OPolyMesh`. This means closed line strips are written out with a repeated starting vertex indicating its closed. (i.e. a closed line strip `0,1,2,3,0` will become an open line strip `0,1,2,3,4` where 0 and 4 are the same point). The [Alembic In POP](https://docs.derivative.ca/Alembic_In_POP "Alembic In POP") detects when the initial and final points are repeated and converts it into a closed line strip.
**Output of Attributes**: Point, Triangle and Quad primitives support Point, Vertex and Primitive attributes while Lines and Line Strips only support Point and Primitive attributes.
**Vertex List**: Alembic uses a reversed winding order for primitives compared to TouchDesigner, this means the vertex order for each primitive is flipped when writing as well as when reading from the Alembic In POP.
**Built in Attributes**: Alembic Out POP will automatically export the following built in attributes
  * Color attribute written as `Cd float4`
  * N attribute written as `N float3`
  * Tex attribute written as either `uv float2` or when Export 3D Texture Coord is toggled as `uv float3`

**Note*** Line Strips and Lines only support built-in attributes for Point and Primitive attributes and does not support custom attribute writing.
For animated point clouds specifying the point attributes Point Id and Velocity writes these attributes as follows.
  * Point Ids as `.pointIds int64`
  * Velocity as `.velocities float3`

These attributes can be created from nodes such as [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP") that create `PartId` and `PartVel` or as a custom attribute.
**Attribute data types** : Point, Triangle, and Quad primitive support the following custom attribute types (for Point, Vertex and Primitive attributes)
  * `uint`, `int`, `float`, `double`
  * `int2`, `float2`, `double2`
  * `int3`, `float3`, `double3`
  * Array attributes

**Output of POP groups**: Alembic Out POP ignores POP groups.
**Animated multi-frame output** : The Topology Unchanged toggle can be enabled when an animated object does not have changing topologies, this will cause the topology write once in the beginning.
**Outputting multiple POPs to one Alembic file** : Alembic Out POP supports exporting multiple POPs into a single Alembic file each as it's own individual object.
See also [Alembic In POP](https://docs.derivative.ca/Alembic_In_POP "Alembic In POP"), [File Out POP](https://docs.derivative.ca/File_Out_POP "File Out POP")
[alembicoutPOP_Class](https://docs.derivative.ca/AlembicoutPOP_Class "AlembicoutPOP Class")



## Parameters - Alembic Out Page
- Unique Suffix `uniquesuff` - ⊞ - When enabled, me.fileSuffix will be a unique suffix when used in the file parameter.
gg
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

- Topology Unchanged `unchangedtopology` - When writing can be used to indicate the topology will be unchanging, this will mean the topology will only be written once.
- Samples per Second `abcfps` - Specify the time sampling rate provided to the Alembic library
- Export 3D Texture Coord `abc3dtex` - When toggled textures will be written to a custom attrib with 3D textures, as Alembic supports 2D textures by default.
- Input `input` - Start of Sequential Parameter Blocks managing the inputs of the POP.
- In POP `input0pop` - Input POP for the current sequence block.
- Object Name `input0objname` - Alembic object name.
- Ids Attribute `input0idname` - Point attribute name containing point id information. Only available when exporting Point primtives.
- Velocity Attribute `input0velname` - Point attribute name containing velocity information. Only available when exporting Point primtives.
- Point Attribute Name `input0ptattrname` - Select with pattern matching which custom point attributes to save.
- Vertex Attribute Name `input0vertattrname` - Select with pattern matching which custom vertex attributes to save.
- Prim Attribute Name `input0primattrname` - Select with pattern matching which custom primitive attributes to save.
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.


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
