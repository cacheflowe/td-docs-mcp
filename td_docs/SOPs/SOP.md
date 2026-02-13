---
url: https://docs.derivative.ca/SOP
category: SOPs
title: SOP
---

# SOP

## Summary

[![OP SOP.png](https://docs.derivative.ca/images/e/e6/OP_SOP.png)](https://docs.derivative.ca/File:OP_SOP.png)
See [Category:SOPs](https://docs.derivative.ca/index.php?title=Category:SOPs&action=edit&redlink=1 "Category:SOPs \(page does not exist\)") for a full list of articles related to SOPs.
**Surface Operators** , also known as **SOPs** , are operators that can generate, import, modify and combine 3D surfaces (also called geometry). The surface types include 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs - see `particlesGpu` in the palette and components in the `PointClouds` folder of the palette.
See also: [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), [Point](https://docs.derivative.ca/Point "Point"), [Point List](https://docs.derivative.ca/Point_List "Point List"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), [Primitive](https://docs.derivative.ca/Primitive "Primitive"), [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").
[SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class")

##  Sweet 16 SOPs
The following 16 SOPs are commonly used, we recommend familiarizing yourself with them.
SOP | Purpose | Related SOP
---|---|---
[Circle](https://docs.derivative.ca/Circle_SOP "Circle SOP") | Circle, sphere, torus primitives. |  [Sphere](https://docs.derivative.ca/Sphere_SOP "Sphere SOP"), [Torus](https://docs.derivative.ca/Torus_SOP "Torus SOP")
[Grid](https://docs.derivative.ca/Grid_SOP "Grid SOP") | Grid, box, rectangle. |  [Box](https://docs.derivative.ca/Box_SOP "Box SOP"), [Rectangle](https://docs.derivative.ca/Rectangle_SOP "Rectangle SOP")
[Merge](https://docs.derivative.ca/Merge_SOP "Merge SOP") | Merge and delete. |  [Object Merge](https://docs.derivative.ca/Object_Merge_SOP "Object Merge SOP"), [Delete](https://docs.derivative.ca/Delete_SOP "Delete SOP")
[Copy](https://docs.derivative.ca/Copy_SOP "Copy SOP") | Copy or replicate. |  [Limit](https://docs.derivative.ca/Limit_SOP "Limit SOP")
[Switch](https://docs.derivative.ca/Switch_SOP "Switch SOP") | Switch or blend multi-inputs. |  [Blend](https://docs.derivative.ca/Blend_SOP "Blend SOP"), [Sequence Blend](https://docs.derivative.ca/Sequence_Blend_SOP "Sequence Blend SOP")
[Texture](https://docs.derivative.ca/Texture_SOP "Texture SOP") | Apply texture coordinated to points or vertices. |  [Material](https://docs.derivative.ca/Material_SOP "Material SOP")
[Noise](https://docs.derivative.ca/Noise_SOP "Noise SOP") | Apply noise, twist and deform. |  [Twist](https://docs.derivative.ca/Twist_SOP "Twist SOP"), [Deform](https://docs.derivative.ca/Deform_SOP "Deform SOP")
[Transform](https://docs.derivative.ca/Transform_SOP "Transform SOP") | Transform point positions. |  [Script](https://docs.derivative.ca/Script_SOP "Script SOP")
[DAT to](https://docs.derivative.ca/DAT_to_SOP "DAT to SOP") |  DAT table to SOP points. |  [Add](https://docs.derivative.ca/Add_SOP "Add SOP")
[CHOP to](https://docs.derivative.ca/CHOP_to_SOP "CHOP to SOP") |  CHOP channel samples to SOP points. |  [Line](https://docs.derivative.ca/Line_SOP "Line SOP")
[Trace](https://docs.derivative.ca/Trace_SOP "Trace SOP") | Trace a TOP image to polygons. |  [File In](https://docs.derivative.ca/File_In_SOP "File In SOP")
[Clip](https://docs.derivative.ca/Clip_SOP "Clip SOP") | Clip and carve. |  [Carve](https://docs.derivative.ca/Carve_SOP "Carve SOP")
[Facet](https://docs.derivative.ca/Facet_SOP "Facet SOP") | Facet, subdivide, convert. |  [Subdivide](https://docs.derivative.ca/Subdivide_SOP "Subdivide SOP"), [Convert](https://docs.derivative.ca/Convert_SOP "Convert SOP")
[Particle](https://docs.derivative.ca/Particle_SOP "Particle SOP") | Particles. |
[Sweep](https://docs.derivative.ca/Sweep_SOP "Sweep SOP") | Sweep, skin, rails. |  [Skin](https://docs.derivative.ca/Skin_SOP "Skin SOP"), [Rails](https://docs.derivative.ca/Rails_SOP "Rails SOP")
[Sort](https://docs.derivative.ca/Sort_SOP "Sort SOP") | Sort and reorder. |
##  Using SOPs
  * 3D geometry data, processed on CPU
  * FBX Import: .fbx importer, File In SOP - recommend importing geometry from more mature modelers
  * FBX Export: Right-click and select **Save Geometry...** In the File Browser that opens, change the file type to .fbx to create a FBX file of that geometry.

##  See Also
[Category:SOPs](https://docs.derivative.ca/index.php?title=Category:SOPs&action=edit&redlink=1 "Category:SOPs \(page does not exist\)")
[Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail")
[Primitive](https://docs.derivative.ca/Primitive "Primitive")
[Point](https://docs.derivative.ca/Point "Point")
