---
url: https://docs.derivative.ca/Internal_Operators
category: Glossary
title: Internal_Operators
---

# Internal Operators

“Internal Operators” (iOPs) provide a simple shortcut to a frequently-used operator, accessing from anywhere in that component.

Simply, you create or choose a node that you would access frequently within a component. You pick a shortcut name for that node. You set it up on the Common page of the parent component by supplying the shortcut name and the path to the node. You can then access it with a syntax like `iop._ShortcutName_`.

`iop._ShortcutName_`searches up in the parent components' hierarchy until it finds a component with a matching Internal OP Shortcut name.

See alo [Internal Parameters](https://docs.derivative.ca/Internal_Parameters "Internal Parameters") which provides more concise shortcuts to parameter collections.

##  Example

Assume you want to refer to `/project1/geo1` frequently.

Go to the parameters of `/project1`, to the Common page. Name your internal operator shortcut by setting Internal OP Shortcut 1 to `TopGeo`.

Give the path to the Geometry component by setting Internal OP 1 to `./geo1`.

The `geo1` component is now easy to refer to within your component:

Go back in `project1` and create a Camera component. In its Look At parameter put in its expression field `iop.TopGeo`.

Move `geo1`, the camera `cam1` will look continue to look at `geo1`.

##  Getting to iop from Outside a Component

You may want to get the value of an `iop` of another component, or you may want a parameter on a component to use an `iop` of that component.

Being "internal" this isn't possible with `iop`. But you can use a member of the component to access it: `COMP.internalOPs['Name']` where `_Name_`is the`iop` name you want. `COMP.internalOPs` is a dictionary of internal operator shortcuts found on the component.

See also [Internal Parameters](https://docs.derivative.ca/Internal_Parameters "Internal Parameters").

Internal Operators (iOPs) provide a simple shortcut to a frequently-used operator, accessing from anywhere in that component.

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
