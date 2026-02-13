---
url: https://docs.derivative.ca/Helios_DAC_CHOP
category: CHOPs
title: Helios_DAC_CHOP
---

# Helios DAC CHOP
## Summary

**DEPRECATED:** use the [Laser Device CHOP](https://docs.derivative.ca/Laser_Device_CHOP "Laser Device CHOP") instead.
Helios DAC is a laser controller. The Helios DAC CHOP takes as input up to five channels interpreted as X and Y (horizontal and vertical) position values in the first 2 channels, and red, green and blue color values in the next 3 channels. It outputs the data to a [Helios DAC](https://bitlasers.com/helios-laser-dac/). The Helios DAC device is connected to a laser using an ILDA cable. The user can then control the image that the laser should output using the Helios DAC CHOP. Applications of the Helios DAC CHOP include displaying computer-generated shape animations or other special effects of a light show.
Blanking (all-off) occurs when the incoming RGB CHOP channels are all zero, or the Red Scale, Green Scale, and Blue Scale parameters are all zero.
Large changes in RGB values from sample-to-sample will likely be visibly correct as lasers generally can switch on-off quickly.
The range of X and Y is typically -1 to +1, and the range of RGB is typically 0 to 1.
**Note:** The Helios DAC CHOP listens for any device changes on the system and will perform a Helios device re-scan when triggered. However, the re-scan can only be triggered if all Helios connections are closed, meaning all Helios DAC CHOPs are either deactivated or bypassed. To perform a Helios device re-scan with only a single Helios DAC CHOP, simply deactivate and reactivate the CHOP.
See also: [EtherDream CHOP](https://docs.derivative.ca/EtherDream_CHOP "EtherDream CHOP"), [EtherDream DAT](https://docs.derivative.ca/EtherDream_DAT "EtherDream DAT"), [Laser CHOP](https://docs.derivative.ca/Laser_CHOP "Laser CHOP"), and the [Pattern CHOP](https://docs.derivative.ca/Pattern_CHOP "Pattern CHOP").
[heliosdacCHOP_Class](https://docs.derivative.ca/HeliosdacCHOP_Class "HeliosdacCHOP Class")

## Parameters - Helios DAC Page
- Active `active` - If turned off, the Helios DAC CHOP will stop sending data to the Helios DAC and will immediately clear its point buffer. Consider it equivalent to powering off the Helios DAC.
- Device `device` - Select the Helios DAC you want to control from this menu.
- Queue Time (Seconds) `queuetime` - Determines the queue size of the Helios DAC CHOP point buffer and the corresponding time required to drain it. It is often useful to reduce this value when sending fewer points.
- X Scale `xscale` - Allows the input x values to be scaled by the specified factor.
- Y Scale `yscale` - Allows the input y values to be scaled by the specified factor.
- Red Scale `redscale` - Allows the input r values to be scaled by the specified factor.
- Green Scale `greenscale` - Allows the input g values to be scaled by the specified factor.
- Blue Scale `bluescale` - Allows the input b values to be scaled by the specified factor.
- Intensity Scale `intensityscale` - Allows the input intensity values (i) to be scaled by the specified factor.

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
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Helios DAC CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Helios DAC CHOP Info Channels
  * heliosdac_queue_seconds -

  * heliosdac_points_dropped -

  * heliosdac_queue_adjusted -

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
