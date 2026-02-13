---
url: https://docs.derivative.ca/ProductEntry_Class
category: Python
title: ProductEntry_Class
---

# ProductEntry Class
A class to interact with a dongle entry for a single dongle connected to the system.

## Members
`licenseType` → `int` **(Read Only)** :
Returns the license type for this product entry on the dongle.

`updateDate` → `tuple[int, int, int]` **(Read Only)** :
The date the product entry is valid until. Returns a tuple in the form (YYYY, MM, DD).

`version` → `str` **(Read Only)** :
The version of TouchDesigner this dongle product entry is valid for.
## Methods
No operator specific methods.
