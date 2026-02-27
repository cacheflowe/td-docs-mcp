---
url: https://docs.derivative.ca/Shader
category: Glossary
title: Shader
---

# Shader
A shader in TouchDesigner is the OpenGL (pre-2022) or Vulkan (2022-) GLSL code that runs on the GPU and creates rendered images from polygons, textures, CHOP channels and parameters.
Shaders are either embedded inside [Materials](https://docs.derivative.ca/index.php?title=Material&action=edit&redlink=1 "Material \(page does not exist\)") or placed in [Text DATs](https://docs.derivative.ca/Text_DAT "Text DAT") and referenced to a [GLSL Material](https://docs.derivative.ca/GLSL_MAT "GLSL MAT") or a [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP").
Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader. (Geometry Shaders are now obsolete.)
All shaders in TouchDesigner are GLSL shaders.
The most commonly-used materials are the [Phong MAT](https://docs.derivative.ca/Phong_MAT "Phong MAT") or [PBR MAT](https://docs.derivative.ca/PBR_MAT "PBR MAT") which contain numerous lighting and surface rendering options. The Phong MAT and PBR MAT can output the specific GLSL shader code that represents the features being used in the material, which is a good starting point for writing your own shaders or adapting other shaders.
A [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP") uses a GLSL shader for generating 2D images.
See also [Write a GLSL Material](https://docs.derivative.ca/Write_a_GLSL_Material "Write a GLSL Material").
The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.
The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](https://docs.derivative.ca/Text_DAT "Text DAT") and referenced by a [GLSL Material](https://docs.derivative.ca/GLSL_MAT "GLSL MAT") or a [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.
MATs or Materials are an [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that applies a Shader to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.
