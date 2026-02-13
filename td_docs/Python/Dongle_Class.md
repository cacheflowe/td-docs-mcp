---
url: https://docs.derivative.ca/Dongle_Class
category: Python
title: Dongle_Class
---

# Dongle Class
A class to interact with a single dongle connected to the system.

## Members
`serialNumber` → `str` **(Read Only)** :
Dongle Serial Number.
## Methods
`applyUpdate(str)`→ `None`:
Takes an update as a string and applies it to the dongle.

`createUpdateContext()`→ `str`:
Returns a string which is the remote programming update context for the dongle.
