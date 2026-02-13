---
url: https://docs.derivative.ca/License_Class
category: Python
title: License_Class
---

# License Class
The License class describes a single instance of an installed license. They can be accessed from the [licenses](https://docs.derivative.ca/Licenses_Class "Licenses Class") object.

## Members
`index` → `int` **(Read Only)** :
The license index in the list.

`isEnabled` → `bool` **(Read Only)** :
True if the license is locally enabled (That is, it has never been disabled).

`isRemotelyDisabled` → `bool` **(Read Only)** :
True if the license has been remotely disabled.

`key` → `str` **(Read Only)** :
The key sequence.

`remoteDisableDate` → `tuple[int, int, int]` **(Read Only)** :
The date the license was remotely disabled, expressed as a tuple (year, month, day).

`status` → `int` **(Read Only)** :
The numeric status code. Negative values indicate the license is not applicable to the current application. A value of zero indicates it does.

`statusMessage` → `str` **(Read Only)** :
A description of the status code.

`systemCode` → `str` **(Read Only)** :
The system code associated with this license.

`type` → `str` **(Read Only)** :
The license type, e.g. some products being 'Pro', 'Non-Commercial', 'Commercial'. See also app.product in [App Class](https://docs.derivative.ca/App_Class "App Class")

`updateExpiryDate` → `tuple[int, int, int]` **(Read Only)** :
The date updates for this license expires, expressed as a tuple (year, month, day).

`version` → `int` **(Read Only)** :
The numeric license version.
## Methods
`serverDisable()`→ `None`:
Disable this license. Use with caution!
