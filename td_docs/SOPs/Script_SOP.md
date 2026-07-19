---
url: https://docs.derivative.ca/Script_SOP
category: SOPs
title: Script_SOP
---

# Script SOP

## Summary

The Script SOP runs a python script each time the Script SOP cooks. It can create, delete and modify points, primitives and their vertices. It can create custom attributes or built-in attributes like `Cd` (color), `uv` and `N` (normals). It can add polygons, bezier curves and meshes among others. It can combine multiple inputs. By default, the Script SOP is created with a docked DAT that contains three Python methods: `cook()`, `onPulse()`, and `setupParameters()`. The `cook()` method is run each time the Script SOP cooks. The `setupParameters()` method is run whenever the Setup Parameter button on the Script page is pressed. The `onPulse()` method is run whenever a custom pulse parameter is pushed.

Refer to Help -> Python Examples, and Help -> [Operator Snippets](../Learn/OP_Snippets.md "OP Snippets").

Note: Because the Script SOP can get data from anywhere, it's difficult to determine what it procedurally depends on. So every time that a Script OP runs it will make a list of operators, parameters, nodes etc that it depends upon, and when they change, the Script OP will re-cook.

See also: [Geometry Detail](../Glossary/Geometry_Detail.md "Geometry Detail"), [Point](../Glossary/Point.md "Point"), [Point List](../Glossary/Point_List.md "Point List"), [Point Class](Point_Class.md "Point Class"), [Primitive](../Glossary/Primitive.md "Primitive"), [Prims Class](Prims_Class.md "Prims Class"), [Polygon](../Glossary/Polygon.md "Polygon"), [Vertex](../Glossary/Vertex.md "Vertex"), [SOP](SOP.md "SOP"), [SOP Class](SOP_Class.md "SOP Class"), [SOP to DAT](../Glossary/SOP_to_DAT.md "SOP to DAT"), [Point SOP](Point_SOP.md "Point SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").

See also: [Script CHOP](../CHOPs/Script_CHOP.md "Script CHOP"), [Script DAT](../DATs/Script_DAT.md "Script DAT"), [Script TOP](../TOPs/Script_TOP.md "Script TOP").

[scriptSOP_Class](Script_SOP_Class.md "ScriptSOP Class")

## Parameters - Script Page
- Callbacks DAT `callbacks` - Specifies the DAT which holds the callbacks. See [scriptSOP_Class](Script_SOP_Class.md "ScriptSOP Class") for usage.
- Setup Parameters `setuppars` - Clicking the button runs the `setupParameters()` callback function.

Default Functions

These functions are included in the default script located in the [docked](../Glossary/Docking.md "Docking") node `script1_callbacks`.
```
# me is this DAT.
# scriptOP is the OP which is cooking.

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def setupParameters(scriptOP):
	scriptOP.appendParFloat('ValueA', page='Custom')
	scriptOP.appendParFloat('ValueB', page='Custom')
	return

#called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def cook(scriptOP):
	scriptOP.clear()
	return
```

## Operator Inputs

  * Input 0:  -

## Info CHOP Channels

Extra Information for the Script SOP can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

###

## Common SOP Info Channels

  * num_points - Number of points in this SOP.
  * num_prims - Number of primitives in this SOP.
  * num_particles - Number of particles in this SOP.
  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.
  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
