---
url: https://docs.derivative.ca/Vertex
category: Glossary
title: Vertex
---

# Vertex

A vertex is part of a [Polygon](Polygon.md "Polygon"), and a Polygon is a [Primitive](Primitive.md "Primitive") in a [SOP](../SOPs/SOP.md "SOP"). A polygon is is formed from a sequence of vertices that are implicitly connected together to form a multi-edge shape in 3D.

Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and optional [Attributes](Attribute.md "Attribute") like Normals and Texture Coordinates.

Each Vertex is a reference to a [Point](Point.md "Point") in a [Point List](Point_List.md "Point List"). Polygons in a [Primitive](Primitive.md "Primitive") List are part of the [Geometry Detail](Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP"). See also: [Geometry Detail](Geometry_Detail.md "Geometry Detail"), [Point](Point.md "Point"), [Point List](Point_List.md "Point List"), [Point Class](../SOPs/Point_Class.md "Point Class"), [Primitive](Primitive.md "Primitive"), [Prims Class](../SOPs/Prims_Class.md "Prims Class"), [Polygon](Polygon.md "Polygon"), [SOP](../SOPs/SOP.md "SOP"), [SOP Class](../SOPs/SOP_Class.md "SOP Class"), [SOP to DAT](SOP_to_DAT.md "SOP to DAT"), [Script SOP](../SOPs/Script_SOP.md "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").

A polygon is a type of [Primitive](Primitive.md "Primitive") that is formed from a set of Vertices in 3D that are implicitly connected together to form a multi-edge shape.

A sequence of vertices form a [Polygon](Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.
