---
url: https://docs.derivative.ca/Folder
category: Glossary
title: Folder
---

# Folder

"Folder" in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders.

In contrast, a TouchDesigner "[Path](Network_Path.md "Network Path")" is the hierarchy of Components internal to TouchDesigner. A Path is a location of a node, which may be a component containing other nodes.

Folders and filesystem paths are found in the operators that read files, such as the [Folder DAT](../DATs/Folder_DAT.md "Folder DAT"), [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP"), [File In CHOP](../CHOPs/File_In_CHOP.md "File In CHOP"), [File In DAT](../DATs/File_In_DAT.md "File In DAT"), [Audio File In CHOP](../CHOPs/Audio_File_In_CHOP.md "Audio File In CHOP").

Filesystem files on the internet can be referred in TouchDesigner parameters by their URL: `http://www.internetplace.com/Movies/movie1.mp4[](http://www.internetplace.com/Movies/movie1.mp4)`, which downloads the file and reads from the temporary local file.

A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](Network_Path.md "Network Path").

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](Root.md "Root"). This path is displayed at the top of every [Pane](Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see Folder.
