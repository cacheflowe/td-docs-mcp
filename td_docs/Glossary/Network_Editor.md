---
url: https://docs.derivative.ca/Network_Editor
category: Glossary
title: Network_Editor
---

# Network Editor

The **Network Editor** is a pane type in TouchDesigner that is used to create and modify [Operators](https://docs.derivative.ca/Operator "Operator"). The Network Editor is the default pane type for TouchDesigner and is visible when the program is launched. Navigating in the Network Editor is an important skill to learn early in TouchDesigner. Mastery of the Network Editor allows you to more easily modify and update your networks over time. The primary tool for network navigation is the mouse, although some operations have menu or keyboard equivalents. Each mouse button manipulates the Network Editor interface in a different way.

##  Network Navigation

###  Node Selection

Use the left mouse button [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") to select nodes. To box-select multiple nodes hold shift while dragging with LMB or use the [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click"). Alternatively, you can hold down the _Ctrl_ key and left-click on each individual node you want to add to the selection. To move a node, select it and keep the LMB depressed to drag it around the Network Editor.

###  Moving Around the Network

The left mouse button (LMB) navigates networks without changing the zoom level. Drag using the LMB in any empty area in the network to pan around the network. A scale 'overview' representation of the Network can be toggled on and off with the "**o** " key.

###  Zooming

The middle mouse button [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") controls the zoom level, hold MMB and drag right or left to zoom in or out. To return to **Unity Zoom** (zoom level of 1), use the keyboard shortcut "**f** " for **Unity Frame All**.

If the middle mouse button is also a scroll wheel on your mouse, scroll forwards to zoom in and scroll backwards to zoom out.

You can also box zoom by holding down the Ctrl button while using the MMB. To zoom in, hold down Ctrl and draw a box from left to right with the MMB. To zoom out, draw the box from right to left.

###  Moving Between Networks

There are several ways to move in and out of Component networks.

To enter a network (go inside a component):
  * double-click on a component to go inside its network
  * use the scroll wheel to zoom up close to a component and keep zooming in to go inside its network
  * select the component and then press <Enter> key to go inside its network
  * select the component and then press the < i > key to go inside its network
  * select the component and then press the 'double arrow' in the [network path](https://docs.derivative.ca/Network_Path "Network Path") found at the top of the [pane](https://docs.derivative.ca/Pane "Pane")
  * on the component click [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") and select **Enter Component** from the menu

When inside a Component, to go up a level:
  * press the `u` key
  * use the scroll wheel to zoom out
  * in the [network path](https://docs.derivative.ca/Network_Path "Network Path") found at the top of the [pane](https://docs.derivative.ca/Pane "Pane"), click on the component’s name you want to see. For example, if the path is /project1/scene1/geo2 and you want to go /project1, simply click on the word "project1".
  * you may find the **Back** and **Forward** buttons in the top [pane bar](https://docs.derivative.ca/Pane_Bar "Pane Bar") handy to navigate in and out of Components.

##  Interacting with Operators

Here are some other interactions you can perform in the Network Editor.
  * Resize nodes by grabbing the edge of the node with LMB and dragging
  * Grid snapping is on by default, adjust grid options in [Preferences](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog") (Edit > Preferences > Network)
  * Layout and Display options are found in the Network Editor's RMB menu
  * [Node Viewers](https://docs.derivative.ca/Node_Viewer "Node Viewer") can go into [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active") mode (interactive mode) by clicking on the [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active") flag found in the lower-right corner.
  * Middle-clicking on node will open the operator info popup.
  * [Flags](https://docs.derivative.ca/Flag "Flag") on the operators can be used to toggle their state (display state, render state, pickable state, etc)
  * Animated [Wires](https://docs.derivative.ca/Wire "Wire") indicate data flow between operators.
  * The Network Editor can be toggled to **list mode** by pressing the shift+t keyboard shortcut or by selecting if from the right-click menu.

##  See also

  * [Network](https://docs.derivative.ca/Network "Network")
  * [Zoomable User Interface](https://docs.derivative.ca/Zoomable_User_Interface "Zoomable User Interface")

A pane type where networks of operators can be created and edited.

Every component contains a network of operators that create and modify data. The operators are connected by wires that define where data is routed after the operator cooks its inputs and generates an output.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

(1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](https://docs.derivative.ca/Timeline "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](https://docs.derivative.ca/Pane "Pane") and [Bookmark](https://docs.derivative.ca/Bookmark "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.
