---
url: https://docs.derivative.ca/Inverse_Kin_CHOP
category: CHOPs
title: Inverse_Kin_CHOP
---

# Inverse Kin CHOP
## Summary

The Inverse Kin CHOP calculates an inverse kinematics simulation for [Bone objects](https://docs.derivative.ca/Bone_COMP "Bone COMP").
[inversekinCHOP_Class](https://docs.derivative.ca/InversekinCHOP_Class "InversekinCHOP Class")

## Parameters - Kinematics Page
- Solver Type `solvertype` - ⊞ - This parameter defines the method used to determine the motion of the Bone object when it, its ancestor, or its children are moved.
  * None `none` - No motion solution is applied to the Bone object.
  * Show Rest Position `rest` - This solver is used to show the rest position of the bones. It orients the bones at the rest position defined by the rest angles in the chain. These rest angles are used in the Inverse Kinematics solver. Therefore, this solver can be used as a helper utility to show you the rest positions of the chain.
  * Show Capture Position `capture` - This solver is used to display the rotation values in the capture angles parameter. These parameters are set in the Skeleton sop when a "capture points" operation is performed, or by using the Grab Capture Angles menu. Like the Show Rest Position solver, this solver can be used to return a chain to its capture orientation.
  * Inverse Kinematics `inverse` - The IK solver tries to position the bones such that the end of the last bone in the chain touches the origin of the object defined as the end affector. The shape of the chain is derived from the rest angles of each the bones in the chain.

In order to adjust the results of the IK solver, you can adjust the rest angles of the bones. Note that the IK solver's solutions are guaranteed to be continuous only for a given set of rest angles. If you animate the rest angles you may end up with chains that jump around. When using kinematics, the rotations given by the kinematic solver can be exported to the bones using by enabling the export flag on the Inverse Kin CHOP. Adding rotation values to bone objects in a kinematic chain is not recommended, as those values will be over-written by the kinematic solver.
  * IK with Constraints `constraint` -
  * Follow Curve `curve` - This solver positions the bones to be aligned along the first curve in an object. It is useful for animating things such as tails and spines.

- Root Bone `boneroot` - The starting bone of the chain; where the chain starts.
- End Bone `boneend` - If you specify a bone as the last bone in chain, then you will be defining a bone chain that has the current bone as the first in the chain and the bone chosen from the menu as the final bone in the chain. This chain includes all bones in between those just chosen.
- End Affector `endaffector` - This specifies which object will serve as the chain's end affector.
- Twist Affector `twistaffector` - If you specify a twist affector, the entire bone chain will twist along the axis from the chain's root to its end-affector so that the first bone is pointing as much as it can at the twist affector. The twist value can be specified as well, and is applied on top of the twist generated for the twist affector.
- IK Twist `iktwist` - Amount of twist allowed by the kinematics solution.
- IK Dampening `ikdampen` - Amount of damping (slows down at the extremes of angular allowability).
- Curve Object `curve` - Curve object to follow.

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
Extra Information for the Inverse Kin CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
