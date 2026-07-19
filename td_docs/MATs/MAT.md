---
url: https://docs.derivative.ca/MAT
category: MATs
title: MAT
---

# MAT

## Summary

[![OP MAT.png](https://docs.derivative.ca/images/b/bc/OP_MAT.png)](https://docs.derivative.ca/File:OP_MAT.png)
MATs or Materials are an [Operator Family](../Glossary/Operator_Family.md "Operator Family") that applies a [Shader](../Glossary/Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

See also [Category:MATs](https://docs.derivative.ca/Category:MATs "Category:MATs") for a full list of articles related to MATs.

**Material Operators**, or **MATs** , are used to create materials for geometry. They can be applied to geometry using the **Material** parameter on the Display page of [Object Components](../Glossary/Object_Component.md "Object Component").

The [Phong MAT](Phong_MAT.md "Phong MAT") and [GLSL MAT](GLSL_MAT.md "GLSL MAT") are designed to use [TOPs](../TOPs/TOP.md "TOP") and [GLSL](../Glossary/GLSL.md "GLSL") programs (pixel and vertex shaders) as inputs to create more advanced shaders.

The most commonly used MAT is the Phong MAT. The Phong MAT contains a large number of lighting options that allow the users to create some very unique effects.

[Phong MAT](Phong_MAT.md "Phong MAT") - applies a phong shader to the geometry. Geometry must have [normals](../Glossary/Normals.md "Normals") for specular shading to work. Geometry must have [Texture Coordinates](https://docs.derivative.ca/Point_Attributes "Point Attributes") for any applied maps to work (ie Color Map, Bump Map, Specular Map, etc). Geometry can be deformed using the Deform parameter page. The Phong MAT offers other advanced features for [Transparency](https://docs.derivative.ca/Transparency "Transparency"), [Rim Lights](https://docs.derivative.ca/Rim_Light "Rim Light"), and [Shadows](https://docs.derivative.ca/Shadows "Shadows").

[PBR MAT](PBR_MAT.md "PBR MAT") - applies a PBR shader to the geometry. Use in conjunction with an [Environment Light COMP](../COMPs/Environment_Light_COMP.md "Environment Light COMP"). [Substance Designer](http://www.allegorithmic.com/products/substance-designer) PBR materials can also be used via .sbsar files loaded into the [Substance TOP](../TOPs/Substance_TOP.md "Substance TOP").

[Line MAT](Line_MAT.md "Line MAT") - renders the geometry edges as lines and points with different geometry.

[Constant MAT](Constant_MAT.md "Constant MAT") - this material applies a constant flat color to the geometry. There is no specular shading, ie shading is not affected by the camera or light positions.

[PBR MAT](PBR_MAT.md "PBR MAT") - applies a PBR shader to the geometry. Use in conjunction with an [Environment Light COMP](../COMPs/Environment_Light_COMP.md "Environment Light COMP"). [Substance Designer](http://www.allegorithmic.com/products/substance-designer) PBR materials can also be used via `.sbsar` files loaded into the [Substance TOP](../TOPs/Substance_TOP.md "Substance TOP").

[Depth MAT](Depth_MAT.md "Depth MAT") - can be used to get depth information from the geometry for a depth-pass render. It will not render any color.

[GLSL MAT](GLSL_MAT.md "GLSL MAT") - a powerful material operator which applies Pixel and Vertex GLSL shaders to the geometry. Geometry can be deformed on the GPU using vertex shaders. Geometry must have [Texture Coordinates](https://docs.derivative.ca/Point_Attributes "Point Attributes") and [normals](../Glossary/Normals.md "Normals").

[Point Sprite MAT](Point_Sprite_MAT.md "Point Sprite MAT") - special material for use with Point Sprite geometry type. The [Particle SOP](../SOPs/Particle_SOP.md "Particle SOP") can create point sprites.

[MAT Class Class](https://docs.derivative.ca/index.php?title=MAT_Class_Class&action=edit&redlink=1 "MAT Class Class \(page does not exist\)")

##  Using MATs

  * for Materials to texture geometry with, Phong MAT, GLSL MAT
  * setup for materials (normals, uvs, where to apply, lighting and rendering)
  * examples of applying a material, example of Rim Lighting, example of shadows

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

MATs or Materials are an [Operator Family](../Glossary/Operator_Family.md "Operator Family") that applies a [Shader](../Glossary/Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

MATs or Materials are an [Operator Family](../Glossary/Operator_Family.md "Operator Family") that applies a [Shader](../Glossary/Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
