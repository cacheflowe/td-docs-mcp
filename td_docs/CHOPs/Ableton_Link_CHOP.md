---
url: https://docs.derivative.ca/Ableton_Link_CHOP
category: CHOPs
title: Ableton_Link_CHOP
---

# Ableton Link CHOP
## Summary

The Ableton Link CHOP retrieves timing information from an Ableton Link supported network. For more information see: <http://www.ableton.com/en/link/>
The full support of the Ableton Live system is [TDAbleton](https://docs.derivative.ca/TDAbleton "TDAbleton"), a group of components that give you access to Ableton Songs, Tracks, Chains, Parameters and MIDI.
Ableton's Link FAQ is very helpful for issues on the Ableton end: <https://help.ableton.com/hc/en-us/articles/209776125-Link-FAQs>.
One common problem is that Ableton Link doesn't work with all sound drivers, including DirectX. The free application [ASIO4All](http://www.asio4all.com/) is an easy replacement that acts as a virtual ASIO device.
See also [Ableton](https://docs.derivative.ca/Ableton "Ableton").
[abletonlinkCHOP_Class](https://docs.derivative.ca/AbletonlinkCHOP_Class "AbletonlinkCHOP Class")

## Parameters - Ableton Page
- Active `active` - Turns the CHOP's output on or off.
- Enable `enable` - Initializes the connection to the Ableton Link session.
- Start Stop Sync Enable `startstopsync` - Enables start stop synchronization for the entire Ableton Link session. Start stop synchronization allows for sharing of start or stop signals between subgroups of peers in a Link session.
- Signature `signature` - ⊞ - Specifies the time signature. The first number is the number of beats per measure and the second number indicates the type of note that constitutes one beat. See [Time Signature - Wikipedia](http://en.wikipedia.org/wiki/Time_signature) for additional information.
  * `signature1` -
  * `signature2` -

- Callbacks DAT `callbacks` - Path to a DAT containing callbacks for each event received.

## Parameters - Output Page
- Status Channels `status` - Enables the following status channels
  * numpeers - number of Ableton Link enabled devices or app found on the network.
  * linked - if the Ableton Link CHOP is connected to the Link network.
  * waiting - if the Ableton Link CHOP is in a waiting state and not synced.
  * synced - if the Ableton Link CHOP has synced with the Link network.

- Ramp `ramp` - Outputs a 0-1 ramp each bar.
- Pulse `pulse` - Outputs a pulse each bar.
- Sine `sine` - Outputs a sine wave each bar.
- Count `count` - Increases the count each bar.
- Count+Ramp `countramp` - A ramp that counts up until the bar is reset.
- Bar `bar` - Output the current bar.
- Beat `beat` - Output the current beat.
- Sixteenths `sixteenths` - Output the current sixteenths.
- Ramp Bar `rampbar` - Outputs a 0-1 ramp each bar.
- Ramp Beat `rampbeat` - Outputs a 0-1 ramp each beat.
- Tempo `tempo` - Outputs the current tempo (also known as BPM).
- Beats `beats` - Outputs the total number of beats.
- Phase `phase` - Outputs the current phase in the bar.

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
Extra Information for the Ableton Link CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Ableton Link CHOP Info Channels
  * ableton_link_clock -

  * ableton_td_clock -

  * ableton_clock_adjust_count -

  * ableton_clock_diff -

  * ableton_max_clock_diff -

  * ableton_clock_diff_to_adjust -

  * ableton_time_behind_link -

  * ableton_lost_time -

  * ableton_startstop_sync_enable -

  * ableton_is_playing -

  * ableton_tempo -

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
