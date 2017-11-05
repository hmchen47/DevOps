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
All Linux distributions have network configuration files, but file formats and locations can differ from one distribution to another. Hand editing of these files can handle quite complicated setups, but is not very dynamic or easy to learn and use. The __Network Manager__ utility was developed to make things easier and more uniform across distributions. It can list all available networks (both wired and wireless), allow the choice of a wired, wireless, or mobile broadband network, handle passwords, and set up __Virtual Private Networks (VPNs)__. Except for unusual situations, it is generally best to let the Network Manager establish your connections and keep track of your settings.

In this section, you will learn how to manage network connections, including wired and wireless connections, and mobile broadband and VPN connections.



# Section 3: Installing and Updating Software



# Summary



[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002900_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005600_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003000_DTH.mp4
[vid3]: 
[vid4]: 
[vid5]: 
[vid6]: 
[vid7]: 
[vid8]: 
[vid9]: 
[vida]: 

[img0]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9ea53b1818b348adb44969d940b63023/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/settingssuse.png
[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/599b9c1a3af2e43a7db33c3903d127a3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/settingsubuntu.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d72ee0ec02ac7e4fb2154ff420f424f5/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/displayubuntu.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5832bdbe563a4fef4230eb54ea55e10e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/displaymodubuntu.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/79afc8b8f7adb2b7041cf833ca5a2cea/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/displaymodrhel7.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c9eb0cbea8aaf75e2c9c130e0013c90e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/daterhel7.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5fa77a6b82c3a0b8faa8ce6c1883730d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/dateubuntu.png
[img7]: 
[img8]: 
[img9]: 
[imga]: 
[imgb]: 
[imgc]: 
[imgd]: 
[imge]: 

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-display.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-time.html
[lab3]: 
[lab4]: 
[lab5]: 

[osds]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/setdisplaysuse/index.html
[ubds]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/setdisplayubuntu/index.html


