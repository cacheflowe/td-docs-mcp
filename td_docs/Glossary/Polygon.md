---
url: https://docs.derivative.ca/Polygon
category: Glossary
title: Polygon
---

# Polygon

A polygon is a type of [Primitive](Primitive.md "Primitive") that is formed from a set of [Vertices](Vertex.md "Vertex") in 3D that are implicitly connected together to form a multi-edge shape. Each [Vertex](Vertex.md "Vertex") is a reference to a [Point](Point.md "Point") in a [Point List](Point_List.md "Point List"). Polygons in a Primitive List are part of the [Geometry Detail](Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP"). **Types of Polygons**
  * **Closed or Open**

A polygon can be closed, where the last vertex is connected to the first vertex, or may be open, where the last vertex is not connected to the first vertex. This is determined by the "closed" flag of a polygon.

A closed polygon shares its first and last vertex and is flagged internally as "closed". Thus, if an open polygon has five vertices, it will still have five vertices when closed. The last (closing) vertex is only implied.
[![ClosedOpenPolys.jpg](https://docs.derivative.ca/images/9/9c/ClosedOpenPolys.jpg)](https://docs.derivative.ca/File:ClosedOpenPolys.jpg)
  * **Planar or Non-planar**

Planar polygons are those whose vertices lie in the same plane in 3D space. Non-planar polygons have vertices that do no lie in the same plane in 3D space.
  * **Convex or Concave**

A polygon can be [convex or concave](https://docs.derivative.ca/Convex_and_Concave_Polygons "Convex and Concave Polygons"), as illustrated below:
[![ConvexPolys.jpg](https://docs.derivative.ca/images/4/44/ConvexPolys.jpg)](https://docs.derivative.ca/File:ConvexPolys.jpg)
Convex Polygons
[![ConcavePolys.jpg](https://docs.derivative.ca/images/a/a8/ConcavePolys.jpg)](https://docs.derivative.ca/File:ConcavePolys.jpg)
Concave Polygons

A polygon is convex if any vertical or horizontal axis intersects it at most twice.

See also: [Geometry Detail](Geometry_Detail.md "Geometry Detail"), [Point](Point.md "Point"), [Point List](Point_List.md "Point List"), [Point Class](../SOPs/Point_Class.md "Point Class"), [Primitive](Primitive.md "Primitive"), [Prims Class](../SOPs/Prims_Class.md "Prims Class"), [Vertex](Vertex.md "Vertex"), [SOP](../SOPs/SOP.md "SOP"), [SOP Class](../SOPs/SOP_Class.md "SOP Class"), [SOP to DAT](SOP_to_DAT.md "SOP to DAT"), [Script SOP](../SOPs/Script_SOP.md "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").

A surface type in [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](Point.md "Point") and Primitives are part of the [Geometry Detail](Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").
