---
url: https://docs.derivative.ca/Point_List
category: Glossary
title: Point_List
---

# Point List

The geo-detail stores all points - both those attached to primitives and those that are free-floating - in a list. These points are simply X Y Z W locations in space. The W component is the spline weight (not mass, but the amount of pull on a spline hull). Each point can also contain [attributes](https://docs.derivative.ca/Attribute "Attribute") like color, normal, and mass.

Every point in the point list can be referenced by one or more primitives in the primitive list. For example, a sphere primitive may reference a point in the point list as its definition for the location of its centre, and the same point might also be the control vertex of a NURBS curve.

## What is the difference between points and vertices?

The difference between points and vertices is that a point can be shared between primitives while vertices are unique. A point is simply "a place in space" as defined by four numbers (X, Y, Z, W).

A vertex on the other hand is a reference to a point. Primitives use vertices to reference a point (e.g. the nodes of a polygon, the center of a sphere, or the control vertex of a spline).
[![PointExample1.jpg](https://docs.derivative.ca/images/3/33/PointExample1.jpg)](https://docs.derivative.ca/File:PointExample1.jpg)
For example, if three polygons have one of their vertices in exactly the same place, and share the same point in the list, that place will contain three vertices, even though it is only a single point in the point list. Similarly, each vertex may reference a unique point, even though the points coincide in space.

It is also possible for certain primitives to use a point more than once.
[![PointExample2.jpg](https://docs.derivative.ca/images/5/5c/PointExample2.jpg)](https://docs.derivative.ca/File:PointExample2.jpg)
_A point being reused: There are seven points and one polygon containing eight vertices (vertex numbers shoen here) where the point at the apex is used twice._

To summarize, the vertices of a primitive are always unique, while the points they reference might be shared between one or more primitives in the geo-detail.

See also: [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), [Point](https://docs.derivative.ca/Point "Point"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), [Primitive](https://docs.derivative.ca/Primitive "Primitive"), [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [SOP](https://docs.derivative.ca/SOP "SOP"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").
