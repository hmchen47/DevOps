Introduction to Linux
=====================

Chapter 03: Linux Basics and System Startup
===========================================

Introduction/ Learning Objectives
---------------------------------
# Linux Basics and System Setup
[video][video1]

# Learning Objectives
By the end of this chapter, you should be able to:

    + Identify Linux filesystems.
    + Identify the differences between partitions and filesystems.
    + Describe the boot process.
    + Install Linux on a computer.


Section 1: The Boot Process
---------------------------
# The Boot Process
Have you ever wondered what happens in the background from the time you press the __Power__ button until the Linux login prompt appears?  

The Linux __boot process__ is the procedure for initializing the system. It consists of everything that happens from when the computer power is first switched on until the user interface is fully operational. 

Once you start using Linux, you will find that having a good understanding of the steps in the boot process may help you with troubleshooting problems, as well as with tailoring the computer's performance to your needs.  

On the other hand, the boot process can be rather technical. You may want to come back and study this section later, if you want to first get a good feel for how to use a Linux system.

![image][img1]

# BIOS - The First Step
Starting an __x86__-based Linux system involves a number of steps. When the computer is powered on, the __Basic Input/Output System (BIOS)__ initializes the hardware, including the screen and keyboard, and tests the main memory. This process is also called __POST (Power On Self Test)__.

The BIOS software is stored on a ROM chip on the motherboard. After this, the remainder of the boot process is controlled by the operating system (OS).

![image][img2]

# Master Boot Record (MBR)
Once the __POST__ is completed, the system control passes from the __BIOS__ to the boot loader. The boot loader is usually stored on one of the hard disks in the system, either in the boot sector (for traditional __BIOS/MBR__ systems) or the __EFI__ partition (for more recent __(Unified) Extensible Firmware Interface__ or __EFI/UEFI__ systems). Up to this stage, the machine does not access any mass storage media. Thereafter, information on the date, time, and the most important peripherals are loaded from the __CMOS__ values (after a technology used for the battery-powered memory store - which allows the system to keep track of the date and time even when it is powered off).

A number of boot loaders exist for Linux; the most common ones are __GRUB__ (for __GRand Unified Boot loader__) and __ISOLINUX__ (for booting from removable media), and __DAS U-Boot__ (for booting on embedded devices/appliances). Most Linux boot loaders can present a user interface for choosing alternative options for booting Linux, and even other operating systems that might be installed. When booting Linux, the boot loader is responsible for loading the kernel image and the initial __RAM__ disk or filesystem (which contains some critical files and device drivers needed to start the system) into memory.

[image][img3]

# Boot Loader in Action
The boot loader has two distinct stages:

First Stage:

    + For systems using the __BIOS/MBR__ method, the boot loader resides at the first sector of the hard disk, also known as the __Master Boot Record (MBR)__. The size of the __MBR__ is just `512 bytes`. In this stage, the boot loader examines the partition table and finds a bootable partition. Once it finds a bootable partition, it then searches for the second stage boot loader e.g, __GRUB__, and loads it into __RAM__ (Random Access Memory).
    + For systems using the EFI/UEFI method, UEFI firmware reads its Boot Manager data to determine which UEFI application is to be launched and from where (i.e., from which disk and partition the EFI partition can be found). The firmware then launches the UEFI application, for example, GRUB, as defined in the boot entry in the firmware's boot manager. This procedure is more complicated, but more versatile than the older MBR methods.

Second Stage:

    The second stage boot loader resides under /boot. A splash screen is displayed, which allows us to choose which Operating System (OS) to boot. After choosing the OS, the boot loader loads the kernel of the selected operating system into RAM and passes control to it.

    The boot loader loads the selected kernel image and passes control to it. Kernels are almost always compressed, so its first job is to uncompress itself. After this, it will check and analyze the system hardware and initialize any hardware device drivers built into the kernel.

[image][img4]


Section 2: Kernel, init and Services
------------------------------------



Section 3: Linux Filesystem Basics
----------------------------------



Section 4: Linux Distribution Installation
------------------------------------------



Summary
-------



[video1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009600_DTH.mp4
[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0ca63407bd9efcd5b980b6df0ea07ef2/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chapter03_flowchart_scr15_th_1.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f02a193180acffca543bf8f69870cc79/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen16.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b053b7b69e99a0c06ef0da7fd84236d7/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen20.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/abd1fcc0cc9a6fe48d886efdd98711ef/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen18.jpg
