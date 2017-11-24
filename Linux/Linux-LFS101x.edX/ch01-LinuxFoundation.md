Introduction to Linux
=====================

Chapter 01: The Linux Foundation
--------------------------------

# Introduction
[video][video1]

## The Linux Foundation
[video][video2]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Discuss the role of The Linux Foundation.
+ Appreciate the learning opportunities provided by The Linux Foundation's training program.
+ Describe the software environment required for this course.
+ Describe the three major Linux distribution families.

# Section 1: The Linux Foundation
## About The Linux Foundation
Since its inception in 1991, Linux has grown to become a major force in computing - powering everything from the New York Stock Exchange, to mobile phones, supercomputers, and consumer devices.

The Linux Foundation partners with the world's leading developers and companies to solve the hardest technology problems and accelerate open technology development and commercial adoption. The Linux Foundation makes it its mission to provide experience and expertise to any initiative working to solve complex problems through open source collaboration, providing the tools to scale open source projects: security best practices, governance, operations and ecosystem development, training and certification, licensing, and promotion.

Linux is the world's largest and most pervasive open source software project in history. The Linux Foundation is home to Linux creator Linus Torvalds and lead maintainer Greg Kroah-Hartman, and provides a neutral home where Linux kernel development can be protected and accelerated for years to come. The success of Linux has catalyzed growth in the open source community, demonstrating the commercial efficacy of open source and inspiring countless new projects across all industries and levels of the technology stack.

The Linux Foundation's work today extends far beyond Linux, fostering innovation at every layer of the software stack. The Linux Foundation is the umbrella organization for many critical open source projects that power corporations today, spanning all industry sectors:

