---
url: https://docs.derivative.ca/Hierarchy
category: Glossary
title: Hierarchy
---

# Hierarchy

Hierarchy relates components with other components. Hierarchies let one component to be positioned relative to another component.

There are two groups of Hierarchy in TouchDesigner. **3D Object Components**, and **2D Panel Components**. Each group can be connected via lines ([Wires](Wire.md "Wire")) between the bottoms/tops of nodes in a network, or by placing one component inside the other.
  * For 3D Object hierarchies, it means that 3D objects are connected to other 3D objects and can be moved/rotated/scaled (transformed) as a group in 3D, and relative to each other.
  * For 2D panel hierarchies, it means that panels are contained inside other panels, and panels can be built into larger user interfaces. panels can be moved and scaled as a group, or relative to each other, by adjusting with their parameters.

[![Hierarchy of 3D Objects](https://docs.derivative.ca/images/thumb/9/96/Hierarchy3DObjects.1.png/600px-Hierarchy3DObjects.1.png)](https://docs.derivative.ca/File:Hierarchy3DObjects.1.png "Hierarchy of 3D Objects") [![Hierarchy of Panels](https://docs.derivative.ca/images/thumb/5/5c/HierarchyPanels.1.png/500px-HierarchyPanels.1.png)](https://docs.derivative.ca/File:HierarchyPanels.1.png "Hierarchy of Panels")
As noted, each group can be related/connected in two ways:
  1. by connecting lines between the bottoms/tops of nodes in a network as shown in the examples above. The node at the top is the parent, the node at the bottom is the child. The child can be transformed relative to the parent via its transform parameters.
  2. by placing one component inside the other. The node inside is the child, the node that encloses it is the parent. The child can be transformed relative to the parent via its transform parameters and via the parent's Layout parameters. You can see the [Network Path](Network_Path.md "Network Path") hierarchy in the [Pane Bar](https://docs.derivative.ca/Pane_Bar "Pane Bar") at the top of each network.

Hierarchy lines always connect nodes in the same component group.

To create a hierarchy where operators are in the same network:
  1. Left-click on a component's bottom or top connector.
  2. Move the cursor to the top/bottom connector of the component you wish to connect to.
  3. Click a second time to complete the connection.

Or, using the embedded approach: For panels, put a panel inside a panel. For 3D objects put a 3D object inside the 3D object.

( "Hierarchies" also exist separately the file system, and in python data structures, but it is not applicable or covered here. )

##  See also

[Connector](Connector.md "Connector"), [Wire](Wire.md "Wire"), [Link](Link.md "Link"), [Operator](../General/Operator.md "Operator"), [Node](Node.md "Node")

Hierarchy relates components with other components. There are two groups of Hierarchy in TouchDesigner. 3D Object Components, and 2D Panel Components. Hierarchies let one component to be positioned relative to another. Each group can be connected via lines between the bottoms/tops of nodes in a network, or by placing one component inside the other.

The sub-[Family](Operator_Family.md "Operator Family") of [Component](Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](Camera_COMP.md "Camera COMP") and [Light COMP](Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

(1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](Timeline.md "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](Pane.md "Pane") and [Bookmark](Bookmark.md "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.
