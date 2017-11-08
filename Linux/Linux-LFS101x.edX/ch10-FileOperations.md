Chapter 10: File Operations
===========================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Explore the filesystem and its hierarchy.
+ Explain the filesystem architecture.
+ Compare files and identify different file types.
+ Back up and compress data.


# Section 1: Filesystems
## Introduction to Filesystems
In Linux (and all UNIX-like operating systems) it is often said “Everything is a file”, or at least it is treated as such. This means whether you are dealing with normal data files and documents, or with devices such as sound cards and printers, you interact with them through the same kind of Input/Output (I/O) operations. This simplifies things: you open a “file” and perform normal operations like reading the file and writing on it (which is one reason why text editors, which you will learn about in an upcoming section, are so important.)

On many systems (including Linux), the __filesystem__ is structured like a tree. The tree is usually portrayed as inverted, and starts at what is most often called the __root directory__, which marks the beginning of the hierarchical filesystem and is also sometimes referred to as the __trunk__, or simply denoted by `/`. The root directory is not the same as the root user. The hierarchical filesystem also contains other elements in the path (directory names), which are separated by forward slashes (/), as in `/usr/bin/emacs`, where the last element is the actual file name.

In this section, you will learn about some basic concepts, including the filesystem hierarchy, as well as about __disk partitions__.

![image][img1]

## Filesystem Varieties
Linux supports a number of native filesystem types, expressly created by Linux developers, such as

+ __ext3, ext4, squashfs, and btrfs.__

It also offers implementations of filesystems used on other alien operating systems, such as those from:

+ __Windows  (ntfs, vfat)__
+ __MacOS (hfs, hfs+)__
+ __IBM (JFS)__
+ __SGI (xfs).__

Many older, legacy filesystems, such as __FAT__, are also supported.

It is often the case that more than one filesystem type is used on a machine, based on considerations such as the size of files, how often they are modified, what kind of hardware they sit on and what kind of access speed is needed etc. The most advanced filesystem types in common use are the __journaling__ varieties: __ext4, xfs, btrfs__, and __jfs__. These have many state-of-the-art features and high performance, and are very hard to corrupt accidentally.

## Linux Partitions
As we discussed earlier, each filesystem on a Linux system occupies (is contained in)  a hard disk __partition__. Partitions help to organize the contents of disks according to the kind  and use of the data contained. For example, important programs required to run the system are often kept on a separate partition (known as __root__ or `/`) than the one that contains files owned by regular users of that system (`/home`). In addition, temporary files created and destroyed during the normal operation of Linux are often located on dedicated partitions. One advantage of this kind of isolation by type and variability is that when all available space on a particular partition is exhausted, the system may still operate normally.

![image][img2]

## Mount Points
Before you can start using a filesystem, you need to __mount__ it to the filesystem tree at a __mount point__. This is simply a directory (which may or may not be empty) where the filesystem is to be attached (mounted). Sometimes, you may need to create the directory if it does not already exist.

Warning: If you mount a filesystem on a non-empty directory, the former contents of that directory are covered-up and not accessible until the filesystem is unmounted. Thus, mount points are usually empty directories.

![image][img3]

## Mounting and Unmounting
The __mount__ command is used to attach a filesystem (which can be local to the computer or, as we shall discuss, on a network) somewhere within the filesystem tree. The basic arguments are the __device node__ and __mount point__. For example,

`$ mount /dev/sda5 /home`

will attach the filesystem contained in the disk partition associated with the `/dev/sda5` device node, into the filesystem tree at the /home mount point. There are other ways to specify the partition other than the device node, such as using the __disk label__ or __UUID__.

To __unmount__ the partition, the command would be:

`$ umount /home`

Note the command is `umount`, not unmount!  Only a root user (logged in as __root__, or using `sudo`) has the privilege to run these commands, unless the system has been otherwise configured.

If you want it to be automatically available every time the system starts up, you need to edit `/etc/fstab` accordingly (the name is short for __Filesystem Table__). Looking at this file will show you the configuration of all pre-configured filesystems. `man fstab` will display how this file is used and how to configure it.

Typing `mount` without any arguments will show all presently mounted filesystems.

The command `df -Th` (__disk-free__) will display information about mounted filesystems, including usage statistics about currently used and available space.

![image][img4]

