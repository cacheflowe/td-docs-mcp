---
url: https://docs.derivative.ca/Point
category: Glossary
title: Point
---

# Point

See [Point Class](https://docs.derivative.ca/Point_Class "Point Class") for Python API.

Each SOP has a list of Points. A Point is an XYZ position with some optional extra attributes. The [point attributes](https://docs.derivative.ca/Attribute "Attribute") are:
  * `P` - an XYZ 3D position represented as 3 floating point numbers.
  * `Cd` - color (optional) a standard 4-value attribute where the RGB color is `Cd[0]`, `Cd[1]`, `Cd[2]` and alpha which is `Cd[3]`. (See [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"))
  * `uv` - texture (optional) a standard 3-value attribute where UV are `uv[0]` and `uv[1]`, and W is `uv[2]`. (See [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"))
  * `N` - normal vector (optional) a standard 3-value attribute. (See [Facet SOP](https://docs.derivative.ca/Facet_SOP "Facet SOP") and [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"))
  * `T` - tangent vector (optional) a standard 4-value attribute. (See [Attribute Create SOP](https://docs.derivative.ca/Attribute_Create_SOP "Attribute Create SOP"))
  * user-defined attributes. (See [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"))

Each [Polygon](https://docs.derivative.ca/Polygon "Polygon") is defined by a vertex list, which is a list of point numbers.

On s SOP, MMB on the node to see a summary of the points, polygons, particle systems and other primitives, attributes and bounding box.

Note: Points can not be rendered directly. To render points they must first be [Particles](https://docs.derivative.ca/Particle "Particle"). Points can be converted to particles using the [Convert SOP](https://docs.derivative.ca/Convert_SOP "Convert SOP") or generated directly by the [Particle SOP](https://docs.derivative.ca/Particle_SOP "Particle SOP"). See also [Point Sprite MAT](https://docs.derivative.ca/Point_Sprite_MAT "Point Sprite MAT").

See also: [Point List](https://docs.derivative.ca/Point_List "Point List"), [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), [Primitive](https://docs.derivative.ca/Primitive "Primitive"), [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [SOP](https://docs.derivative.ca/SOP "SOP"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
