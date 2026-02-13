---
url: https://docs.derivative.ca/Info_CHOP
category: CHOPs
title: Info_CHOP
---

# Info CHOP
## Summary

The Info CHOP gives you extra information about a node. All nodes contain extra inside information, and different types of nodes (TOPs, CHOPs, etc) contain different subsets of information. This additional information can be accessed via an Info CHOP.
The Info CHOP's extra attributes for specific OPs are also expressed as python members of those operators. The the operators python class for more information.
Any OP that has a `.timecode` member will also have a Timecode Info Type available to view the timecode value as a set of CHOP channels. See [OPs with a timecode member](https://docs.derivative.ca/Timecode#Operators_with_a_.timecode_Member "Timecode") and the [Timecode](https://docs.derivative.ca/Timecode "Timecode") page for more info.
[infoCHOP_Class](https://docs.derivative.ca/InfoCHOP_Class "InfoCHOP Class")

## Parameters - Info Page
- Operator `op` - The path of the node that the Info CHOP is getting information from. You can drag and drop any node onto this path, or type the path directly into the field.
- Info Type `infotype` - ⊞ - Select the channel set associated with the Info Type.
  * All `all` - Selects all channel sets and appends them to the output.
  * General `general` - Selects the channels of the specific OP type and the OP family as a whole.
  * Timecode `timecode` - (Optional) **Note:** Timecode entry will only appear in the list if the Operator referenced has a `.timecode` member. Provides the .timecode value as a set of CHOP channels: `hour`, `minute`, `second`, `frame`.

- Scope `iscope` - The names of the attributes to keep. Name patterns may be used as detailed in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Values `values` - ⊞ - Select channel with values inside or outside the range specified in Range.
  * All `all` - All channels selected.
  * Inside Range `inside` - Channels with values inside Range selected.
  * Outside Range `outside` - Channels with values outside Range selected.

- Range `range` - ⊞ - Set the bounds for selecting channels by value.
  * `range1` -
  * `range2` -

- Passive `passive` - When Passive is Off the Info CHOP will cook the Operator it is pointing to before querying its values. When Passive is On it will not force a cook. A side effect: If the Info CHOP and the target are both cooking that frame, the Info may cook before the target, so it’s data will be a frame late.
- Children Cook Time `childcooktime` - When the Info CHOP is monitoring a [Component](https://docs.derivative.ca/Component "Component"), this toggle will enable a channel called `children_cpu_cook_time` which is the total cooktime of all the component's children. This is off by default, enabling it for a large network may impact performance as all cooktimes need to be summed.

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
Extra Information for the Info CHOP can be accessed via an Info CHOP.
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
