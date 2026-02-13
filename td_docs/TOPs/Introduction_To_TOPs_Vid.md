---
url: https://docs.derivative.ca/Introduction_To_TOPs_Vid
category: TOPs
title: Introduction_To_TOPs_Vid
---

# Introduction To TOPs Vid
**UPDATE:** At 13:00 into this vid the tutorial shows exporting from a CHOP to a TOP parameter using the CHOP Exporter in 077. In more recent versions of TouchDesigner, the CHOP Exporter has been removed. To export the the CHOP channel follow these instructions.
  1. Turn on the **Viewer Active** flag on the CHOP _null1_.
  2. Drag the _chan1_ channel from the CHOP viewer and drop it on the first **Scale** parameter (sx) of the _transform3_ TOP.
  3. Select **Export CHOP** from the pop-up dialog.

Refer to [CHOP Export](https://docs.derivative.ca/CHOP_Export "CHOP Export") for additional help exporting CHOP channels in more recent versions of TouchDesigner.
See also [Introduction to TOPs Vid Notes](https://docs.derivative.ca/Introduction_to_TOPs_Vid_Notes "Introduction to TOPs Vid Notes").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.
Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](https://docs.derivative.ca/CHOP_Viewer "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](https://docs.derivative.ca/Parameter "Parameter").
