---
url: https://docs.derivative.ca/Component
category: Glossary
title: Component
---

# Component

## Summary

[![Component.png](https://docs.derivative.ca/images/4/40/Component.png)](https://docs.derivative.ca/File:Component.png)
See also [Category:Components](https://docs.derivative.ca/index.php?title=Category:Components&action=edit&redlink=1 "Category:Components \(page does not exist\)") for a full list of articles related to Components.

**Components** (or **COMPs**) are unique compared to other operator families in that they contain their own networks. To make a new network in your project, create a new Component using the [OP Create Menu](OP_Create_Menu.md "OP Create Menu") and select from the **COMP** tab. Then go inside your new component and start building your network. Component networks can contain operators and/or additional sub-networks (additional components). Sub-networks create a hierarchy of networks that can be navigated (using the [network path](Network_Path.md "Network Path")) and forms the overall hierarchical structure of `.toe`/`.tox` files.

[![Opcreate COMP.jpg](https://docs.derivative.ca/images/9/9c/Opcreate_COMP.jpg)](https://docs.derivative.ca/File:Opcreate_COMP.jpg)
[COMP Class](../Python/COMP_Class.md "COMP Class")

##  Component Types

There are two special sub-[Families](Operator_Family.md "Operator Family") of components: [Object Components](Object.md "Object") and [Panel Components](Panel_Component.md "Panel Component"), as well as numerous other components. These are listed in four separate columns in the OP Create Menu.

###  Object Components (3D objects for rendering)[")]

  * [Ambient Light COMP](../COMPs/Ambient_Light_COMP.md "Ambient Light COMP")
  * [Blend COMP](../COMPs/Blend_COMP.md "Blend COMP")
  * [Bone COMP](../COMPs/Bone_COMP.md "Bone COMP")
  * [Camera COMP](Camera_COMP.md "Camera COMP")
  * [Camera Blend COMP](../COMPs/Camera_Blend_COMP.md "Camera Blend COMP")
  * [Environment Light COMP](../COMPs/Environment_Light_COMP.md "Environment Light COMP")
  * [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP")
  * [Geometry COMP](Geometry_COMP.md "Geometry COMP")
  * [Handle COMP](../COMPs/Handle_COMP.md "Handle COMP")
  * [Light COMP](Light_COMP.md "Light COMP")
  * [Null COMP](../COMPs/Null_COMP.md "Null COMP")
  * [Shared Mem In COMP](../COMPs/Shared_Mem_In_COMP.md "Shared Mem In COMP")
  * [Shared Mem Out COMP](../COMPs/Shared_Mem_Out_COMP.md "Shared Mem Out COMP")
  * [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP")
  * [USD COMP](../COMPs/USD_COMP.md "USD COMP")

Object components can be parented in a hierarchy by connecting them together vertically (using their connectors on the top and bottom of the nodes).

 [ObjectCOMP_Class](../Python/ObjectCOMP_Class.md "ObjectCOMP Class")

###  Panel Components (interactive 2D panels)[")]

  * [Button COMP](../COMPs/Button_COMP.md "Button COMP")
  * [Container COMP](Container_COMP.md "Container COMP")
  * [Field COMP](../COMPs/Field_COMP.md "Field COMP")
  * [List COMP](../COMPs/List_COMP.md "List COMP")
  * [OP Viewer COMP](../COMPs/OP_Viewer_COMP.md "OP Viewer COMP")
  * [Parameter COMP](../COMPs/Parameter_COMP.md "Parameter COMP")
  * [Select COMP](../COMPs/Select_COMP.md "Select COMP")
  * [Slider COMP](../COMPs/Slider_COMP.md "Slider COMP")
  * [Table COMP](../COMPs/Table_COMP.md "Table COMP")
  * [Widget COMP](../COMPs/Widget_COMP.md "Widget COMP")

Panel components can be parented in a hierarchy by connecting them together vertically (using their connectors on the top and bottom of the nodes).

 [PanelCOMP_Class](../Python/PanelCOMP_Class.md "PanelCOMP Class")

###  Miscellaneous Components

  * [Base COMP](../COMPs/Base_COMP.md "Base COMP") - the Base COMP has no panel gadgets and no object gadgets. It is the most basic shell of a component and can be used when a new network is required.
  * [Engine COMP](../COMPs/Engine_COMP.md "Engine COMP") - the Engine COMP will run a .tox file (component) in a separate process.
  * [Time COMP](Time_COMP.md "Time COMP") - the Time COMP contains a network of operators that can drive a Timeline, drive animations in Animation COMPs, or be used to drive any custom time-based system.
  * [Animation COMP](Animation_COMP.md "Animation COMP") - the Animation COMP is used to create keyframe animation data. Keyframed channels are stored inside the component and can be edited by scoping the Animation COMP in the [Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor").
  * [Replicator COMP](Replicator_COMP.md "Replicator COMP") - the Replicator COMP creates a node for every row of a table, adding and deleting nodes ("replicants") as the table changes.
  * [Window COMP](Window_COMP.md "Window COMP") - the Window COMP create a separate floating application window. This can be used for [control panels](Panel_Component.md "Panel Component") or when outputting to [multiple monitors](Multiple_Monitors.md "Multiple Monitors").

###  Component Inputs and Outputs

Components can have operator inputs and outputs on the left/right sides of the node if their network contains In and/or Out operators (of most types: TOP, CHOP, SOP, DAT. e.g. In TOP and Out CHOP).

These allow operator data to flow in and out of the component's network, allowing a Component to share its internal data with other components, operators, and other parts of your project. Adding these OPs inside a Component will add alphanumerically-ordered inputs/outputs on the left/right side of the component that data can flow through. Inputs are on Component’s left side, outputs on the right.
[![ComponentInsOuts.jpg](https://docs.derivative.ca/images/2/26/ComponentInsOuts.jpg)](https://docs.derivative.ca/File:ComponentInsOuts.jpg)
An output preview window is displayed when the cursor is over one of the outputs of a component. [MMB](Mouse_Click.md "Mouse Click") on output preview to see info about that output. [RMB](Mouse_Click.md "Mouse Click") on output preview brings up OP Create menu.

####  Example

A noise component has been constructed to take a TOP, CHOP, and SOP input, apply noise to each one, then output the results. The component's internal network looks like this:
[![NoiseExampleInside.jpg](https://docs.derivative.ca/images/9/91/NoiseExampleInside.jpg)](https://docs.derivative.ca/File:NoiseExampleInside.jpg)
The image below shows how the inputs and outputs of the Component can be connected into a network.
[![NoiseExampleOutside.jpg](https://docs.derivative.ca/images/2/20/NoiseExampleOutside.jpg)](https://docs.derivative.ca/File:NoiseExampleOutside.jpg)

###  Component Flags

Components have the 4 common [Flags](https://docs.derivative.ca/index.php?title=Flags&action=edit&redlink=1 "Flags \(page does not exist\)") along their left side: the [Viewer Flag](Viewer_Flag.md "Viewer Flag"), the [Clone Immune Flag](Immune.md "Immune"), the [Cooking Flag](https://docs.derivative.ca/Cooking_Flag "Cooking Flag"), and the [Lock Flag](Lock_Flag.md "Lock Flag"). [Object Components](Object.md "Object") also have a [Bypass Flag](Bypass_Flag.md "Bypass Flag") and an additional 3 flags in their lower right corner: the [Pickable Flag](https://docs.derivative.ca/Pickable_Flag "Pickable Flag") (orange), the [Render Flag](Render_Flag.md "Render Flag") (purple), and the [Display Flag](Display_Flag.md "Display Flag") (blue).

###  Saving Components to Files

You can save out a Component into a [.tox file](.tox.md ".tox") with a RMB -> Save Component on the node. This is handy for sharing networks with other TouchDesigner users and projects. Any commonly-used tool or network you create in TouchDesigner is good candidate for a Component.

To embed other files, like images, into .tox files, see [Virtual File System (VFS)](Virtual_File_System.md "Virtual File System").

See Also [Category:Components](https://docs.derivative.ca/index.php?title=Category:Components&action=edit&redlink=1 "Category:Components \(page does not exist\)")
