---
url: https://docs.derivative.ca/Mesh_Class
category: Python
title: Mesh_Class
---

# Mesh Class
A Mesh describes an instance of a single [geometry mesh](https://docs.derivative.ca/Mesh "Mesh"). It is an instance of a [Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class").

## Members
`closedU` → `bool` **(Read Only)** :
Returns True if the mesh is closed in U, False otherwise.

`closedV` → `bool` **(Read Only)** :
Returns True if the mesh is closed in V, False otherwise.

`numRows` → `int` **(Read Only)** :
Number of rows in the mesh.

`numCols` → `int` **(Read Only)** :
Number of columns in the mesh.
## Methods
No operator specific methods.

#  Prim Class
## Members
`center` → `TDU.Position` :
Get or set the barycentric coordinate of this primitive. It is expressed as a TDU.Position object.

`index` → `int` **(Read Only)** :
The primitive index in the list.

`normal` → `TDU.Vector` **(Read Only)** :
The calculated normal vector of this primitive, expressed as a TDU.Vector object.

`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.

`weight` → `float` **(Read Only)** :
The associated weight of the primitive. Only certain primitives, such as those created by the [Metaball SOP](https://docs.derivative.ca/Metaball_SOP "Metaball SOP") can modify this value from its default of 2.0.

`direction` → `TDU.Vector` **(Read Only)** :
A normalized vector pointing from the centroid of the SOP to the centroid of this primitive.

`min` → `TDU.Position` **(Read Only)** :
The minimum coordinates of this primitive along each dimension, expressed as a TDU.Position object.

`max` → `TDU.Position` **(Read Only)** :
The maximum coordinates of this primitive along each dimension, expressed as a TDU.Position object.

`size` → `TDU.Position` **(Read Only)** :
The size of this primitive along each dimension, expressed as a TDU.Position object.
## Methods
`destroy(destroyPoints=True)`→ `None`:
Destroy and remove the actual primitive this object refers to. This operation is only valid when the primitive belongs to a [scriptSOP](https://docs.derivative.ca/ScriptSOP_Class "ScriptSOP Class"). Note: after this call, other existing Prim objects in this SOP may no longer be valid.
  * destroyPoints - (Keyword, Optional) If True, its [points](https://docs.derivative.ca/Point_Class "Point Class") are destroyed as well, if false, they are simply detached. The argument is True by default.

`eval(u, v)`→ `TDU.Position`:
Evaluate the [position](https://docs.derivative.ca/Position_Class "Position Class") on the primitive given the u,v coordinates. u,v should be in the range [0,1]. **Note:** Polygons and curves ignore the v parameter.

```
center = op('box1').prim[0].eval(0.5, 0.5)

```

###  Special Functions
`len(Prim)`→ `int`:
Returns the total number of vertices.

```
a = len(op('box1').prim[0])

```

`[index]`→ `td.Vertex`:
Get specific vertex given an integer index

```
n = op('box1').prims[5][0]

```

`[row, col]`→ `td.Vertex`:
Get specific vertex from a Mesh given integer row and column values.

```
v = op('grid1').prims[2,3]

```

`Iterator`→ `td.Vertex`:
Iterate over each vertex.

```
for m in op('box1').prims[5]:
	# do something with m, which is a Vertex

```
