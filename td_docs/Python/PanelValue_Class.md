---
url: https://docs.derivative.ca/PanelValue_Class
category: Python
title: PanelValue_Class
---

# PanelValue Class

A PanelValue describes an instance to a [Panel Value](../Glossary/Panel_Value.md "Panel Value"). They can be accessed through a component's [panel](../Glossary/Panel.md "Panel") member, and are used in the [Panel Execute DAT](../Glossary/Panel_Execute_DAT.md "Panel Execute DAT").

For a list of available panel values, see: [Panel Value](../Glossary/Panel_Value.md "Panel Value").

## Members

`name` → `str` **(Read Only)** :

The name of the panel value. See [Panel Value](../Glossary/Panel_Value.md "Panel Value") for the list of possible names. name is a string.

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

`val` → `Any` :

Get or set the panel value.

`valid` → `bool` **(Read Only)** :

True if the referenced panel value currently exists, False if it has been deleted.

## Methods

No operator specific methods.

###  Casting to a Value

The PanelValue Class implements all necessary methods to be treated as a number or string, which in this case gets or sets its value. Therefore, an explicit call to eval() or set() is unnecessary when used in a parameter, or in a numeric expression. For example, the following are equivalent in a parameter:

```
(float)parent().panel.u
parent().panel.u.val
parent().panel.u

# the following are also equivalent
parent().panel.u.val + 1
parent().panel.u + 1

# as are the following
parent().panel.u.val = 0.5
parent().panel.u = 0.5
```

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").
