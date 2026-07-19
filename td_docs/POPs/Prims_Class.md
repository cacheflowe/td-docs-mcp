---
url: https://docs.derivative.ca/Prims_Class
category: POPs
title: Prims_Class
---

# Prims Class

The Prims class describes the set of [prim objects](../Python/Prim_Class.md "Prim Class") (primitives) owned by one [SOP](../SOPs/SOP_Class.md "SOP Class").

## Members

`owner` → `OP` **(Read Only)** :

The [OP](../Python/OP_Class.md "OP Class") to which this object belongs.

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
