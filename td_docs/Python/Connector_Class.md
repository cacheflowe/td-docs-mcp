---
url: https://docs.derivative.ca/Connector_Class
category: Python
title: Connector_Class
---

# Connector Class
The Connector class describes the input or output connection point of an [operator](https://docs.derivative.ca/OP_Class#Connection "OP Class"). There are two types of connections: those between Components, and those between regular operators. Connections between regular operators can be accessed through the [OP.inputConnectors](https://docs.derivative.ca/OP_Class#Connection "OP Class") and [OP.outputConnectors](https://docs.derivative.ca/OP_Class#Connection "OP Class") members. These are the connectors on the left and right sides of [Operators](https://docs.derivative.ca/Operator "Operator"). Connections between components can be accessed through the [COMP.inputCOMPConnectors](https://docs.derivative.ca/COMP_Class#Connection "COMP Class") and [COMP.outputCOMPConnectors](https://docs.derivative.ca/COMP_Class "COMP Class") members. These are the connectors on the top and bottom of [Component](https://docs.derivative.ca/Component "Component") operators

## Members
`index` → `int` **(Read Only)** :
The numeric index of this connector.

`isInput` → `bool` **(Read Only)** :
True when the connector is an input.

`isOutput` → `bool` **(Read Only)** :
True when the connector is an output.

`inOP` → `OP` **(Read Only)** :
Will return any input operators (e.g. [inSOP](https://docs.derivative.ca/InSOP_Class "InSOP Class"), [inCHOP](https://docs.derivative.ca/InCHOP_Class "InCHOP Class")) associated with this connector. This only applies to regular operator connections attached to components.

`outOP` → `OP` **(Read Only)** :
Will return any output operators (e.g. [outSOP](https://docs.derivative.ca/OutSOP_Class "OutSOP Class"), [outCHOP](https://docs.derivative.ca/OutCHOP_Class "OutCHOP Class")) associated with this connector. This only applies to regular operator connections attached to components.

`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.

`connections` → `list` **(Read Only)** :
The list of connector objects connected to this object.

`description` → `str` **(Read Only)** :
A description for this connection. Example: 'Color Image'.
## Methods
`connect(target)`→ `None`:
Wire this connector to a target location. The target may be an [operator](https://docs.derivative.ca/OP_Class "OP Class") or another connector.
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
