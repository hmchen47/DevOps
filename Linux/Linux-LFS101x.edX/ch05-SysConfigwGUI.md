Chapter 05: System Configuration from the Graphical Interface
=============================================================

# Introduction/ Learning Objectives
## System Configuration from the Graphical Interface
[video][vid1]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Apply system, display, and date and time settings using the __System Settings panel__.
+ Track the network settings and manage connections using __Network Manager__ in Linux.
+ Install and update software in Linux from a graphical interface.

Please note that we will revisit all these tasks later, when we discuss how to accomplish them from the command line interface.


# Section 1: System, Display, Date and Time Settings
## System Settings
The __System Settings__ panel allows you to control most of the basic configuration options and desktop settings, such as specifying the screen resolution, managing network connections, or changing the date and time of the system.

For the __GNOME Desktop Manager__, one clicks on the upper right hand corner and then selects the tools image (screwdriver crossed with a wrench).

For __Ubuntu__, one can follow the same procedure, but click on the gear icon, or click on the gear icon on the right side panel, as shown in the screenshot.

![image][img0]
![image][img1]

## Display Settings
The __Displays__ panel under __System Settings__ contains the most common settings for changing  the desktop appearance. These settings function independently of the specific display drivers you are running.

If your system uses a proprietary video card driver (usually from __nVidia__ or __AMD__), you will probably have a configuration program for that driver that is not included in __System Settings__. This program may give more configuration options, but may also be more complicated, and might require sysadmin (root) access. If possible, you should configure the settings in the __Displays__ panel rather than the proprietary configuration program.

The __X__ server, which actually provides the GUI, uses the `/etc/X11/xorg.conf` file as its configuration file _if it exists_. In modern Linux distributions, this file is usually present only in unusual circumstances, such as when certain less common graphic drivers are in use. Changing this configuration file directly is usually for more advanced users. 

![image][img2]

## Setting Resolution and Configuring Multiple Screens
While your system will usually figure out the best resolution for your screen automatically, it may get this wrong in some cases, or you might want to change the resolution to meet your needs.

You can accomplish this using the __Displays__ panel. The switch to the new resolution will be effective when you click __Apply__, and then confirm that the resolution is working. In case the selected resolution fails to work or you are just not happy with the appearance, the system will switch back to the original resolution after a short timeout.

![image][img3]

In most cases, the configuration for multiple displays is set up automatically as one big screen spanning all monitors, using a reasonable guess for screen layout. If the screen layout is not as desired, a check box can turn on mirrored mode, where the same display is seen on all monitors. In the screenshot, clicking on either image lets you configure the resolution of each and whether they make one big screen, or mirror the same video, etc.

The next few screens contain demonstrations for the three Linux distributions that we reference in this course.

![image][img4]

### Applying System and Display Settings in openSUSE and CentOS
Click below to view a demonstration on how to manage system and display settings in __openSUSE__. Please note the video shows __openSUSE__, but the procedures are exactly the same (and appear the same as well) on __CentOS__ and other recent __GNOME__-based Linux distributions.

[video][vid1]

### Applying System and Display Settings in Ubuntu
Click below to view a demonstration on how to manage system and display settings in __Ubuntu__.

[video][vid2]

## Date and Time Settings
![image][img5]

By default, Linux always uses __Coordinated Universal Time (UTC)__ for its own internal time-keeping. Displayed or stored time values rely on the system time zone setting to get the proper time. __UTC__ is similar to, but more accurate than, __Greenwich Mean Time (GMT)__.

The Date and Time Settings window can be accessed from the __System Settings__ window. If you click on the time displayed on the top panel, you can adjust the format with which the date and time is shown; on some distributions, you can also alter the values. 

The __Ubuntu__ screenshot is graphically nicer than the standard __GNOME__ screenshot below (from __openSUSE__), but the information content is identical. Note that you have to "unlock" to change anything, which means typing the root password.

The "automatic" settings are referring to use of __Network Time Protocol (NTP)__ which we discuss next.

![image][img6]

## Network Time Protocol
The __Network Time Protocol (NTP)__ is the most popular and reliable protocol for setting the local time via Internet servers. Most Linux distributions include a working NTP setup, which refers to specific time servers run by the distribution. This means that no setup, beyond "on or off", is required for network time synchronization. If desired, more detailed configuration is possible by editing the standard NTP configuration file (`/etc/ntp.conf`) for Linux NTP utilities.

## Try-It-Yourself: Adjusting Display Settings
The links below point to Try-It-Yourself activities for some of the Linux distributions that we cover in this course. Click the link for the distribution system that you have selected to practice managing system and display settings.

