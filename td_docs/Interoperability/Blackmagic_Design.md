---
url: https://docs.derivative.ca/Blackmagic_Design
category: Interoperability
title: Blackmagic_Design
---

# Blackmagic Design

TouchDesigner supports [Blackmagic Design](http://www.blackmagicdesign.com) devices through the [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") and [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP").
[![BlackmagicDesign.png](https://docs.derivative.ca/images/thumb/5/5c/BlackmagicDesign.png/300px-BlackmagicDesign.png)](https://docs.derivative.ca/File:BlackmagicDesign.png)
[![DeckLink 8K Pro.png](https://docs.derivative.ca/images/thumb/8/8f/DeckLink_8K_Pro.png/300px-DeckLink_8K_Pro.png)](https://docs.derivative.ca/File:DeckLink_8K_Pro.png)[![DeckLink 4KExtreme12G.png](https://docs.derivative.ca/images/thumb/6/69/DeckLink_4KExtreme12G.png/300px-DeckLink_4KExtreme12G.png)](https://docs.derivative.ca/File:DeckLink_4KExtreme12G.png)
Blackmagic Design builds a wide array of high performance input and output video devices. They offer devices for PCI-e and USB 3.0 interfaces that are available in a variety of input/output connections such as HDMI, SDI/HD-SDI, DVI, Component, and more.

[Blackmagic Products](http://www.blackmagicdesign.com/products) can be found here.

###

Blackmagic Support in TouchDesigner

TouchDesigner has built-in native driver support for Blackmagic devices providing better performance and lower latency than WDM/DirectShow capture devices.

**Requirements**
  * [Decklink](http://www.blackmagicdesign.com/products/decklink) or [Intensity](http://www.blackmagicdesign.com/products/intensity) hardware device
  * Install the [Blackmagic Design Desktop Video](http://www.blackmagicdesign.com/support) drivers.

**Ways to interface with Blackmagic Design in TouchDesigner**
  * [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") - Captures video and timecode streams from capture cards and input devices such as the [Decklink](http://www.blackmagicdesign.com/products/decklink) and [Intensity](http://www.blackmagicdesign.com/products/intensity).
  * [Audio Device In CHOP](../CHOPs/Audio_Device_In_CHOP.md "Audio Device In CHOP") - Captures audio streams from the capture cards.
  * [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP") - Outputs video, audio and timecode from the Decklink and Intensity devices.

###

Tips for Working with Blackmagic Design

  * For additional support and troubleshooting refer to the [Blackmagic Design Community](http://forum.blackmagicdesign.com).

###  ST2110 Support

The [Decklink IP](https://www.blackmagicdesign.com/ca/products/decklinkip) devices allow using [ST2110](https://docs.derivative.ca/ST2110 "ST2110") for both input and output. It includes support for the reecnt Blackmagic 100G ST2110 cards.

Unlike SDI/HDMI workflows, the configuration of these streams is mostly done externally or automatically. ST2110 support is done via the [ST2110 In TOP](../TOPs/ST2110_In_TOP.md "ST2110 In TOP"), [ST2110 Out TOP](../TOPs/ST2110_Out_TOP.md "ST2110 Out TOP") and the [ST2110 Device CHOP](../CHOPs/ST2110_Device_CHOP.md "ST2110 Device CHOP"). Blackmagic supports NMOS as a way to configure the flows. A simple to use tool to try out working with NMOS is available from Riedel, called [NMOS Explorer](https://www.riedel.net/en/downloads/firmware-software), or you can use the Blackmagic 360P Ethernet switch to apply the routes using it's NMOS controller.

SDPs can also be manually assigned using the parameters on the [ST2110 In TOP](../TOPs/ST2110_In_TOP.md "ST2110 In TOP").

###  8K Support

Capture and output at 8K requires all 4 of the 'devices' on the 8k cards to be grouped into one. This is achieved by going to the Blackmagic Video Setup tool, going to the 'Connectors' page for device (1), and choosing 'SDI 1 to 4 In or Out' as the connector selection. Inside of TouchDesigner only one device will now be visible on the menu for this card.

###  Firmware Updating

If your Blackmagic device is not working, ensure it has the correct firmware installed for the drivers you are using. As long as your driver is version 11.5 or later, you can use the following commands from the driver installation folder (usually C:\Program Files\Blackmagic Design\Blackmagic Desktop Video):

List the devices and their firmware version:
```
 DesktopVideoUpdateTool.exe --list
```

To perform updates (-u) on all devices (-a), use:
```
 DesktopVideoUpdateTool.exe -ua
```

###  GPU Direct For Video Support

With the switch to Vulkan we are able to achieve similar performance via Vulkan features directly using something called Pinned Memory. This works on most GPUs (even non-Quadros), so GPU Direct For Video support is no longer needed.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
