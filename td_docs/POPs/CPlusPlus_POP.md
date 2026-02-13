---
url: https://docs.derivative.ca/CPlusPlus_POP
category: POPs
title: CPlusPlus_POP
---

# CPlusPlus POP
## Summary

The CPlusPlus POP allows you to make custom POP operators by writing your own plugin using C++.
See [Write a CPlusPlus Plugin](https://docs.derivative.ca/Write_a_CPlusPlus_Plugin "Write a CPlusPlus Plugin"), [Write a CPlusPlus POP](https://docs.derivative.ca/Write_a_CPlusPlus_POP "Write a CPlusPlus POP") and the other articles in the [ C++ Category](https://docs.derivative.ca/Category:C%2B%2B "Category:C++") for more detailed information on how to make plugins for use with this node and how to access example projects.
[cplusplusPOP_Class](https://docs.derivative.ca/CplusplusPOP_Class "CplusplusPOP Class")

## Parameters - CPlusPlus Page
- Plugin Path `plugin` - The path to the plugin you want to load.
- Re-Init Class `reinit` - ⊞ - When this parameter is On, it will delete the instance of the class created by the plugin, and create a new one.
  * Re-Init Class `reinit` - When this parameter is On, it will delete the instance of the class created by the plugin, and create a new one.
  * Re-Init Class `reinitpulse` - Instantly reinitialize the class.

- Unload Plugin `unloadplugin` - When this parameter goes above 1, it will delete the instance of the class created by the plugin and unload the plugin. If multiple TOPs have loaded the same plugin they will all need to unload it to release the file.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the CPlusPlus POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
