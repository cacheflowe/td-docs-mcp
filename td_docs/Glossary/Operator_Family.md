---
url: https://docs.derivative.ca/Operator_Family
category: Glossary
title: Operator_Family
---

# Operator Family

There are seven **Families** of built-in [Operators](../General/Operator.md "Operator"). Of the seven families, six are basic operator families and one is the [Component](Component.md "Component") family which can further contain networks of operators. Components containing components form the TouchDesigner hierarchy and give rise to the operator [Paths](Network_Path.md "Network Path").
  * **[COMPs - Components](Component.md "Component")** - [Object Components](Object.md "Object") (3D objects), [Panel Components](Panel_Component.md "Panel Component") (2D UI gadgets), and other component types. Components contain other operators.
  * **[TOPs - Texture Operators](../TOPs/TOP.md "TOP")** - all 2D image operations.
  * **[CHOPs - Channel Operators](CHOP.md "CHOP")** - motion, audio, animation, control signals.
  * **[POPs - Point Operators](../POPs/POP.md "POP")** - 3D points, primitives, polygons, point clouds, particles and GPU-based data operations.
  * **[DATs - Data Operators](DAT.md "DAT")** - ASCII text as plain text, scripts, XML, or organized in tables of cells.
  * **[MATs - Material Operators](../MATs/MAT.md "MAT")** - materials and shaders.
  * **[SOPs - Surface Operators](../SOPs/SOP.md "SOP")** - legacy 3D points, polygons and other 3D primitives, with some capabilities not possible in POPs yet.

Within each operator family, "**generator** " operators have 0 inputs and create data, and "**filter** " operators have 1 or more input and filter data.

Each operator family is a unique color. Only operators of the same family (color) can be [Wired](Wire.md "Wire") together. Many operators have parameters that are references to operators in other families: [Links](Link.md "Link"). Also [Exporting](Export.md "Export") flows numeric data from CHOPs to all operators.
[![Nodes088.png](https://docs.derivative.ca/images/thumb/6/6a/Nodes088.png/800px-Nodes088.png)](https://docs.derivative.ca/File:Nodes088.png)
[Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") of family TOP, CHOP, POP, SOP, DAT and SOP can be created using [C++](https://docs.derivative.ca/Category:C%2B%2B "Category:C++"), allowing you to extend TouchDesigner's functionality. They will show up in the [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog") under the 'Custom' tab.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

An Operator Family that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An Operator Family which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

POPs (Point Operators) is a new Operator Family that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

A Operator Family that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An Operator Family that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.
