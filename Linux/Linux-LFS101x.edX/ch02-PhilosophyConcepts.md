Introduction to Linux
=====================

Chapter 02: Linux Philosophy and Concepts
=========================================

Introduction/ Learning Objectives
---------------------------------
[video][video1]

# Learning Objectives
By the end of this chapter, you should be able to:

+ Discuss the history and philosophy of Linux.
+ Describe the Linux community.
+ Define the common terms associated with Linux.
+ Discuss the components of a Linux distribution.

Section 1: Linux History
------------------------
# Introduction
Linux is a free open source computer operating system, initially developed for Intel __x86-based__ personal computers. It has been subsequently ported to many other hardware platforms.

In this section, you will become familiar with how Linux evolved from a student project into a massive effort with an enormous impact on today's world.

# Linux History
Linus Torvalds was a student in Helsinki, Finland, in 1991, when he started a project: writing his own operating system __kernel__. He also collected together and/or developed the other essential ingredients required to construct an entire __operating system__ with his kernel at the center. Soon, this became known as the __Linux__ kernel. 

In 1992, Linux was re-licensed using the __General Public License (GPL)__ by __GNU__ (a project of the Free Software Foundation or FSF, which promotes freely available software), which made it possible to build a worldwide community of developers. By combining the kernel with other system components from the GNU project, numerous other developers created complete systems called __Linux Distributions__ in the mid-90’s.

# More About Linux History
The Linux distributions created in the mid-90s provided the basis for fully free computing and became a driving force in the open source software movement. In 1998, major companies like __IBM__ and __Oracle__ announced their support for the Linux platform and began major development efforts as well.

Today, Linux powers more than half of the servers on the Internet, the majority of smartphones (via the __Android__ system, which is built on top of Linux), and nearly all of the world’s most powerful supercomputers.

# Knowledge Check
When did Linus Torvalds start writing the Linux kernel?

    A. 1952
    B. 1991
    C. 2002
    D. 2010

    Ans: B
    Explanation
    Linus Torvalds started writing the Linux kernel as a hobby in Helsinki in 1991 and later became its chief designer.

Section 2: Linux Philosophy
---------------------------------
# Introduction
Every organization or project has a philosophy that works as a guide while framing its objectives and delineating its growth path. This section contains a description of the Linux philosophy and how this philosophy has impacted its development.

Linux is constantly enhanced and maintained by a network of developers from all over the world collaborating over the Internet, with Linus Torvalds at the head. Technical skill and a desire to contribute are the only qualifications for participating.

# Linux Philosophy
Linux borrows heavily from the __UNIX__ operating system because it was written to be a free and open source version of __UNIX__. Files are stored in a hierarchical filesystem, with the top node of the system being `root` or simply `"/"`. Whenever possible, Linux makes its components available via files or objects that look like files. Processes, devices, and network sockets are all represented by `file-like objects`, and can often be worked with using the same utilities used for regular files.

Linux is a fully __multitasking__ (i.e., multiple threads of execution are performed simultaneously), __multiuser__ operating system, with built-in networking and service processes known as __daemons__ in the __UNIX__ world.

[How Linux Is Built-video][video2]

# Knowledge Check
1. Drag the following statements associated with the Linux philosophy to its corresponding column. (True/False)

	A. Linux was written to be a free and open source version of UNIX.
	B. Linux makes its components available via its servers.
	C. Processes, devices, and network sockets are all represented by file-like objects, and often can be worked with using the same utilities used for regular files.
	D. In Linux all files are stored in one united directory tree, starting at "/", the system's root directory.

	Ans: A: True; B: False; C: True; D: True

2. What are the qualifications required for participating in Linux kernel development?

	A. Technical skills
	B. A desire to contribute
	C. Citizen of the U.S.
	D. University degree in computer science

	Ans: A, B
	Explanation
	Linux is developed by a loose confederation of developers from all over the world, collaborating over the Internet, with Linus Torvalds at the head. Technical skill and a desire to contribute are the only qualifications for participating.

Section 3: Linux Community
---------------------------------
# Introduction to the Community
Suppose that, as part of your job, you need to configure a Linux file server, and you run into some difficulties. If you are not able to figure out the answer yourself or get help from a co-worker, the Linux community might just save the day! There are many ways to engage with the Linux community: you can post queries on relevant discussion forums, subscribe to discussion threads, and even join local Linux groups that meet in your area.

