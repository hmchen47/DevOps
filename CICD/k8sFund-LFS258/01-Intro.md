Course Introduction
===================

## 1.1 Before You Begin
Course navigation
+ next, prev page: righ arrow, left arrow
+ exit: top-right x button
+ home: first page of the course
+ drop-down menu: table of contents
+ progrss: bottonm left bar
+ hyperlink
+ video & captioon: start automatically

Note: auto logout for 30 mins

## 1.2 Cour Introduxtion

## 1.3 Course Objectives
Objectives:
+ history and evolution
+ high-level architecture nad components
+ API, most important rexources that make the API and how to use them
+ how to deploy and ,anahe an app
+ some upcoming features to boost productivity

## 1.4 Course Formatting
Color ciding and formats:
+ __Bold__: names of programms and services (or use for emphasis)
+ Light Blue: designates hyperlinks
+ Dark blue: text typed at the command lin, system output at the command line (markdown using `text` instead)

## 1.5 Grading & Certifcate of Completion
End of course: two buttons __COMPLETED__ and __NOT COMPLETE__
+ Complete: mark course as complete -> download certifcate w/ "The Linux Fundation website > Training > My Portal > Training Classes > Prevoupus Classes > Kubernetes Fundamentls > Download Certificate"
+ Not Complete: beginning of the course

## 1.6 Course Timing
+ self-paced: no fixed schedule
+ access: unlimited for 12 mons from the date registered, even completion

## 1.7 Exercises-Labs Environment
Labs written on Goofle Compute Engine (GCE) nodes but vendor-agnosic, so they could run on AWS, local hardware, or inside of VMs
+ each node with 2 CPUs and 7.5G of memeory, running on Ubuntu 16.04
+ [GCE account info]( https://cloud.google.com/compute/docs/quickstart-linux)
+ [AWS account info](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/)
+ VMs: KVM, VirtualBox, VMWare
+ bare-metal w/ Internet connection

Emphasis on learning-by-doing
+ Instructor led classes: around 50/50 balance between lecture and discussion, and working on labs exercises, or homeworks
+ self-paced: make sure enough time for labs
+ Download all exercise and solutions with "DOCUMENT" [botton](https://lms.quickstart.com/custom/858487/LFS258-Labs_V_2018-02-15.pdf) below

Knowledge Check: designed to help better comprehend the course content and reinforce what have learned

Labs and knowledge check questions are not graded and final exam not required to comple the course

## 1.8 Course Resources
Any changes before update:
+ [link](https://training.linuxfoundation.org/cm/LFS258/)
+ User ID: LFtraining passwd: Penguin2014

## 1.9 Discussion Board Guidelines
Discussion Board on linux.com, [LFS258 Discussion Board](https://www.linux.com/forums/lfs258-class-forum)
+ introduce self to peers on this course
+ discuss concepts, tools, and technologies, or course material
+ course content questions
+ share resources and ideas

## 1.10 Support
Issues on username and password: [link](https://identity.linuxfoundation.org/)

Assistance via email training@linuxfoundation.org w/ LFID username and description of concern

## 1.11 Course Audience and Requirements
LFS258: Kubernetes Fundamentals
+ good understanding Linux
+ familiar with command line
+ familiar with package manager
+ familiar with Git and GitHub
+ access to Linux server or desktop
+ VirtualBox on local machine or access to a public cloud

## 1.12 Software Environment
Main distributions of Linux:
+ Red Hat/Fedora
+ Open-SUSE/SUSE
+ Debian

## 1.13 Which Distribution to Choose?
Questions to choose neew distribution:
+ Has your employer already standarized?
+ Do you want to learn more?
+ Do you wan tot certify?

Technical differences mainly about package management systems, software versions, and file locations

## 1.14 Red Hat/Fedora Family
+ The community distribution forms the basis of Red Hats Enterprise Linux, CentoS, Scientific Linux and Oracle Linux
+ Fedora containing more software than RHEL
+ new version every 6 months or so
+ RHEL 7.x or CentOS 7 for latest version
+ Support x86, x86-64, Itanium, PowerPC, and IBM System Z
+ RPM-based, using yum to install and update
+ Long release cycle, target enterprise server environments
+ Upstream for CentOS, Scientific Linux, and Oracle Linux
+ CentOS used for demos and labs w/o cost

## 1.15 OpenSUSE Family
+ OpenSUSE ~ SUSE Linux Enterprose Server
+ difficult to obtain free SUSE Linux Enterprise Server
+ Course material based on the latest release of OpenSUSE
+ RPM-based, uses zyper to install and update
+ YaST available for admin purpose
+ Support x86 and x86-64
+ Upstream for SUSE Linux Enterprise Server (SLES)
+ OpenSUSE used for demos and labs at no cost

## 1.16 Debian Family
+ Upstream for several distros, including Ubuntu, Linux Mint, and others
+ Pure open source project
+ Provide the largest and most complete software repo
+ Ubuntu - compromise between LTS and ease of use
+ Commonly used on both servers and desktops
+ DPKG-based, use apt-get and frontends for installing and updating
+ Course material based on latest relase of Ubuntu
+ Support x-86 and x86-64
+ Ubuntu used for demos and labs at no cost

## 1.17 New Distribution Similarities
Trends to reduce some of the differences between them
+ __`systemd`__: 
    + system startup and service management
    + used by the most common distributions, replacing the `SysVinit` and `Upstart` packages
    + replae `service` and `chkconfig`
+ __`journald`__
    + manage system log
    + a `systemd` service that collects and stores logging data
    + creates and maintains structured, indexed journals based on loggin info received from a variety of sources
    + depending on distribution, text-based system log may be replaced
+ __`firewalld`__
    + firewall management daemon
    + provide a dynamically managed firewall w/ support for network/firewall zones to define the trust level of network connections
    + support for IPv4, IPv6 firewall setting and for Ethernet bridges
    + replace `iptable` configuration
+ __`ip`__
    + network display and configuration tool
    + part of the net-tools package
    + designed to be a replacement for the `ipconfig` command
    + show or manipulate routing, network devices, routing info and tunnels

Doc reference to tanslate older commands to `systemd` counterpart
+ [SysVinit to Systemd Cheatsheet](https://fedoraproject.org/wiki/SysVinit_to_Systemd_Cheatsheet)
+ [Debian `systemd` CheatSheet](https://wiki.debian.org/systemd/CheatSheet)
+ [OpenSUSE Services](https://en.opensuse.org/openSUSE:Cheat_sheet_13.1#Services)

## 1.18 AWS Free Tier
[Instruction for AWS Free Tier Account and Usage](https://training.linuxfoundation.org/cm/prep/aws.pdf)

## 1.19 Meet Your Instructor: Tim Serewicz
20 more years if experience working with latest technologies

## 1.20 Meet Your Instructor: Sebastien Goasguen
Senior Director of Cloud Technologies at Bitnami; Author of 'Docker Cookbook'

## 1.21 A Word from Tim Serewixz
[video](https://lms.quickstart.com/custom/858487/media/Course%20Introduction.mp4)