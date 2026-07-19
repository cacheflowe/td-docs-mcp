---
url: https://docs.derivative.ca/Event
category: Glossary
title: Event
---

# Event

**Events** in TouchDesigner are single-moment occurrences that are generated from a variety of conditions - from input actions that a user causes, from external devices and software, and from internal TouchDesigner states caused by things like timers and values crossing thresholds.

A variety of operators (mostly DATs) respond to events. Each one has python callback functions in a DAT that enable a user to write code to react to events.

TouchDesigner is a [Procedural](Procedural.md "Procedural") pull-based system (outputs to displays, audio devices and other destinations cook the nodes it needs to generate the outputs). But it is also a push system based on operators that respond to events.

The event operators respond to events they receive via their python callback functions. The callbacks can cause other operators to change and cook via their parameters, table cells, extension properties, storage.

###  Operators that Respond to Events

The operators that respond to events are:

The groups of "Execute" DATs that respond to changes within TouchDesigner:
  * [CHOP Execute DAT](../DATs/CHOP_Execute_DAT.md "CHOP Execute DAT")
  * [Parameter Execute DAT](../DATs/Parameter_Execute_DAT.md "Parameter Execute DAT")
  * [DAT Execute DAT](../DATs/DAT_Execute_DAT.md "DAT Execute DAT")
  * [Execute DAT](../DATs/Execute_DAT.md "Execute DAT")
  * [OP Execute DAT](../DATs/OP_Execute_DAT.md "OP Execute DAT")
  * [OP Find DAT](../DATs/OP_Find_DAT.md "OP Find DAT")

The DATs that respond to user interface interactions:
  * [Panel Execute DAT](Panel_Execute_DAT.md "Panel Execute DAT")
  * [Render Pick DAT](../DATs/Render_Pick_DAT.md "Render Pick DAT"), [Render Pick CHOP](../CHOPs/Render_Pick_CHOP.md "Render Pick CHOP"), [Multi Touch In DAT](../Interoperability/Multi_Touch_In_DAT.md "Multi Touch In DAT")
  * [Keyboard In DAT](../DATs/Keyboard_In_DAT.md "Keyboard In DAT")

Operators that react to external events:
  * [MIDI In DAT](../DATs/MIDI_In_DAT.md "MIDI In DAT"), [MIDI Event DAT](../DATs/MIDI_Event_DAT.md "MIDI Event DAT")
  * [OSC In DAT](../DATs/OSC_In_DAT.md "OSC In DAT")
  * [Serial DAT](../Interoperability/Serial_DAT.md "Serial DAT")
  * [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT")
  * [WebSocket DAT](../Interoperability/WebSocket_DAT.md "WebSocket DAT")
  * [Web Client DAT](../Interoperability/Web_Client_DAT.md "Web Client DAT")
  * [Web Server DAT](../Interoperability/Web_Server_DAT.md "Web Server DAT")
  * [UDP In DAT](../Interoperability/UDP_In_DAT.md "UDP In DAT")
  * [Art-Net DAT](https://docs.derivative.ca/Art-Net_DAT "Art-Net DAT")
  * [Folder DAT](../DATs/Folder_DAT.md "Folder DAT")
  * [Monitors DAT](../DATs/Monitors_DAT.md "Monitors DAT")
  * [MQTT Client DAT](../DATs/MQTT_Client_DAT.md "MQTT Client DAT")

Operators that run scripts when some of their their parameters are pulsed:
  * [Timer CHOP](../CHOPs/Timer_CHOP.md "Timer CHOP")
  * [Event CHOP](../CHOPs/Event_CHOP.md "Event CHOP")

And operators that react to event pulses:
  * [Trigger CHOP](../CHOPs/Trigger_CHOP.md "Trigger CHOP")
  * [Speed CHOP](Speed_CHOP.md "Speed CHOP")
  * [Count CHOP](../CHOPs/Count_CHOP.md "Count CHOP")
  * the numerous operators that react to [Initialize and Start](../Learn/Initialize_Start.md "Initialize Start") pulses.

Operators like [OP Find DAT](../DATs/OP_Find_DAT.md "OP Find DAT") and [Folder DAT](../DATs/Folder_DAT.md "Folder DAT"), have callbacks that are called when conditions change. The callbacks can then change parameters and subsequently cause nodes to cook.

[Pulse](Pulse.md "Pulse") type parameters of operators can be pulsed using `OP.par._parname_.pulse()`. Custom Pulse type parameters can cause the pulse callback in a [Parameter Execute DAT](../DATs/Parameter_Execute_DAT.md "Parameter Execute DAT").

###  Other Causes of Scripts Running

The Script operators ([Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP"), [Script DAT](../DATs/Script_DAT.md "Script DAT"), [Script TOP](../TOPs/Script_TOP.md "Script TOP"), [Script SOP](../SOPs/Script_SOP.md "Script SOP")) are not event nodes - they are part of the pull system and will cook when TouchDesigner determines it depends on some other data in TouchDesigner - channels, parameters, table cells, extension properties, storage.

When the event operators change parameters or other data, the target nodes will then cook according to the pull-system [cooking](Cook.md "Cook") rules.

**Note** : You can force a node to cook by calling `OP.cook()`. Its data is passed downstream according to the cooking rules.

**See also** : [Cook](Cook.md "Cook"), [Event CHOP](../CHOPs/Event_CHOP.md "Event CHOP"), [Procedural](Procedural.md "Procedural")

An [Operator Family](Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](Script.md "Script") or [GLSL](GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").

To "pulse" a parameter is to send it a signal from (1) an [exported](Export.md "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately. A pulse via python is via the `.pulse()` function on a pulse-type parameter, such as Reset parameter in a [Speed CHOP](Speed_CHOP.md "Speed CHOP"). A pulse from a CHOP is typically a 0 to 1 to 0 signal in an exported channel.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](../General/Python.md "Python") and the original [Tscript](Tscript.md "Tscript"). Scripts and single-line commands can also be run in the [Textport](Textport.md "Textport").
