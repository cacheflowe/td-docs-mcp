---
url: https://docs.derivative.ca/Attributes_Class
category: Python
title: Attributes_Class
---

# Attributes Class

An Attributes object describes a set of [Prim](Prim_Class.md "Prim Class") Class, [Point](../SOPs/Point_Class.md "Point Class") Class, or [Vertex Class](Vertex_Class.md "Vertex Class") [attributes](../Glossary/Attribute.md "Attribute"), contained within a [SOP](../SOPs/SOP_Class.md "SOP Class") or a [POP](POP_Class.md "POP Class").

## Members

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

## Methods

`[name]`→ `Attribute`:

[Attributes](Attribute_Class.md "Attribute Class") can be accessed using the [] subscript operator.
  * name - The name of the attribute.

```
attribs = scriptOP.pointAttribs # get the Attributes object
normals = attribs['N']
```

`create(name, default)`→ `Attribute`:

Create a new [Attribute](Attribute_Class.md "Attribute Class") for [SOP](../SOPs/SOP_Class.md "SOP Class").
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

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

shared points, normals on shared points, unique points, recalculate.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

A surface type in [POPs](../POPs/POP.md "POP") and [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](../Glossary/Point.md "Point") and Primitives are part of the [Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").
