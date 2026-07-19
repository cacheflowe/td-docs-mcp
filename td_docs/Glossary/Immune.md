---
url: https://docs.derivative.ca/Immune
category: Glossary
title: Immune
---

# Immune

Every node has an [Immune Flag](Immune_Flag.md "Immune Flag"), when on and the node is inside a [Clone](Clone.md "Clone"), it is not affected by any change to the clone master, so you can store extra data in the clone or set a node to be ignored by the cloning process. The Immune flag of Components is tri-state, where one state makes the entire contents of the component immune too.

You can see if a node is Immune by inspecting the [Immune Flag](Immune_Flag.md "Immune Flag").
  * [![ImmuneFlagOffIcon.png](https://docs.derivative.ca/images/9/91/ImmuneFlagOffIcon.png)](https://docs.derivative.ca/File:ImmuneFlagOffIcon.png) Off
  * [![ImmuneFlagOnIcon.png](https://docs.derivative.ca/images/2/28/ImmuneFlagOnIcon.png)](https://docs.derivative.ca/File:ImmuneFlagOnIcon.png) On - This node is made immune.

What is kept immune: the parameters, the wiring coming to the inputs of the node, and, if the node is a panel, all its [Panel Values](Panel_Value.md "Panel Value") like `state`, `u` and `v`. The data of Table DATs and the data of [Locked](https://docs.derivative.ca/index.php?title=Lock&action=edit&redlink=1 "Lock \(page does not exist\)") nodes are also kept immune.

**WARNING:** If you add a new node in a Clone and make the new node's Immune flag On, you may also have to make the Immune flag On of the nodes its output is connected to, since wiring information is held with the inputs of a node.

####  Immune on Components

Every component node has an Immune 3-state [Flag](Flag.md "Flag"), also known as Clone Immune Flag.

See [Immune Flag](Immune_Flag.md "Immune Flag") and [Clone](Clone.md "Clone") for additional information.

####  Immune by Python

See `cloneImmune` in [OP_Class](../Python/OP_Class.md "OP Class").

Every node has an [Immune Flag](Immune_Flag.md "Immune Flag"), when on and the node is inside a [Clone](Clone.md "Clone"), it is not affected by any change to the clone master, so you can store extra data in the clone or set a node to be ignored by the cloning process.

Cloning makes multiple components match the contents of a master component. A [Component](Component.md "Component") whose Clone parameter is set will be forced to contain the same nodes, wiring and parameters as its master component. Cloning does not create new components as does the [Replicator COMP](Replicator_COMP.md "Replicator COMP").

Indicator of certain states of an operator (bypass, display, lock, viewer active).
