---
url: https://docs.derivative.ca/Panel_Component
category: Glossary
title: Panel_Component
---

# Panel Component

## Summary

Panel Components are a sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Components](https://docs.derivative.ca/Component "Component"), used to create custom interactive 2D control panels and user interfaces (also called [Panels](https://docs.derivative.ca/Panel "Panel")). They are found in the second column of Components in the OP Create dialog.

Examples are in Help > OP Snippets

The panel components are:

[Container COMP](https://docs.derivative.ca/Container_COMP "Container COMP") - holds any number of other buttons, sliders, fields, containers, etc

[Widget COMP](https://docs.derivative.ca/Widget_COMP "Widget COMP") - a Container COMP with extra functionality to support the library of [Widgets](https://docs.derivative.ca/Widgets "Widgets").

[Text COMP](https://docs.derivative.ca/Text_COMP "Text COMP") - for entering text strings and rendering text in Panels.

[Slider COMP](https://docs.derivative.ca/Slider_COMP "Slider COMP") - simple sliders in X, Y and XY, and outputs 1 or 2 channels

[Button COMP](https://docs.derivative.ca/Button_COMP "Button COMP") - simple on/off buttons, including toggle, momentary, and sets of radio buttons

[List COMP](https://docs.derivative.ca/List_COMP "List COMP") - lets you create and define lists using python

[OP Viewer COMP](https://docs.derivative.ca/OP_Viewer_COMP "OP Viewer COMP") - creates a panel out of any operator's viewer

[Parameter COMP](https://docs.derivative.ca/Parameter_COMP "Parameter COMP") - creates a panel out of any operator's parameters

[Select COMP](https://docs.derivative.ca/Select_COMP "Select COMP") - selects a Panel Component from any other location

[Table COMP](https://docs.derivative.ca/Table_COMP "Table COMP") - a concise and optimized way to create a grid of user interface gadgets

 [PanelCOMP_Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class")

[PanelCOMP Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class")

###  Panels within Panels

In 2D control panels, a Panel component is displayed within another panel ([Parenting](https://docs.derivative.ca/Parent "Parent")) in two possible ways:
  * by placing the panel inside another Panel component (normally a Container component).
  * by a node being attached to another node in the same network like in [3D Parenting](https://docs.derivative.ca/3D_Parenting "3D Parenting").

###  Scripting with Panels

See [Panel Value](https://docs.derivative.ca/Panel_Value "Panel Value"), [Panel Execute DAT](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT"), [PanelValue Class](https://docs.derivative.ca/PanelValue_Class "PanelValue Class"), [PanelCOMP Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class"), and the individual Panel COMP classes.

[OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") is a set of 700+ live examples of TouchDesigner operators. You can access snippets via the Help menu, or by right-clicking on network operators, or r-clicking on OP Create dialog items.

The Container component type is a Panel Component that holds, lays out and displays any number of other Panel Components.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D Panel Component types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

The sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Components](https://docs.derivative.ca/Component "Component") that are used to create custom interactive 2D control [panels](https://docs.derivative.ca/Panel "Panel") (Container, Widget, Text COMP Slider, Button, etc.).
