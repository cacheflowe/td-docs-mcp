---
url: https://docs.derivative.ca/FBX
category: Interoperability
title: FBX
---

# FBX

TouchDesigner imports scenes, geometry, and animation using the FBX file format from Maya, 3DS Max, Cinema4D, Houdini and others.

TouchDesigner currently uses the 2020.3.7 version of the FBX SDK.

FBX is a file format and set of libraries from [Autodesk](https://www.autodesk.com/products/fbx/overview) that is used to exchange models, animations and image/texture data between applications. TouchDesigner reads and writes FBX files and supports most of its features. See also [File Types](File_Types.md "File Types")

#####  Importing FBX

You can drag-drop a `.fbx` into a TouchDesigner network, or load it directly into an [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP"). Alternatively they can be imported via the file menu under File -> Import File...

#####  Exporting FBX

You can save [SOP](../SOPs/SOP.md "SOP") geometry to a `.fbx` file by right-clicking on any SOP and selecting 'Save Geometry...' from the menu.

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

The 3D data held in SOPs and passed for rendering by the [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP").
