---
url: https://docs.derivative.ca/Layout
category: Glossary
title: Layout
---

# Layout

The TouchDesigner window is made of a menu bar at the top, a [Timeline](https://docs.derivative.ca/Timeline "Timeline") at the bottom, plus one of a choice of pane Layouts in the middle. A Layout is made of one or more panes, each pane can contain a Network Editor, Viewer, Panel, etc.. See [Panes](https://docs.derivative.ca/Pane "Pane") for additional information on using panes.

##  The Layout Strip

Layouts can be saved and recalled using the **Layout Strip** which is directly below the menu bar at the top of the TouchDesigner window.
[![LayoutStrip.jpg](https://docs.derivative.ca/images/0/09/LayoutStrip.jpg)](https://docs.derivative.ca/File:LayoutStrip.jpg)
To the left there is a collection of default pane layouts. There are 5 to choose; single, quad, vertical split, horizontal split, and tri split. Click on the appropriate icon to load the layout.

##  Saving Custom Layouts

You can also save your own custom layouts by clicking the add layout button.
[![AddLayout.jpg](https://docs.derivative.ca/images/1/19/AddLayout.jpg)](https://docs.derivative.ca/File:AddLayout.jpg)
For example, if a layout is added while the TouchDesigner interface is split into 2 vertical panes, all that pane information (including pane's type and path) is saved in a custom layout and added to the layout strip. Layouts for a project are saved in the [.toe](https://docs.derivative.ca/.toe ".toe") file so that they are accessible each time the project is re-opened. Layouts are saved as layout components in `/local/layouts`.
[![LayoutsCustom.jpg](https://docs.derivative.ca/images/7/78/LayoutsCustom.jpg)](https://docs.derivative.ca/File:LayoutsCustom.jpg)

##  Loading Custom Layouts

Clicking on the custom Layout will load the panes in the configuration that they were saved in as well as loading the saved network path for each pane.
[![LayoutName.jpg](https://docs.derivative.ca/images/6/62/LayoutName.jpg)](https://docs.derivative.ca/File:LayoutName.jpg)

##  Renaming and Deleting Custom Layouts

Right-clicking on a layout will open a menu with options to rename or delete the selected layout.
[![LayoutRename.jpg](https://docs.derivative.ca/images/c/ce/LayoutRename.jpg)](https://docs.derivative.ca/File:LayoutRename.jpg)
(1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](https://docs.derivative.ca/Timeline "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](https://docs.derivative.ca/Pane "Pane") and [Bookmark](https://docs.derivative.ca/Bookmark "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.

A pane type where networks of operators can be created and edited.

The viewer of a node can be (1) the interior of a node (the [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](https://docs.derivative.ca/Pane "Pane") that graphically shows the results of an operator.

A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component").
