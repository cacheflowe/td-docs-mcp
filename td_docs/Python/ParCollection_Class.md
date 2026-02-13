---
url: https://docs.derivative.ca/ParCollection_Class
category: Python
title: ParCollection_Class
---

# ParCollection Class
The ParCollection class can be used to access [Parameters](https://docs.derivative.ca/Par_Class "Par Class"). To access a parameter you need to use its internal name, which you can obtain by hovering your mouse over the parameter name, and looking at the popup that will come up. See also [Par Class](https://docs.derivative.ca/Par_Class "Par Class"). An operator's instance of this can be found in `OP.par`.

## Members
This object contains a member for each parameter in the component. You can both read the value using:

```
a = op('geo1').par.tx

```

You can also change the value using

```
a = op('geo1').par.tx = 4
a = op('geo1').par.lookat = 'null1'

```

`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.
## Methods
`[name]`→ `Par`:
[Parameters](https://docs.derivative.ca/Par_Class "Par Class") may be easily accessed using the [] subscript and assignment operators.
  * name - Must be an exact string name. Wildcards are not supported. If not found None is returned.

```
p = op('base1').par['Myfloat5']

```
