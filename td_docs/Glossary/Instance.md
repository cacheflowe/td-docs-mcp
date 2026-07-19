---
url: https://docs.derivative.ca/Instance
category: Glossary
title: Instance
---

# Instance

There are two kinds of Instancing in TouchDesigner:
1. Geometry instances in the [Geometry Component](Geometry_COMP.md "Geometry COMP") are copies of the geometry object, which can be transformed independently. The Geometry COMP has an **Instance** parameter page to create instances. You can have one instance for every sample of a CHOP, row of a table, pixel of an image, or point of a SOP. Transformations of the instances can be made by supplying [CHOP](CHOP.md "CHOP") channels with X, Y, and Z and other data, for example.
2. An instance is an [OP](../General/Operator.md "Operator") that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Select OPs and Switch OPs. In this context this is a reference to another OP's data.
An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

(1) A [Geometry Component](Geometry_COMP.md "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").
