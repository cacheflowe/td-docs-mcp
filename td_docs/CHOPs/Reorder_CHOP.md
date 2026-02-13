---
url: https://docs.derivative.ca/Reorder_CHOP
category: CHOPs
title: Reorder_CHOP
---

# Reorder CHOP
## Summary

The Reorder CHOP re-orders the first input CHOP's channels by numeric or alphabetic patterns. Either a channel pattern specifies the new order, or a number sequence specifies the new order.
If the second input, the Order Reference is present, the Numeric Pattern and Character Pattern are ignored, and the first input CHOP's channels are reordered to match as well as possible the reference CHOP's. In this case, Method is not used.
Channel values are never affected.
[reorderCHOP_Class](https://docs.derivative.ca/ReorderCHOP_Class "ReorderCHOP Class")

## Parameters - Reorder Page
- Method `method` - ⊞ - There are three different reordering methods. You can enter a Numeric Pattern, a Character Pattern, or use an optional second input CHOP as an order reference.
  * Numeric Pattern `numeric` - This reorders the channels by channel number.
  * Character Pattern `character` - This reorders the channels by channel name.
  * Base Name Sort `basename` - This reorders the channels by their base name discounting the numeric suffix. For example `chan1, abc10` will be reordered to `abc10, chan1`
  * Numeric Suffix Sort `numsuffix` - This reorders the channels by their numeric suffix discounting the base name. For example `abc10, chan1` will be reordered to `chan1, abc10`
  * Channel Value Up `chanvalueup` - This reorders the channels by the channel's value, lowest first.
  * Channel Value Down `chanvaluedown` - This reorders the channels by the channel's value, highest first.
  * Reverse `reverse` - This reverses the input CHOP's channel order.
  * Random `random` - This reorders the channels randomly.
  * Merge N Groups `group` - This reorders the channels in groups the size of N, specified through the `N Value` parameter. This can be useful if you have a sequence of channels `r1, r2, ., rx, g1, g2, ., gx, b1, b2, ., bx` and your desired order is `r1, g1, b1, r2, g2, b2, ., rx, gx, bx`
  * Every Nth Channel `split` - This reorders the channels by selecting every Nth channel, specified through the `N Value` parameter.

- Order Reference `orderref` - ⊞ - Only enabled if a second input is present. Specifies the format of that input.
  * By Name `byname` - The input consists of a list of channels, whose names specify the order.
  * By Index `byindex` - The input consists of a single channel, whose sample values specify the order.

- Numeric Pattern `numpattern` - This reorders the channels by channel number. Normally the index order is 0,1,2,3... etc.. The first channel is at index 0. Standard numeric patterns are allowed such as `"0-6:1,2"` or `"!*:1,3"`.
- Character Pattern `charpattern` - This reorders the channels by channel name. Standard character patterns are allowed such as `"ch[XYZ]"` or `"chan[1-15:2,5]"` or `"chan? ch*"`. See Scope and Channel Name Matching Options p. 102 in the section, Standard Options of CHOPs.
- Seed `seed` - Only available if `Channel Reorder Method` is set to "Random", specify any number, integer or non-integer, which starts the random number generator. Each number gives completely different patterns, but with similar characteristics.
- N Value `nvalue` - Only available if `Channel Reorder Method` is set to "Merge N Groups" or "Every Nth Channel".
- Remaining Position `rempos` - ⊞ - Channels that do not match are called "remaining" and can also be ordered: they can be placed at the At Beginning or At Ending (in reference to the position of the matched channels).
  * At Beginning `begin` -
  * At Ending `end` -

- Remaining Order `remorder` - ⊞ - The channels that did not match can have the Same as Input order, or can be sorted AlphaNumerically.
  * Same as Input `input` -
  * AlphaNumeric `alpha` -

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
Extra Information for the Reorder CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
