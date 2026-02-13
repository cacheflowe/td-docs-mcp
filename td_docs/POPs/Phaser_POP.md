---
url: https://docs.derivative.ca/Phaser_POP
category: POPs
title: Phaser_POP
---

# Phaser POP
## Summary

The Phaser POP works like the [Phaser CHOP](https://docs.derivative.ca/Phaser_CHOP "Phaser CHOP"). It does staggered (time-offset) animation interpolation on a POP attribute. Phaser outputs one new attribute `Phaser`. Each point animates `Phaser` from 0 to 1 over a cycle, but each point's value rises from 0 and arrives at 1 at different times.
The new outputs attribute `Phase` can be used to blend or animate other attributes dpwnstream. `Phase` is multi-component if the input attribute is multi-component.
See also [Phaser CHOP](https://docs.derivative.ca/Phaser_CHOP "Phaser CHOP")
[phaserPOP_Class](https://docs.derivative.ca/PhaserPOP_Class "PhaserPOP Class")

## Parameters - Phaser Page
- Phase Attribute Scope `phaseattrscope` - Input attribute scope.
- Fraction `fract` - Sets the phase fraction.
- Parameter Size `parsize` - ⊞ - Number of independent configurable parameter values.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Edge `edge` - Set the separation edge of the phasing between two states
- Reverse Phase `reversephase` - Reverse the staggered animation interpolation.
- Smooth Step `smoothstep` - Enable value remapping with a smoothstep function.
- Cast to `castto` - ⊞ - Allows to cast the output attribute to a different type if wanted.
  * Automatic `auto` -
  * Float `float` -
  * Int `int` -

- Output Attribute Scope `outputattrscope` - ⊞ - Name of attribute to output (can choose components of attribute), can choose from menu.
  * P `P` -
  * N `N` -
  * Color `Color` -
  * Color.rgb `Color.rgb` -
  * Tex `Tex` -
  * PointScale `PointScale` -
  * LineWidth `LineWidth` -

- Override Automatic Attribute `overrideautoattr` - Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute.
- Attribute Type `attrtype` - ⊞ - The output attribute's data type, default float.
  * float `float` -
  * double `double` -
  * int `int` -
  * uint `uint` -
  * Color `color` -
  * Color (double) `dcolor` -
  * Direction `dir` -
  * Direction (double) `ddir` -

- Components `attrnumcomps` - ⊞ - The number of components in the new custom attribute.
  * 1 `1` -
  * 2 `2` -
  * 3 `3` -
  * 4 `4` -

- Default Value `attrdefaultval` - ⊞ - Default values of the output attribute components if they cannot be computed.
  * Default Value `attrdefaultval0` - Default value(s) of the attribute.
  * Default Value `attrdefaultval1` - Default value(s) of the attribute.
  * Default Value `attrdefaultval2` - Default value(s) of the attribute.
  * Default Value `attrdefaultval3` - Default value(s) of the attribute.

- Attribute Class `attrclass` - ⊞ - Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable.
  * Point `point` -
  * Vertex `vertex` -
  * Primitive `primitive` -

- From Low `fromlow` - Reranges the phase attribute value.
- From High `fromhigh` - Reranges the phase attribute value.
- To Low `tolow` - Sets low value on the output range.
- To High `tohigh` - Sets high value on the output range.
## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Phaser POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
