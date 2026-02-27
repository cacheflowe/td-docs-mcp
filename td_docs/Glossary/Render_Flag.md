---
url: https://docs.derivative.ca/Render_Flag
category: Glossary
title: Render_Flag
---

# Render Flag

The Render Flag is a [flag](https://docs.derivative.ca/Flag "Flag") on all SOP nodes and on all Geometry components that is used to select the SOP for rendering by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP").

In order for the object to be rendered by the Render TOP:
  * the SOP's Render flag must be set.
  * the Geometry component that contains the SOP must have its Render flag set.
  * the Geometry component that contains the SOP must be specified in the Render TOP's "Geometry" parameter.

See also: [Flag](https://docs.derivative.ca/Flag "Flag") and [Display Flag](https://docs.derivative.ca/Display_Flag "Display Flag").

The purple flag on COMP and SOP nodes that determines if the node will be rendered in a [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or [Render Pass TOP](https://docs.derivative.ca/Render_Pass_TOP "Render Pass TOP"). The operator must also be listed in the Render / Render Pass TOP's 'Geometry' parameter.

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP").
