---
url: https://docs.derivative.ca/Object
category: Glossary
title: Object
---

# Object

Object Components (or `3D Objects`) are a sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of all [Components](https://docs.derivative.ca/Component "Component") and are used to define and render 3D scenes with the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP"). The most common object types are the [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") which contain the 3D shapes defined by [SOPs](https://docs.derivative.ca/SOP "SOP") to render, and the [Camera](https://docs.derivative.ca/Camera_COMP "Camera COMP"), [Light](https://docs.derivative.ca/Light_COMP "Light COMP") and [Null](https://docs.derivative.ca/Null_COMP "Null COMP") components.

There are sixteen 3D Object component types, found in the left column of the Components page of the OP Create menu:
  * [Ambient Light COMP](https://docs.derivative.ca/Ambient_Light_COMP "Ambient Light COMP")
  * [Blend COMP](https://docs.derivative.ca/Blend_COMP "Blend COMP")
  * [Bone COMP](https://docs.derivative.ca/Bone_COMP "Bone COMP")
  * [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP")
  * [Camera Blend COMP](https://docs.derivative.ca/Camera_Blend_COMP "Camera Blend COMP") - multi-camera interpolation
  * [Environment Light COMP](https://docs.derivative.ca/Environment_Light_COMP "Environment Light COMP") - light source from a spherical environment around your scene, contributing to reflections
  * [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") - holds the [SOPs](https://docs.derivative.ca/SOP "SOP") that are rendered
  * [Geo Text COMP](https://docs.derivative.ca/Geo_Text_COMP "Geo Text COMP") - 3D text
  * [Handle COMP](https://docs.derivative.ca/Handle_COMP "Handle COMP")
  * [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP")
  * [Null COMP](https://docs.derivative.ca/Null_COMP "Null COMP") - serves only to transform 3D objects in a hierarchy
  * [Nvidia Flow Emitter COMP](https://docs.derivative.ca/Nvidia_Flow_Emitter_COMP "Nvidia Flow Emitter COMP") - emits fluid for the [Nvidia Flow TOP](https://docs.derivative.ca/Nvidia_Flow_TOP "Nvidia Flow TOP")
  * [Shared Mem Out COMP](https://docs.derivative.ca/Shared_Mem_Out_COMP "Shared Mem Out COMP"), [Shared Mem In COMP](https://docs.derivative.ca/Shared_Mem_In_COMP "Shared Mem In COMP")
  * [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP") - imports geometry, motion, textures from `.fbx` files
  * [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP") - imports geometry, motion, textures from `.usd` and `.usdc` files

"**Object Space** " refers to geometry (points in SOPs and other 3D objects) relative to a certain object, like where a point of a SOP is located relative to a camera. For this, the [Object Merge SOP](https://docs.derivative.ca/Object_Merge_SOP "Object Merge SOP") and [Object CHOP](https://docs.derivative.ca/Object_CHOP "Object CHOP") and is useful. A "point in Object Space" is an XYZ position expressed in a reference frame relative to the origin of a certain 3D object.

###  Python Objects

Separately, the term "Objects" is used in the context of Python scripting in TouchDesigner.

The sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Component](https://docs.derivative.ca/Component "Component") types that are used to define and render 3D scenes. A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

The sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Component](https://docs.derivative.ca/Component "Component") types that are used to define and render 3D scenes. A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
