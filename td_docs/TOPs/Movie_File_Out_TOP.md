---
url: https://docs.derivative.ca/Movie_File_Out_TOP
category: TOPs
title: Movie_File_Out_TOP
---

# Movie File Out TOP
## Summary

The Movie File Out TOP saves a TOP stream out to a movie file (`.mov`/`.mp4`) using a variety of codecs, including the H.264/H.265, [Hap Q](https://docs.derivative.ca/Hap "Hap"), [NotchLC](https://docs.derivative.ca/NotchLC "NotchLC"), [Apple ProRes](https://docs.derivative.ca/Apple_ProRes "Apple ProRes") and Animation video codecs. It can also save single frame images, image sequences, or stop-frame movies.
For codecs that support Alpha, use the 'Movie Pixel Format' parameter to select a format that includes alpha.
The [Export Movie Dialog](https://docs.derivative.ca/Export_Movie_Dialog "Export Movie Dialog") is a user interface built around the Movie File Out TOP.
To record movies with audio using the Movie File Out TOP, a [Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing") CHOP with mono or stereo channels of audio is required. If TouchDesigner is running at a lower frame rate than the target video frame rate and a CHOP is specified for audio, the Movie File Out TOP will automatically repeat video frames to ensure the video and audio stay in sync.
Recording a movie without frame drops can be done in non-realtime by turning off the Realtime flag at the top of the user interface. The length of the video is not predetermined and depends on the amount of time the Record parameter is on.
You can record a sequence of `.tif` or `.exr` files by setting the Type parameter to Image Sequence. When Image File Type is set to OpenEXR, the EXR page has options to record any number of color channels from multiple TOPs into an EXR image file, and can create it with metadata that would get read by a [Point File In TOP](https://docs.derivative.ca/Point_File_In_TOP "Point File In TOP").
The audio codecs that can be written out to file are ALAC (Apple Lossless), MP3, AAC, Vorbis, Opus, Uncompressed 16/32/64-bit (PCM).
**H264/H265/AV1 NOTE:** Encoding movies in H.264/H.265/AV1 codec is only available with a [Commercial](https://docs.derivative.ca/TouchDesigner_Commercial "TouchDesigner Commercial") or [Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro") license. NVIDIA graphic hardware is also required on Windows. On macoOS H264 is supported.
Recording still images and stop-frame animation can be done by changing the 'Type' parameter. Then the 'Add Frame' pulse button can be pulsed manually or via a script to cause the frames to be written.
See also [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP"), [Recording Movies with Audio](https://docs.derivative.ca/Recording_Movies_with_Audio "Recording Movies with Audio"), [Video Stream Out TOP](https://docs.derivative.ca/Video_Stream_Out_TOP "Video Stream Out TOP").
[moviefileoutTOP_Class](https://docs.derivative.ca/MoviefileoutTOP_Class "MoviefileoutTOP Class")

## Parameters - Movie Out Page
- Type `type` - ⊞ - Output either a movie, image, image sequence, or stop-frame movie.
  * Movie `movie` - Records a movie file.
  * Image `image` - Records a single image.
  * Image Sequence `imagesequence` - Records a sequence of images.
  * Stop-Frame Movie `stopframemovie` -

- Video Codec `videocodec` - ⊞ - Select the video compression codec used to encode the movie.
  * Animation `rle` - Run-length encoded video, lossless codec and low decode times, but very large file size. Alpha channel can be included when Pixel Format is RGBA.
  * Photo/Motion JPEG `mjpa` - JPEG encoded video, lossy codec and low decode times with medium file sizes. Good for playback both forwards and backwards or for random access.
  * MPEG 4 (Part 2) `mpeg4` - High quality but can produce large files size and/or have high decode times.
  * H.264 (NVIDIA GPU) `h264nvgpu` - H.264 GPU encoding, only available when using Nvidia graphics cards. Great compression and quality and small file sizes. However can suffer from high decode times and not the best for random access, scrubbing, or reverse playback. See the H264 parameter page for additional H264 encoding options.
  * GoPro-Cineform `cineform` - A lossy compression similar to Apple ProRes. Alpha channel can be included.
  * Hap `hap` - See [Hap](https://docs.derivative.ca/Hap "Hap"), a fast codec that uses the GPU. Has many different sub-types that can be chosen from.
  * H.265/HEVC (NVIDIA GPU) `h265nvgpu` - H.265 GPU encoding, only available when using Nvidia graphics cards. Better compression (and sometimes quality) than H.264 but more resource intensive to encode/decode.
  * GIF `gif` - An animated [.gif](https://en.wikipedia.org/wiki/GIF) file. Because there is no way to specific the color palette currently, a default palette will be used.
  * NotchLC `notchlc` - [NotchLC](https://docs.derivative.ca/NotchLC "NotchLC") is a high quality, GPU accelerated video format. It offers higher quality results than HapQ, at the cost of higher GPU usage as well as larger file sizes.
  * VP8 `vp8` - The open standard [VP8](https://en.wikipedia.org/wiki/VP8) format. Somewhat comparable to H264.
  * VP9 `vp9` - The open standard [VP9](https://en.wikipedia.org/wiki/VP9) format. Somehwat comaparable to HEVC/H265.
  * Apple ProRes `prores` - [Apple ProRes](https://docs.derivative.ca/Apple_ProRes "Apple ProRes") video format.
  * VVC/H.266 (Slow) `vvc` - Use H.266 to encode. This is currently CPU-based and quite slow.
  * AV1 (NVIDIA GPU) `av1` - An open source lossy compression format. See <https://en.wikipedia.org/wiki/AV1>.

- Video Codec Type `videocodectype` - Some video codecs such as [Apple ProRes](https://docs.derivative.ca/Apple_ProRes "Apple ProRes"), [Hap](https://docs.derivative.ca/Hap "Hap") and [Hap Q](https://docs.derivative.ca/Hap "Hap") have a various different types such as ProRes 442 HQ, ProRe 4444 HQ etc.
- Image File Type `imagefiletype` - ⊞ - Choose what file type to use when Type is set to Image.
  * TIFF `tiff` - A lossless, compressed, image format that includes alpha.
  * JPEG `jpeg` - A lossy image format, very well compressed. No support for alpha.
  * BMP `bmp` - A lossless, uncompressed, image format that includes alpha.
  * OpenEXR `exr` - A lossless, compressed, image format that can save files in 16-bit float and 32-bit float formats. Can also include alpha. More information [here](https://en.wikipedia.org/wiki/OpenEXR).
  * PNG `png` - A lossless, compressed, image format that can include alpha. Supports bit 8-bit and 16-bit fixed data.
  * DDS `dds` - A lossless, uncompressed, image format that can include alpha. Can include mipmap information. Natively support most pixel formats supported by TOPs.

- Unique Suffix `uniquesuff` - When enabled, me.fileSuffix will be a unique suffix when used in the file parameter.
- N `n` - N is the index used in me.fileSuffix. When unique suffix is enabled, N specifies the starting index to increment from when calculating a unique suffix/name.
- Leading Zeros Digits `leadingzerosdigits` - Specify the minimum number of suffix digits that the filename will have. If the sequence number is less than this number, leading zeros will be appended to total the number of suffix digits to be this value. Enabled only for Image Sequences.
- File `file` - Sets the path and filename of the movie file that is saved out. The filename must include the file extension such as .mov/.mp4 etc. For movies, generally the .mov file extension will work with the most codecs.
- Movie Pixel Format `moviepixelformat` - ⊞ - Options for the pixel format based on the Video Codec selected. Use this parameter to change the color quality of the output (how many bits are used, YUV sampling etc.), as well as selecting formats that include alpha for codecs that support alpha.
  * YUV 4:2:0 `yuv420` - (Photo/Motion JPEG, MPEG 4 (Part 2), )
  * YUV 4:2:0 (8-Bit) `yuv420` - (H.264 (NVIDIA GPU), H.265/HEVC (NVIDIA GPU))
  * YUV 4:2:0 (10-Bit) `yuv420p10bit` - (H.265/HEVC (NVIDIA GPU))
  * YUV 4:2:2 `yuv422` - (Photo/Motion JPEG, )
  * YUV 4:4:4 (8-Bit) `yuv444` - (H.264 (NVIDIA GPU), H.265/HEVC (NVIDIA GPU))
  * YUV 4:4:4 (10-Bit) `yuv444p10bit` - (H.265/HEVC (NVIDIA GPU))
  * RGB `rgb` - (Animation, Hap, Hap Q)
  * RGBA `rgba` - (Animation, GoPro-Cineform, Hap, Hap Q)
  * RGBA BC7 `rgba` - (Hap Q) - Slow, Read Help Before Using!
  * RGB Palette `3` - (GIF)

- Movie Container `moviecontainer` - ⊞ - Controls the movie container (file extension/format) that the file will be written into. Certain codecs require certain containers, and some containers don't support all codecs.
  * Automatic `automatic` - Automatically choose the container based on the preferred one for the video codec selected.
  * mov `mov` - Quicktime .mov container.
  * mp4 `mp4` - [MP4 (formally MPEG-4 Part 14)](https://en.wikipedia.org/wiki/MP4_file_format)
  * mkv `mkv` - An open source container that supports almost every video/audio combination. [Matroska](https://en.wikipedia.org/wiki/Matroska)
  * webm `webm` - Used to hold VP8/VP9 video codec files.

- Video Pixel Format `videopixelformat` - ⊞ - Options for the pixel format based on the Video Codec selected. Use this parameter to change the color quality of the output (how many bits are used, YUV sampling etc.), as well as selecting formats that include alpha for codecs that support alpha.
  * YUV 4:2:0 `yuv420` -
  * YUV 4:2:2 `yuv422` -

- Output Color Space `outputcolorspace` - ⊞ - Controls what color space the data will be converted to before output. If the output (file/SDI/ST2110 etc) supports metadata, will also attempt to include the color space in that. Some output forms only support a limited number of color spaces in their metadata. If the color space is unknown to the output form, then no metadata will be included.
  * sRGB `srgb` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
  * sRGB - Linear `srgblinear` - [sRGB](https://en.wikipedia.org/wiki/SRGB) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.601 (NTSC) `rec601ntsc` - [Rec.601](https://en.wikipedia.org/wiki/Rec._601) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.709 `rec709` - [Rec.709](https://en.wikipedia.org/wiki/Rec._709) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
  * Rec.2020 `rec2020` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
  * Rec.2020 ST2084PQ `rec2020st2084pq` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with [Perceptual Quantizer](https://en.wikipedia.org/wiki/Perceptual_quantizer) transfer function. Considered an HDR color space with respect to Reference White.
  * Rec.2020 HLG `rec2020hlg` - [Rec.2020](https://en.wikipedia.org/wiki/Rec._2020) color space, with [Hybrid Log Gamma](https://en.wikipedia.org/wiki/Hybrid_log%E2%80%93gamma) transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 `dcip3` - [DCI-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * DCI-P3 (D60) `dcip3d60` - [DCI-P3 "D60 sim"](https://en.wikipedia.org/wiki/DCI-P3) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) `displayp3d65` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
  * Display-P3 (D65) - Linear `displayp3d65linear` - [Display-P3](https://en.wikipedia.org/wiki/DCI-P3) color space, with D65 white point, and linear transfer function. Considered an HDR color space with respect to Reference White.
  * ACES2065-1 `aces2065-1` - [ACES 2065-1](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACEScg `acescg` - [ACEScg](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
  * ACESproxy `acesproxy` - [ACESproxy](https://en.wikipedia.org/wiki/Academy_Color_Encoding_System) color space, which has a log transfer function. Considered an HDR color space with respect to Reference White.
  * Passthrough `passthrough` - When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.

- Output Reference White `outputreferencewhite` - ⊞ - When converting the color values to the Working Color Space for output, this controls how they should be treated with respect to [Reference White](https://docs.derivative.ca/Color_Space#Reference_White "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Output Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, and the project Working Color Space is HDR while the Output Color Space is SDR: then a color of (1, 1, 1), which is 80 nits in the HDR color space, will be converted to be (0.66, 0.66, 0.66), which is 80 nits still in the SDR Output Color Space.
  * Default For Color Space `default` - Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
  * Standard (SDR) `sdr` - Will treat the Output Color Space as SDR for it's reference white value.
  * High (HDR) `hdr` - Will treat the Output Color Space as HDR for it's reference white value.

- Audio CHOP `audiochop` - Specify a CHOP to use as the audio track for the movie. Drag & Drop a CHOP here or manually enter the CHOP's path. **The CHOP needs to be [time-sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")**.
- Audio Bit Rate `audiobitrate` - ⊞ - The bitrate to write the audio out at. Depending on the codec this may be per-channel, or overall for all channels combined.
  * ALAC (Apple Lossless) `alac` - A lossless audio codec that still offers some compression for the data.
  * MP3 `mp3` - Compressed lossy codec. Can only do 2 channels of audio. MP3 compression will not have gapless playback.
  * AAC `aac` - [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding) is a lossy audio compression codec. Can only do 2 channels of audio. MP3 compression will not have gapless playback. Note: A particlular behavior on Windows OS AAC encoder; for 1 and 2 channels the selection of bit rate is for both channels combined. i.e. it’s 192kb/s for one channel, or 2x96kb/s for two. However, when using more than 2 channels the bitrate is per channel ie. for 6 channel then it’s 6x192kb/s.
  * Vorbis `vorbis` - [Vorbis](https://en.wikipedia.org/wiki/Vorbis) is a lossy audio compression codec. Vorbis compression will have gapless playback.
  * Opus `opus` - [Opus](https://en.wikipedia.org/wiki/Opus_\(audio_format\)) is a lossy audio compression codec.
  * Uncompressed 16-bit (PCM) `pcm16` - Uncompressed audio (Pulse Code Modulation)
  * Uncompressed 24-bit (PCM) `pcm24` - Uncompressed audio (Pulse Code Modulation)
  * Uncompressed 32-bit (PCM) `pcm32` - Uncompressed audio (Pulse Code Modulation)
  * 128 kb/s `b128` -
  * 192 kb/s `b192` -
  * 256 kb/s `b256` -
  * 320 kb/s `b320` -

- Quality `quality` - Select the quality of the movie compression. NOTE: Some codecs can not output lossless compression.
- Movie FPS `fps` - The frame rate of the movie file created.
- Limit Length `limitlength` - This can be used to automatically stop recording the file once it reaches a specified length.
- Length `length` - The length to stop recording the file at.
- Length Unit `lengthunit` - ⊞ - The unit the length is specified in.
  * I `indices` -
  * F `frames` -
  * S `seconds` -

- Record `record` - When this parameter is set to 1, the movie will be recording.
- Pause `pause` - Pauses the recording.
- Add Frame `addframe` - Adds a single frame to the output for each click of the button. Pause must be **On** to enable the Add Frame parameter.
- Max Threads `maxthread` - When outputting sequences of images, this controls the maximum number of threads can be used to output images (one thread per image). If this is set to 1 then the main thread will be used to write the image.
- Header Source DAT `headerdat` - The path to a Table DAT that stores header metadata that should be written to the output image or movie file. Header data is written as key-value pairs with the first column storing the keys and the second column storing the associated values. See [File Metadata](https://docs.derivative.ca/File_Metadata "File Metadata") for more information on supported metadata. **Note:** Currently only supported for EXR files. **Warning:** Files may fail to save if the header data conflicts with system headers.

## Parameters - EXR Page
The Inputs page can be used to add extra channels of image data to the output file and to change the names of the base 4 channels.
Each 'Additional Input TOP' is a path to a TOP containing the image data to add to the file. The associated Red, Green, Blue and Alpha parameters are the names assigned to that input's channels in the new file. If the channel parameter is left blank, that channel will not be added to the output file. Channels with duplicate names will be overwritten.
**Note:** Additional inputs are currently only supported in EXR images and sequences. In EXR files, channels are stored in alphabetical order.
- Save as Point Cloud `pointcloud` - When enabled, an additional header will be added to the file that indicates the contents are point data rather than images. This header is used to automatically load the file into a [Point File In TOP](https://docs.derivative.ca/Point_File_In_TOP "Point File In TOP") rather than a [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") when dragging and dropping.
- Additional Input TOP `input` - Sequence of TOPs containing image data to add to the file
- Red `input0r` - Name assigned to the specified TOP's Red channel.
- Green `input0g` - Name assigned to the specified TOP's Green channel.
- Blue `input0b` - Name assigned to the specified TOP's Blue channel.
- Alpha `input0a` - Name assigned to the specified TOP's Alpha channel.
- TOP `input1top` - The path to the TOP used to specify addition channels to the EXR file. The first 4 channels specified above come from the input connected to the Movie File Out TOP, this TOPs RGBA data can be assigned unique names in the EXR file using the Red, Green, Blue, Alpha parameters below.
- TOP `input0top` -

## Parameters - Settings Page
- Stall for File Open `stallforopen` - When this is on playback will stall until the file is opened and ready to receive frames, to make sure the frame that was inputted when Record was turned on gets recorded. When this is off recording may start on a later frame, after the file has been opened. Turning this off can avoid a stall in playback, if missing recording some frames at the start is acceptable.
- Start Timecode `starttimecode` -
- Profile `profile` - ⊞ - Select the H.264 profile to use.
  * Auto-Select `autoselect` -
  * Baseline `baseline` -
  * Main `main` -
  * High `high` -

- Preset `preset` - ⊞ - The H264 preset to use.
  * None `none` - Select from the available presets.
  * Lossless `lossless` -

- Bit Rate Mode `bitratemode` - ⊞ - Select between Constant or Variable bit rate, and regular or high quality bit rate modes.
  * Constant (CBR) `constant` -
  * Variable (VBR) `variable` -
  * Constant HQ (CBR) `constanthq` -
  * Variable HQ (VBR) `variablehq` -

- Average Bitrate (Kb/s) `avgbitrate` - Set the average bitrate target for the encoding.
- Peak Bitrate (Kb/s) `peakbitrate` - Set the peak bitrate allowed for the encoding.
- Keyframe Interval `keyframeinterval` - Set the number of frames between key-frames (I-frames) while encoding.
- Max B-Frames `maxbframes` - Controls the maximum number of B-frames (bi-directional frames) that will be created between pairs of key-frames.
- Motion Prediction `motionpredict` - ⊞ - Controls the quality of the Motion Prediction used when encoding H264/H265.
  * Default `default` -
  * Quarter `quarter` -
  * Half `half` -
  * Full `full` -

- Frame Slicing `frameslicing` - Controls if H264/H265 frames are sliced into multiple pieces, allowing them to be decoded using multiple CPUs more easily.
- Num Slices `numslices` - The number of slices each frame is split into.
- Entropy Mode `entropymode` - ⊞ - Controls which entropy mode is used for H265 encoding.
  * Auto-Select `autoselect` -
  * CABAC `cabac` -
  * CAVLC `cavlc` -

- Stereo Mode `stereomode` - ⊞ - Adds metadata to the file to denote that it contains a stereo pair of images in either Left-Right or Top-Bottom formatting. The TOP connected as the input needs to already be in this format, usually by using a [Layout TOP](https://docs.derivative.ca/Layout_TOP "Layout TOP").
  * Off `off` - No metadata is included.
  * Left-Right `leftright` - The metadata denotes that the content should be treated as the left half is the left eye, and the right half is the right eye.
  * Top-Bottom `topbottom` - The metadata denotes that the content should be treated as the top half is the left eye, and the bottom half is the right eye.

- Spherical Mode `sphericalmode` - ⊞ - Adds metadata to the file to denote that it contains a spherical 360 degree rendered output. This is usually created by using the [Projection TOP](https://docs.derivative.ca/Projection_TOP "Projection TOP").
  * Off `off` - No metadata is included.
  * Equirectangular `equirectangular` - The metadata denotes that the content is in Equirectuangular projection format.

- Secondary Compression `secondarycompression` - [Hap](https://docs.derivative.ca/Hap "Hap") uses a secondary CPU compression stage usually. Encoding video without this compression will result in faster playback, but potentially larger file sizes (which would require faster drives to play back).
- Encode Test Mode `encodetestmode` - This mode disables file writting, and only does the encoding. This is useful to test the GPU/CPU performance of encoding while taking the SSD speed out of the equation.
- Include Mip Maps `mipmaps` - When saving out .dds file, mipmaps can be included if this is enabled. This is primarily used for the [PreFilter Map TOP](https://docs.derivative.ca/PreFilter_Map_TOP "PreFilter Map TOP"), which will encode special information into the mipmap levels of the texture which needs to be maintained.

## Parameters - Common Page
- Output Resolution `outputresolution` - ⊞ - quickly change the resolution of the TOP's data.
  * Use Input `useinput` - Uses the input's resolution.
  * Eighth `eighth` - Multiply the input's resolution by that amount.
  * Quarter `quarter` - Multiply the input's resolution by that amount.
  * Half `half` - Multiply the input's resolution by that amount.
  * 2X `2x` - Multiply the input's resolution by that amount.
  * 4X `4x` - Multiply the input's resolution by that amount.
  * 8X `8x` - Multiply the input's resolution by that amount.
  * Fit Resolution `fit` - Fits the width and height to the resolution given below, while maintaining the aspect ratio.
  * Limit Resolution `limit` - The width and height are limited to the resolution given below. If one of the dimensions exceeds the given resolution, the width and height will be reduced to fit inside the given limits while maintaining the aspect ratio.
  * Custom Resolution `custom` - Enables the Resolution parameter below, giving direct control over width and height.

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
  * Mipmap Pixels `mipmap` - Uses [ mipmap](https://docs.derivative.ca/Mipmapping "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.

- Passes `npasses` - Duplicates the operation of the TOP the specified number of times. Making this larger than 1 is essentially the same as taking the output from each pass, and passing it into the first input of the node and repeating the process. Other inputs and parameters remain the same for each pass.
- Channel Mask `chanmask` - Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default.
- Pixel Format `format` - ⊞ - Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](https://docs.derivative.ca/Pixel_Formats "Pixel Formats") for more information.
  * Use Input `useinput` - Uses the input's pixel format.
  * 8-bit fixed (RGBA) `rgba8fixed` - Uses 8-bit integer values for each channel.
  * sRGB 8-bit fixed (RGBA) `srgba8fixed` - Uses 8-bit integer values for each channel and stores color in sRGB colorspace.
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

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Movie File Out TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Movie File Out TOP Info Channels
  * last_frames_written - The number of frames written to the file on the last cook. This many be multiple repeats of the same image if TouchDesigner dropped frames, to ensure time stays in sync.

  * total_frames_written - The total number of frames written to the file so far.

  * last_audio_samples_written - The number of audio samples written to the file on the last cook.

  * total_audio_samples_written - The total number of audio samplers written to the file.

  * last_audio_frames_written - The number of audio frames written to the file on the last cook. This is the samples value, converted to frame units.

  * total_audio_frames_written - The total number of audio frames written to the file. This is the samples value, converted to frame units.

  * total_frames_dropped - The number frames that TouchDesigner failed to provide unique images for in the output file. This occurs when TouchDesigner drops frames when the file needed new images.

  * active_records - When recording sequences of images, they may be written using multiple CPUs at the same time. This tells how many images are currently being recorded.

  * cur_seq_index - When recording sequences of images, this is the current sequence image index.

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
