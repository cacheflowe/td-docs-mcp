---
url: https://docs.derivative.ca/Preferences_Class
category: Python
title: Preferences_Class
---

# Preferences Class
The Preferences class describes the set of configurable preferences that are retained between sessions. It can be accessed with the ui.preferences object or through the [Preferences Dialog](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog").

## Members
`defaults` → `dict` **(Read Only)** :
A dictionary of preferences with their default values.
## Methods
`save()`→ `None`:
Save preference values to disk. Unless saved, changes to preferences will be lost, next time application is started.

`resetToDefaults()`→ `None`:
Reset all preferences to their default values.

`load()`→ `None`:
Restore preference values from disk.
### Special Functions
`len(Preferences)`→ `int`:
Returns the total number of preferences.

```
a = len(ui.preferences)

```

`[<preference name>]`→ `value`:
Get or set specific preference given a preference name key.

```
v = ui.preferences['dats.autoindent']
ui.preferences['dats.autoindent'] = 0

```

`Iterator`→ `str`:
Iterate over each preference name.

```
for p in ui.preferences:
	print(p) # print the name of all preferences

```
