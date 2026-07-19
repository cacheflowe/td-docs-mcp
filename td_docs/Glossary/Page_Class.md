---
url: https://docs.derivative.ca/Page_Class
category: Glossary
title: Page_Class
---

# Page Class

The Page Class describes the list of custom [parameters](../SOPs/Par_Class.md "Par Class") contained on a page. Pages are created on components via the COMP Class. See also the guide [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters").

Methods that create parameters return a [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") that was created.

To view individual attributes of each parameter such as default, min, max, etc, see the [Par Class](../SOPs/Par_Class.md "Par Class") documentation.

Pages can be accessed like a Python list of parameters:

```
page = op('button1').pages[0]	# get the page object
print(len(page))				# number of parameters on the page
debug(page[0])					# first parameter on the page
for p in pages:
	debug(m.description)		# print all the parameters on the page
```

## Members

`name` → `bool` :

Get or set the name of the page.

`owner` → `OP` **(Read Only)** :

The [OP](../Python/OP_Class.md "OP Class") to which this object belongs.

`parGroups` → `list` **(Read Only)** :

A list of [parameter groups](../Python/ParGroup_Class.md "ParGroup Class") on this page. A ParGroup is the set of parameters on one line.

`pars` → `list` **(Read Only)** :

The list of [parameters](../SOPs/Par_Class.md "Par Class") on this page.

`index` → `int` **(Read Only)** :

The numeric index of this page.

`isCustom` → `bool` **(Read Only)** :

Boolean for whether this page is custom or not.

## Methods

`appendOP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will accept references to any operator.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendCOMP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a COMP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to COMPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendObject(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a 3D Object COMP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to 3D Object COMPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendPanelCOMP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a Panel COMP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to Panel COMPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendTOP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a TOP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to TOPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendCHOP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a CHOP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to CHOPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendSOP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a SOP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to SOPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendPOP(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a POP node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to POPs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendMAT(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a MAT node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to MATs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendDAT(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a DAT node reference type [parameter](../SOPs/Par_Class.md "Par Class"). This parameter will only accept references to DATs, and will refuse operators of other families.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendInt(name, label=None, size=1, order=None, replace=True)`→ `ParGroup`:

Create a integer type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * size - (Keyword, Optional) Set the number of values associated with the parameter. When greater than 1, the parameter will be shown as multiple float fields without a slider and multiple parameters will be created with the index of the parameter appended to the parameter name, starting at 1.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendFloat(name, label=None, size=1, order=None, replace=True)`→ `ParGroup`:

Create a float type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * size - (Keyword, Optional) Set the number of values associated with the parameter. When greater than 1, the parameter will be shown as multiple float fields without a slider and multiple parameters will be created with the index of the parameter appended to the parameter name, starting at 1.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendXY(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a XY position type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=2, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendXYZ(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a XYZ position type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=3, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendXYZW(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a XYZW position type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=4, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendWH(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a WH size type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=2, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendUV(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a UV 2D texture type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=2, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendUVW(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a UVW 3D texture type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=3, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendRGB(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a RGB color type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=3, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendRGBA(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a RGBA color type [parameter](../SOPs/Par_Class.md "Par Class"). Similar to creating a float parameter with size=4, but with more appropriate default naming.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendStr(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a string type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendStrMenu(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a menu type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendMenu(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a menu type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.

To set the actual menu entries, use the [Par](../SOPs/Par_Class.md "Par Class") members: .menuNames and .menuLabels.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendFile(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a file reference type [parameter](../SOPs/Par_Class.md "Par Class"). Has built-in functionality to open a new file picker window.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendFileSave(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a file save reference type parameter. Has built-in functionality to open a new file picker window.

Returns the created parameter objects.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendFolder(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a folder reference type [parameter](../SOPs/Par_Class.md "Par Class"). Has built-in functionality to open a new folder picker window.

Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendPulse(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a pulse button type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendMomentary(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a momentary button type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendToggle(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a toggle button type [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendPython(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a python expression [parameter](../SOPs/Par_Class.md "Par Class"). Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendParGroup(name, parGroup=None, label=None, order=None, replace=True)`→ `ParGroup`:

Create a parGroup with attributes copied from an existing parameter. Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object.
  * name - The name of the parameter. Built-in names can be used as they will be automatically adjusted to match proper custom name casing (begin with uppercase letter followed by lowercase letters and numbers only).
  * parGroup - (Keyword, Optional) The parameter group to copy attributes from. If none specified, a default parameter created.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendHeader(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a header parameter. Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object. Only the value will be shown, not its label.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`appendSequence(name, label=None, order=None, replace=True)`→ `ParGroup`:

Create a Sequence header parameter. Returns the created [parameter group](../Python/ParGroup_Class.md "ParGroup Class") object. This also creates a [Sequence](../Python/Sequence_Class.md "Sequence Class") object on the Component with the same name as the parameter.
  * name - The name of the parameter.
  * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
  * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
  * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.

`destroy()`→ `None`:

Destroy the page this object refers to, and all its parameters.

`sort(*pars)`→ `None`:

Reorder custom parameter groups or parameters in specified order.

```
n = op('base1')
page = n.appendCustomPage('Custom1')
page.appendFloat('Value')
page.appendFloat('Speed')
page.appendFloat('Color')
page.sort('Speed','Color','Value')
```

`resetPars()`→ `bool`:

Resets all the parameters in the page.

Returns true if anything was changed.

```
op('geo1').pages[0].resetPars()
op('player').customPages['Setup'].resetPars()
```

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").

A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.

The sub-[Family](Operator_Family.md "Operator Family") of [Component](Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](Camera_COMP.md "Camera COMP") and [Light COMP](Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

POPs (**Point Operators**) is a new [Operator Family](Operator_Family.md "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](../TOPs/Render_TOP.md "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

MATs or Materials are an [Operator Family](Operator_Family.md "Operator Family") that applies a [Shader](Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").
