---
url: https://docs.derivative.ca/Import_Select_CHOP
category: CHOPs
title: Import_Select_CHOP
---

# Import Select CHOP
## Summary

The Import Select CHOP is used to specify CHOP channels from an importing file such as [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP") or [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP"). One of the main purpose of these channels is to represent the changes of transformation of different primitives or the state of some dynamic features of importing file. The Import Select CHOP can have its own animation controls within the Play page or use the settings from its parent COMP.
See Also: [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP"), [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP")
[importselectCHOP_Class](https://docs.derivative.ca/ImportselectCHOP_Class "ImportselectCHOP Class")

## Parameters - General Page
- Import Parent `parent` - Specify the import parent (eg. USD/FBX COMP) to search for the asset. When no COMP is specified it will by default search in the first import parent in its path.
- Take Type `taketype` - ⊞ - Select between playback of an animation or a blend shape.
  * Blend Shapes `blendshapes` -
  * Animation `animation` -

- Blend Shape `blendshape` - Specifices the blend shape name (if any is specified) from the importing file that this CHOP will playback.
- Reload `reload` - Reloads the asset from the import parent.

## Parameters - Playback Page
- Use Parent Animation `useparentanim` - A toggle to specify whether to use the parent COMP animation controls or have a custom setting for this SOP.
- Animation `animation` - Specifices the animation name (if any is specified) from the importing file that this CHOP will playback.
- Shift Animation Start `shiftanimationstart` - A toggle to specify whether to shift the animation to the start of animation indicated in the importing file.
- Sample Rate Mode `sampleratemode` - ⊞ - Select between using the 'File FPS' embedded in the FBX file or setting a 'Custom' sample rate.
  * File FPS `filefps` - uses the FPS from what is defined in the importing file.
  * Custom `custom` - a desired value specified by Sample Rate parameter.

- Sample Rate `samplerate` - Set the sample rate when the "Sample Rate Mode" parameter above is set to 'Custom'.
- Play Mode `playmode` - ⊞ - A menu to specify the method used to play the animation.
  * Locked to Timeline `lockedtotimeline` - This mode locks the animation position to the timeline. The parameters Play, Speed, Index, Cue and Cue Point, are disabled in this mode since the timeline is directly tied to animation position.
  * Specify Index `specifyindex` - This mode allows the user to specify a particular index (position) in the animation using the Index parameter below. Use this mode for random access to any location in the animation.
  * Sequential `sequential` - This mode continually plays regardless of the timeline position (the Index parameter is disabled). Play, Speed, Cue, and Cue Point parameters below are enabled to allow some control. The default is set to this value.
  * Output Full Range `outputfullrange` -

- Index `index` - This parameter explicitly sets the animation position when Play Mode is set to Specify Index. The units’ menu on the right lets you specify the index in the following units: Index, Frames, Seconds, and Fraction (percentage).
- Index Unit `indexunit` - ⊞ - Specifies a unit type for Index. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -

- Play `play` - A toggle that makes the animation to play when it sets to ON. This Parameter is only available/enabled if the Sequential mode is selected from the Play Mode.
- Speed `speed` - This is a speed multiplier which only works when Play Mode is Sequential. A value of 1 is the default playback speed. A value of 2 is double speed, 0.5 is half speed and so on.
- Trim `trim` - A toggle to enable the Trim Start and Trim End parameters.
- Trim Start `tstart` - Sets an in point from the beginning of the animation, allowing you to trim the starting index of the animation. The units’ menu on the right let you specify this position by index, frames, seconds, or fraction (percentage).
- Trim Start Unit `tstartunit` - ⊞ - Specifies a unit type for Trim Start. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -

- Trim End `tend` - Sets an end point from the end of the movie, allowing you to trim the ending index of the animation. The units’ menu on the right let you specify this position by index, frames, seconds, or fraction (percentage).
- Trim End Unit `tendunit` - ⊞ - Specifies a unit type for Trim End. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -

- Cue `cue` - A toggle to jump to Cue Point when it is set to ON and it stays at that position. Only available when Play Mode is Sequential.
- Cue Pulse `cuepulse` - When pressed the animation jumps to the Cue Point and continues from that point.
- Cue Point `cuepoint` - Set any index in the animation as a point to jump to.
- Cue Point Unit `cuepointunit` - ⊞ - Specifies a unit type for Cue Point. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -

- Extend Left `textendleft` - ⊞ - Determines how the parent COMP handles animation positions that lie before the Trim Start position. For example, if Trim Start is set to 1, and the animation current index is -10, the Extend Left menu determines how the animation position is calculated.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

- Extend Right `textendright` - ⊞ - Determines how the parent COMP handles animation positions that lie after the Trim End position. For example, if Trim End is set to 20, and the animation current index is 25, the Extend Right menu determines how the animation position is calculated.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

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
Extra Information for the Import Select CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Import Select CHOP Info Channels
  * animation_length -

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
