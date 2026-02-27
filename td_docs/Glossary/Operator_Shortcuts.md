---
url: https://docs.derivative.ca/Operator_Shortcuts
category: Glossary
title: Operator_Shortcuts
---

# Operator Shortcuts
There are three ways to give shortcut names to operators in TouchDesigner:
[Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") access a higher level component from within that component.
[Global OP Shortcuts](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") access a unique component from anywhere in TouchDesigner.
[Internal Operator Shortcuts](https://docs.derivative.ca/Internal_Operators "Internal Operators") and the related [Internal Parameter Shortcuts](https://docs.derivative.ca/Internal_Parameters "Internal Parameters") provide easy access from operators inside a component to other operators inside that same component.
These should not be confused with [Keyboard Shortcuts](https://docs.derivative.ca/Keyboard_Shortcuts "Keyboard Shortcuts").
##  Python Shortcut Objects
There are a number of Python objects that facilitate the various operator shortcuts in TouchDesigner. They can be accessed in the global namespace through the [Td Module](https://docs.derivative.ca/Td_Module "Td Module") and they can also be accessed relative to operators as members of the [OP Class](https://docs.derivative.ca/OP_Class "OP Class"). For detailed usage instructions follow those links. A brief description of the objects themselves is below:
`**Shortcut**`- the parent object of all the other shortcut classes.
  * `**OPShortcut**`- the most commonly used shortcut, accessed through`op`. Returns an operator (or None if path not found) from a provided path (argument) or [Global OP Shortcut](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") (member).
  * `**OPEXShortcut**`- Works just like`OPShortcut` but raises an exception when an operator path is not found. Accessed through `opex`.
  * `**OPsShortcut**`- Works similarly to`OPShortcut` but accepts multiple patterns, including wildcards, as arguments and returns a list of operators that match.
  * `**ParentShortcut**`- Allows access to hierarchical parents of an operator. Returns an operator from a provided number of levels (argument) or[Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") name (member).
  * `**IOPShortcut**`- Allows access to[Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators") as defined in a components parameters. Returns an operator.
  * `**IparShortcut**`- Allows access to[Internal Parameters](https://docs.derivative.ca/Internal_Parameters "Internal Parameters") as defined in a components parameters. Returns a parameter. This is basically the same as IOPShortcut but returns the `par` member of the operator instead of the operator itself.

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.
