---
url: https://docs.derivative.ca/Select_CHOP
category: CHOPs
title: Select_CHOP
---

# Select CHOP
## Summary

The Select CHOP selects and renames channels from other CHOPs of any CHOP network. You can select the channels from control panel gadgets like sliders and buttons. It retrieves channels from one or more CHOPs.
It selects only the channels you specify. Example: "`c2 c5 c3 c3`" will result in 4 channels, the last two identical, all in the specified order.
There are two ways of getting channels - through the CHOP and Channel Name parameters or directly from a CHOP connected to its input. All extract and renaming options apply when using the CHOP and Channel Name parameters instead of the wired input.
See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") for selecting CHOPs and channels.
It can also rename channels by generating new channel names. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement") and [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion") for patterns you can use.
See [Channel Naming Patterns](https://docs.derivative.ca/Rename_CHOP#Channel_Naming_Patterns "Rename CHOP") for more ways to manipulate existing channel names into new ones.
(The Select CHOP gets channels from any CHOP, the [Parameter CHOP](https://docs.derivative.ca/Parameter_CHOP "Parameter CHOP") gets parameters of any OP.)
See also the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") (Select CHOP does most of the same things and more.)
[selectCHOP_Class](https://docs.derivative.ca/SelectCHOP_Class "SelectCHOP Class")

## Parameters - Select Page
- CHOP `chop` - The source(s) of the channels. (Assuming the CHOP is not directly connected).
- Channel Names `channames` - The names of the channels to keep. Name patterns may be used. Ex: ```
 chan[1-5] *x /project1/geo1:t[xyz]

```

The order of the names determine the order of the output channels. If a channel is specified multiple times, it is included in the output multiple times.
- Rename from `renamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `renameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.
- Filter by Digits `filterbydigits` - This toggle enables the two parameters below to select channels with the specified digits at the end of their name. For examples, this can be used to selct all channels with a name ending in the digit "1", such as tx1, ty1, tz1, rotate1, etc.
- Digits `digits` - Specify the digit at then end of the channel names you want to select when using 'Filter by Digits'
- Strip Digits `stripdigits` - Then On, the selected channel names are output without the digits. When Off, the selected channel names are not changed.
- Align `align` - ⊞ - This menu handles cases where multiple input CHOPs have different start or end times. All channels output from a CHOP share the same start/end interval, so the inputs must be treated with the Align Options:
  * Automatic `auto` - It will trim to the current [Time Slice] if there are any Time Slices, else it will do an Extend Min/Max.
  * Extend to Min/Max `none` - Find the earliest start and latest end, and extend all inputs to that range using the extend conditions. (See [Extend Conditions](https://docs.derivative.ca/CHOP_Channel_Page#Extend_Conditions "CHOP Channel Page")).
  * Stretch to Min/Max `stretch` - Find the earliest start and latest end, and stretch every channel's start and end to that range.
  * Shift to Minimum `start` - Find the earliest start and shift all channels so they all start at that index. All channels are extended to the length of the longest one.
  * Shift to Maximum `end` - Find the latest end and shift all channels so they all end at that index. Extend all channels to the length of the longest one.
  * Shift to First Interval `shift1` - Shift all channels to the start of the first CHOP and sample all inputs using the first input's range.
  * Trim to First Interval `trim1` - Trim all channels to first CHOP's range.
  * Stretch to First Interval `stretch1` - Stretch all channels to the first CHOP's range.
  * Trim to Smallest Interval `trim` - Trim all channels to the smallest start/end interval. The start and end values may not come from the same channel.
  * Stretch to Smallest Interval `squash` - Stretch all channels to the smallest start/end interval. The start and end values may not come from the same channel.

- Automatic Prefix `autoprefix` - When 2 channels have the same name, turning on this option will add the node's name (or the node's parent's name, etc.) as a prefix to the channel name. For example, if selecting a channel from `/wave1/chan1` and `/wave2/chan1`, the channels would be renamed `chan1` and `chan2` if this option is off. Once turned on the channels would be named `wave1:chan1` and `wave2:chan1`.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Select CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
