---
url: https://docs.derivative.ca/RMB_Menu
category: Glossary
title: RMB_Menu
---

# RMB Menu
The **RMB Menu** or **Context Menu** is the menu that appears when the right mouse button is clicked on an [Operator](https://docs.derivative.ca/Operator "Operator").
See [Mouse Click](https://docs.derivative.ca/Mouse_Click "Mouse Click").

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
The viewer of a node can be (1) the interior of a node (the [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](https://docs.derivative.ca/Pane "Pane") that graphically shows the results of an operator.
A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
To re-compute the output data of the [Operators](https://docs.derivative.ca/Operator "Operator"). An operator cooks when (1) its inputs change, (2) its [Parameters](https://docs.derivative.ca/Parameter "Parameter") change, (3) when the timeline moves forward in some cases, or (4) [Scripting](https://docs.derivative.ca/Script "Script") commands are run on the node. When the operator is a [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component"), it also cooks when a user interacts with it. When an operator cooks, it usually causes operators connected to its output to re-cook. When TouchDesigner draws the screen, it re-cooks all the [Dependencies](https://docs.derivative.ca/Dependency "Dependency") - the necessary operators in all [Networks](https://docs.derivative.ca/Network "Network"), contributing to a frame's total "cook time".
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
samples-per-second of a [CHOP](https://docs.derivative.ca/CHOP "CHOP"). Each CHOP in your network has a sample rate. In contrast, the overall timeline has a [Frame Rate](https://docs.derivative.ca/Frame_Rate "Frame Rate"), which is the number of frames to [cook](https://docs.derivative.ca/Cook "Cook") and display per second, generally your monitor display frequency, default 60.
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
The 3D data held in SOPs and passed for rendering by the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").
