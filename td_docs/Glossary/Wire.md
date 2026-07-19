---
url: https://docs.derivative.ca/Wire
category: Glossary
title: Wire
---

# Wire

**Wires** are the colored lines that connect the output of a node to the inputs of other nodes in a network. You can think of wires as passing the data from one node to another.

A second type of wire is the Hierarchy Wire that connects the connectors on the top/bottom of 3D Components and 2D Panel Components, and forms the parent-child relation of these components.

Wires always connect nodes in the same [Family](../General/Operator.md "Operator"): A wire between 2 CHOPs exposes the set of channels of the source CHOP to the destination CHOP. A wire between 2 TOPs exposes the image of the source TOP to the destination TOP. Left-right Data Wires occur on [CHOPs](CHOP.md "CHOP"), [TOPs](../TOPs/TOP.md "TOP"), [SOPs](../SOPs/SOP.md "SOP"), [DATs](DAT.md "DAT") and occasionally [MATs](../MATs/MAT.md "MAT").

To create a wire:
  1. Left-click on a node's input or output.
  2. Move the cursor to the output or input of the node you wish to connect to.
  3. Click a second time to complete the connection.

or
  1. Left-click on a node's input or output, and while holding it down, drag the cursor to the output or input of the node you wish to connect to.
  2. Release the left button.

When the cursor is over a connecting wire, it will highlight in yellow. In this highlighted state, on the wire you can
  * [MMB](Mouse_Click.md "Mouse Click") (middle mouse button click) to get info for the incoming node
  * [RMB](Mouse_Click.md "Mouse Click") to bring up a menu that allows you to
    * insert an operator via the OP Create Dialog
    * select the source node
    * select the destination node
    * disconnect the wire

Wires display animated dashed lines to provides visual feedback as to which nodes in a network are cooking. The animated dashed lines represent the flow of data between nodes.

**Tip** : Wires can be displayed in two modes: spline curves and straight lines. Pressing the hotkey "**s** " (straight) in a [Network Editor](Network_Editor.md "Network Editor") pane will toggle between these two modes. You can also toggle the setting by using the "**Link Straight**" menu option from the Network Editor's context menu.

**Note** : When an operator cooks and data is generated, if it is connected by a wire to another operator, it doesn't actually pass or copy its data to the destination - it only informs the destination of where to get its data to operate on.

**Wires in spline mode**
[![Wires Spline.jpg](https://docs.derivative.ca/images/8/80/Wires_Spline.jpg)](https://docs.derivative.ca/File:Wires_Spline.jpg)
**Wires in straight mode**
[![Wires Straight.jpg](https://docs.derivative.ca/images/a/a7/Wires_Straight.jpg)](https://docs.derivative.ca/File:Wires_Straight.jpg)

##  See also

[Connector](Connector.md "Connector"), [Hierarchy](Hierarchy.md "Hierarchy"), [Link](Link.md "Link"), [Operator](../General/Operator.md "Operator"), [Node](Node.md "Node")

Hierarchy relates components with other components. There are two groups of Hierarchy in TouchDesigner. 3D Object Components, and 2D Panel Components. Hierarchies let one component to be positioned relative to another. Each group can be connected via lines between the bottoms/tops of nodes in a network, or by placing one component inside the other.

The connection of an output of one node to the input of another node in a network. In contrast, see [Link](Link.md "Link").

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

Any floating window that is not a [Pane](Pane.md "Pane") or [Viewer](Viewer.md "Viewer").

A [Link](Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](Operator_Family.md "Operator Family").

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](Export.md "Export"), node [Paths](Network_Path.md "Network Path") in parameters, and [expressions](Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a Wire that connects nodes in the same [Operator Family](Operator_Family.md "Operator Family").

A pane type where networks of operators can be created and edited.
