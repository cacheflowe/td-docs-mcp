---
url: https://docs.derivative.ca/Immune_Flag
category: Glossary
title: Immune_Flag
---

# Immune Flag
[![](https://docs.derivative.ca/images/6/68/ImmuneFlag.png)](https://docs.derivative.ca/File:ImmuneFlag.png)
[](https://docs.derivative.ca/File:ImmuneFlag.png "Enlarge")
Immune Flag is off
[![](https://docs.derivative.ca/images/1/11/ImmuneFlagOn.png)](https://docs.derivative.ca/File:ImmuneFlagOn.png)
[](https://docs.derivative.ca/File:ImmuneFlagOn.png "Enlarge")
Node Immune Flag is on
[![](https://docs.derivative.ca/images/4/47/ImmuneFlagNetworkOn.png)](https://docs.derivative.ca/File:ImmuneFlagNetworkOn.png)
[](https://docs.derivative.ca/File:ImmuneFlagNetworkOn.png "Enlarge")
Network Immune Flag is on
Every non-component node has an [Immune](https://docs.derivative.ca/Immune "Immune") 2-state [Flag](https://docs.derivative.ca/Flag "Flag"), also known as Clone Immune Flag. If the Immune flag is On for a node in a [Clone](https://docs.derivative.ca/Clone "Clone"), it is not affected by changes made to the equivalent node in the master clone. You can use the Immune flag to customize parameters of operators, or to add extra operators and additional data that does not exist in the Clone's Master Component. bi-state The Immune flag on non-components is a 2-state flag.
  * [![ImmuneFlagOffIcon.png](https://docs.derivative.ca/images/9/91/ImmuneFlagOffIcon.png)](https://docs.derivative.ca/File:ImmuneFlagOffIcon.png) Off
  * [![ImmuneFlagOnIcon.png](https://docs.derivative.ca/images/2/28/ImmuneFlagOnIcon.png)](https://docs.derivative.ca/File:ImmuneFlagOnIcon.png) On - This node is made immune.

For example, Table DATs in clones are often made immune to make the table unique in each clone.
What is kept immune: the parameters, the wiring coming to the inputs of the node, and, if the node is a panel, all its [Panel Values](https://docs.derivative.ca/Panel_Value "Panel Value") like `state`, `u` and `v`. The data of Table DATs and the data of [Locked](https://docs.derivative.ca/index.php?title=Lock&action=edit&redlink=1 "Lock \(page does not exist\)") nodes are also kept immune.
**WARNING** : If you add a new node in a Clone and make the new node's Immune flag On, you may also have to make the Immune flag On of the nodes its output is connected to, since wiring information is held with the inputs of a node.
####  Immune on Components
Every component node has an [Immune](https://docs.derivative.ca/Immune "Immune") 3-state [Flag](https://docs.derivative.ca/Flag "Flag"), also known as Clone Immune Flag.
The Immune flag on components is a 3-state flag.
  * [![ImmuneFlagOffIcon.png](https://docs.derivative.ca/images/9/91/ImmuneFlagOffIcon.png)](https://docs.derivative.ca/File:ImmuneFlagOffIcon.png) Off
  * [![ImmuneFlagOnIcon.png](https://docs.derivative.ca/images/2/28/ImmuneFlagOnIcon.png)](https://docs.derivative.ca/File:ImmuneFlagOnIcon.png) On - This node is made immune.
  * [![ImmuneFlagNetworkOnIcon.png](https://docs.derivative.ca/images/6/67/ImmuneFlagNetworkOnIcon.png)](https://docs.derivative.ca/File:ImmuneFlagNetworkOnIcon.png) On Including Children - This node is made immune plus (if the node is a [Component](https://docs.derivative.ca/Component "Component")) all nodes inside the component (recursively) are immune.

If a node is inside a [Clone](https://docs.derivative.ca/Clone "Clone") component and the node's Immune flag is On, it is not affected by changes made to the equivalent node in the master clone.
Thus entire [Components](https://docs.derivative.ca/Component "Component") can be made immune using On Including Children, where all the nodes inside the component's network are immune as well.
The 3-state flag is on the tiles and also in the network editor's list mode (use shift+t to switch modes).
When a `.toe` or `.tox` file is saved, all cloned nodes are NOT saved in the `.toe` except for immune nodes. Immune nodes in clones are saved since they are not defined in the master clone. Otherwise, nodes in clones are not expected to be saved in the file.

See [Clone](https://docs.derivative.ca/Clone "Clone") for additional information.
See also [Flag](https://docs.derivative.ca/Flag "Flag").
####  Immune by Python
See `cloneImmune` in [OP_Class](https://docs.derivative.ca/OP_Class "OP Class").
For components, see `componentCloneImmune` in [COMP_Class](https://docs.derivative.ca/COMP_Class "COMP Class"). When `componentCloneImmune` is True, everything inside the clone is immune. When `componentCloneImmune` is False, it uses the [OP_Class](https://docs.derivative.ca/OP_Class "OP Class") `cloneImmune` member to determine if just the component is immune (its parameters etc, but not the component's network inside).
Every node has an Immune Flag, when on and the node is inside a [Clone](https://docs.derivative.ca/Clone "Clone"), it is not affected by any change to the clone master, so you can store extra data in the clone or set a node to be ignored by the cloning process.
Indicator of certain states of an operator (bypass, display, lock, viewer active).
Cloning makes multiple components match the contents of a master component. A [Component](https://docs.derivative.ca/Component "Component") whose Clone parameter is set will be forced to contain the same nodes, wiring and parameters as its master component. Cloning does not create new components as does the [Replicator COMP](https://docs.derivative.ca/Replicator_COMP "Replicator COMP").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
TOuch Environment file, the file type used by TouchDesigner to save your entire project.
TouchDesigner Component file, the file type used to save a [Component](https://docs.derivative.ca/Component "Component") of your TouchDesigner project.
