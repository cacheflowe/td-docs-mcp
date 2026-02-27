---
url: https://docs.derivative.ca/Docking
category: Glossary
title: Docking
---

# Docking

Docking a node is a way to reduce clutter in a network by hiding an operator as a small dock icon on another node. This icon is color-coded to indicate the [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of the docked node. Any node can be docked to another node. When a dock pa ent node is moved in the [Network Editor](https://docs.derivative.ca/Network_Editor "Network Editor"), the docked node moves with it as well.

Docking does not affect the nodes' behavior, only the look.

A docked node is often docked to a related node to help with network organization, an example is the [Ramp TOP](https://docs.derivative.ca/Ramp_TOP "Ramp TOP"). A new Ramp TOP is created with a docked [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") that stores the ramp color information. To view the Table DAT, click on the DAT-colored dock icon attached to the lower-right corner of the Ramp TOP. Click on the icon again to collapse the docked node back down to an icon.

##  Docking a Node

A node can be docked two different ways:
  * - Right-clicking on the node to be docked and select **Dock to ...** , then click on the node you want to dock to.
  * - Using `Op.dock` and `Op.docked` in python for the [Operator class](https://docs.derivative.ca/OP_Class#Common_Flags "OP Class").

[![](https://docs.derivative.ca/images/9/9c/Docking.png)](https://docs.derivative.ca/File:Docking.png)
_ramp1_ with docked node collapsed, _ramp2_ with docked node exposed

Any [node](https://docs.derivative.ca/Node "Node") can be docked to another node. This helps organize networks as two node that are docked together will stay together when the dock parent is moved in a network editor. A docked node can be collapsed into a small icon under the dock parent, reducing network clutter.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

A form of [DATs](https://docs.derivative.ca/DAT "DAT") (Data Operators) that is structured as rows and columns of text strings.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

The generic thing that holds an [Operator](https://docs.derivative.ca/Operator "Operator"), and includes [Flags](https://docs.derivative.ca/Flag "Flag") (display, bypass, lock, render, immune) and its position/size in the network. Whether you "lay down an Operator" or "lay down an Node", you're doing the same thing.
