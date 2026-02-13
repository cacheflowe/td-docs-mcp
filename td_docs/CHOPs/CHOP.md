---
url: https://docs.derivative.ca/CHOP
category: CHOPs
title: CHOP
---

# CHOP

## Summary

[![OP CHOP.png](https://docs.derivative.ca/images/e/e9/OP_CHOP.png)](https://docs.derivative.ca/File:OP_CHOP.png)
**CHOPs** , or **CHannel OPerators** , are a powerful technology which enables the processing of motion, audio, math, logic, MIDI data, numeric info and data streamed from/to devices and protocols.
CHOPs are an [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))).
CHOPs provide a unique way of creating and editing motion and audio. The combination of procedural editing of motion, keyframe animation, motion capture and live controls provides you with a wide range of animation techniques. In keeping with the TouchDesigner procedural paradigm, channel operators combine and refine the data without destroying the original data. CHOPs were designed to reduce the tedium of motion editing and to help build and manage more complex motion. CHOPs enable creators to think about motion at a more creative level and to experiment with motion more than any other animation technology.
A CHOP contains one or more named **channels**. The channels of a CHOP is made of a sequence of one or more "**samples** ". A sample is one floating point number per channel.
A CHOP has a **sample rate** , which is the number samples-per-second, which matters only when a CHOP represents animation or audio over time.
The length of a CHOP is expressed in samples, and when the CHOP represents animation or audio, the length can also be expressed in seconds or frames. A frame is a unit of time of the timeline, typically 1/60 of a second.
A CHOP creates or modifies the [Channel](https://docs.derivative.ca/Channel "Channel"), and then passes the channels on to the next CHOP in a network. CHOPs are then connected to object motion or any other animated part of TouchDesigner via "[exporting](https://docs.derivative.ca/Export "Export")" and "channel references".
See also [Category:CHOPs](https://docs.derivative.ca/Category:CHOPs "Category:CHOPs") for a full list of articles related to CHOPs, especially [Anatomy of a CHOP](https://docs.derivative.ca/Anatomy_of_a_CHOP "Anatomy of a CHOP") and [Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing").
[CHOP Class](https://docs.derivative.ca/CHOP_Class "CHOP Class")

##  Sweet 16 CHOPs
[![Sweet 16 CHOPs.jpg](https://docs.derivative.ca/images/thumb/4/4f/Sweet_16_CHOPs.jpg/200px-Sweet_16_CHOPs.jpg)](https://docs.derivative.ca/Sweet_16_CHOPs_Vid "Sweet 16 CHOPs Vid")
Click the [video](https://docs.derivative.ca/Sweet_16_CHOPs_Vid "Sweet 16 CHOPs Vid") above to watch an overview of all Sweet 16 CHOPs. Watch individual CHOP videos by clicking on the appropriate CHOP's video icon below. The following 16 CHOPs are commonly used, we recommend familiarizing yourself with them.
CHOP | Purpose | Related CHOP
---|---|---
[Constant](https://docs.derivative.ca/Constant_CHOP "Constant CHOP") | Create new channels. |  [Pattern](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP")
[LFO](https://docs.derivative.ca/LFO_CHOP "LFO CHOP") | Low Frequency Oscillator. |  [Audio Oscillator](https://docs.derivative.ca/Audio_Oscillator_CHOP "Audio Oscillator CHOP")
[Noise](https://docs.derivative.ca/Noise_CHOP "Noise CHOP") | Create semi-random patterns. |
[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP") | Grab a channel from any other CHOP. |  [Switch](https://docs.derivative.ca/Switch_CHOP "Switch CHOP"), [Cross](https://docs.derivative.ca/Cross_CHOP "Cross CHOP")
[Merge](https://docs.derivative.ca/Merge_CHOP "Merge CHOP") | Merge channels from two or more CHOPs. |  [Shuffle](https://docs.derivative.ca/Shuffle_CHOP "Shuffle CHOP")
[Math](https://docs.derivative.ca/Math_CHOP "Math CHOP") | Add, multiply or scale channels. |  [Logic](https://docs.derivative.ca/Logic_CHOP "Logic CHOP"), [Script](https://docs.derivative.ca/Script_CHOP "Script CHOP")
[Lag](https://docs.derivative.ca/Lag_CHOP "Lag CHOP") | Smooth and delay a channel. |  [Filter](https://docs.derivative.ca/Filter_CHOP "Filter CHOP")
[Speed](https://docs.derivative.ca/Speed_CHOP "Speed CHOP") | Use speed to calculate distance. |  [Count](https://docs.derivative.ca/Count_CHOP "Count CHOP"), [Slope](https://docs.derivative.ca/Slope_CHOP "Slope CHOP")
[Lookup](https://docs.derivative.ca/Lookup_CHOP "Lookup CHOP") | Use one channel to get values from another CHOP. |  [Keyframe](https://docs.derivative.ca/Keyframe_CHOP "Keyframe CHOP")
[Trail](https://docs.derivative.ca/Trail_CHOP "Trail CHOP") | Watch a time-history of CHOP channels. |  [Perform](https://docs.derivative.ca/Perform_CHOP "Perform CHOP")
[SOP to](https://docs.derivative.ca/SOP_to_CHOP "SOP to CHOP") | Record a time-history of channels. |  [DAT to](https://docs.derivative.ca/DAT_to_CHOP "DAT to CHOP"), [TOP to](https://docs.derivative.ca/TOP_to_CHOP "TOP to CHOP")
[Limit](https://docs.derivative.ca/Limit_CHOP "Limit CHOP") | Restrict channels to a range or certain step values. |  [Analyze](https://docs.derivative.ca/Analyze_CHOP "Analyze CHOP")
[Audio Device In](https://docs.derivative.ca/Audio_Device_In_CHOP "Audio Device In CHOP") | Get audio from input device. |  [Audio File In](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP")
[OSC In](https://docs.derivative.ca/OSC_In_CHOP "OSC In CHOP") | Open Sound Control, MIDI. |  [MIDI In Map](https://docs.derivative.ca/MIDI_In_Map_CHOP "MIDI In Map CHOP")
[Panel](https://docs.derivative.ca/Panel_CHOP "Panel CHOP") | Get state, u, v etc values from any panel gadget. |  [Info](https://docs.derivative.ca/Info_CHOP "Info CHOP")
[Timer](https://docs.derivative.ca/Timer_CHOP "Timer CHOP") | Run timers, loops, delays and trigger events. |  [Beat](https://docs.derivative.ca/Beat_CHOP "Beat CHOP")
All CHOPs are documented in the [Category:CHOPs](https://docs.derivative.ca/Category:CHOPs "Category:CHOPs").
##  CHOPs Create and Process Channels
CHOPs are procedural networks, where "procedural" means the operators are wired together so the output of one CHOP flows into the input of one or more other CHOPs, and the data flows automatically every time the display is updated (by default, 60 times per second).
Some CHOPs, generator CHOPs, create CHOP channels from scratch. Some examples are the Constant CHOP, the Wave CHOP, and the Timing CHOP. CHOPs can also take data from
  * on-screen sliders, buttons, menus, XY-controllers, XYZ values from clicking in 3D viewers.
  * hardware devices including data via MIDI and OSC protocols.
  * other processes/applications feeding TouchDesigner through pipes.

CHOPs process channel data and connect the results to any other part of TouchDesigner.

##  Parts of a CHOP
[![CHOP.1.png](https://docs.derivative.ca/images/thumb/e/e5/CHOP.1.png/800px-CHOP.1.png)](https://docs.derivative.ca/File:CHOP.1.png)
A CHOP contains a set of **Channels** , plus control **[Parameters](https://docs.derivative.ca/index.php?title=Parameters&action=edit&redlink=1 "Parameters \(page does not exist\)")** , a **sample rate** , some on/off **[Flags](https://docs.derivative.ca/index.php?title=Flags&action=edit&redlink=1 "Flags \(page does not exist\)")** , and a **start/end interval**.
The channels of a CHOP can represent motion, MIDI, audio, color maps, rolloff curves or lookup tables. Any data that can be represented as a sequence of numbers can be represent in CHOP channels. The sequence of numbers are called **samples**.
Like all [Operators](https://docs.derivative.ca/Operator "Operator"), CHOPs have **[Parameters](https://docs.derivative.ca/index.php?title=Parameters&action=edit&redlink=1 "Parameters \(page does not exist\)")** used to define the data, plus the data channels, which are input/output from the CHOP as its data stream. The parameters are usually constant-valued, but can be time-dependent expressions.
CHOPs' parameters can be expressed in different CHOP **units** : samples (indexes), frames or seconds. These units are selected by the user in a menu to the right of such parameters. Each sample index, starting from 0, corresponds to some frame number (based on frames per second), and a moment in time (seconds).
[![CHOP Units menu](https://docs.derivative.ca/images/3/3d/CHOPUnits.jpg)](https://docs.derivative.ca/File:CHOPUnits.jpg "CHOP Units menu")
The **sample rate** (samples per second) is used if the CHOP contains time-dependent motion or audio data. Audio has a high sample rate when compared to animated motion.
Each CHOP has **flags** :
  * The Display flag marks the CHOP to be displayed in a [CHOP Viewer](https://docs.derivative.ca/CHOP_Viewer "CHOP Viewer").
  * The Export flag causes the CHOP channel [exports](https://docs.derivative.ca/Export "Export") to toggle on and off.
  * The Lock flag causes the CHOP to be locked and then can be hand-edited.
  * The [Bypass Flag](https://docs.derivative.ca/Bypass_Flag "Bypass Flag") is a convenient way for a CHOP's effect to be disabled.

CHOPs can have any start/end indexes but all channels in a single CHOP share the same **start-end interval**. The interval goes from a start index to an end index and is not restricted to the length of any animation or timeline.
Each CHOP also has a **comment field** to add a note to a CHOP to explain what it is doing in the network. An **info pop-up** can be opened by middle-clicking on the CHOP, this lists channel names and values, sample rate and intervals.
In CHOPs, **Extend Conditions** determine what numbers you get when you try to get a channel value that is outside its start-end range - in its **Extend Regions** , before the CHOP's start time or after its end time. The CHOP may hold its last value, it may cycle, repeat, or be held at a default value. You can see a CHOP's extend conditions in the info pop-up (middle-mouse click on the CHOP), or by looking at a CHOP in the channel viewer outside its start-end range. You will see that a [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP") cycles and a [Keyframe CHOP](https://docs.derivative.ca/Keyframe_CHOP "Keyframe CHOP") holds in the Extend Regions.
You can change the Extend Conditions with an [Extend CHOP](https://docs.derivative.ca/Extend_CHOP "Extend CHOP") or via menus on the Channel page in many CHOPs.
See also [Anatomy of a CHOP](https://docs.derivative.ca/Anatomy_of_a_CHOP "Anatomy of a CHOP").
##  Inputs and Outputs
Each CHOP receives channels at its inputs. When the CHOP [cooks](https://docs.derivative.ca/Cook "Cook"), the channels of the inputs are combined. The CHOP outputs the resulting channels to other CHOPs.
CHOPs output their data channels as arrays of numbers, not keyframed, interpolated segments. Some CHOPs ([Keyframe CHOP](https://docs.derivative.ca/Keyframe_CHOP "Keyframe CHOP")) retain interpolated segments internally, but all CHOPs always output their data as raw samples. If the CHOP's inputs are not changing and the control parameters are not time-dependent, the CHOP will be non-time-dependent and it will not cook every time the animation frame on the timeline advances.
Some CHOPs output or use CHOP **attributes** , such as channels grouped as quaternion rotation channels.

##  Referencing and Exporting CHOP Channels     _Main article:[Export](https://docs.derivative.ca/Export "Export")_
Parameters of any node are able to get values from CHOP channels with expressions like the following:
```
op('filter1')[0]
op('filter1')['chan2']
op('pattern1')['chan1'][99]    # gets the 100th sample of chan1

```

However, exporting is preferred where possible. It is faster and involves less typing.
CHOP data channels are exported to Components, SOPs, etc. to drive their parameters. CHOPs can be exported to any TouchDesigner operator's parameter. Each CHOP has an Export flag (and an Export Prefix, infrequently used), causing the CHOP to connect its channels to Components, SOPs, TOPs and so on. The Export flag and Export Prefix can also use automatic matching of channels names to find export destinations. For example, a CHOP "tx" channel could map to an Geometry Component's tx parameter. When a CHOP exports to an object, SOP or TOP, the parameters exported to are said to be overridden.

##  Difference Between a Sample and a Frame
A frame always refers to the timeline, which is expressed in frames or seconds, and frames & seconds are tied via a certain number of "frames per second" or FPS. The default FPS for TouchDesigner is 60, and with FPS of 60, there will always be 60 frames per second. A CHOP range can start at any frame number (or second), and end at any later frame number. A frame will always correspond to a certain time expressed in seconds. Precisely, seconds is `(frame-1)/FPS`.
The sample index may have no relation to time or frame, as when a CHOP is used as lookup table. But when "index" is tied to time, the CHOP's samples per second (sample rate), determines how many samples per second there are, and even how many samples per frame. Some CHOPs default to 60 samples per second, which is 1 sample per frame. But CHOPs can be created or resampled to any sample rate, so a CHOP's sample rate of 240 samples per second gives 4 samples per frame, and audio at 24,000 samples per second is 400 samples per frame.
Even if a CHOP is shifted in time to start at a frame number like 301 (10 seconds), its sample index always starts at 0. Its `op('wave1').sampleIndex` is 0 at its first sample.
**NOTE** : Set the "frames per second" of the timeline for the project via the bottom of the timeline, or in Python `project.cookRate = 120`, for example. It is better to DO IT AT THE START OF A PROJECT, lest you get tripped up. Note each component can have its own timeline and its own sample rate. See [Timeline](https://docs.derivative.ca/Timeline "Timeline").
##  Sample Index and Value
[![ChannelsInfo2.gif](https://docs.derivative.ca/images/2/2b/ChannelsInfo2.gif)](https://docs.derivative.ca/File:ChannelsInfo2.gif)
  * The horizontal axis is called the i-axis or the sample index-axis.
  * The vertical axis is called the v-axis or the value-axis.
  * A sample index is a point along the i-axis, denoted by i.
  * A value is a point along the v-axis, denoted by v.
  * A sample is an index-value pair (i,v). i.e. the value of a channel at a certain sample index.
  * A sample is made of a sample index and a sample value.
  * An interval is an index range, which goes from a start index to an end index.
  * A value range goes from a start value to an end value.
  * The index duration is the end index minus the start index + 1.
  * CHOP data channels are arrays of raw samples, in 32-bit floating point format, all computations are done at 64 bits, and parameters are stored as 64 bits.
  * Channels in a CHOP may be control (parameter) channels or data channels. CHOPs manipulate the data channels.
  * CHOPs can be evaluated at integer and non-integer indexes.
  * Frame is used when the index corresponds to time.
  * When speaking of animation frames, you can refer to start frame, end frame and frame range.

##  Using `.chanIndex` in CHOP Parameters
A "Channel Index" is the channel number of a CHOP, 0 being the first channel, and is available for use in parameters in some CHOPs as `me.chanIndex`. Numerous CHOPs like the [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP"), [Math CHOP](https://docs.derivative.ca/Math_CHOP "Math CHOP") and [Delay CHOP](https://docs.derivative.ca/Delay_CHOP "Delay CHOP") have extra local members that allow the customization of each channel: The Python object for the operator has a `.chanIndex` member. For example, if the Pattern CHOP generates three channels you can put something like `[3, 4, 5][me.chanIndex]` in the Amplitude parameter to customize its value for each channel. The first channel will be evaluated with an Amplitude value 3, the second channel with a value of 5, etc. Search `me.chanIndex` in the wiki. See also the Scope parameter on most CHOPs to affect selective channels.
##  Common CHOP Members
There are Python members of a CHOP that are common to many or all CHOPs. See [CHOP Class](https://docs.derivative.ca/CHOP_Class "CHOP Class") and [Channel Class](https://docs.derivative.ca/Channel_Class "Channel Class").

##  See Also
Introduction to CHOPs | [Uses of CHOPs](https://docs.derivative.ca/Uses_of_CHOPs "Uses of CHOPs") |  [Exporting from CHOPs to Parameters](https://docs.derivative.ca/Export "Export")
---|---|---
[Common page of all CHOPs](https://docs.derivative.ca/CHOP_Common_Page "CHOP Common Page") | [Channel page of CHOPs](https://docs.derivative.ca/CHOP_Channel_Page "CHOP Channel Page") |  [Other Frequent Parameters](https://docs.derivative.ca/Edit_Keyframes "Edit Keyframes")
[The Idea of Time Slicing](https://docs.derivative.ca/Time_Slicing "Time Slicing") | [Exporting Channels](https://docs.derivative.ca/Export "Export") |  [CHOP Operator Variables](https://docs.derivative.ca/Variables "Variables")
[CHOP File Formats](https://docs.derivative.ca/File_Types "File Types") | [Tscript Expressions](https://docs.derivative.ca/Expression "Expression") |  [Category:MIDI](https://docs.derivative.ca/index.php?title=Category:MIDI&action=edit&redlink=1 "Category:MIDI \(page does not exist\)") and [OSC](https://docs.derivative.ca/OSC "OSC")
[Manually Editing Key Frames](https://docs.derivative.ca/Edit_Keyframes "Edit Keyframes") | [CHOP Techniques](https://docs.derivative.ca/CHOP_Techniques "CHOP Techniques") |  [Working with Audio](https://docs.derivative.ca/index.php?title=Category:Audio&action=edit&redlink=1 "Category:Audio \(page does not exist\)")
