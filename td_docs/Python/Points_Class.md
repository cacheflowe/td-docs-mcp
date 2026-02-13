---
url: https://docs.derivative.ca/Points_Class
category: Python
title: Points_Class
---

# Points Class
The Points class describes the set of [point objects](https://docs.derivative.ca/Point_Class "Point Class") owned by one [SOP](https://docs.derivative.ca/SOP_Class "SOP Class").

## Members
`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.
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
