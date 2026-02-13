---
url: https://docs.derivative.ca/Bullet_Solver_CHOP
category: CHOPs
title: Bullet_Solver_CHOP
---

# Bullet Solver CHOP
## Summary

The Bullet Solver CHOP is used in conjunction with a [Bullet Dynamics](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics") system. It outputs the solved results from a Bullet simulation and can include the results for the entire system ([Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP")) or an individual actor ([Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP")) within a system.
The Bullet Solver CHOP can also be used with the "Feedback CHOP" parameter on the Bullet Solver COMP or Actor COMP. Bullet Solver simulation results can be grabbed using the Bullet Solver CHOP, modified, then fed back into the [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP") it came from. The values at the beginning of the next step of the simulation will be whatever values are in the CHOP that is fed back. This allows any CHOP data to be injected into the simulation at the beginning of the next frame (time step).
For example: making an actor in the simulation jump to the mouse cursor when clicked.
**Output Channels:**
  * **actor_id:** the OP id of the Actor COMP
  * **body_id:** the id of the body within the Actor COMP. Actor COMPs can have multiple bodies if they are static or if instancing (see: Actor COMP). Body id's increment from 0 to N-1, where N is the total number of bodies in an Actor COMP.
  * **active:** whether the body is active in the simulation
  * **colliding:** whether the body is currently colliding with another body
  * **colliding_actor_id** the ID of the Actor COMP that contains the body we are colliding with
  * **colliding_body_id** the ID of the body we are colliding with; together with colliding_actor_id will map back to a specific body in the simulation
  * **total_collisions:** the total number of collisions this body has had
  * **t[xyz]:** the translation of the body in the given transform space
  * **r[xyz]:** the rotation of the body in the given transform space
  * **s[xyz]:** the scale of the body in the given transform space
  * **vel_t[xyz]:** linear velocity of the body
  * **vel_r[xyz]:** angular velocity of the body

See also: [Bullet Dynamics](https://docs.derivative.ca/Bullet_Dynamics "Bullet Dynamics"), [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP"), [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"), [Force COMP](https://docs.derivative.ca/Force_COMP "Force COMP"), [Impulse Force COMP](https://docs.derivative.ca/Impulse_Force_COMP "Impulse Force COMP"), [Constraint COMP](https://docs.derivative.ca/Constraint_COMP "Constraint COMP").
[bulletsolverCHOP_Class](https://docs.derivative.ca/BulletsolverCHOP_Class "BulletsolverCHOP Class")

## Parameters - General Page
- Solver or Actor COMP `comp` - A reference to either a [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP") or [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"). If a Bullet Solver COMP is referenced then the CHOP will output the simulation results for all of its actors. If an Actor COMP is referenced then the CHOP will output the simulation results for only that actor.
- Transform Space `xformspace` - ⊞ - The space in which to output the transformation values. That is, the transform values (translation/rotation) will be outputted relative to the selected space.
  * World `world` - The output transform is in the world coordinate system.
  * Bullet Solver `bulletsolver` - The transform output is relative to the Bullet Solver COMP.
  * Actor `actor` - The output transform is relative to the Actor COMP.

- Collision Info `collisioninfo` - Adds colliding, colliding_actor_id, colliding_body_id, and total_collisions channels to the CHOP. In order to track these values for a body, "Perform Contact Test" must be enabled on the Bullet Solver COMP.
- Translation `trans` - Adds translation channels to the CHOP.
- Rotation `rot` - Adds rotation channels to the CHOP.
- Scale `scale` - Adds scale channels to the CHOP.
- Linear Velocity `linvel` - Adds linear velocity channels to the CHOP.
- Angular Velocity `angvel` - Adds angular velocity channels to the CHOP.
- Sample Rate `rate` - The sample rate of the CHOP.
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
Extra Information for the Bullet Solver CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
