---
url: https://docs.derivative.ca/RMB_Menu
category: Glossary
title: RMB_Menu
---

# RMB Menu

The **RMB Menu** or **Context Menu** is the menu that appears when the right mouse button is clicked on an [Operator](../General/Operator.md "Operator").

See [Mouse Click](Mouse_Click.md "Mouse Click").

##  Common Options

  * Parameters
    * Reset to Defaults
  * Viewer
  * Edit Comment
  * Create Movie
  * Explore Media Folder
  * Change OP Type
  * Select Inputs
    * Outputs
  * Force Cook
  * Delete

##  COMP specific Options

  * Open Control Panel...
    * Native Size...
    * Borderless...
    * Edit Mode...
  * Save Component
    * with Media...
  * Display Options

##  TOP specific Options

  * Save Image...

##  CHOP specific Options

  * CHOP Exporter...
  * Information...
  * Save CHOP Channels...
  * Edit Keyframes...
  * Play Audio Sample

##  SOP specific Options

  * Spreadsheet...
  * Save Geometry...
  * Model Geometry...
  * Display Parameters...

##  DAT specific Options

  * Save Contents...
  * Edit Contents...
  * Run Script...
  * Toggle Data Format...

The menu that appears when clicking the right mouse button on different parts of TouchDesigner. (Sometimes you need to be holding down Ctrl.)

The viewer of a node can be (1) the interior of a node (the [Node Viewer](Node_Viewer.md "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](Pane.md "Pane") that graphically shows the results of an operator.

A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](Network_Path.md "Network Path").

To re-compute the output data of the [Operators](../General/Operator.md "Operator"). An operator cooks when (1) its inputs change, (2) its [Parameters](Parameter.md "Parameter") change, (3) when the timeline moves forward in some cases, or (4) [Scripting](Script.md "Script") commands are run on the node. When the operator is a [Panel Component](Panel_Component.md "Panel Component"), it also cooks when a user interacts with it. When an operator cooks, it usually causes operators connected to its output to re-cook. When TouchDesigner draws the screen, it re-cooks all the [Dependencies](Dependency.md "Dependency") - the necessary operators in all [Networks](Network.md "Network"), contributing to a frame's total "cook time".

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](Panel_Component.md "Panel Component").

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

samples-per-second of a [CHOP](CHOP.md "CHOP"). Each CHOP in your network has a sample rate. In contrast, the overall timeline has a [Frame Rate](Frame_Rate.md "Frame Rate"), which is the number of frames to [cook](Cook.md "Cook") and display per second, generally your monitor display frequency, default 60.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](Geometry_COMP.md "Geometry COMP").

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](../General/Python.md "Python") and the original [Tscript](Tscript.md "Tscript"). Scripts and single-line commands can also be run in the [Textport](Textport.md "Textport").
