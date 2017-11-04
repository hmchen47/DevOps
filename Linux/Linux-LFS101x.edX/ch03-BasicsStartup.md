Introduction to Linux
=====================

Chapter 03: Linux Basics and System Startup
===========================================

# Introduction/ Learning Objectives

## Linux Basics and System Setup
[video][vid1]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Identify Linux filesystems.
+ Identify the differences between partitions and filesystems.
+ Describe the boot process.
+ Install Linux on a computer.


# Section 1: The Boot Process
## The Boot Process
Have you ever wondered what happens in the background from the time you press the __Power__ button until the Linux login prompt appears?  

The Linux __boot process__ is the procedure for initializing the system. It consists of everything that happens from when the computer power is first switched on until the user interface is fully operational. 

Once you start using Linux, you will find that having a good understanding of the steps in the boot process may help you with troubleshooting problems, as well as with tailoring the computer's performance to your needs.  

On the other hand, the boot process can be rather technical. You may want to come back and study this section later, if you want to first get a good feel for how to use a Linux system.

![image][img1]

## BIOS - The First Step
Starting an __x86__-based Linux system involves a number of steps. When the computer is powered on, the __Basic Input/Output System (BIOS)__ initializes the hardware, including the screen and keyboard, and tests the main memory. This process is also called __POST (Power On Self Test)__.

The BIOS software is stored on a ROM chip on the motherboard. After this, the remainder of the boot process is controlled by the operating system (OS).

![image][img2]

## Master Boot Record (MBR)
Once the __POST__ is completed, the system control passes from the __BIOS__ to the boot loader. The boot loader is usually stored on one of the hard disks in the system, either in the boot sector (for traditional __BIOS/MBR__ systems) or the __EFI__ partition (for more recent __(Unified) Extensible Firmware Interface__ or __EFI/UEFI__ systems). Up to this stage, the machine does not access any mass storage media. Thereafter, information on the date, time, and the most important peripherals are loaded from the __CMOS__ values (after a technology used for the battery-powered memory store - which allows the system to keep track of the date and time even when it is powered off).

A number of boot loaders exist for Linux; the most common ones are __GRUB__ (for __GRand Unified Boot__ loader) and __ISOLINUX__ (for booting from removable media), and __DAS U-Boot__ (for booting on embedded devices/appliances). Most Linux boot loaders can present a user interface for choosing alternative options for booting Linux, and even other operating systems that might be installed. When booting Linux, the boot loader is responsible for loading the kernel image and the initial __RAM__ disk or filesystem (which contains some critical files and device drivers needed to start the system) into memory.

![image][img3]

## Boot Loader in Action
The boot loader has two distinct stages:

First Stage:

+ For systems using the __BIOS/MBR__ method, the boot loader resides at the first sector of the hard disk, also known as the __Master Boot Record (MBR)__. The size of the __MBR__ is just `512 bytes`. In this stage, the boot loader examines the partition table and finds a bootable partition. Once it finds a bootable partition, it then searches for the second stage boot loader e.g, __GRUB__, and loads it into __RAM (Random Access Memory)__.
+ For systems using the __EFI/UEFI__ method, __UEFI firmware__ reads its __Boot Manager__ data to determine which __UEFI__ application is to be launched and from where (i.e., from which disk and partition the __EFI__ partition can be found). The firmware then launches the __UEFI__ application, for example, __GRUB__, as defined in the boot entry in the firmware's boot manager. This procedure is more complicated, but more versatile than the older MBR methods.

Second Stage:

+ The second stage boot loader resides under /boot. A splash screen is displayed, which allows us to choose which Operating System (OS) to boot. After choosing the OS, the boot loader loads the kernel of the selected operating system into RAM and passes control to it.
+ The boot loader loads the selected kernel image and passes control to it. Kernels are almost always compressed, so its first job is to uncompress itself. After this, it will check and analyze the system hardware and initialize any hardware device drivers built into the kernel.

![image][img4]

## Initial RAM Disk
The __initramfs__ filesystem image contains programs and binary files that perform all actions needed to mount the proper root filesystem, like providing kernel functionality for the needed filesystem and device drivers for mass storage controllers with a facility called __udev__ (for __User Device__), which is responsible for figuring out which devices are present, locating the drivers they need to operate properly, and loading them. After the root filesystem has been found, it is checked for errors and mounted.

The __mount__ program instructs the operating system that a filesystem is ready for use, and associates it with a particular point in the overall hierarchy of the filesystem (the __mount point__). If this is successful, the __initramfs__ is cleared from RAM and the __init__ program on the root filesystem (/sbin/init) is executed.

