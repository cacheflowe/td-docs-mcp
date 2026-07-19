---
url: https://docs.derivative.ca/Trigger_CHOP
category: CHOPs
title: Trigger_CHOP
---

# Trigger CHOP

## Summary

The Trigger CHOP starts an audio-style attack/decay/sustain/release (ADSR) envelope to all trigger pulses in the input channels. A trigger point occurs whenever the first input's channel increases across the trigger threshold value. Most commonly, an ADSR starts when the input goes from 0 to 1.

**Note** : To get a channel with the full waveform, turn off the Time Slice parameter on the Common page, and don't connect an input.

The envelope consists of six major sections: delay, attack, peak, decay, sustain and release.

From the time the threshold is reached and while the channel's value is above the release threshold, the envelope is in its sustain phase during which it will delay, attack, peak-hold, decay and then maintain its sustain value.

After the inputs drops below the release threshold, the envelope start its release phase and will drop to 0.

The peak and sustain levels can be set independently, but peak value can never be less than sustain.

This CHOP works with both time-sliced inputs or with static input channels.

For jittery inputs, if you don't want it to trigger until its input has been On for some period, see the [OP Snippets](../Learn/OP_Snippets.md "OP Snippets") for the Trigger CHOP, example "trigger after a time threshold", which uses the Count CHOP.

**Note** : See examples in OP Snippets.

See also: [Timer CHOP](Timer_CHOP.md "Timer CHOP"), [Count CHOP](Count_CHOP.md "Count CHOP"), [Speed CHOP](../Glossary/Speed_CHOP.md "Speed CHOP"), [Event CHOP](Event_CHOP.md "Event CHOP")

[triggerCHOP_Class](Trigger_CHOP_Class.md "TriggerCHOP Class")

## Parameters - Trigger Page
- Release = Trigger Threshold `threshold` - If on, the trigger and release thresholds are the same value.
- Trigger Threshold `threshup` - The trigger threshold (see above).
- Release Threshold `threshdown` - The release threshold (see above).
- Re-Trigger Delay `retrigger` - ⊞ - The amount of time after a trigger point that a new trigger may occur.
  * Re-Trigger Delay `retrigger` -
  * Re-Trigger Delay Unit `retriggerunit` -
- Min Trigger Length `mintrigger` - ⊞ - The minimum amount of time that the trigger will remain active.
  * Min Trigger Length `mintrigger` -
  * Min Trigger Length Unit `mintriggerunit` -
- Trigger On `triggeron` - ⊞ - Determines whether a trigger occurs on an increasing slope or decreasing slope when passing the trigger threshold. A release will occur on the opposite slope.
  * Increasing Values `increase` -
  * Decreasing Values `decrease` -
- Multi Trigger `multitrigger` - ⊞ - When triggering mulitple envelopes, add their values together.
  * Ignore During Attack `ignore` -
  * Add `add` -
  * Restart Envelope `restart` -
- Clamp at Peak Level `clamppeak` - Clamp the additive effect of Multi-Triggers Additive at the level set in Peak Level parameter.
- Update Once per Cycle `updateonce` -
- Complete Envelope `complete` - If on, a complete envelope is produced for each trigger point. If off, the envelope may be terminated at any time by a release point.
- Remainder `remainder` - ⊞ - See Remainder Options. What to do with remaining samples at end of the interval:
  * Discard Remainder `crop` - Output interval = input interval.
  * Make Output Longer `extend` - Output longer if envelope unfinished.
  * Mix Remainder with Beginning `mix` - Add remainder to samples at the start.
- Trigger `trigger` - Instantly trigger an envelope (regardless of input).
- Release `release` - Instantly release an envelope (regardless of input).
- Reset `reset` - When On, resets the envelope, and matches the output to the input.
- Reset Pulse `resetpulse` - Instantly resets the envelope.

## Parameters - Attack Page
- Delay Length `delay` - ⊞ - The amount of time to delay the envelope after the trigger point.
  * Delay Length `delay` -
  * Delay Length Unit `delayunit` -
- Attack Length `attack` - ⊞ - The amount of rise time from zero to the peak level.
  * Attack Length `attack` -
  * Attack Length Unit `attackunit` -
- Attack Shape `ashape` - ⊞ - The shape of the attack ramp.
  * Linear `linear` -
  * Ease In `easein` -
  * Ease Out `easeout` -
  * Ease in Ease out `halfcos` -
- Peak Level `peak` - The peak level it will rise to in the attack phase.
- Peak Length `peaklen` - ⊞ - The length of time of the peak is held before going into the decay phase.
  * Peak Length `peaklen` -
  * Peak Length Unit `peaklenunit` -

## Parameters - Sustain Page
- Decay Length `decay` - ⊞ - The amount of decay time from the peak level to the sustain level.
  * Decay Length `decay` -
  * Decay Length Unit `decayunit` -
- Decay Shape `dshape` - ⊞ - The shape of the decay ramp.
  * Linear `linear` -
  * Ease In `easein` -
  * Ease Out `easeout` -
  * Ease in Ease out `halfcos` -
- Sustain Level `sustain` - The sustain level. This level is held until a release point is reached (the input goes below the threshold).
- Min Sustain Length `minsustain` - ⊞ - Set a minimum amount of time for sustain. When set to 0, sustain is simply held for as long as the input is held, but when setting a minimum time here the evelope will always include a sustain for the specified time.
  * Min Sustain Length `minsustain` -
  * Min Sustain Length Unit `minsustainunit` -
- Release Length `release` - ⊞ - The amount of release time from the sustain level to zero.
  * Release Length `release` -
  * Release Length Unit `releaseunit` -
- Release Shape `rshape` - ⊞ - The shape of the release ramp.
  * Linear `linear` -
  * Ease In `easein` -
  * Ease Out `easeout` -
  * Ease in Ease out `halfcos` -

## Parameters - Chan Page
- Channel Name `channame` - Name of channels output.
- Specify Rate `specifyrate` - Allows you to specify the sample rate in the Sample Rate parameter below.
- Enable Remap Length `enableremaplength` - Enables remapping of the total envelope to a specific length. Note that ‘held sustain’ length is not remapped, only Delay, Attack, Peak, and Release lengths are remapped.
- Remap Length `remaplength` - ⊞ - Sets the total envelope remapped length.
  * Remap Length `remaplength` -
  * Remap Length Unit `remaplengthunit` -
- Sample Rate `rate` - Sets the sample rate of the output. Only used when Specify Rate is turned on.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](../Glossary/Time_Slicing.md "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](../Glossary/Pattern_Matching.md "Pattern Matching").
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.
- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](../Glossary/Export.md "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.
- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](../Glossary/Pattern_Matching.md "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](../Glossary/Pattern_Replacement.md "Pattern Replacement").

**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`

This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.

They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.

See the [Rename CHOP](../Glossary/Rename_CHOP.md "Rename CHOP") for a further description of rename patterns.

## Operator Inputs

  * Input 0:  -

## Info CHOP Channels

Extra Information for the Trigger CHOP can be accessed via an [Info CHOP](Info_CHOP.md "Info CHOP").

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
