---
url: https://docs.derivative.ca/RenderStream_In_CHOP
category: CHOPs
title: RenderStream_In_CHOP
---

# RenderStream In CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
This node is the primary node to control and configure a connection with the [RenderStream](https://docs.derivative.ca/RenderStream "RenderStream") protocol from [Disguise](https://www.disguise.one/en/products/renderstream/). Along with being the sync-point for when a frame starts rendering, it also brings in all of the control channels, and also takes a DAT with schema information to create controllable parameters within Disguise.
Usually you want to have the 'Real-Time' flag on the top of the TouchDesigner UI turned off when using this node, so that this node is what drives frame advancement, not the default TouchDesigner time advancement.
See the [RenderStream](https://docs.derivative.ca/RenderStream "RenderStream") article for more information.
See also [RenderStream Out TOP](https://docs.derivative.ca/RenderStream_Out_TOP "RenderStream Out TOP"), [RenderStream In TOP](https://docs.derivative.ca/RenderStream_In_TOP "RenderStream In TOP"), [RenderStream](https://docs.derivative.ca/RenderStream "RenderStream").
[renderstreaminCHOP_Class](https://docs.derivative.ca/RenderstreaminCHOP_Class "RenderstreaminCHOP Class")

## Parameters - RenderStream In Page
- Active `active` - Controls if the RenderStream session is active.
- Timeout `timeout` - When waiting for a sync signal to start a frame, this controls how long the node will stall (in milliseconds), before giving up waiting for a sync signal.
- Stream Index `streamindex` - Controls which stream index this node should be syncing with and getting channels from.
- Schema DAT `schemadat` - This should be a DAT with a table containing the schema information to create sequencable parameters in Disguise. The Schema DAT supports the columns: `group, label, name, type, default, min, max, step`, where `group, label, name, type` are required. The `type` column should be one of: `float, image, text`. Float data will come in via the primary channels in this node. Image data can be obtained using a [RenderStream In TOP](https://docs.derivative.ca/RenderStream_In_TOP "RenderStream In TOP"). Text data can be obtained using an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") pointing to this node.

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

## Info CHOP Channels
Extra Information for the RenderStream CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific RenderStream CHOP Info Channels
  * num_streams - The number of RenderStream streams available to choose from.

  * last_sync_wait - The amount of time this node stalled the process waiting for a sync signal over RenderStream, in milliseconds.

  * num_timeouts - The number of times the node waited for it's full timeout period and never got a sync signal from RenderStream.

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
