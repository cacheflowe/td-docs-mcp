---
url: https://docs.derivative.ca/Parameter
category: Glossary
title: Parameter
---

# Parameter

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](https://docs.derivative.ca/Network_Path "Network Path"), which determine the output of the operator.

The parameter dialog is normally at the top-right of the network editor. Pressing 'p' turns off and on the parameter dialog. The parameter dialog for any operator can be opened by right-clicking on the operator and selecting "Parameters...".

Parameters in TouchDesigner only exist in [Operators](https://docs.derivative.ca/Operator "Operator") (OPs or "nodes"). Parameter types include:
  * numbers, both integer and floating point
  * number pairs, triples or quadruples (e.g. width and height, XYZ position, RGBA color)
  * on-off flags (toggles)
  * menus
  * text strings
  * [paths](https://docs.derivative.ca/Network_Path "Network Path") to other nodes in TouchDesigner networks
  * "pulse" buttons that initiate actions like running scripts
  * python objects - any python object that you can make using numbers, True/False values, strings, lists and dictionaries. The python object has to be self-contained - it cannot refer to other operators or parameters, for example.

See the [Component Editor](https://docs.derivative.ca/Component_Editor "Component Editor") to create custom parameters and see the range of parameter types that are available.

###  Parameter Modes and Evaluation

Every Parameter can be in one of four modes: Constant Mode, [Expression](https://docs.derivative.ca/Expression "Expression") Mode, [Export](https://docs.derivative.ca/Export "Export") Mode or Bind ([Binding](https://docs.derivative.ca/Binding "Binding")) Mode. An "**evaluated parameter** " is resulting value of the parameter based on its mode, expressions, exports or binds.

Parameters can be driven by [Python](https://docs.derivative.ca/Category:Python "Category:Python") expressions when the [Parameter Mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode") is in Expression Mode.

**TIP** : Pressing ctrl-e/Cmd+e with the cursor in a parameter brings up the current parameter’s expression in your text editor, making it easier to see and edit long expressions.

Parameters can be driven by [CHOPs](https://docs.derivative.ca/CHOP "CHOP") by [Exporting](https://docs.derivative.ca/Export "Export") CHOP channels to a parameter, putting the parameter in [Export Mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode"). In the example Parameter Dialog below, the Y-Translate parameter is being controlled via a CHOP channel export. This is indicated by the green color of the parameter in the dialog (think green for CHOPs!).

Parameters can be bi-directionally synced to other parameters and CHOP channels using [Binding](https://docs.derivative.ca/Binding "Binding"). The parameter will go into [Bind Mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode").

**IMPORTANT** : `op('pattern1').par.phase` is the python [parameter object](https://docs.derivative.ca/Par_Class "Par Class") which usually gets converted to an evaluated value for you, like when you use it in a parameter expression. More safely, especially when using a parameter in scripts, use `op('pattern1').par.phase.eval()`, which always gives you the final evaluated value.

[![Parameter Dialog.png](https://docs.derivative.ca/images/6/6e/Parameter_Dialog.png)](https://docs.derivative.ca/File:Parameter_Dialog.png)

###  Parameter Attributes

Parameters have numerous other attributes, some are parameter type-dependent.
  * name (internal python name you see when you roll over the parameter)
  * label
  * default value
  * minimum, maximum, clamp low, clamp high, clamp low value, clamp high value (for integers and floats)
  * menu entries
  * enable flag and enable expression (determines if you can access the parameter - usually means it it not relevant in the current state of other parameters)
  * read-only - the parameter is active and evaluating but you can't hand-edit it until you turn off read-only
  * section divider - in UI a line appears after the prior parameters

###  Custom Parameters

Custom Parameters are user created parameters which can be added to [Components](https://docs.derivative.ca/Component "Component"), [Custom Operators](https://docs.derivative.ca/Custom_Operators "Custom Operators"), and Script Operators ([Script TOP](https://docs.derivative.ca/Script_TOP "Script TOP") / [Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP") / [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP") / [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT")). In the case of Components and Script Operators, you can create/edit/delete them in the [Component Editor](https://docs.derivative.ca/Component_Editor "Component Editor").

For more information see [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters").

###  Internal Parameters

See [Internal Parameters](https://docs.derivative.ca/Internal_Parameters "Internal Parameters")

###  Sequential Parameters

See [Sequential Parameters](https://docs.derivative.ca/Sequential_Parameters "Sequential Parameters")

See also: [Parameter Python Class](https://docs.derivative.ca/Par_Class "Par Class"), [Parameter Dialog](https://docs.derivative.ca/Parameter_Dialog "Parameter Dialog"), [Parameter Mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode")

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](https://docs.derivative.ca/DAT "DAT") and in scripts.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A floating dialog, pane type, or dialog in a Network Editor that displays one operator's parameters.

Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").

Internal Parameters (iPars) act like local variables in a component. They provide a simple shortcut to collections of parameters that you create within a component, and access from anywhere in that component.

Sequential Parameters are blocks of parameters (Sequential Blocks) that can be reproduced multiple times by a user to create multiple entities.
