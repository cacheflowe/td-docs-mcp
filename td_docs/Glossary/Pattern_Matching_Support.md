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
[Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP") | Forces | Operator | ✅
Collision SOPs | Operator | ✅
Light Mask | Operator | ✅
[Blend COMP](https://docs.derivative.ca/Blend_COMP "Blend COMP") | Light Mask | Operator | ✅
[Bone COMP](https://docs.derivative.ca/Bone_COMP "Bone COMP") | Light Mask | Operator | ✅
[Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP") | Actors | Operator | ✅
Global Forces | Operator | ✅
[Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") | Camera Light Mask | Operator | ✅
[Constraint COMP](https://docs.derivative.ca/Constraint_COMP "Constraint COMP") | Actor Bodies | Index | ✅
[Geo Text COMP](https://docs.derivative.ca/Geo_Text_COMP "Geo Text COMP") | Light Mask | Operator | ✅
[Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") |  Instance Textures | Operator | ✅
Light Mask | Operator | ✅
[Handle COMP](https://docs.derivative.ca/Handle_COMP "Handle COMP") | Light Mask | Operator | ✅
[Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") | Shadow Casters | Operator | ✅
[NVIDIA Flex Solver COMP](https://docs.derivative.ca/NVIDIA_Flex_Solver_COMP "NVIDIA Flex Solver COMP") | Actors | Operator | ✅
Global Forces | Operator | ✅
Light Mask | Operator | ✅
[NVIDIA Flow Emitter COMP](https://docs.derivative.ca/NVIDIA_Flow_Emitter_COMP "NVIDIA Flow Emitter COMP") | Light Mask | Operator | ✅

##  POP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Analyze POP](https://docs.derivative.ca/Analyze_POP "Analyze POP") | Input Attributes | Basic | ✅
[Attribute Combine POP](https://docs.derivative.ca/Attribute_Combine_POP "Attribute Combine POP") | In POP(s) | Operator | ✅
In Attributes | Basic | ✅
[Attribute Convert POP](https://docs.derivative.ca/Attribute_Convert_POP "Attribute Convert POP") | Attribute Name | Basic | ✅
[Attribute POP](https://docs.derivative.ca/Attribute_POP "Attribute POP") | Delete Point Attributes | Basic | ✅
Delete Vertex Attributes | Basic | ✅
Delete Primitive Attributes | Basic | ✅
[Blend POP](https://docs.derivative.ca/Blend_POP "Blend POP") | In POP(s) | Operator | ✅
Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅
[Copy POP](https://docs.derivative.ca/Copy_POP "Copy POP") | Names | Basic | ✅
[Curve POP](https://docs.derivative.ca/Curve_POP "Curve POP") | Lookup Index Attribute | Basic | ✅
[Delete POP](https://docs.derivative.ca/Delete_POP "Delete POP") | Pattern | Index | ✅
[DMX Out POP](https://docs.derivative.ca/DMX_Out_POP "DMX Out POP") | DMX Fixture POPs | Operator | ✅
Local IP Pattern | Basic |
[GLSL Advanced POP](https://docs.derivative.ca/GLSL_Advanced_POP "GLSL Advanced POP") | In POPs | Operator | ✅
Point Output Attributes | Basic | ✅
Prim Output Attributes | Basic | ✅
Vert Output Attributes | Basic | ✅
[GLSL Copy POP](https://docs.derivative.ca/GLSL_Copy_POP "GLSL Copy POP") | Point Output Attributes | Basic | ✅
Vert Ouput Attributes | Basic | ✅
Prim Output Attributes | Basic | ✅
[GLSL POP](https://docs.derivative.ca/GLSL_POP "GLSL POP") | In POPs | Operator | ✅
Output Attributes | Basic | ✅
[Group POP](https://docs.derivative.ca/Group_POP "Group POP") | Pattern | Index | ✅
[Lookup Attribute POP](https://docs.derivative.ca/Lookup_Attribute_POP "Lookup Attribute POP") | Lookup Index Attribute(s) | Basic | ✅
[Math Combine POP](https://docs.derivative.ca/Math_Combine_POP "Math Combine POP") | In POP(s) | Operator | ✅
[Merge POP](https://docs.derivative.ca/Merge_POP "Merge POP") | In POP(s) | Operator | ✅
[Neighbor POP](https://docs.derivative.ca/Neighbor_POP "Neighbor POP") | Neighbor Point Attributes | Basic | ✅
[Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP") | In Attributes | Basic | ✅
[Primitive POP](https://docs.derivative.ca/Primitive_POP "Primitive POP") | Point Index Pattern | Index (Ordered) |
[Ray POP](https://docs.derivative.ca/Ray_POP "Ray POP") | Hit Point Attr Scope | Basic | ✅
Hit Primitive Attr Scope | Basic | ✅
Hit Vertex Attr Scope | Basic | ✅
[Select POP](https://docs.derivative.ca/Select_POP "Select POP") | Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅
[Sprinkle POP](https://docs.derivative.ca/Sprinkle_POP "Sprinkle POP") | Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅
[Switch POP](https://docs.derivative.ca/Switch_POP "Switch POP") | In POP(s) | Operator | ✅
Point Attribute Scope | Basic | ✅
Primitive Attribute Scope | Basic | ✅
Vertex Attribute Scope | Basic | ✅

##  DAT

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Art-Net DAT](https://docs.derivative.ca/Art-Net_DAT "Art-Net DAT") | Local IP Pattern | Basic |
[CHOP Execute DAT](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT") | CHOPs | Operator | ✅
[Clip DAT](https://docs.derivative.ca/Clip_DAT "Clip DAT") | Component | Operator | ✅
[DAT Execute DAT](https://docs.derivative.ca/DAT_Execute_DAT "DAT Execute DAT") | DATs | Operator | ✅
[DMX Map DAT](https://docs.derivative.ca/DMX_Map_DAT "DMX Map DAT") | Net Filter | Basic |
Subnet Filter | Basic |
Universe Filter | Basic |
Network Address Filter | Basic |
[Evaluate DAT](https://docs.derivative.ca/Evaluate_DAT "Evaluate DAT") | Row Select Values | Basic | ✅
Col Select Values | Basic | ✅
[Keyboard In DAT](https://docs.derivative.ca/Keyboard_In_DAT "Keyboard In DAT") | Panels | Operator | ✅
[Merge DAT](https://docs.derivative.ca/Merge_DAT "Merge DAT") | DATs | Operator | ✅
[OP Execute DAT](https://docs.derivative.ca/OP_Execute_DAT "OP Execute DAT") | Monitor OPs | Operator | ✅
[OP Find DAT](https://docs.derivative.ca/OP_Find_DAT "OP Find DAT") | Name | Basic |
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
[OSC In DAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT") | Local IP Pattern | Basic |
[OSC Out DAT](https://docs.derivative.ca/OSC_Out_DAT "OSC Out DAT") | Local IP Pattern | Basic |
[Panel Execute DAT](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT") | Panels | Operator | ✅
[Parameter DAT](https://docs.derivative.ca/Parameter_DAT "Parameter DAT") | Operators | Operator | ✅
[Parameter Execute DAT](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT") | OPs | Operator | ✅
[ParGroup Execute DAT](https://docs.derivative.ca/ParGroup_Execute_DAT "ParGroup Execute DAT") | OPs | Operator | ✅
[POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT") | Attributes | Basic | ✅
[Select DAT](https://docs.derivative.ca/Select_DAT "Select DAT") | Row Select Values | Basic | ✅
Col Select Values | Basic | ✅
[SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT") | Attributes | Basic | ✅
[Substitute DAT](https://docs.derivative.ca/Substitute_DAT "Substitute DAT") | Row Select Values | Basic | ✅
Col Select Values | Basic | ✅
[TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT") | Local IP Pattern | Basic |
[Touch In DAT](https://docs.derivative.ca/Touch_In_DAT "Touch In DAT") | Local IP Pattern | Basic |
[Touch Out DAT](https://docs.derivative.ca/Touch_Out_DAT "Touch Out DAT") | Local IP PatternF | Basic |
[UDP In DAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT") | Local IP Pattern | Basic |
[UDP Out DAT](https://docs.derivative.ca/UDP_Out_DAT "UDP Out DAT") | Local IP Pattern | Basic | ✅

##  CHOP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Audio Render CHOP](https://docs.derivative.ca/Audio_Render_CHOP "Audio Render CHOP") | Mesh SOPs | Operator | ✅
[DAT to CHOP](https://docs.derivative.ca/DAT_to_CHOP "DAT to CHOP") | Row Select Values | Basic |
Col Select Values | Basic |
[Delete CHOP](https://docs.derivative.ca/Delete_CHOP "Delete CHOP") | Channel Names | Basic | ✅
Channel Numbers | Index | ✅
[DMX In CHOP](https://docs.derivative.ca/DMX_In_CHOP "DMX In CHOP") | Local IP Pattern | Basic |
Start Codes | Basic |
[DMX Out CHOP](https://docs.derivative.ca/DMX_Out_CHOP "DMX Out CHOP") | Local IP Pattern | Basic |
[EtherDream CHOP](https://docs.derivative.ca/EtherDream_CHOP "EtherDream CHOP") | Local IP Pattern | Basic |
[FreeD CHOP](https://docs.derivative.ca/FreeD_CHOP "FreeD CHOP") | Local IP Pattern | Basic |
[FreeD Out CHOP](https://docs.derivative.ca/FreeD_Out_CHOP "FreeD Out CHOP") | Local IP Pattern | Basic |
[Join CHOP](https://docs.derivative.ca/Join_CHOP "Join CHOP") | CHOPs | Operator | ✅
[Keyboard In CHOP](https://docs.derivative.ca/Keyboard_In_CHOP "Keyboard In CHOP") | Panels | Operator | ✅
[MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP") | Note Scope | Index | ✅
Controller Index | Index | ✅
MIDI Channels | Index | ✅
[MIDI In Map CHOP](https://docs.derivative.ca/MIDI_In_Map_CHOP "MIDI In Map CHOP") | Sliders | Basic | ✅
Buttons | Basic | ✅
[MoSys CHOP](https://docs.derivative.ca/MoSys_CHOP "MoSys CHOP") | Local IP Pattern | Basic |
[Mouse In CHOP](https://docs.derivative.ca/Mouse_In_CHOP "Mouse In CHOP") | Panels | Operator | ✅
[Ncam CHOP](https://docs.derivative.ca/Ncam_CHOP "Ncam CHOP") | Local IP Pattern | Basic |
[OptiTrack In CHOP](https://docs.derivative.ca/OptiTrack_In_CHOP "OptiTrack In CHOP") | Local IP Pattern | Basic |
[OSC In CHOP](https://docs.derivative.ca/OSC_In_CHOP "OSC In CHOP") | Local IP Pattern | Basic |
[OSC Out CHOP](https://docs.derivative.ca/OSC_Out_CHOP "OSC Out CHOP") | Local IP Pattern | Basic |
[Parameter CHOP](https://docs.derivative.ca/Parameter_CHOP "Parameter CHOP") | Operators | Operator | ✅
Rename From | Basic |
Sequences | Basic |
ParGroups | Basic |
Parameters | Basic |
[PosiStageNet CHOP](https://docs.derivative.ca/PosiStageNet_CHOP "PosiStageNet CHOP") | Local IP Pattern | Basic |
[Reorder CHOP](https://docs.derivative.ca/Reorder_CHOP "Reorder CHOP") | Character Pattern | Basic |
Numeric Pattern | Index | ✅
[Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP") | CHOPs | Operator | ✅
Channel Names | Basic | ✅
Rename From | Basic |
[Sequencer CHOP](https://docs.derivative.ca/Sequencer_CHOP "Sequencer CHOP") | Add Scope | Basic |
Blend Scope | Basic |
[Sort CHOP](https://docs.derivative.ca/Sort_CHOP "Sort CHOP") | Channel Names | Basic |
Channel Indices | Index | ✅
[Stype CHOP](https://docs.derivative.ca/Stype_CHOP "Stype CHOP") | Local IP Pattern | Basic |
[Stype Out CHOP](https://docs.derivative.ca/Stype_Out_CHOP "Stype Out CHOP") | Local IP Pattern | Basic |
[Sync In CHOP](https://docs.derivative.ca/Sync_In_CHOP "Sync In CHOP") | Local IP Pattern | Basic |
[Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP") | Local IP Pattern | Basic |

##  TOP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[Composite TOP](https://docs.derivative.ca/Composite_TOP "Composite TOP") | TOPs | Operator | ✅
[GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP") | TOPs | Operator | ✅
[Layout TOP](https://docs.derivative.ca/Layout_TOP "Layout TOP") | TOPs | Operator | ✅
[NVIDIA Flow TOP](https://docs.derivative.ca/NVIDIA_Flow_TOP "NVIDIA Flow TOP") | Flow Emitters | Operator | ✅
[Ouster TOP](https://docs.derivative.ca/Ouster_TOP "Ouster TOP") | Local IP Pattern | Basic |
[Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") | Geometry | Operator | ✅
Lights | Operator | ✅
Cameras | Operator | ✅

##  SOP

Node | Parameter Name | Pattern Type | Supports Set Matching
---|---|---|---
[DAT to SOP](https://docs.derivative.ca/DAT_to_SOP "DAT to SOP") | Add Float Attributes | Basic | ✅
Add Int Attributes | Basic | ✅
Add String Attributes | Basic | ✅
[Merge SOP](https://docs.derivative.ca/Merge_SOP "Merge SOP") | SOPs | Operator | ✅
[Object Merge SOP](https://docs.derivative.ca/Object_Merge_SOP "Object Merge SOP") | SOP | Operator | ✅
[Select SOP](https://docs.derivative.ca/Select_SOP "Select SOP") | SOPs | Operator | ✅

##  See Also

  * [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion"), [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement"), Pattern Matching Support

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](https://docs.derivative.ca/Group_POP "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

The generic thing that holds an [Operator](https://docs.derivative.ca/Operator "Operator"), and includes [Flags](https://docs.derivative.ca/Flag "Flag") (display, bypass, lock, render, immune) and its position/size in the network. Whether you "lay down an Operator" or "lay down an Node", you're doing the same thing.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").

(1) A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

POPs (**Point Operators**) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes.

A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

A surface type in [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").

A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

Operators that need 1 or more inputs are called Filters in TouchDesigner, like a Math CHOP. See [Generator](https://docs.derivative.ca/Generator "Generator").

A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](https://docs.derivative.ca/Root "Root"). This path is displayed at the top of every [Pane](https://docs.derivative.ca/Pane "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](https://docs.derivative.ca/Folder "Folder").

The connection of an output of one node to the input of another node in a network. In contrast, see [Link](https://docs.derivative.ca/Link "Link").

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](https://docs.derivative.ca/DAT "DAT") and in scripts.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP").

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
