---
url: https://docs.derivative.ca/Object
category: Glossary
title: Object
---

# Object

Object Components (or `3D Objects`) are a sub-[Family](Operator_Family.md "Operator Family") of all [Components](Component.md "Component") and are used to define and render 3D scenes with the [Render TOP](../TOPs/Render_TOP.md "Render TOP"). The most common object types are the [Geometry Component](Geometry_COMP.md "Geometry COMP") which contain the 3D shapes defined by [SOPs](../SOPs/SOP.md "SOP") to render, and the [Camera](Camera_COMP.md "Camera COMP"), [Light](Light_COMP.md "Light COMP") and [Null](../COMPs/Null_COMP.md "Null COMP") components.

There are sixteen 3D Object component types, found in the left column of the Components page of the OP Create menu:
  * [Ambient Light COMP](../COMPs/Ambient_Light_COMP.md "Ambient Light COMP")
  * [Blend COMP](../COMPs/Blend_COMP.md "Blend COMP")
  * [Bone COMP](../COMPs/Bone_COMP.md "Bone COMP")
  * [Camera COMP](Camera_COMP.md "Camera COMP")
  * [Camera Blend COMP](../COMPs/Camera_Blend_COMP.md "Camera Blend COMP") - multi-camera interpolation
  * [Environment Light COMP](../COMPs/Environment_Light_COMP.md "Environment Light COMP") - light source from a spherical environment around your scene, contributing to reflections
  * [Geometry COMP](Geometry_COMP.md "Geometry COMP") - holds the [SOPs](../SOPs/SOP.md "SOP") that are rendered
  * [Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP") - 3D text
  * [Handle COMP](../COMPs/Handle_COMP.md "Handle COMP")
  * [Light COMP](Light_COMP.md "Light COMP")
  * [Null COMP](../COMPs/Null_COMP.md "Null COMP") - serves only to transform 3D objects in a hierarchy
  * [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP") - emits fluid for the [Nvidia Flow TOP](../Interoperability/Nvidia_Flow_TOP.md "Nvidia Flow TOP")
  * [Shared Mem Out COMP](../COMPs/Shared_Mem_Out_COMP.md "Shared Mem Out COMP"), [Shared Mem In COMP](../COMPs/Shared_Mem_In_COMP.md "Shared Mem In COMP")
  * [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP") - imports geometry, motion, textures from `.fbx` files
  * [USD COMP](../COMPs/USD_COMP.md "USD COMP") - imports geometry, motion, textures from `.usd` and `.usdc` files

"**Object Space** " refers to geometry (points in SOPs and other 3D objects) relative to a certain object, like where a point of a SOP is located relative to a camera. For this, the [Object Merge SOP](../SOPs/Object_Merge_SOP.md "Object Merge SOP") and [Object CHOP](../CHOPs/Object_CHOP.md "Object CHOP") and is useful. A "point in Object Space" is an XYZ position expressed in a reference frame relative to the origin of a certain 3D object.

###  Python Objects

Separately, the term "Objects" is used in the context of Python scripting in TouchDesigner.

The sub-[Family](Operator_Family.md "Operator Family") of [Component](Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](Camera_COMP.md "Camera COMP") and [Light COMP](Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

The sub-[Family](Operator_Family.md "Operator Family") of [Component](Component.md "Component") types that are used to define and render 3D scenes. A [Geometry Component](Geometry_COMP.md "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](Camera_COMP.md "Camera COMP") and [Light COMP](Light_COMP.md "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
