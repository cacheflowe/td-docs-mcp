---
url: https://docs.derivative.ca/Operator
category: General
title: Operator
---

# Operator

## Summary

Operators are the "[Nodes](../Glossary/Node.md "Node")" in TouchDesigner networks, and they output data to other operators. Each operator is customized with its [Parameters](../Glossary/Parameter.md "Parameter") and [Flags](../Glossary/Flag.md "Flag").
[![Geo1.jpg](https://docs.derivative.ca/images/thumb/8/85/Geo1.jpg/200px-Geo1.jpg)](https://docs.derivative.ca/File:Geo1.jpg)
[OP Class](../Python/OP_Class.md "OP Class")

##  Operator Families

There are seven **Families** of built-in Operators. Of the seven families, six are basic operator families and one is the [Component](../Glossary/Component.md "Component") family which can further contain networks of operators. Components containing components form the TouchDesigner hierarchy and give rise to the operator [Paths](../Glossary/Network_Path.md "Network Path").
  * **[COMPs - Components](../Glossary/Component.md "Component")** - [Object Components](../Glossary/Object.md "Object") (3D objects), [Panel Components](../Glossary/Panel_Component.md "Panel Component") (2D UI gadgets), and other component types. Components contain other operators.
  * **[TOPs - Texture Operators](../TOPs/TOP.md "TOP")** - all 2D image operations.
  * **[CHOPs - Channel Operators](../Glossary/CHOP.md "CHOP")** - motion, audio, animation, control signals.
  * **[POPs - Point Operators](../POPs/POP.md "POP")** - 3D points, primitives, polygons, point clouds, particles and GPU-based data operations.
  * **[DATs - Data Operators](../Glossary/DAT.md "DAT")** - ASCII text as plain text, scripts, XML, or organized in tables of cells.
  * **[MATs - Material Operators](../MATs/MAT.md "MAT")** - materials and shaders.
  * **[SOPs - Surface Operators](../SOPs/SOP.md "SOP")** - legacy 3D points, polygons and other 3D primitives, with some capabilities not possible in POPs yet.

Within each operator family, "**generator** " operators have 0 inputs and create data, and "**filter** " operators have 1 or more input and filter data.

Each operator family is a unique color. Only operators of the same family (color) can be [Wired](../Glossary/Wire.md "Wire") together. Many operators have parameters that are references to operators in other families: [Links](../Glossary/Link.md "Link"). Also [Exporting](../Glossary/Export.md "Export") flows numeric data from CHOPs to all operators.
[![Nodes088.png](https://docs.derivative.ca/images/thumb/6/6a/Nodes088.png/800px-Nodes088.png)](https://docs.derivative.ca/File:Nodes088.png)
[Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") of family TOP, CHOP, POP, SOP, DAT and SOP can be created using [C++](https://docs.derivative.ca/Category:C%2B%2B "Category:C++"), allowing you to extend TouchDesigner's functionality. They will show up in the [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog") under the 'Custom' tab.

See also:  [OP_Class](../Python/OP_Class.md "OP Class")

##  Creating Operators

To add new operators to a network, use the [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog"). The OP Create Dialog can be opened by pressing the **< tab>** key, double-clicking on the network background, clicking the "+" button in the [Pane Bar](https://docs.derivative.ca/Pane_Bar "Pane Bar"), selecting **Add Operator** from the right-click menu in any network, or by right-clicking on the input or output of another operator.

##  Converting data between OP Families

You can convert data between different Operator families using the following conversion operators. For example, you can convert geometry into a DAT list of point positions using the SOP to DAT operator, or convert a TOP image's pixel values into red, green, and blue channels in CHOP using the TOP to CHOP operator.
  * [TOP to CHOP](../CHOPs/TOP_to_CHOP.md "TOP to CHOP")
  * [CHOP to TOP](../TOPs/CHOP_to_TOP.md "CHOP to TOP")
  * [CHOP to DAT](../DATs/CHOP_to_DAT.md "CHOP to DAT")
  * [CHOP to SOP](../SOPs/CHOP_to_SOP.md "CHOP to SOP")
  * [DAT to CHOP](../CHOPs/DAT_to_CHOP.md "DAT to CHOP")
  * [DAT to SOP](../SOPs/DAT_to_SOP.md "DAT to SOP")
  * [SOP to CHOP](../CHOPs/SOP_to_CHOP.md "SOP to CHOP")
  * [SOP to DAT](../Glossary/SOP_to_DAT.md "SOP to DAT")
  * [Object CHOP](../CHOPs/Object_CHOP.md "Object CHOP")

##  See also

[Node](../Glossary/Node.md "Node"), [Wire](../Glossary/Wire.md "Wire"), [Link](../Glossary/Link.md "Link"), [Flag](../Glossary/Flag.md "Flag"), [Connector](../Glossary/Connector.md "Connector"), [Viewer](../Glossary/Viewer.md "Viewer"), [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog")

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

POPs (Point Operators) is a new [Operator Family](../Glossary/Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](../Glossary/Script.md "Script") or [GLSL](../Glossary/GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](../Glossary/Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

Any floating window that is not a [Pane](../Glossary/Pane.md "Pane") or [Viewer](../Glossary/Viewer.md "Viewer").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").
