---
url: https://docs.derivative.ca/Render_Flag
category: Glossary
title: Render_Flag
---

# Render Flag

The Render Flag is a [flag](Flag.md "Flag") on all SOP nodes and on all Geometry components that is used to select the SOP for rendering by the [Render TOP](../TOPs/Render_TOP.md "Render TOP").

In order for the object to be rendered by the Render TOP:
  * the SOP's Render flag must be set.
  * the Geometry component that contains the SOP must have its Render flag set.
  * the Geometry component that contains the SOP must be specified in the Render TOP's "Geometry" parameter.

See also: [Flag](Flag.md "Flag") and [Display Flag](Display_Flag.md "Display Flag").

The purple flag on COMP and SOP nodes that determines if the node will be rendered in a [Render TOP](../TOPs/Render_TOP.md "Render TOP") or [Render Pass TOP](../TOPs/Render_Pass_TOP.md "Render Pass TOP"). The operator must also be listed in the Render / Render Pass TOP's 'Geometry' parameter.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](Geometry_COMP.md "Geometry COMP").
