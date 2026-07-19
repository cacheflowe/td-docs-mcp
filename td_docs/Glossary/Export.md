---
url: https://docs.derivative.ca/Export
category: Glossary
title: Export
---

# Export

"Exporting" in TouchDesigner means sending data from a CHOP channel to a parameter. Exporting channels from [CHOPs](CHOP.md "CHOP") and/or data from [DATs](DAT.md "DAT") allow you to override parameter values of any operator.

##  [CHOP Exporting](https://docs.derivative.ca/CHOP_Export "CHOP Export")

The values in a **CHOP channel** can be sent to a [parameter](Parameter.md "Parameter") of any [operator](../General/Operator.md "Operator"). See [CHOP Export](https://docs.derivative.ca/CHOP_Export "CHOP Export"), also referred to as **Channel Exporting**.

Here's how: Make the CHOP [Viewer Active](Viewer_Active.md "Viewer Active"). Click and drag the channel to the node you want to export to - after a moment the node will become current and its parameter box will open. Continue to drag to the parameter you want and release. Select 'Export CHOP' from the small menu that pops-up.

A CHOP's exporting can be toggled on and off using the CHOP's [Export Flag](https://docs.derivative.ca/Export_Flag "Export Flag"). Exported data connections are displayed in the network by a gray-dotted data link. An arrowhead shows the direction of data flow, and is animated when cooking to inform you of activity.

You can mass-export a bunch of channels (by naming them `_opnamepath_:_parname_`) to a bunch of parameters without setting them up one-by-one. This is done by changing the CHOP's 'Export Method' parameter on the Common Page to 'Channel Name is Path:Parameter'.

##  [DAT Exporting](../DATs/DAT_Export.md "DAT Export")

When exporting from DATs, the data (character, string, or number) is sent to an operator's parameter. See [DAT Export](../DATs/DAT_Export.md "DAT Export"). Both CHOP and DAT Exporting let you export to parameters that are number values, flags or menus. However DAT exporting also supports exporting to parameters that are text strings, like the text string in a Text TOP, or a path in a Select TOP.

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

Exporting TouchDesigner data to files and other applications is discussed on the [File Types](../Interoperability/File_Types.md "File Types") page.

##  Exporting Movies from TouchDesigner

Refer to either the [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP") or the [Export Movie Dialog](https://docs.derivative.ca/Export_Movie_Dialog "Export Movie Dialog").

##  Examples of Exporting from CHOPs and DATs

This file demonstrates the different methods of exporting data from CHOPs and DATs to parameters in TouchDesigner: [File:Export examples.tox](https://docs.derivative.ca/File:Export_examples.tox "File:Export examples.tox")

See also [Export Flag](https://docs.derivative.ca/Export_Flag "Export Flag"), [Binding](Binding.md "Binding")

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](CHOP_Viewer.md "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](Parameter.md "Parameter").

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](Root.md "Root"). This path is displayed at the top of every [Pane](Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](Folder.md "Folder").

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](Network_Path.md "Network Path"), which determine the output of the operator.

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](DAT.md "DAT") and in scripts.
