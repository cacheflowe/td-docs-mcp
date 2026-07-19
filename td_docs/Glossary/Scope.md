---
url: https://docs.derivative.ca/Scope
category: Glossary
title: Scope
---

# Scope

The Scope parameter in CHOPs is powerful - Scope can be used to select which channels get affected and which get passed-through unaffected. Some CHOPs have a Scope parameter on its Common page.

Patterns can be used in the Scope: `*` (the default, means to match all channel names and therefore affect all channels), `?` (match single character. See [Pattern Matching](Pattern_Matching.md "Pattern Matching").

TOPs have Channel Mask, a similar feature.

####  Resampling

Sample Rate Match - Handle cases where multiple input CHOPs' sample rates are different. When the CHOP needs to combine inputs with different sample rates, the Sample Rate Match Options offers these choices:
  * Resample At First Input's Rate - Use rate of first input to resample others.
  * Resample At Maximum Rate - Resample to the highest sample rate.
  * Resample At Minimum Rate - Resample to the lowest sample rate.
  * Error if Rates Differ - Doesn't accept conflicting sample rates.

When Resampling occurs, the curves are interpolated according to the [Interpolation Method Option](https://docs.derivative.ca/index.php?title=Frequent_CHOP_Parameters&action=edit&redlink=1 "Frequent CHOP Parameters \(page does not exist\)"), or "Linear" if the Interpolate Options are not available.

Export Method - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](Export.md "Export") article for more information.
  * DAT Table by Index - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

Export Root - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.

Export Table - The DAT used to hold the export information when using the DAT Table Export Methods (See above).

Time Slice - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)")". A Time Slice is the time between the last cook frame and the current cook frame.

A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

samples-per-second of a [CHOP](CHOP.md "CHOP"). Each CHOP in your network has a sample rate. In contrast, the overall timeline has a [Frame Rate](Frame_Rate.md "Frame Rate"), which is the number of frames to [cook](Cook.md "Cook") and display per second, generally your monitor display frequency, default 60.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](CHOP_Viewer.md "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](Parameter.md "Parameter").

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](Root.md "Root"). This path is displayed at the top of every [Pane](Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](Folder.md "Folder").

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](Network_Path.md "Network Path"), which determine the output of the operator.

TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](Network_Path.md "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.

A Time Slice is the time from the last cook frame to the current cook frame. In CHOPs it is the set of short channels that contain the CHOP channels' samples between the last and the current cook frame.
