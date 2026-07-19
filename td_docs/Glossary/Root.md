---
url: https://docs.derivative.ca/Root
category: Glossary
title: Root
---

# Root

TouchDesigner is a hierarchy of components. "Root" is the top-most network in the hierarchy. The [Network Path](Network_Path.md "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.

Normally you work in components under `/`, like in `/project1`, but you can put all you want in `/`.

Root also contains `/local`, which contains things line MIDI settings, [Layout](Layout.md "Layout"), python modules that are accessible from anywhere, and [Variables](https://docs.derivative.ca/Variables "Variables"). `/local` is saved intact in the `.toe` file, and is reloaded from the `.toe` on restart. Parts of `/local` are controlled via dialogs like the MIDI mapper, but given a lot of `/local` is text files and tables, most things can be edited manually by the user.

Other things that are commonly put in Root:
  * startup scripts (use [Execute DAT](../DATs/Execute_DAT.md "Execute DAT"))
  * [Window Components](Window_COMP.md "Window COMP") to manage outputs to monitors
  * [Audio Device Out CHOPs](../Interoperability/Audio_Device_Out_CHOP.md "Audio Device Out CHOP") to output to audio devices from one place, if that is desired.
  * common libraries, components and scripts that you want to be accessible to all your parts of your project.

Root is actually a [Base COMP](../COMPs/Base_COMP.md "Base COMP"). See if you can find a way to display its parameter dialog! There are at least two ways.

For this reason, it is better to do most of your work in components like `/project1`, which makes the component exportable and share-able via [RMB](Mouse_Click.md "Mouse Click")->Save Component....

In Root you normally have `/perform`, which is a Window Component. It is tied to the [Window Placement Dialog](https://docs.derivative.ca/Window_Placement_Dialog "Window Placement Dialog") and is the default Window Component used for [Perform Mode](Perform_Mode.md "Perform Mode").

`/ui` and `/sys` are not saved in the `.toe`. They are reloaded when TouchDesigner starts. You can look inside `/ui` and `/sys`, but there is not much use in changing it.

TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](Network_Path.md "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called Root. This path is displayed at the top of every [Pane](Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](Folder.md "Folder").

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](Designer_Mode.md "Designer Mode"), or (2) a user-created [Panel](Panel.md "Panel") inside a [Window Component](Window_COMP.md "Window COMP"). The user-created windows can span [Multiple Monitors](Multiple_Monitors.md "Multiple Monitors") borderless, or be floating windows with borders, or popups.
