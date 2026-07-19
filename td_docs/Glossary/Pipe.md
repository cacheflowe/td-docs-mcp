---
url: https://docs.derivative.ca/Pipe
category: Glossary
title: Pipe
---

# Pipe

A **pipe** is anything that allows the transfer of data from one process to another. The primary way to move data in TouchDesigner is by using specially designed [Operators](../General/Operator.md "Operator"), listed below:
Data Type  | Input  | Output
---|---|---
Images  | Touch In TOP | Touch Out TOP
Channels  | Touch In CHOP -OR- Pipe In CHOP | Touch Out CHOP -OR- Pipe Out CHOP
Data  | TCP or UDP  | TCP or UDP
An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A way of moving data from one TouchDesigner process to another. Images are moved via Touch Out / In TOPs, channels are moved via Touch Out / In CHOPs and Pipe Out / In CHOPs. Data moves via TCP/IP or UDP.
