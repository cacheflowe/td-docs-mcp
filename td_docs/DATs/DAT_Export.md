---
url: https://docs.derivative.ca/DAT_Export
category: DATs
title: DAT_Export
---

# DAT Export
DAT exporting sends numbers, strings or expressions in a table format to a [parameter](https://docs.derivative.ca/Parameter "Parameter") of any [operator](https://docs.derivative.ca/Operator "Operator").
To export data from a DAT, the green Export flag at the bottom of the DAT must be on, AND the DAT must be in a table format with properly named columns. The columns are named:
`path parameter value enable `
Each row represents one value to be exported to a parameter of another node.
The `path` and `parameter` specify the network path to the operator and parameter where the data will be exported to.
The `value` column contains the data to be exported. It can be a numeric value, string value or expression.
The `enable` column is optional. When set to '0' the export in that row is disabled, when set to '1' the export is enabled.
The DAT's green [Export Flag](https://docs.derivative.ca/Export_Flag "Export Flag") must be On to enable the export. Once the export is established, a dotted data [link](https://docs.derivative.ca/Link "Link") will connect the DAT and the operator to indicate a connection.
To disable the export, simply toggle the DAT's export flag off.
[![DATexport.png](https://docs.derivative.ca/images/6/60/DATexport.png)](https://docs.derivative.ca/File:DATexport.png)
For exporting from CHOPs, see also: [CHOP Export](https://docs.derivative.ca/CHOP_Export "CHOP Export").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](https://docs.derivative.ca/CHOP_Viewer "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](https://docs.derivative.ca/Parameter "Parameter").
