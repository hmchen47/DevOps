# Ch06 : Installing Linux Software

## Introduction

+ "package" file: typically Linux developers create their software w/ all the executable and data files bundled into the file
+ Typical Package Managers
    + Used for installing the kernel, or master program
    + __RPM__ (RedHat Package Manager) files:
        + Redhat, Centos and Fedora Linux software
        + Procedure for installing source RPMs involves recompiling source code to fit the needs of these kernel customizations
    + __DEB__ files: Debian and Ubuntu versions of Linux use the Debian Package format
    + __TAR__ packages: universal but need compile source code
    + __Perl programming language__
        + Often used by Linux software developers to create their programs
        + Many Linux distributions install Perl with only the most commonly used ones
        + Sometimes required to install additional prerequisite Perl modules prior to the installation of your packages

## Where to Get Commonly Used Packages

+ Packages on Your Installation CDs
+ Manually Downloaded Packages - Popular Package Download Sites

    | Distribution | Location |
    |--------------|----------|
    | Redhat | http://www.redhat.com/; http://www.rpmfind.net/ |
    | Fedora | ftp://download.fedora.redhat.com/pub/fedora/linux/core/; http://download.fedora.redhat.com/pub/fedora/linux/core/ http://www.rpmfind.net/ |
    | Debian | http://packages.debian.org; Ubuntu; http://packages.ubuntu.com |

+ Automated Package Download: `yum`, `apt`

## How to Download Software

+ Getting Software Using Web-Based FTP
+ Getting RPMs Using Command-Line Anonymous FTP

| Command | Description |
|---------|-------------|
| `binary` | Copy files in binary mode |
| `cd` | Change directory on the FTP server |
| `dir` | List the names of the files in the current remote directory |
| `exit` | Bye bye |
| `get` | Get a file from the FTP server |
| `lcd` | Change the directory on the local machine |
| `ls` | Same as dir |
| `mget` | Same as get, but you can use wildcards like "*" |
| `mput` | Same as put, but you can use wildcards like "*" |
| `passive` | Make the file transfer passive mode |
| `put` | Put a file from the local machine onto the FTP server |
| `pwd` | Give the directory name on the local machine |

+ Getting Software Using wget
    + used to download files quickly w/ know URL
    + e.g. `wget http://linux.stanford.edu/pub/mirrors/fedora/linux/core/2/i386/os/Fedora/RPMS/dhcp-3.0pl2-6.16.i386.rpm`

## Installing Software From RPM Files

### How To Install RPMs Manually

+ Using Downloaded Files
    + Download the RPMs
    + install w/ `rpm -Uvh`
+ Using CD-ROMs or DVDs
    1. Insert the CD-ROM, check the files in the /mnt/cdrom/Fedora/RPMS directory and then install the RPM.
        ```shell
        mount /mnt/cdrom
        cd /mnt/cdrom/Fedora/RPMS
        ls filename*
        rpm -Uvh filename.rpm
        ```
    2. When finished, eject the CD-ROM
        ```shell
        cd /tmp
        eject cdrom
        ```
+ Using ISO Files
    + similar to those used when installing from hard disk
    1. Downloaded the ISO file to the /tmp directory, mount the file, check the files in the /mnt/Fedora/RPMS directory and then install the RPM
        ```shell
        mount -o loop -t iso9660 file.iso /mnt
        cd /mnt/Fedora/RPMS
        ls filename*
        rpm -Uvh filename.rpm
        ```
    2. When finished, unmount the ISO file
        ```shell
        cd /tmp
        umount /mnt
        ```

### How to Install Source RPMs

+ Procedure
    + Download source RPM, usually w/ `.src.rpm`
    + Run the following commands as root: `rpmbuild --rebuild filename.src.rpm`
    + Install the compiled RPMs 

### RPM Installation Errors

+ Failed Dependencies
    + Install w/o dependencies: `--nodeps`
    + Install required dependencies
+ Signature Keys
    + Fedora digitally signs all its RPM files
    + best to import public encryption key beforehand
    + RPM installation program able to verify the validity of the RPM file
    + Usually done automatically in newer versions of Fedora: `/usr/share/rhn/RPM-GPG-KEY` & `/usr/share/rhn/RPM-GPG-KEY-fedora`


### How to List Installed RPMs

### Listing Files Associated with RPMs

+ Listing Files for Already Installed RPMs

+ Listing Files in RPM Files

+ Listing the RPM to Which a File Belongs

+ Uninstalling RPMs

+ Which RPMs Will Start Up At Boot Time?

### Automatic Updates with yum

+ Configuring yum

+ Configuring /etc/yum.repos.d Repository Files

+ How to Automate yum

+ Creating Your Own yum Server

+ How to Automate yum

+ Keeping Your System current with Yum

+ Example of a yum Package Installation

+ Remember The Following Yum Facts

## Installing Software From DEB Files

### How To Install DEBs Manually

+ Using Downloaded Files

+ Using CD-ROMs

### DEB Installation Errors

+ Failed Dependencies

### How to List Installed DEBs

+ Table ## -##  Column Formatting for the dpkg command

### Listing Files Associated with DEBs

+ Listing Files for Previously Installed DEBs

+ Listing Files in DEB Files

+ Listing the DEB Package to Which a File Belongs

### Uninstalling DEBs

### Which DEBs Will Start Up At Boot Time?

### Automatic DEB Updates with apt-get

+ Configuring APT

+ Keeping Your System current with APT

+ Example of an apt-get Package Installation

+ Remember The Following APT Facts

## Installing Software Using tar Files

## Installing Perl Modules

### Manual Installation of Perl Modules

### Automatic Installation of Perl Modules

### Updating Your Perl Modules

## Managing Daemons

### Daemon Management Command Summary

+ Reboot Persistent and Non-Persistent Commands

+ Starting Daemons

+ Stopping Daemons

+ Restarting Daemons

+ Daemon Status

### The chkconfig Command

+ A Simple chkconfig Exercise

+ Using chkconfig to Improve Security

+ Final Tips on chkconfig

### The sysv-rc-conf Command

+ Installing sysv-rc-conf

+ Listing the runlevels for Daemons

+ Setting the runlevels for Daemons
