---
url: https://docs.derivative.ca/Connector_Class
category: Python
title: Connector_Class
---

# Connector Class

The Connector class describes the input or output connection point of an [operator](OP_Class.md#Connection "OP Class"). There are two types of connections: those between Components, and those between regular operators. Connections between regular operators can be accessed through the [OP.inputConnectors](OP_Class.md#Connection "OP Class") and [OP.outputConnectors](OP_Class.md#Connection "OP Class") members. These are the connectors on the left and right sides of [Operators](../General/Operator.md "Operator"). Connections between components can be accessed through the [COMP.inputCOMPConnectors](COMP_Class.md#Connection "COMP Class") and [COMP.outputCOMPConnectors](COMP_Class.md "COMP Class") members. These are the connectors on the top and bottom of [Component](../Glossary/Component.md "Component") operators

## Members

`index` → `int` **(Read Only)** :

The numeric index of this connector.

`isInput` → `bool` **(Read Only)** :

True when the connector is an input.

`isOutput` → `bool` **(Read Only)** :

True when the connector is an output.

`inOP` → `OP` **(Read Only)** :

Will return any input operators (e.g. [inSOP](../SOPs/In_SOP_Class.md "InSOP Class"), [inCHOP](../CHOPs/In_CHOP_Class.md "InCHOP Class")) associated with this connector. This only applies to regular operator connections attached to components.

`outOP` → `OP` **(Read Only)** :

Will return any output operators (e.g. [outSOP](../SOPs/Out_SOP_Class.md "OutSOP Class"), [outCHOP](../CHOPs/Out_CHOP_Class.md "OutCHOP Class")) associated with this connector. This only applies to regular operator connections attached to components.

`owner` → `OP` **(Read Only)** :

The [OP](OP_Class.md "OP Class") to which this object belongs.

`connections` → `list` **(Read Only)** :

The list of connector objects connected to this object.

`description` → `str` **(Read Only)** :

A description for this connection. Example: 'Color Image'.

## Methods

`connect(target)`→ `None`:

Wire this connector to a target location. The target may be an [operator](OP_Class.md "OP Class") or another connector.

When the connector is an input, its connection is replaced with the target. When the connector is an output, a new connection is appended to the target.
  * target - The OP or connector you want to connect to.

```
# connect noise1 to lag1
op('noise1').outputConnectors[0].connect(op('lag1'))

# connect choptotop1 to 2nd input of displace1
op('choptotop1').outputConnectors[0].connect(op('displace1').inputConnectors[1])

# connect geo1 to geo2, two equivalent methods:
op('geo1').outputCOMPConnectors[0].connect(op('geo2'))
op('geo2').inputCOMPConnectors[0].connect(op('geo1'))
```

`disconnect()`→ `None`:

Disconnect this connector.

```
op('lag1').inputConnectors[0].disconnect()
op('lag1').outputConnectors[0].disconnect()

# disconnect geo2 from geo1, two equivalent methods
op('geo1').outputCOMPConnectors[0].disconnect()
op('geo2').inputCOMPConnectors[0].disconnect()
```
