---
url: https://docs.derivative.ca/Splice_CHOP
category: CHOPs
title: Splice_CHOP
---

# Splice CHOP
## Summary

The Splice CHOP inserts CHOP channels connected to the second input into the channels of the first input. You can specify the start sample and length of where to remove samples.
Then the inserted data from the second input can be stretched in various ways, then spliced into the trimmed point in the channels.
You can match by channel number or channel name. Un-matched channels will have the samples in their gaps interpolate in one of three selectable ways.
To extract a sample from a CHOP, modify it and replace it at its original index, connect a Splice CHOP to the original, set Start and Trim Length where you want, turn on Output Trimmed Section, modify the result, then send that as second input to another Splice CHOP with first input from the the original CHOP, and with Start set to `op('splice1').par.start` and Trim Length set to `op('splice1').par.trimlength`.
The Splice CHOP can also smooth a section of a CHOP: Set the Start and Trim Length to that section. Give it a second input with no matching channels. Set Insert Method to Set to Trim Length, and adjust the Insert Interpolate menu.
Check [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") for these and other tricks.
See also [Delete CHOP](https://docs.derivative.ca/Delete_CHOP "Delete CHOP"), [Trim CHOP](https://docs.derivative.ca/Trim_CHOP "Trim CHOP"), [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP")
[spliceCHOP_Class](https://docs.derivative.ca/SpliceCHOP_Class "SpliceCHOP Class")

## Parameters - Splice Page
- Output Trimmed Section `outputtrimmed` - When Off the output is the spliced and trimmed channels based and on the parameters below. When On the output is the opposite and contains the trimmed out portion of the channels.
- Direction `direction` - ⊞ - Specify which direction the Start and Trim parameters below work.
  * First to Last `firsttolast` - Start and Trim are specified in units from the beginning going towards the end of the channel.
  * Last to First `lasttofirst` - Start and Trim are specified in units from the end going towards the beginning of the channel.

- Start `start` - The position the Trim and Insert operations start from. This will be from the first sample or the last sample in the channel depending on the Direction parameter above.
- Start Units `startunits` - Choose between using Samples, Frames, or Seconds as the units for this parameter.
- Trim Method `trimmethod` - ⊞ - Gives options for how to set the trim length.
  * Use Trim Length `trimlength` - Uses the Trim Length parameter below to determine how much to trim.
  * Trim to Insert Input Length `insertlength` - The length of the 2nd input is how much will be trimmed.

- Trim Length `trimlength` - The how long the trimmed region is. To output just the trimmed region, switch Output Trimmed Section to On.
- Trim Length Units `trimlengthunits` -
- Insert Method `insertmethod` - ⊞ - Handles how the 2nd input is spliced into the channel.
  * None `none` - Nothing is insert into the channel.
  * Input Length `natural` - The 2nd input is spliced in maintaining its full length. If Trim parameter = 0, then the total length of the output will be the length of both inputs combined.
  * Stretch to Trim Length `stretchtrim` - The 2nd input is stretched to fill the trimmed section. Since the inserted section is the same length as the trimmed section, the total length of the output will remain the same as the 1st input.
  * Trim to Insert Length `insertlength` - Enables the Insert Length parameter to set the length of the inserted data. See Insert Length below.
  * Stretch to Insert Length `stretchinsert` - Enables the Insert Length parameter to set the length of the inserted data and will stretch it to fit.

- Insert Length `insertlength` - Used to set the length of the inserted data based on the Insert Method above. When set to Trim to Insert Length, the inserted data will be trimmed when this parameter value is shorter than the 2nd input and cycled when it is longer. When set to Stretch to Insert Length, the inserted data is stretched to fit this parameter value.
- Insert Units `insertunits` -
- Insert Interpolate `insertinterp` - ⊞ - Choose interpolation method for stretched insert channel.
  * None `none` -
  * Linear `linear` -
  * Cubic `cubic` -

- Match by `match` - ⊞ - Match channels between inputs by name or number.
  * Channel Number `index` -
  * Channel Name `name` -

- Unmatched Chan Interpolate `unmatchedinterp` - ⊞ - Choose interpolation method for any channels that are unmatched using "Match Channels".
  * None `none` -
  * Linear `linear` -
  * Cubic `cubic` -

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
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Splice CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
