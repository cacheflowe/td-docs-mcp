---
url: https://docs.derivative.ca/Group_Class
category: Python
title: Group_Class
---

# Group Class
An Group describes groups lists of [Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class") or [Point Class](https://docs.derivative.ca/Point_Class "Point Class").
A Group can be created with the [Group SOP](https://docs.derivative.ca/Group_SOP "Group SOP") or using the `createPointGroup(str)` or `createPrimGroup(str)` methods of the [ScriptSOP Class](https://docs.derivative.ca/ScriptSOP_Class "ScriptSOP Class").

## Members
`default` → `tuple` **(Read Only)** :
The default values associated with this Group. It returns a tuple item of group points.

`name` → `str` :
Set/gets the group name.

`owner` → `OP` **(Read Only)** :
Gets the owner of this group.
## Methods
`add(item : Point[](https://docs.derivative.ca/Point_Class "Point Class") | Prim[](https://docs.derivative.ca/Prim_Class "Prim Class") | int)`→ `None`:
Adds a point/primitive to this group. The point or primitive to be added can be specified by a point, primitive object or the index of a point or primitive object.

`discard(item : Point[](https://docs.derivative.ca/Point_Class "Point Class") | Prim[](https://docs.derivative.ca/Prim_Class "Prim Class") | int)`→ `None`:
Removes a point/primitive from this group. The point or primitive to be removed can be specified by a point, primitive object or the index of a point or primitive object.

`destroy()`→ `None`:
Destroys the current point/primitive group.
A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](https://docs.derivative.ca/Group_POP "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
