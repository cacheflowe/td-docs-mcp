---
url: https://docs.derivative.ca/Bone_Group_SOP
category: SOPs
title: Bone_Group_SOP
---

# Bone Group SOP
## Summary

The Bone Group SOP groups primitives by common bones (shared bones). This node often isn't needed in modern workflows with well made models.
This node will split the vertices into subsections, each of which are affected by a different subset of the bones of the skeleton. These are called Bone Groups. This SOP will split up geometry with capture attributes into different bone groups. The detail attributes pCaptData and pCaptPath will be split up into detail attributes with postfixes starting at 0. So for example if the geometry gets split into two bone groups, there will be detail attributes pCaptData0, pCaptPath0, pCaptData1, and pCaptPath1. The original pCaptData and pCaptPath will be deleted. The point/vertex attribute pCapt will become a vertex attribute named pCapt0, pCapt1 etc.. There will also be primitives groups named boneGroup0, boneGroup1 that contain all of the primitives in each bone group. All capture weights are re-normalized.
You should isolate out each of the primitive bone groups using the [Delete SOP](https://docs.derivative.ca/Delete_SOP "Delete SOP"). Next drop down a MAT (like the [Phong MAT](https://docs.derivative.ca/Phong_MAT "Phong MAT")) that supports deforms. You will need to give the MAT a few pieces of information:
  * The path to the SOP that contains the deform information you want this MAT to use. This is generally the Delete SOP, or some node after it.
  * The name of the pCaptData and pCaptPath attribute. So for example if you are rendering bone group 0 with this MAT, you'd specify pCaptData0 and pCaptPath0.
  * The path to the root of the skeleton.

[bonegroupSOP_Class](https://docs.derivative.ca/BonegroupSOP_Class "BonegroupSOP Class")

## Parameters - Page
- Max Bones per Point `bonesperpoint` - Trims the number of bones per point by ignoring the bones with the lowest weight until this maximum number is met.
- Max Bones per Group `bonespergroup` - The maximum number of bones allowed per group of primitives. If there are more bones than this number, a new group is created.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Bone Group SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
