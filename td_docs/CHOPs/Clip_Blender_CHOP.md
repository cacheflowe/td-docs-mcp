---
url: https://docs.derivative.ca/Clip_Blender_CHOP
category: CHOPs
title: Clip_Blender_CHOP
---

# Clip Blender CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Clip Blender CHOP is a an engine for blending, sequencing and scripting animation clips. It loads animation channel data that is formatted using Clip CHOPs. It reads clip CHOP paths from a specified DAT list which can be dynamically scripted. The Clip Blender plays clips from the list DAT; each time it reads a clip, it pop's the item off the list, and when the next clip plays through it will continue playing and popping clips off the list until it is empty. Once the list is empty the last animation in the sequence is looped.
Animation clips will typically come from an FBX or USD asset but can also be read using the Houdini bclip format or raw chan format. Animation clips found in FBX assets must be extracted from the asset hierarchy and then loaded speerately into a [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP"). All [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP")'s loaded into the same clipblender must have the same number of channels, all channel names must match and the all clips must be the same sample rate. If any of these 3 important requirements are not met, there will likely be animation glitches.
Use the [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") and [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") to extract information about its current state. See also the [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP") and [Clip DAT](https://docs.derivative.ca/Clip_DAT "Clip DAT").
[clipblenderCHOP_Class](https://docs.derivative.ca/ClipblenderCHOP_Class "ClipblenderCHOP Class")

## Parameters - ClipBlender Page
- Default Clip CHOP `default` - Operator path to a valid [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP").
- DAT List `datlist` - Operator path to a valid [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT").
- Target `target` - ⊞ - This parameter works in conjunction with the root transform channels as defined on the Channels page of the clpblender CHOP as well as the [Clip CHOP](https://docs.derivative.ca/Clip_CHOP "Clip CHOP") parameter called Position Type. When Position Type is set to "Blend To Target" it will blend the root transform channels for the current clip to the new position defined in this parameter.
  * X `targetx` -
  * Y `targety` -
  * Z `targetz` -

- Play Speed `playspeed` - Provides a scale value to slow down or speed up the playback of the animation sequence.
- Step Forward `stepforward` - Unknown
- Step Backward `stepbackward` - Unknown
- A End Script `aend` - Broken
- Delay Samples `delay` - Delays the output of animation data by the specified number of samples.
- Reset `reset` - When On, resets the clipblender and holds it ready to play the clip defined by the Default Clip CHOP parameter.
- Reset Pulse `resetpulse` - Instantly reset the cliblender and start playing the clip defined by the Default Clip CHOP parameter.

## Parameters - Channels Page
- Output Time Remaining `timeremaining` - A channel of the name defined in this parameter will return the time remaining in the current clip.
- Time Channel `timechannel` - A channel of the name defined in this parameter will return the time elapsed in the current clip.
- X Root Trans `xtrans` - The translate X channel of the animation hierarchy that defines the [Clipblender Motion Root](https://docs.derivative.ca/index.php?title=Clipblender_Motion_Root&action=edit&redlink=1 "Clipblender Motion Root \(page does not exist\)").
- Y Root Trans `ytrans` - The translate Y channel of the animation hierarchy that defines the [Clipblender Motion Root](https://docs.derivative.ca/index.php?title=Clipblender_Motion_Root&action=edit&redlink=1 "Clipblender Motion Root \(page does not exist\)").
- Z Root Trans `ztrans` - The translate Z channel of the animation hierarchy that defines the [Clipblender Motion Root](https://docs.derivative.ca/index.php?title=Clipblender_Motion_Root&action=edit&redlink=1 "Clipblender Motion Root \(page does not exist\)").
- X Root Rot `xrot` - The rotate X channel of the animation hierarchy that defines the [Clipblender Motion Root](https://docs.derivative.ca/index.php?title=Clipblender_Motion_Root&action=edit&redlink=1 "Clipblender Motion Root \(page does not exist\)").
- Y Root Rot `yrot` - The rotate Y channel of the animation hierarchy that defines the [Clipblender Motion Root](https://docs.derivative.ca/index.php?title=Clipblender_Motion_Root&action=edit&redlink=1 "Clipblender Motion Root \(page does not exist\)").
- Z Root Rot `zrot` - The rotate Z channel of the animation hierarchy that defines the [Clipblender Motion Root](https://docs.derivative.ca/index.php?title=Clipblender_Motion_Root&action=edit&redlink=1 "Clipblender Motion Root \(page does not exist\)").
- Queue Enable `qenable` - Specifies the name of the queue enable channel that may be added to all animation clips that will be loaded into this clipblender. A "Queue Enable" channel may be added to the animation clip to define when this clip is safe and unsafe for blending into other clips. If the animation is not safe for blending, the channel would be set to 1, which means the clipblender should "Queue" the next clip in the sequence instead of playing it. When the channel is 0, the any animation request will be executed immediately.
- Queue Trigger `qtrigger` - Unknown
- Pre-Rotate Adds `prerotate` - Unknown

## Parameters - Transform Page
- Transform Next Clip `doxform` -
- Translate `t` - ⊞ -
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ -
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Print State `printstate` -
- Log Jumps `logjumps` -
- Jump Min `jumpmin` -
- Jump Max `jumpmax` -
- Jump Area XY `jumpxy` -
- Fix Jump `fixjump` -
- Log `logpulse` -

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
  * Input 1:  -
  * Input 2:  -

## Info CHOP Channels
Extra Information for the Clip Blender CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Clip Blender CHOP Info Channels
  * queue_state -

  * clipcurrent_start -

  * clipcurrent_end -

  * clipcurrent_frame -

  * clip_blending -

  * clip_current_time -

  * clip_start_blend_time -

  * clip_end_blend_time -

  * trigger_clip_wait -

  * clipa_ -

  * clipa_parent_ -

  * clipb_ -

  * clipb_parent_ -

  * trigger_ -

  * clipa_last_ -

  * clipa_parent_last_ -

  * clipb_last_ -

  * clipb_parent_last_ -

  * clipcurrent_ -

  * clipcurrent_parent_ -

  * clipnext_ -

  * clipnext_parent_ -

  * total_jumps -

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
