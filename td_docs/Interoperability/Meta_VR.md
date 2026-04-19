---
url: https://docs.derivative.ca/Meta_VR
category: Interoperability
title: Meta_VR
---

# Meta VR

##  Oculus Rift and Meta Quest

TouchDesigner supports several VR headsets from Meta including the Meta Quest and Oculus Rift through the [Oculus Rift TOP](https://docs.derivative.ca/Oculus_Rift_TOP "Oculus Rift TOP") and [Oculus Rift CHOP](https://docs.derivative.ca/Oculus_Rift_CHOP "Oculus Rift CHOP").

Download three demos files: [File:OculusRiftCV1Demos.zip](https://docs.derivative.ca/File:OculusRiftCV1Demos.zip "File:OculusRiftCV1Demos.zip")
[![Oculus cv1.jpg](https://docs.derivative.ca/images/e/ea/Oculus_cv1.jpg)](https://docs.derivative.ca/File:Oculus_cv1.jpg)

###  Meta VR support in TouchDesigner

TouchDesigner has built-in support for Meta headsets through the [Oculus Rift TOP](https://docs.derivative.ca/Oculus_Rift_TOP "Oculus Rift TOP") and [Oculus Rift CHOP](https://docs.derivative.ca/Oculus_Rift_CHOP "Oculus Rift CHOP"). Both operators have a **Device** parameter to support using multiple devices connected to one machine.

**Requirements**
  * [VR hardware](https://www.meta.com/quest/)
  * Setup headset device: [Setup Headset](https://www.meta.com/quest/setup/)

**Ways to interface with Meta headsets in TouchDesigner**
  * [Oculus Rift CHOP](https://docs.derivative.ca/Oculus_Rift_CHOP "Oculus Rift CHOP") - Outputs several sets of channels such as orientation, left and right eye camera positions, acceleration and left and right eye projection matrices.
  * [Oculus Rift TOP](https://docs.derivative.ca/Oculus_Rift_TOP "Oculus Rift TOP") - Outputs the left and right images to the headset device.

###  Getting Started

The demos list above are a good starting point for developing for Meta headsets.

For Oculus devices, first ensure that the headset is configured to use the 'Extend Desktop to the HMD' display mode. This can be selected from the Oculus Configuration Utility under the Tools->Rift Display Mode menu. Direct HMD rendering is not supported for OpenGL applications yet. Once the Oculus is appearing as an extra monitor in your OS you need to ensure it has the correct orientation. By default it shows up as 'Portrait' but our tests have shown that the correct orientation is 'Landscape (Flipped)'. Use the 'Show Demo Scene' button in the Oculus Configuration Utility to test and ensure the display is setup correctly. Once the Oculus is working correctly for the demo scene in 'Extend Desktop Mode', it should also work correctly for TouchDesigner.

For Meta Quest devices, enable PC Link. This can be done within the Quest headset by going to Settings -> Link -> Link toggle. You can connect your Quest device to your PC through a physical Link cable or Air Link which uses your local Wi-Fi network. If your PC is connected to your headset, you should see the PC under Settings -> Link -> Launch -> Available PCs. Once PC Link is enabled and a PC is connected to your headset, launch Link.

####  Refresh Rate Issues

Most desktop monitors run at 60hz, but Meta headsets may run at a different refresh rate depending on the model. For example, the Oculus Rift S runs at 80hz and the Oculus Rift DV1 runs at 90hz. Windows may not feed the Oculus 80/90hz data if there are TouchDesigner windows redrawing on the 60hz monitor. If possible, set all your monitors to run at 90hz. However, many monitors don't support that. Going into perform mode with your window and ensuring the 'Redraw' parameter is off avoids this issue. In addition, V-Sync Mode in the perform Window COMP should be disabled.

###  Oculus Rift CHOP

The [Oculus Rift CHOP](https://docs.derivative.ca/Oculus_Rift_CHOP "Oculus Rift CHOP") provides two main sets of data. Each eye's camera render position via a transform matrix as 16 CHOP channels. The other set of data is each eye's projection matrix also as 16 CHOP channels. These two matrices can be used directly in the Camera COMP using the CHOP/DAT Matrix parameters for the Pre-XForm and Projection Matrix.

###  Tips for Working with Meta headsets

  * In [this video](https://youtu.be/N9GoD_1FZ5I?t=7470) Markus Heckmann walks through basic VR setup for Oculus including creating a scene, outputting to Oculus, and using 3D audio. Check the comments for a list of timestamps.
  * For additional support and troubleshooting refer to the [Meta Community forum](https://communityforums.atmeta.com/).

A [Link](https://docs.derivative.ca/Link "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](https://docs.derivative.ca/Export "Export"), node [Paths](https://docs.derivative.ca/Network_Path "Network Path") in parameters, and [expressions](https://docs.derivative.ca/Expression "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](https://docs.derivative.ca/Wire "Wire") that connects nodes in the same [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").

A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](https://docs.derivative.ca/Designer_Mode "Designer Mode"), or (2) a user-created [Panel](https://docs.derivative.ca/Panel "Panel") inside a [Window Component](https://docs.derivative.ca/Window_COMP "Window COMP"). The user-created windows can span [Multiple Monitors](https://docs.derivative.ca/Multiple_Monitors "Multiple Monitors") borderless, or be floating windows with borders, or popups.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
