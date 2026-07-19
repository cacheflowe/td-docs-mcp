---
url: https://docs.derivative.ca/Viewer
category: Glossary
title: Viewer
---

# Viewer

### Locations of Viewers

Viewers of TouchDesigner operators are found in three places:
  * in nodes - Viewers inside nodes are called to as [Node Viewers](Node_Viewer.md "Node Viewer").
  * in floating windows - Opened from panes as floating dialogs (using Tear Off or Copy Pane), or opened by selecting **Viewer...** from a node's right-click menu.
  * in [Panes](Pane.md "Pane")

**Note** : Moving content inside a node viewer does not affect its transforms or parameters. **Exception** : [Camera COMP](Camera_COMP.md "Camera COMP")

###  Styles of Viewers

There is a viewer style for every operator family.       [Geometry Viewer](../Interoperability/Geometry_Viewer.md "Geometry Viewer") - A 3D viewport for viewing and manipulating 3D scenes or objects. You can tumble, pan, and zoom throughout the 3D scene. You can also edit the scene by translating, rotating, and scaling geometry, cameras, and lights at the [Object Component](Object_Component.md "Object Component") level. These viewers are also found as Node Viewers in all 3D Components and SOPs.     In the node viewers of Geometry COMPs and SOPs, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position. This can be turned off globally in Edit > Preferences > Geometry : Adaptive Homing by Default.     Panel Viewer - Displays the view of [Panel Components](Panel_Component.md "Panel Component") and allows for interactions with the control panels.      [CHOP Viewer](CHOP_Viewer.md "CHOP Viewer") - A 2D viewer to inspecting and editing CHOP channel values. Time is on the x-axis, value (or amplitude) is on the y-axis. Also found as a Node Viewer in all CHOPs.      [TOP Viewer](../TOPs/TOP_Viewer.md "TOP Viewer") - A 2D viewer for viewing TOP images. You can pan and zoom around the image. Also found as a Node Viewer in all TOPs.      [SOP Editor](https://docs.derivative.ca/SOP_Editor "SOP Editor") - Similar to the Geometry Viewer but specialized for editing SOP geometry. Using SOP viewer **States** you can directly manipulate geometry or model new geometry from scratch. A SOP viewer can only be opened directly from SOPs by right-clicking on the SOP and selecting **Model Geometry...** from the menu.      [DAT Viewer](https://docs.derivative.ca/DAT_Viewer "DAT Viewer") - Displays the text or table data of the DAT. This can be directly edited (in generator DATs) by making the viewer active. Note that the default node laguage for DATs is python and displayed in blue text, if the text is the same purple color as DATs then this node's language is set to Tscript.

A work area in TouchDesigner's layout that includes the [Network Editor](Network_Editor.md "Network Editor") and 7 other pane types used for different tasks. The TouchDesigner interface can consist of a single pane, or be split into multiple panes.

The viewer of a node can be (1) the interior of a node (the [Node Viewer](Node_Viewer.md "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](Pane.md "Pane") that graphically shows the results of an operator.

In the [Node Viewer](Node_Viewer.md "Node Viewer") of a Geometry COMP or any POP, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](Geometry_COMP.md "Geometry COMP").

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

The viewer found on each operator in a [Network Editor](Network_Editor.md "Network Editor") pane. This viewer is turned on by clicking the [Viewer Flag](Viewer_Flag.md "Viewer Flag").

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

A 3D viewport for viewing and manipulating 3D scenes or objects interactively. A geometry viewer can be found in [Panes](Pane.md "Pane") (alt+3 in any pane) or the [Node Viewers](Node_Viewer.md "Node Viewer") of all Geometry Object components.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

TouchDesigner's original built-in Command scripting language prior to [Python](../General/Python.md "Python").
