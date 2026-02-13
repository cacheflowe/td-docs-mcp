---
url: https://docs.derivative.ca/Replicator_COMP
category: COMPs
title: Replicator_COMP
---

# Replicator COMP

## Summary

The Replicator COMP creates copies of a component, one for every row in a table or using a Number of Replicants parameter - it is the "for-loop" of operators. Unlike [Clone](https://docs.derivative.ca/Clone "Clone"), it automatically creates copies of a master component.
It creates replicant nodes ("[replicants](http://en.wikipedia.org/wiki/Replicant)") and deletes them as the table changes or the replicant count changes. The replicant master can be a full component and its contents or a single node.
It takes the node specified in the Master Node parameter, and makes a copy of the master for every row in the Template Table (or specified by the Number of Replicant parameter).
The nodes that are created can be named in two ways. Copies can be named/numbered sequentially using the prefix specified by the Node Prefix parameter: `item1`, `item2`, ... Alternately, copies can be named based on the string in a column of the table, specified with the Name from Table parameter.
[![Replicator.1.png](https://docs.derivative.ca/images/thumb/d/d4/Replicator.1.png/700px-Replicator.1.png)](https://docs.derivative.ca/File:Replicator.1.png)
If you want to create a node for the first row of the table, un-set the Ignore First Row parameter.
The replicants get laid out in a grid in the network, determined by the Layout and Layout Origin parameters.
The Replicator does not assume or require that the master and replicants are components – they can all be Movie File In TOPs if you want. It also does not assume or require that the replicants are [Clones](https://docs.derivative.ca/Clone "Clone"). However the Master Node can be a component whose [Clone](https://docs.derivative.ca/Clone "Clone") parameter is set to itself, so that all nodes created are clones of the master.
For every replicant, you can run a script in the callback DAT where you can see some examples of typical cases that you can adapt. Here are some others:
  * change the expression of a [parameter](https://docs.derivative.ca/Par_Class "Par Class"): `c.par.display.expr = "op('thing')[op.digits, 'display']"`
  * Change the parameter expression mode: `c.par.display.mode = ParMode.EXPRESSION` The mode is one of: `ParMode.CONSTANT`, `ParMode.EXPRESSION`, or `ParMode.EXPORT`.

If only one line of a table changes, the other existing replicants are not changed or re-created. In the callback DAT, removing `onRemoveReplicant()` will keep the replicants around to be re-used when the table grows again.
This is an extremely powerful node type. Examples: (1) A button gadget for each row of the table. a geometry component, which is replicated at every point of a 3D particle system, each behaving separately. (2) You can feed the table of a [Multi Touch In DAT](https://docs.derivative.ca/Multi_Touch_In_DAT "Multi Touch In DAT") directly to the Replicator to create something at each fingertip.
[replicatorCOMP_Class](https://docs.derivative.ca/ReplicatorCOMP_Class "ReplicatorCOMP Class")

## Parameters - Replicator Page
- Replication Method `method` - ⊞ - Choose between using a Template DAT Table where each row will create a replicant or using the Number of Replicants parameter below to set how many replications to make.
  * By Number `bynum` -
  * By Table `bytable` -

- Number of Replicants `numreplicants` - Set number of replicants when using Replication Method = By Number above.
- Template DAT Table `template` - Path to the table DAT that will drive the replicating.
- Name from Table `namefromtable` - ⊞ - How the node names will be generated.
  * Row Index `rowindex` - Uses the Node Prefix parameter followed by the row number. The default creates nodes named `item1`, `item2`, `item3` .... (The top row is 0).
  * Column by Index `colbyindex` - The node name is in the column specified by a column number.
  * Column by Name `colbyname` - The node name is in a column specified by a column name in the first row.

- Ignore First Row `ignorefirstrow` - Do not create a node for the first row.
- Column Name `colname` - Name at the top of the column.
- Column Index `colindex` - Column number, starting from 0.
- Operator Prefix `opprefix` - Add this prefix to all nodes.
- Master Operator `master` - Which node or component to replicate.
- Destination `destination` - Where to put the replicant nodes. If the location is `..`, it puts the nodes inside the parent, which is actually alongside the Replicator component. If you put `.`, it will put it inside itself, that is, inside the Replicator component. If left blank, it will error.
- Maximum Operators `domaxops` - Enable the parameter below to set a maximum number of allowed replicants.
- Maximum Operators `maxops` - Max number of nodes replicated.
- Script `tscript` - Tscript only (use callback DAT in python): For every replicant, you can run a script to customize it relative to the master, such as setting the Display or Clone parameters, or a Render flag. Replicator runs the script command to customize each replicant versus the master. `me.curItem` can be used here to access the current item and make changes to it. Select one of the 3 entries in the drop menu to the right for some examples.
If you are using [Tscript](https://docs.derivative.ca/Tscript "Tscript"), some local variables are defined:
  * $ITEM Name of current node being replicated.
  * $MASTER Name of master node.
  * $LOCATION Name of the location component.

The most common need is for the master to not display, and the replicants to display. For Panel components it is most commonly "`opparm $ITEM paneldisplay ( 1 )`", and for Geometry components it is most commonly "`opset -d on $ITEM`". Use the popup menu for some common scripts.
- Script Names `scriptmenu` - Select from some commonly used scripts (Tscript) in this menu.
- Callbacks DAT `callbacks` - Path to a DAT containing callbacks for each event received. See [replicatorCOMP_Class](https://docs.derivative.ca/ReplicatorCOMP_Class "ReplicatorCOMP Class") for usage.
- Layout `layout` - ⊞ - How to lay out the new nodes - all in one place (Off), horizontally, vertically, or in a grid.
  * Off `off` -
  * Horizontal `horizontal` -
  * Vertical `vertical` -
  * Grid `grid` -

- Layout Origin `layoutorigin` - ⊞ - Where to lay out the new nodes, giving the XY location of the top-left node's bottom-left corner.
  * `layoutorigin1` -
  * `layoutorigin2` -

- Incremental Update `doincremental` - Enables the parameter below for incremental creation of replicants.
- Incremental Update `increment` - Staggers the replication of operators to avoid large frame drops when creating replicants. It will create the specified number of replicants per frame at most, by default 1 per frame, if Incremental Update is on.
- Recreate All Operators `recreateall` - Deletes all nodes it has created, then re-creates them using the template and its current parameters.
- Recreate Missing Operators `recreatemissing` - Re-creates missing operators from the template table but does not delete and re-create already existing replicants.

## Parameters - Extensions Page
The Extensions parameter page sets the component's python extensions. Please see [extensions](https://docs.derivative.ca/Extensions "Extensions") for more information.
- Re-Init Extensions `reinitextensions` - Recompile all extension objects. Normally extension objects are compiled only when they are referenced and their definitions have changed.
- Init Extensions On Start `initextonstart` - Perform a Re-Init automatically when TouchDEsigner Starts
- Extension `ext` - Sequence of info for creating extensions on this component
- Object `ext0object` - A number of class instances that can be attached to the component.
- Name `ext0name` - Optional name to search by, instead of the instance class name.
- Promote `ext0promote` - Controls whether or not the extensions are visible directly at the component level, or must be accessed through the `.ext` member. Example: `n.Somefunction` vs `n.ext.Somefunction`

## Parameters - Common Page
The Common parameter page sets the component's [node viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer") and [clone](https://docs.derivative.ca/Clone "Clone") relationships.
- Parent Shortcut `parentshortcut` - Specifies a name you can use anywhere inside the component as the path to that component. See [Parent Shortcut](https://docs.derivative.ca/Parent_Shortcut "Parent Shortcut").
- Global OP Shortcut `opshortcut` - Specifies a name you can use anywhere at all as the path to that component. See [Global OP Shortcut](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut").
- Internal OP `iop` - Sequence header for internal operators.
- Shortcut `iop0shortcut` - Specifies a name you can use anywhere inside the component as a path to "Internal OP" below. See [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").
- OP `iop0op` - The path to the Internal OP inside this component. See [Internal Operators](https://docs.derivative.ca/Internal_Operators "Internal Operators").
- Operator Viewer `opviewer` - Select which operator's node viewer to use when the Node View parameter above is set to Operator Viewer.
- Enable Cloning `enablecloning` - Control if the OP should be actively cloneing. Turning this off causes this node to stop cloning it's 'Clone Master'.
- Enable Cloning Pulse `enablecloningpulse` - Instantaneously clone the contents.
- Clone Master `clone` - Path to a component used as the Master [Clone](https://docs.derivative.ca/Clone "Clone").
- Load on Demand `loadondemand` - Loads the component into memory only when required. Good to use for components that are not always used in the project.
- Enable External .tox `enableexternaltox` - When on (default), the external .tox file will be loaded when the .toe starts and the contents of the COMP will match that of the external .tox. This can be turned off to avoid loading from the referenced external .tox on startup if desired (the contents of the COMP are instead loaded from the .toe file). Useful if you wish to have a COMP reference an external .tox but not always load from it unless you specifically push the Re-Init Network parameter button.
- Enable External .tox Pulse `enableexternaltoxpulse` - This button will re-load from the external `.tox` file (if present).
- External .tox Path `externaltox` - Path to a `.tox` file on disk which will source the component's contents upon start of a `.toe`. This allows for components to contain networks that can be updated independently. If the `.tox` file can not be found, whatever the `.toe` file was saved with will be loaded.
- Reload Custom Parameters `reloadcustom` - When this checkbox is enabled, the values of the component's [Custom Parameters](https://docs.derivative.ca/Custom_Parameters "Custom Parameters") are reloaded when the [.tox](https://docs.derivative.ca/.tox ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](https://docs.derivative.ca/.tox ".tox").
- Reload Built-In Parameters `reloadbuiltin` - When this checkbox is enabled, the values of the component's built-in parameters are reloaded when the [.tox](https://docs.derivative.ca/.tox ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](https://docs.derivative.ca/.tox ".tox").
- Save Backup of External `savebackup` - When this checkbox is enabled, a backup copy of the component specified by the External `.tox` parameter is saved in the `.toe` file. This backup copy will be used if the External `.tox` can not be found. This may happen if the `.tox` was renamed, deleted, or the `.toe` file is running on another computer that is missing component media.
- Sub-Component to Load `subcompname` - When loading from an External `.tox` file, this option allows you to reach into the `.tox` and pull out a COMP and make that the top-level COMP, ignoring everything else in the file (except for the contents of that COMP). For example if a `.tox` file named `project1.tox` contains `project1/geo1`, putting `geo1` as the Sub-Component to Load, will result in `geo1` being loaded in place of the current COMP. If this parameter is blank, it just loads the `.tox` file normally using the top level COMP in the file.
- Relative File Path Behavior `relpath` - ⊞ - Set whether the child file paths within this COMP are relative to the .toe itself or the .tox, or inherit from parent.
  * Use Parent's Behavior `inherit` - Inherit setting from parent.
  * Relative to Project File (.toe) `project` - The path, when specified as a relative path, will be relative to the .toe file.
  * Relative to External COMP File (.tox) `externaltox` - The path, when specified as a relative path, will be relative to the .tox file. When no external COMP file is specified, or when Enable External .tox is not toggled on, this doesn't have any impact.

## Info CHOP Channels
Extra Information for the Replicator COMP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common COMP Info Channels
  * num_children - Number of children in this component.

###
## Common Operator Info Channels
  * total_cooks - Number of times the operator has cooked since the process started.

  * cook_time - Duration of the last cook in milliseconds.

  * cook_frame - Frame number when this operator was last cooked relative to the component timeline.

  * cook_abs_frame - Frame number when this operator was last cooked relative to the absolute time.

  * cook_start_time - Time in milliseconds at which the operator started cooking in the frame it was cooked.

  * cook_end_time - Time in milliseconds at which the operator finished cooking in the frame it was cooked.

  * cooked_this_frame - 1 if operator was cooked this frame.

  * warnings - Number of warnings in this operator if any.

  * errors - Number of errors in this operator if any.