[Adjusting Display Settings in openSUSE][osds]

[Adjusting Display Settings in Ubuntu][ubds]

## Knowledge Check
1. Which protocol is used to set the local time via Internet servers?

    A. Network Clock Protocol (NCP)

    B. Network What Time is IT Protocol (NWTIP)

    C. Network Time Protocol (NTP) 

    D. Network GPS Protocol (NGP)

    Ans: C

    Explanation: 
    Network Time Protocol (NTP) allows you to set the date and time via Internet servers.

2. Which of the following settings can you configure using the Display panel?

    A. Preferred Applications

    B. Screen Resolution 

    C. Network Routing

    D. User Name

    Ans: B

    Explanation: 
    Using the Display panel, you can configure Screen Resolution.

## Lab 1: Getting and Setting Screen Resolution
Find out the current screen resolution for your desktop.

Change it to something else, and change it back to its original value.

Note: You can also ascertain your current resolution by typing at a command line:
```
student:/tmp> $ xdpyinfo | grep dim
dimensions: 3200x1080 pixels (847x286 millimeters)
```
Click [the link][lab1] below to view a solution to the Lab exercise.

## Lab 2: Working with Time Settings
Change the time zone of your system to London time (or New York Time, if you are currently in London time). How does the displayed time change?

After noting the time change, change the time zone back to your local time zone.

Click [the link][lab2] to view a solution to the Lab exercise.


# Section 2: Network Manager
## Network Configuration
All Linux distributions have network configuration files, but file formats and locations can differ from one distribution to another. Hand editing of these files can handle quite complicated setups, but is not very dynamic or easy to learn and use. The __Network Manager__ utility was developed to make things easier and more uniform across distributions. It can list all available networks (both wired and wireless), allow the choice of a wired, wireless, or mobile broadband network, handle passwords, and set up __Virtual Private Networks (VPNs)__. Except for unusual situations, it is generally best to let the __Network Manager__ establish your connections and keep track of your settings.

In this section, you will learn how to manage network connections, including wired and wireless connections, and mobile broadband and VPN connections.

## Wired and Wireless Connections
Wired connections usually do not require complicated or manual configuration. The hardware interface and signal presence are automatically detected, and then ___Network Manager__ sets the actual network settings via __DHCP (Dynamic Host Control Protocol)__.

For __static__ configurations that do not use __DHCP__, manual setup can also be done easily through __Network Manager__. You can also change the __Ethernet Media Access Control (MAC)__ address if your hardware supports it. (The MAC address is a unique hexadecimal number of your network card.)

Wireless networks are not connected to the machine by default. You can view the list of available wireless networks and see which one you are connected to by using __Network Manager__. You can then add, edit, or remove known wireless networks, and also specify which ones you want connected by default when present.

## Configuring Wireless Connections in CentOS
To configure a __Wireless Network__ in __CentOS__:

1. Click on the upper right corner of the top panel, which brings up the first figure.
2. Select the __Wi-Fi__ menu item, which brings up the lefsecondtmost figure.
3. Select the wireless network you wish to connect to. If it is a secure network, the first time it will request that you enter the appropriate password. By default, the password will be saved for subsequent connections.

If you click on Wi-Fi Settings, you will bring up the third screenshot. If you click on the gear icon for any connection, you can configure it in more detail.

![image][img8]
![image][img7]
![image][img9]

## Configuring Wireless Connections in Ubuntu and openSUSE
To configure __Wireless Network__ in __Ubuntu__:

1. In the top panel, click __Network Manager__.
2. Click __Enable Wi-Fi__ - to display a list of available __Wireless Networks__.
3. Click the desired __Wireless Network__.
4. For a secured network, enter the password.
5. To modify saved wireless network settings, click __Edit Connections__.

Configuring __Wireless Connections__ in __openSUSE__

___openSUSE__ looks different from __CentOS__ or __Ubuntu__, but Wired, Wireless, Mobile Broadband, VPN, and DSL are all available from the __Network Connections__ dialog box, as you will see in the upcoming demonstration.

The next few screens are demonstrations for the Linux distributions that we cover in this course. You can view a demonstration for the distribution family of your choice. 

![image][imga]

### Accessing Network Settings and Managing Connections in openSUSE
Click below to view a demonstration on how to access network settings and manage connections in __openSUSE__.

[video][vid3]

### Accessing Network Settings and Managing Connections in Ubuntu
Click below to view a demonstration on how to access network settings and manage connections in __Ubuntu__.