__init__ handles the mounting and pivoting over to the final real root filesystem. If special hardware drivers are needed before the mass storage can be accessed, they must be in the __initramfs__ image.

![image][img5]

## Text-Mode Login
Near the end of the boot process, __init__ starts a number of text-mode login prompts. These enable you to type your username, followed by your password, and to eventually get a command shell. However, if you are running a system with a graphical login interface, you will not see these at first.

As you will learn in the  __Command Line Operations__ section, the terminals which run the command shells can be accessed using the __ALT__ key plus a function key. Most distributions start six text terminals and one graphics terminal starting with __F1__ or __F2__. Within a graphical environment, switching to a text console requires pressing __CTRL-ALT +__ the appropriate function key (with __F7__ or __F1__ leading to the GUI).

Usually, the default command shell is __bash__ (the __GNU Bourne Again Shell__), but there are a number of other advanced command shells available. The shell prints a text prompt, indicating it is ready to accept commands; after the user types the command and presses __Enter__, the command is executed, and another prompt is displayed after the command is done.

![image][img6]

## Knowledge Check
Which one of the following component actually loads Linux?

    A. Boot loader
    B. init
    C. X Window System
    D. BIOS

    Ans: A
    Explanation
    The boot loader is software that executes after the hardware's BIOS completes its startup tests. The boot loader then loads the operating system.
    Submit


# Section 2: Kernel, init and Services
## The Linux Kernel
The boot loader loads both the kernel and an initial RAM–based file system (__initramfs__) into memory, so it can be used directly by the kernel.  

When the kernel is loaded in RAM, it immediately initializes and configures the computer’s memory and also configures all the hardware attached to the system. This includes all processors, I/O subsystems, storage devices, etc. The kernel also loads some necessary user space applications.

![image][img7]

## /sbin/init and Services
Once the kernel has set up all its hardware and mounted the root filesystem, the kernel runs the /sbin/init program. This then becomes the initial process, which then starts other processes to get the system running. Most other processes on the system trace their origin ultimately to init; the exceptions are the kernel processes, started by the kernel directly for managing internal operating system details.

Besides starting the system, __init__ is responsible for keeping the system running and for shutting it down cleanly. One of its responsibilities is to act when necessary as manager for all non-kernel processes; it cleans up after them upon completion, and restarts user login services as needed when users log in and out, and does the same for other background system services.

Traditionally, this process startup was done using conventions that date back to __System V UNIX__, with the system passing through a sequence of __runlevels__ containing collections of scripts that start and stop services. Each runlevel supports a different mode of running the system. Within each runlevel, individual services can be set to run, or to be shut down if running.

However, all major recent distributions have moved away from this sequential runlevel method of system initialization, although they usually support the System V conventions for compatibility purposes. Next, we discuss the new methods, __systemd__ and __Upstart__.

![image][img8]

## Startup Alternatives: Upstart and systemd
The older startup system (__SysVinit__) viewed things as a __serial__ process, divided into a series of sequential stages. Each stage required completion before the next could proceed. Thus, startup did not easily take advantage of the parallel processing that could be done on multiple processors or cores.

Furthermore, shutdown and reboot was seen as a relatively rare event; exactly how long it took was not considered important. This is no longer considered true, especially with mobile devices and embedded Linux systems. Thus, modern systems have required newer methods with enhanced capabilities. Finally, the older methods required rather complicated startup scripts which were difficult to keep universal across distribution versions, kernel versions, architectures, and types of systems. The two main alternatives developed were:

+ __Upstart__
    + Developed by __Ubuntu__ and first included in 2006
    + Adopted in __Fedora 9__ (in 2008) and in __RHEL 6__ and its clones.
+ __systemd__
    + Adopted by __Fedora__ first (in 2011)
    + Adopted by __RHEL 7__ and __SUSE__
    + Replaced Upstart in __Ubuntu 16.04__.

While the migration to __systemd__ has been rather controversial, it has been pursued by the major distributions and so we will not discuss the older __System V__ method or Upstart, which has become a dead end.  Regardless of how one feels about the controversies or the technical methods of __systemd__, almost universal adoption has made learning how to work on Linux systems simpler, as there are fewer differences among distributions. We enumerate __systemd__ features next.

## systemd Features
Systems with __systemd__ boot faster than those with earlier init methods. This is largely because it replaces a serialized set of steps with aggressive parallelization techniques, which permits multiple services to be initiated simultaneously.