## NFS and Network Filesystems
It is often necessary to share data across physical systems which may be either in the same location or anywhere that can be reached by the Internet. A __network__ (also sometimes called __distributed__) filesystem may have all its data on one machine or have it spread out on more than one network node. A variety of different filesystems can be used locally on the individual machines; a network filesystem can be thought of as a grouping of lower level filesystems of varying types.

Many system administrators mount remote users' home directories on a __server__ in order to give them access to the same files and configuration files across multiple __client__ systems. This allows the users to log in to different computers, yet still have access to the same files and resources.

The most common such filesystem is named simply __NFS__ (the __Network Filesystem__) and has a very long history and was first developed by Sun Microsystems. Another common implementation is __CIFS__ (also termed __SAMBA__), which has Microsoft roots. We will restrict our attention in what follows to __NFS__.

## NFS on the Server
We will now look in detail at how to use NFS on the server.

On the server machine, __NFS__ daemons (built-in networking and service processes in Linux) and other system servers are started at the command line by typing:

`sudo systemctl start nfs`

The text file `/etc/exports` contains the directories and permissions that a host is willing to share with other systems over NFS. A very simple entry in this file may look like the following:

`/projects *.example.com(rw)`

This entry allows the directory `/projects` to be mounted using NFS with read and write (`rw`) permissions and shared with other hosts in the `example.com` domain. As we will detail in the next chapter, every file in Linux has 3 possible permissions: read (`r`), write (`w`) and execute (`x`).

After modifying the `/etc/exports` file, you can use the `exportfs -av` command to notify Linux about the directories you are allowing to be remotely mounted using NFS. (You can also restart NFS with `sudo systemctl restart nfs`, but this is heavier, as it halts NFS for a short while before starting it up again.)  To make sure the NFS service starts whenever the system is booted, issue `sudo systemctl enable nfs`.

![image][img5]

## NFS on the Client
On the client machine, if it is desired to have the remote filesystem mounted automatically upon system boot, the `/etc/fstab` file is modified to accomplish this. For example, an entry in the client's `/etc/fstab` file might look like the following:

`servername:/projects /mnt/nfs/projects nfs defaults 0 0`

You can also mount the remote filesystem without a reboot or as a one-time mount by directly using the mount command:

`$ sudo mount servername:/projects /mnt/nfs/projects`

Remember, if `/etc/fstab` is not modified, this remote mount will not be present the next time the system is restarted.

![image][img6]

## Knowledge Check
1. Which of the following configuration files shows which filesystems will be automatically mounted when the system is brought up into multi-user mode?

        A. /etc/login.defs
        B. /etc/fstab 
        C. /etc/profile
        D. /proc/sys/fs

        Ans: BExplanation
        Filesystems listed in the /etc/fstab configuration file will be automatically mounted when the system is brought up into multi-user mode.

2. Which command can be used to inquire whether a filesystem is mounted as read-only or as read/write?

        A. df -Th
        B. cat /etc/fstab
        C. mount 
        D. exportfs -av

        Ans: C
        Explanation
        The mount command without options and arguments will list all of the currently mounted filesystems, along with information that will indicate whether they are mounted as read-only or writable. You could try looking at /etc/fstab, but that will usually only provide information about what happens at system start up.

3. Which of the following commands will ensure that the shared files are available over a network?

        A. exportfs 
        B. exportnfs
        C. exportfiles
        D. exportnetwork

        Ans: A
        Explanation
        exportfs will ensure that the shared files are available over a network.

## Lab 1: Exploring Mounted Filesystems
Issue the command::

`student:/tmp> cat /etc/fstab`

Now type:

`student:/tmp> mount`

Compare the results.  What are the differences?

Find another way to see a list of the mounted filesystems,  by examining the `/proc` pseudo-filesystem.

Click [the link][] to view a solution to the Lab exercise.

Solution:
> Typically, mount will show more filesystems mounted than are shown in `/etc/fstab` , which only lists those which are explicitly requested.
> The system, however, will mount additional special filesystems required for normal operation, which are not enumerated in `/etc/fstab`.
> 
> Another way to show mounted filesystems is to type:
> 
> `sudent:/tmp> cat /proc/mounts`
> 
> which is essentially how the utility gets its information.

# Section 2: Filesystem Architecture
## Overview of User Home Directories
Each user has a home directory, usually placed under `/home`. The `/root` ("slash-root") directory on modern Linux systems is no more than the home directory of the root user (or superuser, or system administrator account.)

On multi-user systems, the `/home` directory infrastructure is often mounted as a separate filesystem on its own partition, or even exported (shared) remotely on a network through __NFS__.

