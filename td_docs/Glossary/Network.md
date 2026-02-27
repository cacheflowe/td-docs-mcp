---
url: https://docs.derivative.ca/Network
category: Glossary
title: Network
---

# Network
[![](https://docs.derivative.ca/images/thumb/b/b4/NetworkExample.jpg/400px-NetworkExample.jpg)](https://docs.derivative.ca/File:NetworkExample.jpg)
[](https://docs.derivative.ca/File:NetworkExample.jpg "Enlarge")
A TouchDesigner network
A network is a group of inter-connected [Nodes](https://docs.derivative.ca/Node "Node") of [Operators](https://docs.derivative.ca/Operator "Operator") in one [Component](https://docs.derivative.ca/Component "Component"). Every component contains a network, and every network lives in a component.
Network nodes are connected by colored [wires](https://docs.derivative.ca/Wire "Wire") showing the data flow from operator to operator of the same family (e.g. CHOP to CHOP), each operator cooking its inputs and generating its output.
Some network elements may not be directly wired. Dashed straight gray lines indicate other data references:
  * A [Python](https://docs.derivative.ca/Python "Python") expression in a [parameter](https://docs.derivative.ca/Parameter "Parameter") that refers to another operator.
  * A CHOP channel [exports](https://docs.derivative.ca/Export "Export") to a parameter of another operator.
  * A parameter contains the [path](https://docs.derivative.ca/Network_Path "Network Path") to another operator.

Components contain their own networks that use their input nodes (In OPs) to generate its output (Out OPs).
Some nodes may be referenced by scripts in DATs, between which where no connecting lines are drawn.
Generally, nodes are wired together with data flowing from left to right.


See also: [Network Editor](https://docs.derivative.ca/Network_Editor "Network Editor"), [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
