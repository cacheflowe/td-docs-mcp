---
url: https://docs.derivative.ca/Timecode
category: Interoperability
title: Timecode
---

# Timecode

##  Timecode in TouchDesigner

Timecode is a way of expressing time as a combination of hours, minutes, seconds, and frames. It can be expressed in a string, for example `03:22:11:10`, or as a bit pattern, as in LTC timecode embedded in audio streams. The prevalent standard for timecode, SMPTE Timecode, was originally designed for video tape machines, tapes and broadcast transmissions.

In TouchDesigner we try to represent time everywhere possible as timecode, though the fundamental time units are expressed as frames on the timeline, and in seconds or frames in [Absolute Time](https://docs.derivative.ca/Absolute_Time "Absolute Time").

Timecode in TouchDesigner is represented in a `tdu.Timecode` object (see [Timecode_Class](https://docs.derivative.ca/Timecode_Class "Timecode Class")). These objects are built into some operators, or can be created as their own entities in python.

Numerous operators (see below) that deal with time in various ways have a `.timecode` member that report the timecode of the data in that operator in various formats and units.

The [Timecode CHOP](https://docs.derivative.ca/Timecode_CHOP "Timecode CHOP") contains a `.timecode` member and is an easy-to-use UI to set the current timecode of the CHOP, do some simple arithmetic with timecodes, and convert between different representations of timecode. It gets its timecode values from (1) its parameters, (2) channels coming into the CHOP, (3) other operators, or (4) expressions.

Timecode anywhere in TouchDesigner can be conformed (with limitations) into the SMPTE standard for timecode, or by un-setting a `.smpte` flag on a `.timecode` object, it can be allowed to non-conform, like go past 24 hours, express negative time, or be set to above 60 frames per second.

**Tip** : See the **OP Snippets** for the [Timecode CHOP](https://docs.derivative.ca/Timecode_CHOP "Timecode CHOP").

**Tip** : A useful hardware box for monitoring timecode: [Rosendahl Timecode](https://rosendahl-studiotechnik.com/mif4.html)

##  The `tdu.Timecode` Object

See: [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class")

##  Operators with a `.timecode` Member

  * [Timecode CHOP](https://docs.derivative.ca/Timecode_CHOP "Timecode CHOP")
  * [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP")
  * [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP")
  * [Video Device In TOP](https://docs.derivative.ca/Video_Device_In_TOP "Video Device In TOP")
  * [LTC In CHOP](https://docs.derivative.ca/LTC_In_CHOP "LTC In CHOP")
  * [LTC Out CHOP](https://docs.derivative.ca/LTC_Out_CHOP "LTC Out CHOP")
  * [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP") - has 3 members: `.timecode`, `.runningTimecode`, and `.runningLengthTimecode` – **BACKWARD COMPATIBILITY** : these used to return strings but were updated to return a `tdu.Timecode` instead. There is also `.masterTimecode`, `.playingTimecode`, `.cumulativeTimecode`.
  * [Stype In CHOP](https://docs.derivative.ca/Stype_In_CHOP "Stype In CHOP")
  * [Stype TOP](https://docs.derivative.ca/Stype_TOP "Stype TOP")
  * [Timeline CHOP](https://docs.derivative.ca/Timeline_CHOP "Timeline CHOP")
  * [Time COMP](https://docs.derivative.ca/Time_COMP "Time COMP")
  * [Sync In CHOP](https://docs.derivative.ca/Sync_In_CHOP "Sync In CHOP")
  * [Sync Out CHOP](https://docs.derivative.ca/Sync_Out_CHOP "Sync Out CHOP")
  * [DMX In CHOP](https://docs.derivative.ca/DMX_In_CHOP "DMX In CHOP")
  * [Clock CHOP](https://docs.derivative.ca/Clock_CHOP "Clock CHOP")
  * [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP")
  * [OAK-D](https://docs.derivative.ca/OAK-D "OAK-D") OPs

**Note** : Any OP with a `.timecode` member will also have a Timecode Info Type available on its [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") that provides the timecode value as a set of CHOP channels.

##  The SMPTE Timecode Standard

See:
  * <https://en.wikipedia.org/wiki/SMPTE_timecode>
  * <http://www.philrees.co.uk/articles/timecode.htm>

If the `.smpte` flag is off in any Timecode object or CHOP, you can break the standard and have time greater than 24 hours, negative time, and any number of frames per second above SMPTE's 60 limit.

##  Frames

Frames in timecode are not the same as frames on the timeline or frames in CHOPs. The timeline can be set to any integer number of frames per second, but timecode coming into or out-of TouchDesigner can have another assumption of frames per second. Typically timecode uses 24, 25, 30, 48, 50 or 60 frames per second, or 29.97 frames per second, implementing what is called "drop frames" in the video industry.

##  Drop Frame

See: <https://sonix.ai/resources/what-is-drop-frame-vs-non-drop-frame-timecode/>

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

[OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") is a set of 700+ live examples of TouchDesigner operators. You can access snippets via the Help menu, or by right-clicking on network operators, or r-clicking on OP Create dialog items.

The sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Component](https://docs.derivative.ca/Component "Component") types that are used to define and render 3D scenes. A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

The term "Frame" is a measurement of time used (1) in the [Timeline](https://docs.derivative.ca/Timeline "Timeline"), (2) as a time-unit in CHOPs, and (3) as a time unit in movie files that are read into [TOPs](https://docs.derivative.ca/TOP "TOP") and written out from TOPs. The frame rate is the frames per second ([FPS](https://docs.derivative.ca/index.php?title=FPS&action=edit&redlink=1 "FPS \(page does not exist\)")).
