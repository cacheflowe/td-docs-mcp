---
url: https://docs.derivative.ca/Instance
category: Glossary
title: Instance
---

# Instance

There are two kinds of Instancing in TouchDesigner:
1. Geometry instances in the [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") are copies of the geometry object, which can be transformed independently. The Geometry COMP has an **Instance** parameter page to create instances. You can have one instance for every sample of a CHOP, row of a table, pixel of an image, or point of a SOP. Transformations of the instances can be made by supplying [CHOP](https://docs.derivative.ca/CHOP "CHOP") channels with X, Y, and Z and other data, for example.
2. An instance is an [OP](https://docs.derivative.ca/Operator "Operator") that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Select OPs and Switch OPs. In this context this is a reference to another OP's data.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

(1) A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
