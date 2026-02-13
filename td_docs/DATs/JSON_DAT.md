---
url: https://docs.derivative.ca/JSON_DAT
category: DATs
title: JSON_DAT
---

# JSON DAT
## Summary

The JSON DAT converts and filters JSON text using [JSONPath](https://docs.derivative.ca/JSONPath "JSONPath") syntax and outputs the filtered results. It eliminates having to code scripts to parse and manipulate JSON, and keeps the data flow procedural.
It expects JSON text as input and converts the input to a Python object in the `DAT.source` member.
It then filters the JSON down using the [JSONPath Filter parameter](https://docs.derivative.ca/JSONPath "JSONPath"), and it outputs the resulting data from the DAT as JSON text.
It also puts the filtered results as `DAT.results` (a Python list of results) and `DAT.result` (the first result).
You can test expressions on `DAT.source`, `DAT.result` and `DAT.results` by setting the Output menu to Expression and using expressions like `me.result['city']`, which outputs the evaluated expression from the DAT. You can then use that expression as `op('json1').result['city']` in an expression elsewhere. `DAT.expr` is also a member of the JSON DAT, for example, `op('json1').expr` returns the evaluated expression parameter.
**Output tables** : The JSON DAT can output a table by setting the Output Format menu to Table. It will do its best to take the result of the JSON Filter and form rows and columns of values and headings in a DAT table. Any cell that can't be expressed as a simple string, integer, float or boolean will be left as the JSON string of the remainder. A cell or range of cells can be further reduced with a [Select DAT](https://docs.derivative.ca/Select_DAT "Select DAT") and then passed to another JSON DAT which can convert the JSON strings to a table.
**See also:** [JSONPath](https://docs.derivative.ca/JSONPath "JSONPath"), [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets"), and the [TDJSON](https://docs.derivative.ca/TDJSON "TDJSON") functions for converting and manipulating JSON data.
[jsonDAT_Class](https://docs.derivative.ca/JsonDAT_Class "JsonDAT Class")

## Parameters - JSON Page
- Filter `filter` - A filter string following JSONPath syntax that will be used to filter the input JSON.
- Output `output` - ⊞ - Select the output of the JSON DAT.
  * Filter Result `filterresult` - Outputs list returned from applying the filter to the JSON text input.
  * Expression `expression` - Output a custom expression.

- Expression `expression` - The custom expression to output
- Format Output `formatoutput` - When enabled, the output of the DAT will formatted with indents and newlines.
- Hold Last Non-Empty Results `holdlast` - When enabled, the most recent result will be held if the results become empty, in effect only new non-empty results will update the output.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * frag `frag` -
  * glsl `glsl` -
  * html `html` -
  * md `md` -
  * py `py` -
  * rtf `rtf` -
  * tsv `tsv` -
  * txt `txt` -
  * vert `vert` -
  * xml `xml` -
  * From Language `languageext` - pick extension from DATs script language.
  * Custom Extension `customext` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Operator Inputs
  * Input 0:  - A JSON text input.

## Info CHOP Channels
Extra Information for the JSON DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common DAT Info Channels
  * num_rows - Number of rows in this DAT.

  * num_cols - Number of columns in this DAT.

###
## Common Operator Info Channels
  * total_cooks - Number of times the operator has cooked since the process started.

  * cook_time - Duration of the last cook in milliseconds.

  * cook_frame - Frame number when this operator was last cooked relative to the component timeline.

  * cook_abs_frame - Frame number when this operator was last cooked relative to the absolute time.

  * cook_start_time - Time in milliseconds at which the operator started cooking in the frame it was cooked.

  * cook_end_time - Time in milliseconds at which the operator finished cooking in the frame it was cooked.

  * cooked_this_frame - 1 if operator was cooked this frame.

  * warnings - Number of warnings in this operator if any.

  * errors - Number of errors in this operator if any.
