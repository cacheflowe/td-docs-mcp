---
url: https://docs.derivative.ca/Parameter_Reference
category: Glossary
title: Parameter_Reference
---

# Parameter Reference

A parameter reference can be setup between any two parameters by putting an expression in one parameter that refers to another parameter. This creates a [Link](Link.md "Link") between the two parameters such that when one changes, the other will change automatically. A Parameter reference is a type of [Link](Link.md "Link"), known in other software as a "constraint".

**Source Parameter** - this parameter is being referenced by another parameter.

**Reference Parameter** - this parameter's value is linked (referenced) to the source parameter and contains an expression.

Any change in the source parameter's value will change the referenced parameter's value.

##  Making a Parameter Reference

**Using right-click menus**

1) Right click on any parameter and select _Yank Parameter_. This will be the source parameter.

2) Go to the parameter you wish to be referenced, right-click and select _Put Yanked References_

**Using expressions**

Use a Python expression like `op('pattern1').par.phase * 20.` in the parameter.

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](Network_Path.md "Network Path"), which determine the output of the operator.

A [Link](Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](Operator_Family.md "Operator Family").

The grey dashed lines between nodes is a Reference (or [Link](Link.md "Link")). A Reference is (1) a Parameter Reference, a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](Export.md "Export"), node [Paths](Network_Path.md "Network Path") in parameters, and [expressions](Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](Wire.md "Wire") that connects nodes in the same [Operator Family](Operator_Family.md "Operator Family").

A parameter reference can be setup between any two parameters by putting an expression in one parameter that refers to another parameter. This creates a [Link](Link.md "Link") between the two parameters such that when one changes, the other will change automatically (known in other software as a "constraint").