Complicated startup shell scripts are replaced with simpler configuration files, which enumerate what has to be done before a service is started, how to execute service startup, and what conditions the service should indicate have been accomplished when startup is finished.

One systemd command (__systemctl__) is used for most basic tasks. While we have not yet talked about working at the command line, here is a brief listing of its use:

+ Starting, stopping, restarting a service (__fooservice__ could be something like __nfsd__ or the network) on a currently running system:
`$ sudo systemctl start/stop/restart fooservice`
+ Enabling or disabling a system service from starting up at system boot:
`$ sudo systemctl enable/disable fooservice`

There are many other technical differences with older methods beyond the scope of our discussion.  

## Knowledge Check
Which of the following is responsible for starting system and network services at boot time?

    A. kernel
    B. boot loader
    C. init
    D. GRUB

    Ans: C
    Explanation
    init is the parent of all non-kernel processes in Linux and is responsible for starting system and network services at boot time.


# Section 3: Linux Filesystem Basics
## Linux Filesystems
Think of a refrigerator that has multiple shelves that can be used for storing various items. These shelves help you organize the grocery items by shape, size, type, etc. The same concept applies to a __filesystem__, which is the embodiment of a method of storing and organizing arbitrary collections of data in a human-usable form.

__Different Types of Filesystems Supported by Linux__:

+ Conventional disk filesystems: __ext2, ext3, ext4, XFS, Btrfs, JFS, NTFS__, etc.
+ Flash storage filesystems: __ubifs, JFFS2, YAFFS__, etc.
+ Database filesystems
+ Special purpose filesystems: __procfs, sysfs, tmpfs, debugfs__, etc.

This section will describe the standard filesystem layout shared by most Linux distributions.

## Partitions and Filesystems
A partition is a logical part of the disk, whereas a filesystem is a method of storing/finding files on a hard disk (usually in a partition). By way of analogy, you can think of filesystems as being like family trees that show descendants and their relationships, while the partitions are like different families (each of which has its own tree).

A comparison between filesystems in Windows and Linux is given in the following table:

|   | Windows  | Linux |
----|----------|-------|
| Partition	| Disk1	| /dev/sda1|
| Filesystem type | NTFS/VFAT | EXT3/EXT4/XFS/BTRFS...|
| Mounting Parameters | DriveLetter | MountPoint |
| Base Folder where OS is stored |C:\ | / |

## The Filesystem Hierarchy Standard
__Linux__ systems store their important files according to a standard layout called the __Filesystem Hierarchy Standard (FHS)__, which has long been maintained by __The Linux Foundation__. You can read and/or download the official document that provides details from [here][fhs]. Having a standard is designed to ensure that users, administrators, and developers can move between distributions without having to re-learn how the system is organized.

Linux uses the '`/`' character to separate paths (unlike Windows, which uses '`\`'), and does not have drive letters. Multiple drives and/or __partitions__ are __mounted__ as directories in the single filesystem. Removable media such as __USB__ drives and __CDs__ and __DVDs__ will show up as mounted at `/run/media/yourusername/disklabel` for recent Linux systems, or under `/media` for older distributions. For example, if your username is student a __USB__ pen drive labeled __FEDORA__ might end up being found at `/run/media/student/FEDORA`, and a file __README.txt__ on that disc would be at `/run/media/student/FEDORA/README.txt`.

![image][img9]

All Linux filesystem names are __case-sensitive__, so `/boot`, `/Boot`, and `/BOOT` represent three different directories (or folders). Many distributions distinguish between core utilities needed for proper system operation and other programs, and place the latter in directories under `/usr` (think "__user__"). To get a sense for how the other programs are organized, find the `/usr` directory in the diagram below and compare the subdirectories with those that exist directly under the system root directory (`/`).

Note: The next screen covers the Try-It-Yourself activity for Ubuntu. 

![image][imga]

## Viewing the Filesystem Hierarchy from the Graphical Interface in Ubuntu
Click below to view a video on how to view the filesystem hierarchy from the graphical interface in __Ubuntu__. Please note that this exactly the same on all recent Linux distributions, except perhaps for where to click to start the File Manager program.  We will show the equivalent video for __openSUSE__ but not bother with __CentOS 7__.

[video][vid2]

## Viewing the Filesystem Hierarchy from the Graphical Interface in openSUSE
Click  below to view a video on how to view the filesystem hierarchy from the graphical interface in openSUSE.

[video][vid3]

## Try-It-Yourself: Viewing the Filesystem Hierarchy
Because viewing the Filesystem Hierarchy is exactly the same in the major distribution families, since they all use the same File Manager program, we only do this exercise with Ubuntu.

