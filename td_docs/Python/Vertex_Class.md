---
url: https://docs.derivative.ca/Vertex_Class
category: Python
title: Vertex_Class
---

# Vertex Class

A Vertex describes an instance to a single geometry vertex, contained within a [Prim](Prim_Class.md "Prim Class") object.

## Members

`index` → `int` **(Read Only)** :

The vertex position in its [primitive](Prim_Class.md "Prim Class").

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

`point` → `td.Point` :

Get or set the [point](../SOPs/Point_Class.md "Point Class") to which the vertex refers.

`prim` → `td.Prim` **(Read Only)** :

The [prim](Prim_Class.md "Prim Class") to which the vertex belongs.

###  Attributes

In addition to the above members, all attributes are members as well.

For example, if the Vertex contains texture coordinates, they may be accessed with: `Vertex.uv`

See: [Attribute Class](Attribute_Class.md "Attribute Class") for more information.

## Methods

No operator specific methods.
