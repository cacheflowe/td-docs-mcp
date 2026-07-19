---
url: https://docs.derivative.ca/SOP
category: Glossary
title: SOP
---

# SOP

## Summary

[![OP SOP.png](https://docs.derivative.ca/images/e/e6/OP_SOP.png)](https://docs.derivative.ca/File:OP_SOP.png)
**Surface Operators** , also known as **SOPs** , are operators that can generate, import, modify and combine 3D surfaces (also called geometry). The surface types include 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs - see `particlesGpu` in the palette and components in the `PointClouds` folder of the palette.

See [Category:SOPs](https://docs.derivative.ca/index.php?title=Category:SOPs&action=edit&redlink=1 "Category:SOPs \(page does not exist\)") for a full list of articles related to SOPs.

See also: [Geometry Detail](Geometry_Detail.md "Geometry Detail"), [Point](Point.md "Point"), [Point List](Point_List.md "Point List"), [Point Class](../SOPs/Point_Class.md "Point Class"), [Primitive](Primitive.md "Primitive"), [Prims Class](../SOPs/Prims_Class.md "Prims Class"), [Polygon](Polygon.md "Polygon"), [Vertex](Vertex.md "Vertex"), [SOP Class](../SOPs/SOP_Class.md "SOP Class"), [SOP to DAT](SOP_to_DAT.md "SOP to DAT"), [Script SOP](../SOPs/Script_SOP.md "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attribute](Attribute.md "Attribute").

[SOP Class](../SOPs/SOP_Class.md "SOP Class")

##  Sweet 16 SOPs

The following 16 SOPs are commonly used, we recommend familiarizing yourself with them.
SOP | Purpose | Related SOP
---|---|---
[Circle](../SOPs/Circle_SOP.md "Circle SOP") | Circle, sphere, torus primitives. |  [Sphere](../SOPs/Sphere_SOP.md "Sphere SOP"), [Torus](../SOPs/Torus_SOP.md "Torus SOP")
[Grid](../SOPs/Grid_SOP.md "Grid SOP") | Grid, box, rectangle. |  [Box](../SOPs/Box_SOP.md "Box SOP"), [Rectangle](../SOPs/Rectangle_SOP.md "Rectangle SOP")
[Merge](../SOPs/Merge_SOP.md "Merge SOP") | Merge and delete. |  [Object Merge](../SOPs/Object_Merge_SOP.md "Object Merge SOP"), [Delete](../SOPs/Delete_SOP.md "Delete SOP")
[Copy](../SOPs/Copy_SOP.md "Copy SOP") | Copy or replicate. |  [Limit](../SOPs/Limit_SOP.md "Limit SOP")
[Switch](../SOPs/Switch_SOP.md "Switch SOP") | Switch or blend multi-inputs. |  [Blend](../SOPs/Blend_SOP.md "Blend SOP"), [Sequence Blend](../SOPs/Sequence_Blend_SOP.md "Sequence Blend SOP")
[Texture](../SOPs/Texture_SOP.md "Texture SOP") | Apply texture coordinated to points or vertices. |  [Material](../SOPs/Material_SOP.md "Material SOP")
[Noise](../SOPs/Noise_SOP.md "Noise SOP") | Apply noise, twist and deform. |  [Twist](../SOPs/Twist_SOP.md "Twist SOP"), [Deform](../SOPs/Deform_SOP.md "Deform SOP")
[Transform](../SOPs/Transform_SOP.md "Transform SOP") | Transform point positions. |  [Script](../SOPs/Script_SOP.md "Script SOP")
[DAT to](../SOPs/DAT_to_SOP.md "DAT to SOP") |  DAT table to SOP points. |  [Add](../SOPs/Add_SOP.md "Add SOP")
[CHOP to](../SOPs/CHOP_to_SOP.md "CHOP to SOP") |  CHOP channel samples to SOP points. |  [Line](../SOPs/Line_SOP.md "Line SOP")
[Trace](../SOPs/Trace_SOP.md "Trace SOP") | Trace a TOP image to polygons. |  [File In](../SOPs/File_In_SOP.md "File In SOP")
[Clip](../SOPs/Clip_SOP.md "Clip SOP") | Clip and carve. |  [Carve](../SOPs/Carve_SOP.md "Carve SOP")
[Facet](../SOPs/Facet_SOP.md "Facet SOP") | Facet, subdivide, convert. |  [Subdivide](../SOPs/Subdivide_SOP.md "Subdivide SOP"), [Convert](../SOPs/Convert_SOP.md "Convert SOP")
[Particle](../SOPs/Particle_SOP.md "Particle SOP") | Particles. |
[Sweep](../SOPs/Sweep_SOP.md "Sweep SOP") | Sweep, skin, rails. |  [Skin](../SOPs/Skin_SOP.md "Skin SOP"), [Rails](../SOPs/Rails_SOP.md "Rails SOP")
[Sort](../SOPs/Sort_SOP.md "Sort SOP") | Sort and reorder. |

##  Using SOPs

  * 3D geometry data, processed on CPU
  * FBX Import: .fbx importer, File In SOP - recommend importing geometry from more mature modelers
  * FBX Export: Right-click and select **Save Geometry...** In the File Browser that opens, change the file type to .fbx to create a FBX file of that geometry.

##  See Also

[Category:SOPs](https://docs.derivative.ca/index.php?title=Category:SOPs&action=edit&redlink=1 "Category:SOPs \(page does not exist\)")

[Geometry Detail](Geometry_Detail.md "Geometry Detail")

[Primitive](Primitive.md "Primitive")

[Point](Point.md "Point")
