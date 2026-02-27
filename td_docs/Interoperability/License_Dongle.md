---
url: https://docs.derivative.ca/License_Dongle
category: Interoperability
title: License_Dongle
---

# License Dongle

[![](https://docs.derivative.ca/images/a/a0/CmDongle_regular.png)](https://docs.derivative.ca/File:CmDongle_regular.png)
Regular size - includes confirmation LED
[![](https://docs.derivative.ca/images/1/1f/CmDongle_micro.png)](https://docs.derivative.ca/File:CmDongle_micro.png)
Micro size - same width as a USB port

##  TouchDesigner on the Go

If you want to take TouchDesigner anywhere you go, a dongle [license](https://docs.derivative.ca/Licensing "Licensing") option is available for the ultimate in mobility and convenience. Purchasing a dongle will let you put one of the licenses in your account onto a secure USB licensing dongle. The key installed on the dongle will automatically key TouchDesigner on any computer that the dongle is plugged into (assuming the CodeMeter Runtime is installed on the computer).

Educational, Commercial, or Pro licences for TouchDesigner or TouchPlayer can be transferred onto a dongle.

##  Purchasing a Dongle

  * Purchase a License Dongle from the [Store](https://www.derivative.ca/cart).
  * Derivative will contact you to select a license from your account to be transferred to the dongle. Can be used with existing or new licenses.
  * Derivative will confirm shipping address and send the dongle via International Priority and provide a tracking number.

##  Loading your License on a Dongle

New dongles are shipped unloaded, so you can continue using your licenses normally while waiting for delivery.

Once your dongle arrives:
  * Disable the licenses you want to load onto the dongle using the Key Manager.
  * Email us at **licensing@derivative.ca** with:
    * The dongle ID
    * The license ID(s) you wish to load

Our team will send you an activation link within 24 hours (Monday to Friday).

##  Updating an Existing Dongle

If you have applied [updates](https://docs.derivative.ca/Updates "Updates") or have other changes you would like to make to your dongle, simply email your dongle number or license ID to licensing@derivative.ca to request an **Activation Link**. Dongles do not 'call home' and require a manual activation in order for updates to take effect.

(Office Hours are Monday to Friday, 10:00 am - 6:00 pm EST, and you can expect to receive the link in approximately 24 hours.)

##  Using a Dongle you already own

If you already have a CodeMeter dongle, such as one that comes with Notch or Disguise, you can load your TouchDesigner license on to that. The dongle serial number must start with 2- or 3- (the older 1- ones are not supported). The 'CodeMeter Setup Fee' should be purchased on the Derivative store and then please email us to load the license onto your dongle.

##  Installing Required Codemeter Software

To use USB License Dongles or Floating Cloud licenses, Codemeter Runtime software is required on your system.

**NOTE:** Please update to CodeMeter Runtime 7.60+

###  Windows CodeMeter Install

  * When installing TouchDesigner, the first dialog of the installer will have an option for "**Install Runtime for Dongle Licensing** ", make sure this is checked on. Proceed with the installation. You can alternatively download the dongle runtime from here [CodeMeter Download](https://www.wibu.com/support/user/downloads-user-software.html). We suggest you turn off the 'Automatic server search' option in the CodeMeter installer options, to allow for quicker startup on networks with many machines with CodeMeter installed.

[![InstallOptions.png](https://docs.derivative.ca/images/thumb/a/a1/InstallOptions.png/300px-InstallOptions.png)](https://docs.derivative.ca/File:InstallOptions.png)

###  macOS CodeMeter Install

  * Download and install the CodeMeter Control Center from here:

[CodeMeter Download](https://www.wibu.com/support/user/downloads-user-software.html)

If the software or service fails to start, you may need to enable it in your System's Security Preferences.

##  Using the Dongle

  * Plug the dongle into a USB port on the computer.
  * TouchDesigner will now use whatever license type is installed on the dongle (ie Commercial or Pro etc).

**NOTE:** If there were other keys previously installed on the computer through the [Key Manager](https://docs.derivative.ca/Key_Manager_Dialog "Key Manager Dialog"), TouchDesigner will use the highest available key type from either the installed keys or the dongle. You can disable all the installed keys using the Key Manager if they are no longer needed when using a dongle.

##  Sharing Licenses Over a Network

Multiple licenses can be loaded onto a dongle (and also [Floating Cloud Licenses](https://docs.derivative.ca/Floating_Cloud_Licenses "Floating Cloud Licenses")) and then distributed to other computers on the network when TouchDesigner is launched. The **server** computer will have the dongle plugged in, the **client** computers will then receive a license from the dongle server when requested. Both server and all client computers require the CodeMeter Runtime software to be installed (see above). Note that this is **not** for Cloud licenses, which are setup differently. This is only to share a physical dongle's license(s) over a local area network.

####  Limitations

  * All licenses loaded on the dongle must be for the same product ie. TouchDesigner or TouchPlayer
  * All licenses loaded on the dongle must be the same license type ie. Educational or Commercial or Pro

###  Server Setup

Follow these steps to setup the computer that will act as the license server.
  * Plug the license dongle into the server computer.

  * Open the CodeMeter Control Center, click on the WebAdmin button in the lower-right of the panel.

  * Check the dongle under the **Container** tab. This will let you inspect the licenses that have been loaded onto the dongle.

[![CodeMeterWebAdmin.png](https://docs.derivative.ca/images/3/31/CodeMeterWebAdmin.png)](https://docs.derivative.ca/File:CodeMeterWebAdmin.png)

  * Go to **Configuration > Server > Server Access**, then 'Enable' **Network Sever**. Click 'Apply'.

[![CodeMeterEnableNetworkServer.png](https://docs.derivative.ca/images/8/88/CodeMeterEnableNetworkServer.png)](https://docs.derivative.ca/File:CodeMeterEnableNetworkServer.png)

  * Go to **Configuration > Server> License Access Permissions**.
    * Under **Basic Mode Configuration** add the IP address of the client computers that you want to have access to the license server. For example, IP address 192.168.1.2. Click 'Apply'.

[![CodeMeterLicenseAccessPermissions.png](https://docs.derivative.ca/images/2/20/CodeMeterLicenseAccessPermissions.png)](https://docs.derivative.ca/File:CodeMeterLicenseAccessPermissions.png)

  * Restart the CodeMeter service from the **Process** menu in the CodeMeter Control Center.

[![CodeMeterRestartService.png](https://docs.derivative.ca/images/e/ed/CodeMeterRestartService.png)](https://docs.derivative.ca/File:CodeMeterRestartService.png)

###  Client Setup

Before beginning, confirm that the client computer can communicate with the license server computer over the network. In many (but not all) network environments this can be confirmed by pinging the server computer's IP address.
  * Go to **Configuration > Basic > Server Search List**
    * Under **Server Search List** add the IP address of the license server computer. For example, IP address 192.168.1.15. Click 'Apply'.

[![CodeMeterServerSearchList.png](https://docs.derivative.ca/images/f/fb/CodeMeterServerSearchList.png)](https://docs.derivative.ca/File:CodeMeterServerSearchList.png)

  * Restart the CodeMeter service from the **Process** menu in the CodeMeter Control Center.

[![CodeMeterRestartService.png](https://docs.derivative.ca/images/e/ed/CodeMeterRestartService.png)](https://docs.derivative.ca/File:CodeMeterRestartService.png)

  * In the WebAdmin window, confirm connection to the license server is working by clicking on the **orange-arrow icon** at the bottom of the window. You should see the IP address of the license server computer displayed in the list.

[![CodeMeterServerList.png](https://docs.derivative.ca/images/8/87/CodeMeterServerList.png)](https://docs.derivative.ca/File:CodeMeterServerList.png)

####  Troubleshooting Connection

If you are having issues obtaining a license on a client machine. You can look at the 'Events' tab in the CodeMeter Control Panel to get information on what is occuring. A likely issue is that the firewall on the server machine is blocking the connection. Make sure the CodeMeter.exe application is allowed through the firewall. This .exe is usually located in C:\Program Files (x86)\CodeMeter\Runtime\bin\CodeMeter.exe

###  Administrative Tools

From the license server computer you can inspect the distribution of licenses from the dongle and the active licenses in use on the network.
  * Go to **License Monitoring > All Licenses** to get a summary of licenses in use and available.

[![CodeMeterLicenseMonitoring.png](https://docs.derivative.ca/images/8/8e/CodeMeterLicenseMonitoring.png)](https://docs.derivative.ca/File:CodeMeterLicenseMonitoring.png)

  * Go to **License Monitoring > Sessions** to get a list of each client computer currently using a license. Clicking on an entry in this list displays the license access times and gives the option to end the session on the client computer.

[![CodeMeterSessions.png](https://docs.derivative.ca/images/3/34/CodeMeterSessions.png)](https://docs.derivative.ca/File:CodeMeterSessions.png)

##  Additional Information

###  Important Considerations

  * Dongles will only work for the TouchDesigner version equal to the license that was loaded onto the dongle. To [upgrade](https://docs.derivative.ca/Updates "Updates") TouchDesigner versions on your dongle, please contact us.
  * Dongles will only work for builds compiled before the [Update Date](https://docs.derivative.ca/Updates "Updates") of the license loaded onto the dongle. When you purchase "1 Year of Updates" to extend your license to get newer builds, please contact us to update your dongle.
  * Licenses on dongles that are lost or stolen **can not be recovered**. You will need to purchase a new license to replace the lost one.
  * Licenses transferred to a dongle are no longer available for use through Derivative's online key management system. If you decide you no longer want to use the dongle, you can contact us to remove license from the dongle and it will become active again in your Derivative account online.

###  Advantages of Using a Dongle

  * Take your TouchDesigner key with you wherever you go, plug it into any computer running TouchDesigner and be instantly keyed.
  * If a machine is licensed with a Player license, plugging in a Designer dongle will enable network editor without needing to shutdown/restart the file. When the dongle is unplugged the machine will return back to being licensed as a Player.
  * Save time in a multi-computer environment or studio. Simplify the process of moving around to other computers.
  * Useful in situations with no internet access. Creating/Moving keys via the Key Manager requires an online connection which very often is not guaranteed during installations and working in the field. Using a licensing dongle you don't have to worry about it.
  * Convenience when delivering finished systems to clients. The license required to run TouchDesigner for client projects can be included on a dongle. This will make it easier for the client to keep the license, and they won't need their own Derivative account. Additionally, they will not need to re-key if they change hardware making it a better turnkey solution.
  * Easier when the time comes to repair or replace hardware, creating new keys is not required when using a dongle.

###  Creating a CmDust Log File for Debugging CodeMeter issues

**Windows**
  1. Plug in your dongle or install your .wbc credential file.
  2. Launch TouchDesigner, wait for it to finish opening, and then close TouchDesigner.
  3. Open CmDust using the "Start | All Programs | CodeMeter | Tools" menu item.
  4. The output of the executed program is written to the text file CmDust-Result.log and saved to the user directory which automatically opens when starting CmDust.

**macOS** For macOS, you create the CmDust file using the cmu commandline program. Calling cmu is stored in the search path. To create a CmDust log, please proceed as follows:
  1. Plug in your dongle or install your .wbc credential file.
  2. Launch TouchDesigner, wait for it to finish opening, and then close TouchDesigner.
  3. Open the commandline/terminal
  4. Type in the following command cmu --cmdust.
  5. Using the option --file allows you to specify a name and the storage location. -->cmu --cmdust --file CmDust.log. By default, the file displays in the screen console.

###  Technical Notes

Derivative uses [WIBU-Systems CodeMeter](http://www.wibu.com/codemeter.html) technology for licensing dongles.

See Also: [Floating Cloud Licenses](https://docs.derivative.ca/Floating_Cloud_Licenses "Floating Cloud Licenses")

A [Link](https://docs.derivative.ca/Link "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](https://docs.derivative.ca/Export "Export"), node [Paths](https://docs.derivative.ca/Network_Path "Network Path") in parameters, and [expressions](https://docs.derivative.ca/Expression "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](https://docs.derivative.ca/Wire "Wire") that connects nodes in the same [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").

Every component contains a network of operators that create and modify data. The operators are connected by wires that define where data is routed after the operator cooks its inputs and generates an output.

The Container component type is a [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") that holds, lays out and displays any number of other Panel Components.

A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component").
