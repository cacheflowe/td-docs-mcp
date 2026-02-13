---
url: https://docs.derivative.ca/Audio_VST_CHOP
category: CHOPs
title: Audio_VST_CHOP
---

# Audio VST CHOP
## Summary

The Audio VST CHOP loads VST3 Plugin files that generate (instruments) or process (filter) audio. See the [VST](https://docs.derivative.ca/VST "VST") overview.
The plugin's parameters can be exposed and driven bi-directionally via a corresponding TouchDesigner parameter or the plugin's GUI control. In order to get the full benefit of the bidirectional nature of the plugin parameters it is recommended to use [Binding](https://docs.derivative.ca/Binding "Binding") or a [Bind CHOP](https://docs.derivative.ca/Bind_CHOP "Bind CHOP") when driving the parameter in TouchDesigner, rather than an expression or CHOP reference.
Python calls let you [send MIDI messages](https://docs.derivative.ca/AudiovstCHOP_Class "AudiovstCHOP Class") to the plugin. And if the plugin generates MIDI, you can get and process the messages in the [docked](https://docs.derivative.ca/Docking "Docking") callbacks DAT.
Depending on the plugin, the Audio VST CHOP takes up to 4 multi-channel inputs.
See the discussion on which VST plugins work well with TouchDesigner - [VST Plugin Testing](https://derivative.ca/community-post/vst-plugin-testing/65712). Also for a selection of free VSTs along with a useful set of affordable upgraded versions go here: <https://hy-plugins.com>.
2 Free HY-Plugins are included with TouchDesigner and can be found using the Help > Browse Samples menu. This will open a file browser to the TouchDesigner application Samples folder which contains a VST3 folder holding one synthesizer and filter plugin for both Windows and MacOS. The Windows VST3 plugin files can be distinguished by their included "64 Bit" string.
Installed VST plugins are found in `C:Program Files/Common Files/VST` on Windows, and be `/Library/Audio/Plug-Ins/VST3` on macOS.
**Tip** : You can get detailed info about the VST plugin by attaching an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") to the CHOP.
[VST](https://docs.derivative.ca/VST "VST") is a trademark of Steinberg Media Technologies GmbH, registered in Europe and other countries.
[audiovstCHOP_Class](https://docs.derivative.ca/AudiovstCHOP_Class "AudiovstCHOP Class")

## Parameters - VST Page
- File `file` - The path to the VST3 plugin. Default install location for VST3 plugins is `C:/Program Files/Common Files/VST3` on Windows and `/Library/Audio/Plug-Ins/VST3` on macOS.
- Reload `reloadpulse` - Reloads the VST3 plugin. Pulsing will clear all learned parameters and reset the GUI, as well as any stashed plugin data. Basically, it resets the plugin to a default state.
- Load Plugin State on Start `loadpluginstate` - The plugin state (including preset value and other UI elements) is saved into the toe file and is restored on TouchDesigner start, if enabled. The toggle exists to provide a work-around to plugins that do not behave well (eg. crash) when their plugin state is set; the toggle should be disabled in those cases.
- Sample Rate `rate` - Sets the sample rate of the VST3 plugin.
- Plugin GUI Always on Top `alwaysontop` - When enabled, the plugin window will always be on top of other windows.
- Display Plugin GUI `displaygui` - When pulsed, will open the plugin GUI in a separate window. Changing a parameter in the plugin GUI while the learn toggle is enabled will create the parameter on the Audio VST CHOP side.
- Learn Parameters `learnparms` - When enabled, parameters that are interacted with in the VST Plugin window will be created as parameters on the Plugin page, ie. they will be learned.
- Regular Parameters `regularparms` - When enabled, every Plugin parameter will be created on the Plugin page.
- Read-Only Parameters `readonlyparms` - When enabled, all read-only Plugin parameters will be created on the Plugin page. If Regular Parameters is also toggled on then this toggle will have no effect.
- Clear Learned Parameters `clearlearnedparms` - When pulsed, all learned parameters will be cleared. If neither Regular or Read-only parameters are toggled on then the parameters will be destroyed.
- Callbacks DAT `callbacks` - Reference to the DAT containing Audio VST CHOP supported callbacks.

## Parameters - Bus Layout Page
- Custom Bus Layout `custombuslayout` - Enables custom bus layout. If disabled the bus layout will be the plugin's default.
- Output Bus Layout `outputbuslayout` - Select the output bus layout (ie. number of channels) of the output bus. This will directly affect how many channels the Audio VST CHOP has.
- Main Input Bus Layout `maininputlayout` - Select the main input bus layout (ie. number of channels). The main input bus is always the CHOP's first input, and this selection determines how many channels it accepts from it.
- Aux Input `aux` - This sequence describes the aux inputs to the VST plugin
- Enable `aux0enable` - Enable the auxiliary bus.
- Bus Layout `aux0layout` - Select the auxiliary bus layout (ie. number of channels) for the auxiliary input. An auxiliary input is every input after the main input. Not every plugin will support auxiliary buses, and the parameter will be disabled if not supported. If no more sequential auxiliary buses can be added (ie. the +/- disappears in the parameter sequence) then that means the auxiliary bus maximum has been reached.

## Parameters - Playhead Page
- Custom Playhead `customplayhead` - Enable the custom playhead. When disabled, the plugin will always sequentially step forward in time. Not all plugins support a custom playhead.
- Timecode Object/CHOP/DAT `timecodeop` - Specifies the playhead time of the plugin. A reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") object.
- Tempo (bpm) `tempo` - The tempo of the playhead. Not all plugins support changing of the tempo via the playhead.
- Signature `signature` - ⊞ - The time signature of the playhead. Not all plugins support changing of the time signature via the playhead.
  * Signature `signature1` -
  * Signature `signature2` -

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.
## Info CHOP Channels
Extra Information for the Audio VST CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
