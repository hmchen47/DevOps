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
    + config file: `/boot/grub/grub.conf`
    + used to create GRUB startup menu
    + Sample config file
        ```cfg
        default=0
        timeout=10
        splashimage=(hd0,0)/grub/splash.xpm.gz
        title Fedora Core (2.6.8-1.521)
                root (hd0,0)
                kernel /vmlinuz-2.6.8-1.521 ro root=LABEL=/
                initrd /initrd-2.6.8-1.521.img
        title Windows 2000
            rootnoverify (hd0,1)
            chainloader +1
        ```
    + `default=0`: system boots the first kernel entry (2.6.8-1.521) when you either:
        + "enter" key: presented with the startup splash screen and boot menu
        + timeout: auto boots in an unattended mode
    +  `deault=1`: Windows boots
    + Fedora kernel file: `vmlinuz-2.6.8-1.521`
    + memory based root filesystem image: `initrd-2.6.8-1.521.img`
    + `(hd0,0)` and `(hd0,1)`: the first and second partitions of device `/dev/hda`
        + `/boot/grub/device.map` file maps the Grub device nomenclature to that expected by Linux
        + `/boot/grub/device.map`: `(fd0)     /dev/fd0` & `(hd0)     /dev/hda`

+ Grub Version 2 Configuration
    + updating from old version w/ config files in `/etc/grub/`
    + `grub2-mkconfig`: create an updated grub menu configuration file `/boot/grub2/grub.cfg`
        ```cfg

        # File: /boot/grub2/grub.cfg
        ...
        menuentry 'Fedora (3.4.2-1.fc16.x86_64)' --class fedora --class gnu-linux --class gnu --class os {
                echo 'Loading Fedora (3.4.2-1.fc16.x86_64)'
                linux   /vmlinuz-3.4.2-1.fc16.x86_64 ...
                echo 'Loading initial ramdisk ...'
                initrd /initramfs-3.4.2-1.fc16.x86_64.img
        }
        ...
        ```
    + `menuentry` stanzas: define the entries to be shown in the boot menu and the parameters each requires
    + Sampled `/etc/default/grub` file -> `/boot/grub2/grub.cfg` auto-generated
        ```cfg
        #
        # File: /etc/default/grub
        #
        GRUB_TIMEOUT=5
        GRUB_DISTRIBUTOR="Fedora"
        GRUB_DEFAULT=saved
        GRUB_CMDLINE_LINUX="rd.md=0 rd.dm=0 rd.lvm.lv=vg_web003/LogVol01 \
            rd.lvm.lv=vg_web003/LogVol00 KEYTABLE=us quiet \
            SYSFONT=latarcyrheb-sun16 rhgb rd.luks=0 LANG=en_US.UTF-8"
        ```
        + `GRUB_TIMEOUT`: The timeout in seconds that the boot menu is displayed.
        + `GRUB_DISTRIBUTOR`: The distribution of Linux being used
        + `GRUB_SAVEDEFAULT`: When set to ‘true’, then the menu entry selected will be saved as the new default entry for all future reboots.
        + `GRUB_DEFAULT`: The name of the menuentry to use in the `/boot/grub2/grub.cfg` as the version of Linux to boot. If set to a number N, then the Nth entry is used. If set to "saved" then the value of `GRUB_SAVEDEFAULT` will be used. If `GRUB_SAVEDEFAULT` isn't defined, then the very first menuentry is used.
        + `GRUB_CMDLINE_LINUX`: A list of command-line arguments that will be added to the kernel menuentry stanzas in `/boot/grub2/grub.cfg`.

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


