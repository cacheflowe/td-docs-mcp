---
url: https://docs.derivative.ca/SequenceBlock_Class
category: Python
title: SequenceBlock_Class
---

# SequenceBlock Class
The SequenceBlock class can be used to access the parGroups of a specific block (set of parGroups) in a sequence.

```
block = op('/add1').seq.point[3] # get the fourth block from the sequence named "iop"
print([parGroup for parGroup in block]) # print all the parGroups in the block

```

**Note:** use the parameter name _without_ the sequence prefix.

## Members
`index` → `int` **(Read Only)** :
The numeric index of the block.

`owner` → `OP` **(Read Only)** :
The OP to which this object belongs.

`par` → `ParCollection` **(Read Only)** :
An intermediate parameter collection object, from which a specific sequence parameter can be found.
Names do not include sequence info prefix.

```
n.seq.Info.blocks[2].par.Tx # raises exception if not found

```

```
n.seq.Info.blocks[2].parGroup['Tx'] #returns None if not found

```

`parGroup` → `ParGroupCollection` **(Read Only)** :
An intermediate parameter collection object, from which a specific sequence parameter group can be found.
Names do not include sequence info prefix.

```
n.seq.Info.blocks[2].par.T # raises exception if not found

```

```
n.seq.Info.blocks[2].parGroup['T'] #returns None if not found

```

`name` → `str` :
Get or set the sequence block name parameter value. This is implemented as a specifically named parameter in each block. The name is also used to identify a block by string via Sequence[<block name>].

`namePar` → `Par | None` **(Read Only)** :
The parameter defining the name for this block, or None if there isn't one.

`sequence` → `Sequence` **(Read Only)** :
The sequence object this block belongs to.
## Methods
`destroy()`→ `None`:
Destroy the block of parameters.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
