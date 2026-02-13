---
url: https://docs.derivative.ca/Import_Select_POP
category: POPs
title: Import_Select_POP
---

# Import Select POP
## Summary

The Import Select POP is used to import and load the geometry types primitives defined in [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") and [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP"). It essentially loads any geometry type that [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") or [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP") can support such as a Mesh, Points, NURBS Curves or Patches, Basis Curves. Each geometry represents one primitive from the loading file or it can be a set of primitives merged together for better performance. Where the geometry primitive types are not supportable by POPs, that are converted to triangles, quads, line strips and point primitives.
In [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") and [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP") if the Import Select POP renders merged geometries, an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") operator is created next to this POP which represents the original paths of primitives within/from importing file, which can be useful for user to checkout what geometry the current POP is made of.
Import Select POP can have its own animation controls within the Playback page or use the settings from its parent COMP.
The imported geometry is loaded directly to the GPU.
[importselectPOP_Class](https://docs.derivative.ca/ImportselectPOP_Class "ImportselectPOP Class")

## Parameters - General Page
- Import Parent `parent` - Specify the import parent (eg. USD/FBX COMP) to search for the asset. When no COMP is specified it will by default search in the first import parent in its path.
- Geo Path `geometry` - The geometry path from the imported file.
- Reload `reload` - Re-import and load the geometry.
- Blend Shape `blendshape` - Specifies the blend shape name (if any is specified) from the importing file that this POP will load.
- Compute Tangents `comptang` - Whether to compute tangents.

## Parameters - Playback Page
- Use Parent Animation `useparentanim` - Enable using the parent COMP animation controls
- Shift Animation Start `shiftanimationstart` - A toggle to specify whether to shift the animation to the start of animation indicated in the importing file.
- Sample Rate Mode `sampleratemode` - ⊞ - Sets the sample rate source.
  * File FPS `filefps` -
  * Custom `custom` -

- Sample Rate `samplerate` - Sets the custom sample rate.
- Play Mode `playmode` - ⊞ - Pause or play the geometry animation.
  * Locked to Timeline `lockedtotimeline` -
  * Specify Index `specifyindex` -
  * Sequential `sequential` -

- Initialize `initialize` - Resets the animation to its initial state.
- Start `start` - Start playback of animation sequence.
- Cue `cue` - ⊞ - A toggle to jump to Cue Point when it is set to ON and it stays at that position. Only available when Play Mode is Sequential.
  * Cue `cue` -
  * Cue Pulse `cuepulse` - Triggers animation jump to the Cue Point

- Cue Point `cuepoint` - ⊞ - Set any index in the animation as a point to jump to.
  * Cue Point `cuepoint` -
  * Cue Point Unit `cuepointunit` - Specifies a unit type for Cue Point

- Play `play` - Enable playback.
- Index `index` - ⊞ - This parameter explicitly sets the animation position when Play Mode is set to Specify Index. The units’ menu on the right lets you specify the index in the following units: Index, Frames, Seconds, and Fraction (percentage).
  * Index `index` -
  * Index Unit `indexunit` - Specifies a unit type for Index. Changing this will convert the previous unit to the selected unit.

- Speed `speed` - Playback speed.
- Trim `trim` - Enable the Trim Start and Trim End parameters.
- Trim Start `tstart` - ⊞ - The time to consider the starting time of 0.
  * Trim Start `tstart` -
  * Trim Start Unit `tstartunit` - Sets the trim time unit.

- Trim End `tend` - ⊞ - TTGrime the end of the animation.
  * Trim End `tend` -
  * Trim End Unit `tendunit` - Sets the trim time unit.

- Extend Left `textendleft` - ⊞ - Determines how the parent COMP handles animation positions that lie before the Trim Start position.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

- Extend Right `textendright` - ⊞ - Determines how the parent COMP handles animation positions that lie after the Trim End position.
  * Hold `hold` -
  * Cycle `cycle` -
  * Mirror `mirror` -

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the Import Select POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
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
