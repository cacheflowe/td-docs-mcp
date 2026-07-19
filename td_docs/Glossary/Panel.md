---
url: https://docs.derivative.ca/Panel
category: Glossary
title: Panel
---

# Panel

A Panel, or Control Panel is a custom graphical user interface user control built within TouchDesigner. See [Panel Component](Panel_Component.md "Panel Component"), which are used to create such user interfaces.

The "look" of a panel is created using the [Text COMPs](../COMPs/Text_COMP.md "Text COMP") and [TOPs](../TOPs/TOP.md "TOP").

The "feel" or behavior is determined by the settings of the [Panel Components](Panel_Component.md "Panel Component"), the [Panel Execute DAT](Panel_Execute_DAT.md "Panel Execute DAT"), [Extensions](Extensions.md "Extensions") in the panel, the panel member of the [panelCOMP Class](../Python/PanelCOMP_Class.md "PanelCOMP Class"), and the use of the Panel CHOP which turns [Panel Values](Panel_Value.md "Panel Value") into CHOP Channels.

To display a panel in a floating or fixed-position window on your monitors, use the [Window COMP](Window_COMP.md "Window COMP").

While editing, a panel can be viewed by
  * right-clicking on a [Panel Component](Panel_Component.md "Panel Component") and selecting _View..._
  * changing [Pane](Pane.md "Pane") type to _Panel_
  * clicking on the [Pane Bar](https://docs.derivative.ca/Pane_Bar "Pane Bar") the square icon (Open Viewer) if you are working inside a Panel component

A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](Panel_Component.md "Panel Component").

A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](Panel_Component.md "Panel Component").

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

The viewer of a node can be (1) the interior of a node (the [Node Viewer](Node_Viewer.md "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](Pane.md "Pane") that graphically shows the results of an operator.
