---
url: https://docs.derivative.ca/Folder_DAT
category: DATs
title: Folder_DAT
---

# Folder DAT
## Summary

The Folder DAT lists the files and subfolders found in a file system folder and monitors any changes.
For each item found, a row is created in the table with optional columns for the following information:
  * Name
  * Base Name
  * Extension
  * Type
  * Size
  * Depth
  * Folder
  * Path
  * Relative Path
  * Date Created
  * Date Modified
  * Date Accessed

[folderDAT_Class](https://docs.derivative.ca/FolderDAT_Class "FolderDAT Class")

## Parameters - Folder Page
- Active `active` - When off, the DAT outputs a single-row table with only the headings, useful when dormant or when sending the DAT to a [Replicator COMP](https://docs.derivative.ca/Replicator_COMP "Replicator COMP").
- Root Folder `rootfolder` - The folder in the filesystem whose contents will be displayed in the DAT list.
- Refresh `refresh` - When on, it monitors the specified folder(s) of the filesystem.
- Refresh Pulse `refreshpulse` - The pulse button reads the folder contents once.
- Asynchronous Update `async` - When on, the update happens asynchronously from the main thread so it doesn't make TouchDesigner drop frames or pause. As a result, the Folder DAT way not update its data within the next frame after the change on disk.
- Name Format `nameformat` - ⊞ - Select whether to include the filename extension or not.
  * Include Extension `extension` -
  * No Extension `noextension` -

- Date Format `dateformat` - ⊞ - The format used to display the item's dates in the table.
  * Standard `std` - A standard date format.
  * Epoch `epoch` - A reference date format.

- Type `type` - ⊞ - The types of contents to display.
  * Files `files` - Include files.
  * Folders `folders` - Include folders.
  * Files and Folders `filesandfolders` - Include both files and folders.

- Folders `folders` - Use [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") to specify which folders are included. Matches the folder path. Delimiters used are spaces and commas. To match spaces, enclose the entire search term in double quotes.
- Names `names` - Use [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") to specify which names are included. Delimiters used are spaces and commas. To match spaces, enclose the entire search term in double quotes.
- All Extensions `allextensions` - Includes all file extensions.
- Image Extensions `imageextensions` - Includes image contents that are supported by TouchDesigner. See supported [File Types](https://docs.derivative.ca/File_Types "File Types").
- Movie Extensions `movieextensions` - Includes movie contents that are supported by TouchDesigner. See supported [File Types](https://docs.derivative.ca/File_Types "File Types").
- Audio Extensions `audioextensions` - Includes audio contents that are supported by TouchDesigner. See supported [File Types](https://docs.derivative.ca/File_Types "File Types").
- Extensions `extensions` - Use [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") to specify which extensions are included. Extensions listed here should not include the period. E.g *txt, not *.txt.
- Include Subfolders `subfolders` - Includes the subfolders from the root folder specified.
- Minumum Depth `mindepth` - Set a minmum depth for the subfolders the Folder DAT should recursively search through.
- Limit Depth `limitdepth` - Turns on the Maximum Depth parameter to limit searching through subfolders. Turning this toggle off will search through all subtrees.
- Maximum Depth `maxdepth` - Set the maximum depth for the subfolders the Folder DAT should recursively search through.

## Parameters - Columns Page
- Name `namecol` - The name of the folder or file. In the case of a file this includes the extension. ie. `myfile.txt`
- Base Name `basenamecol` - The name of the folder or file. In the case of a file this form does not includes the extension. ie. `myfile`
- Extension `extensioncol` - The file extension of the file, blank for folders. ie. `txt`
- Type `typecol` - The type of file as reported by the operating system.
- Size `sizecol` - The size of the file in Bytes. Folders do not report any size.
- Depth `depthcol` - How many folders deep the item is found from the Root Folder. Items on the Root Folder level have a depth of 0.
- Folder `foldercol` - The path of the folder, or in the case of a file, the path of the folder the file is found in.
- Path `pathcol` - The full path to the folder or file.
- Relative Path `relpathcol` - The relative path to the folder or file from the Root Folder.
- Date Created `datecreatedcol` - The date of creation.
- Date Modified `datemodifiedcol` - The date of most recent modification.
- Date Accessed `dateaccessedcol` - The date of most recent access or opening.

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
Extra Information for the Folder DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
