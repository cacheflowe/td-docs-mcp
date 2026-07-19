---
url: https://docs.derivative.ca/Procedural
category: Glossary
title: Procedural
---

# Procedural

Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. [Dependency](Dependency.md "Dependency") is the procedural mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](Cook.md "Cook"). This assures all data is consistent in a TouchDesigner process, and causes all the output displays, UIs, devices and protocols to update in realtime.

TouchDesigner is both a "**pull system** " and a "**push system** ". The pull system is the procedural part, as data is generated, modified and pulled toward the outputs such as displays, audio devices, network streams and devices. The push system is based on [Events](Event.md "Event") coming from user inputs, external devices and software, and internally-generated events. Events usually cause changes to parameters, DAT tables and python data structures, which then affects the procedural data being generated when pulls happen, usually once per timeline frame.

####  Automatic Dependency

If there is a change in an operator's output data or parameter value, it causes other operators downstream from it to cook. Downstream means operators that are connected to the output of a changed node, and operators (or their parameters) that refer to the changed operator (often visible as the dashed-lines in a network).

####  Python Data Dependency

Because Python does not inherently have a procedural mechanism, [Dependency Objects](../Python/Dependency_Class.md "Dependency Class") in TouchDesigner allow python data to cause downstream cooking when that data is changed.

See [Dependency_Class](../Python/Dependency_Class.md "Dependency Class") for how to set up Python Dependency. To create recursively dependable Python collections, see [Deeply Dependable Collections](https://docs.derivative.ca/TDStoreTools#Deeply_Dependable_Collections "TDStoreTools").

See also [Event](Event.md "Event").

Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. It is the chain-reaction mechanism of TouchDesigner, where if one piece of data changes, it automatically causes other "[dependent](Dependency.md "Dependency")" operators and expressions to re-[Cook](Cook.md "Cook") and re-generate the outputs.

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

is the Procedural mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](Cook.md "Cook").