# Linux Community
[video][video3]

# More About The Linux Community
The Linux community is a far-reaching ecosystem consisting of developers, system administrators, users and vendors, who use many different forums to connect with one another. Among the most popular are:

+ Linux User Groups (both local and online)
+ Internet Relay Chat (__IRC__) software (such as __Pidgin__ and __XChat__)
+ Online communities and discussion boards
+ Newsgroups and mailing lists, including the __Linux Kernel Mailing List__
+ Community events (such as __Open Source Summits__ and __Embedded Linux Conferences__)

One of the most powerful online user communities is [linux.com][linuxcom]. This site is hosted by __The Linux Foundation__ and serves over one million unique visitors every month. It has active sections on:

+ News
+ Community discussion threads
+ Free tutorials and user tips.

We will refer several times in this course to relevant articles or tutorials on this site.

# Knowledge Check
Which of the following communication channels does the Linux community use to communicate?

A. cnn.com
B. IRC Channels
C. Mailing Lists
D. Community Events

Ans: B, C, D
Explanation
The Linux community consists of vendors, developers, and active users. They communicate via Internet Relay Chat (IRC) channels, mailing lists, community events and other methods.


Section 4: Linux Terminology
---------------------------------
# Introduction
When you start exploring Linux, you will soon come across some unfamiliar terms, like distribution, boot loader, desktop environment, etc. So, before we proceed further, let's stop and take a look at some basic terminology used in Linux to help you get up to speed.

# Linux Terminology
[vidoe][video4]

Termonologies:

+ kernel: glue between hardware and applications, e.g. Linux kernel
+ distribution (distro): collection of software making up a Linux-based operating system, e.g., RHEL, Fedora, Ubuntu, and Gentoo
+ boot loader: program that boots the operating system, e.g. GRUB and ISOLINUX
+ service: program that runs as a background perocess, e.g., httpd, ftsd, ntpd, ftpd, and named
+ filesystem: mtethod for storing and organizing files, e.g., ext3, ext4, FAT, XFS, BTFS, and Btrfs
+ X Window System: graphical subsystem on nearly all Linux systems
    + GUI: Desktop - KDE, XFCE; Window manager; X Window System/X11
    + Console: CLI/shell; kernel; hardware
+ Desktop environment: graphical user interface on top of the operating system, e.g., GNOME, KDE, Xfce, and Fluxbox
+ Command line: interface for typing commands on top of the operating system
+ shell: command line interpreter that interprets the command line input and instructs the OS to perform any necessary tasks and commands, e.g., bash, tcsh, csh

# Knowledge Check
1. What is a kernel?

	A. The glue between hardware and applications.
	B. A collection of software making up a Linux-based Operating System.
	C. A program that runs as a background process.
	D. A graphical subsystem on nearly all Linux systems.

	Ans: A
	Explanation
	A __kernel__ is considered the brain of the Linux Operating System. It controls the hardware and makes the hardware interact with the applications. An example of a kernel is the __Linux kernel__.

2. What is a desktop environment?

	A. A collection of software making up a Linux-based Operating System.
	B. A program that runs as a background process.
	C. A graphical subsystem on nearly all Linux systems.
	D. A graphical user interface on top of the Operating System.

	Ans: D
	Explanation
	A __desktop environment__ is a graphical user interface on top of the Operating System. __GNOME__, __KDE__, __Xfce__, and __Fluxbox__ are some examples of the desktop environment.


3. What is a command line?

	A. A collection of software making up a Linux-based Operating system.
	B. A program that runs as a background process.
	C. An interface for typing commands for the Operating System to execute. 
	D. A list of commands requested to be run in the order presented.

	Ans: C
	Explanation
	A __command line__ is an interface for typing commands for the Operating System to execute.


Section 5: Linux Distributions
---------------------------------
# Introduction
Suppose you have been assigned to a project building a product for a Linux platform. Project requirements include making sure the project works properly on the most widely used Linux distributions. To accomplish this, you need to learn about the different components, services, and configurations associated with each distribution. We are about to look at how you would go about doing exactly that.

# Linux Distributions
![Linus kernel][kernel]

So, what is a Linux distribution and how does it relate to the Linux kernel?

As illustrated above, the Linux kernel is the core of a computer operating system. A full Linux distribution consists of the kernel plus a number of other software tools for file-related operations, user management, and software package management. Each of these tools provides a small part of the complete system. Each tool is often its own separate project, with its own developers working to perfect that piece of the system.

