---
url: https://docs.derivative.ca/Initialize_Start
category: Learn
title: Initialize_Start
---

# Initialize Start
Initialize Start is an approach in TouchDesigner to prepare and run timed processes. It applies to any system in TouchDesigner where there first needs be an initialization (the "`initializing`" state), like reading files into memory, querying servers, pre-simulating dynamics or starting external processes. When initializing is complete, it goes into the "`ready`" state. Then it is signaled to start via a "Start" pulse parameter. For example, before starting a show, you may want to initialize all your generative components at their first frame.
Upon Start, it goes into the "`running`" state, and when complete (when timer reaches its length and it's not looping, or when Go to Done is pulsed) it goes into a "`done`" state.
The `ready` state has to be fully-primed and ready-to-go such that when Start is pressed, the first frame is perfectly valid and suffers no frame drops or delays.
Initialization often takes more than one frame to complete, so there is usually provision to initialize over several frames without substantially stalling TouchDesigner. The `initializing` state may last several frames.
Note: The convention is, if you press Start when it is already `running` or when it is `done`, it is equivalent to going to done, pressing Initialize and then starting. That is, the Initialize stage automatially goes to completion before it starts again.
Initialize Start is based on the [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP").
Examples of parts of TouchDesigner where the Initialize Start approach is used are:
  * [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP")
  * [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP")
  * [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP")
  * [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP")
  * [Nvidia Flow TOP](https://docs.derivative.ca/Nvidia_Flow_TOP "Nvidia Flow TOP"), [Nvidia Flex TOP](https://docs.derivative.ca/Nvidia_Flex_TOP "Nvidia Flex TOP")
  * [Notch TOP](https://docs.derivative.ca/Notch_TOP "Notch TOP")
  * [Animation COMP](https://docs.derivative.ca/Animation_COMP "Animation COMP")
  * [Palette:moviePlayer](https://docs.derivative.ca/Palette:moviePlayer "Palette:moviePlayer") COMP in Palette
  * ( [Palette:particlesGpu](https://docs.derivative.ca/Palette:particlesGpu "Palette:particlesGpu") COMP in Palette )
  * [Engine COMP](https://docs.derivative.ca/Engine_COMP "Engine COMP")
  * [Feedback POP](https://docs.derivative.ca/Feedback_POP "Feedback POP")
  * [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP")

There is a component in the palette called [initalizeStart](https://docs.derivative.ca/Palette:initializeStart "Palette:initializeStart") that you can use to convert any of your components to use the same mechanism.
Initialize Start follows the model of the [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP").
See also [Event](https://docs.derivative.ca/Event "Event").

###  Control Parameters
  * Initialize (pulse) - prepares all data, in `initializing` state
  * Start (pulse) - starts all the timers, puts in `running` state
  * Play (toggle) - used to pause while playing
  * Speed (float) - speed or slows the timer or simulation clock while running.
  * Cue (toggle), Cue Pulse (pulse), Cue Point (float with menu % index, frames, seconds) - allows you to put/scrub system at specified time
  * Length (float) - if behavior is fixed-length, length is sometimes pre-determined like a movie file, sometimes user-set.
  * Pre-Roll (float) - if behavior is a procedural simulation, at initialization, it may run the sim a few seconds to get it going.
  * Initialize Time (float) - for fixed-length systems, where implemented, this initializes part-way into its internal timeline.
  * Go to Done (pulse) - stops all the timers, possibly goes to an end-state, puts in `done` state.

###  Info Channels
This is often achieved by attaching an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") to the operator. It is the actual output in the Timer CHOP and the [initializeStart](https://docs.derivative.ca/Palette:initializeStart "Palette:initializeStart") palette COMP.
States -
  * `initializing` (0 if operator currently initializes in the same-frame)
  * `ready` (after Initialize complete and before Start pressed)
  * `running` goes on after Start, stays on until Done or Initialize
  * `done` where applicable

Counters - used to drive animations, index lookups, etc.
  * `timer_fraction` (where applicable) For fixed-length setups, it is `timer_seconds` / `length_seconds`. (For infinite length setups or length is not known, it is set to 0.)
  * `timer_seconds` (seconds) It is affected by Speed and Play. If the length is known and you loop, your `timer_seconds` goes back to 0. It’s really your calculated index / (end - start) / (file_sample_rate)
  * `timer_frames` (where available - number of frames based on the timeline frames per second.)
  * `cumulative_seconds` (seconds) counts from 0 when you Start. It is slowed down and sped up by the Speed parameter, and paused by the Play parameter. It continues to increase if there is any looping, jumping or scrubbing around.
  * `master_seconds` (seconds) - counts time from 0 when you Start, it is slowed down and sped up by the Speed parameter, and is paused by the Play parameter. This is the main clock. (It will jumps to the appropriate time if there is provision for scrubbing or jumping.)
  * `running_seconds` (seconds) - It keeps counting up after Start and is not affected by changing the Speed or pausing Play or scrubbing. It is basically the "wall clock" after pressing Start. It stops when you Go to Done. It doesn't reset to 0 until you Initialize or Start again.
  * `playing_seconds` (seconds) - counts from 0 when you Start, is like `running_seconds` but it is paused when Play pauses.
  * `length_seconds` for operators with known length
  * ``cycles`` (where applicable)

###  Behavior
Fixed-length vs infinite (unknown) length. An example of infinite length would be a particle simulation. There are two flavors of fixed-length - user-specified length or media-determined length (like an audio file).
###  Callbacks
In some cases, like the [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP"), there are callbacks where you can run python code when events occur, such as the end of initialization, or the end of a fixed-length behavior. The common ones are:
  * `onInitialize()` called when the Initialize is pulsed, and is called every frame thereafter until you return 0, in order for multi-frame initializations to occur.
  * `onReady()` is called when initialization is complete.
  * `onStart()` is called when Start is pressed.
  * `onDone()` is called when fixed-length systems complete, and when Go to Done is pulsed.

###  Errors and Warnings
In some cases, the operator reports errors or warnings, like failure to initialize.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.
To "pulse" a parameter is to send it a signal from (1) an [exported](https://docs.derivative.ca/Export "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately. A pulse via python is via the `.pulse()` function on a pulse-type parameter, such as Reset parameter in a [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP"). A pulse from a CHOP is typically a 0 to 1 to 0 signal in an exported channel.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
