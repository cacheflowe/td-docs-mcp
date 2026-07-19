---
url: https://docs.derivative.ca/Group_Class
category: Python
title: Group_Class
---

# Group Class

An Group describes groups lists of [Prim Class](Prim_Class.md "Prim Class") or [Point Class](../SOPs/Point_Class.md "Point Class").

A Group can be created with the [Group SOP](../SOPs/Group_SOP.md "Group SOP") or using the `createPointGroup(str)` or `createPrimGroup(str)` methods of the [ScriptSOP Class](../SOPs/Script_SOP_Class.md "ScriptSOP Class").

## Members

`default` → `tuple` **(Read Only)** :

The default values associated with this Group. It returns a tuple item of group points.

`name` → `str` :

Set/gets the group name.

`owner` → `OP` **(Read Only)** :

Gets the owner of this group.

## Methods

`add(item : Point[](../SOPs/Point_Class.md "Point Class") | Prim[](Prim_Class.md "Prim Class") | int)`→ `None`:
Adds a point/primitive to this group. The point or primitive to be added can be specified by a point, primitive object or the index of a point or primitive object.

`discard(item : Point[](../SOPs/Point_Class.md "Point Class") | Prim[](Prim_Class.md "Prim Class") | int)`→ `None`:
Removes a point/primitive from this group. The point or primitive to be removed can be specified by a point, primitive object or the index of a point or primitive object.

`destroy()`→ `None`:

Destroys the current point/primitive group.

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").