[video][vid4]

## Mobile Broadband and VPN Connections
You can set up a mobile broadband connection with __Network Manager__, which will launch a wizard to set up the connection details for each connection.

Once the configuration is done, the network is configured automatically each time the broadband network is attached.

__Network Manager__ can also manage your VPN connections.

It supports many VPN technologies, such as native __IPSec, Cisco OpenConnect__ (via either the Cisco client or a native open source client), __Microsoft PPTP__, and __OpenVPN__.

You might get support for VPN as a separate package from your distributor. You need to install this package if your preferred VPN is not supported.

## Try-It-Yourself: Accessing Network Settings and Managing Connections
he links below point to Try-It-Yourself activities for configuring network connections for several Linux distributions.  Exactly how you get into the network settings menu is hard to show uniquely, as it varies from version to version, and there is often more than one way to get into the settings. Please note the CentOS case is for version 6 (not 7) which we have de-emphasized for this course, but you may find interesting. For CentOS 7 the tasks look pretty much the same as for the other distributions, since they all run recent versions of Network Manager

Click the link for the distribution system that you have selected to practice how to access network settings and manage connections.

[Accessing Network Settings and Managing Connections in CentOS][cons]

[Accessing Network Settings and Managing Connections in openSUSE][osns]

[Accessing Network Settings and Managing Connections in Ubuntu][ubns]

## Knowledge Check
1. Which VPN technologies does the Network Manager support?

    A. OpenVPN

    B. Cisco OpenConnect

    C. IPSec

    D. All of the above 

    Ans: D

    Explanation: 
    The Network Manager supports OpenVPN, Cisco OpenConnect, and IPSec VPN technologies.

2. Which of the following network connections are usually automatically configured?

    A. Wireless

    B. Wired 

    C. Broadband Connection

    D. VPN

    Ans: B

    Explanation: 
    Wired connections are usually automatically configured.

## Lab 3: Managing Network Connections
Get the current networking configuration for your desktop.

Are you on a wired or a wireless connection? Or both?

If you have wireless hardware, see what wireless networks are available, if any. Click [the link][lab3] to view a solution to the Lab exercise.


# Section 3: Installing and Updating Software
## Installing and Updating Software
Each __package__ in a Linux distribution provides one piece of the system, such as the Linux __kernel__, the __C__ compiler, the shared software code for interacting with __USB__ devices, or the __Firefox__ web browser.

Packages often depend on each other; for example, because __Firefox__ can communicate using SSL/TLS, it will depend on a package which provides the ability to encrypt and decrypt SSL and TLS communication, and will not install unless that package is also installed at the same time.

One utility handles the low-level details of unpacking a package and putting the pieces in the right places. Most of the time, you will be working with a higher-level utility which knows how to download packages from the Internet and can manage dependencies and groups for you.

In this section, you will learn how to install and update software in Linux using the __Debian__ and __RPM__ systems (which are used by both __Fedora__ and __SUSE__ family systems).

## Debian Family System
Let’s look at the __Package Management__ in the __Debian__ Family System.

`dpkg` is the underlying package manager for these systems; it can install, remove, and build packages. Unlike higher-level package management systems, it does not automatically download and install packages and satisfy their dependencies.

For __Debian__-based systems, the higher-level package management system is the __apt (Advanced Package Tool)__ system of utilities. Generally, while each distribution within the Debian family uses `apt`, it creates its own user interface on top of it (for example, `apt-get`, `aptitude`, `synaptic`, `Ubuntu Software Center`, `Update Manager`, etc). Although `apt` repositories are generally compatible with each other, the software they contain generally is not. Therefore, most `apt` repositories target a particular distribution (like __Ubuntu__), and often software distributors ship with multiple repositories to support multiple distributions. The demonstration using the __Ubuntu Software Center__ is shown later in this section.

![image][imgb]

## Red Hat Package Manager (RPM)
__Red Hat Package Manager (RPM)__ is the other package management system popular on Linux distributions. It was developed by __Red Hat__, and adopted by a number of other distributions, including the __openSUSE, Mandriva, CentOS, Oracle Linux__, and others.

The high-level package manager differs between distributions; most use the basic repository format used in __yum__ (__Yellowdog Updater, Modified__ - the package manager used by __Fedora__ and __Red Hat Enterprise Linux__), but with enhancements and changes to fit the features they support. Recently, the __GNOME__ project has been developing __PackageKit__ as a unified interface; this is now the default interface for __Fedora__. 

![image][imgc]

