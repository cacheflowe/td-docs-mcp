---
url: https://docs.derivative.ca/Handle_CHOP
category: CHOPs
title: Handle_CHOP
---

# Handle CHOP
## Summary

The Handle CHOP is the "engine" which drives Inverse Kinematic solutions using the [Handle COMP](https://docs.derivative.ca/Handle_COMP "Handle COMP"). The role of the Handle CHOP is to generate rotation values for the bones which will bring their attached handles as close to their respective targets as possible.
The use of this method is best described with an example:
  1. Increase the frame range to 10000. Create a [Null COMP](https://docs.derivative.ca/Null_COMP "Null COMP") called 'target' and animate a few random positions for it to travel to.
  2. Create a three bone IK chain with No Kinematics. Append a [Handle COMP](https://docs.derivative.ca/Handle_COMP "Handle COMP") to the last bone.
  3. In the Handle COMP set the Target menu to Target. This is the Null COMP you just created.
  4. The system is now specified. To actually start the IK enter a CHOP pane.
  5. Place a Handle CHOP. In the Source field type in the names of the bones that were earlier created.
  6. Click the Export button on the Handle CHOP and click Play. You should now see the two-bone system chasing the animated null.

**Tip:** In the [geometry viewer](https://docs.derivative.ca/Geometry_Viewer "Geometry Viewer"), you can use the **Select** state to select the bones you created. Then in the Handle CHOP click the **Grab Source Form Selection** button. The names are entered automatically for you. You don't have to worry about being too picky when selecting objects this way, since non-bone objects are ignored.
You can place any number of bones with any number of (possibly zero) Handles attached to the system. The following parameter description will now give a more detailed explanation of the functionality:
[handleCHOP_Class](https://docs.derivative.ca/HandleCHOP_Class "HandleCHOP Class")

## Parameters - Handle Page
- Source `source` - Creates `rx`/`ry`/`rz` channels for each bone listed.
- Fixed `fixed` - If you have entered bones which form a branch or should act as a unit, enter them here. An example may be two bones splitting at the shoulders. You want them to rotate, but only as a unit.
- Iterations `iterations` - Increasing this parameters gives a more accurate solution at the cost of cooking time. Preroll (only when precalculating a range of frames, SingleFrame turned off): This will cook the solution a given number of frames before the requested frame range. Max Angle Change: This will limit the delta angle degrees the bones can move in any given frame. Use this to tame erratic behavior.
- Init Frame `init` - Specifies a frame in which the bones are reset to their default rest angles.
- Preroll `preroll` - Specifies the number of iterations to solve at the initialization frame.
- Max Angle Change `delta` - Specifies the maximum change in degrees the solver is allowed to move each bone per frame. Use this parameter if the solution is too drastic.

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
Extra Information for the Handle CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
