# Ch07 : The Linux Boot Process

## The Linux Boot Sequence

<img src="https://geekstuffweb.files.wordpress.com/2014/08/2732a-rhce_linux_boot_diagram.png?w=794&h=1123&zoom=2" width="400" alt="Linux Boot Process">

<img src="https://blog.frognew.com/images/2017/01/linux-boot-process.jpg" width="300" alt="Linux Boot Porcess & Env Init">

+ __Master Boot Record (MBR)__: the very first sector of the hard disk  reserved for programmable code used in booting
+ When booting from a hard disk, the PC system BIOS starts by loading and executing bootloader code.
+ Fedora Linux: Grub staged bootloader system
+ Grub Version 1
    + _Stage 1_: run bootloader code (boot.img) from the MBR
    + _Stage 1.5_: additional code loaded from the 30 kilobytes of hard disk immediately after the , including enough partition and filesystem drivers to allow the Stage 2 to be loaded from a known location in the boot filesystem, usually /boot/grub
    + _Stage 2_: load other required drivers and kernel modules before reading the Grub configuration file and displaying the boot menu
+ Grub Version 2
    +_Stage 1_: read an image file (core.img) in the 30 kilobytes after the MBR
+ Grub After the Boot 
    + GRUB startup menu displayed
    + Select an operating system to boot or to view and edit kernel startup parameters
    + Procedure after selecting a version of Linux
        + load selected kernel into memory
        + __initrd__ ("init ram disk") or __initramfs__ ("init ram filesystem"): load the image file containing basic root filesystem w/ all kernel modules and files required for the boot process
        + start the kernel w/ memory address of the image file and mount this image file as a "starter" memory based root filesystem.
        + kernel detect the systems' hardware to load required drivers
        + root filesystem on disk takes over from the one in memory
        + start software daemons according to settings
        + create a root file system in memory using A ramdisk file loaded into memory

## Grub Configuration Files

+ Grub Version 1 Configuration
    + Figure 7-1 Sample grub.conf file
+ Grub Version 2 Configuration

## Boot Runlevels and Targets

+ Table 7-1 Runlevel and Target Descriptions
+ Systemd
    + Table 7-2 Systemd Target File Locations
    + Table 7-3 Important Systemd Boot Related Commands
    + Determine the current default target group
    + Set the default target group
+ SysV Init
    + 7-4 Init Runlevel File Locations
    + Determining and Setting the Default Boot runlevel

## System Shutdown and Rebooting

+ Halt/Shut Down The System
+ Reboot The System
+ Entering Single-user Mode
    + Switching to Single-user Mode
    + Entering Single-user Mode At The Grub Splash Screen
    + Reverting To Your Default runlevel From Single User Mode
    + Root Password Recovery

## The Linux Console

+ Getting a GUI Console
+ Get a Basic Text Terminal Without Exiting the GUI
    + Using a GUI Terminal Window
    + Using Virtual Consoles


