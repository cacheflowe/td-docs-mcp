---
url: https://docs.derivative.ca/OAK-D
category: Interoperability
title: OAK-D
---

# OAK-D

OAK-D cameras from [Luxonis](https://luxonis.com/) offer a range of high-resolution cameras with depth vision and on-chip machine learning.

OAK cameras do computer vision tasks on-device and send the processed images or data to TouchDesigner on both Windows and macOS. For example, an OAK camera can compute human skeleton landmarks for a live RGB image and send both the landmarks and image to TouchDesigner. OAK is short for the OpenCV AI Kit, which originated through online crowd-funding. [Luxonis](https://luxonis.com/) has expanded the line of OAK hardware and also released several open-source libraries such as [DepthAI](https://docs.luxonis.com/projects/api/en/latest/) that run on the OAK.

Three operator types work together to implement the OAK functionality: The [OAK Device CHOP](https://docs.derivative.ca/OAK_Device_CHOP "OAK Device CHOP") is the main interface to the camera devices. The [OAK Select CHOP](https://docs.derivative.ca/OAK_Select_CHOP "OAK Select CHOP") extracts channel and dictionary data from the camera results of a OAK Device CHOP. The [OAK Select TOP](https://docs.derivative.ca/OAK_Select_TOP "OAK Select TOP") extracts processed images from the camera. Each DepthAI model running on each camera will have one OAK Device CHOP plus one or more of the OAK Select OPs.

The aim of integrating TouchDesigner with OAK cameras is to facilitate novel interactions with the rest of the TouchDesigner environment while providing low-latency, high throughput performance with the OAK hardware, and offloading some compute to an external device.

Note: If you find a pure Python DepthAI / OpenCV example that doesn't involve TouchDesigner is running faster than one which does, please let Derivative know. For example, Derivative aims for the frames-per-second of an OAK's RGB camera received in TouchDesigner to be at least as fast as what you would receive in pure Python with DepthAI and OpenCV.

The OAK-D is an open source hardware design.

Note: A Time-of-Flight version of the camera with depth-model support is in development as of Summer 2024.

###  Installation

You must select OAK-D when installing TouchDesigner. No other installation steps are necessary. TouchDesigner's installation includes the `depthai` Python module as a [third-party package](https://docs.derivative.ca/Python_Classes_and_Modules#3rd_Party_Packages "Python Classes and Modules"). For simplicity, we ask that you not install `depthai` to any custom Python environments, even if they're not being used with TouchDesigner.

Models will download once the first time they are used.

###  Usage

The example file is `OAKExamples.toe`. Instructions and tips are inside the file. The file is located in `C:/Program Files/Derivative/TouchDesigner.2023.xxxxx/Samples/OAK`.

**NOTE:** To use this file, please copy it to a folder outside the regular program location like your user documents or desktop.

Models by default will be downloaded to %USER%/.cache/blobconverter or %USER%/.cache/TDFileDownloader depending of the source of the model.

###  Troubleshooting

If you encounter issues with the `depthai` examples, consider following these steps to help Derivative fix the issue.
  1. Confirm that the `depthai` Python module being used is from TouchDesigner's site-packages folder. Run this script in a DAT
```
import depthai as dai
print('depthai version:', dai.__version__)
print('depthai location:', dai.__file__)
```

The printed location should be inside TouchDesigner's site-packages folder, not a custom Python environment.
  2. Isolate the issue to the minimal case. Delete any TouchDesigner nodes which aren't necessary to reproduce the issue.
  3. Set the following system environment variables. Set **DEPTHAI_LEVEL** to **debug**. Also set **TOUCH_TEXT_CONSOLE** to **1**.
  4. Open the TouchDesigner project with the issue and then press alt-c to open the console. Follow whichever steps lead to the issue while observing the output in the console. Share detailed instructions of the necessary steps and the console output.

###  Power over Ethernet

Some OAK cameras connect via USB and others connect via Power over Ethernet (PoE). PoE can be used over longer distances than USB cables, but latency will be higher. At short distances, USB3 would still be faster than PoE. If you are seeing issues with PoE examples, try lowering the amount of information being exchanged over the network. For example, you could decrease the FPS of cameras, use a smaller RGB/mono resolution, or use an ISP scale other than (1,1).

A getting started and installation guide for the poe version is located on the Luxonis Website's Helppages here: <https://docs.luxonis.com/projects/hardware/en/latest/pages/guides/getting-started-with-poe/>

###  See Also

  * [OAK Device CHOP](https://docs.derivative.ca/OAK_Device_CHOP "OAK Device CHOP")
  * [OAK Select CHOP](https://docs.derivative.ca/OAK_Select_CHOP "OAK Select CHOP")
  * [OAK Select TOP](https://docs.derivative.ca/OAK_Select_TOP "OAK Select TOP")

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

The [Frames](https://docs.derivative.ca/Frame "Frame")-per-Second that TouchDesigner's [Timeline](https://docs.derivative.ca/Timeline "Timeline") runs at. Set with `project.cookRate`.
