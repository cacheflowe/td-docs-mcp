---
url: https://docs.derivative.ca/DAT
category: Glossary
title: DAT
---

# DAT

## Summary

[![OP DAT.png](https://docs.derivative.ca/images/thumb/c/c5/OP_DAT.png/1000px-OP_DAT.png)](https://docs.derivative.ca/File:OP_DAT.png)
See also [Category:DATs](https://docs.derivative.ca/index.php?title=Category:DATs&action=edit&redlink=1 "Category:DATs \(page does not exist\)") for a full list of articles related to DATs.

**DATa Operators** (or **DATs**) are used to hold text data like strings, scripts, and XML. DATs either contain multiple lines of text as in a script, or a table of rows and columns of cells, each containing one string. You can edit the contents of the DAT directly in the [DAT Viewer](https://docs.derivative.ca/DAT_Viewer "DAT Viewer").

Access a DAT containing normal text using `op('text1').text`. Access a cell in a DAT containing a table using `op('table1')[1,2]` or by row/col names `op('table1')['rowname', 'colname']`.

**IMPORTANT** : `op('table1')[1,2]` is a python [cell object](../Python/Cell_Class.md "Cell Class") which usually gets converted for you to the string in the cell. More safely use `op('table1')[1,2].val` which always gives you the string.

[DAT Class](../Python/DAT_Class.md "DAT Class")

##  Sweet Sixteen DATs

The following 16 DATs are commonly used, we recommend familiarizing yourself with them.
DAT | Purpose | Related DAT
---|---|---
[Text](Text_DAT.md "Text DAT") | A place to edit and hold any text data. |
[Table](Table_DAT.md "Table DAT") | Edit tables of text in rows and columns of "cells". |  [Convert](../DATs/Convert_DAT.md "Convert DAT")
[Merge](../DATs/Merge_DAT.md "Merge DAT") | Merges tables or text DATs into one. |  [Switch](../DATs/Switch_DAT.md "Switch DAT")
[Select](../DATs/Select_DAT.md "Select DAT") | Select specific columns or rows from a DAT. |  [Substitute](../DATs/Substitute_DAT.md "Substitute DAT")
[Reorder](../DATs/Reorder_DAT.md "Reorder DAT") | Re-orders and repeats rows or columns in a DAT. |  [Transpose](../DATs/Transpose_DAT.md "Transpose DAT")
[Insert](../DATs/Insert_DAT.md "Insert DAT") | Adds one row or column to a table filling with text in the new cells. |
[Evaluate](../DATs/Evaluate_DAT.md "Evaluate DAT") | Evaluates expressions in DATs. |  [Script](../DATs/Script_DAT.md "Script DAT")
[CHOP to](../DATs/CHOP_to_DAT.md "CHOP to DAT") | Converts CHOP channels to DATs. |  [SOP to](SOP_to_DAT.md "SOP to DAT")
[CHOP Execute](../DATs/CHOP_Execute_DAT.md "CHOP Execute DAT") | Runs the DAT as a script when a CHOP changes. |
[Panel Execute](Panel_Execute_DAT.md "Panel Execute DAT") | Runs the DAT as a script when a [Panel](Panel.md "Panel") changes. |
[DAT Execute](../DATs/DAT_Execute_DAT.md "DAT Execute DAT") | Runs the DAT as a script when another DAT changes. |  [Execute](../DATs/Execute_DAT.md "Execute DAT")
[OSC In](../DATs/OSC_In_DAT.md "OSC In DAT")/[UDP In](../Interoperability/UDP_In_DAT.md "UDP In DAT") | Receive data from other applications via Open Sound Control. |  [OSC Out](../DATs/OSC_Out_DAT.md "OSC Out DAT")/[UDP Out](../DATs/UDP_Out_DAT.md "UDP Out DAT")
[Web](../DATs/Web_DAT.md "Web DAT") | Fetch a page on the internet based on a URL. |  [XML](../Interoperability/XML_DAT.md "XML DAT")
[Render Pick](../DATs/Render_Pick_DAT.md "Render Pick DAT") | Use mouse to pick 3D objects and surfaces. |  [Info](../DATs/Info_DAT.md "Info DAT")
[Multi Touch In](../Interoperability/Multi_Touch_In_DAT.md "Multi Touch In DAT") | Receive input from Windows 7+ multi-touch devices. |
[MIDI In](../DATs/MIDI_In_DAT.md "MIDI In DAT") | Get MIDI controller and button data. |  [Serial](../Interoperability/Serial_DAT.md "Serial DAT")
All DATs are documented in the [Category:DATs](https://docs.derivative.ca/index.php?title=Category:DATs&action=edit&redlink=1 "Category:DATs \(page does not exist\)").

##  DATs for Scripting

DATs can be linked together to select, re-arrange and evaluate data and expressions, making DATs a powerful **procedural scripting tool**.

DATs that contain scripts can be triggered by events like mouse clicks and any operation of gadgets in TouchDesigner control panels. DAT scripts can also be triggered by channel changes in CHOPs.       **Script Example**: This will create a button that plays a sound when you click it: Create a Button component (Tab -> COMP -> Button). Go inside it (Enter) and create an Audio Play CHOP (Tab -> CHOP -> Audio Play).     Then create a Panel Execute DAT (Tab -> DAT -> Panel Execute) and make its [Viewer Active](Viewer_Active.md "Viewer Active"). Then click in its viewer and and change the `offToOn()` function to be:
```
def offToOn(panelValue):
     op('audioplay1').par.trigger.pulse()
     return
```

Click outside the node to end text entry. Go back up (u), make the button a Momentary button via its Button page and Button Type parameter. Then make the button [Viewer Active](Viewer_Active.md "Viewer Active"). Click on the viewer of the button. It should make a Notify sound.

You can also run a script in a Text DAT by using the "`run`" command from the textport or another DAT.

##  DATs for Tables

DAT tables are rows and columns of cells containing text strings.

The DAT whose name is [Table DAT](Table_DAT.md "Table DAT") is used to define new tables. To manually add, delete rows and columns of tables, press RMB over the table when [Viewer Active](Viewer_Active.md "Viewer Active") is on and select from the menu.

The tables are then manipulated by the [Select DAT](../DATs/Select_DAT.md "Select DAT"), [Evaluate DAT](../DATs/Evaluate_DAT.md "Evaluate DAT"), [Merge DAT](../DATs/Merge_DAT.md "Merge DAT"), [Switch DAT](../DATs/Switch_DAT.md "Switch DAT"), [Sort DAT](../DATs/Sort_DAT.md "Sort DAT") and others.

You can use table DATs to export to parameters. See [DAT Export](../DATs/DAT_Export.md "DAT Export").

DAT tables can be modified with the `tabcell` command.

Table cells are read with a `tab()`, `tabr()`, `tabc()` or `tabrc()` expression. See Help -> Commands and Expressions.       **Table Example** : This will create two TOP images with names in it: Create a Table DAT (Tab -> DAT -> Table). Make its [Viewer Active](Viewer_Active.md "Viewer Active"). Right-click on the viewer and select Add Column, and then Add Row, and again Add Row, which should give you 3 rows and 2 columns of empty cells (or put 2 and 3 in the parameters.)     Click in the top left cell and type `name`, top right type `age`, and fill in the remaining cells with `joe`, `9`, `jane`, `21`.     Now create a Text TOP (Tab -> TOP -> Text) and in its parameter called Text, type this expression to retrieve a cell from the table: ``tabc("table1", $OD, "name")``. You should see "joe" in the Text TOP viewer. Copy/paste the Text TOP (Ctrl-C, Ctrl-V). The new TOP should be called `text2` and its viewer should say "jane".     That `tabc()` expression gets from the table, `table1`, the node you edited. It gets from the column called `name`. And the row is `$OD`, which is a variable you can use in any node that means "operator digits", the digits at the end of the operator name, which in this case is `1` and `2` for `text1` and `text2`.     In the TOPs' expressions, you can replace `"name"` with `"age"`.

##  DATs for manipulating Web and XML Data

The [Web Client DAT](../Interoperability/Web_Client_DAT.md "Web Client DAT") gets HTML or other data by passing a URL to the internet and receiving a response. The result and any XML data can be filtered with an [XML DAT](../Interoperability/XML_DAT.md "XML DAT"), then further processed with the other DATs.

##  DATs for Raw Text

DATs can also be use to hold raw text which can then used by the [Text TOP](../TOPs/Text_TOP.md "Text TOP") and [Text SOP](../SOPs/Text_SOP.md "Text SOP") for use in compositing and 3D. They can also be used to leave comments your networks or for pop-up help messages for panel gadgets.

##  Editing DATs

DATs can be edited directly in their viewers by turning on the [Viewer Active Flag](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag").

You can also edit DATs in the [Textport](Textport.md "Textport") by right-clicking on a DAT and selecting **Edit Contents in Textport**.

Some DAT generators and most DAT filters can not be edited because their data is fed to them from their input. This is indicated in the viewer by a more muted text color compared to those DATs which can be edited. If you need to temporarily edit the contents of one of these DATs you can lock the DAT using the [Lock Flag](Lock_Flag.md "Lock Flag") and then edit it. However, these changes will be lost when the DAT is unlocked and locking it keeps it from [cooking](Cook.md "Cook"), so this is generally only useful for troubleshooting and debugging.

By default, text-type DATs display line numbers in the left margin area and table-type DATs display row and column numbers. The display of these numbers can be controlled in [Preferences](https://docs.derivative.ca/index.php?title=Preferences_Dialog&action=edit&redlink=1 "Preferences Dialog \(page does not exist\)").

##  Editing DAT Text in an External Editor

In any DAT (or any parameter), if you right-click the DAT node and select **Edit Contents...** you will be editing the text in an external editor. Notepad is Windows default text editor.

To change the text editor to something else, like Notepad++, Vim, Sublime, etc. you need to change the Text Editor and Table Editor preference values. These preferences can be found in the Preferences dialog under the DATs page. Set their values to the path of the installed application executable (.exe) of the editor you want to use. For example, `C:/Program Files ..`.

Everyone has a favorite, have a look at Sublime Text 2.

To see how you set an environment variable, see [Variables](https://docs.derivative.ca/Variables "Variables").

##  Using DATs

  * text data, text and table formats (tab delimited)
  * use for scripts, commands, storage of values and arrays
  * can be edited in the viewer, textport, or any external text editor
  * Import: Text DAT, Table DAT, Web DAT
  * Export: (right-click to save)
