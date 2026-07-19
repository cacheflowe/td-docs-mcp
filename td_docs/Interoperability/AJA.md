---
url: https://docs.derivative.ca/AJA
category: Interoperability
title: AJA
---

# AJA

TouchDesigner supports [AJA](https://www.aja.com/) devices in both the [Video Device In TOP](../TOPs/Video_Device_In_TOP.md "Video Device In TOP") and the [Video Device Out TOP](../TOPs/Video_Device_Out_TOP.md "Video Device Out TOP").
[![Aja vs logo.png](https://docs.derivative.ca/images/thumb/5/5f/Aja_vs_logo.png/300px-Aja_vs_logo.png)](https://docs.derivative.ca/File:Aja_vs_logo.png)
[![Kona 5.png](https://docs.derivative.ca/images/thumb/5/5a/Kona_5.png/600px-Kona_5.png)](https://docs.derivative.ca/File:Kona_5.png)

As of the writing of this article, the devices that have been tested in house are the Corvid88, Corvid44, Kona 5, Kona 4, Kona 3G, Kona HDMI and the iO 4K. Other devices will likely work as well. If any AJA device does not work please contact support@derivative.ca and we can try to get one in-house to fix any issues.

##  GPU Direct For Video Support

With the switch to Vulkan we are able to achieve similar performance via Vulkan features directly using something called Pinned Memory. This works on most GPUs (even non-Quadros), so GPU Direct For Video support is no longer needed.

##  Corvid Card Drivers

Although the AJA website does not make this clear, Corvid cards use the same drivers as the Kona cards. So downloading the latest Kona drivers should enable Corvid cards on your system.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
