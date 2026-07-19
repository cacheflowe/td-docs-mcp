---
url: https://docs.derivative.ca/TouchDesigner_Glossary
category: General
title: TouchDesigner_Glossary
---

# TouchDesigner Glossary

##  Learn to Speak the Language of TouchDesigner

**[.toe](../Glossary/.toe.md ".toe")** : TOuch Environment file, the file type used by TouchDesigner to save your entire project.

**[.tox](../Glossary/.tox.md ".tox")** : TouchDesigner Component file, the file type used to save a [Component](../Glossary/Component.md "Component") of your TouchDesigner project.

**[3D Texture](../Glossary/Learning_About_POPs.md "Learning About POPs")** : 2D texture array or 3D gridof pixels.

**[Absolute Time](../Glossary/Absolute_Time.md "Absolute Time")** or **[absTime](../Glossary/Absolute_Time.md "Absolute Time")** : Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off or the root timeline is paused.

**[Adaptive Homing](../Glossary/Viewer.md "Viewer")** : In the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer") of a Geometry COMP or any POP, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position.

**[Adaptive Homing](../Glossary/Learning_About_POPs.md "Learning About POPs")** : In the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer") of a Geometry COMP or POP, the Adaptive Homing option will keep in-view the 3D geometry being displayed.

**[Annotate](../Glossary/Annotate_COMP.md "Annotate COMP")** or **[Annotation](../Glossary/Annotate_COMP.md "Annotate COMP")** : Annotates are displayed in the Network Editor as colored rectangles containing user-authored text and graphics. It is based on the [Annotate COMP](../Glossary/Annotate_COMP.md "Annotate COMP") and allows you to document your networks with useful information like comments and node grouping.

**[Array Attribute](../Glossary/Array_Attribute.md "Array Attribute")** : An Array Attribute is an [Attribute](../Glossary/Attribute.md "Attribute") with multiple **elements** of a chosen **Attribute Data Type**, for example an attribute made of 12 integers.

**[Attribute](../Glossary/Attribute.md "Attribute")** : Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

**[Backdrop](../Glossary/Backdrop.md "Backdrop")** : The Backdrop is the grid of node viewers that are visible behind the [Network](../Glossary/Network.md "Network"), set by turning on [Display Flags](../Glossary/Display_Flag.md "Display Flag") and the network RMB -> Display... Backdrop OPs.

**[Binding](../Glossary/Binding.md "Binding")** : Binding is a [Parameter Mode](../Glossary/Parameter_Mode.md "Parameter Mode") that ties two or more parameters' values together, where changing the value of any one of the bound parameters changes all of them. The actual value is stored in one place.

**[Bookmarks](../Glossary/Bookmark.md "Bookmark")** : A pull-down list at the top of a network [Pane](../Glossary/Pane.md "Pane") containing jump-to [Network Paths](../Glossary/Network_Path.md "Network Path").

**[Bypass](../Glossary/Bypass_Flag.md "Bypass Flag")** or **[Bypass Flag](../Glossary/Bypass_Flag.md "Bypass Flag")** : An operator whose Bypass flag is set does nothing: All data going into its first input appears at its output unaffected.

**[Callback](../Glossary/Callback.md "Callback")** : Some operators have a DAT [docked](../Glossary/Docking.md "Docking") to them that contains some python functions. These functions, called "callbacks", get called when something in the operator changes.

**[Channel](../Glossary/Channel.md "Channel")** : A [CHOP](../Glossary/CHOP.md "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](../Glossary/Sample.md "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](../Glossary/Export.md "Export") to [Parameters](../Glossary/Parameter.md "Parameter").

**[CHOP](../Glossary/CHOP.md "CHOP")** or **[Channel Operator](../Glossary/CHOP.md "CHOP")** : An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

**[Clone](../Glossary/Clone.md "Clone")** : Cloning makes multiple components match the contents of a master component. A [Component](../Glossary/Component.md "Component") whose Clone parameter is set will be forced to contain the same nodes, wiring and parameters as its master component. Cloning does not create new components as does the [Replicator COMP](../Glossary/Replicator_COMP.md "Replicator COMP").

**[Component](../Glossary/Component.md "Component")** or **[COMP](../Glossary/Component.md "Component")** : An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

**[Connector](../Glossary/Connector.md "Connector")** : The notches on the left and right of each [Node](../Glossary/Node.md "Node") that let you [Wire](../Glossary/Wire.md "Wire") the output of one [Operator](Operator.md "Operator") to the input of another of the same [Operator Family](Operator.md "Operator"). The notches on the top and bottom of [3D Object Components](../Glossary/Object.md "Object") and [Panel Components](../Glossary/Panel_Component.md "Panel Component") that tie the components of each sub-[Family](../Glossary/Operator_Family.md "Operator Family") in a [Hierarchy](../Glossary/Hierarchy.md "Hierarchy").

**[Container](../Glossary/Container_COMP.md "Container COMP")** : The Container component type is a [Panel Component](../Glossary/Panel_Component.md "Panel Component") that holds, lays out and displays any number of other Panel Components.

**[Cook](../Glossary/Cook.md "Cook")** : To re-compute the output data of the [Operators](Operator.md "Operator"). An operator cooks when (1) its inputs change, (2) its [Parameters](../Glossary/Parameter.md "Parameter") change, (3) when the timeline moves forward in some cases, or (4) [Scripting](../Glossary/Script.md "Script") commands are run on the node. When the operator is a [Panel Component](../Glossary/Panel_Component.md "Panel Component"), it also cooks when a user interacts with it. When an operator cooks, it usually causes operators connected to its output to re-cook. When TouchDesigner draws the screen, it re-cooks all the [Dependencies](../Glossary/Dependency.md "Dependency") - the necessary operators in all [Networks](../Glossary/Network.md "Network"), contributing to a frame's total "cook time".

