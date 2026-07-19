---
url: https://docs.derivative.ca/OP_Create_Menu
category: Glossary
title: OP_Create_Menu
---

# OP Create Menu

The OP Create Dialog, also called the Tab menu, lets you create new [Operators](../General/Operator.md "Operator") and is accessed by:
  * double-clicking on the background of a network
  * pressing the Tab key
  * clicking the + icon at the top of a Network Editor Pane beside the path
  * use [MMB](https://docs.derivative.ca/index.php?title=MMB&action=edit&redlink=1 "MMB \(page does not exist\)") and/or [RMB](https://docs.derivative.ca/index.php?title=RMB&action=edit&redlink=1 "RMB \(page does not exist\)") on OP inputs/outputs
  * [RMB](https://docs.derivative.ca/index.php?title=RMB&action=edit&redlink=1 "RMB \(page does not exist\)") -> Add Operator on a [Wire](Wire.md "Wire")
  * [RMB](https://docs.derivative.ca/index.php?title=RMB&action=edit&redlink=1 "RMB \(page does not exist\)") -> Add Operator on an empty part of a network

It gives you access to all the operator types, just click on a name and then click anywhere on a [Network Editor Pane](Network_Editor.md "Network Editor") to place it in the network.

Select the [Operator Family](../General/Operator.md "Operator") from the headings COMP TOP CHOP SOP MAT DAT.

Generators (types with no inputs) are shown using a darker shade, and Filters are the lighter shade of the OP color.

You can start typing the name of the OP type you are looking for. Any OP-type that matches the string you’ve typed will highlight in white. For example, type _midi_ and all the OP types starting with _midi_ will turn white.
[![Opcreate CHOP.jpg](https://docs.derivative.ca/images/f/f2/Opcreate_CHOP.jpg)](https://docs.derivative.ca/File:Opcreate_CHOP.jpg)
Advanced Options

###

Adding Multiple Operators

Using the **< ctrl>** key allows multiple operators to be added to the network.

First open the OP Create Dialog. Then press and hold the **< ctrl>** key while making your selection of operators. As operators are clicked on they will be added to the network.

###

Wiring Multiple Operators Together

Using the **< shift>** key allows multiple operators to be wired together and added to the network.

First open the OP Create Dialog. Press and hold the **< shift>** key and as you select operators from the menu they will be wired together and added to the network. When selecting an OP of a different family type, a new branch of connected operators will be started.

See Also [Change OP Type Dialog](https://docs.derivative.ca/Change_OP_Type_Dialog "Change OP Type Dialog")

Any floating window that is not a [Pane](Pane.md "Pane") or [Viewer](Viewer.md "Viewer").

A pane type where networks of operators can be created and edited.

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

MATs or Materials are an [Operator Family](Operator_Family.md "Operator Family") that applies a [Shader](Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").
