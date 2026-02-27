---
url: https://docs.derivative.ca/Internal_Parameters
category: Glossary
title: Internal_Parameters
---

# Internal Parameters

[Parameters](https://docs.derivative.ca/Parameter "Parameter") are a powerful way to hold data in TouchDesigner. But putting parameters on the top level of a [component](https://docs.derivative.ca/Component "Component") that are only used inside makes the component messy. “Internal Parameters” provide a simple shortcut to parameter collections that you create within a component, accessible from anywhere in that component. They act like "persistent local variables".

##  Simplest Procedure

Most simply, right-click on a network background and select Create Internal Parameters.... You pick a shortcut `_Name_`. (By default it's the Parent Shortcut name, if it exists, or "`Local`".) When you press Apply it creates a Base COMP in your network (called `ipar_Name_`) where you can add a collection of custom parameters. When you add a parameter` _Parname_`to the Base COMP, then anywhere in your network you can refer to it with an expression like `ipar._Name_._Parname_`.

(This is set it up on the Common page of the parent component where the shortcut name and the path to the Base COMP are found in Internal OP Shortcut 1 and Internal OP 1.)

`ipar._Name_`searches up in the parent components' hierarchy until it finds a component with a matching Internal OP Shortcut name. From there it finds the Base COMP that holds the set of parameters.

See also [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").

##  Manual Procedure

Go inside any component, say `/project1` of a default TouchDesigner. Create a [Base Component](https://docs.derivative.ca/Base_COMP "Base COMP"), and name it `iparEffect`.

On `iparEffect` create a Float [Custom Parameter](https://docs.derivative.ca/Custom_Parameters "Custom Parameters") and name it `Size`.

Go to the parameters of `/project1`, to the Common page. Name your internal shortcut by setting Internal OP Shortcut 1 to `Effect`.

Give the path to the new Base Component by setting Internal OP 1 to `./iparEffect`.
[![InternalParameters.3.jpg](https://docs.derivative.ca/images/thumb/c/c2/InternalParameters.3.jpg/380px-InternalParameters.3.jpg)](https://docs.derivative.ca/File:InternalParameters.3.jpg)
The base component's parameters are now easy to get and set within your component:

Go back in `project1` and create a Circle SOP. In its Radius parameters put `ipar.Effect.Size`.

Change the Size parameter on `iparEffect`. The expression on the Circle SOP updates correctly.
[![InternalParameters.2.jpg](https://docs.derivative.ca/images/thumb/5/54/InternalParameters.2.jpg/700px-InternalParameters.2.jpg)](https://docs.derivative.ca/File:InternalParameters.2.jpg)
To set the Size parameter in a python script, create a Text DAT and in it put: `ipar.Effect.Size = 1.7`

On the Text DAT, turn off Viewer Active, and on the node rclick -> Run Script. The Size parameter on `iparEffect` will change to `1.7`.

##  Rationale

Holding values inside a component as parameters has advantages versus holding values in tables, Constant CHOPs, [Extensions](https://docs.derivative.ca/Extensions "Extensions") or [Storage](https://docs.derivative.ca/Storage "Storage"), as discussed in Pros and Cons below. Internal Parameters are simple to use, and can reduce or eliminate the need to write code in extensions. And by creating parameters inside your component, they are not needlessly exposed outside. See also [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators") or iOPs.

##  Recommendation

Name your internal parameter extension something meaningful. If it's a bin of movies, make the [Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") parameter be called `Bin`, and the internal parameter name be also `Bin`.

Like any parameter, if an internal parameter is a path to an operator, you have to write, for example, `op(ipar.Effect.Oppath)` or `ipar.Effect.Oppath.eval()`. Otherwise you generally don't need `.eval()`.

To easily see your evaluated parameters in the network, put a Parameter DAT in the Base COMP and put `./parameter1` in the Base COMP's OP Viewer parameter. The viewer will now show the Parameter DAT's table of parameters.

To see where an internal parameter comes from when it appears in a parameter expression, select the text `ipar.Effect` and put your cursor over the parameter label. It will reveal its path.

##  Discussion - Where you can Hold and Modify Data in TouchDesigner

To review, there are already several ways to hold data internally in TouchDesigner:
  * text strings located in [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT") cells and [Text DATs](https://docs.derivative.ca/Text_DAT "Text DAT")
  * pre-existing parameters (on [Constant CHOP](https://docs.derivative.ca/Constant_CHOP "Constant CHOP"), [Add SOP](https://docs.derivative.ca/Add_SOP "Add SOP"), …)
  * [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters") on the outside of components
  * CHOPs, SOPs and TOPs which are "[locked](https://docs.derivative.ca/Lock_Flag "Lock Flag")" (and harder to modify)
  * TouchDesigner-python [Storage](https://docs.derivative.ca/Storage "Storage") in any Operator
  * TouchDesigner-python [Extension](https://docs.derivative.ca/Extensions "Extensions") “Properties”
  * Regular python variables in functions and scripts (these are not persistent after a script runs)
  * data held in [Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP"), [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT") and [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP") that generate data
  * Dialogs -> Variables, where you can create variables and access them in python with `var('VARNAME')`. These are simply strings. These variables are not commonly used.
  * Internal Parameters

##  Pros and Cons of Internal Parameters

###  Benefits

  * procedural (changing the parameter causes cooking downstream reliably)
  * easily hand-editable
  * gives good visual feedback - you can see values changing live
  * you can give them easy-to-understand labels
  * their values can be python expressions dependent on other data, and they get evaluated procedurally. These custom parameters can be driven with animated expressions.
  * you can export to them with animated channels
  * there is tight control over data integrity: they have default values, minimum and maximum ranges are imposed, and menus have specific values and labels
  * it can handle multiple data types (strings, True/False booleans, integers, floats, menus, operator paths, python lists)
  * with the new Python parameter type, a parameter can also hold a python list or dictionary, where the elements are simple strings, booleans, ints and floats. (as with all custom parameters, you create Python parameters in the [Component Editor](https://docs.derivative.ca/Component_Editor_Dialog "Component Editor Dialog") under rclick -> Customize Component)
  * persistent - they are saved in a `.toe` or `.tox` as regular parameters
  * fewer syntax errors when developing
  * can be used in conjunction with extensions, sometimes replacing extensions
  * less coding, less to learn: You don't need to code python classes in a DAT to define anything.
  * are the same speed as parameters anywhere, and at least as fast as animated numbers in DAT cells.
  * are faster than python code in extensions or callbacks because they are compiled into an optimized executable format. (Roll over a parameter with an expression and you will likely see the word "Optimized" that indicates it is compiled into execution code.)

###  Limitations

  * In a parameter you cannot easily represent SOP data (points, polygons, primitives, attributes), non-trivial python structures.
  * It has not been possible to manage long lists or large arrays of 1D, 2D or 3D numbers, although now there is the Python parameter type that can hold simple lists, for example.
  * An internal parameter (any parameter) uses more memory than a DAT cell but is the same as any custom parameter.

  * The syntax for parameters that are operators is: `op(ipar.Effect.Operatorpath)`. As stated above, in the case where the parameter is not a float, integer, boolean or string, but is an operator (like the path to some node), using `ipar.Effect.Operatorpath` in an expression somewhere may resolve to the parameter object and not the value you intend, so you need to put `op(ipar.Effect.Operatorpath)`. Same with a Python type parameter.

##  Getting to ipar from Outside a Component

You may want to get the value of an `ipar` of another component, or you may want a parameter on a component to use an `ipar` of that component.

Being "internal" this isn't possible with `ipar`. But you can use a member of the component to access it: `COMP.internalParameters[**Name**]`where` _Name_`is the`ipar` name you want. `COMP.internalParameters` is a dictionary of internal parameter shortcuts found on the component.

See also [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").

Internal Parameters (iPars) act like local variables in a component. They provide a simple shortcut to collections of parameters that you create within a component, and access from anywhere in that component.

A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

TouchDesigner Component file, the file type used to save a [Component](https://docs.derivative.ca/Component "Component") of your TouchDesigner project.
