---
url: https://docs.derivative.ca/Null_POP
category: POPs
title: Null_POP
---

# Null POP
## Summary

The Null POP does nothing - it passes its input to its output unchanged. It does not consume any CPU or GPU memory.
It is used as a placeholder, and it is best practice while you are working on building a chain of POPs, to put a Null POP at the end, name it something meaningful, and then refer to the Null POP farther downstream, so you can add in new POPs in the chain and not have to think about where the Null is connected.
Note that POPs in general will not consume any memory for attributes that are unchanged by a POP. For example if the input to a Math POP has `P`, `Tex` and `Color` attributes, and the Math POP affect only the `Color` attribute, it will not copy the memory for the `P` and `Tex` attributes - it will "point to" or retrieve `P` and `Tex` from whichever POP they were last modified or created. The popup info (on the middle-click button) on a POP shows which attributes are references (have a `(r)` beside them).
[nullPOP_Class](https://docs.derivative.ca/NullPOP_Class "NullPOP Class")

## Parameters - Null Page
- Bypass `bypass` -

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Null POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
