---
url: https://docs.derivative.ca/Keyframe_CHOP
category: CHOPs
title: Keyframe_CHOP
---

# Keyframe CHOP
## Summary

The Keyframe CHOP uses channel and keys data in an [Animation COMP](https://docs.derivative.ca/Animation_COMP "Animation COMP") and creates channels of samples at a selectable sample rate (frames per second).
See also: [Animation COMP](https://docs.derivative.ca/Animation_COMP "Animation COMP") and [Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor")
The Keyframe CHOP lets you access the keyframed channel data inside an Animation component. The Animation CHOP allows the channels to be played back with the global frame or seconds index. It can be synced to the internal global beat clock, a specified index, or based on a timing or lookup channel sent into the input. It outputs all channels - either as a single sample or an entire start/end range.
To create/edit/delete keyframed channels, create an [Animation COMP](https://docs.derivative.ca/Animation_COMP "Animation COMP") and open the [Animation Editor](https://docs.derivative.ca/Animation_Editor "Animation Editor") by right-clicking on the component and selecting Edit Keyframes... from the pop-up menu. Inside the Animation component a Keyframe CHOP will be outputting the channels created in the editor.
Adding an input to the Keyframe CHOP now acts as a lookup index. In addition it outputs a proper [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") if its input is a Time Slice.
The lookup cycles through all the input channels, though only 1 is necessary.
[keyframeCHOP_Class](https://docs.derivative.ca/KeyframeCHOP_Class "KeyframeCHOP Class")

## Parameters - Keyframe Page
- Animation Component `animation` - The path to the Animation Component holding the channel and key data.
- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before range).
  * Hold `hold` -
  * Slope `slope` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Default Value `default` -

- Extend Right `right` - ⊞ - The right extend conditions (after range).
  * Hold `hold` -
  * Slope `slope` -
  * Cycle `cycle` -
  * Mirror `mirror` -
  * Default Value `default` -

- Default Value `defval` - The default value for extend conditions.

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
Extra Information for the Keyframe CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Keyframe CHOP Info Channels
  * start_index -

  * start_frame -

  * start_second -

  * start_fraction -

  * end_index -

  * end_frame -

  * end_second -

  * end_fraction -

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