Sometimes, you may group users based on their department or function. You can then create subdirectories under the `/home` directory for each of these groups. For example, a school may organize `/home` with something like the following:
```
/home/faculty/
/home/staff/
/home/students/
```
In this section, you will learn to identify and differentiate between the most important directories found in Linux.

## The /bin and /sbin Directories
The `/bin` directory contains executable binaries, essential commands used to boot the system or in single-user mode, and essential commands required by all system users, such as:

| Command | Usage |
|---------|-------|
| `ps` | Produces a list of processes along with status information for the system. |
| `ls` | Produces a listing of the contents of a directory. |
| `cp` | Used to copy files. |

Likewise, the `/sbin` directory is intended for essential binaries related to system administration, such as __fsck__ and __shutdown__. To view a list of these programs, type: `ls /bin /sbin`.

![image][img7]
![image][img8]

Commands that are not essential (theoretically) for the system to boot or operate in single-user mode are placed in the `/usr/bin` and  `/usr/sbin` directories.  Historically, this was done so `/usr` could be mounted as a separate filesystem that could be mounted at a later stage of system startup or even over a network. However, nowadays most find this distinction is obsolete; in fact, many distributions have been discovered to be unable to boot with this separation, as this modality had not been used or tested for a long time. Thus, on the newest Linus distributions, `/usr/bin` and `/bin` are actually just symbolically linked together, as are `/usr/sbin` and `/sbin`. 

## The proc Filesystem
Certain filesystems, like the one mounted at `/proc`, are called __pseudo filesystems__ because they have no permanent presence anywhere on the disk.

