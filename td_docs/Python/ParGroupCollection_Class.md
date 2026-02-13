---
url: https://docs.derivative.ca/ParGroupCollection_Class
category: Python
title: ParGroupCollection_Class
---

# ParGroupCollection Class
The ParGroupCollection class can be used to access [ParGroups](https://docs.derivative.ca/ParGroup_Class "ParGroup Class"). To access a parGroup you need to use its internal name, which you can obtain by hovering your mouse over the parameter name, and looking at the popup that will come up. See also [ParGroup Class](https://docs.derivative.ca/ParGroup_Class "ParGroup Class"). An operator's instance of this can be found in `OP.parGroup`.

## Members
This object contains a member for each parGroup in the component. You can both read the value using:

```
a = op('geo1').par.t

```

You can also change the value using

```
a = op('geo1').parGroup.tx = (1,1,1) # transform has 3 values
a = op('geo1').parGroup.lookat = 'null1'

```

`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.
## Methods
`[name]`→ `Par`:
[ParGroups](https://docs.derivative.ca/ParGroup_Class "ParGroup Class") may be easily accessed using the [] subscript and assignment operators.
  * name - Must be an exact string name. Wildcards are not supported. If not found None is returned.

```
p = op('base1').parGroup['Myfloat5']

```

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
