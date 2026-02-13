---
url: https://docs.derivative.ca/Frequently_Asked_Questions
category: CHOPs
title: Frequently_Asked_Questions
---

# Frequently Asked Questions
**Q:** How much is TouchDesigner? Do I need to buy a license to use TouchDesigner?
**A:** There are a number of different licenses available for TouchDesigner, you can read about the differences here [Licensing](https://docs.derivative.ca/Licensing "Licensing"). If you are using TouchDesigner for non-commercial and personal purposes (you are NOT getting paid for your work with TouchDesigner), then you can use [TouchDesigner Non-Commercial](https://docs.derivative.ca/TouchDesigner_Non-Commercial "TouchDesigner Non-Commercial") at no charge. All paying projects require purchase of a [Commercial](https://docs.derivative.ca/TouchDesigner_Commercial "TouchDesigner Commercial") or [Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro") licenses from the [Derivative Store](https://www.derivative.ca/shop/).

**Q:** What kind of graphics card (GPU) do I need for TouchDesigner?
**A:** TouchDesigner runs on Nvidia Geforce and Quadro GPUs or AMD Radeon and FirePro GPUs. Recent Intel integrated graphics are supported but will have limitations due to the graphics requirements of TouchDesigner. See [System Requirements](https://docs.derivative.ca/System_Requirements "System Requirements") for details.

**Q:** What is the most ideal system I should buy for TouchDesigner?
**A:** TouchDesigner runs on laptops, desktops, and rackmounts. You don't need to buy the fastest CPU, but CPU clock speed is more important than number of cores. Get the best Nvidia graphics card with the most graphics RAM you can afford. TouchDesigner can use a lot of CPU RAM, so get as much as possible.

**Q:** Does TouchDesigner benefit from having multi-core CPUs in the system.
**A:** Yes, there are quite a few parts of TouchDesigner that will use threading to off-load work onto extra CPUs. The most commonly used one is movie/audio reading and decoding, which is always done in separate threads. If you are playing high resolution movies the system will benefit greatly from having extra CPUs to do the decoding. Other things that benefit from multi-core CPUs are network communication and converting SOP data into a format that the GPU can understand.

**Q:** Can I use live audio to drive TouchDesigner visuals?
**A:** Yes, you can use live audio inputs and analyze the incoming signal to create control channels for your visuals, or you can have other audio programs send TouchDesigner raw OSC and MIDI events directly. If you use Ableton Live check out the bi-direction sync environment connecting TouchDesigner to Live called [TDAbleton](https://docs.derivative.ca/TDAbleton "TDAbleton").

**Q:** What input devices can be used with TouchDesigner?
**A:** See [Interoperability](https://docs.derivative.ca/Interoperability "Interoperability"). MIDI is fully supported in TouchDesigner, so any MIDI device will work. Software and hardware devices can also connect to TouchDesigner through [OSC](https://docs.derivative.ca/OSC "OSC") (Open Sound Control), UDP, TCP/IP, and/or serial communications. Other software like Ableton Live, apps on iOS and Android, and custom made applications can connect to TouchDesigner using these tools. There are also builtin operators for inputs from [Kinect](https://docs.derivative.ca/Kinect "Kinect") sensors, [joysticks and gamepads](https://docs.derivative.ca/Joystick_CHOP "Joystick CHOP"), [tablet and stylus](https://docs.derivative.ca/Tablet_CHOP "Tablet CHOP"), and [multi-touch devices](https://docs.derivative.ca/Multi_Touch_In_DAT "Multi Touch In DAT"). Serial devices like [Arduino](https://docs.derivative.ca/Arduino "Arduino") can interface using the [Serial DAT](https://docs.derivative.ca/Serial_DAT "Serial DAT") and/or [Serial CHOP](https://docs.derivative.ca/Serial_CHOP "Serial CHOP").

**Q:** Can TouchDesigner output to multiple screens?
**A:** Running your computer with two monitors allows two images to be displayed on two or more displays. Often the left monitor is a control panel and the right monitor(s) is a full-screen video output, at any resolution your hardware allows.
The right monitor can be a wide view sent to 2 or display outputs, or splitters like DataPathFX4 and Matrox Dualhead2Go/TripleHead2Go devices each going to a different display or projector. This can also be used for left/right eye displays. The same TouchDesigner file can run on several computers at the same time, each with a different camera view, synced through TouchDesigner [TCP/IP](https://docs.derivative.ca/Touch_In_CHOP "Touch In CHOP") pipes or [hardware frame-lock sync](https://docs.derivative.ca/Window_COMP "Window COMP"), or both.

**Q:** Does TouchDesigner support vertex, pixel, and geometry [shaders](https://docs.derivative.ca/Shader "Shader")?
**A:** Yes. [GLSL](https://docs.derivative.ca/GLSL "GLSL") shaders are supported. macOS is limited to GLSL 4.1 while Windows OS is only limited by the graphic drivers you have installed.

**Q:** Where can I find documentation for TouchDesigner?
**A:** All documentation can be found here at <https://docs.derivative.ca> and at <https://derivative.ca/UserGuide/Main_Page>.
The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