[Viewing the Filesystem Hierarchy from the Graphical Interface in Ubuntu][ufs]

## Knowledge Check
Please select a possible correct full path for a file named photo.jpg on a Linux system.

    A. /.data.user1.images.photo.jpg
    B. /Data_user1_images_photo.jpg
    C. /data/user1/images/photo.jpgcorrect
    D. c:\data\user1\images\photo.jpg

    Ans: C
    Explanation
    A possible correct full path for a file named "photo.jpg" on a Linux system is /data/user1/images/photo.jpg.


# Section 4: Linux Distribution Installation
## Choosing a Linux Distribution
![image][imgb]

Suppose you intend to buy a new car. What factors do you need to consider to make a proper choice? Requirements which need to be taken into account include your expected budget, available financing options, the size needed to fit your family in the vehicle, the type of engine, after-sales services, etc.

Similarly, determining which distribution to deploy also requires planning. The figure shows some, but not all choices, as there are other choices for distributions and standard embedded Linux systems are mostly neither __Android__ nor __Tizen__, but slimmed down standard distributions.

## Questions to Ask When Choosing a Distribution
Some questions worth thinking about before deciding on a distribution include:

+ What is the main function of the system (server or desktop)?
+ What types of packages are important to the organization? For example, web server, word processing, etc.
+ How much hard disk space is available? For example, when installing Linux on an embedded device, there will be space limitations.
+ How often are packages updated?
+ How long is the support cycle for each release? For example, __LTS__ releases have long term support.
+ Do you need kernel customization from the vendor?
+ What hardware are you running the Linux distribution on? For example, __X86, ARM, PPC__, etc.
+ Do you need long-term stability or short-term experimental software?

## Linux Installation: Planning
A __partition__ layout needs to be decided at the time of installation because Linux systems handle partitions by mounting them at specific points in the filesystem. You can always modify the design later, but it is always easier to try and get it right to begin with.

Nearly all installers provide a reasonable filesystem layout by default, with either all space dedicated to normal files on one big partition and a smaller swap partition, or with separate partitions for some space-sensitive areas like `/home` and `/var`. You may need to override the defaults and do something different if you have special needs, or if you want to use more than one disk.

![image][imgc]

## More About Planning in Linux Installation
All installations include the bare minimum software for running a Linux distribution.

Most installers also provide options for adding categories of software. Common applications (such as the __Firefox__ web browser and __LibreOffice__ office suite), developer tools (like the __vi__ and __emacs__ text editors, which we will explore later in this course), and other popular services, (such as the __Apache__ web server tools or __MySQL__ database) are usually included. In addition, a desktop environment is installed by default.

All installers secure the system being installed as part of the installation. Usually, this consists of setting the password for the superuser (root) and setting up an initial user. In some cases (such as __Ubuntu__), only an initial user is set up; direct root login is disabled and root access requires logging in first as a normal user and then using `sudo`, as we will describe later. Some distributions will also install more advanced security frameworks, such as __SELinux__ or __AppArmor__.

![image][imgd]

## Linux Installation: Install Source
Like other operating systems, Linux distributions are provided on removable media such as USB drives and CDs or DVDs. Most Linux distributions also support booting a small image and downloading the rest of the system over the network. These small images are usable on media or as network boot images, making it possible to install without any local media at all.

Many installers can do an installation completely automatically, using a configuration file to specify installation options. This file is called a __Kickstart__ file for __Fedora__-based systems, an __AutoYAST__ profile for __SUSE__-based systems, and a __preseed file__ for the __Debian__-based systems.

Each distribution provides its own documentation and tools for creating and managing these files.

## Linux Installation: The Process
The actual installation process is pretty similar for all distributions.

After booting from the installation media, the installer starts and asks questions about how the system should be set up. (These questions are skipped if an automatic installation file is provided.) Then, the installation is performed.

Finally, the computer reboots into the newly-installed system. On some distributions, additional questions are asked after the system reboots.

Most installers have the option of downloading and installing updates as part of the installation process; this requires Internet access. Otherwise, the system uses its normal update mechanism to retrieve those updates after the installation is done.

Note: The next few screens demonstrate the Installation process in each of the three Linux distribution families we cover in this course. You can view a demonstration for the distribution type of your choice.

## Linux Installation: The Warning
IMPORTANT!

The demonstrations show how to install Linux directly on your machine, erasing everything that was there. While the demonstrations will not alter your computer, following these procedures in real life will erase all current data. The Linux Foundation has a document available [here][inst] that describes alternate methods of installing Linux without over-writing existing data that you may want to consult if you need to preserve the information on your hard disk.

