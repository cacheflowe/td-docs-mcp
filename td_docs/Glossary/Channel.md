---
url: https://docs.derivative.ca/Channel
category: Glossary
title: Channel
---

# Channel

A **channel** is a sequence of numbers (also known as [Samples](https://docs.derivative.ca/Sample "Sample")) that can represent motion, control signals, MIDI, audio, color maps, rolloff curves or lookup tables. Channels can be [Exported](https://docs.derivative.ca/Export "Export") to [Parameters](https://docs.derivative.ca/Parameter "Parameter").

A [CHOP](https://docs.derivative.ca/CHOP "CHOP") generated and outputs one or more channels. The group of one or more channels created by a [CHOP](https://docs.derivative.ca/CHOP "CHOP") is called a Clip. A clip is what a CHOP outputs.

Each channel of a CHOP has a channel name that can be set by the user.

Channels are passed between CHOPs in TouchDesigner networks.

A channel can also be [Exported](https://docs.derivative.ca/Export "Export") to a [Parameter](https://docs.derivative.ca/Parameter "Parameter") of any operator, overriding that parameter's value.

###  Channel Names

Channel names can contain numbers, English letters (A-Z a-z), and the special characters `-`, `_`, `:`, and `/`. Other characters will be automatically converted to `_`.

Common practice is to use only lower-case letters for channel names and `_`.

##  See Also

  * [Channel Class](https://docs.derivative.ca/Channel_Class "Channel Class")
  * [CHOP](https://docs.derivative.ca/CHOP "CHOP")
  * [Export](https://docs.derivative.ca/Export "Export")
  * [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP")

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on Channels (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
