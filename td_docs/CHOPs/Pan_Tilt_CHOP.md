---
url: https://docs.derivative.ca/Pan_Tilt_CHOP
category: CHOPs
title: Pan_Tilt_CHOP
---

# Pan Tilt CHOP
## Summary

Calculate pan/tilt rotation values for a series of pan/tilt platforms like moving head light fixtures. Values are calculated to minimize flipping and angular rotation frame by frame. Multiple rigs are calculated per CHOP. The first input is the realtive position of the target to the fixture either as tx, ty, tz channels or a full set of transform channels as output by the Object CHOP. The angles are calculated to point the platform towards the target. If multiple platforms each have their individual moving target, the pan/tilt can be calculated by calculating the transform between target and fixture using the Object CHOP's DAT table parameter.
[pantiltCHOP_Class](https://docs.derivative.ca/PantiltCHOP_Class "PantiltCHOP Class")

## Parameters - Pan/Tilt Page
- Reset `reset` - Discard current orientation of the rigs, and set their last known orientation to this value.
- Reset Values `resetvals` - ⊞ - The beginning rotation for each rig, expressed in degrees. The output orientation is based on this initial orientation, which may or may not be the same.
  * Reset Values `resetvals1` - Pan reset value.
  * Reset Values `resetvals2` - Tilt reset value.

- Clamp Pan `clamppan` - Limit the pan value to a specific range.
- Pan Range `panrange` - ⊞ - The lower and upper angle limits for the pan. Expressed in degrees.
  * Pan Range `panrangemin` - Lower pan value.
  * Pan Range `panrangemax` - Upper pan value.

- Clamp Tilt `clamptilt` - Limit the tilt value to a specific range.
- Tilt Range `tiltrange` - ⊞ - The lower and upper angle limits for the tilt. Expressed in degrees.
  * Tilt Range `tiltrangemin` - Lower tilt value.
  * Tilt Range `tiltrangemax` - Upper tilt value.

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
  * Input 0:  - Platform channels: Must include tx,ty,tz. Must be a full set of transform channels including transform and rotation order if rotation is included. Describes the location of each platform rig.
  * Input 1:  - Reset values: Must include pan,tilt. Use this optional input to override the reset value for each individual platform rig.

## Info CHOP Channels
Extra Information for the Pan Tilt CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
