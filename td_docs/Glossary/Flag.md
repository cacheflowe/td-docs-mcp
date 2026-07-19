---
url: https://docs.derivative.ca/Flag
category: Glossary
title: Flag
---

# Flag

"Flag" in TouchDesigner refers to the indicator of states of an [Operator](../General/Operator.md "Operator") (Bypass flag, Render flag, Lock flag, Viewer Active flag...). Flags are not parameters, they are binary states of an operator.

###  Operator Flags

Operator flags are located along on the left edge and bottom edge of a [Node](Node.md "Node") in the [Network Editor](Network_Editor.md "Network Editor").

Flags are also visible in a network's "Table View": Press "T" in the network to go to/from Table View. It shows nodes in a table format, where the complete set of flags is visible on the columns.

Flags are not parameters and therefore changing a flag does not in itself cause a node to cook. You cannot export to a flag.

Some flags are specific to certain operator families, like the Render flag for 3D Geometry operators.

All flags are set using, for example, `op('nodename').lock = True`.

To program in Python all common operator flags, see the Flags section in:  [OP_Class](../Python/OP_Class.md "OP Class"), and the classes for each operator family.

####  Flags on all Nodes

  * [Viewer](Viewer_Flag.md "Viewer Flag") - turns on the data viewer in the center of the node.
  * [Viewer Active](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag") - makes the viewer interactive so you can inspect the node's output data further, or operate a panel.
  * [Lock](Lock_Flag.md "Lock Flag") - the data the node outputs is frozen in memory (and saved in the `.toe` `.tox`)
  * [Bypass](Bypass_Flag.md "Bypass Flag") - the first input is passed directly to the output. Bypass on a component causes all nodes inside it to be bypassed.
  * [Cooking](https://docs.derivative.ca/Cooking_Flag "Cooking Flag") - on a component, will cause nodes inside not to cook.
  * [Immune](Immune_Flag.md "Immune Flag") - a node inside a clone can be immune from cloning.
  * [Current](https://docs.derivative.ca/Current_Flag "Current Flag") - the node is the current node in a network
  * [Selected](https://docs.derivative.ca/Selected_Flag "Selected Flag") - the node is one of the selected nodes in a network.
  * [Expose](https://docs.derivative.ca/Expose_Flag "Expose Flag") - the node can be hidden from view in a network.
  * Python - a flag that sets the language of the content of a node to be Python (the default). Visible on the Parameter Dialog only.

####  Flags on 3D Object components

  * [Render](Render_Flag.md "Render Flag") - if off, the object will not be seen in any render of the Render TOP or Render Pass TOP.
  * [Display](Display_Flag.md "Display Flag") - if off, the object will not be seen in any camera viewer.
  * [Pickable](https://docs.derivative.ca/Pickable_Flag "Pickable Flag") - if off, the object will not be selectable in [3D Geometry Viewers](../Interoperability/Geometry_Viewer.md "Geometry Viewer") or the [SOP Editor](https://docs.derivative.ca/SOP_Editor "SOP Editor").

####  Flags on CHOPs

  * [Export](https://docs.derivative.ca/Export_Flag "Export Flag") - if off, nothing is exported from that CHOP.

####  Flags on SOPs

  * [Compare](https://docs.derivative.ca/Compare_Flag "Compare Flag") - displays the SOP's input geometry as a green wireframe for comparisons.
  * [Template](https://docs.derivative.ca/Template_Flag "Template Flag") - displays the SOP as templated geometry in 3D viewers. The grey wireframe template is not selectable or editable.

Indicator of certain states of an operator (Bypass flag, Render flag, Lock flag, Viewer Active flag).

A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

TouchDesigner Component file, the file type used to save a [Component](Component.md "Component") of your TouchDesigner project.

A floating dialog, pane type, or dialog in a Network Editor that displays one operator's parameters.

The sub-[Family](Operator_Family.md "Operator Family") of [Component](Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](Camera_COMP.md "Camera COMP") and [Light COMP](Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
