---
url: https://docs.derivative.ca/Parameter_DAT
category: DATs
title: Parameter_DAT
---

# Parameter DAT
## Summary

The Parameter DAT outputs a table of parameter names and values of an operator, including custom parameters, from any OP type.
It can output pre-evaluated expressions, the [Parameter Mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode") plus all attributes that define parameters - their type, label, ranges, menu items, limits, etc. in up to 24 columns of information.
[parameterDAT_Class](https://docs.derivative.ca/ParameterDAT_Class "ParameterDAT Class")

## Parameters - Parameter Page
- Operators `ops` - The operators determine where to obtain the channels. Specify or more operator names or paths. Examples: `wave1`, `slider*`, `constant[1-9] constant[10-19:2]`, `../base1`. Or select the operators using the menu.
- Parameters `parameters` - The list of parameters names (which can include wildcards) you want to get from the OP(s). One or more parameter, or * for all parameters. You can also specify a "NOT" selection with an `^`. Or select the parameter using the menu. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Include Op Name `includeopname` - Adds the OP name to the beginning of each parameter name in the table
- Rename from `renamefrom` - See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `renameto` - See [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion").
- Custom `custom` - Output the operators' custom parameters.
- Built-In `builtin` - Output the operators' built-in parameters.

## Parameters - Output Page
Toggles for information about the parameter and its value
- Header `header` - Outputs the column headers.
- Name `name` - Outputs the parameter name.
- Value `value` - Outputs the evaluated parameter value.
- Eval `eval` - Outputs the evaluated parameter value as a python object.
- Constant `constant` - Outputs the current constant value of the parameter.
- Expression `expression` - Outputs the current python expression of the parameter.
- Export `export` - Outputs the export path of the parameter.
- Mode `mode` - Outputs the current mode of the parameter (constant, expression, or export).
- Style `style` - Outputs what format the parameter is (eg. Float for float parameters, Menu for menu parameters etc.).
- Tuplet Name `tupletname` - Outputs the name of the tuplet the parameter is in. For example, tx on the Geometry COMP is a part of the 't' tuplet.
- Size `size` - Outputs the size of the tuplet. For example, tx on the Geometry COMP would have a tuplet size of 3 since it's a part of the 't' tuplet with 3 parameters.
- Path `path` - Outputs the path to the node.
- Menu Index `menuindex` - If the parameter is a menu, then output the selected index of the menu.

## Parameters - Define Page
Toggles for information that define the parameter.
- Min/Max `minmax` - Outputs the minimum and maximum values of the parameter. These values will clamp the value parameter to be within the range. If clampmin is 0 then the minimum will not clamp and the row/column entry will be 0. If clampmax is 0 then the maximum will not clamp and the row/column entry will be 1.
- Clamp Min/Max `clampminmax` - Outputs whether or not the parameter has a clamped min or clamped max. If true, then the values are defined by min/max columns.
- Norm Min/Max `normminmax` - Outputs the minimum and maximum values of the parameter in the interface (ie. the minimum and maximum values of a slider).
- Default `default` - Outputs the default value of the parameter
- Enabled `enabled` - Outputs whether the parameter is currently enabled
- Read Only `readonly` - Outputs whether the parameter is currently read-only
- Section `section` - Outputs whether the parameter has a section divider/separator (ie. line) above it.
- Menu Names `menunames` - Outputs a list of the menu names for any menu parameters.
- Menu Labels `menulabels` - Outputs a list of the menu labels for any menu parameters.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * From Language `language` - pick extension from DATs script language.
  * Custom Extension `custom` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.
