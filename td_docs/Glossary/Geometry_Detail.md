---
url: https://docs.derivative.ca/Geometry_Detail
category: Glossary
title: Geometry_Detail
---

# Geometry Detail

3D Geometry in TouchDesigner is held in [SOPs](https://docs.derivative.ca/SOP "SOP"), and is stored in the data structure called a Geometry Detail (Geo-Detail). A Geo-Detail is a comprehensive listing of the entire geometry model that exists within a TouchDesigner SOP at a given time. Geo-Details are generated procedurally by SOPs, and when you save your work into a `.geo` or `.bgeo` file, it saves the entire Geo-Detail. The Geo-Detail contains a [Point List](https://docs.derivative.ca/Point_List "Point List"), a [Primitive](https://docs.derivative.ca/Primitive "Primitive") List, [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), and [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"). The detail manages [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)") per point, vertex, and primitive, and its own detail attributes.

See also: [Point](https://docs.derivative.ca/Point "Point"), [Point List](https://docs.derivative.ca/Point_List "Point List"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), [Primitive](https://docs.derivative.ca/Primitive "Primitive"), [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [SOP](https://docs.derivative.ca/SOP "SOP"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group").

[![GeoDetail.jpg](https://docs.derivative.ca/images/c/cf/GeoDetail.jpg)](https://docs.derivative.ca/File:GeoDetail.jpg)
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
