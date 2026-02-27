---
url: https://docs.derivative.ca/Palette
category: Glossary
title: Palette
---

# Palette
The Palette is a collection of useful [Components](https://docs.derivative.ca/Component "Component") that you can drag-drop on to your [network](https://docs.derivative.ca/Network "Network"). It is opened/closed via the [![PaletteIcon.jpg](https://docs.derivative.ca/images/c/c0/PaletteIcon.jpg)](https://docs.derivative.ca/File:PaletteIcon.jpg) icon at the top-left of the UI.
See [Category:Palette](https://docs.derivative.ca/Category:Palette "Category:Palette") for some of the individual palette components.
[![Palette.jpg](https://docs.derivative.ca/images/thumb/7/7b/Palette.jpg/200px-Palette.jpg)](https://docs.derivative.ca/File:Palette.jpg) [![Palette.2.jpg](https://docs.derivative.ca/images/thumb/2/2b/Palette.2.jpg/205px-Palette.2.jpg)](https://docs.derivative.ca/File:Palette.2.jpg)

##  Opening the Palette Browser
The Palette Browser can be accessed:
  * by selecting Dialogs -> Palette Browser from the main menu bar.
  * by clicking on the **Open Palette** button, found to the left of the Pane Layout options, underneath the File menu.
  * use python [UI Class](https://docs.derivative.ca/UI_Class "UI Class") to open `ui.openPaletteBrowser()`

##  The Interface
Clicking on a Folder will display its in the Component section immediately below the folder section. When clicking on a Component, a preview window appears at the bottom of the interface giving you an icon preview and additional information.
##  Loading Palette Elements into TouchDesigner
To load a file from a palette, select the file from the browser and [Drag-and-Drop](https://docs.derivative.ca/Drag-and-Drop "Drag-and-Drop") it into any TouchDesigner network. In addition, the file Preview can also selected and dropped into a network.
##  Adding Items to a Palette
  * To add a component to a palette, drag the component onto a sub-folder under the "My Components" folder section.
  * To create a new sub-folder in My Components
    1. Right-click on My Components or any sub-folder under My Components.
    2. Select “Add Folder” from the contect menu.
    3. Type the name of your new folder in the dialog that comes up.

##  Removing Components or Folders from a Palette
To remove previously added components or folders, right click on it and select “Delete”.
**Note:** Items from the default Palette or that are a part of the initial creation of a personal palette can not be deleted in this way.
##  Updating a Palette
When adding files to a folder that contains a Palette, these files are not automatically loaded into the Palette structure. To have them included, right click on the folder and select "Refresh Folder". The new components will now be displayed in the Palette.
A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.
(1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](https://docs.derivative.ca/Timeline "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](https://docs.derivative.ca/Pane "Pane") and [Bookmark](https://docs.derivative.ca/Bookmark "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.
A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
