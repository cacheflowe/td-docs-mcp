---
url: https://docs.derivative.ca/InputPoint_Class
category: Python
title: InputPoint_Class
---

# InputPoint Class

A Input Point is a special case of a [Point](../SOPs/Point_Class.md "Point Class") object, only available in the [Point SOP's](../SOPs/Point_SOP.md "Point SOP") parameters.

The members below are unique to Input Point. See [Point Class](../SOPs/Point_Class.md "Point Class") for other members and more information.

## Members

`color` → `TDU.Color[](Color_Class.md "Color Class")` **(Read Only)** :

The color for this point. This is different from the Cd attribute, since it can come from a Vertex if there is no color on the inputPoint itself.

`normal` → `TDU.Vector[](Vector_Class.md "Vector Class")` **(Read Only)** :

The normal for this point. This is different from the N attribute, since it can come from a Vertex or from the destination point, if there is no normal on the inputPoint itself.

`sopCenter` → `TDU.Position[](Position_Class.md "Position Class")` **(Read Only)** :

Get the barycentric coordinate of the geometry the inputPoint is a part of. This is faster than other methods to get the center of a SOP's geometry due to internal optimizations. It is expressed as a tdu.Position.

## Methods

No operator specific methods.

Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](../Glossary/Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
