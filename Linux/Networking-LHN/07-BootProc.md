# Ch07 : [The Linux Boot Process](http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch07_:_The_Linux_Boot_Process)

## The Linux Boot Sequence

<img src="https://geekstuffweb.files.wordpress.com/2014/08/2732a-rhce_linux_boot_diagram.png?w=794&h=1123&zoom=2" width="400" alt="Linux Boot Process">

<img src="https://blog.frognew.com/images/2017/01/linux-boot-process.jpg" width="300" alt="Linux Boot Porcess & Env Init">

+ __Master Boot Record (MBR)__: the very first sector of the hard disk  reserved for programmable code used in booting
+ When booting from a hard disk, the PC system BIOS starts by loading and executing bootloader code.
+ Fedora Linux: Grub staged bootloader system
+ Grub Version 1
    + _Stage 1_: run bootloader code (boot.img) from the MBR
    + _Stage 1.5_: additional code loaded from the 30 kilobytes of hard disk immediately after the , including enough partition and filesystem drivers to allow the Stage 2 to be loaded from a known location in the boot filesystem, usually `/boot/grub`
    + _Stage 2_: load other required drivers and kernel modules before reading the Grub configuration file and displaying the boot menu
+ Grub Version 2
    + _Stage 1_: read an image file (core.img) in the 30 kilobytes after the MBR
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

+ Runlevel and Target Descriptions

    | Runlevel | Target | Description |
    |:----------:|--------|-------------|
    | 0 | runlevel0.target , poweroff.target | Halt |
    | 1 | runlevel1.target, rescue.target | Single-user mode |
    | 2 | runlevel2.target | Not used (user-definable) |
    | 3 | runlevel3.target , multi-user.target | Full multi-user mode (no GUI interface) |
    | 4 | runlevel4.target | Not used (user-definable) |
    | 5 | runlevel5.target, graphical.target | Full multiuser mode (with GUI interface) |
    | 6 | runlevel6.target, reboot.target | Reboot |

+ Differences between the `init` and `systemd` systems
    + `init`: 
        + The daemon startup scripts in the `/etc/rc.X/` directory are executed, where "X" is the run level
        + Daemons started sequentially
        + Daemons tracked by process IDs (PIDs) without constraints on resource usage
    + `systemd`:
        + create target directories for daemons in `/etc/systemd/system/`
        + create custom post boot states
        + Daemons started in parallel
        + Daemons tracked by control groups or `cgroups` which limit system resources by class of daemon.

+ __Systemd__
    + Systemd Target File Locations

        | Target | Directory |
        |-------|-----------|
        | Default | /etc/systemd/system/default.target.wants |
        | Multiuser | /etc/systemd/system/multi-user.target.wants |
        | Network | /etc/systemd/system/network.target.wants |
        | Sockets | /etc/systemd/system/sockets.target.wants |
        | Sysinit | /etc/systemd/system/sysinit.target.wants |

    + Fedora RPM daemon packages install their files in the correct locations so that they work correctly at each target level.
    + Steps of system boots:
        1. `systemd` reads all the `.target` files in the `/lib/systemd/system/` directory, containing
            + a list of services that need to be run during the target activation
            + a list of pre-requisite targets that have to be completed and the target which must be completed immediately beforehand
            + Example
                ```cfg
                #
                # File: /lib/systemd/system/basic.target
                #
                [Unit]
                Description=Basic System
                Requires=sysinit.target sockets.target
                After=sysinit.target sockets.target
                RefuseManualStart=yes
                ```
        2. create a master list of services and start in order; stop after executing the services in the `default.target` file found in the `/etc/systemd/system/`        3. When all this is completed without errors, the system has booted successfully.

    + Important Systemd Boot Related Commands

        | Desired Result | Command |
        |----------------|---------|
        | Determine the current default target group | `# ll /etc/systemd/system/default.target` |
        | Determine the current active target group (Alternative method) | `# runlevel` |
        | Set the default target group (multi-user) | `# systemctl enable multi-user.target` |
        | Change the current target group (multi-user) | `# systemctl isolate multi-user.target` / `# systemctl isolate runlevel3.target` |
        | List all active targets in the active target group | `# systemctl list-units --type=target` |

    + Determine the current default target group
        + default target: `/etc/systemd/system/default.target`
        + Verify: `ll /etc/systemd/system/default.target`
        + Active tagrgets: 
            ```shell
            [root@bigboy tmp]# systemctl list-units --type=target 
            UNIT                LOAD   ACTIVE SUB    JOB DESCRIPTION
            basic.target        loaded active active     Basic System
            cryptsetup.target   loaded active active     Encrypted Volumes
            getty.target        loaded active active     Login Prompts
            local-fs-pre.target loaded active active     Local File Systems (Pre)
            local-fs.target     loaded active active     Local File Systems
            multi-user.target   loaded active active     Multi-User
            network.target      loaded active active     Network
            remote-fs.target    loaded active active     Remote File Systems
            sockets.target      loaded active active     Sockets
            sound.target        loaded active active     Sound Card
            swap.target         loaded active active     Swap
            sysinit.target      loaded active active     System Initialization
            syslog.target       loaded active active     Syslog

            LOAD   = Reflects whether the unit definition was properly loaded.
            ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
            SUB    = The low-level unit activation state, values depend on unit type.
            JOB    = Pending job for the unit.
            ```

    + Set the default target group - 2 ways
        + `systemd` cmd: `systemctl enable x.target`  
            > `systemctl enable multi-user.target`  
            > `systemctl enable graphical.target`
        + `ln -sf`: link the `/lib/systemd/system/*.target` file to `/etc/systemd/system/default.target`:   
            > `ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target`   
            > `ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target`

