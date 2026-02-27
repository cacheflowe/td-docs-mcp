---
url: https://docs.derivative.ca/Global_OP_Shortcut
category: Glossary
title: Global_OP_Shortcut
---

# Global OP Shortcut
Global Operator Shortcuts help you get to any [component](https://docs.derivative.ca/COMP_Class "COMP Class") from **any** [operator](https://docs.derivative.ca/OP_Class "OP Class"). In large systems you may want to access components that are not a parent of the current operator, but located in arbitrary components. Thus [Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") would not work in this case.

###  Example
You have a component `/myProject/mediaManager` that you want accessible everywhere.
Set its **Global OP Shortcut** parameter to `MediaManager`.
Then from any operator or script, `op.MediaManager`, will be equivalent to that component: `op('/myProject/mediaManager')`.
A child movie operator `movie1` in that component can then be reached anywhere by `op.MediaManager.op('movie1')`.

###  Conflicts
An error will occur if two components have the same **Global OP Shortcut**. To handle this, either rename them individually, or name them sequentially.
For example `/myProject/Player1` and `Player2` may have their shortcut parameters set with the expression: `'Player'+str(me.digits))`.
This results in shortcuts `Player1` and `Player2`.
For exact usage and details, see [OP Class#Members](https://docs.derivative.ca/OP_Class#Members "OP Class").
See also: `parent()` in [Td_Module](https://docs.derivative.ca/Td_Module "Td Module"), [Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut").
A name for a component that is accessible from any node in a project, which can be declared in a component's Global Operator Shortcut parameter.
