---
url: https://docs.derivative.ca/Vertex_Class
category: Python
title: Vertex_Class
---

# Vertex Class
A Vertex describes an instance to a single geometry vertex, contained within a [Prim](https://docs.derivative.ca/Prim_Class "Prim Class") object.

## Members
`index` → `int` **(Read Only)** :
The vertex position in its [primitive](https://docs.derivative.ca/Prim_Class "Prim Class").

`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.

`point` → `td.Point` :
Get or set the [point](https://docs.derivative.ca/Point_Class "Point Class") to which the vertex refers.

`prim` → `td.Prim` **(Read Only)** :
The [prim](https://docs.derivative.ca/Prim_Class "Prim Class") to which the vertex belongs.
###  Attributes
In addition to the above members, all attributes are members as well.
For example, if the Vertex contains texture coordinates, they may be accessed with: `Vertex.uv`
See: [Attribute Class](https://docs.derivative.ca/Attribute_Class "Attribute Class") for more information.
## Methods
No operator specific methods.
