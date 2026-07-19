---
url: https://docs.derivative.ca/Display_Flag
category: Glossary
title: Display_Flag
---

# Display Flag

Display [flags](Flag.md "Flag") (light blue) are found on [TOPs](../TOPs/TOP.md "TOP"), [CHOPs](CHOP.md "CHOP"), and [SOPs](../SOPs/SOP.md "SOP") and [Object](Object.md "Object") components.

##  Display Flag for Network Backdrop and Viewer Panes

Turning on an operator's Display flag will allow the OP's data to be viewed in a [Viewer](Viewer.md "Viewer") pane (ie [TOP Viewer](../TOPs/TOP_Viewer.md "TOP Viewer"), [SOP Viewer](https://docs.derivative.ca/SOP_Editor "SOP Editor"), [CHOP Viewer](CHOP_Viewer.md "CHOP Viewer"), or [Geometry Viewer](../Interoperability/Geometry_Viewer.md "Geometry Viewer") respectively).

If a [Network Editor](Network_Editor.md "Network Editor") pane has the backdrop display option enabled, then the OPs of that type with their display flags on will be shown in the backdrop of the editing pane. The network will 'float' on top. Backdrop display is enabled using the network editor's right-click menu, **Display > Backdrop TOPs** (or Backdrop CHOPs/Backdrop Geometry).
[![Backdrops.png](https://docs.derivative.ca/images/4/42/Backdrops.png)](https://docs.derivative.ca/File:Backdrops.png)
See also [Render Flag](Render_Flag.md "Render Flag") and [Flag](Flag.md "Flag").

##  Display Flag for Geometry and Camera Viewers

The same Display flag on 3D components is used to select objects to view in a Camera component, and in the parent's viewer.

The blue [flag](Flag.md "Flag") on Geometry components and SOP operators determines if the geometry contained in that operator is visible in node viewers and geometry viewer panes. See [Render Flag](Render_Flag.md "Render Flag").

The Backdrop is the grid of node viewers that are visible behind the [Network](Network.md "Network"), set by turning on Display Flags and the network RMB -> Display... Backdrop OPs.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](Geometry_COMP.md "Geometry COMP").
