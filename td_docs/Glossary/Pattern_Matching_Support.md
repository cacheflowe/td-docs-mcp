---
url: https://docs.derivative.ca/Pattern_Matching_Support
category: Glossary
title: Pattern_Matching_Support
---

# Pattern Matching Support

##  Group Name Expansion

**Note** : Operator Patterns support the `@groupname` pattern expansion.

##  COMP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Actor COMP](../COMPs/Actor_COMP.md "Actor COMP") | Forces | Operator | ✅
Collision SOPs | Operator | ✅
Light Mask | Operator | ✅
[Blend COMP](../COMPs/Blend_COMP.md "Blend COMP") | Light Mask | Operator | ✅
[Bone COMP](../COMPs/Bone_COMP.md "Bone COMP") | Light Mask | Operator | ✅
[Bullet Solver COMP](../COMPs/Bullet_Solver_COMP.md "Bullet Solver COMP") | Actors | Operator | ✅
Global Forces | Operator | ✅
[Camera COMP](Camera_COMP.md "Camera COMP") | Camera Light Mask | Operator | ✅
[Constraint COMP](../COMPs/Constraint_COMP.md "Constraint COMP") | Actor Bodies | Index | ✅
[Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP") | Light Mask | Operator | ✅
[Geometry COMP](Geometry_COMP.md "Geometry COMP") |  Instance Textures | Operator | ✅
Light Mask | Operator | ✅
[Handle COMP](../COMPs/Handle_COMP.md "Handle COMP") | Light Mask | Operator | ✅
[Light COMP](Light_COMP.md "Light COMP") | Shadow Casters | Operator | ✅
[NVIDIA Flex Solver COMP](../COMPs/NVIDIA_Flex_Solver_COMP.md "NVIDIA Flex Solver COMP") | Actors | Operator | ✅
Global Forces | Operator | ✅
Light Mask | Operator | ✅
[NVIDIA Flow Emitter COMP](../COMPs/NVIDIA_Flow_Emitter_COMP.md "NVIDIA Flow Emitter COMP") | Light Mask | Operator | ✅

##  POP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Analyze POP](../POPs/Analyze_POP.md "Analyze POP") | Input Attributes | Basic | ✅
[Attribute Combine POP](../POPs/Attribute_Combine_POP.md "Attribute Combine POP") | In POP(s) | Operator | ✅
In Attributes | Basic | ✅
[Attribute Convert POP](../POPs/Attribute_Convert_POP.md "Attribute Convert POP") | Attribute Name | Basic | ✅
[Attribute POP](../POPs/Attribute_POP.md "Attribute POP") | Delete Point Attributes | Basic | ✅
Delete Vertex Attributes | Basic | ✅
Delete Primitive Attributes | Basic | ✅
[Blend POP](../POPs/Blend_POP.md "Blend POP") | In POP(s) | Operator | ✅
Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅
[Copy POP](../POPs/Copy_POP.md "Copy POP") | Names | Basic | ✅
[Curve POP](../POPs/Curve_POP.md "Curve POP") | Lookup Index Attribute | Basic | ✅
[Delete POP](../POPs/Delete_POP.md "Delete POP") | Pattern | Index | ✅
[DMX Out POP](../POPs/DMX_Out_POP.md "DMX Out POP") | DMX Fixture POPs | Operator | ✅
Local IP Pattern | Basic |
[GLSL Advanced POP](../POPs/GLSL_Advanced_POP.md "GLSL Advanced POP") | In POPs | Operator | ✅
Point Output Attributes | Basic | ✅
Prim Output Attributes | Basic | ✅
Vert Output Attributes | Basic | ✅
[GLSL Copy POP](../POPs/GLSL_Copy_POP.md "GLSL Copy POP") | Point Output Attributes | Basic | ✅
Vert Ouput Attributes | Basic | ✅
Prim Output Attributes | Basic | ✅
[GLSL POP](../POPs/GLSL_POP.md "GLSL POP") | In POPs | Operator | ✅
Output Attributes | Basic | ✅
[Group POP](../POPs/Group_POP.md "Group POP") | Pattern | Index | ✅
[Lookup Attribute POP](../POPs/Lookup_Attribute_POP.md "Lookup Attribute POP") | Lookup Index Attribute(s) | Basic | ✅
[Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") | In POP(s) | Operator | ✅
[Merge POP](../POPs/Merge_POP.md "Merge POP") | In POP(s) | Operator | ✅
[Neighbor POP](../POPs/Neighbor_POP.md "Neighbor POP") | Neighbor Point Attributes | Basic | ✅
[Particle POP](../POPs/Particle_POP.md "Particle POP") | In Attributes | Basic | ✅
[Primitive POP](../POPs/Primitive_POP.md "Primitive POP") | Point Index Pattern | Index (Ordered) |
[Ray POP](../POPs/Ray_POP.md "Ray POP") | Hit Point Attr Scope | Basic | ✅
Hit Primitive Attr Scope | Basic | ✅
Hit Vertex Attr Scope | Basic | ✅
[Select POP](../POPs/Select_POP.md "Select POP") | Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅
[Sprinkle POP](../POPs/Sprinkle_POP.md "Sprinkle POP") | Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅
[Switch POP](../POPs/Switch_POP.md "Switch POP") | In POP(s) | Operator | ✅
Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅

##  DAT

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Art-Net DAT](https://docs.derivative.ca/Art-Net_DAT "Art-Net DAT") | Local IP Pattern | Basic |
[CHOP Execute DAT](../DATs/CHOP_Execute_DAT.md "CHOP Execute DAT") | CHOPs | Operator | ✅
[Clip DAT](../DATs/Clip_DAT.md "Clip DAT") | Component | Operator | ✅
[DAT Execute DAT](../DATs/DAT_Execute_DAT.md "DAT Execute DAT") | DATs | Operator | ✅
[DMX Map DAT](https://docs.derivative.ca/DMX_Map_DAT "DMX Map DAT") | Net Filter | Basic |
Subnet Filter | Basic |
Universe Filter | Basic |
Network Address Filter | Basic |
[Evaluate DAT](../DATs/Evaluate_DAT.md "Evaluate DAT") | Row Select Values | Basic | ✅
Col Select Values | Basic | ✅
[Keyboard In DAT](../DATs/Keyboard_In_DAT.md "Keyboard In DAT") | Panels | Operator | ✅
[Merge DAT](../DATs/Merge_DAT.md "Merge DAT") | DATs | Operator | ✅
[OP Execute DAT](../DATs/OP_Execute_DAT.md "OP Execute DAT") | Monitor OPs | Operator | ✅
[OP Find DAT](../DATs/OP_Find_DAT.md "OP Find DAT") | Name | Basic |
Type | Basic |
Parent Shortcut | Basic |
OP Shortcut | Basic |
Path | Basic |
Parent Path (relative) | Basic |
Wire Path | Basic |
Comment | Basic |
Tags | Basic |
DAT Text | Basic |
Par Name | Basic |
Par Value | Basic |
Par Expression | Basic |
[OSC In DAT](../DATs/OSC_In_DAT.md "OSC In DAT") | Local IP Pattern | Basic |
[OSC Out DAT](../DATs/OSC_Out_DAT.md "OSC Out DAT") | Local IP Pattern | Basic |
[Panel Execute DAT](Panel_Execute_DAT.md "Panel Execute DAT") | Panels | Operator | ✅
[Parameter DAT](../DATs/Parameter_DAT.md "Parameter DAT") | Operators | Operator | ✅
[Parameter Execute DAT](../DATs/Parameter_Execute_DAT.md "Parameter Execute DAT") | OPs | Operator | ✅
[ParGroup Execute DAT](../DATs/ParGroup_Execute_DAT.md "ParGroup Execute DAT") | OPs | Operator | ✅
[POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") | Attributes | Basic | ✅
[Select DAT](../DATs/Select_DAT.md "Select DAT") | Row Select Values | Basic | ✅
Col Select Values | Basic | ✅
[SOP to DAT](SOP_to_DAT.md "SOP to DAT") | Attributes | Basic | ✅
[Substitute DAT](../DATs/Substitute_DAT.md "Substitute DAT") | Row Select Values | Basic | ✅
Col Select Values | Basic | ✅
[TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT") | Local IP Pattern | Basic |
[Touch In DAT](../DATs/Touch_In_DAT.md "Touch In DAT") | Local IP Pattern | Basic |
[Touch Out DAT](../DATs/Touch_Out_DAT.md "Touch Out DAT") | Local IP PatternF | Basic |
[UDP In DAT](../Interoperability/UDP_In_DAT.md "UDP In DAT") | Local IP Pattern | Basic |
[UDP Out DAT](../DATs/UDP_Out_DAT.md "UDP Out DAT") | Local IP Pattern | Basic | ✅

##  CHOP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Audio Render CHOP](../Interoperability/Audio_Render_CHOP.md "Audio Render CHOP") | Mesh SOPs | Operator | ✅
[DAT to CHOP](../CHOPs/DAT_to_CHOP.md "DAT to CHOP") | Row Select Values | Basic |
Col Select Values | Basic |
[Delete CHOP](../CHOPs/Delete_CHOP.md "Delete CHOP") | Channel Names | Basic | ✅
Channel Numbers | Index | ✅
[DMX In CHOP](../CHOPs/DMX_In_CHOP.md "DMX In CHOP") | Local IP Pattern | Basic |
Start Codes | Basic |
[DMX Out CHOP](../CHOPs/DMX_Out_CHOP.md "DMX Out CHOP") | Local IP Pattern | Basic |
[EtherDream CHOP](../CHOPs/EtherDream_CHOP.md "EtherDream CHOP") | Local IP Pattern | Basic |
[FreeD CHOP](../Interoperability/FreeD_CHOP.md "FreeD CHOP") | Local IP Pattern | Basic |
[FreeD Out CHOP](../CHOPs/FreeD_Out_CHOP.md "FreeD Out CHOP") | Local IP Pattern | Basic |
[Join CHOP](../CHOPs/Join_CHOP.md "Join CHOP") | CHOPs | Operator | ✅
[Keyboard In CHOP](../CHOPs/Keyboard_In_CHOP.md "Keyboard In CHOP") | Panels | Operator | ✅
[MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP") | Note Scope | Index | ✅
Controller Index | Index | ✅
MIDI Channels | Index | ✅
[MIDI In Map CHOP](../CHOPs/MIDI_In_Map_CHOP.md "MIDI In Map CHOP") | Sliders | Basic | ✅
Buttons | Basic | ✅
[MoSys CHOP](../Interoperability/MoSys_CHOP.md "MoSys CHOP") | Local IP Pattern | Basic |
[Mouse In CHOP](../CHOPs/Mouse_In_CHOP.md "Mouse In CHOP") | Panels | Operator | ✅
[Ncam CHOP](../CHOPs/Ncam_CHOP.md "Ncam CHOP") | Local IP Pattern | Basic |
[OptiTrack In CHOP](../CHOPs/OptiTrack_In_CHOP.md "OptiTrack In CHOP") | Local IP Pattern | Basic |
[OSC In CHOP](../Interoperability/OSC_In_CHOP.md "OSC In CHOP") | Local IP Pattern | Basic |
[OSC Out CHOP](../CHOPs/OSC_Out_CHOP.md "OSC Out CHOP") | Local IP Pattern | Basic |
[Parameter CHOP](../CHOPs/Parameter_CHOP.md "Parameter CHOP") | Operators | Operator | ✅
Rename From | Basic |
Sequences | Basic |
ParGroups | Basic |
Parameters | Basic |
[PosiStageNet CHOP](../Interoperability/PosiStageNet_CHOP.md "PosiStageNet CHOP") | Local IP Pattern | Basic |
[Reorder CHOP](../CHOPs/Reorder_CHOP.md "Reorder CHOP") | Character Pattern | Basic |
Numeric Pattern | Index | ✅
[Select CHOP](Select_CHOP.md "Select CHOP") | CHOPs | Operator | ✅
Channel Names | Basic | ✅
Rename From | Basic |
[Sequencer CHOP](../CHOPs/Sequencer_CHOP.md "Sequencer CHOP") | Add Scope | Basic |
Blend Scope | Basic |
[Sort CHOP](../CHOPs/Sort_CHOP.md "Sort CHOP") | Channel Names | Basic |
Channel Indices | Index | ✅
[Stype CHOP](https://docs.derivative.ca/Stype_CHOP "Stype CHOP") | Local IP Pattern | Basic |
[Stype Out CHOP](../CHOPs/Stype_Out_CHOP.md "Stype Out CHOP") | Local IP Pattern | Basic |
[Sync In CHOP](../CHOPs/Sync_In_CHOP.md "Sync In CHOP") | Local IP Pattern | Basic |
[Sync Out CHOP](../CHOPs/Sync_Out_CHOP.md "Sync Out CHOP") | Local IP Pattern | Basic |

##  TOP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Composite TOP](../TOPs/Composite_TOP.md "Composite TOP") | TOPs | Operator | ✅
[GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP") | TOPs | Operator | ✅
[Layout TOP](../TOPs/Layout_TOP.md "Layout TOP") | TOPs | Operator | ✅
[NVIDIA Flow TOP](../TOPs/NVIDIA_Flow_TOP.md "NVIDIA Flow TOP") | Flow Emitters | Operator | ✅
[Ouster TOP](../TOPs/Ouster_TOP.md "Ouster TOP") | Local IP Pattern | Basic |
[Render TOP](../TOPs/Render_TOP.md "Render TOP") | Geometry | Operator | ✅
Lights | Operator | ✅
Cameras | Operator | ✅

##  SOP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[DAT to SOP](../SOPs/DAT_to_SOP.md "DAT to SOP") | Add Float Attributes | Basic | ✅
Add Int Attributes | Basic | ✅
Add String Attributes | Basic | ✅
[Merge SOP](../SOPs/Merge_SOP.md "Merge SOP") | SOPs | Operator | ✅
[Object Merge SOP](../SOPs/Object_Merge_SOP.md "Object Merge SOP") | SOP | Operator | ✅
[Select SOP](../SOPs/Select_SOP.md "Select SOP") | SOPs | Operator | ✅

##  See Also

  * [Pattern Expansion](Pattern_Expansion.md "Pattern Expansion"), [Pattern Replacement](Pattern_Replacement.md "Pattern Replacement"), Pattern Matching Support

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

The generic thing that holds an [Operator](../General/Operator.md "Operator"), and includes [Flags](Flag.md "Flag") (display, bypass, lock, render, immune) and its position/size in the network. Whether you "lay down an Operator" or "lay down an Node", you're doing the same thing.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").

(1) A [Geometry Component](Geometry_COMP.md "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

POPs (**Point Operators**) is a new [Operator Family](Operator_Family.md "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](../TOPs/Render_TOP.md "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

Attributes are data associated with [POP](../POPs/POP.md "POP") geometry. [Points](Point.md "Point"), [Vertex (Vertices)](Vertex.md "Vertex") and [Primitives](Primitive.md "Primitive") (polygons, lines, etc) can have any number of attributes.

A sequence of vertices form a [Polygon](Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

A surface type in [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](Point.md "Point") and Primitives are part of the [Geometry Detail](Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").

A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

Operators that need 1 or more inputs are called Filters in TouchDesigner, like a Math CHOP. See [Generator](Generator.md "Generator").

A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](Parent_Shortcut.md "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](Global_OP_Shortcut.md "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](Root.md "Root"). This path is displayed at the top of every [Pane](Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](Folder.md "Folder").

The connection of an output of one node to the input of another node in a network. In contrast, see [Link](Link.md "Link").

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](DAT.md "DAT") and in scripts.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](Geometry_COMP.md "Geometry COMP").

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
