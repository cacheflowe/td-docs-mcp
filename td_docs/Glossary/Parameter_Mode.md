---
url: https://docs.derivative.ca/Parameter_Mode
category: Glossary
title: Parameter_Mode
---

# Parameter Mode

Every [Parameter](Parameter.md "Parameter") can be in one of four modes: Constant Mode, [Expression](Expression.md "Expression") Mode, [Export](Export.md "Export") Mode or Bind ([Binding](Binding.md "Binding")) Mode.

Move the cursor over any parameter and press the + that appears. It exposes a new line where you can quickly switch the parameter mode:
  * Constant value (grey box)
  * Expression (blue box)
  * Export (green box)
  * Bind (purple box)

[![ParameterModes.png](https://docs.derivative.ca/images/6/67/ParameterModes.png)](https://docs.derivative.ca/File:ParameterModes.png)
Every parameter holds a constant value. Optionally, a python expression can be added to any parameter. The parameter can save different values in both modes and the mode can changed between constant or expression at any time. Click on the blue box to enter python expression mode, and on the grey box to return to constant value mode.

Export mode can only be selected if there is already an [Export](Export.md "Export") to the parameter. When an export is created to a parameter, the mode will be automatically set to export. After this export connection has been made, the parameter can be set to constant or expression and back to export at any time. This can be a helpful way to temporarily break an export connection when developing or debuging (ie. switch to constant mode and test specific values).

[Binding](Binding.md "Binding") links parameters together in bi-directional connection. In this mode, changing the value via the UI or a python script will update the value of both (two or more) parameters and keep them in sync.

See [Working with Parameter Modes](Parameter_Dialog.md#Working_with_Parameter_Modes "Parameter Dialog") in the Parameters Dialog for more details.

To change Parameter Mode using python, see `mode` member of  [Par Class](../SOPs/Par_Class.md "Par Class").

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](DAT.md "DAT") and in scripts.

Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](CHOP_Viewer.md "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](Parameter.md "Parameter").

Any floating window that is not a [Pane](Pane.md "Pane") or [Viewer](Viewer.md "Viewer").

Every Parameter can be in one of four modes: Constant Mode, [Expression](Expression.md "Expression") Mode, [Export](Export.md "Export") Mode or Bind ([Binding](Binding.md "Binding")) Mode.
