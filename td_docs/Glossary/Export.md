---
url: https://docs.derivative.ca/Export
category: Glossary
title: Export
---

# Export

"Exporting" in TouchDesigner means sending data from a CHOP channel to a parameter. Exporting channels from [CHOPs](https://docs.derivative.ca/CHOP "CHOP") and/or data from [DATs](https://docs.derivative.ca/DAT "DAT") allow you to override parameter values of any operator.

##  [CHOP Exporting](https://docs.derivative.ca/CHOP_Export "CHOP Export")

The values in a **CHOP channel** can be sent to a [parameter](https://docs.derivative.ca/Parameter "Parameter") of any [operator](https://docs.derivative.ca/Operator "Operator"). See [CHOP Export](https://docs.derivative.ca/CHOP_Export "CHOP Export"), also referred to as **Channel Exporting**.

Here's how: Make the CHOP [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active"). Click and drag the channel to the node you want to export to - after a moment the node will become current and its parameter box will open. Continue to drag to the parameter you want and release. Select 'Export CHOP' from the small menu that pops-up.

A CHOP's exporting can be toggled on and off using the CHOP's [Export Flag](https://docs.derivative.ca/Export_Flag "Export Flag"). Exported data connections are displayed in the network by a gray-dotted data link. An arrowhead shows the direction of data flow, and is animated when cooking to inform you of activity.

You can mass-export a bunch of channels (by naming them `_opnamepath_:_parname_`) to a bunch of parameters without setting them up one-by-one. This is done by changing the CHOP's 'Export Method' parameter on the Common Page to 'Channel Name is Path:Parameter'.

##  [DAT Exporting](https://docs.derivative.ca/DAT_Export "DAT Export")

When exporting from DATs, the data (character, string, or number) is sent to an operator's parameter. See [DAT Export](https://docs.derivative.ca/DAT_Export "DAT Export"). Both CHOP and DAT Exporting let you export to parameters that are number values, flags or menus. However DAT exporting also supports exporting to parameters that are text strings, like the text string in a Text TOP, or a path in a Select TOP.

##  Exporting vs Expression References - The Perpetual Debate

Since the early dawn of mankind, TouchDesigner users have debated the pros and cons of exporting from CHOPs (and DATs) versus using expressions in parameters to reference the CHOP channels. **Which one is better?**

Firstly, since about 2017, both methods perform as well as each other. Now that expressions in parameters are "compiled" once into a fast-executing pseodocode, they pull values from CHOP channels as well as parameters pull them from CHOP exports.

So what should help you to decide one vs the other? The other factors are:
  * If channels in a CHOP are re-ordered or renamed, it will break the exporting usually, though you sometimes will be asked if a new paths should be used.
  * If channels in a CHOP are re-ordered, it will not break the CHOP channel references. If channels in a CHOP are renamed, the CHOP references are broken.
  * With expressions you can do extra math: `op('null1')[0] * 2 - 1`
  * With CHOP exporting, by naming the channels appropriately, you can mass-export a bunch of channels (`_opnamepath_:_parname_`) to a bunch of parameters without setting them up one-by-one. You can't do this with parameter references.
  * With expressions it's easier to reference parameters in other components (though it's generally bad practice to do so), and you can use all sorts of python trickery to build up those expressions.
  * Similarly, with expressions, in python you can switch which CHOP or channel you are referencing based on some logic, like `op('lfo2' if parent().par.Faster else 'lfo1')[0]`.
  * With exporting you can easily disable a bunch of exports, and using the table attached to the CHOP that's exporting, or using rclick on a parameter, you can disable one export at a time.

##  Exporting Files from TouchDesigner

Exporting TouchDesigner data to files and other applications is discussed on the [File Types](https://docs.derivative.ca/File_Types "File Types") page.

##  Exporting Movies from TouchDesigner

Refer to either the [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP") or the [Export Movie Dialog](https://docs.derivative.ca/Export_Movie_Dialog "Export Movie Dialog").

##  Examples of Exporting from CHOPs and DATs

This file demonstrates the different methods of exporting data from CHOPs and DATs to parameters in TouchDesigner: [File:Export examples.tox](https://docs.derivative.ca/File:Export_examples.tox "File:Export examples.tox")

See also [Export Flag](https://docs.derivative.ca/Export_Flag "Export Flag"), [Binding](https://docs.derivative.ca/Binding "Binding")

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](https://docs.derivative.ca/CHOP_Viewer "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](https://docs.derivative.ca/Parameter "Parameter").

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](https://docs.derivative.ca/Root "Root"). This path is displayed at the top of every [Pane](https://docs.derivative.ca/Pane "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](https://docs.derivative.ca/Folder "Folder").

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](https://docs.derivative.ca/Network_Path "Network Path"), which determine the output of the operator.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](https://docs.derivative.ca/DAT "DAT") and in scripts.
