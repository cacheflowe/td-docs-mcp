---
url: https://docs.derivative.ca/AttributeData_Class
category: Python
title: AttributeData_Class
---

# AttributeData Class
An AttributeData contains specific geometric [Attribute](https://docs.derivative.ca/Attribute "Attribute") values, associated with a [Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), or [Vertex Class](https://docs.derivative.ca/Vertex_Class "Vertex Class"). Each value of the attribute must be of the same type, and can be one of float, string or integer. For example, a point or vertex normal attribute data, consists of 3 float values.

## Members
`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.

`val` → `float | int | str | tuple | TDU.Position[](https://docs.derivative.ca/Position_Class "Position Class") | TDU.Vector[](https://docs.derivative.ca/Vector_Class "Vector Class")` **(Read Only)** :
The set of values contained within this object. Dependent on the type of attribute, it may return a float, integer, string, tuple, [Position](https://docs.derivative.ca/Position_Class "Position Class"), or [Vector](https://docs.derivative.ca/Vector_Class "Vector Class"). For example Normal attribute data is expressed as a [Vector](https://docs.derivative.ca/Vector_Class "Vector Class"), while [Position](https://docs.derivative.ca/Position_Class "Position Class") attribute data is expressed as a Position.
## Methods
No operator specific methods.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
