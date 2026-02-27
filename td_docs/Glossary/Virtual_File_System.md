---
url: https://docs.derivative.ca/Virtual_File_System
category: Glossary
title: Virtual_File_System
---

# Virtual File System

## Overview

TouchDesigner's Virtual File system (VFS) allows image, movie, audio, fonts, other media and any files to be embedded in a `.tox[](https://docs.derivative.ca/.tox ".tox")` or `.toe[](https://docs.derivative.ca/.toe ".toe")` file. You can open and read them as if they are files in the filesystem. This makes `.tox` and `.toe` files more portable if they depend on images or sounds or font files. It will of course make your `.tox` and `.toe` files larger by whatever the hard drive file size is, but one virtual file can be referred to by multiple OPs at the same time.

The palette component [virtualFile](https://docs.derivative.ca/Palette:virtualFile "Palette:virtualFile") in the Tools section lets you store virtual files without scripting.

###  Accessing Files

Internal files can be addressed directly with the `vfs:` prefix. Example: `vfs:/project1:test.jpg`. This VFS address will work in any parameter that is used to point at external files. All Operators that open files, like the [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") and [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP") allow the VFS syntax in their file parameters.

###  Details

Unlike locking a TOP where the image saved in the `.tox`/`.toe` is compressed with LZW, a Movie File In TOP that refers to a `.jpeg` file in VFS, it remains fully JPEG compressed. VFS can hold entire movie files and audio files including H.264 and `.mp3` files. It can also hold `.ttf` font files and in some circumstances, `.dll` files for the [CPlusPlus TOP](https://docs.derivative.ca/CPlusPlus_TOP "CPlusPlus TOP"), [CPlusPlus SOP](https://docs.derivative.ca/CPlusPlus_SOP "CPlusPlus SOP") and [CPlusPlus CHOP](https://docs.derivative.ca/CPlusPlus_CHOP "CPlusPlus CHOP").

Together with the [Privacy](https://docs.derivative.ca/Privacy "Privacy") option (can be set using TouchDesigner Pro only), VFS allows for additional privacy of media built into your TouchDesigner `.tox`/`.toe` files.

## Usage

Two python classes give you full access to VFS functionality.
  * [VFS Class](https://docs.derivative.ca/VFS_Class "VFS Class") - describes a COMP's virtual file system.
  * [VFSFile Class](https://docs.derivative.ca/VFSFile_Class "VFSFile Class") - describes a virtual file contained within a virtual file system.

###  Examples

See the above class wikis for full details.
Add a file from disk  |  `op('/base1').vfs.addFile('Banana.tif')`
---|---
Add an image from TOP |  `op('/base1').vfs.addByteArray(op('someTop').saveByteArray('.jpg'), 'imageName.jpg')`
Delete an image  | `op('/base1').vfs['Banana.tif'].destroy() `
Save virtual file to disk  |  `op('/base1').vfs['Banana.tif'].export('diskFolderName')`
Access virtual file in OP's file parameter (constant mode)  |  `vfs:/base1:Banana.tif`

Palette Example

Use the [virtualFile](https://docs.derivative.ca/Palette:virtualFile "Palette:virtualFile") component in the [Palette](https://docs.derivative.ca/Palette "Palette") (under `Tools`) as a user interface for VFS. This allows you to use VFS without the scripting that is otherwise required.

Lets you embed files inside a `.tox[](https://docs.derivative.ca/.tox ".tox")` or `.toe[](https://docs.derivative.ca/.toe ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.

TouchDesigner Component file, the file type used to save a [Component](https://docs.derivative.ca/Component "Component") of your TouchDesigner project.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").

A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.
