---
url: https://docs.derivative.ca/Pattern_Replacement
category: Glossary
title: Pattern_Replacement
---

# Pattern Replacement

Pattern Replacement takes place in a 2nd parameter after certain [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") parameters, for example in the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP"). It builds up the new names to replace the matched names using both the features of [Pattern Expansion](https://docs.derivative.ca/Pattern_Expansion "Pattern Expansion"), as well as extra syntax specific to Pattern Replacement. The extra syntax allows for pulling out wildcards matched during the Pattern Matching.

The synxtax is either a `*` or a `?`, followed by (_wildcardIndex_). Where _wildcardIndex_ is an integer which is the index of the wildcard in the Pattern Matching parameter. For example if there are three `*` wildcards, you would reference them using `*(0) *(1)` and `*(2)`. Similarly if there are 2 `?` wildcard, they would be referenced using `?(0)` and `?(1)`.

For example if a CHOP has 3 channels named
```
 left_side_monitor
 right_side_projector
 top_side_led
```

And the 'Rename From' has
```
 *_side_*
```

as it's entry. You can pull out what was matched by the first * and the second * by using *(0) and *(1).

A pattern replacement of
```
 *(1)_floor_*(0)
```

Will result in the channel names
```
 monitor_floor_left
 projector_floor_right
 led_floor_top
```

Pattern Replacement occurs in:

[Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP"), [Select CHOP](https://docs.derivative.ca/Select_CHOP "Select CHOP"), [File In CHOP](https://docs.derivative.ca/File_In_CHOP "File In CHOP"), [Parameter CHOP](https://docs.derivative.ca/Parameter_CHOP "Parameter CHOP")

See also [Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP") where you can re-create channel names.

Used in conjunction with Pattern Matching to replace all or portions of matched strings with new data. Used in places such as the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP").

Matching names using wildcard characters and bracketing. Useful in "[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

Matching names using wildcard characters and bracketing. Useful in "[Select](https://docs.derivative.ca/Select_CHOP "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
