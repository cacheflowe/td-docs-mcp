---
url: https://docs.derivative.ca/Table_DAT
category: DATs
title: Table_DAT
---

# Table DAT

## Summary

The Table DAT lets you hand-edit or create a table of rows and columns of cells, each cell containing a text string. A "table" is one of the two forms of DATs (the other being simply lines of "free-form" text via the [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT")).
**Manually editing cells** - When a Table DAT has its [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active") on, you can add rows and columns by right-clicking on row 0 or column 0 to add rows/columns, and typing text into any cell of its [node viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer"). Use the Tab key to jump to the next cell, and the up/down arrow keys to navigate to adjacent cells.
**Procedurally filling cells** - You can conveniently create and fill rows and columns of a table. On the Fill page, the Fill Type menu gives 5 options: Manual, Set Size, Set Size and Contents, Fill by Column, and Fill by Row. When a Fill option is chosen, you can generate multiple rows/columns with specific headings using space-separated names or an expression, plus expressions to fill the cells.
You can use `me.subRow` and `me.subCol` (for sub-section being filled) in your expressions. See the popup menu on the Cell Expression parameter for suggestions.
Click the + below the parameters to you generate multiple sets of new cols or rows.
**Filling cells externally with python** - If you are not auto-filling, you can put strings into table cells using something like `op('table1')[2,'select'] = 'yes'` in a python script elsewhere, or append rows using `.appendRow()` in python. See also the [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT") and its Snippets.
**Loading from external files** - The Table DAT can also can load a table from a comma-separated file `(.csv)`, tab-separated file `(.tsv)`, or TouchDesigner DAT file `(.dat)` file on disk or on the web. Other text files `(.txt, .py, .glsl, etc)` can also be loaded, but will be treated as tab-separated files. Either drag-drop the file into a network, or use the File parameter.
Use `http://` when specifying a table on the internet.
If you drag the Table DAT to a desktop or folder, The DAT text will be converted into tab-delimited tables in a `.txt` file.
See also [Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT"), [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT").
[tableDAT_Class](https://docs.derivative.ca/TableDAT_Class "TableDAT Class")

## Parameters - Table Page
- Edit.. `edit` - Clicking this opens a text editor to add/edit/delete text from the DAT.
- File `file` - The filesystem path and name of the file to load. Supports comma-separated `(.csv)`, tab-separated `(.tsv)`, or TouchDesigner DAT files `(.dat)`. Other text file formats `(.txt, .py, .glsl, etc)` will be treated as tab-separated files.
- Sync to File `syncfile` - When On, loads the file from disk into the DAT when the projects starts. A filename must be specified. Turning on the option will load the file from disk immediately. If the file does not exist, it will be created the first time the DAT is updated. The file is monitored so that any changes made to the file will update the DAT, and any changes made to the DAT will be written to the file right away. If the file is removed, the DAT will retain its current contents.
- Default Read Encoding `defaultreadencoding` - ⊞ - Sets the expected file encoding format, or auto-detects the format. UTF8, UTF16-LE, UTF16-BE, CP1252
  * Auto Detect `manual` -
  * UTF8 `utf8` -
  * UTF16-LE `utf16le` -
  * UTF16-BE `utf16be` -
  * CP1252 `cp1252` -

- Load on Start `loadonstart` - When On, reloads the file from disk into the DAT when the projects starts.
- Write on Toe Save `write` - When On, writes the contents of the DAT out to the file on disk when the project is saved.
- Remove Blank Lines `removeblank` - When enabled, do not convert blank lines into empty rows when loading files.

## Parameters - Fill Page
- Fill Type `fill` - ⊞ - You can create and fill rows and columns of a table. Fill Type menu gives 5 options: Manual, Set Size, Set Size and Contents, Fill by Column, and Fill by Row. When a Fill option is chosen, you can generate multiple rows/columns with specific headings using space-separated names or an expression, plus expressions to fill the cells.
  * Manual `manual` - Rows and Columns will be added manually by user.
  * Set Size `setsize` - The size will be set by the Rows and Columns parameters, but the cells will not be filled in.
  * Set Size and Contents `setsizeandcontents` - The size will be set by the Rows and Columns parameters, and the cells will be filled based on the Cell Expression.
  * Fill by Column `fillbycol` - The number of rows will be set by the Rows parameter, and the content of the columns will be defined by the Names 0 and Cell Expression 0 parameters.
  * Fill by Row `fillbyrow` - The number of columns will be set by the Columns parameter, and the content of the rows will be defined by the Names 0 and Cell Expression 0 parameters.

- Rows `rows` - Defines the number of rows in the table, where applicable.
- Columns `cols` - Defines the number of columns in the table, where applicable.
- Cell Expression `cellexpr` - Expression used to fill each cell if the Fill Type is Set Size and Contents. Can include expressions `me.subRow` and `me.subCol`
- Include Names `includenames` - Creates an extra row at the top, or a column at the left for the names of the columns or rows, filled with the Include Names parameter.
- Fills `fills` - Sequence of fill information for _Fill by Column_ and _Fill by Row_ Fill Types
- Names `fills0names` - Space-separated names of one or more columns or rows. If it is an expression, each name can be the member of a python list, like `['heading1', 'heading2']`. This parameter is the start of a sequential block.
- Cell Expression `fills0expr` - Expression used to fill each cell if the Fill Type is Fill by Row or Fill by Column. Can include expressions `me.subRow` and `me.subCol`.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * From Language `language` - pick extension from DATs script language.
  * Custom Extension `custom` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Info CHOP Channels
Extra Information for the Table DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common DAT Info Channels
  * num_rows - Number of rows in this DAT.

  * num_cols - Number of columns in this DAT.

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
