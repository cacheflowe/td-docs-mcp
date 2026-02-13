---
url: https://docs.derivative.ca/Attributes_Class
category: Python
title: Attributes_Class
---

# Attributes Class
An Attributes object describes a set of [Prim](https://docs.derivative.ca/Prim_Class "Prim Class") Class, [Point](https://docs.derivative.ca/Point_Class "Point Class") Class, or [Vertex Class](https://docs.derivative.ca/Vertex_Class "Vertex Class") [attributes](https://docs.derivative.ca/Attribute "Attribute"), contained within a [SOP](https://docs.derivative.ca/SOP_Class "SOP Class").

## Members
`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.
## Methods
`[name]`→ `Attribute`:
[Attributes](https://docs.derivative.ca/Attribute_Class "Attribute Class") can be accessed using the [] subscript operator.
  * name - The name of the attribute.

```
attribs = scriptOP.pointAttribs # get the Attributes object
normals = attribs['N']

```

`create(name, default)`→ `Attribute`:
Create a new [Attribute](https://docs.derivative.ca/Attribute_Class "Attribute Class").
  * name - The name of the attribute.
  * default - (Optional) Specify default values for custom attributes. For standard attributes, default values are implied.

Standard attributes are: N (normal), uv (texture), T (tangent), v (velocity), Cd (diffuse color).

```
# create a Normal attribute with implied defaults.
n = scriptOP.pointAttribs.create('N')

# set the X component of the first point's Normal attribute.
scriptOp.points[0].N[0] = 0.3

# Create a Vertex Attribute called custom1 with defaults set to (0.0, 0.0)
n = scriptOP.vertexAttribs.create('custom1', (0.0, 0.0) )

# Create a Primitive Attribute called custom2 defaulting to 1
n = scriptOP.primAttribs.create('custom2', 1 )

```

Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.
A surface type in [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").
