---
url: https://docs.derivative.ca/SequenceCollection_Class
category: Python
title: SequenceCollection_Class
---

# SequenceCollection Class
The SequenceCollection class can be used to access sequences by name.

```
	myOperator.seq.Color #raises Exception if not found.
	# or
	myOperator.seq['Color'] #returns None if not found.

```

## Members
`owner` → `OP` **(Read Only)** :
The OP to which this object belongs.
## Methods
No operator specific methods.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
