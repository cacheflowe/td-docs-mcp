---
url: https://docs.derivative.ca/Parameter_CHOP
category: CHOPs
title: Parameter_CHOP
---

# Parameter CHOP
## Summary

The Parameter CHOP gets parameter values, including custom parameters, from all OP types.
(This replaces the Fetch CHOP.)
Retrieve from parameters alternatively using a `node.par.Customname` expression of the [Par Class](https://docs.derivative.ca/Par_Class "Par Class"), or the [Parameter Execute DAT](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT").
See the [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP") for retrieving channels from the output of other CHOPs.
[parameterCHOP_Class](https://docs.derivative.ca/ParameterCHOP_Class "ParameterCHOP Class")

## Parameters - Source Page
- Operators `ops` - The operators determine where to obtain the channels. Specify or more operator names or paths. Examples: `wave1`, `slider*`, `constant[1-9] constant[10-19:2]`, `../base1`. Or select the operators using the menu.
- Fetch `fetch` - ⊞ - Pick between fetching Parameters or Sequences.
  * Parameters `partypes` - When set to Parameters, use the ParGroups and Parameters parameters to pick.
  * Sequences `sequencetypes` - When set to Sequences, use the Sequences parameter to pick which sequences to look at. Then use the ParGroups and Parameters parameters to pick from within the selected sequences.

- Sequences `sequences` - The list of sequence names (which can include wildcards) you want to get from the OP(s). Used by the Parameters and ParGroups parameters to select from within the picked sequences. One or more sequence, or * for all sequences. You can also specify a "NOT" selection with an `^`. Or select the sequences using the menu. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching"). Only enabled if Fetch menu option is set to Sequences
If the number of blocks of the selected sequences is more than one, the channel will become multisample, each index representing the block index. If multiple sequences of varying block lengths are selected, then HOLD mode will apply to the sequences with lesser block length.
- ParGroups `pargroups` - The list of pargroup names (which can include wildcards) you want to get from the OP(s). One or more pargroups, or * for all pargroups. You can also specify a "NOT" selection with an `^`. Or select the pargroup using the menu. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Parameter `parameter` - The list of parameters names (which can include wildcards) you want to get from the OP(s). One or more parameter, or * for all parameters. You can also specify a "NOT" selection with an `^`. Or select the parameter using the menu. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Custom `custom` - Output the operators' custom parameters.
- Built-In `builtin` - Output the operators' built-in parameters.
- Name Format `nameformat` - ⊞ - Channels can be named suitably for multi-exporting. See [CHOP_Export](https://docs.derivative.ca/CHOP_Export "CHOP Export").
  * Parameter Name `parameter` -
  * OP and Parameter Names `op` -
  * Full Path Name `path` -

- Rename from `renamefrom` - See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `renameto` - See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").

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
