---
url: https://docs.derivative.ca/SOP
category: SOPs
title: SOP
---

# SOP

## Summary

[![OP SOP.png](https://docs.derivative.ca/images/e/e6/OP_SOP.png)](https://docs.derivative.ca/File:OP_SOP.png)
**Surface Operators** , also known as **SOPs** , are operators that can generate, import, modify and combine 3D surfaces (also called geometry). The surface types include 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs - see `particlesGpu` in the palette and components in the `PointClouds` folder of the palette.

See [Category:SOPs](https://docs.derivative.ca/index.php?title=Category:SOPs&action=edit&redlink=1 "Category:SOPs \(page does not exist\)") for a full list of articles related to SOPs.

See also: [Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail"), [Point](../Glossary/Point.md "Point"), [Point List](../Glossary/Point_List.md "Point List"), [Point Class](Point_Class.md "Point Class"), [Primitive](../Glossary/Primitive.md "Primitive"), [Prims Class](Prims_Class.md "Prims Class"), [Polygon](../Glossary/Polygon.md "Polygon"), [Vertex](../Glossary/Vertex.md "Vertex"), [SOP Class](SOP_Class.md "SOP Class"), [SOP to DAT](../Glossary/SOP_to_DAT.md "SOP to DAT"), [Script SOP](Script_SOP.md "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attribute](../Glossary/Attribute.md "Attribute").

[SOP Class](SOP_Class.md "SOP Class")

##  Sweet 16 SOPs

The following 16 SOPs are commonly used, we recommend familiarizing yourself with them.
SOP | Purpose | Related SOP
---|---|---
[Circle](Circle_SOP.md "Circle SOP") | Circle, sphere, torus primitives. |  [Sphere](Sphere_SOP.md "Sphere SOP"), [Torus](Torus_SOP.md "Torus SOP")
[Grid](Grid_SOP.md "Grid SOP") | Grid, box, rectangle. |  [Box](Box_SOP.md "Box SOP"), [Rectangle](Rectangle_SOP.md "Rectangle SOP")
[Merge](Merge_SOP.md "Merge SOP") | Merge and delete. |  [Object Merge](Object_Merge_SOP.md "Object Merge SOP"), [Delete](Delete_SOP.md "Delete SOP")
[Copy](Copy_SOP.md "Copy SOP") | Copy or replicate. |  [Limit](Limit_SOP.md "Limit SOP")
[Switch](Switch_SOP.md "Switch SOP") | Switch or blend multi-inputs. |  [Blend](Blend_SOP.md "Blend SOP"), [Sequence Blend](Sequence_Blend_SOP.md "Sequence Blend SOP")
[Texture](Texture_SOP.md "Texture SOP") | Apply texture coordinated to points or vertices. |  [Material](Material_SOP.md "Material SOP")
[Noise](Noise_SOP.md "Noise SOP") | Apply noise, twist and deform. |  [Twist](Twist_SOP.md "Twist SOP"), [Deform](Deform_SOP.md "Deform SOP")
[Transform](Transform_SOP.md "Transform SOP") | Transform point positions. |  [Script](Script_SOP.md "Script SOP")
[DAT to](DAT_to_SOP.md "DAT to SOP") |  DAT table to SOP points. |  [Add](Add_SOP.md "Add SOP")
[CHOP to](CHOP_to_SOP.md "CHOP to SOP") |  CHOP channel samples to SOP points. |  [Line](Line_SOP.md "Line SOP")
[Trace](Trace_SOP.md "Trace SOP") | Trace a TOP image to polygons. |  [File In](File_In_SOP.md "File In SOP")
[Clip](Clip_SOP.md "Clip SOP") | Clip and carve. |  [Carve](Carve_SOP.md "Carve SOP")
[Facet](Facet_SOP.md "Facet SOP") | Facet, subdivide, convert. |  [Subdivide](Subdivide_SOP.md "Subdivide SOP"), [Convert](Convert_SOP.md "Convert SOP")
[Particle](Particle_SOP.md "Particle SOP") | Particles. |
[Sweep](Sweep_SOP.md "Sweep SOP") | Sweep, skin, rails. |  [Skin](Skin_SOP.md "Skin SOP"), [Rails](Rails_SOP.md "Rails SOP")
[Sort](Sort_SOP.md "Sort SOP") | Sort and reorder. |

##  Using SOPs

  * 3D geometry data, processed on CPU
  * FBX Import: .fbx importer, File In SOP - recommend importing geometry from more mature modelers
  * FBX Export: Right-click and select **Save Geometry...** In the File Browser that opens, change the file type to .fbx to create a FBX file of that geometry.

##  See Also

[Category:SOPs](https://docs.derivative.ca/index.php?title=Category:SOPs&action=edit&redlink=1 "Category:SOPs \(page does not exist\)")

[Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail")

[Primitive](../Glossary/Primitive.md "Primitive")

[Point](../Glossary/Point.md "Point")
