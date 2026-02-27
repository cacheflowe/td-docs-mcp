---
url: https://docs.derivative.ca/Link
category: Glossary
title: Link
---

# Link
A Link or Reference is a grey dashed line between nodes that that indicates one operator is getting data from another operator. In contrast, a colored [Wire](https://docs.derivative.ca/Wire "Wire") connects the output of one node to an input of another node in the same [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
Reference / Link types include:
  1. a parameter in an OP that is a name or path to another operator - node paths where a node fetches the data of another node, as in the [Select TOP](https://docs.derivative.ca/Select_TOP "Select TOP") and [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP").
  2. a [Python](https://docs.derivative.ca/Python "Python") expression in a [Parameters](https://docs.derivative.ca/Parameter "Parameter") or a DAT script that contains:
    1. the name or path of another operator
    2. data from the output of another parameter: `op('pattern1')['chan1'][5]`
    3. a parameter of another operator: `op('pattern1').par.phase`
    4. a python member of another operator, like `op('pattern1').numSamples`
  3. a CHOP [Exporting](https://docs.derivative.ca/Export "Export") where a CHOP channel is sent to an operator [Parameter](https://docs.derivative.ca/Parameter "Parameter").
  4. s [DAT Export](https://docs.derivative.ca/DAT_Export "DAT Export") where a row of a table DAT is sent to an operator [Parameter](https://docs.derivative.ca/Parameter "Parameter").
  5. a DAT operator executing its content on changes in another node, as in the [CHOP Execute DAT](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT").

When a reference is in an expression, like `op('base1/pattern1').par.phase`, it specifies the location to retrieve a value from. for example `op('table1')[3,4]` from a table cell or `op{'pattern1')['chan1']` from a CHOP's output channel.
When a reference is a parameter in an OP, such as `/project1/pattern1`, the data output from the source OP is passed to, or shared with the OP containing the reference. For example, if it's a reference to a TOP, the source image is not copied but is used to generate the output of the OP.
In some cases a parameter that is an OP reference is actually a reference to multiple OPs - the path to multiple OPs is obtained by listing their paths or using wildcards to specify multiple OPs. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
Examples of operators that have reference parameters:
  * [Select TOP](https://docs.derivative.ca/Select_TOP "Select TOP"), [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP"), [Select DAT](https://docs.derivative.ca/Select_DAT "Select DAT")
  * [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") the names of cameras, lights and geometry objects
  * [Composite TOP](https://docs.derivative.ca/Composite_TOP "Composite TOP")
  * [Join CHOP](https://docs.derivative.ca/Join_CHOP "Join CHOP")

##  See also
[Wire](https://docs.derivative.ca/Wire "Wire"), [Reference](https://docs.derivative.ca/Reference "Reference"), [Parameter Reference](https://docs.derivative.ca/Parameter_Reference "Parameter Reference"), [Connector](https://docs.derivative.ca/Connector "Connector"), [Node](https://docs.derivative.ca/Node "Node"), [Operator](https://docs.derivative.ca/Operator "Operator")
A Link. The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](https://docs.derivative.ca/Export "Export"), node [Paths](https://docs.derivative.ca/Network_Path "Network Path") in parameters, and [expressions](https://docs.derivative.ca/Expression "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](https://docs.derivative.ca/Wire "Wire") that connects nodes in the same [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
A Link. The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
The grey dashed lines between nodes is a Reference (or Link). A Reference is (1) a [Parameter Reference](https://docs.derivative.ca/Parameter_Reference "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.
A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](https://docs.derivative.ca/Export "Export"), node [Paths](https://docs.derivative.ca/Network_Path "Network Path") in parameters, and [expressions](https://docs.derivative.ca/Expression "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](https://docs.derivative.ca/Wire "Wire") that connects nodes in the same [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
