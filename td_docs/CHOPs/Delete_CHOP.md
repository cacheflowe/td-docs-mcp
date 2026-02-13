---
url: https://docs.derivative.ca/Delete_CHOP
category: CHOPs
title: Delete_CHOP
---

# Delete CHOP
## Summary

The Delete CHOP removes entire channels and/or individual samples of its input.
For deleting channels, on the Channels page, you can specify which channels to delete by channel name or a channel number range. A second method deletes channels using a value range to select channels whose values are all within a range. The third method deletes constant-valued channels. An option selects whether to delete or retain the matched channels.
For deleting individual samples (i.e. no channels are deleted), on the Samples page you can delete, for example, only the samples whose value is below 0, which will shorten the length of the CHOP.
In CHOPs with two or more channels, one or more "compare" channels are used to determine which samples are to be deleted. By default it uses the first channel to compare against. Deleting a sample at a certain index deletes a value for all the channels. If there are 4 channels, `red`, `green`, `blue`, `alpha` and you specify `alpha` as the "compare" channel, you can delete all the samples with an `alpha` of `0`. If a CHOP is 3 channels with an X,Y,Z position, you can delete all samples where the XYZ length is below a threshold.
This is useful, for example, for thinning your data before sending a CHOP to a Geometry component for instancing.
When all the samples are deleted, the CHOP will keep one sample for all channels and will have a `length` of one sample. When this happens, if you have an Info CHOP attached to the Delete CHOP, it's
See also [Splice CHOP](https://docs.derivative.ca/Splice_CHOP "Splice CHOP"), [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP"), [Trim CHOP](https://docs.derivative.ca/Trim_CHOP "Trim CHOP")
[deleteCHOP_Class](https://docs.derivative.ca/DeleteCHOP_Class "DeleteCHOP Class")

## Parameters - Channels Page
- Delete Channels `delchannels` - Toggle to enable channel deleting.
- Delete `discard` - ⊞ - Determines whether the scoped channels should be deleted or retained:
  * Scoped Channels `scoped` - The scoped channels are deleted. The rest are output.
  * Non-scoped Channels `nonscoped` - The scoped channels are output. The rest are deleted.

- Select Channels `select` - ⊞ - How to select channels - By Name, or By Numeric index.
  * By Channel Name `byname` -
  * By Channel Number `bynum` -

- Channel Names `delscope` - Enter a scope pattern here to specify the names of channels to delete or extract. You do this by specifying a scope pattern, as detailed in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").     The default scope pattern `t*` will scope the translation channels: `tx`, `ty`, and `tz` , or any other channel whose name starts with `t`.
- Channel Numbers `selnumbers` - The indices of the channels to delete or extract. - See possible number patterns below.
- Channel Value `chanvalue` - ⊞ - Chooses the type of value range selection:
  * Off `off` - Don't perform range selection.
  * Channel Completely Within Range `complete` - All the channel's samples must be within the specified range for it to be selected.
  * Channel Partially Within Range `partial` - At least one of the channel's samples must be in the range for it to be selected.
  * Channel Completely Outside Range `outside` - None of the channel's samples can be in the range for it to be selected.

- Value Range `selrange` - ⊞ - The lower and upper values of the range used for Range Selection.
  * `selrange1` -
  * `selrange2` -

- Select Constant Valued Channels `selconst` - Select channels which have the same value for all samples. These kinds of channel name patterns are used to select existing channels in an input CHOP, see [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") for details.
Also these kinds of channel number patterns can be used to select existing channels in an input CHOP:
  * ` 0 1 4` - Matches the first, second and fifth channel.
  * ` [0-4]` - Matches the first five channels.
  * `[3-9:2]` - Matches channels at indices 3,5, 7 and 9.

## Parameters - Samples Page
- Delete Samples `delsamples` - Toggle to enable sample deleting.
- Channels to Compare `compchans` - ⊞ - How to select channels used to compare against criteria - By Name, by Numeric index, by using the First Channel, or by using the Last Channel.
  * Use First Channel `firstchan` -
  * Use Last Channel `lastchan` -
  * By Channel Name `byname` -
  * By Channel Number `bynum` -

- Channel Names `compnames` - Enter a scope pattern here to specify the names of channels to be used as compare channels. You do this by specifying a scope pattern, as detailed in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Channel Numbers `compnums` - The indices of the channels to be used as compare channels, the default being **0** , the first channel. - See possible number patterns above.
- Multi-Compare Channels `compmulti` - ⊞ - If there is more that one compare channel, this determines how to treat the values in the compare channels before checking against the criteria:
  * Any Chan in Range `any` - Delete the sample if any of the compare channels meets the criteria.
  * All Chans in Range `all` - Delete the sample if all the compare channels meets the criteria.
  * Add `add` - Add all the compare channels and delete the sample if the result meets the criteria.
  * Subtract `sub` - Subtract all the compare channels from the first and delete the sample if the result meets the criteria.
  * Multiply `mul` - Multiply all the compare channels and delete the sample if the result meets the criteria.
  * Divide `div` - Divide the first channel by rest of the compare channels and delete the sample if the result meets the criteria.
  * Average `avg` - Find the average of all the compare channels and delete the sample if the result meets the criteria.
  * Minimum `min` - Find the minimum of all the compare channels and delete the sample if the result meets the criteria.
  * Maximum `max` - Find the maximum of all the compare channels and delete the sample if the result meets the criteria.
  * Length `len` - Assume all the compare channels are vectors and find their length, and delete the sample if the result meets the criteria.

- Delete Condition `condition` - ⊞ - Choose the criteria for the samples to be compare against:
  * Less Than Value 1 `less` - Delete if the comparing samples are below Value 1.
  * Greater Than Value 1 `greater` - Delete if the comparing samples are above Value 1.
  * Equal to Value 1 `equal` - Delete if the comparing samples are equal to Value 1.
  * Not Equal to Value 1 `notequal` - Delete if the comparing samples are not equal to Value 1.
  * Inside Range `inside` - Delete if the comparing samples are inside the range assigned by Value 1 and Value 2.
  * Outside Range `outside` - Delete if the comparing samples are outside the range assigned by Value 1 and Value 2.

- Value 1 `value1` - Set a value for Value 1.
- Include Value 1 `inclvalue1` - Toggle the inclusivity of Value 1.
- Value 2 `value2` - Set a value for Value 2.
- Include Value 2 `inclvalue2` - Toggle the inclusivity of Value 2.
- Delete Compare Channels `deletecomp` - Determines whether the compare channels should be deleted or retained.
- One Sample if All Deleted `onesample` - Leaves one sample even when all samples are deleted.

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
Extra Information for the Delete CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Delete CHOP Info Channels
  * actual_length -

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
