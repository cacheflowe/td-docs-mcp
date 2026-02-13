---
url: https://docs.derivative.ca/Audio_Render_CHOP
category: CHOPs
title: Audio_Render_CHOP
---

# Audio Render CHOP
## Summary

**Note:** For Apple Silicon Macs, this operator only works starting with build 2022.33910.
The Audio Render CHOP uses the [Steam Audio SDK](https://steamcommunity.com/games/596420/announcements/detail/521693426582988261) to spatially render audio based on the full transforms (translation, rotation, scale) of a listener and an audio source. The Audio Render CHOP takes sound audio sources as input, and spatially outputs the sound in the format specified from the Output Format parameter. The number of channels outputted by the Audio Render CHOP depends on the Output Format.
You specify a 3D component for the transform of the listener, plus a 3D component for the transform of a source.
The sample rate of the output is determined by the audio source, which must be either 44100 or 48000.
An [Info DAT](https://docs.derivative.ca/Info_DAT "Info DAT") can be used to populate the position and radius of baked probes in Simulation mode.
Look at the Audio Render CHOP example in Help -> Operator Snippets.
See also [Oculus Audio CHOP](https://docs.derivative.ca/Oculus_Audio_CHOP "Oculus Audio CHOP").
[audiorenderCHOP_Class](https://docs.derivative.ca/AudiorenderCHOP_Class "AudiorenderCHOP Class")

## Parameters - Audio Render Page
- Active `active` - Turns the Audio Render on or off.
- Mode `mode` - ⊞ - This menu determines which Steam Audio mode to use.
  * Simple Positional `simple` - Sound simulation for only a mono source.
  * Simulation `simulation` - Sound simulation for multiple sources.

- Output Format `outputformat` - ⊞ - The output format of the audio.
  * Binaural `Binaural` - Spatialize sound based on 3D position of source relative to listener.
  * Stereo `stereo` - Spatialize sound based on left and right channels.
  * Quadraphonic Surround `quadraphonic` - Spatialize sound based on front left, front right, rear left, and rear right channels.
  * 5.1 Surround `fiveone` - Spatialize sound based on front left, front right, front center, LFE, rear left, and rear right channels.
  * 7.1 Surround `sevenone` - Spatialize sound based on Ffont left, front right, front center, LFE, rear left, rear right, side left, and side right channels.
  * Custom Setup `custom` - Custom Setup requires use of the Mapping Table.
  * Ambisonics `ambisonics` - Ambisonics is a format for encoding three-dimensional 360 degree audio. The Ambisonics format used in the Audio Render CHOP is the 3rd order SN3D format consisting of 16 encoded channels (WXYZ, RSTUV, KLMNOPQ) that define the sphere of sound. Ambisonics is disabled in Simulation mode when reflections are enabled.
  * Direct Effect `direct` - Used in Simulation mode only to simulate sound based on the direct path between a point source and listener. Direct Effect is disabled when reflections are enabled.

- Enable Attenuation `attenuation` - Attenuate the sound based on the distance between the center position of the listener and a source. The attenuation level is determined by the selected attenuation mode for each source.
- Ambisonics Order `ambisonicsorder` - Ambisonics order of the output buffer.
- Mapping Table `mappingtable` - A DAT Table that specifies the various speakers in the setup and their position. The Table must have 3 columns named x, y, z. Each row specifies an individual speaker, and the 3 columns specify its position. Used with the Custom Setup Output Format. The mapping table will create one channel per row.
- Listener Object COMP `listenerobject` - A COMP that represents the listening head. Must be a COMP that contains transform data, such as a Geometry or Camera COMP.
- Source `source` - Sequence of the audio sources.
- Object COMP `source0object` - A COMP that represents the source of the sound. Must be a 3D Object COMP that contains transform data, such as a [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") or [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP").
- Enable Directivity `source0directivity` - Turns directivity on or off. When disabled, sound will emit from the source from all directions (i.e. omnidirectional)
- Dipole Weight `source0dipoleweight` - The weight of the dipole to blend in the directivity pattern. 0 = pure omnidirectional, 1 = pure dipole, 0.5 = cardioid directivity pattern.
- Dipole Power `source0dipolepower` - The sharpness of the dipole. Higher values make the sound direction narrower.
- Attenuation Mode `source0attnmode` - ⊞ - This menu determines which attenuation mode to use for the source. **Note:** Attenuation modes are disabled when reflections are enabled due to a known issue. If attenuation is enabled while reflections are on, it will revert to Steam Audio's default attenuation model of inverse distance with power of 1.
  * Inverse Distance `inverse` - Attenuation level is calculated by an inverse distance falloff function.
  * Custom Curve `custom` - Attenuation level is calculated by a custom curve.

- Attenuation Inverse Power `source0invpower` - The power of the inverse falloff function. For example, a power of 2 causes an attenuation level of (1/distance)^2.
- Attenuation Curve CHOP `source0chop` - The path of the custom attenuation curve CHOP being referenced. The CHOP must have exactly one channel to represent the curve. The vertical axis represents the attenuation level, and the horizontal axis represents the distance. Attenuation levels are clamped between [0, 1]. The distance should always be non-negative and assumes the CHOP is using samples as the unit.

## Parameters - Meshes Page
- Update Meshes `update` - When enabled, any static mesh changes will automatically be updated in the simulation
- Update Meshes Pulse `updatepulse` - When pulsed, will update the static meshes in the simulation if they changed.
- Mesh `mesh` - Sequence of static meshes.
- Mesh Objects/POPs/SOPs `mesh0object` - The object for the mesh which can be geometry COMP, POP, or SOP. COMPs must contain SOP or POP geometries in triangle polygon form. The root COMP's display flag can be off and still be collected. However, child COMPs will only be added to the scene if their display flag is on.
- Absorption `mesh0absorb` - ⊞ - The fraction of sound absorbed at low, medium, and high frequencies. 0 = no sound is absorbed, 1 = sound is fully absorbed by the mesh surface.
  * Absorption `mesh0absorb1` - Absorption at low frequencies (0 - 800 Hz).
  * Absorption `mesh0absorb2` - Absorption at medium frequencies (800 Hz - 8 kHz).
  * Absorption `mesh0absorb3` - Absorption at high frequencies (8 kHz and above).

- Scattering `mesh0scatter` - Scatters sound for reflections. 0 = reflect at the same angle as it hit the surface (i.e. pure specular), 1 = reflect uniformly randomly (i.e. pure diffuse).
- Transmission `mesh0trans` - ⊞ - The fraction of sound transmitted through at low, medium, and high frequencies. 0 = no sound transmits through, 1 = sound fully transmits through the mesh surface.
  * Transmission `mesh0trans1` - Transmission at low frequencies (0 - 800 Hz).
  * Transmission `mesh0trans2` - Transmission at medium frequencies (800 Hz - 8 kHz).
  * Transmission `mesh0trans3` - Transmission at high frequencies (8 kHz and above).

## Parameters - Simulation Page
- Enable Air Absorption `airabsorb` - Turns air absorption on or off for all sources. Air absorption is how much sound is lost over the distance travelling from source to listener.
- Enable Occlusion `occlusion` - Turns raycast occlusion on or off for all meshes. If a single ray from listener to source is occluded, then the source is considered occluded.
- Number of Surfaces `numsurfaces` - Maximum number of surfaces, starting from closest surface to the listener, whose transmission coefficients will be considered when calculating the total sound transmission.
- Enable Reflection `reflection` - Turns reflection on or off for all meshes.
- Diffuse Samples `diffsamp` - Number of directions to generate for reflecting rays.
- Duration `duration` - Duration in seconds of the impulse responses generated.
- Ambisonics Order `refambixord` - Ambisonics order of the impulse responses generated.
- Number of Rays `numrays` - Number of rays to trace from the listener.
- Number of Threads `numthreads` - Number of threads used for real-time reflection simulations.
- Number of Bounces `numbounces` - Number of times each ray is reflected off a surface.
- Irradiance Min Distance `irmindist` - The minimum distance used to calculate how much sound energy reaches a surface from a source.
- Reflection Bake Mode `bakemode` - ⊞ - This menu determines which bake mode to use. Baking is useful as an optimization tool when calculating reflections. Baking will generate probes that are uniformly spaced and placed above any mesh "floor" at a fixed height. The mesh "floor" is meant to resemble a floor or terrain, meaning meshes should be horizontal or lie along the XZ plane for any probes to be generated on top of it. The probes' region of influence is defined by a 3D position and a radius. Baking has two variations: static listener and static source. For example, if static listener is selected, baking assumes the position of the listener remains fixed. Each probe is then baked reflection data that simulates the sound between its position and the listener. Once baking is done, sources can move around dynamically, and as long as they are within the range of any baked probe, they will use the probe's baked reflection data to calculate its reflected sound, allowing for a reduction in computation and simulation time. If a source is not within the range of any baked probe, the source will not be influenced by any baked data and can lead to incorrect sound calculations. All parameters used for reflections will also be used for baking. Baking will not generate probes for any of the following reasons: Scene has no geometry, spawn box does not contain any of the geometries in the scene, all probes generated lie outside of the spawn box, or all geometries are X-Y or Y-Z planar.
  * Off `off` - Baking is turned off. Turning baking off will disable any bakes that are currently active.
  * Manual `manual` - Baking is turned on, but Baked Reflections must be pulsed to start baking.
  * Automatic `auto` - Baking is turned on and will automatically start baking when changes to baking parameters have been made.

- Bake Reflections `bake` - Immediately start baking. Once complete, reflections will automatically used the baked data. Baking status can be monitored using the bake_complete channel in the Info CHOP.
- Baked Data Variation `variation` - ⊞ - This menu determines which objects will have a fixed position for baking. If the selected static object's position changes, you must re-bake or else the calculated reflections will be incorrect.
  * Static Listener `listener` - Each baking probe calculates reflections with the source at the probe position and the listener at some fixed position. The listener's position must stay static. This mode is useful for modeling reflections from a moving source to a static listener.
  * Static Source `source` - Each baking probe calculates reflections with the listener at the probe position and the source at some fixed position. The source's position must stay static. This mode is useful for modeling reflections from a moving listener to a static source.

- Probes Distance `probedist` - The spacing between two neighboring probes.
- Y-Offset from Surface `yoffset` - The height above the surface of a geometry all probes will be generated at.
- Size of Spawn Box `size` - ⊞ - Size of the spawn box along the X, Y, and Z axes where probes will be generated.
  * Size of Spawn Box `sizex` -
  * Size of Spawn Box `sizey` -
  * Size of Spawn Box `sizez` -

- Origin of Spawn Box `origin` - ⊞ - These X,Y, and Z Values determine where the center of the spawn box is located.
  * Origin of Spawn Box `originx` -
  * Origin of Spawn Box `originy` -
  * Origin of Spawn Box `originz` -

- Distance from Listener `lstnrdist` - The maximum distance from the listener where baked data will be stored for probes.
- Save Duration `savedur` - Duration in seconds of the impulse responses saved at each probe.
- Batch Size `batchsize` - Number of probes to bake simultaneously.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Audio Render CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Audio Render CHOP Info Channels
  * audioposition_full_time -

  * audioposition_panbin_time -

  * distance_attenuation -

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
