---
url: https://docs.derivative.ca/Panel_Class
category: Python
title: Panel_Class
---

# Panel Class
The Panel class manages Panel Components, and is used to access the state of a panel via its [Panel Value Class](https://docs.derivative.ca/PanelValue_Class "PanelValue Class").
For a list of available panel values, see: [Panel Value](https://docs.derivative.ca/Panel_Value "Panel Value").

## Members
`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.
In addition to the above, this object contains a member for each panel value in the component.

```
a = op('button1').panel.u

```

## Methods
No operator specific methods.
