---
url: https://docs.derivative.ca/Network_Path
category: Glossary
title: Network_Path
---

# Network Path
Every node has a **network path** or **path**. The path is the location of an [operator](https://docs.derivative.ca/Operator "Operator") within the [Hierarchy](https://docs.derivative.ca/Hierarchy "Hierarchy") of a TouchDesigner project. For example, `/geo1/circle1`, is a node called `circle1` in a component called `geo1`. The path `/` is called Root or Home. [Components](https://docs.derivative.ca/Component "Component") are used to create another level in the path, slike folders/directories do for the file paths on your computer.
Example: The path of a node `text1` is `/project1/container1/button2/text1`. All nodes in the path up the last node in a path are Components. That is, `project1`, `container1` and `button2` are all components.
If a path starts with `/`, it is an "absolute path", which refers back to the top root of the heirarchy. Example: `/project1/wave1`.
If you refer to another node is in the same network, you can just put the node name: `text1` or `button1/out1`. This is a "relative path".
If you are in `/project1/container1/button2`, the "parent node" is `/project1/container1`. You can refer to another node in `/project1/container1` using the "`..`" form: `../button3`, where `..` means "my parent". `../button3` is a "relative path".
Network path does not refer to location of a TouchDesigner file in the Windows file system. The network path of the currently selected operator is located at the top of every [pane](https://docs.derivative.ca/Pane "Pane") in TouchDesigner. The highest level of a TouchDesigner network is indicated by a ' **`/`**' and is called the**root** of the network.
You can navigate up and down the network hierarchy by using the mouse's roller wheel, the Enter and "i" keys, or left-clicking on the network path at the top of the pane. Clicking on the lowest level of the current path will show a drop down list of available child Components that may be selected. To navigate up the hierarchy, use the roller wheel, the "u" key, or select the appropriate ' `/` ' in the path to navigate to that level.
####  Where you will find Paths
At the top of every [Network Editor](https://docs.derivative.ca/Network_Editor "Network Editor") you see a path of the component whose network you are looking at.
Operators often have a path parameter, like the [Select TOP](https://docs.derivative.ca/Select_TOP "Select TOP"), which allows it to get an image from any network.
Any parameter can have a Python expression that contains paths.
Paths are found in Python scripts and callbacks are contained in DATs, typically a [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT").
You may see an expression `op('wave1')['chan1']`, which is a channel called `chan1` in the CHOP called `wave1`.
You may see an expression `op('/project1/effect/transform1').par.tx`, which is the `tx` parameter of the `transform1` node.
The [OP Find DAT](https://docs.derivative.ca/OP_Find_DAT "OP Find DAT") outputs a table of paths.
In exporting you will see the path to a parameter: `transform:tx` This is the `tx` parameter of a Transform TOP.
####  See Also
* * *
  * [Folder](https://docs.derivative.ca/Folder "Folder")
  * [Bookmarks](https://docs.derivative.ca/Bookmark "Bookmark")

TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The Network Path or Path for root is simply `/`. A typical path is `/project1/moviein1`.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
