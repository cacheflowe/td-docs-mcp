---
url: https://docs.derivative.ca/File_Types
category: Interoperability
title: File_Types
---

# File Types

TouchDesigner can import and export most common media file formats. Files can be loaded into TouchDesigner by:
  * [Drag-and-Drop](https://docs.derivative.ca/Drag-and-Drop "Drag-and-Drop"): Drag a file directly into TouchDesigner and drop it to automatically create an OP or a component.
  * Open With... menu: Right-click on a TouchDesigner supported file in Windows and select Open With...->TouchDesigner 0xx to launch TouchDesigner with the file pre-loaded.
  * Load a file using Operators like [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP"), [File In CHOP](../CHOPs/File_In_CHOP.md "File In CHOP"), [File In SOP](../SOPs/File_In_SOP.md "File In SOP"), [Audio File In CHOP](../CHOPs/Audio_File_In_CHOP.md "Audio File In CHOP"). Files can be loaded from disk or from the web using http://_file-url_.
  * Start TouchDesigner using the operating system shell command `touchdesigner filename.ext`, which will start TouchDesigner with your file pre-loaded.

##  Native TouchDesigner Files

TouchDesigner has three native files types:
  * [.toe](../Glossary/.toe.md ".toe"): TouchDesigner Environment files are the default file type for creating projects.
  * [.tox](../Glossary/.tox.md ".tox"): TouchDesigner Component files let you save out components. .tox files enable the re-use and portability of component libraries.
  * [.tog](https://docs.derivative.ca/.tog ".tog"): TouchDesigner Geometry files are exports of other geometry types in a native TouchDesigner format.

##  Files Imported

File Type | Supported Extensions | Operator Type
---|---|---
Image | `.tif .tiff .bmp .gif .hdr .jpeg .jpg .pic .png .swf .tga .dds .exr .dpx .ffs` |  [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP")
Movie | `.m4v .mkv .mov .mp4 .hsp .notchlc .mpeg .mpg .avi .flv .m2ts .wmv  .h265 .vp8 .vp9 .3gp .mxf .ts .r3d` |  [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP")
Point Cloud | `.obj .ply .exr .xyz .pts .csv .txt .fits/.fit(astronomy format)` |  [Point File In POP](../POPs/Point_File_In_POP.md "Point File In POP"), [Point File In TOP](../TOPs/Point_File_In_TOP.md "Point File In TOP")
Audio | `.aif .aiff .wav .mp3 .flac .ogg .m4a .avi .flv .m2ts .m4v .mkv .mov .mp4 .mpeg .mpg .mts .wmv .3gp .mxf .ts .r3d` |  [Audio File In CHOP](../CHOPs/Audio_File_In_CHOP.md "Audio File In CHOP"), [Audio Play CHOP](../CHOPs/Audio_Play_CHOP.md "Audio Play CHOP"), [File In CHOP](../CHOPs/File_In_CHOP.md "File In CHOP")
Geometry and Scene | `.usd, .usda, usdc, .usdz[](USD.md "USD") .fbx[](FBX.md "FBX") .obj .3ds .dxf .dae .abc ` |  [USD COMP](../COMPs/USD_COMP.md "USD COMP"), [FBX COMP](../COMPs/FBX_COMP.md "FBX COMP"), [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP"), [File In POP](../POPs/File_In_POP.md "File In POP"), [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP"), [Alembic Out POP](https://docs.derivative.ca/Alembic_Out_POP "Alembic Out POP")
Shader |  `.glsl .frag .vert`, geometry shaders |  [Text DAT](../Glossary/Text_DAT.md "Text DAT")
JSON | `.json` |  [JSON DAT](../DATs/JSON_DAT.md "JSON DAT")
Channel (Houdini) | .`bchan .bclip .chan .clip` |  [File In CHOP](../CHOPs/File_In_CHOP.md "File In CHOP")
Geometry (Houdini) | `.bhclassic .hclassic` |  [File In POP](../POPs/File_In_POP.md "File In POP")
MIDI | `.mid .midi` |  [MIDI In CHOP](../CHOPs/MIDI_In_CHOP.md "MIDI In CHOP")
Script | `.bat .cmd .txt` |  [Text DAT](../Glossary/Text_DAT.md "Text DAT")
Table | `.csv .dat` |  [Table DAT](../Glossary/Table_DAT.md "Table DAT")
Font | `.ttf .otf` |  [Text COMP](../COMPs/Text_COMP.md "Text COMP"), [Geo Text COMP](../COMPs/Geo_Text_COMP.md "Geo Text COMP")
The Movie File In TOP also supports audio embedded in a movie. **Tip** : Tie an [Audio Movie CHOP](../CHOPs/Audio_Movie_CHOP.md "Audio Movie CHOP") to the Movie File In TOP to get the audio, then an [Audio Device Out CHOP](Audio_Device_Out_CHOP.md "Audio Device Out CHOP") to play it. An [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP") attached to either operator gives extra inside info.

##  Files Exported

File Type | Supported Extensions | Operator Type or Dialog
---|---|---
Image | `.tif .tiff .jpeg .jpg .bmp .exr .png .dds` | File -> Create Movie, RMB menu
Movie | `.mov .mp4 .hap .notchlc .h265 .vp8 .vp9` |  [Movie File Out TOP](../TOPs/Movie_File_Out_TOP.md "Movie File Out TOP"), File -> Create Movie
Audio | `.aif .aiff .wav` | Save File on RMB menu
Project | `.toe` | File -> Save Env
Component and Scene | `.tox` | File -> Save, RMB menu components
Channel | `.bchan .bclip .chan .clip` |  [File Out CHOP](../CHOPs/File_Out_CHOP.md "File Out CHOP"), RMB menu
Geometry | `.tog .bhclassic .fbx .pop` | RMB menu
Geometry | `.obj .ply .e57 .pop` |  [File Out POP](../POPs/File_Out_POP.md "File Out POP")
Point Cloud | `.exr .ply .e57 .pop` |  [File Out POP](../POPs/File_Out_POP.md "File Out POP")
Gaussian Splat | `.spz .ply` |  [File Out POP](../POPs/File_Out_POP.md "File Out POP")
MIDI |  |  [MIDI Out CHOP](../CHOPs/MIDI_Out_CHOP.md "MIDI Out CHOP")
Shader | `.frag .glsl .vert` |  [Phong MAT](../MATs/Phong_MAT.md "Phong MAT")
Script | `.py .html .md .dat .rtf .tsv .txt .xml` | RMB menu
Table | `.dat` | RMB menu
An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

TouchDesigner Component file, the file type used to save a [Component](../Glossary/Component.md "Component") of your TouchDesigner project.

Any component can be extended with its own Python classes which contain python functions and data.

The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](../Glossary/Text_DAT.md "Text DAT") and referenced by a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](../General/Python.md "Python") and the original [Tscript](../Glossary/Tscript.md "Tscript"). Scripts and single-line commands can also be run in the [Textport](../Glossary/Textport.md "Textport").

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

Any floating window that is not a [Pane](../Glossary/Pane.md "Pane") or [Viewer](../Glossary/Viewer.md "Viewer").

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

A [CHOP](../Glossary/CHOP.md "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](../Glossary/Sample.md "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](../Glossary/Export.md "Export") to [Parameters](../Glossary/Parameter.md "Parameter").

The 3D data held in POPs and passed for rendering by the [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP").
