---
url: https://docs.derivative.ca/Shared_Mem_In_CHOP
category: CHOPs
title: Shared_Mem_In_CHOP
---

# Shared Mem In CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Educational](https://docs.derivative.ca/TouchDesigner_Educational "TouchDesigner Educational"), [TouchDesigner Commercial](https://docs.derivative.ca/TouchDesigner_Commercial "TouchDesigner Commercial") and [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Shared Mem In CHOP receives CHOPs from a shared memory segment that is attached to a [Shared Mem Out CHOP](https://docs.derivative.ca/Shared_Mem_Out_CHOP "Shared Mem Out CHOP") in another process or the same process.
See [Using Shared Memory in TouchDesigner](https://docs.derivative.ca/Using_Shared_Memory_in_TouchDesigner "Using Shared Memory in TouchDesigner"), [Write a Shared Memory CHOP](https://docs.derivative.ca/Write_a_Shared_Memory_CHOP "Write a Shared Memory CHOP") and the [Pipe In CHOP](https://docs.derivative.ca/Pipe_In_CHOP "Pipe In CHOP").
[sharedmeminCHOP_Class](https://docs.derivative.ca/SharedmeminCHOP_Class "SharedmeminCHOP Class")

## Parameters - SharedMemIn Page
- Active `active` - When active, the CHOP cooks and reads from the memory block.
- Shared Mem Name `name` - The name of the memory block it reads from.
- Shared Mem Type `memtype` - ⊞ - Reads from a Local or a Global memory location.
  * Local `local` - This node will use a shared memory segment unique for the given name. This mode must be used for sharing with applications other than TouchDesigner.
  * Global `global` - This mode uses a combined shared memory segment that all of the nodes will read for. More details in the [Global Shared Memory](https://docs.derivative.ca/Shared_Memory#Global_Shared_Memory "Shared Memory") article.

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
Extra Information for the Shared Mem In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
