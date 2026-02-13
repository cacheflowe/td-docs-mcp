---
url: https://docs.derivative.ca/POP_to_CHOP
category: CHOPs
title: POP_to_CHOP
---

# POP to CHOP
## Summary

POP to CHOP converts POP attributes to CHOP channels.
You can choose between getting POP points, vertices or primitives attributes into the channels. When Extract is set to Points, each point becomes one sample of the channels.
You can thin out (reduce) the number of points etc using the Thin parameters: every Nth point, Start-End range, or Random thinning of points.
The format of the channel names is limited since you cannot have `()` or `[]` in channel names. The Name Format menu lets you choose between Basic: a simple CHOP-like format with lowercase letters with numbers following, or Precise format, where `()` is represented by _ and `[]` is represented by _ in a form that can be interpreted exactly by [CHOP to POP](https://docs.derivative.ca/CHOP_to_POP "CHOP to POP") when returning channels back to POPs.
If you want to preserve the type of data in POPs - floating point, integer, unsigned integer, as well as single or double precision, the Type Suffix adds a character at the end of the channel name that preserves this information. Lowercase is single precision, upper case is double precision. Matrices are named `m00`, `m01` etc.
```
f float
F double float
u unsigned int
t transform (float)
T double transform
d direction (float)
D double direction
m matrix (of any type)
c byte
b bool (of any type)

```

See also [CHOP to POP](https://docs.derivative.ca/CHOP_to_POP "CHOP to POP"), [POP to TOP](https://docs.derivative.ca/POP_to_TOP "POP to TOP"), [POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT")
[poptoCHOP_Class](https://docs.derivative.ca/PoptoCHOP_Class "PoptoCHOP Class")

## Parameters - CHOP To Page
- Active `active` -
- POP `pop` -
- Download Type `downloadtype` - ⊞ -
  * Immediate (Slow) `immediate` -
  * Next frame (Fast) `nextframe` -

- Extract `extract` - ⊞ -
  * Points `points` -
  * Vertices `vertices` -
  * Primitives `primitives` -

- Thin Out Range `thinoutrange` -
- Thin Range Start `thinrangestart` -
- Thin Range Length `thinrangelength` -
- Thin Step `thinstep` -
- Thin Random `thinrandom` -
- Thin Random Seed `thinrandomseed` -
- Name Format `nameformat` - ⊞ -
  * Basic `basic` -
  * Precise `precise` -

- Type Suffix `typesuffix` -
- Attributes Scope `attribscope` -
- Rename Scope `renscope` -
- Group `group` -
- Invert Group `invertgroup` -
- Sample Rate `rate` -

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
Extra Information for the POP to CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
