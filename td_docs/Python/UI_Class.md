---
url: https://docs.derivative.ca/UI_Class
category: Python
title: UI_Class
---

# UI Class
The UI class describes access to the UI elements of the application, found in the automatically imported [td module](https://docs.derivative.ca/Td_Module "Td Module").
To access members and methods of this class use the default instance `ui`.
For Example:

```
# open the Midi Device Mapper Dialog
ui.openMIDIDeviceMapper()

```

## Members
`clipboard` → `str` :
Get or set the operating system clipboard text contents.

`colors` → `Colors` **(Read Only)** :
Access to the application [colors](https://docs.derivative.ca/Colors_Class "Colors Class").

`dpiBiCubicFilter` → `bool` :
Get or set the global DPI scale filtering mode of TouchDesigner windows. True means bi-cubic, False means linear.

`masterVolume` → `float` :
Get or set the master audio output volume. A value of 0 is no output, while a value of 1 is full output.

`options` → `Options` **(Read Only)** :
Access to the application [options](https://docs.derivative.ca/Options_Class "Options Class").

`panes` → `Panes` **(Read Only)** :
Access to the set of all [panes](https://docs.derivative.ca/Panes_Class "Panes Class").

`performMode` → `bool` :
Get or set [Perform Mode](https://docs.derivative.ca/Perform_Mode "Perform Mode"). Set to True to go into Perform Mode, False to go into [Designer Mode](https://docs.derivative.ca/Designer_Mode "Designer Mode").

`preferences` → `Preferences` **(Read Only)** :
Access to the application [preferences](https://docs.derivative.ca/Preferences_Class "Preferences Class"), which can also be access through the [Preferences Dialog](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog").

`redrawMainWindow` → `bool` :
Get or set whether the main window should redraw. The main window is either the main network editor, or the perform window.

`rolloverOp` → `OP | None` **(Read Only)** :
Operator currently under the mouse in a network editor.

`rolloverPar` → `Par | None` **(Read Only)** :
Parameter currently under the mouse in a parameter dialog.

`rolloverParGroup` → `ParGroup | None` **(Read Only)** :
ParGroup currently under the mouse in a parameter dialog.

`rolloverPanel` → `PanelCOMP | None` **(Read Only)** :
returns the panel currently under the mouse.

`rolloverPage` → `Page | None` **(Read Only)** :
returns the Page currently under the mouse in a parameter dialog.

`rollover` → `Par | ParGroup | Page | OP | PanelCOMP | None` **(Read Only)** :
combines the other rollover members into one test, reporting the TD object under the mouse. Because there is some overlap, priority is in the following order: Par | ParGroup | Page | OP | Panel. **Note:** Panel and OP tests both return a PanelCOMP, so to tell the difference between rolling over a PanelCOMP operator in a network and rolling over an active Panel, you may have to use the specific `rolloverPanel` or `rolloverOP` methods.

`lastChopChannelSelected` → `Channel` **(Read Only)** :
Last [CHOP channel](https://docs.derivative.ca/Channel "Channel") selected via mouse.

`showPaletteBrowser` → `bool` :
Get or set display of the palette browser.

`status` → `str` :
Get or set the status message.

```
ui.status = 'Operation Complete'

```

`undo` → `Undo` **(Read Only)** :
The [Undo](https://docs.derivative.ca/Undo_Class "Undo Class") object, which provides access to application undo functions.

`windowWidth` → `int` **(Read Only)** :
Get the app window width.

`windowHeight` → `int` **(Read Only)** :
Get the app window height.

`windowX` → `int` **(Read Only)** :
Get the app window X position.

`windowY` → `int` **(Read Only)** :
Get the app window Y position.
## Methods
`copyOPs(listOfOPs)`→ `None`:
Copy a list of operators to the operator clipboard. All operators must be children of the same component.
  * listOfOPs - A list containing one or more OPs to be copied.

```
ui.copyOPs( op('geo1').selected )

```

`pasteOPs(COMP, x=None, y=None)`→ `None`:
Copy the contents of the operator clipboard into the specified component.
  * COMP - The destination to receive the operators.
  * x - Optional network coordinates at which to paste the operators.
  * y - see x

```
l = ui.pasteOPs( op('geo2') )

```

`messageBox(title, message, buttons=['Ok'])`→ `int`:
This method will open a message dialog box with the specified message. Returns the index of the button clicked.
  * title - Specifies the window title.
  * message - Specifies the content of the dialog.
  * buttons - (Keyword, Optional) Specifies a list button labels to show in the dialog.

```
# basic usage
ui.messageBox('Warning', 'Have a nice day.')
# specify options and report result
a = ui.messageBox('Please select:', 'Buttons:', buttons=['a', 'b', 'c'])
ui.messageBox('Results', 'You selected item: ' + str(a))
# pick a node from their paths
ui.messageBox('Please select:', 'Nodes:', buttons=parent().children)
# pick a node from their first names (list comprehension)
ui.messageBox('Please select:', 'Nodes:', buttons=[x.name for x in parent().children])
# pick a cell
ui.messageBox('Please select:', 'Cells:', buttons=op('table1').cells('*','*'))

```

`refresh()`→ `None`:
Update and redraw all viewports, nodes, UI elements etc immediately. This update is otherwise done once per frame at the end of all script executions. For example, if the current frame is manually changed during a script, a call to refresh will cause all dependent data to update immediately.

```
for i in range(100):
	ui.status = str(i)
	ui.refresh()

```

`chooseFile(load=True, start=None, fileTypes=None, title=None, asExpression=False)`→ `str | None`:
Open a dialog box for loading or saving a file. Returns the filename selected or None if the dialog is cancelled.
  * load - (Keyword, Optional) If set to True, the dialog will be a Load dialog, otherwise it's a Save dialog.
  * start - (Keyword, Optional) If provided, specifies an initial folder location and/or filename selection.
  * fileTypes - (Keyword, Optional) If provided, specifies a list of file extensions that can be used as filters. Otherwise '*.*' is the only filter.
  * asExpression - (Keyword, Optional) If set to true, the results are provided as an expression, suitable for a [Parameter](https://docs.derivative.ca/Par_Class "Par Class") expression or as input to an eval() call. [App Class](https://docs.derivative.ca/App_Class "App Class") member constants such as samplesFolder may be included in the result.
  * title (Keyword, Optional) If provided, will override the default window title.

```
a = ui.chooseFile(start='python_examples.toe', fileTypes=['toe'], title='Select a toe') # specify extension
a = ui.chooseFile(fileTypes=tdu.fileTypes['image'], title='Select an image') # any support image extension
path = ui.chooseFile(load=False,fileTypes=['txt'],title='Save table as:')
if (path):
	op('table1').save(path)

```

`chooseFolder(title='Select Folder', start=None, asExpression=False)`→ `str | None`:
Open a dialog box for selecting a folder. Returns the folder selected or None if the dialog is cancelled.
  * title - (Keyword, Optional) If provided, specifies the window title.
  * start - (Keyword, Optional) If provided, specifies an initial folder location and/or filename selection.
  * asExpression - (Keyword, Optional) If set to true, the results are provided as an expression, suitable for a [Parameter](https://docs.derivative.ca/Par_Class "Par Class") expression or as input to an eval() call. [App Class](https://docs.derivative.ca/App_Class "App Class") member constants such as samplesFolder may be included in the result.

```
a = ui.chooseFolder()
a = ui.chooseFolder(title='Select a folder location.')

```

`viewFile(URL_or_path, showInFolder=False)`→ `None`:
View a URL or file in the default external application. You can use `ui.viewFile()` to open a folder/directory in Windows Explorer or macOS Finder.
  * URL_or_path - URL or path to launch.

```
a = ui.viewFile('output.txt')

```

  * showInFolder - Show file as selected in Explorer or macOS Finder instead of launching an external application.

```
a = ui.viewFile('output.txt', showInFolder=True)

```

`openBeat()`→ `None`:
Open the [Beat Dialog](https://docs.derivative.ca/Beat_Dialog "Beat Dialog").

`openBookmarks()`→ `None`:
Open the [Bookmarks Dialog](https://docs.derivative.ca/Bookmarks_Dialog "Bookmarks Dialog").

`openCOMPEditor(path)`→ `None`:
Open component editor for the specific operator.
  * path - Specifies the path to the operator. An OP can be passed in as well.

`openConsole()`→ `None`:
Open the [Console Window](https://docs.derivative.ca/index.php?title=Console_Window&action=edit&redlink=1 "Console Window \(page does not exist\)").

`openDialogHelp(title)`→ `None`:
Open help page for the specific dialog.
  * title - Specifies the help page to open.

```
ui.openDialogHelp('Window Placement Dialog')

```

`openErrors()`→ `None`:
Open the [Errors Dialog](https://docs.derivative.ca/Errors_Dialog "Errors Dialog").

`openExplorer()`→ `None`:
Open an Explorer window.

`openExportMovie(path)`→ `None`:
Open the [Export Movie Dialog](https://docs.derivative.ca/Export_Movie_Dialog "Export Movie Dialog").
  * path - Specifies the operator content to export, optional.

```
ui.openExportMovie('/project1/out1')

```

`openImportFile()`→ `None`:
Open the [Import File Dialog](https://docs.derivative.ca/Import_File_Dialog "Import File Dialog").

`openKeyManager()`→ `None`:
Open the [Key Manager Dialog](https://docs.derivative.ca/Key_Manager_Dialog "Key Manager Dialog").

`openMIDIDeviceMapper()`→ `None`:
Open the [MIDI Device Mapper Dialog](https://docs.derivative.ca/MIDI_Device_Mapper_Dialog "MIDI Device Mapper Dialog").

`openNewProject()`→ `None`:
Open the [New Project Dialog](https://docs.derivative.ca/New_Project_Dialog "New Project Dialog").

`openOperatorSnippets(optype=None, example=None)`→ `None`:
Open the Operator Snippets window.
  * optype - (Keyword, Optional) Specify the operator by python operator class type to open.
  * example - (Keyword, Optional) Specify the numeric example for the available operator snippets.

`openPaletteBrowser()`→ `None`:
Open the [Palette](https://docs.derivative.ca/Palette "Palette").

`openPerformanceMonitor()`→ `None`:
Open the [Performance Monitor Dialog](https://docs.derivative.ca/Performance_Monitor_Dialog "Performance Monitor Dialog").

`openPreferences()`→ `None`:
Open the [Preferences Dialog](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog").

`openSearch()`→ `None`:
Open the [Search Replace Dialog](https://docs.derivative.ca/Search_Replace_Dialog "Search Replace Dialog").

`openTextport()`→ `None`:
Open the [Textport](https://docs.derivative.ca/Textport "Textport").

`openVersion()`→ `None`:
Open a dialog displaying current version information. See also: [App.version](https://docs.derivative.ca/App_Class "App Class")

`openWindowPlacement()`→ `None`:
Open the [Window Placement Dialog](https://docs.derivative.ca/Window_Placement_Dialog "Window Placement Dialog").

`findEditDAT(filename)`→ `DAT | None`:
Given an external filename, finds the corresponding DAT thats update from this filename if any..
Any floating window that is not a [Pane](https://docs.derivative.ca/Pane "Pane") or [Viewer](https://docs.derivative.ca/Viewer "Viewer").
Perform Mode is an optimized mode for live performance that only renders one specified [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") which is one window that contains your video outputs and your (optional) control interface. In Perform Mode the network editing window is not open - you edit your networks in [Designer Mode](https://docs.derivative.ca/Designer_Mode "Designer Mode"). Alternate with F1 and Esc.
A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.
A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component").
A [CHOP](https://docs.derivative.ca/CHOP "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](https://docs.derivative.ca/Export "Export") to [Parameters](https://docs.derivative.ca/Parameter "Parameter").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
TOuch Environment file, the file type used by TouchDesigner to save your entire project.
A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](https://docs.derivative.ca/Designer_Mode "Designer Mode"), or (2) a user-created [Panel](https://docs.derivative.ca/Panel "Panel") inside a [Window Component](https://docs.derivative.ca/Window_COMP "Window COMP"). The user-created windows can span [Multiple Monitors](https://docs.derivative.ca/Multiple_Monitors "Multiple Monitors") borderless, or be floating windows with borders, or popups.
[OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") is a set of 700+ live examples of TouchDesigner operators. You can access snippets via the Help menu, or by right-clicking on network operators, or r-clicking on OP Create dialog items.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
