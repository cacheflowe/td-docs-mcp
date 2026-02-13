---
url: https://docs.derivative.ca/Options_Class
category: Python
title: Options_Class
---

# Options Class
The Options class describes the set of configurable UI options. It can be accessed with the ui.options object.

## Members
No operator specific members.

## Methods
`resetToDefaults()`→ `None`:
Reset all options to their default values.
###  Special Functions
`len(Options)`→ `int`:
Returns the total number of options.

```
a = len(ui.options)

```

`[<option name>]`→ `value`:
Get or set specific option given an option name key.

```
v = ui.options['DAT.width']
ui.options['DAT.width'] = 50

```

`Iterator`→ `str`:
Iterate over each option name.

```
for n in ui.options:
	print(n) # print the name of all options

```
