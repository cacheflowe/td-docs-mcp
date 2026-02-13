---
url: https://docs.derivative.ca/ST2110_Device_CHOP
category: CHOPs
title: ST2110_Device_CHOP
---

# ST2110 Device CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
This node is used to configure the IP settings of a ST2110 Device such as the DHCP settings, IP configuration and PTP settings. Currently this node does not have any channels it outputs, but it does have some [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP") channels that give diagnostic information.
See also [ST2110 In TOP](https://docs.derivative.ca/ST2110_In_TOP "ST2110 In TOP"), [ST2110 Out TOP](https://docs.derivative.ca/ST2110_Out_TOP "ST2110 Out TOP").
[st2110deviceCHOP_Class](https://docs.derivative.ca/St2110deviceCHOP_Class "St2110deviceCHOP Class")

## Parameters - ST2110 Device Page
- Active `active` - Controls if this node is actively configuring this device's settings.
- Driver `driver` - ⊞ - Select which device driver to use to search and communicate with devices.
  * Blackmagic `blackmagic` - Use the Blackmagic driver.
  * Deltacast `deltacast` - Use the Deltacast driver.

- Device `device` - Select the device to configure.
- Use DHCP `usedhcp` - Chooses if the IP address of the primary port on the device should be configured using DHCP.
- IP Address `ipaddress` - Manually set the IP address, if DHCP is disabled.
- Subnet `subnet` - Manually set the subnet, if DHCP is disabled.
- Gateway `gateway` - Manually set the gateway, if DHCP is disabled.
- PTP Profile `ptpprofile` - ⊞ - Select the PTP profile to use, for devices that support selection.
  * Off `off` -
  * ST2059-2 `st2059-2` -
  * AES67 `aes67` -

- PTP Address `ptpaddress` - Manually set the address of the PTP grandmaster.
- PTP Domain `ptpdomain` - Manually set the PTP domain.
- IGMP Version `igmpversion` - ⊞ - Select the IGMP version(s) to use for multicast join/leave and other IGMP operations.
  * Version 2 `vesion2` -
  * Version 3 `version3` -
  * Version 2 and 3 `version2and3` -

## Parameters - SPS Page
- Enable SPS `enablesps` - Enables the SPS port on the device.
- Use DHCP `spsusedhcp` - Chooses if the IP address of the SPS port on the device should be configured using DHCP.
- SPS IP Address `spsipaddress` - Manually set the IP address, if DHCP is disabled.
- SPS Subnet `spssubnet` - Manually set the subnet, if DHCP is disabled.
- SPS Gateway `spsgateway` - Manually set the gateway, if DHCP is disabled.

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
Extra Information for the ST2110 Device CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific ST2110 Device CHOP Info Channels
  * packets_received - The number of packets received on the primary port, or -1 if this query isn't supported by the device.

  * packet_errors - The number of packets errors that occured on primary port, or -1 if this query isn't supported by the device.

  * multicast_groups_joined - The number of times a multicast group has been joined by primary port, or -1 if this query isn't supported by the device.

  * multicast_sources_added - The number of times a multicast source has been added by primary port, or -1 if this query isn't supported by the device.

  * multicast_changes - The number of multicast change operations that have occurred on the primary port, or -1 if this query isn't supported by the device.

  * ptp_locked - 1 if the PTP on the primary port is locked to a PTP grandmaster, 0 if PTP is not locked, or -1 if this query isn't supported by the device.

  * sps_packets_received - The number of packets received on the SPS port, or -1 if this query isn't supported by the device.

  * sps_packet_errors - The number of packets errors that occured on SPS port, or -1 if this query isn't supported by the device.

  * sps_multicast_groups_joined - The number of times a multicast group has been joined by SPS port, or -1 if this query isn't supported by the device.

  * sps_multicast_sources_added - The number of times a multicast source has been added by SPS port, or -1 if this query isn't supported by the device.

  * sps_multicast_changes - The number of multicast change operations that have occurred on the SPS port, or -1 if this query isn't supported by the device.

  * sps_ptp_locked - 1 if the PTP on the SPS port is locked to a PTP grandmaster, 0 if PTP is not locked, or -1 if this query isn't supported by the device.

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
