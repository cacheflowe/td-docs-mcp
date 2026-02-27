---
url: https://docs.derivative.ca/System_Requirements
category: Learn
title: System_Requirements
---

# System Requirements

System requirements for [TouchDesigner](https://docs.derivative.ca/TouchDesigner_Products "TouchDesigner Products") and [TouchPlayer](https://docs.derivative.ca/TouchPlayer "TouchPlayer").

#####  Basic Requirements

_Older than hereafter specified configurations might work but some features will not be available._

##  Windows

**Operating System**
  * Microsoft Windows 10 / Windows 11

**Hardware**
  * A minimum of 4GB GPU memory, 8GB+ is recommended.
  * The most recent [Nvidia drivers](http://www.nvidia.com/Download/index.aspx?lang=en-us), [AMD drivers](http://support.amd.com/us/gpudownload/Pages/index.aspx) or Intel drivers are recommended.

TouchDesigner requires a GPU and drivers that support Vulkan 1.1.

**Nvidia GPUs**
  * Nvidia Geforce 1000-series or better.
  * Nvidia Quadro/RTX Pascal series or better.
  * Requires Driver 530.00 or newer. Driver 581.00 or later recommended.

**AMD GPUs**
  * AMD Radeon 5000 series or better (RDNA architecture GPUs).

**Intel GPUs** NOTE: Not all features are supported on integrated video chipsets and there is a lower expectation on overall performance.
  * Intel 500 and newer GPUs (not the 5000, 6000 series). You can look for your GPU [here.](https://www.intel.ca/content/www/ca/en/support/articles/000005524/graphics.html)

##  Apple Mac

**Operating System**
  * Apple macOS 13 (Ventura) and up (See also [macOS](https://docs.derivative.ca/MacOS "MacOS"))

**Hardware**
  * Mac Pro / iMac / Mac Mini / MacBook Pro / MacBook Air 2020+
  * We require macOS 13 or higher, but we recommend running the latest macOS version your Mac supports.
  * We highly recommend a Mac with Apple Silicon for TouchDesigner. For Intel-based Macs we require a model with a discrete AMD GPU.

##  Input Devices

  * A three-button mouse with scroll-wheel is required.

##  Feature Specific Requirements

  * [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") - H.264 and H.265 hardware accelerated decoding
    * On Windows Nvidia GPU only, or macOS for codecs the hardware supports.
  * [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP") - H.264 and H.265 encoding
    * On Windows OS requires Nvidia GPU, also works on macOS.
  * [Video Stream Out TOP](https://docs.derivative.ca/Video_Stream_Out_TOP "Video Stream Out TOP") - Uses H.264 encoding
    * Windows OS & Nvidia GPU only
  * [Syphon Spout In TOP](https://docs.derivative.ca/Syphon_Spout_In_TOP "Syphon Spout In TOP") / [Syphon Spout Out TOP](https://docs.derivative.ca/Syphon_Spout_Out_TOP "Syphon Spout Out TOP")
    * For Spout on Windows, Nvidia or AMD GPUs are required, Intel does not work.
  * [Face Track CHOP](https://docs.derivative.ca/Face_Track_CHOP "Face Track CHOP") and [Face Track SOP](https://docs.derivative.ca/Face_Track_SOP "Face Track SOP")
    * Windows OS & Nvidia RTX GPU only.
    * Mesh fitting using the Face Track SOP requires a compatible mesh file that can be downloaded from external sources.
  * [Nvidia Background TOP](https://docs.derivative.ca/Nvidia_Background_TOP "Nvidia Background TOP")
    * Windows OS & Nvidia RTX GPU only.
  * [Nvidia Denoise TOP](https://docs.derivative.ca/Nvidia_Denoise_TOP "Nvidia Denoise TOP")
    * Windows OS & Nvidia RTX GPU only.
  * [Nvidia Flex](https://docs.derivative.ca/Flex "Flex")
    * Windows OS & Nvidia GPU only
  * [Nvidia Flow TOP](https://docs.derivative.ca/Nvidia_Flow_TOP "Nvidia Flow TOP")
    * Windows OS & Nvidia GPU only
  * [Notch TOP](https://docs.derivative.ca/Notch_TOP "Notch TOP") - Playback Notch blocks
    * Windows OS
  * [Optical Flow TOP](https://docs.derivative.ca/Optical_Flow_TOP "Optical Flow TOP") - detects patterns of motion in its input.
    * Windows OS & Nvidia 3000 GPU or higher
  * [Scalable Display TOP](https://docs.derivative.ca/Scalable_Display_TOP "Scalable Display TOP")
    * Windows OS
  * CUDA in [C++ TOP](https://docs.derivative.ca/CPlusPlus_TOP "CPlusPlus TOP")
    * Windows OS & Nvidia GPU only
  * [DirectX In TOP](https://docs.derivative.ca/DirectX_In_TOP "DirectX In TOP") and [DirectX Out TOP](https://docs.derivative.ca/DirectX_Out_TOP "DirectX Out TOP")
    * Windows OS & DirectX 9.0 and higher
  * [Photoshop In TOP](https://docs.derivative.ca/Photoshop_In_TOP "Photoshop In TOP")
    * Adobe Photoshop CS6 and up
  * [SVG TOP](https://docs.derivative.ca/SVG_TOP "SVG TOP")
    * Windows OS & Nvidia GPU only
  * [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") Texture Instancing
    * Windows OS & Nvidia GPU only
  * [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") Hardware Frame Lock
    * Windows OS & Nvidia Quadro Sync or AMD S400 only
  * [Pangolin CHOP](https://docs.derivative.ca/Pangolin_CHOP "Pangolin CHOP") - Drive Pangolin lasers through their Beyond software.
    * Windows OS
  * [RealSense CHOP](https://docs.derivative.ca/RealSense_CHOP "RealSense CHOP") - Skeleton and face tracking with old legacy RealSense devices.
    * Windows OS
  * [Kinect](https://docs.derivative.ca/Kinect "Kinect") 2 Support
    * Windows OS - 8 or 10
    * dedicated USB 3.0 Controller
  * [Kinect Azure TOP](https://docs.derivative.ca/Kinect_Azure_TOP "Kinect Azure TOP") / [Kinect Azure CHOP](https://docs.derivative.ca/Kinect_Azure_CHOP "Kinect Azure CHOP") - Body tracking and Player Index support
    * Windows OS
    * Nvidia GPU is recommended, but AMD and Intel graphics cards are now supported. CPU-based option is too slow for most use cases.
  * [NatNet In CHOP](https://docs.derivative.ca/NatNet_In_CHOP "NatNet In CHOP") - Receives tracking data from OptiTrack systems.
    * Windows OS
  * [Oculus Rift](https://docs.derivative.ca/Oculus_Rift "Oculus Rift")
    * Windows OS
    * Oculus Rift DK2 or CV1
  * [OpenVR](https://docs.derivative.ca/OpenVR "OpenVR") - HTC Vive or other OpenVR supported HMDs.
    * Windows OS
  * [ZED](https://docs.derivative.ca/ZED "ZED") - TOP, CHOP, POP and SOP that access ZED devices.
    * Windows OS

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

POPs (**Point Operators**) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
