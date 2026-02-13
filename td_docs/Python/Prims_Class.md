---
url: https://docs.derivative.ca/Prims_Class
category: Python
title: Prims_Class
---

# Prims Class
The Prims class describes the set of [prim objects](https://docs.derivative.ca/Prim_Class "Prim Class") (primitives) owned by one [SOP](https://docs.derivative.ca/SOP_Class "SOP Class").

## Members
`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.
## Methods
No operator specific methods.
###  Special Functions
`len(Prims)`→ `int`:
Returns the total number of prims.

```
a = len(op('box1').prims)

```

`[index]`→ `td.Prim`:
Get a specific prim given an integer index.

```
n = op('box1').prims[0]

```

`Iterator`→ `td.Prim`:
Iterate over each prim.

```
for m in op('box1').prims:
	# do something with m, which is a Prim

```
