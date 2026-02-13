---
url: https://docs.derivative.ca/Web_Render_TOP
category: TOPs
title: Web_Render_TOP
---

# Web Render TOP
## Summary

The Web Render TOP takes a URL or DAT and renders a webpage via separate browser processes that uses Chromium Embedded Frameworks, and passes the result back through shared memory. The processes names starts with TouchDesigner Web Render and there may be multiple spawned per Web Render TOP. It renders non-Flash pages, including HTML, HTML5, PDF, SVG and more. Targets can be on the internet, in local files with a `file://` syntax, or a [DAT](https://docs.derivative.ca/DAT "DAT").
It is implemented with the [Chromium Embedded Frameworks](https://bitbucket.org/chromiumembedded/cef) project (CEF).
Attach an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") to get the loaded status `loaded` of the page, and `num_handle_updates`, the number of times the page has been rendered.
Attach an [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") to get the shared memory `handle`, the `status` of the browser process, the `process_id`, versions for Chromium Embedded Frameworks `cef` and Chromium `chromium`, the `url` currently displayed, page `title` and `error` state of the process.
See also [Palette:webBrowser](https://docs.derivative.ca/Palette:webBrowser "Palette:webBrowser"), [Audio Web Render CHOP](https://docs.derivative.ca/Audio_Web_Render_CHOP "Audio Web Render CHOP"), [Palette:SVG](https://docs.derivative.ca/Palette:SVG "Palette:SVG")
[webrenderTOP_Class](https://docs.derivative.ca/WebrenderTOP_Class "WebrenderTOP Class")

## Parameters - Web Render Page
- Active `active` - Enables/disables the Web Render TOP.
- Source `source` - ⊞ - Source of the webpage, which can be an address via URL or File, or data from a DAT
  * URL or File `urlorfile` -
  * DAT `dat` -

- URL or File `url` - Uniform Resource Locator or the address of the web page
- DAT `dat` - Text to be loaded into a webpage
- Reload Source `reloadsrc` - Reload source DAT, URL or File.
- Reload Current Page `reload` - Reloads the current page, the same as refreshing a web browser.
- Reset Update Count `resetcount` - Reset the counter for the number of times the webpage has been updated (available via an Info CHOP).
- Only Update when Loaded `updatewhenloaded` - Only shows the web page when it is full loaded.
- Cook Always `alwayscook` - Cook every frame if on. If off, the Web Render TOP will cook for a 10 additional frames after the last update received to maintain continuity.
- Transparent Background `transparent` - Loads the webpage with a transparent background. This option will restart the browser process.
- Audio Options `audio` - ⊞ - Let the browser process play audio if the web page contains audio. This option will restart the browser process.
  * Off `off` - Sound disabled.
  * Route to System Audio Out `system` - Redirect to system audio out.
  * Route to Audio Web Render CHOPs `audiochop` - Redirect to Audio Web Render CHOPs
  * Off `off` -
  * Route to System Audio Out `system on` -
  * Route to Audio Web Render CHOPs `audiochop capture` -

- Enable Media Stream `mediastream` - Allows the web render instance to use the mic and the camera.
- Redirect Popups `redirectpopups` - Instead of ignorning popups, the Web Render TOP switches to the url for the popup.
- Maximum Render Frame Rate `maxrenderrate` - Sets the maximum frame rate the page will be rendered at. Can be higher than 60 but does not guarantee a frame rate.
- Number of Frame Buffers `numbuffers` - Sets the maximum number of cached images
- DPI Scaling Factor `dpiscale` - Sets the DPI scaling factor for the rendered webpage. Default expression matches the DPI Scale for monitor 0 of TouchDesigner.
- Use Shared Texture `sharedtexture` - Share a Direct3d 11 texture between TouchDesigner and TouchDesignerWebRender process instead of using shared memory, which is less efficient. Windows only.
- User Cache Directory `userdir` - Persistent directory used by cef for storing user data. Note that the directory must be unique per Web Render TOP, otherwise the TOP will error. By default, a temporary user cache directory is generated for each Web Render TOP.
- Modify Header DAT `headerdat` - Modify request headers for a given url. Specify a table with columns Name, Value & URL. For a matching URL in the url columen, the corresponding name and value will be inserted into the request header map, replacing any existing values.
- Options `options` - Additional options that can be passed to the browser process. This option will restart the browser process. A list of options for the chromium browser can be found at [here](https://peter.sh/experiments/chromium-command-line-switches/). Note that these options may change without notice with version updates.
- Restart if Process Died `autorestart` - Automatically restart the browser process if it died.
- Restart `autorestartpulse` - Triggers the Restart immediately on button release (button-up). This can be accessed in python using the pulse() method.
## Parameters - Common Page
- Output Resolution `outputresolution` - ⊞ - quickly change the resolution of the TOP's data.
  * Use Input `useinput` - Uses the input's resolution
  * Eighth `eighth` - Multiply the input's resolution by that amount.
  * Quarter `quarter` - Multiply the input's resolution by that amount.
  * Half `half` - Multiply the input's resolution by that amount.
  * 2X `2x` - Multiply the input's resolution by that amount.
  * 4X `4x` - Multiply the input's resolution by that amount.
  * 8X `8x` - Multiply the input's resolution by that amount.
  * Fit Resolution `fit` - Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
  * Limit Resolution `limit` - Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
  * Custom Resolution `custom` - Directly control the width and height.

- Resolution `resolution` - ⊞ - Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions.
  * W `resolutionw` -
  * H `resolutionh` -

- Resolution Menu `resmenu` - A drop-down menu with some commonly used resolutions.
- Use Global Res Multiplier `resmult` - Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier.
- Output Aspect `outputaspect` - ⊞ - Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.)
  * Use Input `useinput` - Uses the input's aspect ratio.
  * Resolution `resolution` - Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
  * Custom Aspect `custom` - Lets you explicitly define a custom aspect ratio in the Aspect parameter below.

- Aspect `aspect` - ⊞ - Use when Output Aspect parameter is set to Custom Aspect.
  * Aspect1 `aspect1` -
  * Aspect2 `aspect2` -

- Aspect Menu `armenu` - A drop-down menu with some commonly used aspect ratios.
- Input Smoothness `inputfiltertype` - ⊞ - This controls pixel filtering on the input image of the TOP.
  * Nearest Pixel `nearest` - Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
  * Interpolate Pixels `linear` - Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
  * Mipmap Pixels `mipmap` - Uses [ mipmap](https://docs.derivative.ca/Mipmapping "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.

- Fill Viewer `fillmode` - ⊞ - Determine how the TOP image is displayed in the viewer.
**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing.
  * Use Input `useinput` - Uses the same Fill Viewer settings as it's input.
  * Fill `fill` - Stretches the image to fit the edges of the viewer.
  * Fit Horizontal `width` - Stretches image to fit viewer horizontally.
  * Fit Vertical `height` - Stretches image to fit viewer vertically.
  * Fit Best `best` - Stretches or squashes image so no part of image is cropped.
  * Fit Outside `outside` - Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
  * Native Resolution `nativeres` - Displays the native resolution of the image in the viewer.

- Viewer Smoothness `filtertype` - ⊞ - This controls pixel filtering in the viewers.
  * Nearest Pixel `nearest` - Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
  * Interpolate Pixels `linear` - Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
  * Mipmap Pixels `mipmap` - Uses [ mipmap](https://docs.derivative.ca/Mipmapping "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).

- Passes `npasses` - Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image.
- Channel Mask `chanmask` - Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default.
- Pixel Format `format` - ⊞ - Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](https://docs.derivative.ca/Pixel_Formats "Pixel Formats") for more information.
  * Use Input `useinput` - Uses the input's pixel format.
  * 8-bit fixed (RGBA) `rgba8fixed` - Uses 8-bit integer values for each channel.
  * sRGB 8-bit fixed (RGBA) `srgba8fixed` - Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](https://docs.derivative.ca/SRGB "SRGB").
  * 16-bit float (RGBA) `rgba16float` - Uses 16-bits per color channel, 64-bits per pixel.
  * 32-bit float (RGBA) `rgba32float` - Uses 32-bits per color channel, 128-bits per pixels.
  * 10-bit RGB, 2-bit Alpha, fixed (RGBA) `rgb10a2fixed` - Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
  * 16-bit fixed (RGBA) `rgba16fixed` - Uses 16-bits per color channel, 64-bits total per pixel.
  * 11-bit float (RGB), Positive Values Only `rgba11float` - A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
  * 16-bit float (RGB) `rgb16float` -
  * 32-bit float (RGB) `rgb32float` -
  * 8-bit fixed (Mono) `mono8fixed` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
  * 16-bit fixed (Mono) `mono16fixed` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
  * 16-bit float (Mono) `mono16float` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
  * 32-bit float (Mono) `mono32float` - Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
  * 8-bit fixed (RG) `rg8fixed` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
  * 16-bit fixed (RG) `rg16fixed` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
  * 16-bit float (RG) `rg16float` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
  * 32-bit float (RG) `rg32float` - A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
  * 8-bit fixed (A) `a8fixed` - An Alpha only format that has 8-bits per channel, 8-bits per pixel.
  * 16-bit fixed (A) `a16fixed` - An Alpha only format that has 16-bits per channel, 16-bits per pixel.
  * 16-bit float (A) `a16float` - An Alpha only format that has 16-bits per channel, 16-bits per pixel.
  * 32-bit float (A) `a32float` - An Alpha only format that has 32-bits per channel, 32-bits per pixel.
  * 8-bit fixed (Mono+Alpha) `monoalpha8fixed` - A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
  * 16-bit fixed (Mono+Alpha) `monoalpha16fixed` - A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
  * 16-bit float (Mono+Alpha) `monoalpha16float` - A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
  * 32-bit float (Mono+Alpha) `monoalpha32float` - A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.

## Info CHOP Channels
Extra Information for the Web Render TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Web Render TOP Info Channels
  * num_handle_updates - Number of updates received from cef

  * loaded - Page load state

  * update_frame - Last update frame

  * update_abs_frame - Last update in absolute frames

  * updates_per_second - Frame rate for received images

  * num_skipped_updates - Number of updates received but not rendered

  * error_code - Web page error code

  * audio - Audio state. 1 if audio has started in the Web Render process.

###
## Common TOP Info Channels
  * resx - Horizontal resolution of the TOP in pixels.

  * resy - Vertical resolution of the TOP in pixels.

  * aspectx - Horizontal aspect of the TOP.

  * aspecty - Vertical aspect of the TOP.

  * depth - Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.

  * gpu_memory_used - Total amount of texture memory used by this TOP.

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
