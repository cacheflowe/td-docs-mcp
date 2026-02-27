---
url: https://docs.derivative.ca/Normals
category: Glossary
title: Normals
---

# Normals

[![](https://docs.derivative.ca/images/thumb/b/b1/Normals.jpg/300px-Normals.jpg)](https://docs.derivative.ca/File:Normals.jpg)
[](https://docs.derivative.ca/File:Normals.jpg "Enlarge")

A box SOP with point normals (blue) and primitive normals (pink).

A **normal** is a directional vector associated with a particular geometric entity, commonly perpendicular to it. The normal to a surface at a given point is a vector perpendicular to the surface at that point, and is computed as the cross product of the tangent vectors at that point.

The direction the normals take (up or down) is dependent on the order in which the cross product is computed (imagine a cork moving up or down depending on the direction the cork screw turns).

Normals are used for such things as: the basis for the direction things move over time, and for determining shading. In the Model Editor you can use point and primitive normals to pick, and even translate geometry along the normal.

Surface normals indicate the direction a surface faces. This is used to determine the amount of shading that a surface receives; the more it faces the light, the lighter the shading it receives.

##  Types of Normals

Normals come in four varieties: plane normals, point normals, vertex normals, and surface normals. They indicate the orientation (direction) of a point, plane, vertex, or surface curve. If a curve is planar and does not share its points with other primitives, its default point, vertex, and primitive normals are identical, perpendicular to the plane of the curve.

##  Activating Normals Display

Activate the Point, Vertex, and Primitive Normal Display in TouchDesigner by enabling the normals option in the [Display Options](https://docs.derivative.ca/Display_Options "Display Options") dialog, available by right-clicking any SOP and selecting _Display Parameters_ from the context menu.

Note that the point normals must have been computed first (in a Point SOP, for example). Primitive normals are computed on the spot and only when they are turned on for display. Some systematic primitives, like sphere and cylinder do not have a normal.

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](https://docs.derivative.ca/Primitive "Primitive") is defined by a vertex list, which is list of point numbers.

A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

A surface type in [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").
