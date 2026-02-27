---
url: https://docs.derivative.ca/Pattern_Expansion
category: Glossary
title: Pattern_Expansion
---

# Pattern Expansion

Pattern Expansion takes a short string and expands it to generate a longer string of individual elements. Example: `chan[1-3]` generates `chan1 chan2 chan3`.

[Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement") uses Pattern Expansion, along with having some of it's own syntax on-top of Pattern Expansion. Pattern Expansion is different from "[Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching")", in Pattern Expansion you are creating a list of strings, while in Pattern Matching you are looking for a pattern in a string or a set of strings.

Expansion is done by using putting the data to expand into `[]`. Valid syntax is
  * `[_alphaset_]`- Where _alphaset_ is one or more letters (not numbers), each of which will be split out into it's own result. The [a-g] format is not currently supported, the characters must be listed as [abcdefg]
  * `[_int1_-_int2_]`- Where _int1_ and _int2_ form a range of numbers. A result will be created for each number in the range.
  * `[_int1_-_int2_:_increment_]`- Similar to the previous one, but _increment_ allows for skipping numbers in the range.
  * `[_int1,int2,int3_]`- Match the specific integers given

**Note** Each expansion will be expanded against every possible other expansion in the string. So one expansion with 2 results followed by one with 3 results, will result in a final result containing 6 results. The order the numbers and ranges appear in `[]` is the order they are generated. See examples below.

###  Examples

`[tr][xyz]` | Starts expansion from right to left. Expands to `tx ty tz rx ry rz`
---|---
`chan[1-11:2]` | Starts expansion at chan1 to chan11 in increments of 2. Expands to `chan1 chan3 chan5 chan7 chan9 chan11`
`chan[1-3] pos[xyz]` | Starts expanding first term, and then the second. Expands to `chan1 chan2 chan3 posx posy posz`
Pattern expansion occurs in:
  * [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP"), [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP") and [Panel CHOP](https://docs.derivative.ca/Panel_CHOP "Panel CHOP") - where channels are renamed.
  * [Constant CHOP](https://docs.derivative.ca/Constant_CHOP "Constant CHOP"), [Noise CHOP](https://docs.derivative.ca/Noise_CHOP "Noise CHOP"), [Wave CHOP](https://docs.derivative.ca/Wave_CHOP "Wave CHOP"), [LFO CHOP](https://docs.derivative.ca/LFO_CHOP "LFO CHOP"), [Pulse CHOP](https://docs.derivative.ca/Pulse_CHOP "Pulse CHOP") and [Joystick CHOP](https://docs.derivative.ca/Joystick_CHOP "Joystick CHOP") - where channels are created using patterns.
  * [Merge DAT](https://docs.derivative.ca/Merge_DAT "Merge DAT") - where DATs are selected for merging.

**Note** : See `tdu.expand[](https://docs.derivative.ca/TDU_Class "TDU Class")()`

**Note** : To expand a list of operators that is in a parameter type that is a list of operators, see `.evalOPs()` in [Par Class](https://docs.derivative.ca/Par_Class "Par Class")

See also [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement"), [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").

Pattern Expansion takes a short string and expands it to generate a longer string of individual elements.

Matching names using wildcard characters and bracketing. Useful in "[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

Matching names using wildcard characters and bracketing. Useful in "[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.
