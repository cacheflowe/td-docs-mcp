---
url: https://docs.derivative.ca/SOP_to_CHOP
category: CHOPs
title: SOP_to_CHOP
---

# SOP to CHOP
## Summary

The SOP to CHOP uses a [geometry object](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") to choose a [SOP](https://docs.derivative.ca/SOP "SOP") from which the channels will be created. The channels are created from the point attributes of a SOP, such as the X, Y and Z of the point position.
From the SOP you can select a subset of the points using Point Groups. The set of attributes that are converted to channels are chosen using the names of the attributes seen on the Info popup of SOP tiles (middle mouse click on a SOP in a SOP network pane).
For data going the opposite direction, see the [Channel SOP](https://docs.derivative.ca/CHOP_to_SOP "CHOP to SOP").
**Note:** This CHOP works in tandem with the [Channel SOP](https://docs.derivative.ca/CHOP_to_SOP "CHOP to SOP"). Point data is modified in CHOPs as regular channel data (samples) and then fed back to geometry as point attributes through the Channel SOP.
[soptoCHOP_Class](https://docs.derivative.ca/SoptoCHOP_Class "SoptoCHOP Class")

## Parameters - SOP to CHOP Page
- SOP `sop` - Specifies which Object / SOP contains the geometry you want to fetch.
- Group `group` - Only points within the specified group are Fetched. If blank, all points are fetched.
- Position `position` - When On will retrieve the position attributes (P) from the SOP and create channels tx, ty, tz.
- Color RGB `colorrgb` - When On will retrieve the RGB color attributes (Cd0, Cd1, Cd2) from the SOP and create channels cr, cg, cb.
- Color Alpha `coloralpha` - When On will retrieve the Alpha color attribute (Cd4) from the SOP and create channel alpha.
- Normal `normal` - When On will retrieve the Normal attributes (N) from the SOP and create channels nx, ny, nz.
- Texture UV `textureuv` - When On will retrieve the UV texture attributes (uv0, uv1) from the SOP and create channels u and v.
- Texture W `texturew` - When On will retrieve the W texture attribute (uv2) from the SOP and create channel w.
- Point Index `pointindex` - Turn On to output the point index of each point in the SOP in a channel called index.
- Normal Position XYZ `normpos` - Turn On
- Custom `custom` - Turn On to access any attributes in the SOP including Custom Attributes by using the two parameters below.
- Attribute Scope `attribscope` - This selects the custom attributes of the SOP to acquire.
You can use any attribute. If you look at the SOP's info by middle-mouse clicking on the SOP and there are other attributes, you can specify them. For example "pscale" will the particel scale attribute if it exists.
See [Attributes](https://docs.derivative.ca/Attribute "Attribute") for a complete list of attributes.
- Rename Scope `renamescope` - This parameter matches each channel acquired in the Attribute Scope. There must be one name per attribute value. By default, it translates the P attribute (position of the point) to `tx`, `ty` and `tz` channels. You can use [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") to specify multiple channels.
- Transform Object `transobj` - If a transform object is specified, the point values will be represented relative to that object's origin and rotation.
- Sample Rate `rate` - The sample rate of the channels, in samples per second.

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
Extra Information for the SOP to CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
