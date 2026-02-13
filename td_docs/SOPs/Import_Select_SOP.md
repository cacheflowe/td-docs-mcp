---
url: https://docs.derivative.ca/Import_Select_SOP
category: SOPs
title: Import_Select_SOP
---

# Import Select SOP
## Summary

The Import Select SOP is used to import and load the geometry types primitives defined in [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") and [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP"). It essentially loads any geometry type that [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") or [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP") can support such as a Mesh, Points, NURBS Curves or Patches, Basis Curves. Each geometry represents one primitive from the loading file or it can be a set of primitives merged together for better performance.
In [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") and [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP") if the Import Select SOP renders merged geometries, an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") operator is created next to this SOP which represents the original paths of primitives within/from importing file, which can be useful for user to checkout what geometry the current SOP is made of. Import Select SOP can have its own animation controls within the Playback page or use the settings from its parent COMP.
The imported geometry can be loaded directly from GPU or CPU, depending on whether the Straight To GPU toggle is set to ON or not at the parent COMP node.
[importselectSOP_Class](https://docs.derivative.ca/ImportselectSOP_Class "ImportselectSOP Class")

## Parameters - General Page
- Import Parent `parent` - Specify the import parent (eg. USD/FBX COMP) to search for the asset. When no COMP is specified it will by default search in the first import parent in its path.
- Geo Path `geometry` - The geometry path from the imported file.
- Reload `reload` - Reloads the asset from the import parent.
- Compute Tangents `comptang` - A toggle to compute the tangents for this SOP.
## Parameters - Playback Page
- Use Parent Animation `useparentanim` - A toggle to specify whether to use the parent COMP animation controls or have a custom setting for this SOP.
- Shift Animation Start `shiftanimationstart` - A toggle to specify whether to shift the animation to the start of animation indicated in the importing file.
- Sample Rate Mode `sampleratemode` - ⊞ - A menu to choose between the FPS or use a custom sample rate.
  * File FPS `filefps` - uses the FPS from what is defined in the importing file.
  * Custom `custom` - a desired value specified by Sample Rate parameter.

- Sample Rate `samplerate` - It is used to specify the sample rate (FPS) for the animation. This parameter is disabled by default and can be enabled once the Custom option is selected from the Sample Rate Menu.
- Play Mode `playmode` - ⊞ - A menu to specify the method used to play the animation.
  * Locked to Timeline `lockedtotimeline` - This mode locks the animation position to the timeline. The parameters Play, Speed, Index, Cue and Cue Point, are disabled in this mode since the timeline is directly tied to animation position.
  * Specify Index `specifyindex` - This mode allows the user to specify a particular index (position) in the animation using the Index parameter below. Use this mode for random access to any location in the animation.
  * Sequential `sequential` - This mode continually plays regardless of the timeline position (the Index parameter is disabled). Play, Speed, Cue, and Cue Point parameters below are enabled to allow some control. The default is set to this value.

- Initialize `initialize` - Resets the animation to its initial state.
- Start `start` - Resets the animation to its initial state and starts playback.
- Cue `cue` - A toggle to jump to Cue Point when it is set to ON and it stays at that position. Only available when Play Mode is Sequential.
- Cue Pulse `cuepulse` - When pressed the animation jumps to the Cue Point and continues from that point.
- Cue Point `cuepoint` - Set any index in the animation as a point to jump to.
- Cue Point Unit `cuepointunit` - ⊞ - Specifies a unit type for Cue Point. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -

- Play `play` - A toggle that makes the animation to play when it sets to ON. This Parameter is only available/enabled if the Sequential mode is selected from the Play Mode.
- Index `index` - This parameter explicitly sets the animation position when Play Mode is set to Specify Index. The units’ menu on the right lets you specify the index in the following units: Index, Frames, Seconds, and Fraction (percentage).
- Index Unit `indexunit` - ⊞ - Specifies a unit type for Index. Changing this will convert the previous unit to the selected unit.
  * Frames `frames` -
  * Seconds `seconds` -
  * Fraction `fraction` -
  * Index `indices` -

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

- Extend Left `textendleft` - ⊞ - Determines how the parent COMP handles animation positions that lie before the Trim Start position. For example, if Trim Start is set to 1, and the animation current index is -10, the Extend Left menu determines how the animation position is calculated.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

- Extend Right `textendright` - ⊞ - Determines how the parent COMP handles animation positions that lie after the Trim End position. For example, if Trim End is set to 20, and the animation current index is 25, the Extend Right menu determines how the animation position is calculated.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

## Info CHOP Channels
Extra Information for the Import Select SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Import Select SOP Info Channels
  * true_start_time -

  * true_end_time -

###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
