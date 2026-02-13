---
url: https://docs.derivative.ca/Count_CHOP
category: CHOPs
title: Count_CHOP
---

# Count CHOP
## Summary

The Count CHOP counts the number of times a channel crosses a trigger or release threshold. It operates in either static or realtime ("Cook to Current Frame") mode.
The trigger value by default is 0, so the count occurs when the input goes from below (or equal to) 0 to a value that is greater than zero.
Crossing the trigger threshold (increasing past the trigger level) creates a trigger event. Similarly, crossing the release threshold (decreasing past the release level) creates a release event. Operations may also be performed while the input remain above or below the trigger or release levels. On each event, the count may be increased or decreased by 1 or the time, or reset to zero. The time per sample varies with the sample rate (i.e. for 100 samples/second, the time for each sample would be 1/100th of a second).
The optional second input is a reset input. The first channel is interpreted as a channel containing reset pulses. Whenever this channel is non-zero, the count for all channels is reset.
The third input is labeled "Increment Value". It allows you to specify a value other than the default +-1 to count. If you want to count by Fives, then put a channel with a value of 5 in this input. It will increment by 5 each count, or by 5 per second depending on the On / Off menus on the second page.
[countCHOP_Class](https://docs.derivative.ca/CountCHOP_Class "CountCHOP Class")

## Parameters - Trigger Page
- Release = Trigger Threshold `threshold` - If on, the trigger threshold is also used as the release threshold.
- Trigger Threshold `threshup` - The channel level that must be exceeded in order to trigger a count.
- Release Threshold `threshdown` - A release count is triggered when the channel level drops below this threshold.
- Re-Trigger Delay `retrigger` - The amount of time after a trigger point that a new trigger may occur.
- Re-Trigger Delay Unit `retriggerunit` -
- Trigger On `triggeron` - ⊞ - Determines whether a trigger occurs on an increasing slope or decreasing slope when passing the trigger threshold. A release will occur on the opposite slope.
  * Increasing Values `increase` -
  * Decreasing Values `decrease` -

## Parameters - Count Page
- Limit `output` - ⊞ - Select limit options such as loop and/or clamp from the menu. The value will remain in the range from Min to Max.
  * Off `off` - No limits.
  * Loop Min/Max `loop` - Will cycle in a loop between the values given by Limit Minimum / Maximum.
  * Clamp Min/Max `min` - Clamp will hold the count value at the maximum/minimum value if it goes above or below the limits.
  * Loop Min, Clamp Max `lc` - Will loop the count back between the limits by shifting the count to the maximum limit.
  * Clamp Min, Loop Max `cl` - Will loop the count back between the limits by shifting the count to the minimum limit.
  * Zigzag Min/Max `zigzag` - Will zig-zag the count back and forth between the minimum and maximum limit.

- Limit Minimum `limitmin` - The minimum allowed count number.
- Limit Maximum `limitmax` - The maximum allowed count number.
- Off to On `offtoon` - ⊞ - The operation to perform when a trigger event (off to on) occurs.
  * None `none` -
  * Increase Count `inc` -
  * Decrease Count `dec` -
  * Increase Count by Time `inctime` -
  * Decrease Count by Time `dectime` -
  * Reset Count to Zero `reset` -

- While On `on` - ⊞ - The operation to perform while the input remains triggered (on).
  * None `none` -
  * Increase Count `inc` -
  * Decrease Count `dec` -
  * Increase Count by Time `inctime` -
  * Decrease Count by Time `dectime` -
  * Reset Count to Zero `reset` -

- On to Off `ontooff` - ⊞ - The operation to perform when a release event (on to off) occurs.
  * None `none` -
  * Increase Count `inc` -
  * Decrease Count `dec` -
  * Increase Count by Time `inctime` -
  * Decrease Count by Time `dectime` -
  * Reset Count to Zero `reset` -

- While Off `off` - ⊞ - The operation to perform while the input is not triggered (off).
**Note** : The scripts are run relative to the parent node of this CHOP, as if the script is in the node above this CHOP.
  * None `none` -
  * Increase Count `inc` -
  * Decrease Count `dec` -
  * Increase Count by Time `inctime` -
  * Decrease Count by Time `dectime` -
  * Reset Count to Zero `reset` -

- Reset Condition `resetcondition` - ⊞ - This menu determines how the Reset input triggers a reset of the channel(s).
  * Off to On `offtoon` - Channels are reset when the Reset input goes off to on.
  * While On `on` - Channels are reset when the Reset input goes on. The channel will hold the reset value until the input turns off.
  * On to Off `ontooff` - Channels are reset when the Reset input goes on to off.
  * While Off `off` - Channels are reset when the Reset input goes off. The channel will hold the reset value until the input turns on.

- Reset Value `resetvalue` - The channel(s) is set to this value when reset.
- Reset `reset` - When On resets the channel(s) to the Reset Value. The Count CHOP will only begin counting again when Reset is Off.
- Reset Pulse `resetpulse` - Instantly resets the channel(s) to the Reset Value.

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
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Count CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
