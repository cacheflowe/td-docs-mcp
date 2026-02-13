---
url: https://docs.derivative.ca/Pane_Class
category: Python
title: Pane_Class
---

# Pane Class
The Pane class describes an instance of a [pane](https://docs.derivative.ca/Pane "Pane") interface. It can be accessed through the [ui.panes](https://docs.derivative.ca/Panes_Class "Panes Class") object. It is the parent class of the [NetworkEditor Class](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class").

## Members
`owner` → `COMP` :
Get or set the [component](https://docs.derivative.ca/COMP_Class "COMP Class") this pane points to.

`id` → `int` **(Read Only)** :
A unique numeric identifier.

`link` → `int` :
Get or set the numeric link index.

`enable` → `bool` :
Get or set mouse and keyboard interactivity on the pane.

`maximize` → `bool` :
Enable or disable the pane maximize state.

`name` → `str` :
Get or set the pane name.

`ratio` → `float` :
Get or set the split proportion of the pane, if the pane was previously split.

`bottomLeft` → `Coords` **(Read Only)** :
The coordinates of the bottom left corner, expressed as both x/y and u/v in a named tuple.

`topRight` → `Coords` **(Read Only)** :
The coordinates of the top right corner, expressed as both x/y and u/v in a named tuple.

`open` → `bool` **(Read Only)** :
Returns True if the Pane is currently open.

`type` → `PaneType` **(Read Only)** :
The enumerated type of the pane. Example: NetworkEditor.
The enumeration is called PaneType and consists of:
  * PaneType.NETWORKEDITOR
  * PaneType.PANEL
  * PaneType.GEOMETRYVIEWER
  * PaneType.TOPVIEWER
  * PaneType.CHOPVIEWER
  * PaneType.ANIMATIONEDITOR
  * PaneType.PARAMETERS
  * PaneType.TEXTPORT

## Methods
`changeType(paneType)`→ `td.Pane`:
Change the pane to the specified type. Will return a new Pane object that represents the Pane. After being called, the current Pane instance will no longer be valid.
  * paneType - The type of pane to change this pane to.

```
p = ui.panes[0]
p = p.changeType(PaneType.TOPVIEWER)  # note: must re-assign p to new object.

```

`close()`→ `None`:
Close the pane.

`floatingCopy()`→ `td.Pane`:
Return a floating copy of the pane.

`splitBottom()`→ `td.Pane`:
Split the bottom portion of the pane into a new pane.

`splitLeft()`→ `td.Pane`:
Split the left portion of the pane into a new pane.

`splitRight()`→ `td.Pane`:
Split the right portion of the pane into a new pane.

`splitTop()`→ `td.Pane`:
Split the top portion of the pane into a new pane.

`tearAway()`→ `bool`:
Detach the pane into a floating window. Returns True if successful.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
A work area in TouchDesigner's layout that includes the [Network Editor](https://docs.derivative.ca/Network_Editor "Network Editor") and 7 other pane types used for different tasks. The TouchDesigner interface can consist of a single pane, or be split into multiple panes.
