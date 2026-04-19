---
url: https://docs.derivative.ca/POP_Topology
category: Glossary
title: POP_Topology
---

# POP Topology

POP Topology is the relationship between geometric entities making up POPs, and refers to the POP's [Primitives](https://docs.derivative.ca/Primitive "Primitive"), the [ Vertex / Vertices](https://docs.derivative.ca/Vertex "Vertex") of each Primitive, and the [Points](https://docs.derivative.ca/Point "Point") list that the Vertices refer to.

For certain POPs operations:
  * The number of resulting points is only known on the GPU. The resulting POP will have “Point Count Info on GPU” instead of “Point Count Info on CPU” in the info popup (examples: [Facet POP](https://docs.derivative.ca/Facet_POP "Facet POP"): Cusp and Consolidate operation…)
  * The number of resulting vertices and primitives (Topology Info) is only known on the GPU. The resulting POP will have “Topology Info on GPU” instead of “Topology Info on CPU” in the info popup (example [Convert POP](https://docs.derivative.ca/Convert_POP "Convert POP"): open or close line strips)
  * Both the point count and the topology info are only known on the GPU. In that case the resulting POPs will have “Point Count Info on GPU” and “Topology Info on GPU” in the info popup (example [Delete POP](https://docs.derivative.ca/Delete_POP "Delete POP"))


For the points and/or topology of these POPs, the memory allocated is the maximum memory the POP could use. Downloading the actual point count and topology info (number of primitives and vertices) for these POPs from the GPU causes a stall.

For the downstream POPs compute shaders, the point count info and the topology info are passed through buffers to avoid the stall and unnecessary work: this is called indirect dispatch of compute shaders. Additional command buffers have to be filled for these dispatches, which make them a bit more expansive than regular dispatches.

The middle click info popup does the download and shows what is used versus what is allocated.

Some OPs ([POP to DAT](https://docs.derivative.ca/POP_to_DAT "POP to DAT"), [POP to SOP](https://docs.derivative.ca/POP_to_SOP "POP to SOP"), [POP to CHOP](https://docs.derivative.ca/POP_to_CHOP "POP to CHOP")) as well as the python functions allow a “next frame” asynchronous download that prevents the stall but introduces a 1 frame latency. The "Copy topology back to CPU" parameter on certain POPs turns the POP back into a regular POP, only allocating necessary memory again downstream. This is also a mode found on the Convert POP.

The [Topology POP](https://docs.derivative.ca/Topology_POP "Topology POP") allows you to manually allocate memory for POPs with info on the GPU, so some unused memory can be reclaimed without a stall, or to manually set the point count info and topology info on the CPU when it is known, turning the POP back into a "regular" POP without incurring a stall.

The [Feedback POP](https://docs.derivative.ca/Feedback_POP "Feedback POP") has a toggle to limit the memory allocated to a multiple of the input memory to prevent the memory used from blowing up when geometry is created inside the feedback loop. This can also be accomplish with the Topology POP which has more features and gives finer control.

POP Topology refers to the [Primitives](https://docs.derivative.ca/Primitive "Primitive") of POPs, and the [Vertices](https://docs.derivative.ca/Vertex "Vertex") of each Primitive, and the [Points](https://docs.derivative.ca/Point "Point") list of a POP that the Vertices refer to.

POPs (Point Operators) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

A surface type in [POPs](https://docs.derivative.ca/POP "POP") and [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").

A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

POP Topology refers to the [Primitives](https://docs.derivative.ca/Primitive "Primitive") of POPs, and the [Vertices](https://docs.derivative.ca/Vertex "Vertex") of each Primitive, and the [Points](https://docs.derivative.ca/Point "Point") list of a POP that the Vertices refer to.
