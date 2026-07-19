---
url: https://docs.derivative.ca/Pane
category: Glossary
title: Pane
---

# Pane

A Pane is a work area in TouchDesigner's layout. The TouchDesigner window can be split into 2 or more panes. There is a choice of 9 pane types for different tasks that will fill a pane.

At the top of every Pane resides the [Pane Bar](https://docs.derivative.ca/Pane_Bar "Pane Bar"). In its middle is the [network path](Network_Path.md "Network Path") of the pane. Buttons and icons on the left and right sides let you select the viewer in the pane, bookmarks, jump through a network history, split the pane, go fullscreen, or link one pane to another.

In the network path, click on the `/` characters to navigate through menus, or click on the open space to type in a network path or cut/paste a network path.
[![A TouchDesigner Pane](https://docs.derivative.ca/images/thumb/6/6a/Pane.jpg/650px-Pane.jpg)](https://docs.derivative.ca/File:Pane.jpg "A TouchDesigner Pane")
The TouchDesigner authoring interface, [Designer Mode](Designer_Mode.md "Designer Mode") can consist of a single pane or be split into multiple panes (Also known as Worksheets). The way the panes are arranged and displayed is referred to as a pane [layout](Layout.md "Layout"). Layouts can be managed using the [ Layout Strip](Layout.md "Layout").

Split a pane or use the Pane Layout bar to select a multi-pane layout.

The Network Editor pane type is the primary view and allows you to connect OPs together.

Panel view allows you to view control panels and interact with them.

Geometry Viewer allows you to interact with 3D scenes and objects. The TOP Viewer, CHOP Viewer and Geometry Spreadsheet allow you to look at and, for the Geometry Spreadsheet, modify data in TOPs, CHOPs and SOPs, respectively.

The Parameter and Textport views give access to the same information as the [dialogs](Dialog.md "Dialog") of the same names.

Browser loads a multi-purpose tree browser into the pane. This Browser can be used to investigate TouchDesigner networks, CHOP channels, the file system on disk, and the [Palette](../Learn/Palette.md "Palette") Library all in one convenient pane.

See also the `desk` Command and the `neteditor` Command.

##  Pane Types

[Network Editor](Network_Editor.md "Network Editor")

[Panel](Panel.md "Panel")

[Geometry Viewer](../Interoperability/Geometry_Viewer.md "Geometry Viewer")

[TOP Viewer](../TOPs/TOP_Viewer.md "TOP Viewer")

[CHOP Viewer](CHOP_Viewer.md "CHOP Viewer")

[Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor")

[Parameters](Parameter.md "Parameter")

[Textport and DATs](Textport.md "Textport")

(1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](Timeline.md "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See Pane and [Bookmark](Bookmark.md "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.

A pane type where networks of operators can be created and edited.

A 3D viewport for viewing and manipulating 3D scenes or objects interactively. A geometry viewer can be found in Panes (alt+3 in any pane) or the [Node Viewers](Node_Viewer.md "Node Viewer") of all Geometry Object components.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

The viewer of a node can be (1) the interior of a node (the [Node Viewer](Node_Viewer.md "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a Pane that graphically shows the results of an operator.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

Currently, use a [SOP to DAT](SOP_to_DAT.md "SOP to DAT") to look at SOP point/polygon XYZ and other attributes. Formerly a Pane type.

The dialog box in which commands and scripts can typed in manually. Output to the textport includes script errors and messages from `print()` and `debug()` calls in python code. You can also edit DATs in the textport.
