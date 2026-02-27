---
url: https://docs.derivative.ca/Event
category: Glossary
title: Event
---

# Event

**Events** in TouchDesigner are single-moment occurrences that are generated from a variety of conditions - from input actions that a user causes, from external devices and software, and from internal TouchDesigner states caused by things like timers and values crossing thresholds.

A variety of operators (mostly DATs) respond to events. Each one has python callback functions in a DAT that enable a user to write code to react to events.

TouchDesigner is a [Procedural](https://docs.derivative.ca/Procedural "Procedural") pull-based system (outputs to displays, audio devices and other destinations cook the nodes it needs to generate the outputs). But it is also a push system based on operators that respond to events.

The event operators respond to events they receive via their python callback functions. The callbacks can cause other operators to change and cook via their parameters, table cells, extension properties, storage.

###  Operators that Respond to Events

The operators that respond to events are:

The groups of "Execute" DATs that respond to changes within TouchDesigner:
  * [CHOP Execute DAT](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT")
  * [Parameter Execute DAT](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT")
  * [DAT Execute DAT](https://docs.derivative.ca/DAT_Execute_DAT "DAT Execute DAT")
  * [Execute DAT](https://docs.derivative.ca/Execute_DAT "Execute DAT")
  * [OP Execute DAT](https://docs.derivative.ca/OP_Execute_DAT "OP Execute DAT")
  * [OP Find DAT](https://docs.derivative.ca/OP_Find_DAT "OP Find DAT")

The DATs that respond to user interface interactions:
  * [Panel Execute DAT](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT")
  * [Render Pick DAT](https://docs.derivative.ca/Render_Pick_DAT "Render Pick DAT"), [Render Pick CHOP](https://docs.derivative.ca/Render_Pick_CHOP "Render Pick CHOP"), [Multi Touch In DAT](https://docs.derivative.ca/Multi_Touch_In_DAT "Multi Touch In DAT")
  * [Keyboard In DAT](https://docs.derivative.ca/Keyboard_In_DAT "Keyboard In DAT")

Operators that react to external events:
  * [MIDI In DAT](https://docs.derivative.ca/MIDI_In_DAT "MIDI In DAT"), [MIDI Event DAT](https://docs.derivative.ca/MIDI_Event_DAT "MIDI Event DAT")
  * [OSC In DAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT")
  * [Serial DAT](https://docs.derivative.ca/Serial_DAT "Serial DAT")
  * [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT")
  * [WebSocket DAT](https://docs.derivative.ca/WebSocket_DAT "WebSocket DAT")
  * [Web Client DAT](https://docs.derivative.ca/Web_Client_DAT "Web Client DAT")
  * [Web Server DAT](https://docs.derivative.ca/Web_Server_DAT "Web Server DAT")
  * [UDP In DAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT")
  * [Art-Net DAT](https://docs.derivative.ca/Art-Net_DAT "Art-Net DAT")
  * [Folder DAT](https://docs.derivative.ca/Folder_DAT "Folder DAT")
  * [Monitors DAT](https://docs.derivative.ca/Monitors_DAT "Monitors DAT")
  * [MQTT Client DAT](https://docs.derivative.ca/MQTT_Client_DAT "MQTT Client DAT")

Operators that run scripts when some of their their parameters are pulsed:
  * [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP")
  * [Event CHOP](https://docs.derivative.ca/Event_CHOP "Event CHOP")

And operators that react to event pulses:
  * [Trigger CHOP](https://docs.derivative.ca/Trigger_CHOP "Trigger CHOP")
  * [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP")
  * [Count CHOP](https://docs.derivative.ca/Count_CHOP "Count CHOP")
  * the numerous operators that react to [Initialize and Start](https://docs.derivative.ca/Initialize_Start "Initialize Start") pulses.

Operators like [OP Find DAT](https://docs.derivative.ca/OP_Find_DAT "OP Find DAT") and [Folder DAT](https://docs.derivative.ca/Folder_DAT "Folder DAT"), have callbacks that are called when conditions change. The callbacks can then change parameters and subsequently cause nodes to cook.

[Pulse](https://docs.derivative.ca/Pulse "Pulse") type parameters of operators can be pulsed using `OP.par._parname_.pulse()`. Custom Pulse type parameters can cause the pulse callback in a [Parameter Execute DAT](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT").

###  Other Causes of Scripts Running

The Script operators ([Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP"), [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT"), [Script TOP](https://docs.derivative.ca/Script_TOP "Script TOP"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP")) are not event nodes - they are part of the pull system and will cook when TouchDesigner determines it depends on some other data in TouchDesigner - channels, parameters, table cells, extension properties, storage.

When the event operators change parameters or other data, the target nodes will then cook according to the pull-system [cooking](https://docs.derivative.ca/Cook "Cook") rules.

**Note** : You can force a node to cook by calling `OP.cook()`. Its data is passed downstream according to the cooking rules.

**See also** : [Cook](https://docs.derivative.ca/Cook "Cook"), [Event CHOP](https://docs.derivative.ca/Event_CHOP "Event CHOP"), [Procedural](https://docs.derivative.ca/Procedural "Procedural")

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").

To "pulse" a parameter is to send it a signal from (1) an [exported](https://docs.derivative.ca/Export "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately. A pulse via python is via the `.pulse()` function on a pulse-type parameter, such as Reset parameter in a [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP"). A pulse from a CHOP is typically a 0 to 1 to 0 signal in an exported channel.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").