These alternate methods are:

+ Re-partitioning your hard disk to free up enough room to permit dual boot (side-by-side) installation of Linux, along with your present operating system.
+ Using a host machine hypervisor program (such as VMWare's products or Oracle Virtual Box) to install a client Linux Virtual Machine.
+ Booting off of and using a Live CD or USB stick and not writing to the hard disk at all.

The first method is sometimes complicated and should be done when your confidence is high and you understand the steps involved. The second and third methods are quite safe and make it difficult to damage your system.

## Steps to Install Ubuntu
Click below to view a video to learn the steps to install __Ubuntu__, a member of the __Debian__ Family Version of Linux. Please note this video is for __Ubuntu 14.04__, while the rest of this course is more centered around __Ubuntu 16.04__.  However, there is almost no difference in content in the installation procedure.

[video][vid4]

## Steps to Install CentOS
Click below to view a video to learn the steps to install __CentOS__, a member of the __Fedora__ family version of Linux. Please note this video is for __CentOS 6__, while the rest of this course is more centered around __CentOS 7__.  However, there is almost no difference in content in the installation procedure.

[vido][vid5]

## Steps to Install openSUSE
Click below to view a video to learn the steps to install __openSUSE__, a member of the __SUSE__ family version of Linux.  Please note this video is for __openSUSE 13.1__, while the rest of this course is more centered around __openSUSE-LEAP-42__.  However, there is almost no difference in content in the installation procedure.

[video][vid6]

## Knowledge Check
1. You have just brought home a new set top box for your television, that includes a digital video recorder (DVR). It is probably running Linux, like most currently popular multi-media appliances. 

    Which variety of Linux would you expect to have been installed on it?

    a. A Desktop version with a friendly graphical interface

    b. A Server version, such as Red Hat Enterprise Linux

    c. A specialized version with only the minimal set of software needed to accomplish its task 

    Ans: C

    Explanation
    Linux-based appliances have rather specialized needs and usually have customized installations that do not use any extra memory or storage.

2. What type of Linux configuration file(s) is/are used to automate the installation process?

    A. Kickstart

    B. AutoYaST

    C. CD/DVD

    D. USB

    Ans: A, B

    Explanation
    For Fedora-based systems, Kickstart is used to automate the installation process and for SUSE-based systems, AutoYAST installations are used for automating the installation process.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ A __partition__ is a logical part of the disk.
+ A __filesystem__ is a method of storing/finding files on a hard disk.
+ By dividing the hard disk into partitions, data can be grouped and separated as needed. When a failure or mistake occurs, only the data in the affected partition will be damaged, while the data on the other partitions will likely survive.
+ The boot process has multiple steps, starting with __BIOS__, which triggers the __boot loader__ to start up the __Linux kernel__. From there, the __initramfs__ filesystem is invoked, which triggers the __init__ program to complete the startup process.
+ Determining the appropriate distribution to deploy requires that you match your specific system needs to the capabilities of the different distributions.





[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009600_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004800_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002000_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006700_DTH.mp4
[vid5]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007700_DTH.mp4
[vid6]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V010400_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0ca63407bd9efcd5b980b6df0ea07ef2/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chapter03_flowchart_scr15_th_1.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f02a193180acffca543bf8f69870cc79/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen16.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b053b7b69e99a0c06ef0da7fd84236d7/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen20.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/abd1fcc0cc9a6fe48d886efdd98711ef/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen18.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/13f8548b13ebe15a19aa1a6c3964fceb/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen22.jpg
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e35bea5a8c6b9a41453a0e01c5ca3077/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen26.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b953394cd3145a1bd239673dc5c5a5b7/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen21.jpg
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/640a31713f9fded06718cb06c468f685/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen24.jpg
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/71b440fdff2f4f06605b78916081d396/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chapter03_flowchart_scr05a.jpg
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/cfe1173f34f6dfd285082a41cecfb54d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chapter03_flowchart_scr06.jpg
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dd787615daeae99f4a13ec156c807005/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chapter03_flowchart_scr32.jpg
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ae8955c30e5b10b2fd1cab2c79673555/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen_34.jpg
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/10f3cbf30f540761b32e02764de07e5c/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen_35.jpg


[fhs]: https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf
[ufs]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/fileexploreubuntu/index.html
[inst]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3fa6f8f7a7482a6344efeb7dd0d5bdf0/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/Preparing_Your_Computer_for_LFS101x.pdf


