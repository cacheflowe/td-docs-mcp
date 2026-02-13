---
url: https://docs.derivative.ca/Sequence_Class
category: Python
title: Sequence_Class
---

# Sequence Class
An object describing and controlling a set of [sequential parameters](https://docs.derivative.ca/Sequential_Parameters "Sequential Parameters"). Accessed via
  * the `sequence` member of [parameters](https://docs.derivative.ca/Par_Class "Par Class")
  * `OP.seq` [Sequence Collection](https://docs.derivative.ca/SequenceCollection_Class "SequenceCollection Class") - the set of sequences of an object.
  * `me.curSeq` in a parameter expression

```
mySequence = op('/add1').par.point0weight.sequence	# get the sequence object
alsoMySequence = op('/add1').seq.point				# another way to get the sequence object

# A sequence block is a SequenceBlock object, which gives access to one set of parameters in the sequence.
print(len(seq))									# number of sequence blocks in the sequence
print(seq[0])									# first sequence block in the sequence
for parBlock in seq:
	print([par for par in parBlock])			# print all sequence blocks
seq.numBlocks += 1							    # add a new sequence block (same as pressing + in the UI)

# Example 2
# Examine siblings of a constant CHOP sequence

n = op('/project1/constant1')
p = n.par.const2name
p.sequenceBlock.par.name  # const2name
p.sequenceBlock.par.value  # const2value

# Example 3
# add a sequence with a float and an int parameter
base = op('/project1/base1')
page = base.appendCustomPage('Custom')
page.appendSequence('Numbers') # add a sequence parameter. Sequence object automatically has the same name
page.appendFloat('F')
page.appendInt('I')
base.seq.Numbers.blockSize = 2 # include the 2 parameter groups in the sequence

```

See also: [Sequential Parameters](https://docs.derivative.ca/Sequential_Parameters "Sequential Parameters"), [SequenceBlock Class](https://docs.derivative.ca/SequenceBlock_Class "SequenceBlock Class"), [SequenceCollection Class](https://docs.derivative.ca/SequenceCollection_Class "SequenceCollection Class")

## Members
`blockSize` → `int` :
Get or set the sequence blocksize, which is the number of [ParGroups](https://docs.derivative.ca/ParGroup "ParGroup") in the block. Changing this will add ParGroups to or remove ParGroups from the sequence.

`blocks` → `list[SequenceBlock]` **(Read Only)** :
The set of all blocks in this sequence. A block is a set of parameters which can be repeated in an operator. See [SequenceBlock](https://docs.derivative.ca/SequenceBlock_Class "SequenceBlock Class") class.

`maxBlocks` → `int | None` **(Read Only)** :
The maximum number of blocks allowed in the sequence, or None if limitless.

`name` → `str` :
Get or set the sequence name, which affects all its parameter names.

`blockName` → `str` **(Read Only)** :
Get the base name of the block name parameter. By default this is 'blockname' for builtin sequences and 'Blockname' for custom sequences.

`numBlocks` → `int` :
Get or set the total number of parameter blocks in this sequence.

`owner` → `OP` **(Read Only)** :
The OP to which this object belongs.

`blockPars` → `list` **(Read Only)** :
An intermediate parameter collection object, from which specific sequence parameters can be found.
Returns a list of one parameter from each block.

```
n.seq.Info.blockPars.Tx
n.seq.Info.blockPars.Tx[3] #Par from 4th block.

```

```
n.seq.Info.blockPars['Tx'] #returns None if not found.

```

`blockParGroups` → `list` **(Read Only)** :
An intermediate parGroup collection object, from which specific sequence parameter groups can be found.
Returns a list of one parGroup from each block.

```
n.seq.Info.blockParGroups.T
n.seq.Info.blockParGroups.T[3] #ParGroup from 4th block.

```

```
n.seq.Info.blockParGroups['T'] #returns None if not found.

```

`sequencePar` → `Par` **(Read Only)** :
The main sequence parameter defining this sequence.
## Methods
`[block index]`→ `SequenceBlock`:
[Sequence blocks](https://docs.derivative.ca/SequenceBlock_Class "SequenceBlock Class") may be easily accessed using the `[]` subscript and assignment operators.
  * block index - The index of the desired block.

`destroyBlock(block)`→ `None`:
Destroy the block of parameters at the given location.
  * block - The index of the existing block to destroy.

`insertBlock(block : SequenceBlock)`→ `SequenceBlock`:
Insert a block of parameters at the given location.
  * block - The index of the new block to insert.

Returns the newly created block.

`moveBlock(blockFrom, blockTo, num=1)`→ `None`:
Move one or more blocks of parameters to the given location.
  * blockFrom - The index or name of the new block to move. SequenceBlock objects also accepted.
  * blockTo - The index or name of the new block to move. SequenceBlock objects also accepted.
  * num - (Keyword, Optional) The number of blocks to move.

`reorderBlocks(*indexes : int)`→ `None`:
Reorder the specified blocks, leaving the rest in place.
  * indexes - Integer indexes of the blocks to reorder, in their new order.

```
n.seq.Info.reorderBlocks(1,0)
# swaps position of first two blocks

```

`sortBlocks(key=lambda Block, baseName="", reverse=False)`→ `None`:
Sorts the blocks based on the given `key` function or `baseName` parameter. If both are provided, an exception will be raised.
  * key - A function that is passed every block in the sequence and which returns a sortable value. By default it evaluates the block's name parameter, if defined, otherwise it sorts by the first parameter of the block.
  * baseName - If specified, sort by the values of the parameter with this name.
  * reverse - If True, reverses the order of the sort.

```
n.seq.Info.sortBlocks(reverse=True) # just reverse current order
n.seq.Info.sortBlocks(baseName='Value') # sort by the evaluation of <code>Value</code> parameters in each block
n.seq.Info.sortBlocks(key=lambda block: block.par.Key) # sort by the evaluation of <code>Key</code> parameters in each block
n.seq.Info.sortBlocks(key=lambda block: block.par.X + block.par.Y) # sort on the sum of X and Y parameters in each block
n.seq.Info.sortBlocks(key=lambda block: (block.par.X, block.par.Y)) # sort by X parameter, then Y parameter within that.

```

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.
