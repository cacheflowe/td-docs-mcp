---
url: https://docs.derivative.ca/File_Types
category: Interoperability
title: File_Types
---

# File Types
TouchDesigner can import and export most common media file formats. Files can be loaded into TouchDesigner by:
  * [Drag-and-Drop](https://docs.derivative.ca/Drag-and-Drop "Drag-and-Drop"): Drag a file directly into TouchDesigner and drop it to automatically create an OP or a component.
  * Open With... menu: Right-click on a TouchDesigner supported file in Windows and select Open With...->TouchDesigner 0xx to launch TouchDesigner with the file pre-loaded.
  * Load a file using Operators like [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP"), [File In CHOP](https://docs.derivative.ca/File_In_CHOP "File In CHOP"), [File In SOP](https://docs.derivative.ca/File_In_SOP "File In SOP"), [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP"). Files can be loaded from disk or from the web using http://_file-url_.
  * Start TouchDesigner using the operating system shell command `touchdesigner filename.ext`, which will start TouchDesigner with your file pre-loaded.

##  Native TouchDesigner Files
TouchDesigner has three native files types:
  * [.toe](https://docs.derivative.ca/.toe ".toe"): TouchDesigner Environment files are the default file type for creating projects.
  * [.tox](https://docs.derivative.ca/.tox ".tox"): TouchDesigner Component files let you save out components. .tox files enable the re-use and portability of component libraries.
  * [.tog](https://docs.derivative.ca/.tog ".tog"): TouchDesigner Geometry files are exports of other geometry types in a native TouchDesigner format.

##  Files Imported
File Type | Supported Extensions | Operator Type
---|---|---
Image | `.tif .tiff .bmp .gif .hdr .jpeg .jpg .pic .png .swf .tga .dds .exr .dpx .ffs` |  [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP")
Movie | `.m4v .mkv .mov .mp4 .hsp .notchlc .mpeg .mpg .avi .flv .m2ts .wmv  .h265 .vp8 .vp9 .3gp .mxf .ts .r3d` |  [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP")
Point Cloud | `.obj .ply .exr .xyz .pts .csv .txt .fits/.fit(astronomy format)` |  [Point File In TOP](https://docs.derivative.ca/Point_File_In_TOP "Point File In TOP")
Audio | `.aif .aiff .wav .mp3 .flac .ogg .m4a .avi .flv .m2ts .m4v .mkv .mov .mp4 .mpeg .mpg .mts .wmv .3gp .mxf .ts .r3d` |  [Audio File In CHOP](https://docs.derivative.ca/Audio_File_In_CHOP "Audio File In CHOP"), [Audio Play CHOP](https://docs.derivative.ca/Audio_Play_CHOP "Audio Play CHOP"), [File In CHOP](https://docs.derivative.ca/File_In_CHOP "File In CHOP")
Geometry and Scene | `.usd, .usda, usdc, .usdz[](https://docs.derivative.ca/USD "USD") .fbx[](https://docs.derivative.ca/FBX "FBX") .obj .3ds .dxf .dae .abc ` |  [USD COMP](https://docs.derivative.ca/USD_COMP "USD COMP"), [FBX COMP](https://docs.derivative.ca/FBX_COMP "FBX COMP"), [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP"), [File In SOP](https://docs.derivative.ca/File_In_SOP "File In SOP"), [Alembic SOP](https://docs.derivative.ca/Alembic_SOP "Alembic SOP")
Shader |  `.glsl .frag .vert`, geometry shaders |  [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT")
JSON | `.json` |  [JSON DAT](https://docs.derivative.ca/JSON_DAT "JSON DAT")
Channel (Houdini) | .`bchan .bclip .chan .clip` |  [File In CHOP](https://docs.derivative.ca/File_In_CHOP "File In CHOP")
Geometry (Houdini) | `.bhclassic .hclassic` |  [File In SOP](https://docs.derivative.ca/File_In_SOP "File In SOP")
MIDI | `.mid .midi` |  [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP "MIDI In CHOP")
Script | `.bat .cmd .txt` |  [Text DAT](https://docs.derivative.ca/Text_DAT "Text DAT")
Table | `.csv .dat` |  [Table DAT](https://docs.derivative.ca/Table_DAT "Table DAT")
Font | `.ttf .otf` |  [Text COMP](https://docs.derivative.ca/Text_COMP "Text COMP"), [Geo Text COMP](https://docs.derivative.ca/Geo_Text_COMP "Geo Text COMP")
The Movie File In TOP also supports audio embedded in a movie. **Tip** : Tie an [Audio Movie CHOP](https://docs.derivative.ca/Audio_Movie_CHOP "Audio Movie CHOP") to the Movie File In TOP to get the audio, then an [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP") to play it. An [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") attached to either operator gives extra inside info.
##  Files Exported
File Type | Supported Extensions | Operator Type or Dialog
---|---|---
Image | `.tif .tiff .jpeg .jpg .bmp .exr .png .dds` | File -> Create Movie, RMB menu
Movie | `.mov .mp4 .hap .notchlc .h265 .vp8 .vp9` |  [Movie File Out TOP](https://docs.derivative.ca/Movie_File_Out_TOP "Movie File Out TOP"), File -> Create Movie
Audio | `.aif .aiff .wav` | Save File on RMB menu
Project | `.toe` | File -> Save Env
Component and Scene | `.tox` | File -> Save, RMB menu components
Channel | `.bchan .bclip .chan .clip` |  [File Out CHOP](https://docs.derivative.ca/File_Out_CHOP "File Out CHOP"), RMB menu
Geometry | `.tog .bhclassic .fbx ` | RMB menu
MIDI |  |  [MIDI Out CHOP](https://docs.derivative.ca/MIDI_Out_CHOP "MIDI Out CHOP")
Shader | `.frag .glsl .vert` |  [Phong MAT](https://docs.derivative.ca/Phong_MAT "Phong MAT")
Script | `.py .html .md .dat .rtf .tsv .txt .xml` | RMB menu
Table | `.dat` | RMB menu
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
TouchDesigner Component file, the file type used to save a [Component](https://docs.derivative.ca/Component "Component") of your TouchDesigner project.
Any component can be extended with its own Python classes which contain python functions and data.
The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](https://docs.derivative.ca/Text_DAT "Text DAT") and referenced by a [GLSL Material](https://docs.derivative.ca/GLSL_MAT "GLSL MAT") or a [GLSL TOP](https://docs.derivative.ca/GLSL_TOP "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.
A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
Any floating window that is not a [Pane](https://docs.derivative.ca/Pane "Pane") or [Viewer](https://docs.derivative.ca/Viewer "Viewer").
TOuch Environment file, the file type used by TouchDesigner to save your entire project.
A [CHOP](https://docs.derivative.ca/CHOP "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](https://docs.derivative.ca/Export "Export") to [Parameters](https://docs.derivative.ca/Parameter "Parameter").
The 3D data held in SOPs and passed for rendering by the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP").
