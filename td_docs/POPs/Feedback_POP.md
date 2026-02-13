---
url: https://docs.derivative.ca/Feedback_POP
category: POPs
title: Feedback_POP
---

# Feedback POP
## Summary

The Feedback POP receives the output of another POP called the “target” POP, from the previous frame, i.e. delayed by one cook cycle, and passes it down a chain of operators back to the target POP. This allows existing POP data to be incrementally modified frame after frame.
When you Initialize, it snapshots the connected input which is considered its initial state, and holds that until you click Start. (Pressing Start without pressing Initialize snapshots and starts right away.) However if Pre-Roll is greater than 0, pressing Initialize will run the loop for that number of seconds and then put it in a "ready" state waiting for a Start.
Attach an Info CHOP and look at its `initializing`, `ready`, `running` and `done` channels as well as some timer counter channels (`timer_seconds` ....
Turning the Play parameter off pauses the looping, and clicking Go To Done ends the feedback loop awaiting an Initialize. Both actions stop nodes along the chain from further cooking.
See also the [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP"), which is an extension of the Feedback POP. See also the [Trail POP](https://docs.derivative.ca/Trail_POP "Trail POP") and the [Cache POP](https://docs.derivative.ca/Cache_POP "Cache POP") which capture, hold and manipulate past POP data in other ways.
[feedbackPOP_Class](https://docs.derivative.ca/FeedbackPOP_Class "FeedbackPOP Class")

## Parameters - Feedback Page
- Target POP `targetpop` - A reference to a POP node downstream in the network whose data is retrieved one frame later.
- Initialize `initializepulse` - Initializes the POP from its input and parameters, it indicates it’s ready by turning on the ready channel in an attached Info CHOP, awaiting a Start pulse.
- Start `startpulse` - Start playback.
- Play `play` - ⊞ - Pause or play the feedback loop.
  * Play `play` -
  * Step Pulse `steppulse` - Steps one frame only.

- Pre-Roll `preroll` - ⊞ - Run the loop for this time before it is ready during initialization..
  * Pre-Roll `preroll` -
  * Pre-Roll Unit `prerollunit` - Warm-up stage time units.

- Go to Done `donepulse` - Will immediately go to the done state.
- Use Memory Limit `usememlimit` - Enable a memory limit on the target POP data that can be copied back.
- Input Multiplier `inputmul` - Limits the GPU memory usage of this POP to a multiplier of the input GPU memory usage.
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Feedback POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
###
## Common Operator Info Channels
  * total_cooks - Number of times the operator has cooked since the process started.

  * cook_time - Duration of the last cook in milliseconds.

  * cook_frame - Frame number when this operator was last cooked relative to the component timeline.

  * cook_abs_frame - Frame number when this operator was last cooked relative to the absolute time.

  * cook_start_time - Time in milliseconds at which the operator started cooking in the frame it was cooked.

  * cook_end_time - Time in milliseconds at which the operator finished cooking in the frame it was cooked.

  * cooked_this_frame - 1 if operator was cooked this frame.

  * warnings - Number of warnings in this operator if any.

  * errors - Number of errors in this operator if any.