The `/proc` filesystem contains virtual files (files that exist only in memory) that permit viewing constantly varying kernel data. This filesystem contains files and directories that mimic kernel structures and configuration information. It does not contain real files, but runtime system information (e.g. system memory, devices mounted, hardware configuration, etc). Some important files in `/proc` are:
```
/proc/cpuinfo
/proc/interrupts
/proc/meminfo
/proc/mounts
/proc/partitions
/proc/version
```
`/proc` has subdirectories as well, including:
```
/proc/<Process-ID-#>
/proc/sys
```
The first example shows there is a directory for every process running on the system, which contains vital information about it. The second example shows a virtual directory that contains a lot of information about the entire system, in particular its hardware and configuration. The `/pro`c` filesystem is very useful because the information it reports is gathered only as needed and never needs storage on the disk.

![image][img9]

## The /dev Directory
The `/dev` directory contains device nodes, a type of pseudo-file used by most hardware and software devices, except for network devices. This directory is:

+ Empty on the disk partition when it is not mounted
+ Contains entries which are created by the udev system, which creates and manages device nodes on Linux, creating them dynamically when devices are found. The /dev directory contains items such as:
    + /dev/sda1 (first partition on the first hard disk)
    + /dev/lp1 (second printer)
    + /dev/dvd1 (first DVD drive).

![image][imga]

## The /var Directory
The `/var` directory contains files that are expected to change in size and content as the system is running (__var__ stands for __variable__), such as the entries in the following directories:

+ System log files: `/var/log`
+ Packages and database files: `/var/lib`
+ Print queues: `/var/spool`
+ Temp files: `/var/tmp`

The `/var` directory may be put in its own filesystem so that growth of the files can be accommodated and the file sizes do not fatally affect the system. Network services directories such as `/var/ftp` (the FTP service) and `/var/www` (the HTTP web service) are also found under /var.

![image][imgb]

## The /etc Directory
The `/etc` directory is the home for system configuration files. It contains no binary programs, although there are some executable scripts. For example, the file `resolv.conf` tells the system where to go on the network to obtain host name to IP address mappings (DNS). Files like `passwd`, `shadow` and `group` for managing user accounts are found in the `/etc` directory. System runlevel scripts are found in subdirectories of `/etc`.  While some distributions have historically had their own extensive infrastructure under `/etc`  (for example, __Red Hat__ and __SUSE__ has used  `/etc/sysconfig`) , with the advent of systemd there is much more uniformity among distributions today.

Note that `/etc` is for system-wide configuration files and only the superuser can modify files there.  User-specific configuration files are always found under their home directory.

![image][imgc]

## The /boot Directory
The `/boot` directory contains the few essential files needed to boot the system. For every alternative kernel installed on the system there are four files:

1. `vmlinuz`: the compressed Linux kernel, required for booting
2. `initramfs`: the initial ram filesystem, required for booting, sometimes called initrd, not initramfs
3. `config`: the kernel configuration file, only used for debugging and bookkeeping
4. `System.map`: kernel symbol table, only used for debugging

Each of these files has a kernel version appended to its name.

The __Grand Unified Bootloader (GRUB)__ files (such as `/boot/grub/grub.conf` or `/boot/grub2/grub2.cfg`) are also found under the `/boot` directory.

The image shows an example listing of the `/boot` directory, taken from a __RHEL 7__ system that has multiple installed kernels, including both distribution-supplied and custom-compiled ones. Names will vary and things will tend to look somewhat different on a different distribution.

![image][imgd]

## The /lib and /lib64 Directories
`/lib` contains libraries (common code shared by applications and needed for them to run) for the essential programs in `/bin` and `/sbin`. These library filenames either start with `ld` or `lib`, for example, `/lib/libncurses.so.5.9`.

Most of these are what known as __dynamically loaded libraries__ (also known as __shared libraries__ or __Shared Objects (SO)__). On some Linux distributions there exists a `/lib64` directory containing 64-bit libraries, while `/lib` contains 32-bit versions.

Kernel __modules__ (kernel code, often device drivers, that can be loaded and unloaded without re-starting the system) are located in `/lib/modules/<kernel-version-number>`.

![image][imge]

## Removable media: the /media, /run and /mnt Directories
One often uses removable media, such as __USB__ drives and __CDs__ and __DVDs__.  To make the material accessible through the regular filesystem, it has to be mounted at a convenient location. Most Linux systems are configured so the removable media is automatically mounted when the system notices it has been plugged in.

Historically, this was done under the `/media` directory.  However, newer Linux distributions place these mount points under the `/run` directory.  For example, a USB pen drive with a label myusbdrive for a user name student would be mounted at `/run/media/student/myusbdrive`.

The  `/mnt` directory has been used since the early days of UNIX for temporarily mounting filesystems.  These might be network filesystems with __NFS__, not normally mounted or temporary partitions, or so-called __loopback__ filesystems, which are files which pretend to be partitions.

## Additional Directories Under /:
The following is a list of some additional directories under /and their purpose:

| Directory name | Usage |
|----------------|-------|
| `/opt` | Optional application software packages. |
| `/sys` | Virtual pseudo-filesystem giving information about the system and the hardware. Can be used to alter system parameters and for debugging purposes. |
| `/srv` | Site-specific data served up by the system. Seldom used. |
| `/tmp` | Temporary files; on some distributions erased across a reboot and/or may actually be a ramdisk in memory. |
| `/usr` | Multi-user applications, utilities and data. |

## The /usr Directory Tree
The /usr directory tree contains theoretically non-essential programs and scripts (in the sense that they should not be needed to initially boot the system) and has at least the following sub-directories:

| Directory name | Usage |
|----------------|-------|
| `/usr/include` | Header files used to compile applications. |
| `/usr/lib` | Libraries for programs in `/usr/bin` and `/usr/sbin`. |
| `/usr/lib64` | 64-bit libraries for 64-bit programs in `/usr/bin` and `/usr/sbin`. |
| `/usr/sbin` | Non-essential system binaries, such as system daemons. |
| `/usr/share` | Shared data used by applications, generally architecture-independent. |
| `/usr/src` | Source code, usually for the Linux kernel. |
| `/usr/local` | Data and programs specific to the local machine. Subdirectories include bin, sbin, lib, share, include, etc. |
| `/usr/bin` | This is the primary directory of executable commands on the system. |

## Knowledge Check
1. Which is the home directory of the superuser account?

        A. /bin
        B. /root 
        C. /dev
        D. /boot

        Ans: B
        Explanation
        /root is the home directory of the superuser account (root).

2. Where can you find the device nodes of a Linux system?

        A. /etc
        B. /mnt
        C. /dev 
        D. /var

        Ans: C
        Explanation
        Device nodes are located in the /dev directory.


# Section 3: Comparing Files and File Types
## Comparing Files with diff
Now that you know about the filesystem and its structure, so let’s learn how to manage files and directories.

`diff` is used to compare files and directories. This often-used utility program has many useful options (see `man diff`) including:

| diff Option | Usage |
|-------------|-------|
| `-c` | Provides a listing of differences that include 3 lines of context before and after the lines differing in content |
| `-r` | Used to recursively compare subdirectories, as well as the current directory |
| `-i` | Ignore the case of letters |
| `-w` | Ignore differences in spaces and tabs (white space) |
| `-q` | Be quiet: only report if files are different without listing the differences |

To compare two files, at the command prompt, type `diff [options] <filename1> <filename2>`.  `diff` is meant to be used for text files; for binary files, one can use `cmp`. 

In this section, you will learn additional methods for comparing files and how to apply patches to files.

## Using diff3 and patch
You can compare three files at once using `diff3`, which uses one file as the reference basis for the other two. For example, suppose you and a co-worker both have made modifications to the same file working at the same time independently. `diff3` can show the differences based on the common file you both started with. The syntax for `diff3` is as follows:

`$ diff3 MY-FILE COMMON-FILE YOUR-FILE`

The graphic shows the use of `diff3`.

![image][imgf]

Many modifications to source code and configuration files are distributed utilizing __patches__, which are applied, not surprisingly, with the __patch__ program. A patch file contains the __deltas__ (changes) required to update an older version of a file to the new one. The patch files are actually produced by running `diff` with the correct options, as in:

`$ diff -Nur originalfile newfile > patchfile`

Distributing just the patch is more concise and efficient than distributing the entire file. For example, if only one line needs to change in a file that contains 1,000 lines, the __patch__ file will be just a few lines long.

To apply a patch, you can just do either of the two methods below:
```
$ patch -p1 < patchfile
$ patch originalfile patchfile
```
The first usage is more common, as it is often used to apply changes to an entire directory tree, rather than just one file, as in the second example. To understand the use of the `-p1` option and many others, see the __man__ page for __patch__.

![image][imgg]

## Using the 'file' Utility
In Linux, a file's extension often does not categorize it the way it might in other operating systems. One cannot assume that a file named `file.txt` is a text file and not an executable program. In Linux, a filename is generally more meaningful to the user of the system than the system itself; in fact, most applications directly examine a file's contents to see what kind of object it is rather than relying on an extension. This is very different from the way __Windows__ handles filenames, where a filename ending with `.exe`, for example, represents an executable binary file.

The real nature of a file can be ascertained by using the `file` utility. For the file names given as arguments, it examines the contents and certain characteristics to determine whether the files are plain text, shared libraries, executable programs, scripts, or something else.

![image][imgh]

## Try-It-Yourself: Comparing Files
To practice, click [the link][compf] provided.

## Try-It-Yourself: Using file
To practice, click [the link][file] provided.

## Knowledge Check
1. Which of the following commands will recursively compare two directory trees, just mentioning which files are different, new or deleted?

        A. diff -wq /usr/src/linux-4.9 /usr/src/linux-4.10:
        B. diff -qr /usr/src/linux-4.9 /usr/src/linux-4.10:
        C. diff -sr /usr/src/linux-4.9 /usr/src/linux-4.10:
        D. diff -ir /usr/src/linux-4.9 /usr/src/linux-4.10:

        Ans: B
        Explanation
        The command diff -qr /usr/src/linux-4.9 /usr/src/linux-4.10: will recursively compare two directories (the -r option) and report only the differences (the -q option).

2. Which command will show you the type of the file named some_file?

        A. identify some_file
        B. locate some_file
        C. file some_file 
        D. diff some_file

        Ans: C
        Explanation
        Typing file data will show you the type of the file named some_file.

## Lab 2: Using diff and patch
Linux and other open source communities often use the __patch__ utility to disseminate modifications and updates. Here, we will give a practical introduction to using `diff` and `patch`.

It would be a good idea to read the man pages for both `patch` and `diff` to learn more about advanced options and techniques, that will help one to work more effectively with `patch`. In particular, the form of patches has a lot to do with whether they can be accepted in their submitted form.

1. Change to the `/tmp` directory.
2. Copy a text file to `/tmp`. For example, copy `/etc/group` to `/tmp`.
3. __dd__ cannot only copy directly from raw disk devices, but from regular files as well. (Remember, in Linux, everything is pretty much treated as a file.) __dd__ can also perform various conversions; the `conv=ucase` option will convert all of the characters to upper-case characters. We will use __dd__ to copy the text file to a new file in `/tmp` while converting characters to upper-case, as in `student:/tmp> dd if=/tmp/group of=/tmp/GROUP conv=ucase`.
4. According to the man page for patch, the preferred options for preparing a patch with `diff` are `-Naur` when comparing two directory trees recursively. We will ignore the `-a` option, which means treat all files as text, since `patch` and `diff` should only be used on text files anyway. Since we are just comparing two files, we do not need to use the `N` or `r` options to `diff`, but we could use them anyway as it will not make a difference. Compare `group` and `GROUP` using `diff`, and prepare a proper patch file.
5. Use `patch` to patch the original file, `/tmp/group`, so its contents now match those of the modified file, `/tmp/GROUP`. (You might try with the `--dry-run` option first!)
6. Finally, to prove that your original file is now patched to be the same one with all upper-case characters, use diff on those two files. The files should be the same and you will not get any output from diff.

Click [the link][lab2] to view a solution to the Lab exercise.


# Section 4: Backing Up and Compressing Data
## Backing Up Data
There are many ways you can back up data or even your entire system. Basic ways to do so include the use of simple copying with `cp` and use of the more robust `rsync`.

Both can be used to synchronize entire directory trees. However, `rsync` is more efficient, because it checks if the file being copied already exists. If the file exists and there is no change in size or modification time, `rsync` will avoid an unnecessary copy and save time. Furthermore, because `rsync` copies only the parts of files that have actually changed, it can be very fast.

`cp` can only copy files to and from destinations on the local machine (unless you are copying to or from a filesystem mounted using NFS), but `rsync` can also be used to copy files from one machine to another. Locations are designated in the `target:path` form, where `target` can be in the form of `[user@]host`. The `user@` part is optional and used if the remote user is different from the local user.

`rsync` is very efficient when recursively copying one directory tree to another, because only the differences are transmitted over the network. One often synchronizes the destination directory tree with the origin, using the `-r` option to recursively walk down the directory tree copying all files and directories below the one listed as the source.

## Using rsync
__rsync__ is a very powerful utility. For example, a very useful way to back up a project directory might be to use the following command:

`$ rsync -r project-X archive-machine:archives/project-X`

Note that rsync can be very destructive! Accidental misuse can do a lot of harm to data and programs, by inadvertently copying changes to where they are not wanted. Take care to specify the correct options and paths. It is highly recommended that you first test your `rsync` command using the `-dry-run` option to ensure that it provides the results that you want.

To use __rsync__ at the command prompt, type `rsync sourcefile destinationfile`, where either file can be on the local machine or on a networked machine.

The contents of `sourcefile` are copied to `destinationfile`.

## Compressing Data
File data is often compressed to save disk space and reduce the time it takes to transmit files over networks.

Linux uses a number of methods to perform this compression, including:

| Command | Usage |
|---------|-------|
| `gzip` | The most frequently used Linux compression utility |
| `bzip2` | Produces files significantly smaller than those produced by gzip |
| `xz` | The most space-efficient compression utility used in Linux |
| `zip` | Is often required to examine and decompress archives from other operating systems |

These techniques vary in the efficiency of the compression (how much space is saved) and in how long they take to compress; generally, the more efficient techniques take longer. Decompression time does not vary as much across different methods.

In addition, the `tar` utility is often used to group files in an __archive__ and then compress the whole archive at once.

## Compressing Data Using gzip
__gzip__ is the most often used Linux compression utility. It compresses very well and is very fast. The following table provides some usage examples:

| Command | Usage |
|---------|-------|
| `gzip *` | Compresses all files in the current directory; each file is compressed and renamed with a `.gz` extension. |
| `gzip -r projectX` | Compresses all files in the `projectX` directory, along with all files in all of the directories under `projectX`. |
| `gunzip foo` | De-compresses `foo` found in the file `foo.gz`. Under the hood, the `gunzip` command is actually the same as `gzip –d`. |

## Compressing Data Using bzip2
__bzip2__ has a syntax that is similar to gzip but it uses a different compression algorithm and produces significantly smaller files, at the price of taking a longer time to do its work. Thus, it is more likely to be used to compress larger files.

Examples of common usage are also similar to gzip:

| Command | Usage |
|---------|-------|
| `bzip2 *` | Compresses all of the files in the current directory and replaces each file with a file renamed with a `.bz2` extension. |
| `bunzip2 *.bz2` | Decompresses all of the files with an extension of .bz2 in the current directory. Under the hood, bunzip2 is the same as calling `bzip2 -d`. |

## Compressing Data Using xz
__xz__ is the most space efficient compression utility used in Linux and is now used by `www.kernel.org` to store archives of the Linux kernel. Once again, it trades a slower compression speed for an even higher compression ratio.

Some usage examples:

| Command | Usage |
|---------| ------|
| `xz *` | Compresses all of the files in the current directory and replaces each file with one with a `.xz` extension. |
| `xz foo` | Compresses the file foo into `foo.xz` using the default compression level (-6), and removes foo if compression succeeds. |
| `xz -dk bar.xz` | Decompresses `bar.xz` into bar and does not remove bar.xz even if decompression is successful. |
| `xz -dcf a.txt b.txt.xz > abcd.txt` | Decompresses a mix of compressed and uncompressed files to standard output, using a single command. |
| `xz -d *.xz` | Decompresses the files compressed using xz.|

Compressed files are stored with a `.xz` extension. 

## Handling Files Using zip
The `zip` program is not often used to compress files in Linux, but is often required to examine and decompress archives from other operating systems. It is only used in Linux when you get a zipped file from a Windows user. It is a legacy program.

| Command | Usage |
|--|--|
| `zip backup *` | Compresses all files in the current directory and places them in the file backup.zip. |
| `zip -r backup.zip ~` | Archives your login directory (~) and all files and directories under it in the file backup.zip. |
| `unzip backup.zip` | Extracts all files in the file backup.zip and places them in the current directory. |

## Archiving and Compressing Data Using tar
Historically, __tar__ stood for "tape archive" and was used to archive files to a magnetic tape. It allows you to create or extract files from an archive file, often called a __tarball__. At the same time, you can optionally compress while creating the archive, and decompress while extracting its contents.

Here are some examples of the use of `tar`:

| Command | Usage |
|---|---|
| `tar xvf mydir.tar` | Extract all the files in mydir.tar into the mydir directory |
| `tar zcvf mydir.tar.gz mydir` | Create the archive and compress with `gzip` |
| `tar jcvf mydir.tar.bz2 mydir` | Create the archive and compress with `bz2` |
| `tar Jcvf mydir.tar.xz mydir` | Create the archive and compress with `xz` |
| `tar xvf mydir.tar.gz` | Extract all the files in `mydir.tar.gz` into the mydir directory. Note you do not have to tell tar it is in gzip format. |

You can separate out the archiving and compression stages, as in:
```
$ tar mydir.tar mydir ; gzip mydir.tar
$ gunzip mydir.tar.gz ; tar xvf mydir.tar
```
but this is slower and wastes space by creating an unneeded intermediary `.tar` file.

## Disk-to-Disk Copying
The __dd__ program is very useful for making copies of `raw disk space`. For example, to back up your __Master Boot Record (MBR)__ (the first 512-byte sector on the disk that contains a table describing the partitions on that disk), you might type:

`dd if=/dev/sda of=sda.mbr bs=512 count=1`

To use `dd` to make a copy of one disk onto another, (WARNING!) deleting everything that previously existed on the second disk, type:

`dd if=/dev/sda of=/dev/sdb`

An exact copy of the first disk device is created on the second disk device.

Do not experiment with this command as written above, as it can erase a hard disk!

Exactly what the name `dd` stands for is an often-argued item. The words __data definition__ is the most popular theory and has roots in early __IBM__ history. Often, people joke that it means __disk destroyer__ and other variants such as __delete data__!

## Knowledge Check
1. While copying one directory to a similar directory on another system over the network, rsync copies:

        A. all files
        B. all subdirectories
        C. all files and subdirectories that have changed
        D. only the parts of all files and subdirectories that have changed 

        Ans: D
        Explanation
        While copying one directory to a similar directory on another system over the network, rsync copies only the parts of all files and subdirectories that have changed.

2. The command tar zcvf backup.tar.gz ~ will archive which of the following in the file backup.tar.gz?

        A. The user's home directory
        B. The user's entire home directory tree 
        C. The entire Hard Disk
        D. The entire partition the user's home directory resides in

        Ans: B
        Explanation
        The command `tar zcvf backup.tar.gz ~` will archive the user's entire home directory tree in the file `backup.tar.gz`.

3. Which of the following commands will compress all the files in some_dir, along with all of the files in all the directories under it?

        A. $ gzip *
        B. $ gzip -r some_dir 
        C. $ gzip -d some_dir
        D. $ gunzip some_dir

        Ans: B
        Explanation
        The $ gzip -r some_dir will compress all the files in some_dir, along with all of the files in all of the subdirectories under it.

4. The two commands gunzip foo and gzip -d foo do the same thing.

        Ans: True
        Explanation
        The two commands gunzip foo and gzip -d foo do the same thing; they decompress the contents of the file foo.

## Lab 3: Archiving (Backing Up) the Home Directory
Archiving (or backing up) your files from time to time is essential good hygiene. You might type a command and thereby unintentionally clobber files you need and did not mean to alter.

Furthermore, while your hardware may be deemed fairly reliable, all devices do fail in some fashion eventually (even if it is just an unexpected power failure). Often, this happens at the worst possible time. Periodically backing up files is a good habit to get into.

It is, of course, important to do backups to external systems through a network, or onto external storage, such as an external drive or USB stick. Here, we will be making a back up archive on the same system, which is very useful, but won’t help if the drive fails catastrophically, or your computer is stolen or the building gets zapped by an asteroid or a fire.

First, using `tar`, back up all files and subdirectories under your home directory. Place the resulting tarball file in the /tmp directory, giving it the name backup.tar .

Second, accomplish the same task with `gzip` compression using the `-z` option to tar, creating `/tmp/backup.tar.gz`.

Compare the size of the two files (with ls `-l` ).

For additional experience, make backups using the `-j` option using the `bzip2` compression, and `-J` option for using `xz` compression.

Click [the link][lab3] to view a solution to the Lab exercise.


# Summary
The key concepts we covered in this chapter are:

+ The filesystem tree starts at what is often called the __root__ directory (or __trunk__, or __/__).
+ The __Filesystem Hierarchy Standard (FHS)__ provides Linux developers and system administrators a standard directory structure for the filesystem.
+ Partitions help to segregate files according to usage, ownership, and type.
+ Filesystems can be __mounted__ anywhere on the main filesystem tree at a mount point. Automatic filesystem mounting can be set up by editing `/etc/fstab`.
+ __NFS (The Network Filesystem)__ is a useful method for sharing files and data through the network systems.
+ Filesystems like `/proc` are called pseudo filesystems because they exist only in memory.
+ `/root` (slash-root) is the home directory for the root user.
+ `/var` may be put in its own filesystem so that growth can be contained and not fatally affect the system.
+ `/boot` contains the basic files needed to boot the system.
+ `patch` is a very useful tool in Linux. Many modifications to source code and configuration files are distributed with patch files, as they contain the deltas or changes to go from an old version of a file to the new version of a file.
+ File extensions in Linux do not necessarily mean that a file is of a certain type.
+ `cp` is used to copy files on the local machine, while `rsync` can also be used to copy files from one machine to another, as well as synchronize contents.
+ `gzip`, `bzip2`, `xz` and `zip` are used to compress files.
+ `tar` allows you to create or extract files from an archive file, often called a __tarball__. You can optionally compress while creating the archive, and decompress while extracting its contents.
+ `dd`  can be used to make large exact copies, even of entire disk partitions, efficiently.


[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009500_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6c6a76e5e83450a2f75777a86ba8e790/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch08_screen_03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ac62a14ab6f4013601e09546d5a7e70c/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch08_screen05.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/90eea9eba0b63783a8bcf2b85ae8a9e3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch08_screen06.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/18cd65d8ee6e189efd405e7e3c890f2d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/dfmountdebian.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c9d06cf0b5114c7ff0553aae608e96bd/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/exportsnfs.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/80a14e19e05a9cfdc8b19f09d20e8e07/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/nfsclientubuntu.png
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0f4cc85473fc7a961b3bc98b87d33a24/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lsbin.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f60523278764a748d479ef923f75b0d7/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lssbin.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5851a953799d1db46c17d156b1cd23bc/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lsproc.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ee00318b4e056829ec5580f3f8c6ca10/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lsdev.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5fe4351bb47d35094accf1fc602ceb91/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Ch08_screen17.jpg
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5fe4351bb47d35094accf1fc602ceb91/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Ch08_screen17.jpg
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e134514444baf41b5ce0f1b6dbff8c53/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lsboot.png
[imge]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2f0c7f904c4caf99b69bda968386650d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Ch8_screen19.jpg
[imgf]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/33d173c484df38d28dcb85d2a49a010e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/diff3centos.png
[imgg]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6bb8e04e57d74c83cd0de7335128892d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/patchrhel.png
[imgh]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/257161c915cc7d71d00efa086067716d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/fileprogrhel.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-mount.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-diff.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-archive.html

[compf]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingdiff/index.html
[file]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingfile/index.html

