---
url: https://docs.derivative.ca/Null_CHOP
category: CHOPs
title: Null_CHOP
---

# Null CHOP
## Summary

The Null CHOP is used as a place-holder and does not alter the data coming in.
It is often used to [Export](https://docs.derivative.ca/Export "Export") channels to parameters, which allows you to experiment with the CHOPs that feed into the Null without having to un-export from one CHOP and re-export from another.
The Null CHOP also has options to force-cook nodes downstream from it, or the opposite, to stop cooking nodes downstream if its inputs are not changing.
[![NullCHOP.jpg](https://docs.derivative.ca/images/3/35/NullCHOP.jpg)](https://docs.derivative.ca/File:NullCHOP.jpg)
[nullCHOP_Class](https://docs.derivative.ca/NullCHOP_Class "NullCHOP Class")

## Parameters - Null Page
- Cook Type `cooktype` - ⊞ - This controls how nodes downstream from the Null CHOP are triggered for recooking when the Null CHOP output changes. See also: [Cook](https://docs.derivative.ca/Cook "Cook")
  * Automatic `auto` - Downstream nodes are triggered for recooking normally.
  * Always `always` - This node and dirty upstream nodes will cook every frame. Downstream nodes will recook every frame their data is requested.
  * Selective `selective` - Select which criteria will cause downstream nodes to require recooking, using the parameters below. This option can optimize your network by reducing the number of cooks downstream if the upstream CHOP has inputs that are time dependent or changes often, but output is mostly static (e.g. a Math CHOP rounding a constantly changing float to 0 or 1). The downside is that the nodes upstream of the Null will cook whenever something changes, even if no data is requested downstream. See [Cook](https://docs.derivative.ca/Cook "Cook") for more information on when data is requested.

- Check Values `checkvalues` - Recook when the Null CHOP values change.
- Check Names `checknames` - Recook when the Null CHOP channel names change.
- Check Range `checkrange` - Recook when the Null CHOP channel range changes.
Please note that downstream cooks may also cook for a variety of reasons including viewing the contents of the data while editing nodes, etc.

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
Extra Information for the Null CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