**[DAT](../Glossary/DAT.md "DAT")** or **[Data Operator](../Glossary/DAT.md "DAT")** : An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](../Glossary/Script.md "Script") or [GLSL](../Glossary/GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](../Glossary/Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

**[Dependency](../Glossary/Dependency.md "Dependency")** : is the [Procedural](../Glossary/Procedural.md "Procedural") mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](../Glossary/Cook.md "Cook").

**[Dependency](../Glossary/Learning_About_POPs.md "Learning About POPs")** or **[Dependable](../Glossary/Learning_About_POPs.md "Learning About POPs")** : applies to python objects, parameters, nodes.

**[Designer Mode](../Glossary/Designer_Mode.md "Designer Mode")** : You edit your networks in Designer Mode. See [Perform Mode](../Glossary/Perform_Mode.md "Perform Mode").

**[Dialog](../Glossary/Dialog.md "Dialog")** : Any floating window that is not a [Pane](../Glossary/Pane.md "Pane") or [Viewer](../Glossary/Viewer.md "Viewer").

**[Dimension](../Glossary/Dimension.md "Dimension")** : Dimension is metadata of a POP that describes the structure of the point list, which may be arranged as rows and columns of points (which is two dimensions of size _nrows_ and _ncolumns_).

**[Display Flag](../Glossary/Display_Flag.md "Display Flag")** : The blue [flag](../Glossary/Flag.md "Flag") on Geometry components and SOP operators determines if the geometry contained in that operator is visible in node viewers and geometry viewer panes. See [Render Flag](../Glossary/Render_Flag.md "Render Flag").

**[Docking](../Glossary/Docking.md "Docking")** or **[Docked](../Glossary/Docking.md "Docking")** : Any [node](../Glossary/Node.md "Node") can be docked to another node. This helps organize networks as two node that are docked together will stay together when the dock parent is moved in a network editor. A docked node can be collapsed into a small icon under the dock parent, reducing network clutter.

**[Event](../Glossary/Event.md "Event")** : Events are single-moment occurrences that are generated from a variety of conditions - from input actions that a user causes, from external devices and software, and from internal TouchDesigner states. A wide set of operator types respond to events and give the user a place to write python code that reacts to events.

**[Export](../Glossary/Export.md "Export")** : Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](../Glossary/CHOP_Viewer.md "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](../Glossary/Parameter.md "Parameter").

**[Expression](../Glossary/Expression.md "Expression")** : A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](../Glossary/DAT.md "DAT") and in scripts.

**[Extend Conditions](../Glossary/Extend_Conditions.md "Extend Conditions")** or **[Extend Region](../Glossary/Extend_Conditions.md "Extend Conditions")** : In CHOPs, Extend Conditions determine what numbers you get when you try to get a channel value that is outside its start-end range - in its Extend Regions.

**[Extensions](../Glossary/Extensions.md "Extensions")** : Any component can be extended with its own Python classes which contain python functions and data.

**[File Metadata](../Glossary/File_Metadata.md "File Metadata")** : Read and write different types of file metadata.

**[Filter](../Glossary/Filter.md "Filter")** : Operators that need 1 or more inputs are called Filters in TouchDesigner, like a Math CHOP. See [Generator](../Glossary/Generator.md "Generator").

**[Filter per Sample](../Glossary/Filter_per_Sample.md "Filter per Sample")** : A powerful feature of CHOPs that filter over time, like the [Lag CHOP](../Glossary/Lag_CHOP.md "Lag CHOP") and [Filter CHOP](../Glossary/Filter_CHOP.md "Filter CHOP") where each sample acts as its own filter.

**[Flag](../Glossary/Flag.md "Flag")** : Indicator of certain states of an operator (Bypass flag, Render flag, Lock flag, Viewer Active flag).

**[Folder](../Glossary/Folder.md "Folder")** : A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](../Glossary/Network_Path.md "Network Path").

**[Frame](../Glossary/Frame.md "Frame")** : The term "Frame" is a measurement of time used (1) in the [Timeline](../Glossary/Timeline.md "Timeline"), (2) as a time-unit in CHOPs, and (3) as a time unit in movie files that are read into [TOPs](../TOPs/TOP.md "TOP") and written out from TOPs. The [Frame Rate](../Glossary/Frame_Rate.md "Frame Rate") is the frames per second (FPS).

**[Frame Rate](../Glossary/Frame_Rate.md "Frame Rate")** or **[FPS](../Glossary/Frame_Rate.md "Frame Rate")** : The [Frames](../Glossary/Frame.md "Frame")-per-Second that TouchDesigner's [Timeline](../Glossary/Timeline.md "Timeline") runs at. Set with `project.cookRate`.

**[Generator](../Glossary/Generator.md "Generator")** : Operators that do not need any inputs connected are called Generators in TouchDesigner, like a Pattern CHOP. See [Filter](../Glossary/Filter.md "Filter").

