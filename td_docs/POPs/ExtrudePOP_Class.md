---
url: https://docs.derivative.ca/ExtrudePOP_Class
category: POPs
title: ExtrudePOP_Class
---

# extrudePOP Class

This class inherits from the [ POP class](https://docs.derivative.ca/POP_Class "POP Class"). It references a specific [Extrude POP](https://docs.derivative.ca/Extrude_POP "Extrude POP").


## Members
No operator specific members.


## Methods
No operator specific methods.
#  POP Class
## Members
`compare` → `bool` :
Get or set Compare Flag.

`dimension` → `Dimension` **(Read Only)** :
The dimension in this POP.

`maxVertsPerLineStrip` → `int` **(Read Only)** :
The max number of verts per line strip in this POP.
`pointAttributes` → **(Read Only)** :
The set of point attributes defined in this POP.
`pointAttributesChanged` → **(Read Only)** :
The point attributes changed by this POP.
`primAttributes` → **(Read Only)** :
The set of primitive attributes defined in this POP.
`primAttributesChanged` → **(Read Only)** :
The prim attributes changed by this POP.

`template` → `bool` :
Get or set Template Flag.
`vertAttributes` → **(Read Only)** :
The set of vertex attributes defined in this POP.
`vertAttributesChanged` → **(Read Only)** :
The vert attributes changed by this POP.
## Methods
`bounds(delayed=False)`→ `Bounds`:
Returns an [object](https://docs.derivative.ca/Bounds_Class "Bounds Class") with the bounds, center and size of the POP's geometry.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to bounds(), avoiding stalling the GPU waiting for the result immediately.

`computeBounds(display=False, render=False, delayed=False)`→ `Bounds`:
Returns an [object](https://docs.derivative.ca/Bounds_Class "Bounds Class") with the bounds, center and size of the POP's geometry.
  * display - (Keyword, Optional) If set to True, only calculate Bounding Box if POP display flag is set.
  * render - (Keyword, Optional) If set to True, only calculate Bounding Box if POP render flag is set.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to computeBounds(), avoiding stalling the GPU waiting for the result immediately.

`numPoints(delayed=False, max=False)`→ `int`:
Returns the number of points contained in this POP.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to numPoints(), avoiding stalling the GPU waiting for the result immediately.
  * max - (Keyword, Optional) If set to True, returns the number of allocated points (max number of points). In that case result is always instant, delayed is disregarded.

`numPrims(delayed=False, max=False, primType=None)`→ `int`:
Returns the number of primitives contained in this POP.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to numPrims(), avoiding stalling the GPU waiting for the result immediately.
  * max - (Keyword, Optional) If set to True, returns the number of allocated primitives (max number of primitives). In that case result is always instant, delayed is disregarded.
  * primType - (Keyword, Optional) If set to triangles, quads, lineStrips, lines or pointPrims, returns the number of primitives for that primitive type only.

`numVerts(delayed=False, max=False, lineStrips=False)`→ `int`:
Returns the number of vertices contained in this POP.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to numVerts(), avoiding stalling the GPU waiting for the result immediately.
  * max - (Keyword, Optional) If set to True, returns the number of allocated vertices (max number of verts). In that case result is always instant, delayed is disregarded.
  * lineStrips - (Keyword, Optional) If set to true, returns the number of verts for line strips only.

`points(attributeName, startIndex=0, count=-1, delayed=False)`→ `list`:
Returns the point attribute values as a list.
  * attributeName - The attribute name.
  * startIndex - (Keyword, Optional )The point index to start at (default 0).
  * count - (Keyword, Optional) The number of points to download. A value of -1 fetches all elements from the start index onward.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.

`prims(attributeName, startIndex=0, count=-1, delayed=False)`→ `list`:
Returns the primitive attribute values as a list.
  * attributeName - The attribute name.
  * startIndex - (Keyword, Optional )The primitive index to start at (default 0).
  * count - (Keyword, Optional) The number of primitives to download. A value of -1 fetches all elements from the start index onward.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.

`reallocate()`→ `None`:
Forces the POP to reallocate its GPU buffers.

`save(filepath, createFolders=False)`→ `str`:
Save the POP geometry to file system. Multiple file types are supported. Returns the filename and path saved.
  * filepath - (Optional) The path and filename to save to. If not given then a default filename will be used, and the file will be saved in the project.folder folder.
  * createFolders - (Keyword, Optional) If True, it creates the not existent directories provided by the filepath.

`verts(attributeName, startIndex=0, count=-1, delayed=False)`→ `list`:
Returns the vertex attribute values as a list.
  * attributeName - The attribute name.
  * startIndex - (Keyword, Optional )The vertex index to start at (default 0).
  * count - (Keyword, Optional) The number of vertices to download. A value of -1 fetches all elements from the start index onward.
  * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.

#  OP Class
## Members
###  General
`valid` → `bool` **(Read Only)** :
True if the referenced operator currently exists, False if it has been deleted.

`id` → `int` **(Read Only)** :
Unique id for the operator. This id can also be passed to the op() and ops() shortcuts. Id's are not consistent when a file is re-opened, and will change if the OP is copied/pasted, changes OP types, deleted/undone. The id will not change if the OP is renamed though. Its data type is integer.

`supported` → `bool` **(Read Only)** :
True if supported on the current Operating System.

`name` → `str` :
Get or set the operator name.

`path` → `str` **(Read Only)** :
Full path to the operator.

`digits` → `int` **(Read Only)** :
Returns the numeric value of the last consecutive group of digits in the name, or None if not found. The digits can be in the middle of the name if there are none at the end of the name.

`base` → `str` **(Read Only)** :
Returns the beginning portion of the name occurring before any digits.

`par` → `ParCollection` **(Read Only)** :
An intermediate [parameter collection](https://docs.derivative.ca/ParCollection_Class "ParCollection Class") object, from which a specific [parameter](https://docs.derivative.ca/Par_Class "Par Class") can be found.

```
n.par.tx
# or
n.par['tx']

```

`parGroup` → `ParGroupCollection` **(Read Only)** :
An intermediate [parameter collection](https://docs.derivative.ca/ParGroupCollection_Class "ParGroupCollection Class") object, from which a specific [parameter group](https://docs.derivative.ca/ParGroup_Class "ParGroup Class") can be found.

```
n.parGroup.t
# or
n.parGroup['t']

```

`ext` → `Ext` **(Read Only)** :
Object that searches for parent [extensions](https://docs.derivative.ca/Extensions "Extensions").

```
me.ext.MyClass

```

`passive` → `bool` **(Read Only)** :
If true, operator will not cook before its access methods are called. To use a passive version of an operator n, use passive(n).

`curPar` → `Par` **(Read Only)** :
The parameter currently being evaluated. Can be used in a parameter expression to reference itself. An easy way to see this is to put the expression `curPar.name` in any string parameter.

`curBlock` → `SequenceBlock` **(Read Only)** :
The SequenceBlock of the parameter currently being evaluated. Can be used in a parameter expression to reference itself.

`curSeq` → `Sequence` **(Read Only)** :
The Sequence of the parameter currently being evaluated. Can be used in a parameter expression to reference itself.

`time` → `OP` **(Read Only)** :
[Time Component](https://docs.derivative.ca/TimeCOMP_Class "TimeCOMP Class") that defines the operator's time reference.

`fileFolder` → `str` **(Read Only)** :
Returns the folder where this node is saved.

`filePath` → `str` **(Read Only)** :
Returns the file location of this node.

`mod` → `MOD` **(Read Only)** :
Get a [module on demand](https://docs.derivative.ca/MOD_Class "MOD Class") object that searches for DAT modules relative to this operator.

`pages` → `List[Page]` **(Read Only)** :
A list of all built-in pages.

`seq` → `SequenceCollection` **(Read Only)** :
An intermediate [sequence collection](https://docs.derivative.ca/SequenceCollection_Class "SequenceCollection Class") object, from which a specific [sequence](https://docs.derivative.ca/index.php?title=Sequence&action=edit&redlink=1 "Sequence \(page does not exist\)") can be found.

```
comp.seq.ext
# or
comp.seq['ext']

```

`builtinPars` → `List[Par]` **(Read Only)** :
A list of all [built-in parameters](https://docs.derivative.ca/Par_Class "Par Class").

`customParGroups` → `List[ParGroup]` **(Read Only)** :
A list of all [ParGroups](https://docs.derivative.ca/ParGroup_Class "ParGroup Class"), where a ParGroup is a set of parameters all drawn on the same line of a dialog, sharing the same label.

`customPars` → `List[Par]` **(Read Only)** :
A list of all [custom parameters](https://docs.derivative.ca/Par_Class "Par Class").

`customPages` → `List[Page]` **(Read Only)** :
A list of all [custom pages](https://docs.derivative.ca/Page_Class "Page Class").

`replicator` → `OP` **(Read Only)** :
The [replicatorCOMP](https://docs.derivative.ca/ReplicatorCOMP_Class "ReplicatorCOMP Class") that created this operator, if any.

`storage` → `dict` **(Read Only)** :
[Storage](https://docs.derivative.ca/Storage "Storage") is dictionary associated with this operator. Values stored in this dictionary are persistent, and saved with the operator. The dictionary attribute is read only, but not its contents. Its contents may be manipulated directly with methods such as OP.fetch() or OP.store() described below, or examined with an [Examine DAT](https://docs.derivative.ca/Examine_DAT "Examine DAT").

`tags` → `set` :
Get or set a set of user defined strings. [Tags](https://docs.derivative.ca/Tag "Tag") can be searched using OP.findChildren() and the [OP Find DAT](https://docs.derivative.ca/OP_Find_DAT "OP Find DAT").
The set is a regular python set, and can be accessed accordingly:

```
n.tags = ['effect', 'image filter']
n.tags.add('darken')

```

`children` → `List[OP]` **(Read Only)** :
A list of [operators](https://docs.derivative.ca/OP_Class "OP Class") contained within this operator. Only [component](https://docs.derivative.ca/COMP_Class "COMP Class") operators have children, otherwise an empty list is returned.

`numChildren` → `int` **(Read Only)** :
Returns the number of children contained within the operator. Only [component](https://docs.derivative.ca/COMP_Class "COMP Class") operators have children.

`numChildrenRecursive` → `int` **(Read Only)** :
Returns the number of operators contained recursively within this operator. Only [component](https://docs.derivative.ca/COMP_Class "COMP Class") operators have children.

`op` → `OPShortcut` **(Read Only)** :
The operator finder object, for accessing operators through paths or shortcuts. **Note:** a version of this method that searches relative to '/' is also in the global [td module](https://docs.derivative.ca/Td_Module "Td Module").
`**op(pattern1, pattern2..., includeUtility=False)**`→`OP[](https://docs.derivative.ca/OP_Class "OP Class") or None`

>> Returns the first OP whose path matches the given pattern, relative to the inside of this operator. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used.

  * `pattern` - Can be string following the [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.
  * `includeUtility` **(Optional)** - if True, allow [Utility nodes](https://docs.derivative.ca/Network_Utilities:_Comments,_Network_Boxes,_Annotates "Network Utilities: Comments, Network Boxes, Annotates") to be returned. If False, Utility operators will be ignored.

>>

```
b = op('project1')
b = op('foot*', 'hand*') #comma separated
b = op('foot* hand*')  #space separated
b = op(154)

```

`**op.shortcut**`→`OP`

>>     An operator specified with by a [Global OP Shortcut](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut"). If no operator exists an exception is raised. These shortcuts are global, and must be unique. That is, cutting and pasting an operator with a Global OP Shortcut specified will lead to a name conflict. One shortcut must be renamed in that case. Furthermore, only components can be given Global OP Shortcuts.

  * `shortcut` - Corresponds to the Global OP Shortcut parameter specified in the target operator.

>>

```
b = op.Videoplayer

```

>> To list all Global OP Shortcuts:

```
for x in op:
	print(x)

```

`opex` → `OPEXShortcut` **(Read Only)** :
An operator finder object, for accessing operators through paths or shortcuts. Works like the op() shortcut method, except it will raise an exception if it fails to find the node instead of returning None as op() does. This is now the recommended way to get nodes in parameter expressions, as the error will be more useful than, for example, `NoneType has no attribute "par"`, that is often seen when using op(). **Note:** a version of this method that searches relative to '/' is also in the global [td module](https://docs.derivative.ca/Td_Module "Td Module").
`**op(pattern1, pattern2..., includeUtility=False)**`→`OP[](https://docs.derivative.ca/OP_Class "OP Class")`

>> Returns the first OP whose path matches the given pattern, relative to the inside of this operator. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used.

  * `pattern` - Can be string following the [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.
  * `includeUtility` **(Optional)** - if True, allow [Utility nodes](https://docs.derivative.ca/Network_Utilities:_Comments,_Network_Boxes,_Annotates "Network Utilities: Comments, Network Boxes, Annotates") to be returned. If False, Utility operators will be ignored.

>>

`parent` → `ParentShortcut` **(Read Only)** :
The [Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") object, for accessing parent components through indices or shortcuts.
**Note:** _a version of this method that searches relative to the current operator is also in the global[td module](https://docs.derivative.ca/Td_Module "Td Module")._
`parent(n)` → `OP or None`

>> The nth parent of this operator. If n not specified, returns the parent. If n = 2, returns the parent of the parent, etc. If no parent exists at that level, None is returned.

  * n - (Optional) n is the number of levels up to climb. When n = 1 it will return the operator's parent.

>>

```
p = parent(2) #grandfather

```

`parent.shortcut` → `OP`

>> A parent component specified with a shortcut. If no parent exists an exception is raised.

  * shortcut - Corresponds to the [Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") parameter specified in the target parent.

>>

```
n = parent.Videoplayer

```

>> See also Parent Shortcut for more examples.

`iop` → `IOPShortcut` **(Read Only)** :
The Internal Operator Shortcut object, for accessing internal shortcuts. See also [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators"). **Note:** a version of this method that searches relative to the current operator is also in the global [td Module](https://docs.derivative.ca/Td_Module "Td Module").

`ipar` → `IparShortcut` **(Read Only)** :
The Internal Operator Parameter Shortcut object, for accessing internal shortcuts. See also [Internal Parameters](https://docs.derivative.ca/Internal_Parameters "Internal Parameters"). **Note:** a version of this method that searches relative to the current operator is also in the global [td Module](https://docs.derivative.ca/Td_Module "Td Module").

`currentPage` → `Page[](https://docs.derivative.ca/Page_Class "Page Class")` :
Get or set the currently displayed parameter page. It can be set by setting it to another page or a string label.

```
n.currentPage = 'Common'

```

`enclosedBy` → `List[annotateCOMP]` **(Read Only)** :
The (possibly empty) list of Annotate operators enclosing this node. See also [AnnotateCOMP.enclosedOPs](https://docs.derivative.ca/AnnotateCOMP_Class "AnnotateCOMP Class").
###  Common Flags
The following methods get or set specific operator [Flags](https://docs.derivative.ca/Flag "Flag"). Note specific operators may contain other flags not in this section.


`activeViewer` → `bool` :
Get or set [Viewer Active Flag](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag").

`allowCooking` → `bool` :
Get or set [Cooking Flag](https://docs.derivative.ca/Cooking_Flag "Cooking Flag"). Only COMPs can disable this flag.

`bypass` → `bool` :
Get or set [Bypass Flag](https://docs.derivative.ca/Bypass_Flag "Bypass Flag").

`cloneImmune` → `bool` :
Get or set [Clone Immune Flag](https://docs.derivative.ca/Immune_Flag "Immune Flag").

`current` → `bool` :
Get or set [Current Flag](https://docs.derivative.ca/Current_Flag "Current Flag").

`display` → `bool` :
Get or set [Display Flag](https://docs.derivative.ca/Display_Flag "Display Flag").

`expose` → `bool` :
Get or set the [Expose Flag](https://docs.derivative.ca/Expose_Flag "Expose Flag") which hides a node from view in a network.

`lock` → `bool` :
Get or set [Lock Flag](https://docs.derivative.ca/Lock_Flag "Lock Flag").

`selected` → `bool` :
Get or set [Selected Flag](https://docs.derivative.ca/Selected_Flag "Selected Flag"). This controls if the node is part of the network selection. (yellow box around it).

`python` → `bool` :
Get or set parameter expression language as python.

`render` → `bool` :
Get or set [Render Flag](https://docs.derivative.ca/Render_Flag "Render Flag").

`showCustomOnly` → `bool` :
Get or set the Show Custom Only Flag which controls whether or not non custom parameters are display in[ parameter dialogs](https://docs.derivative.ca/Parameter_Dialog "Parameter Dialog").

`showDocked` → `bool` :
Get or set [Show Docked Flag](https://docs.derivative.ca/Docking "Docking"). This controls whether this node is visible or hidden when it is docked to another node.

`viewer` → `bool` :
Get or set [Viewer Flag](https://docs.derivative.ca/Viewer_Flag "Viewer Flag").
###  Appearance
`color` → `tuple[float, float, float]` :
Get or set color value, expressed as a 3-tuple, representing its red, green, blue values. To convert between color spaces, use the built in colorsys module.

`comment` → `str` :
Get or set comment string.

`nodeHeight` → `int` :
Get or set node height, expressed in [network editor](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class") units.

`nodeWidth` → `int` :
Get or set node width, expressed in [network editor](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class") units.

`nodeX` → `int` :
Get or set node X value, expressed in [network editor](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class") units, measured from its left edge.

`nodeY` → `int` :
Get or set node Y value, expressed in [network editor](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class") units, measured from its bottom edge.

`nodeCenterX` → `int` :
Get or set node X value, expressed in [network editor](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class") units, measured from its center.

`nodeCenterY` → `int` :
Get or set node Y value, expressed in [network editor](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class") units, measured from its center.

`dock` → `OP` :
Get or set the [operator](https://docs.derivative.ca/OP_Class "OP Class") this operator is docked to. To clear docking, set this member to None.

`docked` → `List[OP]` **(Read Only)** :
The (possibly empty) list of [operators](https://docs.derivative.ca/OP_Class "OP Class") docked to this node.
###  Connection
See also the `OP.parent` methods. To connect components together see [COMP_Class#Connection](https://docs.derivative.ca/COMP_Class#Connection "COMP Class") section.


`inputs` → `List[OP]` **(Read Only)** :
List of input [operators](https://docs.derivative.ca/OP_Class "OP Class") (via left side connectors) to this operator. To get the number of inputs, use len(OP.inputs).

`outputs` → `List[OP]` **(Read Only)** :
List of output [operators](https://docs.derivative.ca/OP_Class "OP Class") (via right side connectors) from this operator.

`inputConnectors` → `List[Connector]` **(Read Only)** :
List of input [connectors](https://docs.derivative.ca/Connector_Class "Connector Class") (on the left side) associated with this operator.

`outputConnectors` → `List[Connector]` **(Read Only)** :
List of output [connectors](https://docs.derivative.ca/Connector_Class "Connector Class") (on the right side) associated with this operator.
###  Cook Information
`cookFrame` → `float` **(Read Only)** :
Last frame at which this operator cooked.

`cookTime` → `float` **(Read Only)** :
**Deprecated** Duration of the last measured cook (in milliseconds).

`cpuCookTime` → `float` **(Read Only)** :
Duration of the last measured cook in CPU time (in milliseconds).

`cookAbsFrame` → `float` **(Read Only)** :
Last absolute frame at which this operator cooked.

`cookStartTime` → `float` **(Read Only)** :
Last offset from frame start at which this operator cook began, expressed in milliseconds.

`cookEndTime` → `float` **(Read Only)** :
Last offset from frame start at which this operator cook ended, expressed in milliseconds. Other operators may have cooked between the start and end time. See the cookTime member for this operator's specific cook duration.

`cookedThisFrame` → `bool` **(Read Only)** :
True when this operator has cooked this frame.

`cookedPreviousFrame` → `bool` **(Read Only)** :
True when this operator has cooked the previous frame.

`childrenCookTime` → `float` **(Read Only)** :
**Deprecated** The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a [COMP](https://docs.derivative.ca/COMP_Class "COMP Class") and/or has no children.

`childrenCPUCookTime` → `float` **(Read Only)** :
The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a [COMP](https://docs.derivative.ca/COMP_Class "COMP Class") and/or has no children.

`childrenCookAbsFrame` → `float` **(Read Only)** :
**Deprecated** The absolute frame on which childrenCookTime is based.

`childrenCPUCookAbsFrame` → `float` **(Read Only)** :
The absolute frame on which childrenCPUCookTime is based.

`gpuCookTime` → `float` **(Read Only)** :
Duration of GPU operations during the last measured cook (in milliseconds).

`childrenGPUCookTime` → `float` **(Read Only)** :
The total accumulated GPU cook time of all children of this operator during the last frame. Zero if the operator is not a COMP and/or has no children.

`childrenGPUCookAbsFrame` → `float` **(Read Only)** :
The absolute frame on which childrenGPUCookTime is based.

`totalCooks` → `int` **(Read Only)** :
Number of times the operator has cooked.

`cpuMemory` → `int` **(Read Only)** :
The approximate amount of CPU memory this Operator is using, in bytes.

`gpuMemory` → `int` **(Read Only)** :
The amount of GPU memory this OP is using, in bytes.
###  Type
`type` → `str` **(Read Only)** :
Operator type as a string. Example: 'oscin'.

`subType` → `str` **(Read Only)** :
Operator subtype. Currently only implemented for [components](https://docs.derivative.ca/Component "Component"). May be one of: 'panel', 'object', or empty string in the case of base components.

`opType` → `str` **(Read Only)** :
Python operator class type, as a string. Example: 'oscinCHOP'. Can be used with COMP.create() method.

`label` → `str` **(Read Only)** :
Operator type label. Example: 'OSC In'.

`icon` → `str` **(Read Only)** :
Get the letters used to create the operator's icon.

`family` → `str` **(Read Only)** :
Operator family. Example: CHOP. Use the global dictionary families for a list of each operator type.

`isFilter` → `bool` **(Read Only)** :
True if operator is a filter, false if it is a generator.

`minInputs` → `int` **(Read Only)** :
Minimum number of inputs to the operator.

`maxInputs` → `int` **(Read Only)** :
Maximum number of inputs to the operator.

`isMultiInputs` → `bool` **(Read Only)** :
True if inputs are ordered, false otherwise. Operators with an arbitrary number of inputs have unordered inputs, example [Merge CHOP](https://docs.derivative.ca/Merge_CHOP "Merge CHOP").

`visibleLevel` → `int` **(Read Only)** :
Visibility level of the operator. For example, expert operators have visibility level 1, regular operators have visibility level 0.

`isBase` → `bool` **(Read Only)** :
True if the operator is a Base (miscellaneous) [component](https://docs.derivative.ca/Component "Component").

`isCHOP` → `bool` **(Read Only)** :
True if the operator is a [CHOP](https://docs.derivative.ca/CHOP "CHOP").

`isCOMP` → `bool` **(Read Only)** :
True if the operator is a [component](https://docs.derivative.ca/Component "Component").

`isDAT` → `bool` **(Read Only)** :
True if the operator is a [DAT](https://docs.derivative.ca/DAT "DAT").

`isMAT` → `bool` **(Read Only)** :
True if the operator is a [Material](https://docs.derivative.ca/MAT "MAT").

`isObject` → `bool` **(Read Only)** :
True if the operator is an [object](https://docs.derivative.ca/Object "Object").

`isPanel` → `bool` **(Read Only)** :
True if the operator is a [Panel](https://docs.derivative.ca/Panel "Panel").

`isSOP` → `bool` **(Read Only)** :
True if the operator is a [SOP](https://docs.derivative.ca/SOP "SOP").

`isTOP` → `bool` **(Read Only)** :
True if the operators is a [TOP](https://docs.derivative.ca/TOP "TOP").

`isPOP` → `bool` **(Read Only)** :
True if the operators is a [POP](https://docs.derivative.ca/POP "POP").

`isCustom` → `bool` **(Read Only)** :
True if the operators is a [Custom Operator](https://docs.derivative.ca/Custom_Operators "Custom Operators").

`licenseType` → `str` **(Read Only)** :
Type of [License](https://docs.derivative.ca/License_Class "License Class") required for the operator.
## Methods
###  General
**NOTE** : `create()`, `copy()` and `copyOPs()` is done by the parent operator (a component). For more information see [COMP.create, COMP.copy and COMP.copyOPs methods](https://docs.derivative.ca/COMP_Class#Methods "COMP Class").


`pars(pattern)`→ `list[Par]`:
Returns a (possibly empty) list of [parameter objects](https://docs.derivative.ca/Par_Class "Par Class") that match the pattern.
  * pattern - Is a string following the [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") rules, specifying which parameters to return.

```
newlist = op('geo1').pars('t?', 'r?', 's?') #translate/rotate/scale parameters

```

Note: If searching for a single parameter given a name, it's much more efficient to use the subscript operator. For example:

```
name = 'MyName1'
op('geo1').par[name]

```

`parGroups(pattern)`→ `list[Par]`:
Returns a (possibly empty) list of [parGroup objects](https://docs.derivative.ca/ParGroup_Class "ParGroup Class") that match the pattern.
  * pattern - Is a string following the [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") rules, specifying which parameters to return.

```
debug(op('geo1').parGroups('p*'))

```

**Note:** If searching for a single ParGroup given a name, it's much more efficient to use the subscript operator. For example:

```
name = 'MyColor'
op('geo1').parGroup[name]

```

or even:

```
op('geo1').parGroup.MyColor

```

`ops(*patterns, includeUtility=False)`→ `List[OP]`:
Returns a (possibly empty) list of OPs that match the patterns, relative to the inside of this OP.
Multiple patterns may be provided. Numeric OP ids may also be used. The `ops` member is technically a Python Shortcut Object, not a true method.
  * `pattern` - Can be string following the [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") rules, specifying which OPs to return, or an integer, which must be an OP Id. Multiple patterns can be given and all matched OPs will be returned.
  * `includeUtility` - (Keyword, Optional) If specified, controls whether or not utility components (eg Comments) are included in the results.

**Note:** a version of this method that searches relative to '/' is also in the global [td module](https://docs.derivative.ca/Td_Module "Td Module").

```
newlist = n.ops('arm*', 'leg*', 'leg5/foot*')

```

`cook(force=False, recurse=False, includeUtility=False)`→ `None`:
Cook the contents of the operator if required.
  * force - (Keyword, Optional) If True, the operator will always cook, even if it wouldn't under normal circumstances.
  * recurse - (Keyword, Optional) If True, all children and sub-children of the operator will be cooked.
  * includeUtility - (Keyword, Optional) If specified, controls whether or not utility components (eg Comments) are included in the results.

`copyParameters(OP, custom=True, builtin=True)`→ `None`:
Copy all of the parameters from the specified [operator](https://docs.derivative.ca/OP_Class "OP Class"). Both operators should be the same type.
  * OP - The operator to copy.
  * custom - (Keyword, Optional) When True, custom parameters will be copied.
  * builtin - (Keyword, Optional) When True, built in parameters will be copied.

```
op('geo1').copyParameters( op('geo2') )

```

`changeType(OPtype)`→ `OP`:
Change referenced operator to a new operator type. After this call, this OP object should no longer be referenced. Instead use the returned OP object.
  * OPtype - The python class name of the operator type you want to change this operator to. This is not a string, but instead is a class defined in the global [td module](https://docs.derivative.ca/Td_Module "Td Module").

```
n = op('wave1').changeType(nullCHOP) #changes 'wave1' into a Null CHOP
n = op('text1').changeType(tcpipDAT) #changes 'text1' operator into a TCPIP DAT

```

`dependenciesTo(OP)`→ `list`:
Returns a (possibly empty) list of operator dependency paths between this operator and the specified operator. Multiple paths may be found.

`evalExpression(str)`→ `Any`:
Evaluate the expression from the context of this OP. Can be used to evaluate arbitrary snippets of code from arbitrary locations.
  * str - The expression to evaluate.

```
op('wave1').evalExpression('me.digits')  #returns 1

```

If the expression already resides in a parameter, use that parameters [evalExpression()](https://docs.derivative.ca/Par_Class "Par Class") method instead.

`destroy()`→ `None`:
Destroy the operator referenced by this OP. An exception will be raised if the OP's operator has already been destroyed.

`var(name, search=True)`→ `str`:
Evaluate a[ variable](https://docs.derivative.ca/Variables "Variables"). This will return the empty string, if not found. Most information obtained from variables (except for Root and Component variables) are accessible through other means in Python, usually in the global [td module](https://docs.derivative.ca/Td_Module "Td Module").
  * name - The variable name to search for.
  * search - (Keyword, Optional) If set to True (which is default) the operator hierarchy is searched until a variable matching that name is found. If false, the search is constrained to the operator.

`openMenu(x=None, y=None)`→ `None`:
Open a node menu for the operator at x, y. Opens at mouse if x & y are not specified.
  * x - (Keyword, Optional) The X coordinate of the menu, measured in screen pixels.
  * y - (Keyword, Optional) The Y coordinate of the menu, measured in screen pixels.

`relativePath(OP)`→ `str`:
Returns the relative path from this operator to the OP that is passed as the argument. See OP.shortcutPath for a version using expressions.

`setInputs(listOfOPs)`→ `None`:
Set all the operator inputs to the specified list.
  * listOfOPs - A list containing one or more OPs. Entries in the list can be None to disconnect specific inputs. An empty list disconnects all inputs.

`shortcutPath(OP, toParName=None)`→ `str`:
Returns an expression from this operator to the OP that is passed as the argument. See OP.relativePath for a version using relative path constants.
  * toParName - (Keyword, Optional) Return an expression to this parameter instead of its operator.

`resetPars(parNames='*', parGroupNames='*', pageNames='*', includeBuiltin=True, includeCustom=True)`→ `bool`:
Resets the specified parameters in the operator.
Returns true if anything was changed.
  * parNames (Keyword, Optional) - Specify parameters by Par name.
  * parGroupNames (Keyword, Optional) - Specify parameters by ParGroup name.
  * pageNames (Keyword, Optional) - Specify parameters by page name.
  * includeBuiltin (Keyword, Optional) - Include builtin parameters.
  * includeCustom (Keyword, Optional) - Include custom parameters.

```
op('player').resetPars(includeBuiltin=False) # only reset custom

```

`unload(cacheMemory=False)`→ `None`:
Unloads CPU and GPU for the node. The memory will be realloted next time the node cooks, so make sure nothing is still using it to keep it released.
  * cacheMemory - (Keyword, Optional) Currently only supported by the [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP"). If you are preloading into a Movie File In TOP that already has video, and the video format/resolution is the same, you can use the cacheMemory option to first unload the original movie and cache its memory, avoiding a reallocation when the `preload()` occurs. If True the memory (textures, upload buffers) of the movie will be cached for use by another movie later on. Useful if you are opening/closing many movies with the same codec and resolution.>

`asType(opType, checkType=False)`→ `OP`:
Casts this OP to the given type for editor code analysis. Returns the OP.
  * opType - The type to cast this OP to.
  * checkType: (Optional) If True, will check that this OP is of the given asType, and raise an exception if not.

###  Errors
`addScriptError(msg)`→ `None`:
Adds a script error to a node.
  * msg - The error to add.

`addError(msg)`→ `None`:
Adds an error to an operator. Only valid if added while the operator is cooking. (Example Script SOP, CHOP, DAT).
  * msg - The error to add.

`addWarning(msg)`→ `None`:
Adds a warning to an operator. Only valid if added while the operator is cooking. (Example Script SOP, CHOP, DAT).
  * msg - The error to add.

`errors(recurse=False)`→ `str`:
Get error messages associated with this OP.
  * recurse - Get errors in any children or subchildren as well.

`warnings(recurse=False)`→ `str`:
Get warning messages associated with this OP.
  * recurse - Get warnings in any children or subchildren as well.

`scriptErrors(recurse=False)`→ `str`:
Get script error messages associated with this OP.
  * recurse - Get errors in any children or subchildren as well.

`clearScriptErrors(recurse=False, error='*')`→ `None`:
Clear any errors generated during script execution. These may be generated during execution of DATs, Script Nodes, Replicator COMP callbacks, etc.
  * recurse - Clear script errors in any children or subchildren as well.
  * error - Pattern to match when clearing errors

```
op('/project1').clearScriptErrors(recurse=True)

```

`childrenCPUMemory()`→ `int`:
Returns the total CPU memory usage for all the children from this COMP.

`childrenGPUMemory()`→ `int`:
Returns the total GPU memory usage for all the children from this COMP.
###  Appearance
`resetNodeSize()`→ `None`:
Reset the node tile size to its default width and height.
###  Viewers
`closeViewer(topMost=False)`→ `None`:
Close the floating content viewers of the OP.
  * topMost - (Keyword, Optional) If True, any viewer window containing any parent of this OP is closed instead.

```
op('wave1').closeViewer()
op('wave1').closeViewer(topMost=True) # any viewer that contains 'wave1' will be closed.

```

`openViewer(unique=False, borders=True)`→ `None`:
Open a floating content viewer for the OP.
  * unique - (Keyword, Optional) If False, any existing viewer for this OP will be re-used and popped to the foreground. If unique is True, a new window is created each time instead.
  * borders - (Keyword, Optional) If true, the floating window containing the viewer will have borders.

```
op('geo1').openViewer(unique=True, borders=False) # opens a new borderless viewer window for 'geo1'

```

`resetViewer(recurse=False)`→ `None`:
Reset the OP content viewer to default view settings.
  * recurse - (Keyword, Optional) If True, this is done for all children and sub-children as well.

```
op('/').resetViewer(recurse=True) # reset the viewer for all operators in the entire file.

```

`openParameters()`→ `None`:
Open a floating dialog containing the operator parameters.
###  Storage
[Storage](https://docs.derivative.ca/Storage "Storage") can be used to keep data within components. Storage is implemented as one python dictionary per node.
When an element of storage is changed by using `n.store()` as explained below, expressions and operators that depend on it will automatically re-cook. It is retrieved with the `n.fetch()` function.
Storage is saved in `.toe` and `.tox` files and restored on startup.
Storage can hold any python object type (not just strings as in Tscript variables). Storage elements can also have optional startup values, specified separately. Use these startup values for example, to avoid saving and loading some session specific object, and instead save or load a well defined object like `None`.
See the [Examine DAT](https://docs.derivative.ca/Examine_DAT "Examine DAT") for procedurally viewing the contents of storage.


`fetch(key, default, search=True, storeDefault=False)`→ `Any`:
Return an object from the OP storage dictionary. If the item is not found, and a default it supplied, it will be returned instead.
  * key - The name of the entry to retrieve.
  * default - (Optional) If provided and no item is found then the passed value/object is returned instead.
  * storeDefault - (Keyword, Optional) If True, and the key is not found, the default is stored as well.
  * search - (Keyword, Optional) If True, the parent of each OP is searched recursively until a match is found

```
v = n.fetch('sales5', 0.0)

```

`fetchOwner(key)`→ `OP`:
Return the operator which contains the stored key, or None if not found.
  * key - The key to the stored entry you are looking for.

```
who = n.fetchOwner('sales5') #find the OP that has a storage entry called 'sales5'

```

`store(key, value)`→ `Any`:
Add the key/value pair to the OP's storage dictionary, or replace it if it already exists. If this value is not intended to be saved and loaded in the toe file, it can be be given an alternate value for saving and loading, by using the method storeStartupValue described below.
  * key - A string name for the storage entry. Use this name to retrieve the value using fetch().
  * value - The value/object to store.

```
n.store('sales5', 34.5) # stores a floating point value 34.5.
n.store('moviebank', op('/project1/movies')) # stores an OP for easy access later on.

```

`unstore(*keys)`→ `None`:
For each key, remove it from the OP's storage dictionary. Pattern Matching is supported as well.
  * keys - The name or pattern defining which key/value pairs to remove from the storage dictionary.

```
n.unstore('sales*') # removes all entries from this OPs storage that start with 'sales'

```

`storeStartupValue(key, value)`→ `None`:
Add the key/value pair to the OP's storage startup dictionary. The storage element will take on this value when the file starts up.
  * key - A string name for the storage startup entry.
  * value - The startup value/object to store.

```
n.storeStartupValue('sales5', 1) # 'sales5' will have a value of 1 when the file starts up.

```

`unstoreStartupValue(*keys)`→ `None`:
For key, remove it from the OP's storage startup dictionary. Pattern Matching is supported as well. This does not affect the stored value, just its startup value.
  * keys - The name or pattern defining which key/value pairs to remove from the storage startup dictionary.

```
n.unstoreStartupValue('sales*') # removes all entries from this OPs storage startup that start with 'sales'

```

###  Miscellaneous
`__getstate__()`→ `dict`:
Returns a dictionary with persistent data about the object suitable for pickling and deep copies.

`__setstate__()`→ `dict`:
Reads the dictionary to update persistent details about the object, suitable for unpickling and deep copies.
POPs (**Point Operators**) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
Indicator of certain states of an operator (bypass, display, lock, viewer active).
Dimension is metadata of a POP that describes the structure of the point list, which may be made of rows and columns of points (which is two dimensions of size nrows and ncolumns).
The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.
A name for a component that is accessible from any node in a project, which can be declared in a component's Global Operator Shortcut parameter.
A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.
Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.
Annotates are displayed in the Network Editor as colored rectangles containing user-authored text and graphics. It is based on the [Annotate COMP](https://docs.derivative.ca/Annotate_COMP "Annotate COMP") and allows you to document your networks with useful information like comments and node grouping.
The notches on the left and right of each [Node](https://docs.derivative.ca/Node "Node") that let you [Wire](https://docs.derivative.ca/Wire "Wire") the output of one [Operator](https://docs.derivative.ca/Operator "Operator") to the input of another of the same [Operator Family](https://docs.derivative.ca/Operator "Operator"). The notches on the top and bottom of [3D Object Components](https://docs.derivative.ca/Object "Object") and [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component") that tie the components of each sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") in a [Hierarchy](https://docs.derivative.ca/Hierarchy "Hierarchy").
To re-compute the output data of the [Operators](https://docs.derivative.ca/Operator "Operator"). An operator cooks when (1) its inputs change, (2) its [Parameters](https://docs.derivative.ca/Parameter "Parameter") change, (3) when the timeline moves forward in some cases, or (4) [Scripting](https://docs.derivative.ca/Script "Script") commands are run on the node. When the operator is a [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component"), it also cooks when a user interacts with it. When an operator cooks, it usually causes operators connected to its output to re-cook. When TouchDesigner draws the screen, it re-cooks all the [Dependencies](https://docs.derivative.ca/Dependency "Dependency") - the necessary operators in all [Networks](https://docs.derivative.ca/Network "Network"), contributing to a frame's total "cook time".
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
The sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Component](https://docs.derivative.ca/Component "Component") types that are used to define and render 3D scenes. A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.
TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](https://docs.derivative.ca/Network_Path "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
Creates copies of a component, one for every row in a table or using a Number of Replicants parameter - it is the "for-loop" of operators. Unlike [Clone](https://docs.derivative.ca/Clone "Clone"), it automatically creates copies of a master component.
Storage is a python dictionary in each operator, where users can store and fetch extra data.
TOuch Environment file, the file type used by TouchDesigner to save your entire project.
TouchDesigner Component file, the file type used to save a [Component](https://docs.derivative.ca/Component "Component") of your TouchDesigner project.
TouchDesigner's original built-in Command scripting language prior to [Python](https://docs.derivative.ca/Python "Python").
Matching names using wildcard characters and bracketing. Useful in "[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.
Matching names using wildcard characters and bracketing. Useful in "[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.