+ __SysV Init__
    + Init Runlevel File Locations

        | Runlevel | Directory |
        |----------|-----------|
        | 0 | `/etc/rc.d/rc0.d` |
        | 1 | `/etc/rc.d/rc1.d` |
        | 2 | `/etc/rc.d/rc2.d` |
        | 3 | `/etc/rc.d/rc3.d` |
        | 4 | `/etc/rc.d/rc4.d` |
        | 5 | `/etc/rc.d/rc5.d` |
        | 6 | `/etc/rc.d/rc6.d` |
    
    + listing of the scripts in the `/etc/rc.d/rc3.d`
        ```shell
        [root@bigboy tmp]# ls /etc/rc.d/rc3.d
        ...    ...    K75netfs      K96pcmcia    ...    ...
        ...    ...    K86nfslock    S05kudzu     ...    ...
        ...    ...    K87portmap    S09wlan      ...    ...
        ...    ...    K91isdn       S10network   ...    ...
        ...    ...    K92iptables   S12syslog    ...    ...
        ...    ...    K95firstboot  S17keytable  ...    ...
        ```
        + "S": run at startup
        + "K": run when shutting down
        + "number" following "K" or "S": scripts run in ascending order
        + autogen: Fedora using `chkconfig` while Debian / Ubuntu using `update-rc.d`
    + Most Linux packages place their startup script in the `/etc/init.d/` and place symbolic links (pointers) to this script in the appropriate subdirectory of `/etc/rc.d/`.

    + Determining and Setting the Default Boot runlevel
        + default boot runlevel set in `/etc/inittab` with `initdefault` variable
        + Snippet of the file:
            ```cfg
            # Default runlevel. The runlevels used by RHS are:
            # 0 - halt (Do NOT set initdefault to this)
            # 1 - Single user mode
            # 2 - Multiuser, without NFS (The same as 3, if you do not have networking)
            # 3 - Full multiuser mode
            # 4 - unused
            # 5 - X11
            # 6 - reboot (Do NOT set initdefault to this)
            # 
            id:3:initdefault:                         # Console Text Mode
            id:5:initdefault:                         # Console GUI Mode
            ```
            + Most home users: GUI (runlevel 5)
            + Most techies: CLI (runlevel 3)
            + Changing `initdefault` from 3 to 5, or vice-versa: effect upon next reboot

## System Shutdown and Rebooting

+ Halt/Shut Down The System
    + SysV cmd: `init 0`
    + Fedora cmd : `shutdown -hy 0` (0 = Now, # = mins)
+ Reboot The System
    + SysV cmd: `init 6`
    + Fedora cmd: `reboot` or `shutdown -ry <min>`
+ Entering Single-user Mode
    + Switching to Single-user Mode
        + SysV cmd: `init 1`
        + Entering maintenance mode: `shutdown 1`
    + Entering Single-user Mode At The Grub Splash Screen
        1. Power on your system. Wait for the "Grub loading" message to appear and, depending on your Linux distribution, get ready to hit either any key or the ESC key to enter the grub boot menu.
        2. Use the arrow keys to scroll to your desired version of the kernel and then press e for "edit"
        3. Use the arrow keys to scroll to the "kernel" line and then press e for "edit"
        4. Use the arrow keys to move to the end of the line and add the word "single" to the end, separated by a space:
            > grub edit> kernel /vmlinuz-2.6.18-1.2239.fc5smp ro root=LABEL=/  
            > grub edit> kernel /vmlinuz-2.6.18-1.2239.fc5smp ro root=LABEL=/ single
        5. Save changes, and then `b` for "boot"
        6. system  boot w/ root `#` prompt
    + Reverting To Your Default runlevel From Single User Mode
        + forcing the system to exit runlevel 1 and revert to the default runlevel for the system: `exit`
    + Root Password Recovery
        1. `Ctrl-Alt-Del`: shut down in an orderly fashion
        2. Reboot the system and enter single-user mode
        3. Once at the command prompt, change your password.
        4. Return to default runlevel w/ `exit` cmd

## The Linux Console

+ Getting a GUI Console
    + manual method: `startx`
    + Automatic method: `init 5`
+ Get a Basic Text Terminal Without Exiting the GUI
    + Using a GUI Terminal Window
        + Click on the Fedora logo button in the bottom left hand corner of the screen.
        + Click on Systems Tools and then Terminal
    + Using Virtual Consoles
        + default: 6 virtual console or TTY sessions
        + defined by the `mingetty` statements in the `/etc/inittab` file
        + switch between virtual consoles: `Ctl-Alt-Fn`, where `n`=1~6
        + GUI login: `CTl-Alt-F7` w/ runlevel 5 or `startx` at CLI

