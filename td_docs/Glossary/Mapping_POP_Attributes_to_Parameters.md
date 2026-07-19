---
url: https://docs.derivative.ca/Mapping_POP_Attributes_to_Parameters
category: Glossary
title: Mapping_POP_Attributes_to_Parameters
---

# Mapping POP Attributes to Parameters

On some parameters of some POPs, you can have a different parameter value for each point of the POP. Some POPs let you map one of its [Attributes](Attribute.md "Attribute") to a parameter via a Map page on the parameter dialog.

For example, on the [Transform POP](../POPs/Transform_POP.md "Transform POP")'s Map page, you can choose an attribute or a component of an attribute, and map the values of that attribute to a parameter, giving a different value for each point.

The Combine Operation menu lets you choose how to combine the attribute value with the parameter value you set in the OP dialog - you can Add them, Multiply them, or ignore the value in the parameter and Set it to the attribute value alone.

Using Sequential Blocks, you can map multiple attributes to multiple parameters.

Each block has a menu for possible attributes and a menu for acceptable parameters to map to. You can also get attributes from any of the inputs (`_in0` by default)

See also: [Transform POP](../POPs/Transform_POP.md "Transform POP"), [Blend POP](../POPs/Blend_POP.md "Blend POP"), [Noise POP](../POPs/Noise_POP.md "Noise POP"), [Random POP](../POPs/Random_POP.md "Random POP"), [Line Smooth POP](../POPs/Line_Smooth_POP.md "Line Smooth POP")
Mapping POP Attributes to Parameters  [![MapPOPAttributesToParameters.1.jpg](https://docs.derivative.ca/images/thumb/e/e6/MapPOPAttributesToParameters.1.jpg/300px-MapPOPAttributesToParameters.1.jpg)](https://docs.derivative.ca/File:MapPOPAttributesToParameters.1.jpg) |  [![MapPOPAttributesToParameters.2.jpg](https://docs.derivative.ca/images/thumb/1/16/MapPOPAttributesToParameters.2.jpg/300px-MapPOPAttributesToParameters.2.jpg)](https://docs.derivative.ca/File:MapPOPAttributesToParameters.2.jpg)
---|---
POPs (Point Operators) is a new [Operator Family](Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
