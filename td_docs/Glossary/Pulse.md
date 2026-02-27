---
url: https://docs.derivative.ca/Pulse
category: Glossary
title: Pulse
---

# Pulse
To "pulse" a parameter is to send it a signal from (1) an [exported](https://docs.derivative.ca/Export "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately.
Some parameters are specifically Pulse-type parameters such as Reset Pulse in a [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP"). You can create custom Pulse-type parameters in the [Component Editor](https://docs.derivative.ca/Component_Editor "Component Editor").
A pulse via python is via the `.pulse()` function on a pulse-type parameter, for example `op('speed1').par.resetpulse.pulse()`
**TIP** : The benefit of the Pulse parameters on timed things in TouchDesigner is they act immediately - [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP")'s Reset pulses and Cue pulses on [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") etc often have a on-off toggle plus a Pulse parameter. For the on-off toggle, while they are on, even for 1 frame, it's frozen in a cued/reset state. It's better to pulse the Pulse parameter with something like `op('speed1').par.resetpulse.pulse()`, which starts counting up on the frame that it's pulsed.
A pulse from a CHOP is typically a 0 to 1 to 0 signal in a channel exported to the Pulse-type parameter.
You can also pulse a Pulse-type parameter using an expression in the parameter that goes from 0 to 1 to 0.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
To "pulse" a parameter is to send it a signal from (1) an [exported](https://docs.derivative.ca/Export "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately. A pulse via python is via the `.pulse()` function on a pulse-type parameter, such as Reset parameter in a [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP"). A pulse from a CHOP is typically a 0 to 1 to 0 signal in an exported channel.
