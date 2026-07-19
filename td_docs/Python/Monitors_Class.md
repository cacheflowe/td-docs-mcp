---
url: https://docs.derivative.ca/Monitors_Class
category: Python
title: Monitors_Class
---

# Monitors Class

The Monitors class describes the set of all installed [monitor objects](Monitor_Class.md "Monitor Class"). It can be accessed with the monitors object, found in the automatically imported [td module](https://docs.derivative.ca/Td_Module "Td Module"). It operates much like a Python list of monitor objects.

```
print(len(monitors))		# number of monitors
print(monitors[0])			# first monitor in the list
for m in monitors:
	print(m.description)	# print all installed monitors' descriptions
```

## Members

`primary` → `int` **(Read Only)** :

The primary [monitor](Monitor_Class.md "Monitor Class") display.

`width` → `int` **(Read Only)** :

The width of the combined monitor area, measured in pixels.

`height` → `int` **(Read Only)** :

The height of the combined monitor area, measured in pixels.

`left` → `int` **(Read Only)** :

The leftmost edge of the combined monitor area, measured in pixels.

`right` → `int` **(Read Only)** :

The rightmost edge of the combined monitor area, measured in pixels.

`top` → `int` **(Read Only)** :

The topmost position of the combined monitor area, measured in pixels.

`bottom` → `int` **(Read Only)** :

The bottommost position of the combined monitor area, measured in pixels.

## Methods

`locate(x,y)`→ `td.Monitor`:

Return the [monitor](Monitor_Class.md "Monitor Class") at the specified mouse coordinates, or None.

`refresh()`→ `None`:

Causes the application to behave as if a monitor device has changed. [Monitors DAT](../DATs/Monitors_DAT.md "Monitors DAT") and other sources will be updated. This is typically done automatically by the operating system, but in special cases can be triggered manually with this method.
