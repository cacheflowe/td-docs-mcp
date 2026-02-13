---
url: https://docs.derivative.ca/Operator
category: CHOPs
title: Operator
---

# Operator

## Summary

Operators are the "[Nodes](https://docs.derivative.ca/Node "Node")" in TouchDesigner networks, and they output data to other operators. Each operator is customized with its [Parameters](https://docs.derivative.ca/Parameter "Parameter") and [Flags](https://docs.derivative.ca/Flag "Flag").
[![Geo1.jpg](https://docs.derivative.ca/images/thumb/8/85/Geo1.jpg/200px-Geo1.jpg)](https://docs.derivative.ca/File:Geo1.jpg)
[OP Class](https://docs.derivative.ca/OP_Class "OP Class")

##  Operator Families
There are seven **Families** of built-in Operators. Of the six families, five are basic operator families and one is the [Component](https://docs.derivative.ca/Component "Component") family which can further contain networks of operators. Components containing components form the TouchDesigner hierarchy and give rise to the operator [Paths](https://docs.derivative.ca/Network_Path "Network Path").
  * **[COMPs - Components](https://docs.derivative.ca/Component "Component")** - [Object Components](https://docs.derivative.ca/Object "Object") (3D objects), [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component") (2D UI gadgets), and other component types. Components contain other operators.
  * **[TOPs - Texture Operators](https://docs.derivative.ca/TOP "TOP")** - all 2D image operations.
  * **[CHOPs - Channel Operators](https://docs.derivative.ca/CHOP "CHOP")** - motion, audio, animation, control signals.
  * **[POPs - Point Operators](https://docs.derivative.ca/POP "POP")** - 3D points, primitives, polygons, point clouds, particles and GPU-based data operations.
  * **[DATs - Data Operators](https://docs.derivative.ca/DAT "DAT")** - ASCII text as plain text, scripts, XML, or organized in tables of cells.
  * **[MATs - Material Operators](https://docs.derivative.ca/MAT "MAT")** - materials and shaders.
  * **[SOPs - Surface Operators](https://docs.derivative.ca/SOP "SOP")** - legacy 3D points, polygons and other 3D primitives, with some capabilities not possible in POPs yet.

Within each operator family, "**generator** " operators have 0 inputs and create data, and "**filter** " operators have 1 or more input and filter data.
Each operator family is a unique color. Only operators of the same family (color) can be [Wired](https://docs.derivative.ca/Wire "Wire") together. Many operators have parameters that are references to operators in other families: [Links](https://docs.derivative.ca/Link "Link"). Also [Exporting](https://docs.derivative.ca/Export "Export") flows numeric data from CHOPs to all operators.
[![Nodes088.png](https://docs.derivative.ca/images/thumb/6/6a/Nodes088.png/800px-Nodes088.png)](https://docs.derivative.ca/File:Nodes088.png)
[Custom Operators](https://docs.derivative.ca/Custom_Operators "Custom Operators") of family TOP, CHOP, POP, SOP, DAT and SOP can be created using [C++](https://docs.derivative.ca/Category:C%2B%2B "Category:C++"), allowing you to extend TouchDesigner's functionality. They will show up in the [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog") under the 'Custom' tab.
See also:  [OP_Class](https://docs.derivative.ca/OP_Class "OP Class")
##  Creating Operators
To add new operators to a network, use the [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog"). The OP Create Dialog can be opened by pressing the **< tab>** key, double-clicking on the network background, clicking the "+" button in the [Pane Bar](https://docs.derivative.ca/Pane_Bar "Pane Bar"), selecting **Add Operator** from the right-click menu in any network, or by right-clicking on the input or output of another operator.
##  Converting data between OP Families
You can convert data between different Operator families using the following conversion operators. For example, you can convert geometry into a DAT list of point positions using the SOP to DAT operator, or convert a TOP image's pixel values into red, green, and blue channels in CHOP using the TOP to CHOP operator.
  * [TOP to CHOP](https://docs.derivative.ca/TOP_to_CHOP "TOP to CHOP")
  * [CHOP to TOP](https://docs.derivative.ca/CHOP_to_TOP "CHOP to TOP")
  * [CHOP to DAT](https://docs.derivative.ca/CHOP_to_DAT "CHOP to DAT")
  * [CHOP to SOP](https://docs.derivative.ca/CHOP_to_SOP "CHOP to SOP")
  * [DAT to CHOP](https://docs.derivative.ca/DAT_to_CHOP "DAT to CHOP")
  * [DAT to SOP](https://docs.derivative.ca/DAT_to_SOP "DAT to SOP")
  * [SOP to CHOP](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP")
  * [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT")
  * [Object CHOP](https://docs.derivative.ca/Object_CHOP "Object CHOP")

##  See also
[Node](https://docs.derivative.ca/Node "Node"), [Wire](https://docs.derivative.ca/Wire "Wire"), [Link](https://docs.derivative.ca/Link "Link"), [Flag](https://docs.derivative.ca/Flag "Flag"), [Connector](https://docs.derivative.ca/Connector "Connector"), [Viewer](https://docs.derivative.ca/Viewer "Viewer"), [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog")
The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
POPs (**Point Operators**) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
Any floating window that is not a [Pane](https://docs.derivative.ca/Pane "Pane") or [Viewer](https://docs.derivative.ca/Viewer "Viewer").
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