## openSUSE’s YaST Software Management
The __YaST (Yet another Setup Tool)__ Software Manager is similar to other graphical package managers. It is an __RPM__-based application. You can add, remove, or update packages using this application very easily. To access the __YaST__ Software Manager:

1. Click __Activities__
2. In the __Search__ box, type __YaST__
3. Click the __YaST__ icon
4. Click __Software Management__.

__openSUSE’s YaST Software Management__ application is similar to the graphical package managers in other distributions. The demonstration of the __YaST Software Manager__ is shown later in this section.

![image][imgd]

## Installing and Updating Software in CentOS
Click below to view a demonstration on how install and update software in __CentOS__. The video shows __CentOS 6__; for __CentOS 7__ (on which this course is focused) the steps are the same, except for how to start the package manager. Just click on __Applications->System Tools->Software__ in the upper right corner to begin.

[video][vid5]

## Installing and Updating Software in openSUSE
Click below to view a demonstration on how install and update software in __openSUSE__.

[video][vid6]

## Installing and Updating Software in Ubuntu
Click below to view a demonstration on how install and update software in Ubuntu.

[video][vid7]

## Knowledge Check
1. Which two of the following package management utilities are used by Ubuntu?
Select the correct items below.

    A. up2date

    B. dpkg 

    C. yum

    D. the Ubuntu Software Center

    Ans: B, D

    Explanation: 
    Ubuntu uses the dpkg and Ubuntu Software Center package management utilities.

2. OpenSUSE uses _____________ to add and remove software packages.

    A. Google Play

    B. YaST Software Management 
    
    C. YaST Configuration Management

    D. SUSE Software Center

    Ans: B

    Explanation: YaST Software Management is used to add and remove software in openSUSE.

## Lab 4: Installing and Removing Software Packages
Using graphical package management tools, find the __dump__ package.

If it is not installed, install it.

If it is already installed, remove it, and then re-install it.

[Lab Solution][lab4]

# Summary
You have completed this chapter. Let's summarize the key concepts covered:

+ You can control basic configuration options and desktop settings through the __System Settings__ panel.
+ Linux always uses __Coordinated Universal Time (UTC)__ for its own internal time-keeping. You can set the __Date and Time Settings__ from the __System Settings__ window.
+ The __Network Time Protocol__ is the most popular and reliable protocol for setting the local time via Internet servers.
+ The __Displays__ panel allows you to change the resolution of your display and configure multiple screens.
+ __Network Manager__ can present available wireless networks, allow the choice of a wireless or mobile broadband network, handle passwords, and set up VPNs.
+ __dpkg__ and __RPM__ are the most popular package management systems used on Linux distributions.
+ __Debian__ distributions use `dpkg` and `apt`-based utilities for package management.
+ __RPM__ was developed by __Red Hat__, and adopted by a number of other distributions, including the __openSUSE, Mandriva, CentOS, Oracle Linux__, and others.


[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002900_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005600_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003000_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008400_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007200_DTH.mp4
[vid5]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V010200_DTH.mp4
[vid6]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006800_DTH.mp4
[vid7]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V010500_DTH.mp4

[img0]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9ea53b1818b348adb44969d940b63023/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/settingssuse.png
[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/599b9c1a3af2e43a7db33c3903d127a3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/settingsubuntu.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d72ee0ec02ac7e4fb2154ff420f424f5/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/displayubuntu.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5832bdbe563a4fef4230eb54ea55e10e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/displaymodubuntu.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/79afc8b8f7adb2b7041cf833ca5a2cea/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/displaymodrhel7.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c9eb0cbea8aaf75e2c9c130e0013c90e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/daterhel7.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5fa77a6b82c3a0b8faa8ce6c1883730d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/dateubuntu.png
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1fd394a9d4dccbc6b73088a3f311325d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/netrhel71.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fae657ad0388e71c9d1196948333678d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/netrhel72.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0f2e07365dc4a011392053b03e91f2f4/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/netrhel73.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6072c53f9d229d0dd2307edb29a75a98/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch05_screen21.jpg
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c3ddb34d7f243624f888143c74665a94/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch05_screen34.jpg
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d803cf81ee0659af701365b16aebcb3a/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch05_screen35.jpg
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3daba44866ca7ac7880f9eb6e74bc467/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch05_screen36.jpg

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-display.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-time.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-netmanage.html
[lab4]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-guipackage.html

[osds]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/setdisplaysuse/index.html
[ubds]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/setdisplayubuntu/index.html
[cons]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/netsetcentos/index.html
[osns]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/netsetsuse/index.html
[ubns]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/netsetubuntu/index.html


