---
url: https://docs.derivative.ca/Multiple_Monitors
category: Glossary
title: Multiple_Monitors
---

# Multiple Monitors

##  Output to Multiple Monitors
Multiple monitors are also known as: second monitor, multi-monitors, right monitor, dual monitors, multi-display.
TouchDesigner can send video out to multiple projectors, monitors and recorders. TouchDesigner can run single-monitor or across many monitors.
Most modern graphics cards allow for at least 4 outputs. The easiest way to get more outputs is to use splitters such as [QuadHead2Go](https://www.matrox.com/en/video/products/video-walls/quadhead2go-series) or [Datapath Fx4](https://www.datapath.co.uk/datapath-products/video-wall-controllers/datapath-fx4/) monitor expansion devices.
Laptops all have different multi-monitor capabilities based on the manufacturer's specifications. Sometimes a laptop will have many output connections but still have limitations on the number of monitors it can drive simultaneously. Refer to the specifications for your specific laptop to understand its capabilities.
###  Spanning Monitors for Best Performance
TouchDesigner will run fastest in [Perform Mode](https://docs.derivative.ca/Perform_Mode "Perform Mode") if you combine all your panels into one canvas that spans across all your monitors. This can be done easily with [Container COMPs](https://docs.derivative.ca/Container_COMP "Container COMP"), then by assigning this to the [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") that is set for Perform Mode in the [Window Placement Dialog](https://docs.derivative.ca/Window_Placement_Dialog "Window Placement Dialog"). Using multiple Window COMPs is not suggested, and will result in poor performance.
Example for two 1920x1080 monitors [File:PerformMode Windows.toe](https://docs.derivative.ca/File:PerformMode_Windows.toe "File:PerformMode Windows.toe")
###  Windows
  * On the Desktop background, right-click -> Display Settings -> Multiple Displays -> Extend These Displays.

####  Combining Monitors into a Single Virtual Monitor Even Better Performance
If possible, you should also join your monitors together into a single virtual monitor using [Nvidia Mosaic](https://docs.derivative.ca/Nvidia_Geforce_vs_Quadro#Mosaic "Nvidia Geforce vs Quadro"), Nvidia Surround or AMD EyeFinity.
###  macOS
  * System Preferences -> Displays -> Arrangement -> Mirror Displays = Off.

To allow monitor spanning on macOS, make sure the following is also set
  * System Preferences -> Desktop & Dock -> Mission Control -> Displays have separate Spaces = Off

[![DisplaysHaveSeparateSpaces.png](https://docs.derivative.ca/images/thumb/d/d7/DisplaysHaveSeparateSpaces.png/650px-DisplaysHaveSeparateSpaces.png)](https://docs.derivative.ca/File:DisplaysHaveSeparateSpaces.png)
###  Additional Setup Tips
  * [Window Placement Dialog](https://docs.derivative.ca/Window_Placement_Dialog "Window Placement Dialog") can be used to quickly assign Perform mode to different Window COMPs, and adjust parameters, jump to the network, and open/close the windows.
  * [Perform Mode](https://docs.derivative.ca/Perform_Mode "Perform Mode") can be turned On and Off with the [Shortcut](https://docs.derivative.ca/Shortcut "Shortcut") keys F1 (On) and Esc (Off).
  * The **Always on Top** parameter in the Window COMP forces TouchDesigner to always be the top-most visible window.

See also [Using Multiple Graphic Cards](https://docs.derivative.ca/Using_Multiple_Graphic_Cards "Using Multiple Graphic Cards"), [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP"), [Window Placement Dialog](https://docs.derivative.ca/Window_Placement_Dialog "Window Placement Dialog")
Perform Mode is an optimized mode for live performance that only renders one specified [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") which is one window that contains your video outputs and your (optional) control interface. In Perform Mode the network editing window is not open - you edit your networks in [Designer Mode](https://docs.derivative.ca/Designer_Mode "Designer Mode"). Alternate with F1 and Esc.
A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](https://docs.derivative.ca/Designer_Mode "Designer Mode"), or (2) a user-created [Panel](https://docs.derivative.ca/Panel "Panel") inside a [Window Component](https://docs.derivative.ca/Window_COMP "Window COMP"). The user-created windows can span Multiple Monitors borderless, or be floating windows with borders, or popups.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
