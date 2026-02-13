---
url: https://docs.derivative.ca/Component
category: COMPs
title: Component
---

# Component

## Summary

[![Component.png](https://docs.derivative.ca/images/4/40/Component.png)](https://docs.derivative.ca/File:Component.png)
See also [Category:Components](https://docs.derivative.ca/index.php?title=Category:Components&action=edit&redlink=1 "Category:Components \(page does not exist\)") for a full list of articles related to Components.
**Components** (or **COMPs**) are unique compared to other operator families in that they contain their own networks. To make a new network in your project, create a new Component using the [OP Create Menu](https://docs.derivative.ca/OP_Create_Menu "OP Create Menu") and select from the **COMP** tab. Then go inside your new component and start building your network. Component networks can contain operators and/or additional sub-networks (additional components). Sub-networks create a hierarchy of networks that can be navigated (using the [network path](https://docs.derivative.ca/Network_Path "Network Path")) and forms the overall hierarchical structure of `.toe`/`.tox` files.

[![Opcreate COMP.jpg](https://docs.derivative.ca/images/9/9c/Opcreate_COMP.jpg)](https://docs.derivative.ca/File:Opcreate_COMP.jpg)
[COMP Class](https://docs.derivative.ca/COMP_Class "COMP Class")

##  Component Types
There are two special sub-[Families](https://docs.derivative.ca/Operator_Family "Operator Family") of components: [Object Components](https://docs.derivative.ca/Object "Object") and [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component"), as well as numerous other components. These are listed in four separate columns in the OP Create Menu.
###  Object Components (3D objects for rendering)[")]
  * [Ambient Light COMP](https://docs.derivative.ca/Ambient_Light_COMP "Ambient Light COMP")
  * [Blend COMP](https://docs.derivative.ca/Blend_COMP "Blend COMP")
  * [Bone COMP](https://docs.derivative.ca/Bone_COMP "Bone COMP")
  * [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP")
  * [Camera Blend COMP](https://docs.derivative.ca/Camera_Blend_COMP "Camera Blend COMP")
  * [Environment Light COMP](https://docs.derivative.ca/Environment_Light_COMP "Environment Light COMP")
  * [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP")
  * [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP")
  * [Handle COMP](https://docs.derivative.ca/Handle_COMP "Handle COMP")
  * [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP")
  * [Null COMP](https://docs.derivative.ca/Null_COMP "Null COMP")
  * [Shared Mem In COMP](https://docs.derivative.ca/Shared_Mem_In_COMP "Shared Mem In COMP")
  * [Shared Mem Out COMP](https://docs.derivative.ca/Shared_Mem_Out_COMP "Shared Mem Out COMP")
  * [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP")
  * [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP")

Object components can be parented in a hierarchy by connecting them together vertically (using their connectors on the top and bottom of the nodes).
 [ObjectCOMP_Class](https://docs.derivative.ca/ObjectCOMP_Class "ObjectCOMP Class")
###  Panel Components (interactive 2D panels)[")]
  * [Button COMP](https://docs.derivative.ca/Button_COMP "Button COMP")
  * [Container COMP](https://docs.derivative.ca/Container_COMP "Container COMP")
  * [Field COMP](https://docs.derivative.ca/Field_COMP "Field COMP")
  * [List COMP](https://docs.derivative.ca/List_COMP "List COMP")
  * [OP Viewer COMP](https://docs.derivative.ca/OP_Viewer_COMP "OP Viewer COMP")
  * [Parameter COMP](https://docs.derivative.ca/Parameter_COMP "Parameter COMP")
  * [Select COMP](https://docs.derivative.ca/Select_COMP "Select COMP")
  * [Slider COMP](https://docs.derivative.ca/Slider_COMP "Slider COMP")
  * [Table COMP](https://docs.derivative.ca/Table_COMP "Table COMP")
  * [Widget COMP](https://docs.derivative.ca/Widget_COMP "Widget COMP")

Panel components can be parented in a hierarchy by connecting them together vertically (using their connectors on the top and bottom of the nodes).
 [PanelCOMP_Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class")
###  Miscellaneous Components
  * [Base COMP](https://docs.derivative.ca/Base_COMP "Base COMP") - the Base COMP has no panel gadgets and no object gadgets. It is the most basic shell of a component and can be used when a new network is required.
  * [Engine COMP](https://docs.derivative.ca/Engine_COMP "Engine COMP") - the Engine COMP will run a .tox file (component) in a separate process.
  * [Time COMP](https://docs.derivative.ca/Time_COMP "Time COMP") - the Time COMP contains a network of operators that can drive a Timeline, drive animations in Animation COMPs, or be used to drive any custom time-based system.
  * [Animation COMP](https://docs.derivative.ca/Animation_COMP "Animation COMP") - the Animation COMP is used to create keyframe animation data. Keyframed channels are stored inside the component and can be edited by scoping the Animation COMP in the [Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor").
  * [Replicator COMP](https://docs.derivative.ca/Replicator_COMP "Replicator COMP") - the Replicator COMP creates a node for every row of a table, adding and deleting nodes ("replicants") as the table changes.
  * [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") - the Window COMP create a separate floating application window. This can be used for [control panels](https://docs.derivative.ca/Panel_Component "Panel Component") or when outputting to [multiple monitors](https://docs.derivative.ca/Multiple_Monitors "Multiple Monitors").

###  Component Inputs and Outputs
Components can have operator inputs and outputs on the left/right sides of the node if their network contains In and/or Out operators (of most types: TOP, CHOP, SOP, DAT. e.g. In TOP and Out CHOP).
These allow operator data to flow in and out of the component's network, allowing a Component to share its internal data with other components, operators, and other parts of your project. Adding these OPs inside a Component will add alphanumerically-ordered inputs/outputs on the left/right side of the component that data can flow through. Inputs are on Component’s left side, outputs on the right.
[![ComponentInsOuts.jpg](https://docs.derivative.ca/images/2/26/ComponentInsOuts.jpg)](https://docs.derivative.ca/File:ComponentInsOuts.jpg)
An output preview window is displayed when the cursor is over one of the outputs of a component. [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") on output preview to see info about that output. [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") on output preview brings up OP Create menu.
####  Example
A noise component has been constructed to take a TOP, CHOP, and SOP input, apply noise to each one, then output the results. The component's internal network looks like this:
[![NoiseExampleInside.jpg](https://docs.derivative.ca/images/9/91/NoiseExampleInside.jpg)](https://docs.derivative.ca/File:NoiseExampleInside.jpg)
The image below shows how the inputs and outputs of the Component can be connected into a network.
[![NoiseExampleOutside.jpg](https://docs.derivative.ca/images/2/20/NoiseExampleOutside.jpg)](https://docs.derivative.ca/File:NoiseExampleOutside.jpg)

###  Component Flags
Components have the 4 common [Flags](https://docs.derivative.ca/index.php?title=Flags&action=edit&redlink=1 "Flags \(page does not exist\)") along their left side: the [Viewer Flag](https://docs.derivative.ca/Viewer_Flag "Viewer Flag"), the [Clone Immune Flag](https://docs.derivative.ca/Immune "Immune"), the [Cooking Flag](https://docs.derivative.ca/Cooking_Flag "Cooking Flag"), and the [Lock Flag](https://docs.derivative.ca/Lock_Flag "Lock Flag"). [Object Components](https://docs.derivative.ca/Object "Object") also have a [Bypass Flag](https://docs.derivative.ca/Bypass_Flag "Bypass Flag") and an additional 3 flags in their lower right corner: the [Pickable Flag](https://docs.derivative.ca/Pickable_Flag "Pickable Flag") (orange), the [Render Flag](https://docs.derivative.ca/Render_Flag "Render Flag") (purple), and the [Display Flag](https://docs.derivative.ca/Display_Flag "Display Flag") (blue).
###  Saving Components to Files
You can save out a Component into a [.tox file](https://docs.derivative.ca/.tox ".tox") with a RMB -> Save Component on the node. This is handy for sharing networks with other TouchDesigner users and projects. Any commonly-used tool or network you create in TouchDesigner is good candidate for a Component.
To embed other files, like images, into .tox files, see [Virtual File System (VFS)](https://docs.derivative.ca/Virtual_File_System "Virtual File System").

See Also [Category:Components](https://docs.derivative.ca/index.php?title=Category:Components&action=edit&redlink=1 "Category:Components \(page does not exist\)")