As mentioned earlier, the current Linux kernel, along with past Linux kernels (as well as earlier release versions) can be found at the www.kernel.org web site. The various Linux distributions may be based on different kernel versions.  For example, the very popular __RHEL 7__ distribution is based on the `3.10` version of the Linux kernel, which is not new , but is extremely stable. Other distributions may move more quickly in adopting the latest kernel releases. It is important to note that the kernel is not an all or nothing proposition, for example, __RHEL 7__ and __CentOS 7__ have incorporated many of the more recent kernel improvements into their version of `3.10`, as have __Ubuntu 16.04__, and __openSUSE-Leap-42.2__ and __SLES-12 SP2__ in their respective versions of the `4.4` kernel.

Examples of other essential tools and ingredients provided by distributions include the __C/C++__ compiler, the __gdb__ debugger, the core system libraries applications need to link with in order to run, the low-level interface for drawing graphics on the screen, as well as the higher-level desktop environment, and the system for installing and updating the various components, including the kernel itself.

# Services Associated with Distributions
![Services][srv]

The vast variety of Linux distributions are designed to cater to many different audiences and organizations, according to their specific needs and tastes. However, large organizations, such as companies and governmental institutions and other entities, tend to choose the major commercially-supported distributions from __Red Hat, SUSE__, and __Canonical (Ubuntu)__.

__CentOS__ is a popular free alternative to __Red Hat Enterprise Linux (RHEL)__ and is often used by organizations that are comfortable operating without paid technical support. __Ubuntu__ and __Fedora__ are popular in the educational realm. __Scientific Linux__ is favored by the scientific research community for its compatibility with scientific and mathematical software packages. Both __CentOS__ and __Scientific Linux__ are binary-compatible with __RHEL__; i.e., binary software packages in most cases will install properly across the distributions.

Many commercial distributors, including __Red Hat, Ubuntu, SUSE__, and __Oracle__, provide long term fee-based support for their distributions, as well as hardware and software certification. All major distributors provide update services for keeping your system primed with the latest security and bug fixes, and performance enhancements, as well as provide online support resources.

# Knowledge Check
1. In addition to the kernel, what are some of the purposes of the other software tools required for developing a full Linux distribution?
    A. Performing file-related operations 
    B. Catering to different audiences
    C. Maintaining user management 
    D. Taking care of software package management 

    Ans: A, C, D
    Explanation
    A full Linux distribution consists of the kernel plus a number of other software tools, including those for file-related operations, user management, and software package management.

2. Which of the following are binary-compatible Linux distributions which are free alternatives to Red Hat Enterprise Linux (RHEL)? Choose all that apply.

    A. CentOS 
    B. Ubuntu
    C. Scientific Linux 
    D. openSUSE

    Ans: A, C
    Explanation
    __CentOS__ and __Scientific Linux__ are both binary-compatible Linux distributions which are free alternatives to __Red Hat Enterprise Linux (RHEL)__.


Summary
-------
You have completed this chapter. Let’s summarize the key concepts covered:+ 

+ Linux borrows heavily from the __UNIX__ operating system, with which its creators were well versed. 
+ Linux accesses many features and services through `files` and `file-like objects`.
+ Linux is a fully `multi-tasking, multi-user` operating system, with built-in networking and service processes known as `daemons`.
+ Linux is developed by a loose confederation of developers from all over the world, collaborating over the Internet, with Linus Torvalds at the head. _Technical skill_ and a _desire to contribute_ are the only qualifications for participating.
+ The Linux community is a far reaching ecosystem of developers, vendors, and users that supports and advances the Linux operating system.
+ Some of the common terms used in Linux are: Kernel, Distribution, Boot Loader, Service, Filesystem, X Window system, Desktop Environment, and Command Line.
+ A full Linux distribution consists of the kernel plus a number of other software tools for file-related operations, user management, and software package management.



[video1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003600_DTH.mp4
[video2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008200_DTH.mp4
[vidoe3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009900_DTH.mp4
[video4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006600_DTH.mp4
[linuxcom]: http://www.linux.com/
[kernel]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dcb43b188ca10a2337434952480f27b8/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch02_screen_23.jpg
[srv]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/85a0445af315a7fb90444a2d3cd0e608/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch02_screen_24.jpg