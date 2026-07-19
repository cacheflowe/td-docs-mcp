---
url: https://docs.derivative.ca/CHOP_Viewer
category: Glossary
title: CHOP_Viewer
---

# CHOP Viewer

The CHOP Viewer is a 2D graph used to preview and edit CHOP channels. Any pane in TouchDesigner can be set to CHOP Viewer (shortcut alt+5).

The path for the CHOP viewer can be set to a particular CHOP or a network. The [Display Flag](Display_Flag.md "Display Flag") of the CHOP(s) must be turned on to view the channels in the CHOP viewer. When set to a network (ie no specific CHOP), the viewer can display channel from multiple CHOPs. The viewer can be divided into multiple graphs in 3 modes, Graph Per Single Channel, Graph Per CHOP, or Graph Per Channel Name.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [CHOP](CHOP.md "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](Sample.md "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](Export.md "Export") to [Parameters](Parameter.md "Parameter").
