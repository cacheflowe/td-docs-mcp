---
url: https://docs.derivative.ca/Displace_TOP
category: TOPs
title: Displace_TOP
---

# Displace TOP
## Summary

The Displace TOP will cause one image to be warped by another image. A pixel of the output image at (Uo,Vo, Wo) gets its RGBA value from a different pixel (Ui, Vi, Wi) of the Source Image by using the second input image (the Displace Image).
For each pixel in the output image, three factors affect which pixel to fetch from the source:
  * The horizontal, vertical, and z source channels of the Displace Image (Red, Green, and Blue by default).
  * the Uo, Vo, Wo coordinate of the output pixel.
  * A constant Ua, Va, Wa anchor point (Offset).
