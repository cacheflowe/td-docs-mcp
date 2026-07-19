---
url: https://docs.derivative.ca/Parent_Shortcut
category: Glossary
title: Parent_Shortcut
---

# Parent Shortcut

A Parent Shortcut allows any component to be referenced in any of its children operators with a `parent._Name_`notation, no matter how deep the children reside inside the component.

**Note** : For global shortcuts to components in another part of your project, see [Global OP Shortcut](Global_OP_Shortcut.md "Global OP Shortcut").

The advantages of using the parent shortcut inside a component is:
  * You don't need to know how many parent levels up the main component is. Instead of writing `parent(3)` to get to a main component, you write `parent.Name`.
  * The component then becomes very portable and can be copy/pasted or moved into any network.

To specify a shortcut, enter a name in a component's Parent Shortcut parameter, for example, `Effect`. To reference the shortcut, use `parent._Name_`where` _Name_`is the value entered in the component's shortcut parameter,`parent.Effect` in this case.

Since all uses of `parent._Name_`will refer to the parent shortcut instead of using absolute paths, moving the component into another network will not break any expressions in the component.

Note that by default, the component `/project1` has its Parent Shortcut parameter set to `Project`. Thus `parent.Project` will refer to this top level operator from anywhere inside.

**Example:** A panel is located at `/project1/fireEffect`. Instead of using `parent().par.w` or `parent(2).par.w` etc to access its width, (depending on where the expression is located), set the Parent Shortcut of the panel to `Effect`. Then anywhere inside the component, `parent.Effect` will refer to `/project1/fireEffect`, and `parent.Effect.par.w` is the width parameter of the panel.

If you move the `fireEffect` component to an entirely different location: `/project3/controlpanel/effects/fireEffect`, then any internal expression with `parent.Effect` will conveniently point to `/project3/controlpanel/effects/fireEffect`.

If all [clones](Clone.md "Clone") of a master component have the same parent shortcut, using that name inside any of the clones will refer to the unique location of each clone, making paths in clones simpler and clones more portable.

(Parent Shortcut was formerly called Path Variable or Internal Shortcut.)

For exact usage and details, see [OP Class#Members](../Python/OP_Class.md#Members "OP Class").

See also: `parent()` in [Td_Module](https://docs.derivative.ca/Td_Module "Td Module"), [Global OP Shortcut](Global_OP_Shortcut.md "Global OP Shortcut")

A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](Root.md "Root"). This path is displayed at the top of every [Pane](Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](Folder.md "Folder").

Operator shortcuts are Python objects that return operators (or sometimes parameters). These include Parent Shortcuts for accessing a component from within that component, and [Global OP Shortcuts](Global_OP_Shortcut.md "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.
