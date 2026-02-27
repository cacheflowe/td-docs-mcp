---
url: https://docs.derivative.ca/Procedural
category: Glossary
title: Procedural
---

# Procedural

Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. [Dependency](https://docs.derivative.ca/Dependency "Dependency") is the procedural mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](https://docs.derivative.ca/Cook "Cook"). This assures all data is consistent in a TouchDesigner process, and causes all the output displays, UIs, devices and protocols to update in realtime.

TouchDesigner is both a "**pull system** " and a "**push system** ". The pull system is the procedural part, as data is generated, modified and pulled toward the outputs such as displays, audio devices, network streams and devices. The push system is based on [Events](https://docs.derivative.ca/Event "Event") coming from user inputs, external devices and software, and internally-generated events. Events usually cause changes to parameters, DAT tables and python data structures, which then affects the procedural data being generated when pulls happen, usually once per timeline frame.

####  Automatic Dependency

If there is a change in an operator's output data or parameter value, it causes other operators downstream from it to cook. Downstream means operators that are connected to the output of a changed node, and operators (or their parameters) that refer to the changed operator (often visible as the dashed-lines in a network).

####  Python Data Dependency

Because Python does not inherently have a procedural mechanism, [Dependency Objects](https://docs.derivative.ca/Dependency_Class "Dependency Class") in TouchDesigner allow python data to cause downstream cooking when that data is changed.

See [Dependency_Class](https://docs.derivative.ca/Dependency_Class "Dependency Class") for how to set up Python Dependency. To create recursively dependable Python collections, see [Deeply Dependable Collections](https://docs.derivative.ca/TDStoreTools#Deeply_Dependable_Collections "TDStoreTools").

See also [Event](https://docs.derivative.ca/Event "Event").

Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. It is the chain-reaction mechanism of TouchDesigner, where if one piece of data changes, it automatically causes other "[dependent](https://docs.derivative.ca/Dependency "Dependency")" operators and expressions to re-[Cook](https://docs.derivative.ca/Cook "Cook") and re-generate the outputs.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

is the Procedural mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](https://docs.derivative.ca/Cook "Cook").