+ Networking: [OpenDaylight][OpenDaylight], [OPNFV][OPNFV]
+ Embedded: [Dronecode][Dronecode]
+ Web tools: [JS Foundation[JSFoundation], [Node.js][Node.js]
+ Cloud computing: [Cloud Foundry][CF], [Cloud Native Computing Foundation][CNCF], [Open Container Initiative][OCI]
+ Automotive: [Automotive Grade Linux][AGL]
+ Security: [The Core Infrastructure Initiative][CII]
+ Blockchain: [Hyperledger][HL]
+ And many more.

To learn more about The Linux Foundation, [click here][LF].

## The Linux Foundation Events
The Linux Foundation hosts conferences and other events throughout the world which bring community members together in person. These events: 

+ Provide an open forum for development of the next kernel (the actual operating system) release.
+ Bring together developers and system administrators to solve problems in a real-time environment.
+ Host workgroups and community groups for active discussions.
+ Connect end users, system administrators, and kernel developers in order to grow Linux use in the enterprise.
+ Encourage collaboration among the entire community.
+ Provide an atmosphere that is unmatched in its ability to further the platform.

 view a [video][video3] on the events organized by The Linux Foundation.

## Knowledge Check
What are the objectives of The Linux Foundation?

    A. To promote Linux and provide neutral collaboration and education.
    B. To improve Linux as a technical platform.
    C. To sponsor the work of Linus Torvalds.
    D. To manage Linux and UNIX servers on a commercial basis.

    Ans: A, B, C
    Explanation
    The Linux Foundation aims to promote Linux, provide neutral collaboration and education, improve Linux as a technical platform, and protect and support Linux development. It sponsors the work of Linus Torvalds.

# Section 2: The Linux Foundation Training
## The Linux Foundation Training
Although we believe in individual initiative and creativity, learning Linux need not be intimidating. You can leverage the power of collaboration to jump start your learning. Our classes build the critical skills that individuals and organizations need to get the most out of Linux and continue with self-directed learning.

## Training That Builds Skills
The Linux Foundation training is for the community and is designed by members of the community. The System Administration courses focus on Enterprise Linux environments and target system administrators, technical support, and architects. The Developer courses feature instructors and content straight from the leaders of the Linux developer community.

The Linux Foundation training is distribution-flexible, technically advanced, and created with the actual leaders of the Linux development community themselves. Most courses are more than 50% focused on hands-on labs and activities to build real world skills.

[video][video4]

## Copyright
The Linux Foundation has a copyright on all the materials in this course.

All Linux Foundation training, including all material provided herein is supplied without any guarantees from The Linux Foundation. The Linux Foundation assumes no liability for damages or legal action arising from the use or misuse of contents or details contained herein.

If you believe The Linux Foundation materials are being used, copied, or otherwise improperly distributed, please email training@linuxfoundation.org.

# Section 3: Course Linux Requirements
## Course Software Requirements
In order to fully benefit from this course, you will need to have at least one __Linux distribution__ installed (if you are not already familiar with the term distribution, as it relates to Linux, you soon will be!).

On the next screen, you will learn some more details about the many available __Linux__ distributions and the __families__ they can be considered to belong to. Because there are literally hundreds of distributions, we have not covered them all in this course. Instead, we have decided to focus on the three major distribution families, and we have chosen one specific distribution from within each family to use for all illustrations, examples, and exercises. This is not meant to suggest that we endorse these specific distributions; they were simply chosen because they are fairly widely used and each is broadly representative of its respective family.

The families and representative distributions we are using are: 

+ Debian Family Systems (such as Ubuntu)
+ SUSE Family Systems (such as openSUSE)
+ Fedora Family Systems (such as CentOS)

## Focus on Three Major Linux Distribution Families
![LinuxDistFamilies][LunixDistFam]

In the next chapter you will learn about the components that make up a Linux distribution. For now, what you need to know is that this course focuses on the three major Linux distribution families that currently exist. However, as long as there are talented contributors, the families of distributions and the distributions within these families will continue to change and grow. People see a need and develop special configurations and utilities to respond to that need. Sometimes that effort creates a whole new distribution of Linux. Sometimes, that effort will leverage an existing distribution to expand the members of an existing family. For a rather long list of available distributions, see [https://lwn.net/Distributions/](https://lwn.net/Distributions/)

## The Fedora Family
__Fedora__ is the community distribution that forms the basis of __Red Hat Enterprise Linux (RHEL), CentOS, Scientific Linux, and Oracle Linux__. __Fedora__ contains significantly more software than __Red Hat’s__ enterprise version. One reason for this is that a diverse community is involved in building __Fedora__, with many contributors who do not work for __Red Hat__. Furthermore, it is used as a testing platform for future __RHEL__ releases.

In this course, __CentOS__ is used for activities, demos, and labs because it is available at no cost to the end user and has a much longer release cycle than __Fedora__ (which releases a new version every six months or so).

For this reason, we have standardized the __Fedora__ part of this course material on __CentOS 7__. The basic version of __CentOS__ is also virtually identical to __RHEL__, the most popular Linux distribution in enterprise environments.

## Key Facts About the Fedora Family
Some of the key facts about the Fedora distribution family are:

+ The __Fedora__ family is upstream for __CentOS, RHEL, and Oracle Linux__.
+ Kernel version 3.10 is used in __RHEL/CentOS 7__.
+ It supports hardware platforms such as x86, x86-64, Itanium, PowerPC, and IBM System z.
+ It uses the __RPM__-based __yum__ package manager (we cover it in more detail later) to install, update, and remove packages in the system.
+ __RHEL__ is widely used by enterprises which host their own systems.

## The SUSE Family
The relationship between __SUSE__, __SUSE Linux Enterprise Server (SLES)__, and __openSUSE__ is similar to the one described between __Fedora, Red Hat Enterprise Linux__, and __CentOS__. In this case, we decided to use __openSUSE-Leap-42.2__ as the reference distribution for the SUSE family, as it is available to end users at no cost. Because the two products are extremely similar, the material that covers __openSUSE__ can typically be applied to __SLES__ with few problems.

## Key Facts About the SUSE Family
Some of the key facts about the SUSE family are listed below:

+ __SUSE Linux Enterprise Server (SLES)__ is upstream for __openSUSE__.
+ Kernel version 4.4 is used in __openSUSE-Leap-42.2__.
+ It uses the __RPM__-based __zypper__ package manager (we cover it in more detail later) to install, update, and remove packages in the system.
+ It includes the __YaST__ (Yet Another Setup Tool) application for system administration purposes.
+ __SLES__ is widely used in retail and other sectors.

# The Debian Family
The __Debian__ distribution is upstream for several other distributions, including __Ubuntu__. In turn, __Ubuntu__ is upstream for __Linux Mint__ and a number of other distributions. It is commonly used on both servers and desktop computers. __Debian__ is a pure open source project and has a strong focus on stability.

__Debian__ provides by far the largest and most complete software repository to its users of any Linux distribution.

__Ubuntu__ aims at providing a good compromise between long term stability and ease of use. Since __Ubuntu__ gets most of its packages from __Debian__’s stable branch, __Ubuntu__ also has access to a very large software repository. For those reasons, we will use __Ubuntu 16.04 LTS__ (Long Term Support) as the reference __Debian__ family distribution for this course. Ubuntu is a registered trademark of __Canonical Ltd.__ and is used throughout this course with their permission.

## Key Facts About the Debian Family
Some key facts about the Debian family are listed below:

+ The __Debian__ family is upstream for __Ubuntu__, and __Ubuntu__ is upstream for __Linux Mint__ and others.
+ Kernel version 4.4 is used in __Ubuntu 16.04 LTS__.
+ It uses the __DPKG__-based __APTv__ package manager (using __apt-get__, __apt-cache__ etc. which we cover in more detail later) to install, update, and remove packages in the system.
+ __Ubuntu__ has been widely used for cloud deployments.
+ While __Ubuntu__ is built on top of Debian and is __GNOME__-based under the hood, it uses the Unity graphical interface and differs quite a bit visually from the interface on standard Debian, as well as other distributions.

## More About the Software Environment
The material produced by The Linux Foundation is __distribution-flexible__. This means that technical explanations, labs, and procedures should work on almost all most modern distributions. While choosing between available Linux systems, you will notice that the technical differences are mainly about package management systems, software versions, and file locations. Once you get a grasp of those differences, it becomes relatively painless to switch from one Linux distribution to another.

The desktop environment used for this course is __GNOME__. As we will note in Chapter 4, there are different environments, but we selected __GNOME__ as it is the most widely used

## Knowledge Check
The three distribution families (Fedora, SUSE, and Debian) we are using are upstream for a number of Linux distributions. Some distributions are listed below.

    `Centos`,  `Linux Mint`,  'SLES`,  `Oracle Linux`, `Ubuntu`
    
    ![Linux Distribution Drag & Drop][LinuxDistDD]

# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ The Linux Foundation is the umbrella organization for many critical open source projects that power corporations today, spanning all industry sectors. Its work today extends far beyond Linux, fostering innovation at every layer of the software stack.
+ The Linux Foundation training is for the community and by the community. Linux training is distribution-flexible, technically advanced, and created with the leaders of the Linux development community.
+ There are three major distribution families within Linux: __Fedora__, __SUSE__ and __Debian__. In this course, we will work with representative members of all of these families throughout.


[LF]: https://www.linuxfoundation.org/
[LinuxDistFam]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7175fc9c8300a1e9937054f0debe55f6/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chapter01_screen18.jpg
[LinuxDistDD]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ce902e4a060199a9fd62587d89b81768/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/Drag_and_Drop_Background.png
[OpenDaylight]: https://www.opendaylight.org/
[OPNFV]: https://www.opnfv.org/
[Dronecode]: https://www.dronecode.org/
[JSFoundation]: https://js.foundation/
[Node.js]: https://nodejs.org/en/
[CF]: https://www.cloudfoundry.org/
[CNCF]: https://cncf.io/
[OCI]: https://www.opencontainers.org/
[AGL]: https://www.automotivelinux.org/
[CII]: https://www.coreinfrastructure.org/
[HL]: https://www.hyperledger.org/
[video1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V010000_DTH.mp4
[video2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005800_DTH.mp4
[video3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006200_DTH.mp4
[video4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007400_DTH.mp4