---
url: https://docs.derivative.ca/VFSFile_Class
category: Python
title: VFSFile_Class
---

# VFSFile Class
The VFSFile Class describes a virtual file contained within a [Virtual File System](https://docs.derivative.ca/Virtual_File_System "Virtual File System").
To access a virtual file in any operator's file parameter, use the virtual path as described below in the `virtualPath` member.

## Members
`name` → `str` :
Get or set the name of the file. This name can include slashes but should not include leading slashes.

`size` → `int` **(Read Only)** :
Get the size of the file data.

`date` → `"datetime.datetime"` **(Read Only)** :
Get the modified date of the file in the form of a datetime Python object.

`virtualPath` → `str` **(Read Only)** :
Get the virtual path of the file. Returns a String formatted for fetching the file data from VFS in operators such as the Movie File In TOP. Format is `vfs:<path to owner>:<filename>`.

`originalFilePath` → `str` **(Read Only)** :
Get the original file path on disk. If the VFSFile was created from a bytearray and not a file on disk then this will be empty.

`owner` → `OP` **(Read Only)** :
Get the OP owner.

`byteArray` → `bytearray` :
Get or set the file data as a bytearray.
## Methods
`destroy()`→ `None`:
Destroys the file in VFS referenced by this object.

`export(folder)`→ `str`:
Exports the file to the specified folder on disk and returns the location.
  * folder - The folder on disk to export the file to.

Lets you embed files inside a `.tox[](https://docs.derivative.ca/.tox ".tox")` or `.toe[](https://docs.derivative.ca/.toe ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
