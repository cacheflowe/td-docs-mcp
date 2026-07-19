---
url: https://docs.derivative.ca/Point_Class
category: SOPs
title: Point_Class
---

# Point Class

A Point describes an instance to a single [geometry point](../Glossary/Point.md "Point"). They are accessible through the [SOP.points](SOP_Class.md "SOP Class") member.

## Members

`index` → `int` **(Read Only)** :

The point index in the list.

`owner` → `OP` **(Read Only)** :

The [OP](../Python/OP_Class.md "OP Class") to which this object belongs.

`P` → `td.AttributeData` :

The coordinates as [AttributeData](../Python/AttributeData_Class.md "AttributeData Class"). Individual components can be read or written with the [] operator.

```
point.P[0] = 5
point.P = (1,0,1)
```

`x` → `float` :

Get or set x coordinate value. This is the same as P[0].

`y` → `float` :

Get or set y coordinate value. This is the same as P[1].

`z` → `float` :

Get or set z coordinate value. This is the same as P[2].

`normP` → `tdu.Position` **(Read Only)** :

The normalized position of this point within the bounding box of the SOP. Will always be in the range [0,1]. Expressed as tdu.Position object.

###  Attributes

In addition to the above members, all [attributes](../Python/Attribute_Class.md "Attribute Class") are members as well.

For example, if the Point contains texture coordinates, they may be accessed with:`Point.uv`

```
box = op('box1')
print(box.N[0], box.N[1], box.N[2])
print(box.uv[0], box.uv[1], box.uv[2])
```

See: [Attribute Class](../Python/Attribute_Class.md "Attribute Class") for more information.

## Methods

`destroy()`→ `None`:

Destroy and remove the actual point this object refers to. This operation is only valid when the primitive belongs to a [scriptSOP](Script_SOP_Class.md "ScriptSOP Class"). Note: after this call, other existing Point objects in this SOP may no longer be valid.
