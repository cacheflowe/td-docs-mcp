---
url: https://docs.derivative.ca/Panel_CHOP
category: CHOPs
title: Panel_CHOP
---

# Panel CHOP
## Summary

The Panel CHOP reads [Panel Values](https://docs.derivative.ca/Panel_Value "Panel Value") from [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component") into CHOP channels. Panel values can also be accessed by using the `panel` Member of the [PanelCOMP Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class").
[panelCHOP_Class](https://docs.derivative.ca/PanelCHOP_Class "PanelCHOP Class")

## Parameters - Panel Page
- Component `component` - The path of the Component being referenced.
- Select `select` - Specify which panel values to create channels for. Use * to select all panel values. Add individual values using the drop down menu on the right.
- Rename `rename` - Rename the panel value channels selected with the Select parameter here. For example, if "u v" are selected in the Select parameter, you can rename these channels to horizontal and vertical by entering "horizontal vertical".
- Queue Overlapping Events `queue` - Queue all events that occur in a [time slice](https://docs.derivative.ca/Time_Slicing "Time Slicing"). Some [panel values](https://docs.derivative.ca/Panel_Value "Panel Value"), such as wheel or key, switches between a value and 0 in the same time slice and are considered instantaneous. When this parameter is off, only the last value in the time slice will be used, and changes could be missed. Turning this on will keep as many events as possible based on queue size. Each queued item will be released in the next time slice until the queue is empty, and value changes within the same time slice are synchronized.
- Queue Size `queuesize` - Size of queue. If the number of events is larger than the queue size, earlier events will be discarded.

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

## Info CHOP Channels
Extra Information for the Panel CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
