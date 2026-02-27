---
url: https://docs.derivative.ca/Macro
category: Glossary
title: Macro
---

# Macro

A **macro** is a single word that represents a script of commands. The user can pass arguments to the script via the macro. Macros are written in the legacy [Tscript](https://docs.derivative.ca/Tscript "Tscript").

The F1 to F12 keys run macros. The F1 macro puts you in [Perform Mode](https://docs.derivative.ca/Perform_Mode "Perform Mode"). Pressing F9 or F10 over a panel brings up the network of the panel element you are pointing at.

Access Macros via Dialogs -> Macros in the TouchDesigner menu bar, and learn about the dialog at [Macros Dialog](https://docs.derivative.ca/Macros_Dialog "Macros Dialog").

Macros can be created locally in any component. A Text DAT placed inside a component's `local/macros` component will define a macro for the component, the name of the macro is the name of the Text DAT. TouchDesigner will search for a macro in the current component first, if not found it will look in the parent component, and so on up to the [Root](https://docs.derivative.ca/Root "Root"). Any macro defined in the root will be available for use anywhere in the project.

Macros can also be defined more simply by using the [Tscript](https://docs.derivative.ca/Tscript "Tscript") `Macro` Command.

See also [Script](https://docs.derivative.ca/Script "Script"), [DAT](https://docs.derivative.ca/DAT "DAT") and [Python](https://docs.derivative.ca/Python "Python").

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

The F1 to F12 keys run macros. The F1 macro puts you in [Perform Mode](https://docs.derivative.ca/Perform_Mode "Perform Mode"). Pressing F9 or F10 over a panel brings up the network of the panel element you are pointing at. Macros are written in the legacy [Tscript](https://docs.derivative.ca/Tscript "Tscript").
