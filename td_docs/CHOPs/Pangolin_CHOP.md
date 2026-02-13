---
url: https://docs.derivative.ca/Pangolin_CHOP
category: CHOPs
title: Pangolin_CHOP
---

# Pangolin CHOP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The Pangolin CHOP interfaces with Pangolin's [Beyond](https://pangolin.com/collections/beyond-software). Beyond is a professional laser and multimedia show control application. When Beyond is running, the Pangolin CHOP will send laser image frames to it. The image frames are created from either a POP, CHOP or SOP. See [Lasers](https://docs.derivative.ca/Lasers "Lasers") for an overview of lasers with TouchDesigner.
The Pangolin CHOP should work with any version of Beyond but it is recommended to use at least Beyond v5.1.
**TouchDesigner Non-Commercial licenses will only work with the demo version of Beyond. A TouchDesigner Commercial, Educational, or Pro license is required to interface with licensed versions of Beyond.**
**Using a SOP Input**: input points will be grouped by primitive, and point position as well as color attributes from either vertex, point, or primitives will be used to construct the points to send to Beyond.
**Using a CHOP input**: Input channels are determined by name: `x`, `y`, `z`, `r`, `g`, `b`, `id`, `zone`. Only the `x`, and `y` channels are required. Every sample will be interpreted as a point to be drawn. Points can be grouped together into different shapes using the `id` channel. If not used then all points will be considered as part of the same shape. The `zone` channel can be used to override the zone parameter value for each sample, adding the option to have more control over which sample/point goes to which zone in Beyond.
**Using a POP input**: similar to SOP, input points will be grouped by primitive. A Point position attribute (`P`) is a required, and a Point color attribute (`Color`) can optionally be used. If `Color` is not specified then point color will be set to white. Additionally, a primitive `Zone` attribute can be used to control which primitive goes to which zone in Beyond.
See also: [Laser CHOP](https://docs.derivative.ca/Laser_CHOP "Laser CHOP"), [Lasers](https://docs.derivative.ca/Lasers "Lasers").
[pangolinCHOP_Class](https://docs.derivative.ca/PangolinCHOP_Class "PangolinCHOP Class")

## Usage
Beyond must be open to use the Pangolin CHOP.
The Pangolin CHOP will construct a laser image from the points of a SOP or samples of a CHOP and send it to Beyond. With Beyond open and the Pangolin CHOP active (with input) the laser image can immediately be seen in its respective zone in the zone viewer of Beyond. See below an example of sending a circle to zone 1 in Beyond from the Pangolin CHOP.

[![PangolinTDZone.PNG](https://docs.derivative.ca/images/1/1e/PangolinTDZone.PNG)](https://docs.derivative.ca/File:PangolinTDZone.PNG)

## Parameters - Pangolin Page
- Active `active` - When disabled, the CHOP will no longer send to Beyond. The corresponding image in Beyond will also be cleared.
- Source `source` - ⊞ - Select the source operator.
  * SOP `sop` - Use a SOP as the source. Apart from position attributes, the SOP's point color attributes are used to determine the color output.
  * CHOP `chop` - Use a CHOP as the source. Input channels are determined by name: `x`, `y`, `z`, `r`, `g`, `b`, `id`. Only the `x`, and `y` channels are required. Every sample will be interpreted as a point to be drawn. Points can be grouped together into a single shape using the `id` channel.

- SOP `sop` - Path to the SOP.
- CHOP `chop` - Path to the CHOP. The input CHOP must have **x** , **y** channels for the point positions. In addition, it also supports **z** , **r** , **g** , **b** , and **id** channels. The **id** channel is used for grouping points together as a single shape. By default when no **id** channel is present, each point is separate and unconnected.
- POP `pop` - Path to the POP.
- Zone `zone` - The index of the zone to send to in Beyond.
- Rate Mode `ratemode` - ⊞ - Select the mode for calculating the rate of the image in Beyond. Note: this is not the rate of the CHOP.
  * Percent of Projector Sample Rate `percent` - Rate will be calculated as a percent of the default projector sample rate. Specify the percent using the Percent parameter.
  * Sample Rate `sample` - Specify the sample rate.

- Percent `percent` - Specify the sample rate as a percent of the projector default sample rate.
- Sample Rate `rate` - Specify the sample rate of the image in Beyond
- Vertex Repeat `repeat` - How often to repeat each point in the image (not including blanked points).
- Vector Frame `vector` - When enabled, the image will be sent to Beyond as a vector frame. A vector frame will have extra computation done in Beyond, such as the addition of blanking points. When disabled, the image will be sent as points to the DAC, with nothing extra added.
- Resend Image `resend` - Resend the image to Beyond.
- Enable Laser Output `enableout` - Enables laser output in Beyond. Has the same effect as hitting the "Enable Laser Output" button in Beyond.
- Disable Laser Output `disableout` - Disables laser output in Beyond. Has the same effect as hitting the "Disable Laser Output" button in Beyond.
- Blackout `blackout` - Sends a blackout command to Beyond. Has the effect as hitting the "Blackout" button in Beyond.

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
Extra Information for the Pangolin CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Pangolin CHOP Info Channels
  * beyond_dll_loaded -

  * beyond_dll_version -

  * beyond_started -

  * beyond_ready -

  * beyond_version -

  * beyond_projector_count -

  * beyond_zone_count -

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
