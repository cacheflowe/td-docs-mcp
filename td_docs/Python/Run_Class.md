---
url: https://docs.derivative.ca/Run_Class
category: Python
title: Run_Class
---

# Run Class
The Run class describes a single instance of a delayed script execution. See [Run Command Examples](https://docs.derivative.ca/Run_Command_Examples "Run Command Examples") for more info. They can be accessed from the [runs](https://docs.derivative.ca/Runs_Class "Runs Class") object. Scripts can be executed with delays with the following methods:

```
DAT.run()
Cell.run()
td.run()

```

## Members
`active` → `bool` :
Get or set whether or not this script will execute once its target frame is reached.

`group` → `str` :
Get or set the group label associated with this script.

`isCell` → `bool` **(Read Only)** :
Returns true when the source is a [cell](https://docs.derivative.ca/Cell_Class "Cell Class"), from a Cell.run() call.

`isDAT` → `bool` **(Read Only)** :
Returns true when the source is a [DAT](https://docs.derivative.ca/DAT_Class "DAT Class"), from a DAT.run() call.

`isString` → `bool` **(Read Only)** :
Returns true when the source is a string, from a td module run() call

`path` → `OP` **(Read Only)** :
The [operator](https://docs.derivative.ca/OP_Class "OP Class") location from which this script will execute.

`remainingFrames` → `int` :
Get or set the remaining number of frames before the execution will occur.

`remainingMilliseconds` → `int` :
Get or set the remaining number of milliseconds before the execution will occur.

`source` → `DAT | Cell | str` **(Read Only)** :
The source of the run. It will be either a [DAT](https://docs.derivative.ca/DAT_Class "DAT Class"), [cell](https://docs.derivative.ca/Cell_Class "Cell Class"), or string.
## Methods
`kill()`→ `None`:
Kill this run before it executes, and remove it from the global runs list, located in the [td Module](https://docs.derivative.ca/Td_Module "Td Module").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
