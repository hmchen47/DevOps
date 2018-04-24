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
        umount /mnt/cdrom
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


###  How to List Installed RPMs

+ List installed RPMs: `rpm -q [pkg]`
+ List all the files associated with an installed RPM: `rpm -ql <pkg>`
+ list all the files in an RPM archive: `rpm -qpl <pkg>`
+ Listing the RPM to Which a File Belongs: `rpm -qf <filename>`, e.g., `rpm -qf /etc/my.cnf`
+ Uninstalling RPMs: `rpm -e <pkg>`
+ Which RPMs Will Start Up At Boot Time?: `chkconfig --list`

### Automatic Updates with yum

+ `yum` automatic RPM update program comes as a standard feature of Fedora Core
+ Features:
    + configure the URLs of download sites containing the RPM repositories
    + multiple attempts to download RPMs
    + automatically updating and supporting RPMs
+ Configuring `yum`: server URLs are stored in the [main] section of the `/etc/yum.conf` file
+ Configuring `/etc/yum.repos.d` Repository Files
    + Containing files where to find the latest Linux updates
        ```script
        [repositoryid]
        name=Some name for this repository
        baseurl=url://path/to/repository/
        ```
        +  `[repositoryid]`:` an identifier that is unique to all files in the directory
        + the `[repositoryid]` in the `.repo` file unique to all other files
        + [Web site](http://fedora.redhat.com/download/mirrors.html) to get a listing of alternative download sites
        + `baseurl` points to a URL with a `/repodata` sub-directory containing files nd instructions for `yum` to use in doing its updates
    + `yum` accepts the use of variables in the configuration file
        + `$releasever` variable: the current version of Fedora Core running on server
        + `$basearch` variable maps to the base architecture of the server automatically
    + Best to select yum update sites that use `HTTP` instead of `FTP`
        + `FTP` firewall rules are more difficult to implement than `HTTP`
        + Multiple baseurl statements in each section then yum may act strangely, frequently only selecting the last one in the list
    + Checksum 
        + `yum` utility configured to match the downloaded RPMs against checksum files 
        + achieved by `gpgcheck` variable in the `.repo` files
        ```script
        gpgcheck=1
        gpgkey=http://URL/example.key
        ```
+ How to Automate `yum`
    + Older versions
        + run in the background as a daemon
        + used a unified `yum.conf` file for all its configuration data
    + Newer versions
        + use the `yum-updatesd` daemon
        + uses the /etc/yum/yum-updatesd.conf configuration file 
            + update frequency
            + types of files to be downloaded
            + whether they should be automatically installed
    + Procedure:
        1. Install `yum-updatesd` package: `yum –y install yum-updatesd`
        2. Get `yum` configured to start at boot: 
            + Systems using `sysvinit`: `chkconfig yum-updatesd on`
            + Systems using `systemd`: `systemctl enable yum-updatesd.service`
        3. instruct the /etc/init.d yum script to start/stop `yum` after booting
            + Systems using `sysvinit`: `service yum-updatesd start` & `service yum-updatesd stop`
            + Systems using `systemd`: `systemctl start yum-updatesd.service` & `systemctl stop yum-updatesd.service`
    + Ensure update w/ `yum-updatesd` daemon in `/etc/yum/yum-updatesd.conf`: 
        ```script
        [main]
        do_update = yes
        ```
### Creating Your Own yum Server

+ Requriements:
    + small business: five to six gigabytes of free disk space per distribution
    + Large enterprise: twenty-five megabytes in size
    + Network load: minimal on average with an update once or twice a week per server
+ Server farms: a more robust system
+ `yum` clients accessing the `yum` server w/ FTP or HTTP requests

### How to Automate yum Manually

+ Procedure to manually configure:
    1. Get yum configured to start at boot: `chkconfig yum-updatesd on` & `chkconfig yum on`
    2. instruct the `/etc/init.d` `yum` script to start/stop yum after booting:
        ```script
        service yum-updatesd start
        service yum-updatesd stop

        service yum start
        service yum stop
        ```
+ Keeping Your System current with Yum: `yum update`
+ Remember The Following Yum Facts
    + Updates using TCP port 80 for `http://` update URLs and uses passive FTP for `ftp://` update URLs in `/etc/yum.conf`
    + Details on configuring yum: `man yum.conf`
    + Run automatically each day w/ cron file in `/etc/cron.daily/`
    + Don't limit yourself to the default `yum.conf` URLs --> overloaded

## Installing Software From DEB Files

+ How To Install DEBs Manually
    + Using Downloaded Files: `dpkg --install <pkg>`
    + Using CD-ROMs
        ``` shell
        # mount & install 
        mount /media/cdrom -o unhide
        cd /media/cdrom
        dpkg --install ndiswrapper-utils_1.8-ubuntu2_i386.deb 

        # unmount 
        cd /tmp
        umount /media/cdrom
        eject cdrom
        ```
+ DEB Installation Errors: Failed Dependencies

+ How to List Installed DEBs: `dpkg --list`

    | Desired State (Col. 1) | Current State (Col. 2) | Error State (Col. 3) | Description |
    |------------------------|------------------------|----------------------|-------------|
    | `u` |  |  | __Unknown__: The package has never been installed |
    | `i` |  |  | __Installed__: A privileged user has requested the installation of the package |
    | `r` |  |  | __Remove__: A privileged user has requested the removal of the package. Configuration files for the package most likely remain. |
    | `p` |  |  | __Purge__: A previously installed package has been removed. Configuration files for the package have probably been removed. |
    | `h` |  |  | __Hold__: A privileged user has requested that the package remain at its current version with no automatic upgrades. |
    |  | `n` |  | __Not Installed__: The package is not installed |
    |  | `i` |  | __Installed__: The package is installed |
    |  | `c` |  | __Configuration Files Exist__: Package was installed, but the configuration files exist. |
    |  | `u` |  | __Unpacked__: Files have been unpacked, but not installed |
    |  | `f` |  | __Failed__: Configuration of the package has failed. |
    |  | `h` |  | __Halt__: The package installation failed to complete |
    |  |  | `h` | __Enforced Hold__: Package upgrade is on hold because another dependent package with a user defined hold requires this package to remain not upgraded. |
    |  |  | `r` | __Reinstallation__: The package is broken and requires a reinstallation. |
    |  |  | `x` | The package is both broken and on enforced hold. |

+ Listing Files Associated with DEBs
    + Listing Files for Previously Installed DEBs: `dpkg --listfiles <pkg>`
    + Listing Files in DEB Files: `dpkg --contents <pkg>`
    + Listing the DEB Package to Which a File Belongs: `dpkg --search <file>`

+ Uninstalling DEBs: `dpkg --remove <pkg>`
+ Which DEBs Will Start Up At Boot Time?: `update-rc.d`

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
