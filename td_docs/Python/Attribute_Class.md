---
url: https://docs.derivative.ca/Attribute_Class
category: Python
title: Attribute_Class
---

# Attribute Class

An [Attribute](../Glossary/Attribute.md "Attribute") describes a general geometric Attribute, associated with a [Prim Class](Prim_Class.md "Prim Class"), [Point Class](../SOPs/Point_Class.md "Point Class"), or [Vertex Class](Vertex_Class.md "Vertex Class"). Specific values for each Prim, Point or Vertex are described with the [AttributeData Class](AttributeData_Class.md "AttributeData Class"). Lists of attributes for the [SOP](../SOPs/SOP_Class.md "SOP Class") and [POP](POP_Class.md "POP Class") are described with the [Attributes Class](Attributes_Class.md "Attributes Class").

## Members

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

`name` → `str` **(Read Only)** :

The name of this attribute.

`size` → `int` **(Read Only)** :

The number of values associated with this attribute. For example, a normal attribute has a size of 3.

`type` → `float | int | str | tuple | TDU.Position[](Position_Class.md "Position Class") | TDU.Vector[](Vector_Class.md "Vector Class")` **(Read Only)** :
The type associated with this attribute: float, integer, string, tuple, [Position](Position_Class.md "Position Class"), or [Vector](Vector_Class.md "Vector Class").

`default` → `float | int | str | tuple | TDU.Position[](Position_Class.md "Position Class") | TDU.Vector[](Vector_Class.md "Vector Class")` **(Read Only)** :
The default values associated with this attribute. Dependent on the type of attribute, it may return a float, integer, string, tuple, [Position](Position_Class.md "Position Class"), or [Vector](Vector_Class.md "Vector Class").

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

Returns the attribute values as a list for POPs.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.

###  Accessing Attributes

See [Attributes](Attributes_Class.md "Attributes Class") for examples on how to access individual attributes.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
