---
url: https://docs.derivative.ca/DMX_In_CHOP
category: CHOPs
title: DMX_In_CHOP
---

# DMX In CHOP
## Summary

The DMX In CHOP receives channels from DMX, [Art-Net](https://docs.derivative.ca/Art-Net "Art-Net"), [sACN](https://docs.derivative.ca/SACN "SACN") or [KiNET](https://www.colorkinetics.com/global/learn/optics-matter) devices. Channel values for DMX are 0-255. Note that input rate is limited to the DMX maximum refresh rate of 44Hz.
A Filter Table can be provided in a DAT where addresses can be specified by adding rows for each channel and specifying **net** , **subnet** and **universe**. Optionally, packets can be filtered using the **srcaddress** and **destaddress** columns; only packets that have a matching source IP address and destination IP address will be accepted. The cell values for these columns should be a single IP address (ie. [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") **not** supported); if left blank then all packets will be accepted.
The **srcaddress** column is useful for when there is DMX noise on the network that needs to be filtered out; the IP of the desired controller can be specified in the **srcaddress** cell. The **id** column should be used in conjunction with **srcaddress** and **destaddress** to provide a unique channel suffix.
[Wireshark](https://www.wireshark.org/) is a useful tool for debugging network issues. In the Art-Net case, packets can easily be filtered using **artnet** , **dmx** , or **dmx_chan**.
**ENTTEC NOTE:** - Use ENTTEC's [NMU (Node Management Utility)](http://www.enttec.com/us/products/controls/dmx-over-ethernet/nmu/) to configure and inspect the ENTTEC devices found on your network.
See also: [DMX Out POP](https://docs.derivative.ca/DMX_Out_POP "DMX Out POP"), [Art-Net](https://docs.derivative.ca/Art-Net "Art-Net"), [DMX Out CHOP](https://docs.derivative.ca/DMX_Out_CHOP "DMX Out CHOP"), [DMX](https://docs.derivative.ca/DMX "DMX")
[dmxinCHOP_Class](https://docs.derivative.ca/DmxinCHOP_Class "DmxinCHOP Class")

## Parameters - Port Page
- Active `active` - Connects to the device while On.
- Interface `interface` - ⊞ - Select the type of interface to connect to the device with.
  * Enttec Generic Serial `serial` - Uses the operating system's serial calls to read data.
  * Enttec USB Pro `enttecusbpro` -
  * Enttec USB Pro Mk2 `enttecusbpromk2` -
  * Art-Net `artnet` - Sets the interface to [Art-Net](http://en.wikipedia.org/wiki/Art-Net) protocol.
  * sACN `sacn` - Sets the interface to [sACN](https://en.wikipedia.org/wiki/Architecture_for_Control_Networks) protocol.
  * KiNET `kinet` - Sets the interface to [KiNET](https://www.colorkinetics.com/global/learn/led-lighting-technology#KiNET) protocol.

- KiNET Version `kinetversion` - ⊞ - Set the version of the KiNET protocol to use.
  * DmxOut (v1) `v1` -
  * PortOut (v2) `v2` -

- Device `device` - Select a DMX device from the menu.
- Serial Port `serialport` - When the Interface parameter is set Generic Serial this parameter lets you select which Serial (COM) port to use.
- Format `format` - ⊞ - Select between receiving Packet Per Sample (Timesliced), Packet Per Channel (Latest) or Packet Per Channel (All). When selecting Packet Per Channel (Latest), any messages outside the last cook are being discarded while the option Packet Per Channel (All) will append channels that would get otherwise skipped by dropped frames.
  * Packet Per Sample (Timesliced) `packetpersample` -
  * Packet Per Channel (Latest) `packetperchan` -
  * Packet Per Channel (All) `packetperchanall` -

- Art-Net Net (0-127) `net` - When the Interface parameter is set to Art-Net, this sets the net address. A net is a groups of 16 consecutive subnets or 256 consecutive universes. The range for this parameter is 0-127. This is **not** a network IP address.
- Art-Net Subnet (0-15) `subnet` - When the Interface parameter is set to Art-Net, this sets the subnet address. A subnet is a group of 16 consecutive universes. The range for this parameter is 0-15. This is **not** a network subnet mask.
- Art-Net Universe (0-15) `universe` - When the Interface parameter is set to Art-Net, this sets the universe address. A single DMX512 frame of 512 channels is referred to as a universe. The range for this parameter is 0-15.
- Filter Table `filterdat` - Available when using Packet Per Channel Format for Art-Net or sACN. Use the docked Table DAT to specify which net, subnet, universe channels are being received from.
**Note:** For sACN the first available universe has the index 1 as universe 0 is reserved by the system for future use.
- Net Name `netname` - Specify the channel prefix for the net part of the address.
- Subnet Name `subnetname` - Specify the channel prefix for the subnet part of the address.
- Universe Name `universename` - Specify the channel prefix for the universe part of the address.
- KiNET Port Name `kinetportname` - Specify the channel prefix for the KiNET port part of the address.
- Start Codes `startcodes` - A list of accepted start codes when using sACN. If the DMX In CHOP receives an sACN packet with a start code not in the list then it will discard it.
- Multicast `multicast` - Enable multicast for sACN. Multicast automatically builds the IP based on Net, Subnet, and Universe of the device. This allows for the DMX In CHOP to automatically receive from a sender without knowledge of it's address.
- Queue Size `queuesize` - When using interface Art-Net or sACN, this will set the size of the incoming packets queue. This can be used to smooth data, though latency will be higher. In the case of Packet Per Channel (All), this parameter controls the maximum number of packets created per cook.
- Rate `rate` - Resample the incoming data to this rate.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).

## Info CHOP Channels
Extra Information for the DMX In CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

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
