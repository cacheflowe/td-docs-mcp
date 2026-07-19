---
url: https://docs.derivative.ca/NDI_DAT
category: DATs
title: NDI_DAT
---

# NDI DAT

## Summary

The NDI DAT lists in a table and monitors all NDI sources and streams found on the network. Callbacks are provided to trigger actions when sources are added/removed/changed and when streams start/stop.

See [NDI](../Interoperability/NDI.md "NDI"), [NDI In TOP](../TOPs/NDI_In_TOP.md "NDI In TOP") and [NDI Out TOP](../TOPs/NDI_Out_TOP.md "NDI Out TOP").

[ndiDAT_Class](NDI_DAT_Class.md "NdiDAT Class")

## Parameters - Monitors Page
- Callbacks DAT `callbacks` - Script callbacks for events relating to NDI sources and streams.
- Extra Search IPs `extraips` - By default NDI searches using mDNS, which is usually limited to locate networks. To find sources available on machines not reachable by mDNS, this parameter can be filled with a space-separated list of one or more IP address.
- Persistence (ms) `persistence` - Persistence affects how long an entry in the DAT stays present even after the source has disappeared. This allows for a source to disappear for a bit and then reappear without being removed from the list.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.
- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * frag `frag` -
  * glsl `glsl` -
  * html `html` -
  * md `md` -
  * py `py` -
  * rtf `rtf` -
  * tsv `tsv` -
  * txt `txt` -
  * vert `vert` -
  * xml `xml` -
  * From Language `languageext` - pick extension from DATs script language.
  * Custom Extension `customext` - Specify a custom extension.
- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Info CHOP Channels

Extra Information for the NDI DAT can be accessed via an [Info CHOP](../CHOPs/Info_CHOP.md "Info CHOP").

###

## Common DAT Info Channels

  * num_rows - Number of rows in this DAT.
  * num_cols - Number of columns in this DAT.

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
