---
url: https://docs.derivative.ca/Storage
category: Glossary
title: Storage
---

# Storage

Each operator has an attached Python "**storage** " dictionary. Values stored in this dictionary are persistent, and saved with the operator. The storage dictionary contents may be manipulated directly with methods such as `OP.fetch()` or `OP.store()`. See [Storage Class](https://docs.derivative.ca/OP_Class#Storage "OP Class"). You can examine storage with an [Examine DAT](https://docs.derivative.ca/Examine_DAT "Examine DAT").

The storage dictionary is accessible directly via [`n.storage`](https://docs.derivative.ca/OP_Class#Storage "OP Class"). There are also a number of utility functions associated with storage, which can be found here: [OP Storage](https://docs.derivative.ca/OP_Class#Storage "OP Class").

####  Automatic Cooking

When an immutable element of storage changes, expressions that depend on it will automatically cook. For information about cooking of mutable elements (lists, dicts, sets), see [deeply dependable collections.](https://docs.derivative.ca/TDStoreTools#Deeply_Dependable_Collections "TDStoreTools")

####  Preserving in Files

Storage is saved with `.toe` and `.tox` files and is loaded on startup. If you want the values to be in an initial state on startup, regardless of what they were when the file was saved, you can use the `storeStartupValue()` method to first create the storage entry, instead of `store()`

Also see: [StorageManager Class](https://docs.derivative.ca/StorageManager_Class "StorageManager Class"), [Storage in OP_Class](https://docs.derivative.ca/OP_Class#Storage "OP Class").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").

Storage is a python dictionary in each operator, where users can store and fetch extra data.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

TouchDesigner Component file, the file type used to save a [Component](https://docs.derivative.ca/Component "Component") of your TouchDesigner project.
