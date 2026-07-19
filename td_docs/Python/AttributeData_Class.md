---
url: https://docs.derivative.ca/AttributeData_Class
category: Python
title: AttributeData_Class
---

# AttributeData Class

An AttributeData contains specific geometric [Attribute](../Glossary/Attribute.md "Attribute") values, associated with a [Prim Class](Prim_Class.md "Prim Class"), [Point Class](../SOPs/Point_Class.md "Point Class"), or [Vertex Class](Vertex_Class.md "Vertex Class"). Each value of the attribute must be of the same type, and can be one of float, string or integer. For example, a point or vertex normal attribute data, consists of 3 float values.

## Members

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

`val` → `float | int | str | tuple | TDU.Position[](Position_Class.md "Position Class") | TDU.Vector[](Vector_Class.md "Vector Class")` **(Read Only)** :
The set of values contained within this object. Dependent on the type of attribute, it may return a float, integer, string, tuple, [Position](Position_Class.md "Position Class"), or [Vector](Vector_Class.md "Vector Class"). For example Normal attribute data is expressed as a [Vector](Vector_Class.md "Vector Class"), while [Position](Position_Class.md "Position Class") attribute data is expressed as a Position.

## Methods

No operator specific methods.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").
