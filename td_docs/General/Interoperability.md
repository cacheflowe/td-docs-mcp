---
url: https://docs.derivative.ca/Interoperability
category: General
title: Interoperability
---

# Interoperability

TouchDesigner supports a wide range of devices, protocols and external tools that interface via their respective [Operators](Operator.md "Operator"), [Palette](../Learn/Palette.md "Palette") components, and TouchDesigner Python methods, known collectively as TouchDesigner's Interops.

### Video Capture and Output Cards

[Blackmagic (SDI, ST2110, HDMI)](../Interoperability/Blackmagic_Design.md "Blackmagic Design") | [AJA (SDI, ST2110, HDMI)](../Interoperability/AJA.md "AJA") | [Deltacast](../Interoperability/Deltacast.md "Deltacast") | [Bluefish](../Interoperability/Bluefish444.md "Bluefish444") | [Datapath](https://www.datapath-us.com/) | [DirectShow](https://en.wikipedia.org/wiki/DirectShow) | [Windows Media Foundation](https://en.wikipedia.org/wiki/Media_Foundation) | [NVIDIA Direct Display](../TOPs/Direct_Display_Out_TOP.md "Direct Display Out TOP")

###  IP Cameras

[IDS](https://www.ids-imaging.us/) | [Ximea](https://www.ximea.com/) | [Point Grey/Flir](https://www.flir.com/) | [Allied Vision](https://www.alliedvision.com/en/)

###  Movie File Codecs

[Many codecs supported by FFMPEG](../Interoperability/FFmpeg.md "FFmpeg") | [H.266 H.265 H.264](../Interoperability/FFmpeg.md "FFmpeg") | [Hap, Hap Q, Hap R and Hap HDR](../Interoperability/Hap.md "Hap") | [NotchLC](../Interoperability/Notch.md#NotchLC_Codec "Notch") | [EXR](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") | [Apple ProRes](../Interoperability/Apple_ProRes.md "Apple ProRes") | [AV1](../Interoperability/AV1.md "AV1") | [GoPro Cineform](../Interoperability/GoPro_Cineform.md "GoPro Cineform") |

###  Video Streaming

[Newtek NDI](../Interoperability/NDI.md "NDI") | [H.264 and HLS/DASH Streaming](../TOPs/Video_Stream_In_TOP.md "Video Stream In TOP") | [RTMP and Enhanced RTMP](../TOPs/Video_Stream_Out_TOP.md "Video Stream Out TOP") | [Syphon and Spout](../TOPs/Syphon_Spout_In_TOP.md "Syphon Spout In TOP") | [WebRTC](../Interoperability/WebRTC.md "WebRTC") | [RTSP](../Interoperability/RTSP.md "RTSP") | [SRT](../Interoperability/SRT.md "SRT") | [NDI Stream from iPhone](https://apps.apple.com/ca/app/ndi-camera-easy-streaming/id1477266080) | [iPhone as macOS Video Device In](https://www.engadget.com/mobile/smartphones/how-to-use-your-iphone-as-a-webcam-with-your-mac-164248242.html) |

###  DMX-Based Protocols

[DMX](../Interoperability/DMX.md "DMX") | [Art-Net](https://docs.derivative.ca/Art-Net "Art-Net") | [sACN](../Interoperability/SACN.md "SACN") | [FTDI](../Interoperability/DMX.md "DMX") | [KiNET](../POPs/DMX_Out_POP.md "DMX Out POP") |

###  Lasers

[EtherDream](../Interoperability/Lasers.md#EtherDream "Lasers") | [Helios](../Interoperability/Lasers.md#Helios "Lasers") | [ShowNET](../Interoperability/Lasers.md#ShowNET "Lasers") | [LaserAnimation Sollinger AVB](../Interoperability/Lasers.md#LaserAnimation_Sollinger_and_AVB_Protocol "Lasers") | [Pangolin Beyond](../Interoperability/Lasers.md#Pangolin_Beyond "Lasers") |

###  Audio

[Steinberg VST](../Interoperability/VST.md "VST") | [ASIO](../Interoperability/Audio_Device_Out_CHOP.md "Audio Device Out CHOP") | [DirectSound](../Interoperability/Audio_Device_Out_CHOP.md "Audio Device Out CHOP") | macOS Core Audio | [Dante](../Interoperability/Dante.md "Dante") | [MP3, AIFF, WAV, AAC, OPUS, Vorbis, ALAC](../Interoperability/File_Types.md#Files_Imported "File Types") + others | [LTC TimeCode](../Interoperability/LTC_In_CHOP.md "LTC In CHOP") | [Steam Audio](../Interoperability/Audio_Render_CHOP.md "Audio Render CHOP") | [WebRTC](../Interoperability/WebRTC.md "WebRTC") |

###  Digital Audio Workstations (DAWs)[")]

[Ableton Live and TDAbleton](../Interoperability/TDAbleton.md "TDAbleton") | [Ableton Link](../Interoperability/Ableton_Link_CHOP.md "Ableton Link CHOP") | [Bitwig Studio and TDBitwig](../Interoperability/Bitwig.md "Bitwig") |

###  Camera-based Tracking

[Orbbec (Femto Kinect replacement)](../Interoperability/Orbbec.md "Orbbec") | [ZED depth and body-track](../Interoperability/ZED.md "ZED") | [Kinect Azure](../TOPs/Kinect_Azure_TOP.md "Kinect Azure TOP") | [NVIDIA Face Track](../Interoperability/Face_Track_CHOP.md "Face Track CHOP") | [NVIDIA Body Track](../Interoperability/Body_Track_CHOP.md "Body Track CHOP") | [Leap Motion](../Interoperability/Leap_Motion.md "Leap Motion") | [Augmenta](https://augmenta.tech/tracking-technology/) | [Movin3D](../Interoperability/Movin3D.md "Movin3D") (**new**) | [NatNet OptiTrack](../Interoperability/NatNet_In_CHOP.md "NatNet In CHOP") | [BlackTrax](../Interoperability/BlackTrax.md "BlackTrax") | [PosiStageNet](../Interoperability/PosiStageNet_CHOP.md "PosiStageNet CHOP") | Vicon | [ZIG SIM Pro (Apple AR)](https://apps.apple.com/ca/app/zig-sim-pro/id1481556614) |

###  [LIDAR](../Interoperability/LIDAR.md "LIDAR") Scanners and Depth Cameras

[Hokuyo Scanner](../Interoperability/Hokuyo_CHOP.md "Hokuyo CHOP") | [Intel RealSense](../Interoperability/RealSense.md "RealSense") | [Ouster LIDAR](../TOPs/Ouster_TOP.md "Ouster TOP") | [SICK LIDAR](../Interoperability/SICK.md "SICK") | [Leuze ROD4](../Interoperability/Leuze_ROD4_CHOP.md "Leuze ROD4 CHOP") |

###  ML Cameras

[Luxonis OAK-D ML Camera](https://docs.derivative.ca/OAK-D "OAK-D") |

###  3D Scene Data

[FBX](../Interoperability/FBX.md "FBX") | [Alembic (**new**)](../Interoperability/Alembic.md "Alembic") | [OpenUSD](../Interoperability/USD.md "USD") |

###  Graphics Languages

[GLSL](../Interoperability/Write_a_GLSL_Material.md "Write a GLSL Material") | [Compute Shaders](../Interoperability/Compute_Shader.md "Compute Shader") | Vulkan | [CUDA](../Interoperability/CUDA.md "CUDA") | [C++ Custom Operators](../Interoperability/Custom_Operators.md "Custom Operators") |

###  Materials and Renderers

[Substance Designer](../TOPs/Substance_TOP.md "Substance TOP") | [Notch](../Interoperability/Notch.md "Notch") |

###  Virtual Reality

[OpenVR](../Interoperability/OpenVR.md "OpenVR") | [Meta Quest and Oculus Rift](../Interoperability/Meta_VR.md "Meta VR") | [Steam Audio](../Interoperability/Audio_Render_CHOP.md "Audio Render CHOP") |

###  XR Tracking

[Stype camera tracking](../Interoperability/Stype.md "Stype") | [Mosys camera tracking](../Interoperability/MoSys_CHOP.md "MoSys CHOP") | [ FreeD](../Interoperability/FreeD_CHOP.md "FreeD CHOP") |

###  Physics and Dynamics

[Bullet Rigid Body Dynamics](../Interoperability/Bullet_Dynamics.md "Bullet Dynamics") | [NVIDIA FLow](../Interoperability/Nvidia_Flow_TOP.md "Nvidia Flow TOP") | [NVIDIA Flex](../Interoperability/Nvidia_Flex_Solver_COMP.md "Nvidia Flex Solver COMP") |

###  Network Protocols

[OSC](../Interoperability/OSC_In_CHOP.md "OSC In CHOP") | [TCP/IP](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT") | [UDP](../Interoperability/UDP_In_DAT.md "UDP In DAT") | [WebRTC](../Interoperability/WebRTC.md "WebRTC") |

###  Web Browser and Web Tools

[Embedded Chromium/CEF Renderer and Browser](../Interoperability/Palette_webBrowser.md "Palette:webBrowser") | [WebSockets](../Interoperability/WebSocket_DAT.md "WebSocket DAT") | [Socketio](../Interoperability/SocketIO_DAT.md "SocketIO DAT") | [Web Server](../Interoperability/Web_Server_DAT.md "Web Server DAT")/[Web Client](../Interoperability/Web_Client_DAT.md "Web Client DAT") | [WebRTC](../Interoperability/WebRTC.md "WebRTC") |

###  Projection Mapping and Calibration

[MPCDI projection mapping file standard](../Interoperability/MPCDI.md "MPCDI") | [Scalable Displays](../TOPs/Scalable_Display_TOP.md "Scalable Display TOP") | [kantanMapper](../Interoperability/Palette_kantanMapper.md "Palette:kantanMapper") | [camSchnappr](../Interoperability/Palette_camSchnappr.md "Palette:camSchnappr") | [projectorBlend](../Interoperability/Palette_projectorBlend.md "Palette:projectorBlend") | [(key)Stoner](../Interoperability/Palette_stoner.md "Palette:stoner") | [Lens Distortion](../TOPs/Lens_Distort_TOP.md "Lens Distort TOP") | [Nestmap](https://nestimmersion.ca/nestmap.php) | [Vioso](../Interoperability/Vioso.md "Vioso") |

###  Unreal Engine and other Third Party TouchEngine Integrations

[Unreal Engine Plugin](https://docs.derivative.ca/TouchEngine-UE_Unreal_Engine_Plugin "TouchEngine-UE Unreal Engine Plugin") | [TouchEngine](../Interoperability/TouchEngine.md "TouchEngine") |

###  Arduino

[Arduino](../Interoperability/Arduino.md "Arduino") | [Firmata](../Interoperability/Palette_firmata.md "Palette:firmata") | [Serial Ports](../Interoperability/Serial_DAT.md "Serial DAT") |

###  Controllers

[MIDI](../Interoperability/MIDI.md "MIDI") | [Joystick](../Interoperability/Joystick_CHOP.md "Joystick CHOP") | [3Dconnexion SpaceMouse](../Interoperability/Geometry_Viewer.md#3D_SpaceMouse_Navigation_Modes "Geometry Viewer") | [ZIG SIM PRO (iPhone iPad data stream)](https://apps.apple.com/us/app/zig-sim-pro/id1481556614) |

###  Internet of Things

[MQTT IoT](../Interoperability/MQTT.md "MQTT") |

###  Python and Structured Data

[Python 3.11](Python.md "Python") | [JSON](../Interoperability/JSON.md "JSON") | [XML](../Interoperability/XML_DAT.md "XML DAT") |

###  Timecode

[Timecode](../Interoperability/Timecode.md "Timecode")

###  Multi-Touch

[Windows Multi-Touch](../Interoperability/Multi_Touch_In_DAT.md "Multi Touch In DAT") | [TUIO and TUIO2](../Interoperability/TUIO.md "TUIO") | [TouchOSC](../Interoperability/TouchOSC.md "TouchOSC") | [ZIG SIM PRO (iPhone iPad multitouch)](https://apps.apple.com/us/app/zig-sim-pro/id1481556614) |

###  Image, Color, Text

[Color Space Workflows](../Interoperability/Color_Space_Workflows.md "Color Space Workflows") | [OpenColorIO](../TOPs/OpenColorIO_TOP.md "OpenColorIO TOP") | [Slug Font Rendering](../Interoperability/Slug_Library.md "Slug Library") | [live video from Photoshop](../TOPs/Photoshop_In_TOP.md "Photoshop In TOP") | SVG ( [Web Render TOP](../TOPs/Web_Render_TOP.md "Web Render TOP")) |

###  Licensing

[CodeMeter USB and Cloud Dongles](../Interoperability/License_Dongle.md "License Dongle") |
_Edited November 2025_

The devices, protocols and software tools that TouchDesigner interfaces to, via native [Operators](Operator.md "Operator") and [Palette](../Learn/Palette.md "Palette") components.

A technique or workflow that allows for displaying content on often irregular shapes and surfaces.

Display devices in TouchDesigner that support multiple-finger or control-point input.
