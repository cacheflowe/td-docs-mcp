---
url: https://docs.derivative.ca/Ouster_TOP
category: TOPs
title: Ouster_TOP
---

# Ouster TOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Educational](https://docs.derivative.ca/TouchDesigner_Educational "TouchDesigner Educational"), [TouchDesigner Commercial](https://docs.derivative.ca/TouchDesigner_Commercial "TouchDesigner Commercial") and [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
[Ouster](https://docs.derivative.ca/Ouster "Ouster") makes LIDAR devices for scanning 3D environments. The Ouster TOP sends and receives data with an Ouster Imaging Lidar, converting to point cloud data on the GPU. For more information see the user guides at [Ouster.io](https://www.ouster.io/resources)
**Requirements:**
  * The TOP only supports Windows and macOS ARM builds of TouchDesigner.
  * The TOP supports Ouster devices using version 2.x or 3.x firmware.
  * Access to your local network to connect with the sensor device. Check your firewall settings if you have trouble accessing the device.
  * High resolution scanning modes require up to 130Mbps of bandwidth. Gigabit Ethernet hardware is required for full operation. Insufficient bandwidth will cause broken images and missing frames.

**Features include:**
  * Additional sensor data like IMU (Inertial Measurement Unit - the gyroscope and accelerometer) via Info CHOP.
  * Flexible output mappings to RGBA GPU Image Channels.
  * Time Sync Mode for supporting multiple devices in the same area (Internal OSC, Sync Pulse In, PTP 1588).
  * Auto startup features.

**Connection Instructions:**
To connect to the sensor, you will need either the IP addressed assigned by the local DHCP server or the name of the device. The name is based on the serial number that is usually printed on the top of the sensor in the format "os-############". This name can be entered directly into the Device Address parameter (see parameter help below). You can also connect to the device through a web browser using the IP or name in the format `http://os-###########/[](http://os-###########/)`. The web interface allows you to check the status of the device and gives additional error information.
**Note:** If the "os-############" syntax isn't able to connect, you can also try "os-############.local".
Once the device is configured, it will continue to send output to the target IP address so it is not required to enter the device address again unless you need to change the configuration.
Range data collected from the device is presented as 32bit floating point values in the RGBA channels of the output image. The output is arranged as a panoramic image. IMU data from the device can be accessed by connecting an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP"). If more than 4 output channels are needed, you can use a [Ouster Select TOP](https://docs.derivative.ca/Ouster_Select_TOP "Ouster Select TOP") to create additional output images.
**Ouster Outputs:**
Range, Signal, Reflectivity, Near IR, and Flags are raw data channels coming from the sensor, while XYZ position values are calculated by using the range data and the look up table of beam azimuth and altitude angles. Range is measured in millimeters, while XYZ positions are in meters. If you need more than 4 channels of data, use a [Ouster Select TOP](https://docs.derivative.ca/Ouster_Select_TOP "Ouster Select TOP") to create a second output image from the same sensor data. In addition to the sensor data, you can also assign a constant value of one or zero to a channel by selecting the corresponding entry from the menu.
**Note:** All 3D coordinates are transformed into TouchDesigner space where Y is up and X and Z represent the ground plane. This is different from the original coordinate space defined in the Ouster documentation.
See also: [Ouster Select TOP](https://docs.derivative.ca/Ouster_Select_TOP "Ouster Select TOP")
[ousterTOP_Class](https://docs.derivative.ca/OusterTOP_Class "OusterTOP Class")

## Parameters - Connection Page
- Active `active` - Enables connections with the device.
- Re-Init `reinitialize` - Manually reinitialize the device.
- Device Address `deviceaddress` - The IP address or the name of the Ouster device. The address is only required during configuration. The device will request an address from the local DHCP server when it is connected to the network. The name of the device is printed on the top of the sensor in the format "os-#####", where ##### is the serial number e.g. "os-991900123456". If you want to use the name of the device, you may have to input "os-#####.local" in this parameter to connect to your sensor. You can determine the IP address using the ping command and the device name e.g. ping -4 os-991900123456. For more information see the Ouster User Guide at [Ouster.io](https://www.ouster.io/downloads).
- Lidar Port `lidarport` - The UDP port number to receive lidar data.
- IMU Port `imuport` - The UDP port number to receive data from the inertial measurement unit (IMU) on the device. The IMU data can be accessed by connecting the Ouster TOP to an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
- Target Address `targetaddress` - The IP address where the sensor should send the lidar and IMU data to. If the parameter is blank, the address of the current machine will be used. This field should only be necessary if the sending machine has more than one IP address or if you wish to send the lidar data to a different machine than the one you are configuring it on.
- Scan Mode `scanmode` - ⊞ - Select a scanning mode to set the sensor's horizontal resolution and number of revolutions per second. The vertical resolution is determined by the hardware e.g. an OS1-64 sensor has vertical resolution of 64 pixels (samples).
  * 512 x 10Hz `mode512x10` -
  * 512 x 20Hz `mode512x20` -
  * 1024 x 10Hz `mode1024x10` -
  * 1024 x 20Hz `mode1024x20` -
  * 2048 x 10Hz `mode2048x10` -
  * 4096 x 5Hz `mode4096x5` -

- Operating Mode `opmode` - ⊞ - Select operating mode for the sensor.
  * Normal `normal` - Normal operating mode.
  * Standby `standby` - Low power (5W) mode where the sensor won't spin and lasers won't fire.

- Azimuth Window `azimuthwindow` - ⊞ - Set the sensor's visible region of interest in millidegrees where only data within the window bounds is sent.
  * `azimuthwindow1` - The minimum window millidegree.
  * `azimuthwindow2` - The maximum window millidegree.

- Signal Multiplier `signalmultiplier` - ⊞ - Set a multiplier for the signal strength of the sensor. The maximum azimuth window depends on the signal multiplier strength. For each signal multiplier value, the max window sizes are as follows:
  * `0.25` - 360 degrees.
  * `0.5` - 360 degrees.
  * `1` - 360 degrees.
  * `2` - 180 degrees.
  * `3` - 120 degrees.

- Data Format `dataformat` - ⊞ - Sets the packet format of the lidar data.
  * Legacy `legacy` -
  * Single Return `single` -
  * Dual Return `dual` -
  * Low Data Rate (Single Return) `lowrate` -

- Red `redchannel` - ⊞ - Select what sensor data will be placed into the red channel of the output image.
  * X `x` -
  * Y `y` -
  * Z `z` -
  * Range `range` -
  * Range `range2` -
  * Signal Photons `signal` -
  * Signal Photons 2 `signal2` -
  * Reflectivity `reflectivity` -
  * Reflectivity 2 `reflectivity2` -
  * Near IR Photons `nir` -
  * Flags `flags` -
  * Flags 2 `flags2` -
  * Constant 1 `one` -
  * Constant 0 `zero` -

- Green `greenchannel` - ⊞ - Select what sensor data will be placed into the green channel of the output image.
  * X `x` -
  * Y `y` -
  * Z `z` -
  * Range `range` -
  * Range `range2` -
  * Signal Photons `signal` -
  * Signal Photons 2 `signal2` -
  * Reflectivity `reflectivity` -
  * Reflectivity 2 `reflectivity2` -
  * Near IR Photons `nir` -
  * Flags `flags` -
  * Flags 2 `flags2` -
  * Constant 1 `one` -
  * Constant 0 `zero` -

- Blue `bluechannel` - ⊞ - Select what sensor data will be placed into the blue channel of the output image.
  * X `x` -
  * Y `y` -
  * Z `z` -
  * Range `range` -
  * Range `range2` -
  * Signal Photons `signal` -
  * Signal Photons 2 `signal2` -
  * Reflectivity `reflectivity` -
  * Reflectivity 2 `reflectivity2` -
  * Near IR Photons `nir` -
  * Flags `flags` -
  * Flags 2 `flags2` -
  * Constant 1 `one` -
  * Constant 0 `zero` -

- Alpha `alphachannel` - ⊞ - Select what sensor data will be placed into the alpha channel of the output image.
  * X `x` -
  * Y `y` -
  * Z `z` -
  * Range `range` -
  * Range `range2` -
  * Signal Photons `signal` -
  * Signal Photons 2 `signal2` -
  * Reflectivity `reflectivity` -
  * Reflectivity 2 `reflectivity2` -
  * Near IR Photons `nir` -
  * Flags `flags` -
  * Flags 2 `flags2` -
  * Constant 1 `one` -
  * Constant 0 `zero` -

## Parameters - Timing Page
- Time Sync Mode `timemode` - ⊞ - Select how the sensor generates timestamp information.
  * Internal OSC `internalosc` - Timestamps are generated from an internal oscillator. This is the default setting.
  * Sync Pulse In `syncpulsein` - Timing is synced to pulses on the SYNC_PULSE_IN input.
  * PTP 1588 `ptp1588` - Timing is synced to an external PTP master.

- Sync Pulse In Polarity `pulseinpolarity` - ⊞ - The polarity of the SYNC_PULSE_IN signal to use.
  * Active Low `activelow` -
  * Active High `activehigh` -

- Multipurpose IO Mode `iomode` - ⊞ - Determines how the sensor uses the SYNC_PULSE_OUT signal.
  * Off `off` - The signal is not used. This is the default setting.
  * Input NMEA `inputnmea` - The sensor will expect standard NMEA $GPRMC UART messages on the multipurpose IO port. See [here](https://www.gpsworld.com/what-exactly-is-gps-nmea-data/) for more information on GPS NMEA data.
  * Output Internal OSC `outputinternalosc` - Signal output is taken from the internal oscillator.
  * Output Sync Pulse In `outputsyncpulsein` -
  * Output PTP 1588 `outputptp1588` -
  * Output Encoder Angle `outputangle` - Signal output is based on the angle of the encoder.

- Sync Pulse Out Polarity `pulseoutpolarity` - ⊞ - Polarity of the output signal pulse.
  * Active Low `activelow` -
  * Active High `activehigh` -

- Sync Pulse Out Frequency `pulseoutfrequency` - Frequency of the output pulse in Hz (must be greater than 0).
- Sync Pulse Out Angle `pulseoutangle` - The encoder angle at which to output a signal pulse. Measured in degrees less than 360.
- Sync Pulse Out Width `pulseoutwidth` - Width of the output signal pulse in mm.
- NMEA In Polarity `nmeainpolarity` - ⊞ - Sets the polarity of the NMEA URT input $GPRMC messages. Set to 'Active High' if UART is active high, idle low, and the start bit is after a falling edge.
  * Active Low `activelow` -
  * Active High `activehigh` -

- NMEA Ignore Valid Char `nmeaignorevalidchar` - Turn off, if the NMEA UART input $GPRMC messages should be ignored if valid character is not set, and turn on if messages should be used for time syncing regardless of the valid character.
- NMEA Baud Rate `nmeabaudrate` - ⊞ - The baud rate for the incoming NMEA URT input $GPRMC messages.
  * Baud 9600 `baud9600` -
  * Baud 115200 `baud115200` -

- NMEA Leap Seconds `nmealeapseconds` - An integer number of leap seconds that will be added to the UDP timestamp when calculating seconds since 00:00:00 Thursday, 1 Jan 1970. Set to 0 for Unix Epoch Time.
- Phase Lock `phaselock` - When enabled, the sensor synchronizes its rotation using the phase lock offset.
- Phase Lock Offset `phaselockoffset` - The angle to synchronize the sensor's rotation at an input pulse.

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
Extra Information for the Ouster TOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Ouster TOP Info Channels
  * imu_read_time - The time the measurement was take in nanoseconds since the device was booted.

  * accel_read_time - The time the accelerometer measurement was take in nanoseconds relative to the current timestamp mode (see Ouster User Guide).

  * gyro_read_time - The time the gyroscope measurement was take in nanoseconds relative to the current timestamp mode (see Ouster User Guide)

  * accel_tx - Acceleration in the x-axis (g)

  * accel_ty - Acceleration in the y-axis (g)

  * accel_tz - Acceleration in the z-axis (g)

  * vel_rx - Angular velocity around the x-axis (deg per sec)

  * vel_ry - Angular velocity around the y-axis (deg per sec)

  * vel_rz - Angular velocity around the z-axis (deg per sec)

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
