---
url: https://docs.derivative.ca/Shader
category: Glossary
title: Shader
---

# Shader

A shader in TouchDesigner is the OpenGL (pre-2022) or Vulkan (2022-) GLSL code that runs on the GPU and creates rendered images from polygons, textures, CHOP channels and parameters.

Shaders are either embedded inside [Materials](https://docs.derivative.ca/index.php?title=Material&action=edit&redlink=1 "Material \(page does not exist\)") or placed in [Text DATs](Text_DAT.md "Text DAT") and referenced to a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP").

Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader. (Geometry Shaders are now obsolete.)

All shaders in TouchDesigner are GLSL shaders.

The most commonly-used materials are the [Phong MAT](../MATs/Phong_MAT.md "Phong MAT") or [PBR MAT](../MATs/PBR_MAT.md "PBR MAT") which contain numerous lighting and surface rendering options. The Phong MAT and PBR MAT can output the specific GLSL shader code that represents the features being used in the material, which is a good starting point for writing your own shaders or adapting other shaders.

A [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP") uses a GLSL shader for generating 2D images.

See also [Write a GLSL Material](../Interoperability/Write_a_GLSL_Material.md "Write a GLSL Material").

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A sequence of vertices form a [Polygon](Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](Text_DAT.md "Text DAT") and referenced by a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.

MATs or Materials are an [Operator Family](Operator_Family.md "Operator Family") that applies a Shader to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.
