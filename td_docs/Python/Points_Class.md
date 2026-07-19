---
url: https://docs.derivative.ca/Points_Class
category: Python
title: Points_Class
---

# Points Class

The Points class describes the set of [point objects](../SOPs/Point_Class.md "Point Class") owned by one [SOP](../SOPs/SOP_Class.md "SOP Class").

## Members

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

## Methods

No operator specific methods.

###  Special Functions

`len(Points)`→ `int`:

Returns the total number of points.

```
a = len(op('box1').points)
```

`[index]`→ `td.Point`:

Get a specific point given an integer index.

```
n = op('box1').points[0]
```

`Iterator`→ `td.Point`:

Iterate over each point.

```
for m in op('box1').points:
	# do something with m, which is a Point
```
