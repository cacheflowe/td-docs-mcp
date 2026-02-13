---
url: https://docs.derivative.ca/Phaser_CHOP
category: CHOPs
title: Phaser_CHOP
---

# Phaser CHOP
## Summary

The Phaser CHOP does staggered (time-offset) animation interpolation. Phaser outputs one channel with multi-samples. Each sample animates from 0 to 1 over a cycle, but each sample value rises from 0 and arrives at 1 at different times.
For example, you may have a set of N objects that you want to animate from a start position to an end position. You set Num Samples to N, which will make the Phaser CHOP output one channel with N samples that will animate the samples from 0 to 1 and be interpolated with an easing function. In the Phaser CHOP the start-to-end cycle is controlled by the first input of the CHOP, which is expected to be one channel with value between 0 to 1.
The 0-1 values can be used with the [Lookup CHOP](https://docs.derivative.ca/Lookup_CHOP "Lookup CHOP") to animate groups of channels.
By default the timing is staggered uniformly. If you want to stagger their transitions irregularly, you use the second input, a set of values in one CHOP channel (typically N samples) that are between 0 and 1. The phase value specifies the object's timing relationship with the rest of those in the CHOP. A phase value of 1 corresponds to an animated object thats "ahead of the pack" (ie. it will start animating before the others). A value of 0 corresponds to an object that is late (ie. it will be the last to start easing/animating). If a phase input is not provided then the phase will simply be i/N where N is the total number of objects (ie. samples), and i is the index of the current sample.
There is also a notion of an "Edge" in the Phaser, which describes the cohesiveness of the group of animated objects and how fast the samples rise. A small value will cause the objects to go through the animation very quickly or at high value, very slowly and in unison with other samples.
Look at David Braun's **[TouchDesigner Summit Talk](https://www.youtube.com/watch?v=S4PQW4f34c8)** to see the background of the Phaser CHOP. Its functionality draws heavily from David's research and development in quantitative easing.
See also the [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets").
[phaserCHOP_Class](https://docs.derivative.ca/PhaserCHOP_Class "PhaserCHOP Class")

## Parameters - Phaser Page
- Edge `edge` - The separation edge of the phasing between two states. A smaller edge corresponds to sharper separation according to differences in phase. Edge Parameter will not be used if there is an Edge Input.
- Num Samples `nsamples` - Specify the size of the output. This parameter will not be used if there is a phase input.
- Output Format `outputformat` - ⊞ - Specifies the format of the output.
  * Multi-Samples `samples` - Multiple samples in a channel.
  * Multi-Channel `channels` - Multiple channels.

- Extend Input `extend` - ⊞ - Specifies how the time input is interpreted to calculate the phaser value, if the time input is outside the 0-1 range.
  * Clamp `clamp` - Time input clamped to 0-1 range.
  * Cycle `cycle` - The phaser cycles the input time 0-1.
  * Mirror `mirror` - The phaser Zig-Zags the input time between 0-1.
  * Mirror Slope `mirrorslope` - The phaser Zig-Zags the input time between 0-1, with the slope of the phaser flipped.
  * Add `add` - The phaser values keep on increasing (or decreasing) when the time input goes over 1 (or below 0).

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0: Time - The timing of the phase. When not wired the timing will default to an LFO ramp over 4 seconds. The CHOP should only contain one channel; all other channels except the first will be ignored.
  * Input 1: Phase - When wired the Phaser CHOP's output will mirror the phase input's. However, if Mult-Channel Output Format is selected it will in effect transpose the output.
  * Input 2: Edge - Edge samples will be used instead of the Edge parameter.

## Info CHOP Channels
Extra Information for the Phaser CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

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
