---
url: https://docs.derivative.ca/Sequential_Parameters
category: Glossary
title: Sequential_Parameters
---

# Sequential Parameters

##  The Basics

Sequential Parameters are blocks of parameters (**Sequence Blocks**) that can be reproduced multiple times by a user to create multiple entities. For example, the [Constant CHOP](../CHOPs/Constant_CHOP.md "Constant CHOP") lets you create multiple channels by clicking the + button in the parameter dialog. The Point POP lets you create multiple points, etc.

( See "Creating Custom Sequential Parameters" at the end of this page to create your own sequential blocks. )

All parameter sequences start with a sequence header parameter with a + and - button, followed by one or more "blocks" of parameters. The image below shows the parameter dialog for [Add SOP](../SOPs/Add_SOP.md "Add SOP")'s Points page. The sequence header has the label "Point", and is followed by two sequence blocks, each block containing a Position and a Weight parameter.
[![Seqpars.png](https://docs.derivative.ca/images/7/72/Seqpars.png)](https://docs.derivative.ca/File:Seqpars.png)
The parameters in sequence blocks are named in the form:      `<sequence name><sequence index><parameter name>`
  * _sequence name_ : the sequence name, which is also the name of the sequence's header parameter
  * _block index_ : the zero-based index of the block in the sequence
  * _parameter name_ : the descriptive name of the parameter

In the example below, the sequence parameters are expanded to show their Python names. The sequence name is "point".
[![Expanded seq.png](https://docs.derivative.ca/images/5/59/Expanded_seq.png)](https://docs.derivative.ca/File:Expanded_seq.png)
You can add and remove sequential parameter blocks in multiple ways. The + and - buttons in the header add and remove sequence blocks respectively. You can also choose Insert Block or Remove Block in the RMB menu after right-clicking on a block parameter's name in the parameter dialog. Lastly, you can use Python (see Python section below)

###  Sequence Helpers for Parameter Expressions

In a parameter expression, you can use:
  * `me.curSeq` to access the [sequence](../Python/Sequence_Class.md "Sequence Class") of the parameter currently being evaluated.
  * `me.curSeq.numBlocks` to access the number of blocks in the sequence of the parameter currently being evaluated. `len(me.curSeq)` works too.
  * `me.curBlock` to access the [sequence block](../Python/SequenceBlock_Class.md "SequenceBlock Class") of the parameter currently being evaluated.
  * With that you can refer to any other parameter in the block, for example, `me.curBlock.par.posz`, not needing to specify the sequence name or block number.

Below are some examples:
[![CurBlock.png](https://docs.derivative.ca/images/2/2c/CurBlock.png)](https://docs.derivative.ca/File:CurBlock.png)
See what else you can use here: [Sequence Class](../Python/Sequence_Class.md "Sequence Class"), [SequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class"), [SequenceCollection Class](../Python/SequenceCollection_Class.md "SequenceCollection Class").

##  Working with Sequential Parameters in Python

There are a number of utility classes, members, and methods that allow you to work with sequential parameters in Python. This section will give an overview of these features, but for detailed documentation please refer to: [Sequence Class](../Python/Sequence_Class.md "Sequence Class"), [SequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class"), [SequenceCollection Class](../Python/SequenceCollection_Class.md "SequenceCollection Class")

###  Sequence Objects

**[Sequence objects](../Python/Sequence_Class.md "Sequence Class")** are the main interface for interacting with parameter sequences in Python. They can be accessed via the `sequence` member of any parameter in a sequence or via the sequence name and **[seq](../Python/SequenceCollection_Class.md "SequenceCollection Class")** member of operators.
```
mySequence = op('/add1').par.point0posx.sequence	# get the sequence object
sameSequence = op('/add1').seq.point				# another way to get the sequence object
```

Every sequence has a unique **sequence name**. This name is used to identify the sequence and to prefix the names of all block parameters. It is also the name of the sequence header parameter. You can find the sequence name by hovering over the sequence header's label or by looking at the block parameter names. It is also stored in the sequence object's `name` member.

###  Sequence Blocks

**[Sequence blocks](../Python/SequenceBlock_Class.md "SequenceBlock Class")** are the blocks of parameters that are repeated in parameter sequences. The blocks in a sequence can be accessed and controlled using through the Sequence object. The following examples use the `point` sequence shown in the ADD SOP images above.
```
seq = op('/add1').seq.point				# get the sequence object with the name "point"
alsoSeq = op('/add1').seq['point']		# you can also use bracket notation
allBlocks = seq.blocks					# list of all sequence blocks
count = len(seq)						# number of sequence blocks
firstBlock = seq[0]						# first block in the sequence
print(firstBlock.index)					# print the parameter block's index within the sequence. 0 in this case
```

You can also use the sequece object to control the number of blocks in the sequence:
```
seq.numBlocks = 4						# set the number of blocks to 4
seq.insertBlock(2)						# insert a block at position 2
seq.destroyBlock(0)						# destroy the first block
```

Sequence blocks provide easy access to the parameters within the block, using the familiar `par[](../Python/ParCollection_Class.md "ParCollection Class")` and `parGroup[](../Python/ParGroupCollection_Class.md "ParGroupCollection Class")` collection classes. Note that when accessing parameters from a sequence block, you use their base names (no sequence prefix) instead of their full names. The examples below illustrate this, again using the Add SOP images above:
```
seq = op('/add1').seq.point				# get the sequence object with the name "point"
block = seq[1]							# second block in the sequence

block.par.weight = 3					# access the block's "weight" parameter. Its actual name is "point1weight"
block.par['weight'] = 4					# you can also use bracket notation
block.parGroup.pos = [1,1,1]			# access the block's "pos" parameter group.
```

###  Parameters in Sequence Blocks

Three ways to get a parameter in a sequence.
```
op('add1').par.point1posx                # normal
op('add1').seq.point[1].par.point1posx   # by block index
op('add1').seq.point[1].par.posx         # simplest, by block index
```

There are a number of ways to iterate through a given parameter in each block:
```
seq = op('add1').seq.point

# print the value of all weight parameters

# using Sequence.blocks
for block in seq.blocks:
	print(block.par.weight)

# using Sequence[blockIndex]
for index in range(len(seq)):
	print(seq[index].par.weight.eval())

# using Sequence.blockPars:
for weightPar in seq.blockPars.weight:
	print(weightPar.eval())
```

###  Sequence Helper Members in Parameters and ParGroups

There are a few helper members to work with sequences, built directly into parameters and parGroups:
```
# parameter helpers
par = op('/add1').par.point0weight
print(par.sequence)						# prints the sequence object. Will be None if the parameter is not in a sequence

# parGroup helpers
parGroup = op('/add1').parGroup.point1pos
print(parGroup.sequence)				# prints the sequence object. Will be None if the parGroup is not in a sequence
print(parGroup.sequenceIndex)			# prints the index of the parGroup's sequence block within the sequence. 1 in this case
print(parGroup.blockIndex)				# prints the index of the parGroup within its block. 0 in this case (it is the first par in the block)
```

#  Creating Custom Sequential Parameters

You can create custom sequential parameters on your components using the [Component Editor](https://docs.derivative.ca/Component_Editor_Dialog "Component Editor Dialog"). You can create a sequence in two ways:

###  Method One

  1. Create a Sequence parameter, which creates the sequence header
  2. Create the block parameters you want below the Sequence parameter
  3. Change the Sequence parameter's `numBlocks` to the number of block parameters you created

###  Method Two

  1. Create the block parameters you want
  2. Select the block parameters
  3. Right-click on one of the selected parameters and choose Create Sequence

###  Adding and Removing Parameters from the Sequence

There are a few ways to add or remove parameters from a sequence:
  * Drag them into or out of the sequence.
  * Select them in the parameter list and choose Add To Sequence or Remove From Sequence in the RMB menu.
  * Change the `numBlocks` member of the Sequence header parameter.

###  Referring to Another Block

Referring to another block in your sequence, where blocks may be re-ordered, deleted or inserted requires something invariant in blocks. For example, `me.curSeq[3]` will become `me.curSeq[2]` if you delete any of the prior blocks 0, 1 or 2.

However if you create a parameter (numeric or string) in a block specifically called `Blockname`, then for each new block, its value is automatically appended with a unique number. If for example the first `Blockname` in a block has been set to `A7`, then next block will contain a blockname set to `A8` etc. To get that block any time in the future, you can index it directly by name: `me.curSeq['A7']` and to get to a parameter of that block, it is simply `me.curSeq['A7'].par.Speed`, for example.

If you make the original parameter of the block Read-only, then any newly-created `Blockname` parameters will also be read-only, which is preferable as you don't want anyone accidentally changing it.

Sequential Parameters are blocks of parameters (Sequential Blocks) that can be reproduced multiple times by a user to create multiple entities.

Sequential Parameters are blocks of parameters (Sequential Blocks) that can be reproduced multiple times by a user to create multiple entities.

Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
