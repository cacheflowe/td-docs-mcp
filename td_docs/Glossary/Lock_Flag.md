---
url: https://docs.derivative.ca/Lock_Flag
category: Glossary
title: Lock_Flag
---

# Lock Flag

If a node is locked, it will not [cook](Cook.md "Cook") and its data will not update when inputs or parameters change. The node's data is saved in the locked operator.
[![Unlocked.jpg](https://docs.derivative.ca/images/f/fa/Unlocked.jpg)](https://docs.derivative.ca/File:Unlocked.jpg) [![Locked.jpg](https://docs.derivative.ca/images/e/e4/Locked.jpg)](https://docs.derivative.ca/File:Locked.jpg)
See also [Flag](Flag.md "Flag").

##  Locking TOPs

A locked TOP saves the image inside the `.toe` file as uncompressed image data. The `.toe` file size will increase by the same amount as the locked image data size. A [.toe](.toe.md ".toe") file saved with locked TOP(s) can be opened by anyone and the image will remain in the TOP(s). For example, a locked [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") will keep the TOP image stored in the `.toe` file so it can be opened on any computer, even if the file the TOP references does not exist. If the [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") is then unlocked, the TOP will try to load the file referenced by its File parameter.

##  Locking SOPs

Locking a SOP prevents it from cooking so that manual modelling changes you make to the SOP (which can only be done fi you lock the SOP) are retained instead of updating parametrically.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
