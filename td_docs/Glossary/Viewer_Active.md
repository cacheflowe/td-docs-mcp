---
url: https://docs.derivative.ca/Viewer_Active
category: Glossary
title: Viewer_Active
---

# Viewer Active
A node's Viewer Active state lets you operate a [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer") interactively.
Normally when you click/drag on a node, you move it. When the node's viewer is a three-letter icon, it will always move when clicked-dragged. Click the top-left flag on a node to toggle the viewer on. That makes the viewer visible, but it's not yet active. Then
  * click + at the bottom right of a node.
  * The [shortcut](https://docs.derivative.ca/Shortcut "Shortcut") key "a" will set/unset the Viewer Active Flag of all selected nodes (those with yellow borders).
  * When Alt+a is held down, all node viewers are temporarily in the Viewer Active state.
  * Viewers can be set to always be in the **Viewers Always Active** state using the RMB menu in the Network Editor.
  * All nodes have their own [Viewer Active Flag](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag") on the bottom right corner of the node. Setting the Viewer Active Flag keeps the node viewer in an state where the viewer can always be operated.

The viewer active cursor is ^. The Viewers Always Active state is saved in the `.toe`.
[![ViewerActiveOptions.jpg](https://docs.derivative.ca/images/c/cc/ViewerActiveOptions.jpg)](https://docs.derivative.ca/File:ViewerActiveOptions.jpg)
left: node with 3-letter icon. middle: node with viewer (top-left flag of node). right: node with viewer active (bottom right flag).

When a viewer is active, you will only see a viewer and the name below it. You can manipulate, tumble, pan, zoom and operate the contents of the node viewer. Control panels can be fully-operated.
**Tip** : When a view is active, you can still drag a node around by clicking on the name field at the bottom, and dragging around the network. You can also right-click on the name field to get the node's right-click menu.
Viewer Active is temporarily switched on for all nodes by holding down Alt in [Network Editor](https://docs.derivative.ca/Network_Editor "Network Editor"), or pressing Alt-a to sustain it. Pressing Alt-a again turns Viewer Active off for all nodes except nodes that have their own Viewer Active flag on.
When not in Viewer Active, the node viewer area is disabled and acts like the rest of the node. This allows you to click anywhere to select and move the node, or right-click anywhere to access the node's menu.
**Note** : Moving content inside a node viewer does not affect its transforms or parameters. **Exception** : [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP")
[![ViewerActiveMenu.png](https://docs.derivative.ca/images/4/42/ViewerActiveMenu.png)](https://docs.derivative.ca/File:ViewerActiveMenu.png)
A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.
Indicator of certain states of an operator (bypass, display, lock, viewer active).
A pane type where networks of operators can be created and edited.
TOuch Environment file, the file type used by TouchDesigner to save your entire project.
