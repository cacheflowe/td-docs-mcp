---
url: https://docs.derivative.ca/Bezier_Class
category: Python
title: Bezier_Class
---

# Bezier Class
A Bezier describes an instance of a single geometry Bezier primitive (containing a set of connected Bezier curves). It is an instance of a [Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class"). It can be created from either a [Model SOP](https://docs.derivative.ca/ModelSOP_Class "ModelSOP Class") or [Script SOP](https://docs.derivative.ca/ScriptSOP_Class "ScriptSOP Class"). Each curve is described by a set of segments, where each segment is a list of [vertices](https://docs.derivative.ca/Vertex_Class "Vertex Class"). The first and last vertex of each segment is an anchor position, while its neighboring vertices describe tangent handles.
The members and methods below allow modification of the Bezier in a modelling context, however the Bezier can also be modified by direction manipulation of its vertices. See [Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class") for more details.

## Members
`anchors` → `list` **(Read Only)** :
Returns the list of anchor [vertices](https://docs.derivative.ca/Vertex_Class "Vertex Class").

`basis` → `list` **(Read Only)** :
Return the bezier basis as a list of float values.

`closed` → `bool` :
Get or set whether the curve is closed or open.

`order` → `float` **(Read Only)** :
Return the bezier order. The order is one more than the degree.

`segments` → `list` **(Read Only)** :
Returns a list of segments, where each segment is a list of [vertices](https://docs.derivative.ca/Vertex_Class "Vertex Class").

`tangents` → `list` **(Read Only)** :
Returns the tangents as a list of [vertex](https://docs.derivative.ca/Vertex_Class "Vertex Class") pairs.
## Methods
`insertAnchor(u)`→ `Vertex`:
inserts anchor at given position (u from 0..1) and returns anchor vertex.

`updateAnchor(anchorIndex, targetPosition, tangents=True)`→ `tdu.Position`:
Modify the anchor vertex to the new [position](https://docs.derivative.ca/Position_Class "Position Class"). If tangents is True, modify neighboring tangent vertices as well. Returns resulting position.

`appendAnchor(targetPosition, preserveShape=True)`→ `Vertex`:
Appends a set of vertices, creating a new segment on the curve, ending with the targetPosition.
Returns final anchor vertex.
  * preserveShape - (Keyword, Optional) Specifies whether the new tangent will align with the previous segment or not.

`updateTangent(tangentIndex, targetPosition, rotate=True, scale=True, rotateLock=True, scaleLock=True)`→ `tdu.Position`:
Modify the vertex vertex to the new [position](https://docs.derivative.ca/Position_Class "Position Class"), constraining either rotation or scale. Locked controls matching tangent. Returns resulting position.

`deleteAnchor(anchorIndex)`→ `None`:
Deletes the anchor and its neighbouring tangents.
