---
url: https://docs.derivative.ca/Point
category: Glossary
title: Point
---

# Point

_(note - to be updated for POPs - currently SOP-leaning)_

See [Point Class](../SOPs/Point_Class.md "Point Class") for the Python API.

Each POP and SOP has a list of Points. A Point is an XYZ position with some optional extra attributes. The [point attributes](Attribute.md "Attribute") are:
  * `P` - an XYZ 3D position represented as 3 floating point numbers.
  * `Cd` - color (optional) a standard 4-value attribute where the RGB color is `Cd[0]`, `Cd[1]`, `Cd[2]` and alpha which is `Cd[3]`. (See [Point SOP](../SOPs/Point_SOP.md "Point SOP"))
  * `uv` - texture (optional) a standard 3-value attribute where UV are `uv[0]` and `uv[1]`, and W is `uv[2]`. (See [Point SOP](../SOPs/Point_SOP.md "Point SOP"))
  * `N` - normal vector (optional) a standard 3-value attribute. (See [Facet SOP](../SOPs/Facet_SOP.md "Facet SOP") and [Point SOP](../SOPs/Point_SOP.md "Point SOP"))
  * `T` - tangent vector (optional) a standard 4-value attribute. (See [Attribute Create SOP](../SOPs/Attribute_Create_SOP.md "Attribute Create SOP"))
  * user-defined attributes. (See [Point SOP](../SOPs/Point_SOP.md "Point SOP"))

Each [Polygon](Polygon.md "Polygon") is defined by a vertex list, which is a list of point numbers.

On s SOP, MMB on the node to see a summary of the points, polygons, particle systems and other primitives, attributes and bounding box.

Note: Points can not be rendered directly. To render points they must first be [Particles](https://docs.derivative.ca/Particle "Particle"). Points can be converted to particles using the [Convert SOP](../SOPs/Convert_SOP.md "Convert SOP") or generated directly by the [Particle SOP](../SOPs/Particle_SOP.md "Particle SOP"). See also [Point Sprite MAT](../MATs/Point_Sprite_MAT.md "Point Sprite MAT").

See also: [Point List](Point_List.md "Point List"), [Geometry Detail](Geometry_Detail.md "Geometry Detail"), [Point SOP](../SOPs/Point_SOP.md "Point SOP"), [Point Class](../SOPs/Point_Class.md "Point Class"), [Primitive](Primitive.md "Primitive"), [Polygon](Polygon.md "Polygon"), [Vertex](Vertex.md "Vertex"), [Prims Class](../SOPs/Prims_Class.md "Prims Class"), [SOP](../SOPs/SOP.md "SOP"), [SOP Class](../SOPs/SOP_Class.md "SOP Class"), [SOP to DAT](SOP_to_DAT.md "SOP to DAT"), [Script SOP](../SOPs/Script_SOP.md "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attribute](Attribute.md "Attribute").

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
