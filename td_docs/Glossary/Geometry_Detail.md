---
url: https://docs.derivative.ca/Geometry_Detail
category: Glossary
title: Geometry_Detail
---

# Geometry Detail

3D Geometry in TouchDesigner is held in [SOPs](../SOPs/SOP.md "SOP"), and is stored in the data structure called a Geometry Detail (Geo-Detail). A Geo-Detail is a comprehensive listing of the entire geometry model that exists within a TouchDesigner SOP at a given time. Geo-Details are generated procedurally by SOPs, and when you save your work into a `.geo` or `.bgeo` file, it saves the entire Geo-Detail. The Geo-Detail contains a [Point List](Point_List.md "Point List"), a [Primitive](Primitive.md "Primitive") List, [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), and [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"). The detail manages [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)") per point, vertex, and primitive, and its own detail attributes.

See also: [Point](Point.md "Point"), [Point List](Point_List.md "Point List"), [Point Class](../SOPs/Point_Class.md "Point Class"), [Primitive](Primitive.md "Primitive"), [Polygon](Polygon.md "Polygon"), [Vertex](Vertex.md "Vertex"), [Prims Class](../SOPs/Prims_Class.md "Prims Class"), [SOP](../SOPs/SOP.md "SOP"), [SOP Class](../SOPs/SOP_Class.md "SOP Class"), [SOP to DAT](SOP_to_DAT.md "SOP to DAT"), [Script SOP](../SOPs/Script_SOP.md "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group").

[![GeoDetail.jpg](https://docs.derivative.ca/images/c/cf/GeoDetail.jpg)](https://docs.derivative.ca/File:GeoDetail.jpg)
A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
