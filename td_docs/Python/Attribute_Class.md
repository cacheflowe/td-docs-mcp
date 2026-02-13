---
url: https://docs.derivative.ca/Attribute_Class
category: Python
title: Attribute_Class
---

# Attribute Class
An [Attribute](https://docs.derivative.ca/Attribute "Attribute") describes a general geometric Attribute, associated with a [Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), or [Vertex Class](https://docs.derivative.ca/Vertex_Class "Vertex Class"). Specific values for each Prim, Point or Vertex are described with the [AttributeData Class](https://docs.derivative.ca/AttributeData_Class "AttributeData Class"). Lists of attributes for the [SOP](https://docs.derivative.ca/SOP_Class "SOP Class") are described with the [Attributes Class](https://docs.derivative.ca/Attributes_Class "Attributes Class").

## Members
`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.

`name` → `str` **(Read Only)** :
The name of this attribute.

`size` → `int` **(Read Only)** :
The number of values associated with this attribute. For example, a normal attribute has a size of 3.

`type` → `float | int | str | tuple | TDU.Position[](https://docs.derivative.ca/Position_Class "Position Class") | TDU.Vector[](https://docs.derivative.ca/Vector_Class "Vector Class")` **(Read Only)** :
The type associated with this attribute: float, integer, string, tuple, [Position](https://docs.derivative.ca/Position_Class "Position Class"), or [Vector](https://docs.derivative.ca/Vector_Class "Vector Class").

`default` → `float | int | str | tuple | TDU.Position[](https://docs.derivative.ca/Position_Class "Position Class") | TDU.Vector[](https://docs.derivative.ca/Vector_Class "Vector Class")` **(Read Only)** :
The default values associated with this attribute. Dependent on the type of attribute, it may return a float, integer, string, tuple, [Position](https://docs.derivative.ca/Position_Class "Position Class"), or [Vector](https://docs.derivative.ca/Vector_Class "Vector Class").

`isArray` → `bool` **(Read Only)** :
True if the attribute is an an array.

`arraySize` → `int` **(Read Only)** :
The size of the array for array attributes, 0 otherwise.

`numMatCols` → `int` **(Read Only)** :
The number of columns for matrix attributes, 0 otherwise.

`numMatRows` → `int` **(Read Only)** :
The number of rows for matrix attributes, 0 otherwise.
## Methods
`destroy()`→ `None`:
Destroy the attribute referenced by this object.

```
n = scriptOP.pointAttribs['N'].destroy()

```

`vals(delayed=False)`→ `list`:
Returns the attribute values as a list.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.

###  Accessing Attributes
See [Attributes](https://docs.derivative.ca/Attributes_Class "Attributes Class") for examples on how to access individual attributes.

A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes.