**[Geometry](../Glossary/Geometry_COMP.md "Geometry COMP")** : The 3D data held in POPs and passed for rendering by the [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP").

**[Geometry Spreadsheet](../Glossary/Geometry_Spreadsheet.md "Geometry Spreadsheet")** : Currently, use a [SOP to DAT](../Glossary/SOP_to_DAT.md "SOP to DAT") to look at SOP point/polygon XYZ and other attributes. Formerly a [Pane](../Glossary/Pane.md "Pane") type.

**[Geometry Viewer](../Interoperability/Geometry_Viewer.md "Geometry Viewer")** : A 3D viewport for viewing and manipulating 3D scenes or objects interactively. A geometry viewer can be found in [Panes](../Glossary/Pane.md "Pane") (alt+3 in any pane) or the [Node Viewers](../Glossary/Node_Viewer.md "Node Viewer") of all Geometry Object components.

**[Global OP Shortcut](../Glossary/Global_OP_Shortcut.md "Global OP Shortcut")** : A name for a component that is accessible from any node in a project, which can be declared in a component's Global Operator Shortcut parameter.

**[GPU](../Glossary/GPU.md "GPU")** : The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

**[Group](../Glossary/Group.md "Group")** : A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

**[Hierarchy](../Glossary/Hierarchy.md "Hierarchy")** : Hierarchy relates components with other components. There are two groups of Hierarchy in TouchDesigner. 3D Object Components, and 2D Panel Components. Hierarchies let one component to be positioned relative to another. Each group can be connected via lines between the bottoms/tops of nodes in a network, or by placing one component inside the other.

**[Immune](../Glossary/Immune.md "Immune")** : Every node has an [Immune Flag](../Glossary/Immune_Flag.md "Immune Flag"), when on and the node is inside a [Clone](../Glossary/Clone.md "Clone"), it is not affected by any change to the clone master, so you can store extra data in the clone or set a node to be ignored by the cloning process.

**[Index and ID](../Glossary/Learning_About_POPs.md "Learning About POPs")** : Index is where a point is in a point list and is not an attribute. ID is often an attribute used for particles and has no order, has unique value, and can be reused.

**[Input Block](../Glossary/Learning_About_POPs.md "Learning About POPs")** : POPs that take unlimited inputs have one seq block of parameters per input. An input can be a pattern of OPs.

**[Instance](../Glossary/Instance.md "Instance")** : (1) A [Geometry Component](../Glossary/Geometry_COMP.md "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

**[Internal Operators](../Glossary/Internal_Operators.md "Internal Operators")** : Internal Operators (iOPs) provide a simple shortcut to a frequently-used operator, accessing from anywhere in that component.

**[Internal Parameters](../Glossary/Internal_Parameters.md "Internal Parameters")** : Internal Parameters (iPars) act like local variables in a component. They provide a simple shortcut to collections of parameters that you create within a component, and access from anywhere in that component.

**[Interoperability](Interoperability.md "Interoperability")** or **[Interops](Interoperability.md "Interoperability")** : The devices, protocols and software tools that TouchDesigner interfaces to, via native [Operators](Operator.md "Operator") and [Palette](../Learn/Palette.md "Palette") components.

**[Keyboard Shortcuts](../Glossary/Keyboard_Shortcuts.md "Keyboard Shortcuts")** : There are two types of keyboard shortcuts: [Application Shortcuts](../Glossary/Application_Shortcuts.md "Application Shortcuts") that are built-in to TouchDesigner's authoring interface, and [Panel Shortcuts](../Glossary/Panel_Shortcuts.md "Panel Shortcuts") that you create for any custom built panels.

**[Keyframe](../Glossary/Keyframe.md "Keyframe")** : In the [Animation component](../Glossary/Animation_COMP.md "Animation COMP") each keyframe specifies a channel's value at a specific time (or frame). A keyframe holds a value, slopes and accelerations, and an interpolation type. A channel's keyframes are used to interpolate and determine the values of all the samples of the channel.

**[Layout](../Glossary/Layout.md "Layout")** : (1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](../Glossary/Timeline.md "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](../Glossary/Pane.md "Pane") and [Bookmark](../Glossary/Bookmark.md "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.

**[Line Strip](../Glossary/Learning_About_POPs.md "Learning About POPs")** : A primitive in POPs that has 1 or more connected points.

**[Link](../Glossary/Link.md "Link")** or **[Reference](../Glossary/Link.md "Link")** : A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](../Glossary/Export.md "Export"), node [Paths](../Glossary/Network_Path.md "Network Path") in parameters, and [expressions](../Glossary/Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](../Glossary/Wire.md "Wire") that connects nodes in the same [Operator Family](../Glossary/Operator_Family.md "Operator Family").

**[Lock Flag](../Glossary/Lock_Flag.md "Lock Flag")** : When an operator is locked, it does not [cook](../Glossary/Cook.md "Cook") and its output data remains frozen, even when the TouchDesigner session is saved to a [.toe](../Glossary/.toe.md ".toe") file and restarted.

**[Macro](../Glossary/Macro.md "Macro")** : The F1 to F12 keys run macros. The F1 macro puts you in [Perform Mode](../Glossary/Perform_Mode.md "Perform Mode"). Pressing F9 or F10 over a panel brings up the network of the panel element you are pointing at. Macros are written in the legacy [Tscript](../Glossary/Tscript.md "Tscript").

**[Map Point Attributes to Parameters](../Glossary/Mapping_POP_Attributes_to_Parameters.md "Mapping POP Attributes to Parameters")** : On some parameters of some POPs, you can have a different parameter value for each point of the POP by mapping one of its [Attributes](../Glossary/Attribute.md "Attribute") to a parameter via a Map page on the parameter dialog.

**[MAT](../MATs/MAT.md "MAT")** or **[Material](../MATs/MAT.md "MAT")** : MATs or Materials are an [Operator Family](../Glossary/Operator_Family.md "Operator Family") that applies a [Shader](../Glossary/Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

**[Menu Bar](../Glossary/Menu_Bar.md "Menu Bar")** : The bar at the top of the [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode") interface that contains menus, links, status messages and other controls.

**[MultiTouch](../Glossary/MultiTouch.md "MultiTouch")** or **[Multi-Touch](../Glossary/MultiTouch.md "MultiTouch")** : Display devices in TouchDesigner that support multiple-finger or control-point input.

**[Network](../Glossary/Network.md "Network")** : Every component contains a network of operators that create and modify data. The operators are connected by wires that define where data is routed after the operator cooks its inputs and generates an output.

**[Network Editor](../Glossary/Network_Editor.md "Network Editor")** : A pane type where networks of operators can be created and edited.

**[Node](../Glossary/Node.md "Node")** : The generic thing that holds an [Operator](Operator.md "Operator"), and includes [Flags](../Glossary/Flag.md "Flag") (display, bypass, lock, render, immune) and its position/size in the network. Whether you "lay down an Operator" or "lay down an Node", you're doing the same thing.

**[Node Viewer](../Glossary/Node_Viewer.md "Node Viewer")** : The viewer found on each operator in a [Network Editor](../Glossary/Network_Editor.md "Network Editor") pane. This viewer is turned on by clicking the [Viewer Flag](../Glossary/Viewer_Flag.md "Viewer Flag").

**[Normal](../Glossary/Learning_About_POPs.md "Learning About POPs")** : shared points, normals on shared points, unique points, recalculate.

**[Object](../Glossary/Object.md "Object")** or **[3D Object](../Glossary/Object.md "Object")** or **[Object Space](../Glossary/Object.md "Object")** : The sub-[Family](../Glossary/Operator_Family.md "Operator Family") of [Component](../Glossary/Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](../Glossary/Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP") and [Light COMP](../Glossary/Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

**[OP Create Menu](../Glossary/OP_Create_Menu.md "OP Create Menu")** : The menu used to select and create a new operator. Can be opened in the [Network Editor](../Glossary/Network_Editor.md "Network Editor") by pressing the <tab> key or double-clicking the background, or by clicking the [MMB](../Glossary/Mouse_Click.md "Mouse Click") or [RMB](../Glossary/Mouse_Click.md "Mouse Click") on an operator's output connector, or by the **+** sign in the [Pane Bar](../Glossary/Pane.md "Pane").

**[OP](Operator.md "Operator")** or **[Operator](Operator.md "Operator")** : Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

**[Operator Family](../Glossary/Operator_Family.md "Operator Family")** or **[Family](../Glossary/Operator_Family.md "Operator Family")** : The Operator Families are [TOPs](../TOPs/TOP.md "TOP"), [CHOPs](../Glossary/CHOP.md "CHOP"), [POPs](../POPs/POP.md "POP") (Point Operators), [MATs](../MATs/MAT.md "MAT") (Materials), [DATs](../Glossary/DAT.md "DAT") (data operators), [SOPs](../SOPs/SOP.md "SOP") and [Components](../Glossary/Component.md "Component") (Panel Gadgets and Objects).

**[Palette](../Learn/Palette.md "Palette")** : A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.

**[Pane](../Glossary/Pane.md "Pane")** : A work area in TouchDesigner's layout that includes the [Network Editor](../Glossary/Network_Editor.md "Network Editor") and 7 other pane types used for different tasks. The TouchDesigner interface can consist of a single pane, or be split into multiple panes.

**[Pane Type](../Glossary/Pane.md "Pane")** : There are 8 pane types; Network, Panel, Textport, Geometry Viewer, TOP Viewer, CHOP Viewer, Parameters, Graph Editor for CHOP Channels, or a Geometry Spreadsheet.

**[Panel Component](../Glossary/Panel_Component.md "Panel Component")** : The sub-[Family](../Glossary/Operator_Family.md "Operator Family") of [Components](../Glossary/Component.md "Component") that are used to create custom interactive 2D control [panels](../Glossary/Panel.md "Panel") (Container, Widget, Text COMP Slider, Button, etc.).

**[Panel Value](../Glossary/Panel_Value.md "Panel Value")** : The internal states of a panel component are Panel Values, and are accessed with a Panel CHOP, a `OP.panel` Python expression, or a [Panel Execute DAT](../Glossary/Panel_Execute_DAT.md "Panel Execute DAT").

**[Panel](../Glossary/Panel.md "Panel")** or **[Control Panel](../Glossary/Panel.md "Panel")** : A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](../Glossary/Panel_Component.md "Panel Component").

**[Parameter](../Glossary/Parameter.md "Parameter")** : Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](../Glossary/Network_Path.md "Network Path"), which determine the output of the operator.

**[Parameter Dialog](../Glossary/Parameter_Dialog.md "Parameter Dialog")** : A floating dialog, pane type, or dialog in a Network Editor that displays one operator's parameters.

**[Parameter Expression](../Glossary/Parameter_Expression.md "Parameter Expression")** : A parameter expression is a python expression that is in the expression field of a parameter.

**[Parameter Mode](../Glossary/Parameter_Mode.md "Parameter Mode")** : Every Parameter can be in one of four modes: Constant Mode, [Expression](../Glossary/Expression.md "Expression") Mode, [Export](../Glossary/Export.md "Export") Mode or Bind ([Binding](../Glossary/Binding.md "Binding")) Mode.

**[Parameter Reference](../Glossary/Parameter_Reference.md "Parameter Reference")** : A parameter reference can be setup between any two parameters by putting an expression in one parameter that refers to another parameter. This creates a [Link](../Glossary/Link.md "Link") between the two parameters such that when one changes, the other will change automatically (known in other software as a "constraint").

**[Parameter Size](../Glossary/Learning_About_POPs.md "Learning About POPs")** : In a parameter dialog, Setting Parameter Size to 3 gives 3 columns of parameters to control X Y and Z separately for example.

**[Parameter Value](../Glossary/Parameter.md "Parameter")** : Parameter Value refers to the constant, the expression, the export, the bind reference and the [Parameter Mode](../Glossary/Parameter_Mode.md "Parameter Mode") that are used together to determine the "evaluated" parameter value.

**[Parent](../Glossary/Parent.md "Parent")** : There are 2 kinds of parenting. The "parent component" is the component in which a node resides. The metaphor is extended to include grand parents, grand-grand parents, etc. The root `/` is the ultimate parent to all nodes. See also [3D Parenting](../Glossary/3D_Parenting.md "3D Parenting") and panel [Parenting](../Glossary/Parent.md "Parent").

**[Parent Shortcut](../Glossary/Parent_Shortcut.md "Parent Shortcut")** : A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.

**[ParGroup](../Glossary/ParGroup.md "ParGroup")** or **[Parameter Group](../Glossary/ParGroup.md "ParGroup")** : A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.

**[Path](../Glossary/Network_Path.md "Network Path")** or **[Network Path](../Glossary/Network_Path.md "Network Path")** : The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](../Glossary/Root.md "Root"). This path is displayed at the top of every [Pane](../Glossary/Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](../Glossary/Folder.md "Folder").

**[Pattern Expansion](../Glossary/Pattern_Expansion.md "Pattern Expansion")** : Pattern Expansion takes a short string and expands it to generate a longer string of individual elements.

**[Pattern Matching](../Glossary/Pattern_Matching.md "Pattern Matching")** : Matching names using wildcard characters and bracketing. Useful in "[Select](../Glossary/Select_CHOP.md "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

**[Pattern Replacement](../Glossary/Pattern_Replacement.md "Pattern Replacement")** : Used in conjunction with Pattern Matching to replace all or portions of matched strings with new data. Used in places such as the [Rename CHOP](../Glossary/Rename_CHOP.md "Rename CHOP").

**[Perform Mode](../Glossary/Perform_Mode.md "Perform Mode")** : Perform Mode is an optimized mode for live performance that only renders one specified [Window COMP](../Glossary/Window_COMP.md "Window COMP") which is one window that contains your video outputs and your (optional) control interface. In Perform Mode the network editing window is not open - you edit your networks in [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode"). Alternate with F1 and Esc.

**[Performance Monitor](../Glossary/Performance_Monitor.md "Performance Monitor")** : The tool built-in to TouchDesigner that analyzes and displays what TouchDesigner is doing as it generates the output images, audio and data.

**[Pipe](../Glossary/Pipe.md "Pipe")** : A way of moving data from one TouchDesigner process to another. Images are moved via Touch Out / In TOPs, channels are moved via Touch Out / In CHOPs and Pipe Out / In CHOPs. Data moves via TCP/IP or UDP.

**[Playbar](../Glossary/Timeline.md "Timeline")** : Playbar is the former name for Timeline. See [Timeline](../Glossary/Timeline.md "Timeline").

**[Point](../Glossary/Point.md "Point")** : Each POP and SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](../Glossary/Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

**[Polygon](../Glossary/Polygon.md "Polygon")** : A polygon is a type of [Primitive](../Glossary/Primitive.md "Primitive") that is formed from a set of [Vertices](../Glossary/Vertex.md "Vertex") in 3D that are implicitly connected together to form a multi-edge shape.

**[POP](../POPs/POP.md "POP")** or **[Point Operators](../POPs/POP.md "POP")** : POPs (Point Operators) is a new [Operator Family](../Glossary/Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

**[Popup Help](../Glossary/Popup_Help.md "Popup Help")** : Help messages appear when (1) moving the cursor over the TouchDesigner user interface, (2) clicking the ? help button on the corner of each operator's Parameters page, (3) holding the Alt key while moving the cursor over the parameter names in the Parameter Dialogs, and (4) evaluating selected text in parameter expressions.

**[Primitive](../Glossary/Primitive.md "Primitive")** : A surface type in [POPs](../POPs/POP.md "POP") and [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](../Glossary/Point.md "Point") and Primitives are part of the [Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").

**[Privacy](../Glossary/Privacy.md "Privacy")** : Privacy of TouchDesigner Components (`.tox` files) or Projects (`.toe` files) is the protection of networks that enables them to be used but not be visible or editable.

**[Procedural](../Glossary/Procedural.md "Procedural")** : Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. It is the chain-reaction mechanism of TouchDesigner, where if one piece of data changes, it automatically causes other "[dependent](../Glossary/Dependency.md "Dependency")" operators and expressions to re-[Cook](../Glossary/Cook.md "Cook") and re-generate the outputs.

**[Projection Mapping](../Learn/Projection_Mapping.md "Projection Mapping")** : A technique or workflow that allows for displaying content on often irregular shapes and surfaces.

**[Pulse](../Glossary/Pulse.md "Pulse")** : To "pulse" a parameter is to send it a signal from (1) an [exported](../Glossary/Export.md "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately. A pulse via python is via the `.pulse()` function on a pulse-type parameter, such as Reset parameter in a [Speed CHOP](../Glossary/Speed_CHOP.md "Speed CHOP"). A pulse from a CHOP is typically a 0 to 1 to 0 signal in an exported channel.

**[Quad Reprojection](../Glossary/Quad_Reprojection.md "Quad Reprojection")** : Quad Reprojection renders pixel-perfect perspective-correct images for flat TVs and LED panels hung at any orientation.

**[Reference](../Glossary/Reference.md "Reference")** : The grey dashed lines between nodes is a Reference (or [Link](../Glossary/Link.md "Link")). A Reference is (1) a [Parameter Reference](../Glossary/Parameter_Reference.md "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.

**[Reference](../Glossary/Link.md "Link")** or **[Link](../Glossary/Link.md "Link")** : A [Link](../Glossary/Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](../Glossary/Operator_Family.md "Operator Family").

**[Render Flag](../Glossary/Flag.md "Flag")** : The purple flag on COMP and SOP nodes that determines if the node will be rendered in a [Render TOP](../TOPs/Render_TOP.md "Render TOP") or [Render Pass TOP](../TOPs/Render_Pass_TOP.md "Render Pass TOP"). The operator must also be listed in the Render / Render Pass TOP's 'Geometry' parameter.

**[Rendering](../Glossary/Rendering.md "Rendering")** : Rendering is the creation of a 3D image with the Render TOP. Rendering is also used more generally to include the compositing (with TOPs) to generate an output image.

**[Replicator](../Glossary/Replicator_COMP.md "Replicator COMP")** : Creates copies of a component, one for every row in a table or using a Number of Replicants parameter - it is the "for-loop" of operators. Unlike [Clone](../Glossary/Clone.md "Clone"), it automatically creates copies of a master component.

**[Resolution](../TOPs/Resolution_TOP.md "Resolution TOP")** : The width and height of an image in pixels. Most TOPs, like the [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") can set the image resolution. See [Aspect Ratio](../Glossary/TOP_Generator_Common_Page.md "TOP Generator Common Page") for the width/height ratio of an image, taking into account non-square pixels.

**[RMB Menu](../Glossary/RMB_Menu.md "RMB Menu")** : The menu that appears when clicking the right mouse button on different parts of TouchDesigner. (Sometimes you need to be holding down Ctrl.)

**[Root](../Glossary/Root.md "Root")** : TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](../Glossary/Network_Path.md "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.

**[Sample Rate](../Glossary/CHOP.md "CHOP")** or **[Sample](../Glossary/CHOP.md "CHOP")** : samples-per-second of a [CHOP](../Glossary/CHOP.md "CHOP"). Each CHOP in your network has a sample rate. In contrast, the overall timeline has a [Frame Rate](../Glossary/Frame_Rate.md "Frame Rate"), which is the number of frames to [cook](../Glossary/Cook.md "Cook") and display per second, generally your monitor display frequency, default 60.

**[Scope](../Glossary/Scope.md "Scope")** : A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

**[Script](../Glossary/Script.md "Script")** : A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](Python.md "Python") and the original [Tscript](../Glossary/Tscript.md "Tscript"). Scripts and single-line commands can also be run in the [Textport](../Glossary/Textport.md "Textport").

**[Sequential Parameters](../Glossary/Sequential_Parameters.md "Sequential Parameters")** or **[Sequence Blocks](../Glossary/Sequential_Parameters.md "Sequential Parameters")** : Sequential Parameters are blocks of parameters (Sequential Blocks) that can be reproduced multiple times by a user to create multiple entities.

**[Shader](../Glossary/Shader.md "Shader")** : The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](../Glossary/Text_DAT.md "Text DAT") and referenced by a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.

**[Shortcut](../Glossary/Operator_Shortcuts.md "Operator Shortcuts")** : Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](../Glossary/Parent_Shortcut.md "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](../Glossary/Global_OP_Shortcut.md "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

**[Snippets](../Learn/OP_Snippets.md "OP Snippets")** : [OP Snippets](../Learn/OP_Snippets.md "OP Snippets") is a set of 700+ live examples of TouchDesigner operators. You can access snippets via the Help menu, or by right-clicking on network operators, or r-clicking on OP Create dialog items.

**[SOP](../SOPs/SOP.md "SOP")** or **[Surface Operator](../SOPs/SOP.md "SOP")** : A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

**[Status Bar](../Glossary/Status_Bar.md "Status Bar")** : The line of text at the top of the TouchDesigner window which displays messages from TouchDesigner when certain events succeed or fail.

**[Storage](../Glossary/Storage.md "Storage")** : Storage is a python dictionary in each operator, where users can store and fetch extra data.

**[Swizzle](../Glossary/Learning_About_POPs.md "Learning About POPs")** : .

**[Synth](../Glossary/Synth.md "Synth")** : Synths is a legacy term for the artworks created by TouchDesigner. A Synth consists of the [.toe](../Glossary/.toe.md ".toe") file created by TouchDesigner and all the associates media files that are needed to run an artwork in [TouchPlayer](../Glossary/TouchPlayer.md "TouchPlayer") or, in [Perform Mode](../Glossary/Perform_Mode.md "Perform Mode"), [TouchDesigner](../Glossary/TouchDesigner.md "TouchDesigner").

**[Table DAT](../Glossary/Table_DAT.md "Table DAT")** : A form of [DATs](../Glossary/DAT.md "DAT") (Data Operators) that is structured as rows and columns of text strings.

**[Tag](../Glossary/Tag.md "Tag")** : Each operator can have a set of text strings that are its "tags". You can set them and search for them within TouchDesigner.

**[Tangent](../Glossary/Learning_About_POPs.md "Learning About POPs")** : .

**[Textport](../Glossary/Textport.md "Textport")** : The dialog box in which commands and scripts can typed in manually. Output to the textport includes script errors and messages from `print()` and `debug()` calls in python code. You can also edit DATs in the textport.

**[Time Slice](../Glossary/Time_Slicing.md "Time Slicing")** or **[Time Slicing](../Glossary/Time_Slicing.md "Time Slicing")** : A Time Slice is the time from the last cook frame to the current cook frame. In CHOPs it is the set of short channels that contain the CHOP channels' samples between the last and the current cook frame.

**[Timeline](../Glossary/Timeline.md "Timeline")** : The panel at the bottom of TouchDesigner, it controls the current global looping [Time](../Glossary/Time_COMP.md "Time COMP") your TouchDesigner project, or of just one component.

**[TOP](../TOPs/TOP.md "TOP")** or **[Texture Operator](../TOPs/TOP.md "TOP")** : An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

**[Topology](../Glossary/POP_Topology.md "POP Topology")** or **[POP Topology](../Glossary/POP_Topology.md "POP Topology")** : POP Topology is the relationship between geometric entities making up POPs, and refers to the POP's [Primitives](../Glossary/Primitive.md "Primitive"), the [Vertx / Vertices](../Glossary/Vertex.md "Vertex") of each Primitive, and the [Points](../Glossary/Point.md "Point") list that the Vertices refer to.

**[Tscript](../Glossary/Tscript.md "Tscript")** : TouchDesigner's original built-in Command scripting language prior to [Python](Python.md "Python").

**[Tuplet](../Glossary/Tuplet.md "Tuplet")** : A tuplet is the set of parameters that appear on one line of the parameter dialog. Tuplets occupy a [page](../Python/Page_Class.md "Page Class") of parameters.

**[Unicode](../Glossary/Unicode.md "Unicode")** : Unicode text is fully supported in TouchDesigner. Unicode can be typed into parameters, DATs, Python scripts etc. Unicode encoded text files can be loaded into DATs. File paths can include any unicode character that is legal for a file path.

**[Vertex](../Glossary/Vertex.md "Vertex")** or **[Vertices](../Glossary/Vertex.md "Vertex")** : A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

**[VFS](../Glossary/Virtual_File_System.md "Virtual File System")** or **[Virtual File System](../Glossary/Virtual_File_System.md "Virtual File System")** : Lets you embed files inside a `.tox[](../Glossary/.tox.md ".tox")` or `.toe[](../Glossary/.toe.md ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.

**[Viewer](../Glossary/Viewer.md "Viewer")** : The viewer of a node can be (1) the interior of a node (the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](../Glossary/Pane.md "Pane") that graphically shows the results of an operator.

**[Viewer Active](../Glossary/Viewer_Active.md "Viewer Active")** : A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.

**[Viewer flag](../Glossary/Node_Viewer.md "Node Viewer")** : Each node has a viewer flag that turns on/off the node's viewer in the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer").

**[Widgets](../Glossary/Widgets.md "Widgets")** : Widgets is a diverse collection of components located in the Palette, designed for building user interfaces.

**[Window](../Glossary/Window.md "Window")** : A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode"), or (2) a user-created [Panel](../Glossary/Panel.md "Panel") inside a [Window Component](../Glossary/Window_COMP.md "Window COMP"). The user-created windows can span [Multiple Monitors](../Glossary/Multiple_Monitors.md "Multiple Monitors") borderless, or be floating windows with borders, or popups.

**[Wire](../Glossary/Wire.md "Wire")** : The connection of an output of one node to the input of another node in a network. In contrast, see [Link](../Glossary/Link.md "Link").

**[WYSIWID](../Glossary/Network.md "Network")** : TouchDesigner is WYSIWID - What You See Is What It's Doing. All nodes can have interactive viewers of their data.

Now you are fluent in Touchese.

To add: Input Block, Legacy Mode for parameters or operators

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off or the root timeline is paused.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

POPs (Point Operators) is a new [Operator Family](../Glossary/Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

In the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer") of a Geometry COMP or POP, the Adaptive Homing option will keep in-view the 3D geometry being displayed.

In the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer") of a Geometry COMP or any POP, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position.

A pane type where networks of operators can be created and edited.

An Array Attribute is an [Attribute](../Glossary/Attribute.md "Attribute") with multiple **elements** of a chosen **Attribute Data Type** , for example an attribute made of 12 integers.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

A surface type in [POPs](../POPs/POP.md "POP") and [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](../Glossary/Point.md "Point") and Primitives are part of the [Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

The Backdrop is the grid of node viewers that are visible behind the [Network](../Glossary/Network.md "Network"), set by turning on [Display Flags](../Glossary/Display_Flag.md "Display Flag") and the network RMB -> Display... Backdrop OPs.

Binding is a [Parameter Mode](../Glossary/Parameter_Mode.md "Parameter Mode") that ties two or more parameters' values together, where changing the value of any one of the bound parameters changes all of them. The actual value is stored in one place.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](../Glossary/Script.md "Script") or [GLSL](../Glossary/GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](../Glossary/Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

Cloning makes multiple components match the contents of a master component. A [Component](../Glossary/Component.md "Component") whose Clone parameter is set will be forced to contain the same nodes, wiring and parameters as its master component. Cloning does not create new components as does the [Replicator COMP](../Glossary/Replicator_COMP.md "Replicator COMP").

The Container component type is a [Panel Component](../Glossary/Panel_Component.md "Panel Component") that holds, lays out and displays any number of other Panel Components.

The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](../Glossary/Text_DAT.md "Text DAT") and referenced by a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.

You edit your networks in Designer Mode. See [Perform Mode](../Glossary/Perform_Mode.md "Perform Mode").

Dimension is metadata of a POP that describes the structure of the point list, which may be arranged as rows and columns of points (which is two dimensions of size _nrows_ and _ncolumns_).

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

TouchDesigner's original built-in Command scripting language prior to [Python](Python.md "Python").

In CHOPs, Extend Conditions determine what numbers you get when you try to get a channel value that is outside its start-end range - in its Extend Regions.

A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.

A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](../Glossary/Network_Path.md "Network Path").

The term "Frame" is a measurement of time used (1) in the [Timeline](../Glossary/Timeline.md "Timeline"), (2) as a time-unit in CHOPs, and (3) as a time unit in movie files that are read into [TOPs](../TOPs/TOP.md "TOP") and written out from TOPs. The [Frame Rate](../Glossary/Frame_Rate.md "Frame Rate") is the frames per second (FPS).

The [Frames](../Glossary/Frame.md "Frame")-per-Second that TouchDesigner's [Timeline](../Glossary/Timeline.md "Timeline") runs at. Set with `project.cookRate`.

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](../Glossary/Parent_Shortcut.md "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](../Glossary/Global_OP_Shortcut.md "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

Hierarchy relates components with other components. There are two groups of Hierarchy in TouchDesigner. 3D Object Components, and 2D Panel Components. Hierarchies let one component to be positioned relative to another. Each group can be connected via lines between the bottoms/tops of nodes in a network, or by placing one component inside the other.

The sub-[Family](../Glossary/Operator_Family.md "Operator Family") of [Component](../Glossary/Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](../Glossary/Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP") and [Light COMP](../Glossary/Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

Internal Operators (iOPs) provide a simple shortcut to a frequently-used operator, accessing from anywhere in that component.

Internal Parameters (iPars) act like local variables in a component. They provide a simple shortcut to collections of parameters that you create within a component, and access from anywhere in that component.

(1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](../Glossary/Timeline.md "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](../Glossary/Pane.md "Pane") and [Bookmark](../Glossary/Bookmark.md "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.

The viewer of a node can be (1) the interior of a node (the [Node Viewer](../Glossary/Node_Viewer.md "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](../Glossary/Pane.md "Pane") that graphically shows the results of an operator.

A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](../Glossary/Panel_Component.md "Panel Component").

A [Link](../Glossary/Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](../Glossary/Operator_Family.md "Operator Family").

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](../Glossary/Export.md "Export"), node [Paths](../Glossary/Network_Path.md "Network Path") in parameters, and [expressions](../Glossary/Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](../Glossary/Wire.md "Wire") that connects nodes in the same [Operator Family](../Glossary/Operator_Family.md "Operator Family").

A [Link](../Glossary/Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](../Glossary/Operator_Family.md "Operator Family").

The grey dashed lines between nodes is a Reference (or [Link](../Glossary/Link.md "Link")). A Reference is (1) a [Parameter Reference](../Glossary/Parameter_Reference.md "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](../Glossary/Export.md "Export"), node [Paths](../Glossary/Network_Path.md "Network Path") in parameters, and [expressions](../Glossary/Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](../Glossary/Wire.md "Wire") that connects nodes in the same [Operator Family](../Glossary/Operator_Family.md "Operator Family").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

The generic thing that holds an [Operator](Operator.md "Operator"), and includes [Flags](../Glossary/Flag.md "Flag") (display, bypass, lock, render, immune) and its position/size in the network. Whether you "lay down an Operator" or "lay down an Node", you're doing the same thing.

POPs (Point Operators) is a new [Operator Family](../Glossary/Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

Every component contains a network of operators that create and modify data. The operators are connected by wires that define where data is routed after the operator cooks its inputs and generates an output.

The dialog box in which commands and scripts can typed in manually. Output to the textport includes script errors and messages from `print()` and `debug()` calls in python code. You can also edit DATs in the textport.

A 3D viewport for viewing and manipulating 3D scenes or objects interactively. A geometry viewer can be found in [Panes](../Glossary/Pane.md "Pane") (alt+3 in any pane) or the [Node Viewers](../Glossary/Node_Viewer.md "Node Viewer") of all Geometry Object components.

Currently, use a [SOP to DAT](../Glossary/SOP_to_DAT.md "SOP to DAT") to look at SOP point/polygon XYZ and other attributes. Formerly a [Pane](../Glossary/Pane.md "Pane") type.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

In a parameter dialog, Setting Parameter Size to 3 gives 3 columns of parameters to control X Y and Z separately for example.

Parameter Value refers to the constant, the expression, the export, the bind reference and the [Parameter Mode](../Glossary/Parameter_Mode.md "Parameter Mode") that are used together to determine the "evaluated" parameter value.

A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.

A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.

Pattern Expansion takes a short string and expands it to generate a longer string of individual elements.

Matching names using wildcard characters and bracketing. Useful in "[Select](../Glossary/Select_CHOP.md "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

Perform Mode is an optimized mode for live performance that only renders one specified [Window COMP](../Glossary/Window_COMP.md "Window COMP") which is one window that contains your video outputs and your (optional) control interface. In Perform Mode the network editing window is not open - you edit your networks in [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode"). Alternate with F1 and Esc.

A way of moving data from one TouchDesigner process to another. Images are moved via Touch Out / In TOPs, channels are moved via Touch Out / In CHOPs and Pipe Out / In CHOPs. Data moves via TCP/IP or UDP.

Playbar is the former name for Timeline. See [Timeline](../Glossary/Timeline.md "Timeline").

The panel at the bottom of TouchDesigner, it controls the current global looping [Time](../Glossary/Time_COMP.md "Time COMP") your TouchDesigner project, or of just one component.

Each POP and SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](../Glossary/Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

Privacy of TouchDesigner Components (`.tox` files) or Projects (`.toe` files) is the protection of networks that enables them to be used but not be visible or editable.

TouchDesigner Component file, the file type used to save a [Component](../Glossary/Component.md "Component") of your TouchDesigner project.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. It is the chain-reaction mechanism of TouchDesigner, where if one piece of data changes, it automatically causes other "[dependent](../Glossary/Dependency.md "Dependency")" operators and expressions to re-[Cook](../Glossary/Cook.md "Cook") and re-generate the outputs.

Quad Reprojection renders pixel-perfect perspective-correct images for flat TVs and LED panels hung at any orientation.

The 3D data held in POPs and passed for rendering by the [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP").

Rendering is the creation of a 3D image with the Render TOP. Rendering is also used more generally to include the compositing (with TOPs) to generate an output image.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](../Glossary/Root.md "Root"). This path is displayed at the top of every [Pane](../Glossary/Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](../Glossary/Folder.md "Folder").

Sequential Parameters are blocks of parameters (Sequential Blocks) that can be reproduced multiple times by a user to create multiple entities.

Storage is a python dictionary in each operator, where users can store and fetch extra data.

Synths is a legacy term for the artworks created by TouchDesigner. A Synth consists of the [.toe](../Glossary/.toe.md ".toe") file created by TouchDesigner and all the associates media files that are needed to run an artwork in [TouchPlayer](../Glossary/TouchPlayer.md "TouchPlayer") or, in [Perform Mode](../Glossary/Perform_Mode.md "Perform Mode"), [TouchDesigner](../Glossary/TouchDesigner.md "TouchDesigner").

A Time Slice is the time from the last cook frame to the current cook frame. In CHOPs it is the set of short channels that contain the CHOP channels' samples between the last and the current cook frame.

POP Topology is the relationship between geometric entities making up POPs, and refers to the POP's [Primitives](../Glossary/Primitive.md "Primitive"), the [Vertx / Vertices](../Glossary/Vertex.md "Vertex") of each Primitive, and the [Points](../Glossary/Point.md "Point") list that the Vertices refer to.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

Unicode text is fully supported in TouchDesigner. Unicode can be typed into parameters, DATs, Python scripts etc. Unicode encoded text files can be loaded into DATs. File paths can include any unicode character that is legal for a file path.

Lets you embed files inside a `.tox[](../Glossary/.tox.md ".tox")` or `.toe[](../Glossary/.toe.md ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.

Widgets is a diverse collection of components located in the Palette, designed for building user interfaces.

A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.

A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode"), or (2) a user-created [Panel](../Glossary/Panel.md "Panel") inside a [Window Component](../Glossary/Window_COMP.md "Window COMP"). The user-created windows can span [Multiple Monitors](../Glossary/Multiple_Monitors.md "Multiple Monitors") borderless, or be floating windows with borders, or popups.

TouchDesigner is WYSIWID - What You See Is What It's Doing. All nodes can have interactive viewers of their data.

POPs that take unlimited inputs have one seq block of parameters per input. An input can be a pattern of OPs.
